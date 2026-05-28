# Burp Suite

> [!abstract] In una riga **Intercepting proxy** che si mette in mezzo tra browser e applicazione web: è l'**hub** del web application penetration testing. Tutto passa di lì, e da lì lo modifichi, lo rilanci, lo analizzi.

## Come funziona

Burp è un **proxy man-in-the-middle**: il browser non parla direttamente col server, ma manda tutto a Burp (di default `127.0.0.1:8080`), che intercetta ogni messaggio **al livello HTTP** prima di inoltrarlo. Vede e modifica **HTTP, HTTPS e WebSocket**.

> [!warning] HTTPS e certificato CA Per leggere il traffico cifrato, il browser deve fidarsi del **certificato CA di Burp** (`http://burp` → scarica `cacert.der` → installalo). In alternativa, e oggi è la via più semplice, usi il **browser Chromium integrato** in Burp, che è già pre-configurato con proxy e certificato.

![[burp-proxy-flow.svg|601]] 
_Il traffico del browser passa attraverso Burp prima di raggiungere il server: è lì che lo intercetti, lo leggi e lo modifichi._

## Edizioni

|Edizione|Costo|Per chi / cosa|
|---|---|---|
|**Community**|Gratis|Studio e testing manuale. Proxy, Repeater, Decoder, Sequencer, Comparer + Intruder _demo_ (rallentato)|
|**Professional**|~450 $/anno|Pentest reali. Aggiunge **Scanner** automatico, **Intruder a piena velocità**, **Collaborator**, project file e gestione|
|**Enterprise / DAST**|Enterprise|Scanner automatico in **CI/CD** (Docker, Jenkins, GitHub Actions…), a scala aziendale|

> [!tip] Per studiare basta la Community Proxy e Repeater — dove avviene la maggior parte del testing manuale — sono **completi** anche nella versione gratuita. La Pro serve davvero solo quando ti serve lo scanner automatico o l'Intruder veloce.

## I moduli principali

### Proxy

Il cuore di Burp. Intercetta le richieste (puoi metterle in pausa, modificarle, droparle) e tiene la **HTTP history**: lo storico di tutto il traffico, da cui mandi le richieste agli altri moduli.

### Target

La **site map** dell'applicazione (struttura di URL e risorse scoperte) e soprattutto lo **scope**: definisci cosa è "in scope" per non testare per errore domini di terzi.

### Repeater

Prendi una singola richiesta, la **modifichi a mano e la rilanci** quante volte vuoi, osservando la risposta. È lo strumento del testing manuale: provare payload, manomettere parametri, analizzare flussi di autenticazione.

### Intruder

Automatizza l'invio di una richiesta variando uno o più punti (`§marcati§`) con liste di payload. Quattro **modalità d'attacco**:

|Modalità|Set di payload|Comportamento|Uso tipico|
|---|---|---|---|
|**Sniper**|1|Un punto alla volta|Fuzzing di un singolo parametro|
|**Battering Ram**|1|Stesso payload in **tutti** i punti insieme|Stesso valore ripetuto|
|**Pitchfork**|N (paralleli)|1°-con-1°, 2°-con-2°…|Coppie note user/password|
|**Cluster Bomb**|N (combinati)|**Tutte** le combinazioni|Brute force user × password|

![[burp-intruder-modes.svg|637]] 
_Le quattro modalità a confronto: come i payload riempiono i punti marcati e quante richieste ne risultano. Nota come Cluster Bomb esploda (a × b) rispetto a Pitchfork (a coppie)._

### Scanner _(Pro)_

Crawler + scanner automatico delle vulnerabilità: invia richieste costruite e analizza le risposte per trovare SQLi, [[XSS]], ecc. Si lancia dalla **Dashboard**. _(Nelle versioni vecchie la fase di crawling si chiamava "Spider": oggi è integrata qui.)_

### Sequencer

Analizza la **qualità della casualità** dei token di sessione (o altri valori che dovrebbero essere imprevedibili). Token deboli = sessioni indovinabili.

### Decoder

Codifica/decodifica al volo: **URL, HTML, Base64, ASCII Hex, Hex, Gzip**. Ha lo **Smart Decode** che riconosce e srotola più livelli di codifica — utilissimo contro i trucchi di [[Canonicalization]].

### Comparer

Fa il **diff visivo** tra due risposte, per cogliere differenze sottili (es. comportamento diverso tra login valido e non valido → user enumeration).

### Logger

Registra e analizza tutto il traffico HTTP generato da Burp in un'unica vista.

### Extensions (ex _Extender_) — BApp Store

Sistema di estensioni: oltre **500** plugin nel **BApp Store**, più estensioni custom scritte in **Java o Python**. È ciò che rende Burp espandibile (manipolazione JWT, test di access control, autorizzazione, ecc.).

### Collaborator _(Pro)_

Server esterno di Burp per scoprire vulnerabilità **out-of-band**: quando il server bersaglio "richiama a casa" (DNS/HTTP) lo intercetti — fondamentale per SSRF, SQLi blind out-of-band, ecc.

## Workflow tipico

1. **Configura** proxy + scope (o apri il browser integrato).
2. **Naviga** l'app: tutto finisce nella HTTP history del Proxy.
3. **Mappa** la superficie nel Target.
4. **Indaga a mano** con il Repeater sulle richieste interessanti.
5. **Automatizza** con l'Intruder (fuzzing, brute force).
6. **Verifica** randomness (Sequencer), decodifica (Decoder), confronta (Comparer).
7. _(Pro)_ lancia lo **Scanner** dalla Dashboard per la copertura automatica.

## Limiti della Community (cosa ti manca senza licenza)

- **Niente Scanner** automatico.
- **Intruder rallentato** (throttling artificiale → inutile per attacchi grossi).
- **Niente crawler** automatico né salvataggio dei **project file**.
- Niente **Collaborator**.

> [!note] Alternativa gratuita Se ti servono scanner e funzioni avanzate senza pagare, **OWASP ZAP** ([[Web Hacking Tools]]) le offre open source. Burp resta lo standard di settore, ZAP è il "fratello free".

## Collegamenti

- ⬆️ [[Web Hacking Tools]] · [[Web Application Hacking]]
- ↔️ [[SQL Injection]] · [[XSS]] · [[Canonicalization]] (Decoder/Smart Decode)