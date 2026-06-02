## titolo: "Meterpreter" corso: Ethical Hacking Lab (Sapienza) tipo: nota di ripasso tags: [ethical-hacking, lab, metasploit, meterpreter, post-exploitation, payload, esame] collegata-a: "[[ETHL 0x01 — Vulnerabilities]]"

# Meterpreter

> [!abstract] In una riga **Meterpreter** è il **payload di post-exploitation** avanzato di Metasploit: una shell potente che gira **interamente in memoria** (fileless), comunica su un canale **cifrato** e si estende con moduli caricati a runtime. Lo ottieni _dopo_ un exploit riuscito, e ti serve per fare privesc, [[Pivoting]] e raccolta dati.

> [!info] Dove si colloca nel workflow
> 
> ```
> exploit riuscito → session → (sessions -u <n>) → Meterpreter → post-exploitation
> ```
> 
> Spesso un exploit ti dà prima una **shell di sistema grezza**; con `sessions -u <n>` la **promuovi a Meterpreter** per avere tutte le funzioni qui sotto.

---

## 1. Cos'è davvero (i dettagli che fanno punteggio)

- **Payload, non un exploit.** L'exploit apre la breccia; Meterpreter è _ciò che gira dopo_ dentro il processo compromesso.
- **In-memory / fileless.** Vive nella RAM del processo bersaglio, **non scrive un eseguibile su disco** → evade gli antivirus basati su **firme di file** e lo scanning del filesystem.
- **Estensibile a runtime.** Carica moduli/estensioni **in memoria** quando servono (via reflective/in-memory DLL injection), senza toccare il disco.
- **Canale cifrato.** Comunica con l'attaccante su un canale **TLS**, con un protocollo a messaggi **TLV (Type-Length-Value)** → il traffico non è in chiaro.
- **Un processo "ospite".** Inizialmente vive nel processo bucato (che potrebbe chiudersi o essere instabile) → da qui l'importanza della **migration** (sotto).

---

## 2. Funzionalità chiave (le 6 della slide + perché)

|Funzionalità|Cosa fa|Perché conta|
|---|---|---|
|**Fileless Execution**|Gira tutto in memoria|Riduce la **detection** (niente file da firmare per l'AV)|
|**Command Execution**|Shell ricca di **comandi integrati**|Operi sul sistema senza tool esterni|
|**Privilege Escalation**|Aiuta a scalare i permessi|Da utente normale → SYSTEM/root|
|**Session Migration**|Si **sposta in un processo più stabile**|Sopravvive alla chiusura del processo bucato + si nasconde meglio|
|**Screenshots & Keylogging**|Cattura schermo e tasti|Raccolta di **dati sensibili** (credenziali)|
|**Pivoting**|Usa la macchina compromessa per **attaccarne altre**|Raggiunge segmenti di rete interni altrimenti irraggiungibili|

> [!tip] La migration in due righe Il processo iniziale (es. un servizio che hai sfruttato) può crashare o essere chiuso. `migrate <pid>` inietta Meterpreter in un altro processo (più longevo, più "innocuo" tipo `explorer.exe`): **persistenza della sessione** + **occultamento**.

---

## 3. Comandi più comuni (per capire, non da memorizzare a pappagallo)

|Categoria|Comandi|Note|
|---|---|---|
|**Sistema/info**|`sysinfo`, `getuid`, `getpid`, `ps`|Chi sono, dove sono, quali processi girano|
|**Privesc**|`getsystem`, `getprivs`|Tenta l'escalation a SYSTEM (Windows)|
|**Credenziali**|`hashdump`|Estrae gli hash delle password (poi cracking offline)|
|**Filesystem**|`ls`, `cd`, `cat`, `download`, `upload`|Esfiltrazione / caricamento file|
|**Processi**|`migrate <pid>`, `execute`, `kill`|Migrazione e gestione processi|
|**Rete / pivoting**|`ipconfig`, `route`, `portfwd`, `autoroute`|Mappa la rete interna e instrada il traffico attraverso il target|
|**Cattura**|`screenshot`, `keyscan_start` / `keyscan_dump`, `webcam_snap`|Raccolta dati|
|**Sessione**|`shell` (passa a shell di sistema), `background`, `clearev`, `exit`|`clearev` pulisce i log eventi|

---

## 4. Gestione delle sessioni (dal lab)

Una volta consegnato l'exploit, ottieni una **session**:

|Azione|Comando|
|---|---|
|Mandare in background la sessione corrente|`Ctrl+Z` (`^z`)|
|Elencare le sessioni attive|`sessions`|
|Passare alla sessione `<n>`|`sessions <n>`|
|**Promuovere** la sessione `<n>` a Meterpreter|`sessions -u <n>`|

---

## 5. Tipi di payload — Staged vs Stageless

> [!warning] Trappola d'esame Sapere la differenza **e** saperla leggere dal nome del payload.

|Tipo|Esempio|Come funziona|Pro / Contro|
|---|---|---|---|
|**Staged**|`php/meterpreter/reverse_tcp`|**Due fasi**: lo _stage 1_ (piccolo) richiama l'attaccante e **scarica** lo _stage 2_ (Meterpreter completo)|+ footprint iniziale minimo (utile quando lo spazio dell'exploit è limitato, es. buffer overflow) <br> − richiede il round-trip di rete e un handler che serva lo stage 2|
|**Stageless**|`python/meterpreter_reverse_tcp`|**Una fase**: l'intero payload è consegnato in una volta|+ più **autonomo e affidabile** su connessioni instabili <br> − più **grande**, più facile da firmare staticamente|

> [!tip] Regola di lettura del nome **`/`** (slash) ⟶ **staged** → `meterpreter/reverse_tcp` **`_`** (underscore) ⟶ **stageless** → `meterpreter_reverse_tcp`

### reverse vs bind (dimensione ortogonale)

- **`reverse_tcp`**: è **il target** che si connette **verso l'attaccante** → attraversa NAT e firewall in **uscita** (di solito permessi). È la scelta tipica.
- **`bind_tcp`**: l'attaccante si connette a un **listener aperto sul target** → spesso bloccato dai firewall in **ingresso**.

---

## 6. msfvenom (da dove esce un payload Meterpreter)

- Genera payload (reverse/bind shell, Meterpreter), supporta **staged e stageless**.
- **Encoding** per evadere gli antivirus; output in vari formati (**EXE, ELF, APK, PSH, …**).
- Ai fini d'esame conta capire **cosa produce** e le **scelte** (staged/stageless, reverse/bind, formato), non la stringa esatta.

---

## 7. Lato difensivo (blue team) — utile per il "perché ha funzionato o meno"

> [!note] Come si rileva/contrasta Meterpreter
> 
> - **Rete:** traffico **TLS anomalo in uscita**, pattern di **beaconing** verso un C2, firme di protocollo note (IDS/IPS).
> - **Host/EDR:** rilevamento di **iniezione in memoria** e **reflective DLL loading**, **process migration** sospetta, comportamenti anomali → l'AV "classico" basato su file **non basta**, proprio perché è fileless.
> - **Memory forensics** e detection **comportamentale** (non a firma).
> - **Segmentazione di rete** per limitare il **pivoting**; egress filtering per ostacolare le reverse shell.

---

## 8. Checklist "domande probabili"

- [ ] Cos'è Meterpreter e **perché in-memory/fileless** è importante.
- [ ] Le sue **funzionalità** principali (migration, pivoting, keylogging…).
- [ ] **Staged vs stageless**: differenza, trade-off, e come leggerlo dal nome (`/` vs `_`).
- [ ] **reverse vs bind** e quale passa meglio i firewall.
- [ ] Comandi per **gestire le sessioni** (`sessions`, `-u`, `^z`).
- [ ] Cos'è la **migration** e a cosa serve.
- [ ] Come un blue team **rileva** Meterpreter nonostante sia fileless.

## 9. Collegamenti

- [[ETHL 0x01 — Vulnerabilities]] (workflow Metasploit completo)
- [[Metasploitable 2]] (target su cui ottenere una sessione)
- [[Hacking Exposed - Cap 6 APT]] (post-exploitation, pivoting, persistenza)