## titolo: "ETHL 0x01 — Vulnerabilities" corso: Ethical Hacking Lab (Sapienza) tipo: nota di ripasso tags: [ethical-hacking, lab, vulnerabilities, cve, cwe, cvss, nmap, metasploit, esame]

# ETHL 0x01 — Vulnerabilities

> [!abstract] In una riga 
> Questo lab insegna a **classificare** le vulnerabilità (CVE / CWE / CVSS), a **cercarle** (Exploit-DB, Vulners…), a **enumerarle** (Nmap + NSE) e a **gestire l'intero workflow** con Metasploit. È quasi tutto concetti + metodologia → terreno perfetto per il richiamo attivo.

> [!tip] Sovrapposizione con la teoria Nmap, banner grabbing ed enumerazione coincidono con il **recon di Hacking Exposed (Cap. 1-3)**. Studi una volta, vale doppio: teoria + lab.

---

## 1. [[CVE]] — Common Vulnerabilities and Exposures

**Cos'è:** un _riferimento standardizzato_ di vulnerabilità **note** (già scoperte).

- Utile sia al **red team** (cosa posso sfruttare) sia al **blue team** (cosa devo patchare).
- Ogni vulnerabilità riceve un **identificatore univoco**.
    - A volte pubblicato _senza dettagli_ → si lascia tempo al vendor di rilasciare la patch ⇒ **responsible disclosure**.
- **Formato:** `CVE-YYYY-NNNN` (anno + numero progressivo).
- **Esempio:** `CVE-2021-44228` = **Log4Shell** (Log4j), uno dei CVE più dolorosi degli ultimi anni — esecuzione di codice arbitrario via JNDI/LDAP nei messaggi di log.

### Chi assegna i CVE (submission a NVD)

|Via|Chi|Caratteristiche|
|---|---|---|
|**CNA** (CVE Numbering Authority)|Organizzazioni autorizzate ad assegnare ID **direttamente**|Portale sicuro, pubblicazione **più veloce**, più controllo sul record|
|**Non-CNA**|Ricercatori indipendenti|Via candidato esterno (CERT/CC, FIRST) o first-hand → **lento e macchinoso**|

> [!quote] Punto chiave **CVE = una vulnerabilità specifica, in un prodotto specifico.** (vedi sotto il contrasto con CWE)

---

## 2. CVSS — Common Vulnerability Scoring System

A ogni [[CVE]] si assegna un punteggio di **severità** nell'intervallo **[0.0, 10.0]**. Versione più usata: **v3.1**. Il punteggio è codificato in un **vettore** su tre gruppi di metriche:

|Gruppo|N° attributi|A cosa serve|
|---|---|---|
|**Base**|8|Caratteristiche **intrinseche e immutabili** della vuln (comune)|
|**Temporal**|3|Variano nel tempo (maturità dell'exploit, livello di rimedio, affidabilità del report)|
|**Environmental**|11|**Personalizza** il punteggio sul tuo specifico ambiente|

### Le 8 metriche Base (e come leggere un vettore)

Vettore esempio (Log4j): `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H` → **10.0 (Critical)**

![[Pasted image 20260601123852.png]]

|Sigla|Metrica|Valori|Lettura rapida|
|---|---|---|---|
|**AV**|Attack Vector|**N**etwork / **A**djacent / **L**ocal / **P**hysical|Da quanto lontano colpisci. `N` = via rete = peggiore|
|**AC**|Attack Complexity|**L**ow / **H**igh|Quanto è facile riuscirci|
|**PR**|Privileges Required|**N**one / **L**ow / **H**igh|`N` = nessun privilegio richiesto = peggiore|
|**UI**|User Interaction|**N**one / **R**equired|`N` = non serve che la vittima clicchi|
|**S**|Scope|**U**nchanged / **C**hanged|`C` = l'impatto esce dal componente vulnerabile|
|**C / I / A**|Confidentiality / Integrity / Availability|**N** / **L** / **H**|Impatto sulla triade CIA|

> [!example] Perché `AV:N` + `PR:N` fa paura Significa "sfruttabile **da remoto**, **senza alcun privilegio**" e (se anche `UI:N`) **senza interazione utente**. È il profilo del worm/exploit di massa: chiunque, da Internet, senza credenziali. Log4j era esattamente così → 10.0.

> [!warning] Trappola d'esame: lo score **NON è il rischio** Il prof ci batte sopra. $$Risk = f(impact,\ likelihood)$$ Il **CVSS modella solo l'impatto sulla _sicurezza_**. **Ignora**:
> 
> - **Compliance** (sanzioni, obblighi normativi)
> - **Reputazione**
> - il **contesto di business** e la **likelihood reale** di sfruttamento (quella la cattura il **KEV**, vedi sotto) Quindi un CVSS 9.8 su un sistema isolato e non esposto può essere meno _rischioso_ di un 6.0 su un server pubblico critico.

🔗 _CVSS v3.1 Calculator_ (link nelle slide) per esercitarti a comporre/leggere vettori.

---

## 3. [[CWE]] — Common Weakness Enumeration

**Cos'è:** lista community-driven dei **tipi** di debolezza software **e hardware**.

- Fornisce un **linguaggio comune** per descrivere _categorie_ di debolezze.
- **Esempio:** `CWE-416: Use After Free` — uso di memoria già liberata → da corruzione dati fino a esecuzione di codice arbitrario.

> [!quote] CVE vs CWE — la differenza che chiedono all'esame
> 
> - **CWE** = **tipo / categoria** di debolezza ("Use After Free", "SQL Injection", "Buffer Overflow"). È astratto.
> - **CVE** = **istanza concreta** di una debolezza in un **prodotto e versione specifici** (`CVE-2021-44228` in Log4j). Mnemonica: _CWE è la **classe**, CVE è l'**oggetto** di quella classe._ Un CVE "appartiene a" uno (o più) CWE.

### KEV — Known Exploited Vulnerabilities

- Pubblicato dalla **CISA** (US Cybersecurity and Infrastructure Security Agency).
- Elenca vuln **sfruttate attivamente in the wild** → segnale di _likelihood_ reale (ciò che manca al CVSS).

**Classifiche utili (annuali):**

- **CWE Top 25 Most Dangerous Software Weaknesses** → basata sui CVE rilasciati.
- **CWE Top 10 KEV Weaknesses** → basata su KEV + CVE. Qui lo _score_ È una misura di rischio (frequenza × severità media dei CVE).
    - _Insight della slide:_ in cima dominano **memory safety** (CWE-787 Out-of-bounds Write, CWE-416 Use After Free, CWE-122 Heap Overflow), input validation (CWE-20), injection/OS command (CWE-78), access control (SSRF CWE-918, Path Traversal CWE-22).
![[Pasted image 20260601123922.png]]

---

## 4. Cercare vulnerabilità

Dal punto di vista dell'attaccante: trovare vuln per **un sistema specifico** (che prima vai a identificare con l'enumerazione).

|Risorsa|Note|
|---|---|
|**Exploit-DB**|Motore di ricerca di riferimento, ha la **CLI** (`searchsploit`)|
|**Vulners**|Usato da `nmap --script vulners`|
|**GitHub**|Advisories — spesso il materiale migliore/più aggiornato|
|**Sploitus**|Aggregatore di exploit/PoC|

### Tipi di vulnerability scanner (automatici)

|Tipo|Come funziona|Accuratezza|
|---|---|---|
|**Network-based**|Da fuori: **banner grabbing** (deduce dalla versione) _oppure_ **active exploitation** (prova davvero)|Banner = **meno accurato**; active = **alta confidenza**|
|**Authenticated / Agent-based**|**Fa login** (es. SSH) e scansiona filesystem, memoria, pacchetti installati|Alta (vede dall'interno)|
|**Dependency scanner**|Raccoglie l'**SBOM** (Software Bill Of Materials) e fa matching con i DB di vuln|Ottima per la supply chain|

> [!note] Filosofia del corso 
> L'obiettivo è **saper ricercare** vulnerabilità, **non** usare exploit "pre-confezionati" alla cieca. Ma devi saper **usare** i tool e **capirli fin nel dettaglio** (= saper spiegare _perché_ un attacco funziona). È esattamente ciò che valuta l'esame.

---

## 5. Enumeration con NMAP

Nmap = enumerazione potente: scopre **servizi, versioni, protocolli e configurazioni**, costruendo la mappa della rete.
### Flag chiave

- **`--reason`** → mostra **perché** una porta è in un certo stato (es. `syn-ack` ⇒ open, `conn-refused` ⇒ closed). Da usare _mentre si impara_.![[Pasted image 20260601125048.png]]
- **`-sV`** → **version detection** + banner grabbing (es. `OpenSSH 9.4p1 Debian`, con CPE).![[Pasted image 20260601125117.png]]

### NSE — Nmap Scripting Engine

Script in **Lua** (al momento ~604 predefiniti, alcuni accettano argomenti). **Categorie:**

|Categoria|Cosa fa|
|---|---|
|**safe**|Non danneggia il target|
|**intrusive**|Può impattarlo (anche **crasharlo**)|
|**vuln**|Cerca vulnerabilità|
|**exploit**|Tenta di sfruttarle|
|**auth**|Bypass autenticazione (es. login FTP anonimo)|
|**brute**|Brute-force credenziali|
|**discovery**|Interroga per scoprire info|

**Esempi di script:** `vulners` (CVE+exploit dai banner), `http-php-version` (versione PHP anche se nascosta), `smb-*` (enum/brute SMB).

![[Pasted image 20260601125221.png]]

### [[Metasploitable 2]] — domande pratiche (stile esame)

> [!question] C'è un firewall? Spiega. Lo deduci dagli **stati/ragioni** delle porte (`--reason`). 
> Su Metasploitable 2 le porte chiuse rispondono con **`conn-refused` (RST)** → niente firewall che fa _drop_ silenzioso. Se invece molte porte risultassero **`filtered`** (nessuna risposta), sarebbe il sintomo di un **firewall che scarta i pacchetti**. → _Risposta: no, perché vediamo RST e non drop._

> [!question] `nmap -sU -sV -p1-53 <target>` — c'è un servizio? 
> Scan **UDP**. L'UDP è _connectionless_: il "nessuna risposta" è ambiguo → Nmap marca **`open|filtered`**. Deduce **closed** solo se riceve un **ICMP port-unreachable**. Quindi "come fa Nmap a sapere che non c'è servizio?" → tramite l'**ICMP unreachable**; in assenza di esso resta nel dubbio open|filtered. Servizi trovati: **21/udp, 53/udp**.

> [!question] Porta `2121/tcp`? 
> **ProFTPD** (FTP secondario su Metasploitable). Esistono exploit noti per certe versioni → ricerca su Exploit-DB / `search` in Metasploit.

> [!question] Due modi "diretti" per fare root su Metasploitable 2 
> Senza loggarti come `msfadmin`, i vettori classici sono **servizi con backdoor / versioni vulnerabili note**, ad esempio:
> 
> 1. **vsftpd 2.3.4** (porta 21) → versione con backdoor famigerata.
> 2. **UnrealIRCd 3.2.8.1** (porta 6667) → backdoor nella tarball. _(altri: Samba `usermap_script`, distccd, ecc.)_. Il punto d'esame è il **ragionamento**: enumero versione → cerco CVE/exploit noto → spiego perché funziona.

🔗 _Pratica:_ TryHackMe room `furthernmap` (gratuita).

---

## 6. [[Metasploit]] — il workflow completo

Framework open-source di pentesting. Offre: **Exploits, Payloads, Auxiliary modules, Encoders, Evasion techniques**.

### Pipeline da ricordare (è la spina dorsale di una possibile domanda)

```
DB → workspace → db_nmap (discovery+enum) → hosts/services/vulns → search → exploit → sessions → meterpreter
```

|Fase|Comandi|
|---|---|
|**Database**|`sudo msfdb reinit` · `msfconsole` · `db_status`|
|**Workspace** (isola gli engagement)|`workspace` (quale uso) · `workspace -a nome` (crea) · `workspace nome` (switch)|
|**Discovery**|`db_nmap -sn <rete>` (host discovery)|
|**Enum + vuln mapping**|`db_nmap --script=vulners -O -sV <box>`|
|**Analisi risultati**|`hosts` · `services` · `vulns`|
|**Exploit**|`search vsftpd 2.3.4` · `search UnrealIRCd` · `search vnc`|
|**Sessioni**|`Ctrl+Z` (background) · `sessions` (lista) · `sessions <n>` (switch) · `sessions -u <n>` (upgrade a Meterpreter)|

### [[Meterpreter]]

Payload avanzato **in-memory**. Caratteristiche:

- **Fileless** → gira in RAM, riduce la detection.
- **Command execution** → shell ricca di comandi integrati.
- **Privilege escalation** assistita.
- **Session migration** → si sposta su processi più stabili per non farsi notare.
- **Screenshot & keylogging**.
- **Pivoting** → usa la macchina compromessa per attaccarne altre nella rete.

### Tipi di payload (trappola d'esame)

|Tipo|Esempio|Come funziona|Trade-off|
|---|---|---|---|
|**Staged**|`php/meterpreter/reverse_tcp`|2 fasi: stage 1 (piccolo) richiama l'attaccante e **scarica** lo stage 2 (Meterpreter completo)|Footprint iniziale minimo, ma richiede il round-trip di rete|
|**Stageless**|`python/meterpreter_reverse_tcp`|Fase unica: **tutto il payload** consegnato in una volta|Più grande, ma più **autonomo e affidabile**|

> Nota di lettura: la **`/`** (es. `meterpreter/reverse_tcp`) indica staged; il **`_`** (es. `meterpreter_reverse_tcp`) indica stageless.

### msfvenom (generatore di payload — livello concettuale)

- Crea payload: reverse shell, bind shell, Meterpreter.
- Supporta staged e stageless; **encoding** per evadere gli antivirus; output in vari formati (**EXE, ELF, APK, PSH…**).
- _Le slide mostrano esempi di sintassi_ (es. un bind shell PHP su una porta, un reverse SSL Python con `LHOST`/`LPORT`) — l'importante per l'esame è capire **cosa fa il tool e la differenza bind vs reverse / staged vs stageless**, non memorizzare la stringa.

---

## 7. Checklist "domande probabili"

- [ ] Spiega la **differenza tra CVE e CWE** con un esempio di ciascuno.
- [ ] Cos'è il **CVSS**, i suoi 3 gruppi di metriche, e **perché non è un punteggio di rischio**.
- [ ] **Leggi un vettore CVSS** (cosa dicono AV, PR, UI, Scope).
- [ ] Cos'è il **KEV** e perché aggiunge ciò che manca al CVSS.
- [ ] **Tipi di vulnerability scanner** e differenza di accuratezza (banner vs active vs authenticated).
- [ ] **NSE**: a cosa serve e le sue categorie (safe/intrusive/vuln/exploit/auth/brute/discovery).
- [ ] **Scan UDP**: perché è ambiguo (`open|filtered`) e come Nmap deduce "closed".
- [ ] Come capisci se c'è un **firewall** dagli stati delle porte (`--reason`).
- [ ] **Workflow Metasploit** end-to-end.
- [ ] **Staged vs stageless** payload + cos'è **Meterpreter** (fileless, pivoting, migration).

## 8. Collegamenti

- [[Hacking Exposed - Cap 1-3 Recon]] (enumerazione, banner grabbing, scan TCP/UDP)
- [[Hacking Exposed - Cap 5 UNIX]] (i CWE memory-safety → buffer overflow, use-after-free)
- [[Metasploitable 2]]