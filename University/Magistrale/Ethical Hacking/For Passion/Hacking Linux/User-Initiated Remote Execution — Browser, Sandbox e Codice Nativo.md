---

tags:

- client-side-attacks
- browser-exploit
- xss
- csrf
- social-engineering
- hacking-exposed-7
- privilege-escalation aliases:
- drive-by download
- browser exploit chain
- user-initiated execution

---

# User-Initiated Remote Execution — Browser, Sandbox e Codice Nativo

## 1. Il concetto

L'attaccante non attacca direttamente il server — **fa in modo che sia la vittima ad eseguire il codice**. I vettori principali:

- Aprire un allegato e-mail malevolo
- Navigare su un sito controllato dall'attaccante
- Cliccare un link in un contesto trusted (phishing)

Il punto chiave: l'utente è il vettore involontario. Questo bypassa firewall perimetrali e policy di rete — il traffico è iniziato dall'interno, verso l'esterno, ed è "legittimo" dal punto di vista del firewall.

---

## 2. XSS e CSRF — cosa fanno davvero

> [!warning] Equivoco comune XSS e CSRF eseguono codice **nel browser**, non sul sistema operativo. Sono attacchi all'applicazione web, non al kernel. Non danno una shell.

|Attacco|Dove gira il codice|Cosa ottieni|
|---|---|---|
|**XSS** (Cross-Site Scripting)|JavaScript nel browser della vittima|Furto cookie/sessione, keylog nel browser, azioni come l'utente loggato, redirect|
|**CSRF** (Cross-Site Request Forgery)|Nessun codice — forgi una richiesta HTTP|Azioni non autorizzate su siti dove la vittima è autenticata|
|**Browser exploit / drive-by**|Codice nativo che sfugge la sandbox|Shell sul sistema operativo della vittima|

XSS ti dà **controllo della sessione browser**, non una shell. È un attacco all'identità digitale, non al sistema.

### XSS in breve

La vittima visita una pagina che contiene JavaScript iniettato dall'attaccante (o reflesso dalla stessa applicazione vulnerabile). Il browser lo esegue nel contesto del dominio della pagina — quindi con accesso ai cookie, localStorage, DOM di quel sito.

```
Vittima loggata su banca.com
    ↓ apre link con XSS payload
JS malevolo gira nel contesto di banca.com
    → legge cookie di sessione → invia all'attaccante
    → attaccante si autentica come vittima
```

### CSRF in breve

Non serve JavaScript. Basta una richiesta HTTP che il browser invia automaticamente (con i cookie della vittima allegati).

```html
<!-- Pagina malevola che la vittima visita -->
<img src="https://banca.com/transfer?to=attaccante&amount=1000">
```

Il browser carica l'immagine → invia la richiesta GET a banca.com → con i cookie della sessione attiva → bonifico eseguito.

---

## 3. Il vero salto: dal browser al sistema operativo

Per ottenere **code execution sul sistema operativo** serve una catena diversa — una vulnerabilità nel browser stesso, non nell'applicazione web.

```
Vittima visita reallyevilwebsite.com
        ↓
Browser carica contenuto malevolo (JS, HTML, media, plugin)
        ↓
Bug nel motore JS (V8, SpiderMonkey) o plugin (Flash, Java, ActiveX)
        ↓  [RCE nel processo renderer — ancora sandboxato]
Sandbox escape (secondo stage exploit)
        ↓
Shell sul sistema operativo come il processo del browser
```

Ogni freccia è un exploit distinto. In era moderna (Chrome, Firefox con process isolation) servono **almeno due bug concatenati** per arrivare all'OS.

### Perché era molto più facile nell'era HE7 (2011)

|Tecnologia|Problema|
|---|---|
|**Java applet**|Plugin universale, CVE numerosi, eseguiva codice nativo diretto|
|**Flash / Shockwave**|Stesso problema, installato su quasi tutti i browser|
|**ActiveX (IE)**|Praticamente codice nativo nel browser senza sandbox|
|**Browser sandbox**|Chrome la introduce solo ~2008-2010, Firefox ancora più tardi|

Oggi queste tecnologie sono scomparse. Il browser moderno è molto più difficile da bucare, ma non impossibile — i bounty per "full chain" browser exploit (renderer RCE + sandbox escape) valgono milioni di dollari.

---

## 4. "What if you were root?" — il principio di least privilege

Se il browser gira come root (o SYSTEM su Windows):

```
Browser exploit → sandbox escape → shell come root
```

Non serve privilege escalation locale. L'attaccante ottiene root diretto.

> [!tip] Principio di least privilege Il processo del browser eredita i privilegi dell'utente che lo ha lanciato. Per questo:
> 
> - **Non navigare mai come root** su Linux
> - Su Windows pre-Vista era la norma avere utenti admin di default → ogni drive-by dava SYSTEM
> - Vista introduce UAC proprio per mitigare questo: anche un utente admin non ha token elevato di default

Su Linux questo è raramente un problema per abitudine sysadmin. Su ambienti Windows aziendali mal configurati (utenti con diritti admin locali) è ancora un vettore reale.

---

## 5. Kill chain moderna completa

```
Drive-by (sito malevolo)
    ↓ renderer RCE (bug V8/SpiderMonkey/WebKit)
Shell nel processo renderer (sandboxato)
    ↓ sandbox escape (bug nel broker process / OS)
Shell come utente del browser
    ↓ privilege escalation locale (LPE)
root / SYSTEM
```

Ogni step ha la sua classe di vulnerabilità e il suo mercato di exploit.

---

## 6. Difese lato utente / sysadmin

|Difesa|Cosa mitiga|
|---|---|
|**Browser aggiornato**|Chiude i CVE dei motori JS e del sandbox|
|**Least privilege** (no root/admin)|Limita il danno anche in caso di sandbox escape|
|**Content Security Policy (CSP)**|Mitiga XSS lato server|
|**SameSite cookie attribute**|Mitiga CSRF|
|**NoScript / uBlock**|Riduce la superficie di attacco JS|
|**Sandboxing OS-level** (seccomp, AppArmor)|Limita syscall del processo browser anche dopo sandbox escape|

---

## Takeaways

1. **XSS e CSRF ≠ code execution sul sistema** — agiscono nel browser e sulla sessione web, non sull'OS
2. Per ottenere una shell serve un **browser exploit** (bug nel motore o plugin) + spesso un **sandbox escape** come secondo stage
3. Nell'era HE7 questo era banale grazie a Java/Flash/ActiveX; oggi è molto più costoso (milioni in bounty)
4. Il "what if you were root?" è una lezione di **least privilege** — il browser eredita i tuoi privilegi
5. Il firewall perimetrale non aiuta: il traffico è generato dalla vittima verso l'esterno, quindi è "legittimo"

---

## Wiki-links

- [[xss]]
- [[csrf]]
- [[social_engineering]]
- [[privilege_escalation]]
- [[least_privilege]]
- [[browser_sandbox]]
- [[hacking_exposed_7_unix]]
- [[user_initiated_remote_execution]]