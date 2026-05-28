# Web Application Security Scanners

> [!abstract] In una riga Tool **automatici** che cercano vulnerabilità in un'app web testandola dall'esterno. Oggi rientrano nella sigla **DAST**. La _categoria_ è attualissima; i _nomi_ in HE7 sono datati.

## Cos'è (DAST)

Uno scanner di sicurezza per web app è un tool **DAST** (_Dynamic Application Security Testing_): testa l'**applicazione in esecuzione** dall'esterno, come farebbe un attaccante (black-box), senza vedere il codice sorgente. Si colloca accanto agli altri approcci:

- **DAST** — testa l'app _in funzione_ (dall'esterno). ← questa nota
- **SAST** — analizza il _codice sorgente_ (statico).
- **IAST** — strumenta l'app _dall'interno_ mentre gira.
- **SCA** — controlla le _dipendenze/librerie_ per CVE note.

## Come funziona

1. **Crawl:** mappa l'app seguendo link, form e parametri.
2. **Attack / fuzz:** invia richieste costruite (payload per [[SQL Injection]], [[XSS]], ecc.).
3. **Analyze:** confronta le risposte per dedurre la presenza di vulnerabilità.

## I limiti (il punto da ricordare)

> [!important] Perché lo scanner non basta
> 
> - Genera **falsi positivi** (e falsi negativi): ogni risultato va verificato a mano.
> - **Non trova** le falle di **logica di business**, di [[Authorization|autorizzazione]] (es. IDOR) né i bypass di [[Authentication Attacks|autenticazione]]: richiedono comprensione del contesto, cioè testing **manuale**.
> - Per questo il workflow reale è: **scanner per l'ampiezza + [[Burp Suite]]/manuale per la profondità.** È il motivo dell'"analisi più profonda e pazienza" del livello applicativo.

## Tool: vecchio → nuovo

I due nomi-bandiera di HE7 sono cambiati di mano, ma sono vivissimi (oggi suite complete DAST+SAST+IAST+SCA):

|HE7 (2012)|Oggi (2026)|
|---|---|
|**HP WebInspect**|**OpenText Fortify WebInspect** (HP → Micro Focus → OpenText)|
|**IBM / Rational AppScan**|**HCL AppScan** (acquisito da HCL nel 2019)|
|**Acunetix**|sotto **Invicti Group**|
|**Paros**, **WebScarab**|❌ morti → oggi **OWASP ZAP** (ZAP nasce da Paros)|
|**Cenzic Hailstorm**, **NTOSpider**|❌ assorbiti / estinti|

## Cosa usare oggi

- **OWASP ZAP** — lo scanner DAST open source di riferimento, gratis.
- **Burp Scanner** (in [[Burp Suite]] Professional) — standard de facto, a pagamento; si **affianca** a un DAST enterprise, non lo sostituisce.
- **Enterprise / CI-CD:** OpenText Fortify, HCL AppScan, Invicti/Acunetix, Checkmarx DAST, StackHawk, Veracode.

## Collegamenti

- ⬆️ [[Web Application Hacking]]
- 🛠️ [[Web Hacking Tools]] · [[Burp Suite]]
- ↔️ [[SQL Injection]] · [[XSS]] (ciò che lo scanner cerca) · [[Authorization]] (ciò che NON trova)