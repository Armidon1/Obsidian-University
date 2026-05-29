# Cross-Site Request Forgery (CSRF)

**Tag:** #security #web-security #vulnerability #CSRF #session-management

**Fonte:** [[5 - CS Application Level - Web Security Part II]]

---

## 📝 Definizione

Il **Cross-Site Request Forgery (CSRF)** è un attacco che abusa del meccanismo automatico con cui i browser allegano i cookie alle richieste HTTP. L'attaccante costringe il browser della vittima a eseguire azioni indesiderate su un'applicazione web in cui l'utente è attualmente autenticato.

- **Concetto chiave:** Il sito vulnerabile non riesce a distinguere se una richiesta è stata avviata intenzionalmente dall'utente o se è stata innescata da una pagina malevola di terze parti.
    
- **Prerequisito:** La vittima deve avere una sessione attiva (essere loggata) sul sito target.
    

---

## ⚙️ Meccanismo di Attacco

L'attacco segue generalmente questo flusso:

1. **Preparazione:** L'attaccante predispone una pagina web o un link malevolo che contiene una richiesta verso il sito target (es. `bank.com/transfer`).
    
2. **Esecuzione:** La vittima visita il sito dell'attaccante.
    
3. **Trigger:** La pagina malevola invia automaticamente la richiesta al sito target (es. tramite un form nascosto inviato via JavaScript per richieste POST, o caricando un'immagine per richieste GET).
    
4. **Autenticazione Automatica:** Il browser della vittima allega automaticamente i cookie di sessione validi alla richiesta verso il dominio target.
    
5. **Azione:** Il server riceve la richiesta, verifica i cookie (che sono validi) e la esegue (es. effettua il bonifico o cambia la password), credendo sia legittima.
    

---

## 🛡️ Prevenzione e Mitigazione

### 1. Anti-CSRF Tokens

La difesa più robusta consiste nell'utilizzare token segreti e imprevedibili che il browser non include automaticamente.

- **Synchronizer Token Pattern:** Il server genera una stringa casuale (token) e la inserisce come campo nascosto (`<input type="hidden">`) in tutti i form HTML. Al momento della sottomissione, il server verifica che il token sia presente e corretto.
    
- **Cookie-to-header:** Un token viene impostato in un cookie; il client (JavaScript) legge questo cookie e lo inserisce in un header HTTP personalizzato. Il server verifica la corrispondenza.
    

### 2. SameSite Cookie Attribute

Un attributo dei cookie che controlla se questi devono essere inviati nelle richieste cross-site.

- **Lax (Default moderni):** Il cookie viene inviato solo se la navigazione avviene nel "top-level" (l'utente cambia URL nella barra degli indirizzi), proteggendo da molti attacchi CSRF automatici ma non da tutti.
    
- **Strict:** Il cookie non viene mai inviato in richieste cross-site.
    
- **Nota:** Non protegge contro attaccanti che controllano un sottodominio ("related-domain attackers").
    

### 3. Referer Validation

L'applicazione verifica l'header HTTP `Referer` per assicurarsi che la richiesta provenga da una pagina consentita (dello stesso dominio).

- **Limiti:** L'header può essere soppresso per motivi di privacy o manipolato in certi contesti; la validazione può essere troppo permissiva ("Lenient") o rompere funzionalità legittime ("Strict").
    

### 4. Fetch Metadata

Utilizzo di nuovi header HTTP (`Sec-Fetch-Site`, `Sec-Fetch-Mode`, ecc.) che informano il server sul contesto della richiesta (es. se è cross-site o same-origin). Il server può usare queste informazioni per scartare richieste sospette (es. un bonifico bancario non dovrebbe essere innescato da un tag `<img>`).

# Web Security: CSRF & Defenses

**Tags:** #ingegneria #sicurezza_informatica #web_security #CSRF #token #Fetch_Metadata

## 1. Cross Site Request Forgery (CSRF)

L'attacco **[[CSRF]]** (Cross Site Request Forgery) sfrutta l'inclusione automatica dei cookie alle richieste effettuate dai browser per eseguire azioni arbitrarie all'interno della sessione stabilita dalla vittima con il sito web target.

> [!abstract] Visual Analysis
> 
> **What to look at:** Un utente autenticato su un sito vulnerabile visita un sito malevolo che scatena una richiesta automatica (es. cambio email).
> 
> **Meaning:**
> 
> 1. Vittima visita `evil-user.net`.
>     
> 2. Senza interazione, parte una richiesta verso `vulnerable-website.com`.
>     
> 3. L'azione (cambio email) viene eseguita perché il browser ha allegato i cookie di sessione validi.
>     

### Meccanismo dell'attacco

1. **Presupposto:** La vittima è autenticata sul sito web target.
    
2. **Innesco:** La vittima visita il sito web dell'attaccante.
    
3. **Richiesta forgiata:** La pagina dell'attaccante innesca una richiesta verso il sito della vittima:
    
    - Tramite **form** inviati automaticamente via JavaScript (per richieste **POST**).
        
    - Tramite il caricamento di un'**immagine** (per richieste **GET**).
        
4. **Risultato:** Il cookie che identifica la sessione viene **automaticamente allegato** dal browser.
    

---

## 2. Esempio di Attacco CSRF

Le slide mostrano un esempio pratico di attacco contro `bank.com`.

### Scenario 1: Login legittimo (POST)

L'utente Alice effettua il login legittimo.

![[Pasted image 20260131135952.png]]

**Here is the exact implementation shown in the slides:**

```http
POST /login
Host: bank.com
user=alice&pass=mypwd

200 OK
Set-Cookie: session=XYZ; Secure; HttpOnly
```

### Scenario 2: Attacco CSRF tramite GET (Image Tag)

L'attaccante usa un tag `<img>` per scatenare una richiesta GET verso l'endpoint di trasferimento denaro.

![[Pasted image 20260131140040.png]]
![[Pasted image 20260131140051.png]]

**Here is the exact implementation shown in the slides:**

```html
<HTML>
<BODY>
	<IMG src="https://bank.com/?act=attacker&amt=3000">
</BODY>
</HTML>
```

**Flusso HTTP:**

1. Il browser della vittima carica l'immagine.
    
2. Invia una richiesta GET a `bank.com`.
    
3. Include automaticamente `Cookie: session=XYZ`.
    
4. Il server risponde `200 OK` e il trasferimento viene eseguito.
    

**Problema:** `bank.com` non può distinguere le richieste legittime da quelle innescate da un sito di terze parti.

---

## 3. Difese CSRF: Anti-CSRF Tokens

La difesa principale consiste nell'uso di token casuali segreti che l'attaccante non può conoscere.

### Synchronizer token pattern (Forms)

- Una stringa segreta e generata casualmente viene incorporata in tutti i form HTML come campo nascosto (`hidden input field`).
    
- All'invio del form, l'applicazione verifica la presenza e la correttezza del token.
    

**Here is the exact implementation shown in the slides:**

```html
<INPUT type="hidden" value="ak34F9dmAvp">
```

### Cookie-to-header token (JavaScript)

- Un cookie con un token generato casualmente viene impostato alla prima visita.
    
- JavaScript legge il valore del cookie e lo inserisce in un **HTTP header personalizzato**.
    
- Il server verifica che l'header sia presente e che il suo valore corrisponda a quello del cookie.
    

**Here is the exact implementation shown in the slides:**

```http
Set-Cookie: _Host-CSRF_token=aen4GjH9b3s; Path=/; Secure
```

### Progettazione dei Token CSRF

- **Generazione:**
    
    - _Refreshed at every page load:_ Limita il tempo in cui un token trapelato (es. via XSS) è valido.
        
    - _Generated once on session setup:_ Migliora l'usabilità (es. navigazione su più tab) ma è meno sicuro del precedente.
        
- **Vincolo:** I token devono essere legati a una **specifica sessione utente** per impedire che un attaccante usi un token valido ottenuto dal proprio account.
    

> [!abstract] Nota
> 
> La maggior parte dei moderni framework web utilizza token anti-CSRF per impostazione predefinita.

### non ho capito come viene implementato questo token causale e come fa il server a verificare che il token è valido se lo genera il client

Hai centrato il dubbio chiave, ed è esattamente l'inceppamento che hanno tutti la prima volta. La risposta è breve e cambia tutto:

> **Il token non lo genera il client. Lo genera il _server_.** Il client si limita a **restituirlo** così com'è. Il server lo confronta con quello che si era segnato in precedenza.

Una volta capito questo, le due implementazioni filano da sole. Te le smonto passo per passo.

#### Synchronizer Token Pattern (con il form)

Lo scenario: vuoi cambiare la password sul sito `banca.com`.

1. **Richiesta del form:** il tuo browser chiede a `banca.com/cambia-password`.
2. **Il server genera il token:** sul server viene generata una stringa casuale, es. `ak34F9dmAvp`.
3. **Il server se la _segna_**: la salva nella tua sessione lato server (in memoria, associata a te).
4. **Il server te la _manda_** incorporata nell'HTML del form:
    
    ```html
    <form method="POST" action="/cambia-password">  
		<input type="hidden" name="csrf_token" value="ak34F9dmAvp">  
		<input type="password" name="nuova">  
	<button type="submit">Cambia</button></form>
    ```
    
5. **Tu invii il form:** il browser rispedisce a `banca.com` la nuova password **e il token nascosto**.
6. **Il server verifica:** confronta il `csrf_token` ricevuto con quello che si era segnato nella tua sessione. Combaciano → ok. Non combaciano (o manca) → richiesta rifiutata.

**Perché blocca il CSRF:** l'attaccante su `evil.com` riesce a far partire la richiesta dal tuo browser (con i cookie, come al solito), ma **non può leggere l'HTML del form legittimo** — la _Same-Origin Policy_ del browser glielo impedisce. Quindi non conosce `ak34F9dmAvp`, non riesce a metterlo nella richiesta, e il server la scarta.

Il punto-chiave: il server genera _e ricorda_. Il client è solo un postino.

#### Cookie-to-header (la versione JS / AJAX)

L'idea è la stessa, ma il "promemoria" del server non sta nella sessione lato server, sta **in un cookie che il server ha già piazzato nel tuo browser**. Si chiama anche _double-submit cookie_.

1. **Prima visita:** il server ti manda
    
    ```http
    Set-Cookie: __Host-CSRF_token=aen4GjH9b3s; Path=/; Secure
    ```
    
    (di nuovo: lo genera il _server_, te lo _consegna_).
2. **Il browser memorizza il cookie.**
3. **Quando fai un'azione** (submit AJAX, chiamata API), il **JavaScript della pagina legittima** legge il valore del cookie e lo aggiunge come **header HTTP personalizzato**, es. `X-CSRF-Token: aen4GjH9b3s`.
4. **La richiesta arriva al server** con **due pezzi**: il cookie (allegato in automatico dal browser) e l'header (messo dal JS della pagina).
5. **Il server confronta i due valori.** Se l'header c'è e combacia col cookie → ok. Altrimenti → rifiutata.

**Perché blocca il CSRF — e qui c'è la finezza:** l'attaccante può far partire una richiesta cross-site e il browser allega comunque il cookie in automatico (come al solito). Però:

- Non può **leggere il valore** del cookie (è di un altro dominio → Same-Origin Policy, rafforzata dal prefisso `__Host-` e dal flag `Secure`).
- Non può **aggiungere l'header custom** `X-CSRF-Token`, perché le richieste cross-origin non possono impostare header arbitrari senza un _preflight CORS_ che il server di `banca.com` rifiuta.

Quindi la richiesta dell'attaccante arriva al server **con il cookie ma senza l'header** (o con un header sbagliato perché non conosce il valore). Il confronto fallisce, la richiesta viene scartata.

#### Riassunto del meccanismo (vale per entrambi)

> [!tip] Il punto in una frase Il server crea un **segreto condiviso** che invia al browser per un canale, e poi pretende di vederlo tornare per un **secondo canale che l'attaccante non può manipolare cross-site** (l'HTML del form, oppure un header HTTP custom).

L'attaccante può sempre "spingere" il browser a fare richieste con i cookie. Ciò che non può fare è **scoprire il token** né **mettercelo dentro nel modo giusto**.

#### E la storia di "ricaricato a ogni pagina" vs "una volta a sessione"?

Solo un compromesso pratico:

- **Generato una volta per sessione** → comodo: navighi con tab multiple, fai più azioni, il token è sempre lo stesso. Se però ti capita uno [[XSS]] che riesce a leggere il token, gliene basta uno solo per fare tutto.
- **Rigenerato a ogni page load** → più sicuro: un token rubato vale solo per pochi secondi, prima del prossimo refresh. Ma rompe usabilità di tab multiple, back/forward, ecc.

E il vincolo finale che il libro nomina (**"i token devono essere legati alla sessione utente"**) chiude un'ultima scappatoia: senza quel binding, un attaccante potrebbe registrarsi sul sito col _suo_ account, ottenere un token valido, e poi infilarlo nelle richieste fatte fare alla vittima. Legandolo alla sessione, il token di Tizio è valido **solo** per le richieste di Tizio.


### Ma non abbiamo detto che esiste già i flag SameSite=Lax per proteggerci dal CSRF?

Hai fatto un'osservazione eccellente. È vero, l'introduzione di `SameSite=Lax` come default ha cambiato radicalmente il panorama della sicurezza web, ma **non ha reso obsoleti i Token Anti-CSRF**.

La risposta breve è: **`SameSite` protegge contro gli attaccanti esterni ("Classic Web Attackers"), ma i Token servono per proteggersi contro gli attaccanti interni ("Related-Domain Attackers") e per la difesa in profondità.**

Ecco il dettaglio basato sulle fonti per chiarire questa distinzione cruciale.

#### 1. Il Ruolo di `SameSite=Lax` (La prima linea di difesa)

Come hai notato correttamente, e come confermano le slide, da Febbraio 2020 i browser moderni impostano di default i cookie su `SameSite=Lax`.

- Questo blocca efficacemente il CSRF classico proveniente da siti esterni (es. `evil.com` che attacca `bank.com`), perché il browser si rifiuta di allegare il cookie nelle richieste "cross-site" generate da immagini, iframe o form automatici.

#### 2. Perché i Token servono ancora? (Il buco nella difesa)

Le slide evidenziano un limite critico dell'attributo `SameSite` che rende necessari i token: **i "Related-Domain Attackers"**.

L'attributo `SameSite` non distingue tra origini diverse se condividono lo stesso **dominio registrabile** (eTLD+1).

- **Lo Scenario:** Immagina che la tua università abbia il dominio `uni.it`.
    - Il portale voti è su `voti.uni.it`.
    - Un portale gestito dagli studenti (o un sottodominio compromesso/vulnerabile a XSS) è su `studenti.uni.it`.
- **Il Fallimento di SameSite:** Se `studenti.uni.it` lancia un attacco CSRF verso `voti.uni.it`, il browser considera questa richiesta come **Same-Site** (stesso "cognome" `uni.it`). Di conseguenza, il cookie `Lax` **viene inviato** e l'attacco ha successo.
- **La Soluzione (Token):** I Token Anti-CSRF (come il _Synchronizer token pattern_) sono specifici per l'applicazione e non dipendono dal dominio DNS. Anche se il cookie passa, il form malevolo inviato da `studenti.uni.it` fallirà perché l'attaccante non conosce il token segreto nascosto nel form HTML di `voti.uni.it`.

#### 3. Conferma sulla tua Flashcard (Token Anti-CSRF)

La tua descrizione dei token è **corretta e perfettamente allineata alle slide**. Ecco un riscontro puntuale sui dettagli che hai scritto:

- **Synchronizer token pattern:** Corretto. Le slide confermano che è una stringa segreta incorporata come `<INPUT type="hidden" ...>` e verificata all'invio.
- **Cookie-to-header token:** Corretto. Le slide mostrano l'implementazione in cui JavaScript legge un cookie e lo copia in un header HTTP personalizzato (es. `X-CSRF-Token`). Questo funziona perché la SOP impedisce a un sito attaccante di leggere il cookie della vittima o di impostare header personalizzati nelle richieste cross-origin semplici.
- **Vincolo alla sessione:** Corretto. È fondamentale che il token sia legato alla sessione dell'utente (cryptographically bound), altrimenti un attaccante potrebbe usare un _proprio_ token valido per forgiare una richiesta valida per la vittima.

#### Sintesi per l'Esame

Non scegliere tra l'uno o l'altro. La sicurezza moderna usa la **Defense in Depth** (difesa in profondità):

1. **`SameSite=Lax`:** Protegge di default contro la maggior parte degli attacchi provenienti da domini esterni.
2. **Anti-CSRF Tokens:** Proteggono contro attacchi provenienti da sottodomini compromessi (related-domain) e offrono una garanzia esplicita che l'intenzione dell'utente fosse legittima.

---

## 4. Referer Validation

Un'altra tecnica difensiva è la validazione dell'header `Referer`.

- I browser allegano automaticamente l'header `Referer` alle richieste in uscita, indicando la pagina di origine.
    
- L'applicazione web ispeziona questo header per verificare se la richiesta proviene da un dominio consentito.
    

**Esempio di richiesta valida:**

```http
POST /login HTTP/2
Host: example.com
Referer: https://example.com/index
user=sempronio&pass=s3cr3tpwd
```

### Caveat (Limiti) della Referer Validation

L'header `Referer` può essere soppresso o mancare per vari motivi:

- Filtrato da firewall aziendali.
    
- Rimosso dalla macchina locale o dal browser (es. transizioni HTTPS -> HTTP).
    
- Preferenze utente.
    

**Tipi di validazione:**

1. **Lenient:** Accetta richieste senza header (rischio vulnerabilità).
    
2. **Strict:** Rifiuta richieste senza header (rischio blocco utenti legittimi).
    

---

## 5. Altre Mitigazioni: SameSite Cookie & Fetch Metadata

### SameSite Cookie Attribute

Offre una mitigazione efficace contro attacchi CSRF classici.

- **Default:** `SameSite = Lax` (protegge dai "classic web attackers").
    
- **Limite:** Nessuna protezione contro attacchi da **related-domain attackers**, poiché le richieste dal dominio dell'attaccante (se sottodominio) sono considerate same-site.
    

### Fetch Metadata

Fornisce al server informazioni sul **contesto** in cui una richiesta è stata generata, permettendo di scartare richieste sospette.

- Supportato attualmente solo dai browser basati su Chromium.
    
- Inviato solo su HTTPS.
    

**Principali Header:**

- `Sec-Fetch-Dest`: Destinazione della richiesta (es. `image`, `script`, `document`).
    
- `Sec-Fetch-Mode`: Modalità della richiesta (es. `Maps`, `cors`).
    
- `Sec-Fetch-Site`: Relazione tra l'origine dell'iniziatore e quella del target (`cross-site`, `same-site`, `same-origin`).
    
- `Sec-Fetch-User`: Inviato se la richiesta è scatenata da un'azione utente.
    

**Policy di Esempio (Resource Isolation):**

$$Sec\text{-}Fetch\text{-}Site == \text{'cross-site'} \land (Sec\text{-}Fetch\text{-}Mode \neq \text{'navigate'/'nested-navigate'} \lor method \notin [GET, HEAD])$$

> [!abstract] Math Analysis
> 
> Questa regola logica dice: Se la richiesta è cross-site E (non è una navigazione OPPURE il metodo non è sicuro come GET/HEAD), allora blocca o isola la risorsa.

---
