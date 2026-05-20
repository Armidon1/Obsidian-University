---

tags:

- browser-exploit
- client-side-attacks
- sandbox-escape
- rce
- 0day
- exploitation aliases:
- browser exploit
- drive-by attack
- browser RCE
- sandbox escape

---

# Browser Attack — Anatomia, Catene di Exploit, Difese

## 1. Perché il browser è un target d'elezione

Il browser è probabilmente **la superficie d'attacco più ricca** su qualsiasi endpoint moderno. Le ragioni sono strutturali:

|Caratteristica|Perché lo rende vulnerabile|
|---|---|
|**Processa input non fidato per definizione**|Ogni pagina visitata è potenzialmente ostile|
|**Codebase enorme**|Chromium ≈ 30M LOC, Firefox ≈ 25M LOC|
|**Performance critical**|JIT compilation, ottimizzazioni aggressive → bug logici|
|**Molte API verso l'OS**|File system, GPU, network, audio, USB, fotocamera|
|**Standard web in continua evoluzione**|WebGL, WebAssembly, WebRTC, WebUSB → nuove primitive nuove vulnerabilità|
|**Sempre in esecuzione**|Tutti lo aprono, sempre, ovunque|

> [!abstract] Analogia Un browser è come un **kernel general-purpose** che esegue programmi non fidati (le pagine web). Solo che il "kernel" gira in user space e deve anche renderizzare grafica 3D, suonare audio, e fare tutto questo a 60fps.

---

## 2. Anatomia di un browser moderno

I browser moderni usano **architettura multi-processo** per isolamento:

```
┌─────────────────────────────────────────────────┐
│  Browser Process (privilegiato, "il broker")    │
│  - Gestisce UI, network, file access            │
│  - Coordina i renderer                          │
└─────────────────────────────────────────────────┘
         │ IPC (Mojo su Chrome, IPDL su Firefox)
         │
┌────────┴────────────────────────┐
│ Renderer 1   Renderer 2   ...   │  ← sandboxati, uno per sito (site isolation)
│ (sito A)     (sito B)           │
│ - Parsing HTML/CSS/JS           │
│ - Layout, paint                 │
│ - JavaScript execution          │
└─────────────────────────────────┘

+ GPU Process (sandboxato, accesso GPU)
+ Network Service (sandboxato, gestisce HTTP/DNS)
+ Plugin Processes (legacy, oggi quasi vuoti)
```

> [!note] Site Isolation Chrome dal 2018 isola **ogni sito** in un proprio processo renderer. Significa che un bug nel parser di un sito non compromette i dati di un altro sito aperto in un'altra tab. Costa molta RAM ma è la difesa più importante contro Spectre e contro cross-origin attacks.

---

## 3. Dove vivono i bug — superfici di attacco principali

### JavaScript Engine

V8 (Chrome/Edge), SpiderMonkey (Firefox), JavaScriptCore (Safari).

- **Type confusion** nel JIT compiler — l'ottimizzatore assume un tipo che poi cambia → memory corruption
- **Bug nei builtins** (Array, Object, RegExp) — funzioni implementate in C++ con assunzioni fragili
- **WebAssembly** — un secondo motore di esecuzione, più nuovo, ancora con bug emergenti

### Parser e renderer

- **HTML parser** — gestire markup malformato è complesso
- **CSS engine** — selettori complessi, layout algorithm
- **SVG / MathML** — formati strutturati con la loro logica di rendering

### Decoder media

Spesso il vettore più produttivo perché sono librerie C/C++ legacy:

- **libwebp** (CVE-2023-4863 — Pegasus 0-click su iMessage via WebP)
- **libpng**, **libjpeg-turbo**, **libavif**
- **Font engines** (FreeType, DirectWrite)

### IPC e broker

- I messaggi tra renderer e browser process — se il broker valida male i parametri, un renderer compromesso può chiedergli di fare cose che non dovrebbe (file open, network request privilegiata, ecc.)

---

## 4. La catena d'attacco completa

```
Vittima visita reallyevilwebsite.com
        │
        ▼
[STEP 1] Initial RCE nel renderer
   ├─ JavaScript exploit (es. type confusion in V8)
   ├─ oppure: media decoder bug (WebP, immagine in <img>)
   └─ oppure: font rendering bug
        │  ottieni esecuzione arbitraria
        │  ma sei dentro la sandbox del renderer
        ▼
[STEP 2] Sandbox escape
   ├─ Bug nel broker process (IPC validation insufficiente)
   ├─ oppure: bug del kernel OS (LPE per uscire dalla sandbox)
   └─ oppure: bug della GPU stack (driver in kernel space)
        │  ora hai shell come l'utente del browser
        ▼
[STEP 3] (opzionale) Privilege escalation
   └─ Per arrivare a root/SYSTEM se non ci sei già
```

> [!warning] Costo economico Una catena completa "no-click" su browser moderno vale **$1M+ sul mercato bounty**. Pwn2Own paga $150k–$500k per chain Chrome/Firefox. NSO Group e simili vendono chain mobile a stati per cifre a 7-8 zeri.

---

## 5. Vettori di delivery

|Vettore|Modalità|Esempio|
|---|---|---|
|**Drive-by**|Vittima visita un sito|Pubblicità malevola (malvertising) su rete legittima|
|**Watering hole**|Compromesso un sito che la target visita abitualmente|Forum di settore, news site|
|**Phishing link**|Link via mail/chat che apre il browser|Spear-phishing mirato|
|**0-click**|Browser/parser viene invocato senza interazione|WebP in iMessage, preview link in Slack|
|**Compromised CDN/library**|Sito legittimo serve JS malevolo|Supply chain attack|

---

## 6. Difese moderne — perché oggi è più difficile

### Process isolation

Renderer in processi separati, comunicazione solo via IPC validata.

### OS-level sandboxing

- **Linux**: seccomp-bpf filtra le syscall del renderer
- **macOS**: App Sandbox, Mandatory Access Control
- **Windows**: AppContainer, restricted tokens
- **Android**: SELinux + isolatedProcess

### V8 Sandbox (Heap Sandbox)

Iniziato 2021 — isola la heap del JIT in una regione di memoria con accesso virtualizzato. Anche con RCE nel renderer non puoi corrompere puntatori arbitrari.

### MiraclePtr (Chrome)

Mitigazione contro use-after-free — uno dei bug più comuni nei browser.

### Site Isolation

Già menzionato — un sito ≠ un processo, niente Spectre-style cross-origin reads.

### Control Flow Integrity (CFI)

A livello compilatore — i salti indiretti possono andare solo verso target legittimi. Rende molte tecniche ROP/JOP impraticabili.

### Update automatico

Chrome e Firefox si aggiornano in background. La finestra di sfruttamento di una vulnerabilità nota è ridotta a ore/giorni.

---

## 7. Esempi storici notevoli

|Anno|Exploit / Chain|Note|
|---|---|---|
|2010|**Aurora** (CVE-2010-0249)|IE6 use-after-free, attacco a Google da APT cinesi|
|2013|**Java applet exploits**|Era d'oro del drive-by, prima della morte di Java nel browser|
|2016|**Pwn2Own Chrome**|Prima full chain Chrome → SYSTEM|
|2019|**iOS Project Zero (Ian Beer)**|0-click via WiFi su iOS, classe magistrale di exploitation|
|2021|**FORCEDENTRY** (NSO)|0-click su iMessage via CoreGraphics PDF parser|
|2023|**libwebp CVE-2023-4863**|0-day in libreria comune, colpiva Chrome, Firefox, Safari, Electron|

---

## 8. Stato dell'arte difensivo — perché ne vale la pena

> [!tip] La buona notizia Bucare un browser moderno **patched** è uno degli attacchi più difficili al mondo. Tra sandbox multi-livello, ASLR/PIE, CFI, V8 Sandbox e site isolation, una catena affidabile richiede 2–4 bug indipendenti, settimane/mesi di ricerca, e spesso scade in pochi mesi per via degli update automatici.

> [!warning] La cattiva notizia Conta solo se l'utente **aggiorna**. Browser non aggiornato + plugin obsoleti (PDF reader integrato, Flash residuo, ecc.) = vettore ancora viabile per attaccanti con poco budget.

---

## 9. Difese pratiche lato utente / sysadmin

1. **Aggiornamento automatico abilitato** — la singola difesa più efficace
2. **Profili separati per attività sensibili** — bancario in un profilo, navigazione generica in un altro
3. **Estensioni minimali** — ogni estensione è codice che gira con privilegi del browser
4. **uBlock Origin** — blocca malvertising, riduce superficie JS
5. **Mai navigare come root/admin**
6. **Sandboxing OS-level aggiuntivo** — su Linux: firejail, bubblewrap; su macOS già attivo di default
7. **DNS filtering** (Pi-hole, NextDNS) — blocca domini malevoli noti prima del DNS resolve

---

## Takeaways

1. Il browser è un **target d'elezione** per superficie d'attacco enorme e ubiquità
2. L'architettura multi-processo + sandbox rende necessaria una **catena di exploit**, non un singolo bug
3. I vettori principali sono: **JIT engine, decoder media, parser HTML/CSS, IPC del broker**
4. Una full chain moderna vale **milioni** sul mercato — non è alla portata di attaccanti generici
5. Per attaccanti generici (criminali, malvertising) il vettore principale è **vittime con browser non aggiornati** o plugin obsoleti
6. La difesa più efficace per l'utente è **aggiornare**, **least privilege**, **estensioni minimali**

---

## Wiki-links

- [[user_initiated_remote_execution]]
- [[xss]]
- [[csrf]]
- [[sandbox_escape]]
- [[privilege_escalation]]
- [[social_engineering]]
- [[malvertising]]
- [[supply_chain_attack]]
- [[zero_day]]