---

tags:

- tools
- password-attack
- hashcat
- offline-attack
- cracking
- gpu
- hacking-exposed-7 aliases:
- hashcat reference
- password cracking
- hash mode

---

# Hashcat — Offline Password Cracking

## 1. Filosofia e ruolo

Hashcat è il **gold standard** del cracking di hash. Non attacca servizi di rete (a differenza di [[hydra]] e [[medusa]]) — opera **offline** su hash che hai già rubato altrove. Genera password candidate, le hasha con l'algoritmo target, le confronta con l'hash da crackare.

> [!abstract] Concetto centrale Hashcat **non rompe** la crittografia. Genera candidati e li prova uno a uno (o miliardi al secondo). La sicurezza di un hash dipende da: complessità della password originale, lentezza dell'algoritmo (bcrypt vs MD5), uso di salt, hardware dell'attaccante.

### Online vs Offline — ricapitolazione

|Attacco|Tool|Limite di velocità|Rilevabile dal target|
|---|---|---|---|
|**Online**|[[hydra]], [[medusa]]|Rete + server|Sì — ogni tentativo è un login fallito|
|**Offline**|**hashcat**, john|Solo la tua GPU|No — non tocchi mai il target|

Su [[htb_sauna]] hai fatto offline puro: rubato l'hash AS-REP, crackato in locale, **zero traffico verso il DC**.

---

## 2. Hashcat vs John the Ripper

|Aspetto|Hashcat|John the Ripper|
|---|---|---|
|**Hardware target**|GPU (massivo parallelismo)|CPU (john) + GPU (john-jumbo)|
|**Velocità su algoritmi veloci** (MD5, NTLM)|Vince nettamente|Più lento|
|**Velocità su algoritmi lenti** (bcrypt, argon2)|Vicini|Vicini|
|**Sintassi**|Flag numerici, esplicita|Auto-detect, più "magica"|
|**Hash format detection**|Manuale (devi sapere `-m`)|Spesso automatica|
|**Estensibilità**|Rules + masks potenti|Rules + incremental mode|
|**Quando preferire**|Hai una GPU decente|Solo CPU, o hash auto-detection comoda|

> [!tip] In pratica Su Kali ci sono entrambi. Hashcat è il default per AD/Kerberos/NTLM. John è comodo per hash misti o quando non ricordi il mode.

---

## 3. I due flag che contano: `-m` e `-a`

```bash
hashcat -m <hash_mode> -a <attack_mode> <hash_file> <wordlist_o_mask>
```

|Flag|Cosa specifica|
|---|---|
|`-m`|**Algoritmo dell'hash** (es. 1000 = NTLM, 18200 = AS-REP)|
|`-a`|**Modalità di attacco** (0 = dictionary, 3 = mask, ecc.)|

Questi due determinano tutto il comportamento. Ogni mode/attack è un numero — non c'è autodetect.

---

## 4. Hash modes — riferimento rapido

Lista completa: `hashcat --help` o https://hashcat.net/wiki/doku.php?id=example_hashes

### Modes più rilevanti per pentest

|Mode|Algoritmo|Contesto|
|---|---|---|
|**0**|MD5|Hash generici, CTF|
|**100**|SHA1|Hash generici|
|**1000**|**NTLM**|Hash Windows locale, dump SAM|
|**1100**|Domain Cached Credentials (DCC)|Cache credenziali domain logon|
|**2100**|**DCC2 / mscash2**|Cache moderne (Win Vista+)|
|**1800**|**sha512crypt**|Linux `/etc/shadow` ($6$)|
|**7400**|sha256crypt|Linux `/etc/shadow` ($5$)|
|**500**|md5crypt|Linux legacy ($1$)|
|**3200**|**bcrypt**|App moderne, lentissimo|
|**5500**|NetNTLMv1|Catturato da Responder (raro)|
|**5600**|**NetNTLMv2**|Catturato da Responder (comune)|
|**13100**|**Kerberos 5 TGS-REP**|**Kerberoasting**|
|**18200**|**Kerberos 5 AS-REP (RC4)**|**AS-REP Roasting** (visto su Sauna)|
|**19900**|Kerberos 5 AS-REP (AES)|AS-REP variante AES|
|**22000**|WPA-PBKDF2-PMKID+EAPOL|WiFi WPA/WPA2|
|**7500**|Kerberos 5 AS-REQ Pre-Auth|Cattura pre-auth|

> [!note] Hash format hint Spesso il **prefisso dell'hash** ti dice quale mode usare:
> 
> |Prefisso|Mode|Algoritmo|
> |---|---|---|
> |`$1$`|500|md5crypt|
> |`$5$`|7400|sha256crypt|
> |`$6$`|1800|sha512crypt|
> |`$2a$ / $2b$ / $2y$`|3200|bcrypt|
> |`$krb5asrep$23$`|18200|AS-REP RC4|
> |`$krb5tgs$23$`|13100|TGS-REP RC4 (Kerberoast)|
> |`$NTLM$` o hash a 32 hex|1000|NTLM|

---

## 5. Identificare un hash sconosciuto — 3 vie

1. **Prefisso** (tabella sopra) — è il modo più veloce quando lo riconosci
2. **Strumenti automatici**:
    
    ```bash
    hashid '$6$abc$def...'nth '$6$abc$def...'   # name-that-hash, più moderno
    ```
    
3. **Output del tool che lo produce** — Impacket con `-format hashcat` ti dà già l'hash nel formato giusto per hashcat
4. **`hashcat --example-hashes | grep <pattern>`** — ti mostra esempi per ogni mode

---

## 6. Attack modes — `-a`

|`-a`|Nome|Cosa fa|
|---|---|---|
|**0**|**Dictionary / Straight**|Prova ogni parola della wordlist|
|**1**|Combination|Combina due wordlist (parolaA + parolaB)|
|**3**|**Mask / Brute force**|Genera tutte le combinazioni di un pattern|
|**6**|Hybrid Wordlist + Mask|Wordlist con suffisso pattern|
|**7**|Hybrid Mask + Wordlist|Prefisso pattern + wordlist|
|**9**|Association|Username-based (vedi sotto)|

> [!warning] Attack mode 2, 4, 5 Esistevano ma sono stati deprecati. Non ti preoccupare se vedi solo 0, 1, 3, 6, 7, 9.

### Attack mode 0 — Dictionary (il più comune)

```bash
hashcat -m 1000 -a 0 hash.txt rockyou.txt
```

Semplice: prova ogni password della wordlist. Si potenzia enormemente con **rules** (vedi sezione dedicata).

### Attack mode 3 — Mask

Permette di definire pattern di caratteri:

|Charset|Significato|
|---|---|
|`?l`|lettere minuscole (a-z)|
|`?u`|lettere maiuscole (A-Z)|
|`?d`|cifre (0-9)|
|`?h`|hex minuscolo (0-9a-f)|
|`?H`|hex maiuscolo (0-9A-F)|
|`?s`|simboli (!@#$...)|
|`?a`|tutto (`?l?u?d?s`)|
|`?b`|byte (0x00-0xFF)|

```bash
# Brute force password 8 caratteri tutti lowercase
hashcat -m 1000 -a 3 hash.txt ?l?l?l?l?l?l?l?l

# Pattern "Password" + 4 cifre + simbolo
hashcat -m 1000 -a 3 hash.txt Password?d?d?d?d?s

# Charset custom: maiuscola + 7 chars qualsiasi
hashcat -m 1000 -a 3 hash.txt ?u?a?a?a?a?a?a?a
```

> [!tip] Custom charset Puoi definire fino a 4 charset personalizzati con `-1`, `-2`, `-3`, `-4`:
> 
> ```bash
> # ?1 = lettere e cifre (alphanumeric)
> hashcat -m 1000 -a 3 -1 ?l?d hash.txt ?1?1?1?1?1?1
> ```

### Attack mode 6 — Hybrid Wordlist + Mask

Password = parola dalla wordlist + pattern aggiunto. Pattern molto comune:

```bash
# rockyou.txt + 4 cifre alla fine (es. password2024, hello1234)
hashcat -m 1000 -a 6 hash.txt rockyou.txt ?d?d?d?d
```

Questo cattura abitudini umane reali — "estate2024", "milan2024!", ecc.

### Attack mode 9 — Association (avanzato)

Per ogni hash, prova una specifica wordlist. Utile per Kerberoasting quando hai username e vuoi provare varianti del nome utente come password.

---

## 7. Rules — moltiplicatori di wordlist

Le **rules** trasformano ogni parola della wordlist applicando regole (maiuscola, sostituzioni leet, append cifre, ecc.). Una wordlist di 10M parole con una buona ruleset diventa effettivamente 1G+ tentativi.

```bash
hashcat -m 1000 -a 0 hash.txt rockyou.txt -r /usr/share/hashcat/rules/best64.rule
```

### Ruleset famosi

|Rule file|Note|
|---|---|
|`best64.rule`|Default, veloce, copre trasformazioni comuni|
|`dive.rule`|Aggressivo, molto più tentativi|
|`rockyou-30000.rule`|Derivato da analisi reali su rockyou|
|**OneRuleToRuleThemAll**|Comunità — combina i migliori, molto efficace|

> [!note] Sintassi rules Una rule è una sequenza di trasformazioni. Esempi:
> 
> - `l` → minuscolo tutto
> - `u` → maiuscolo tutto
> - `c` → capitalize (prima lettera maiuscola)
> - `$1` → appendi "1"
> - `^!` → prependi "!"
> - `sa@` → sostituisci 'a' con '@'
> 
> `c $1 $2 $3` applicato a `password` → `Password123`

---

## 8. OpenCL / CUDA — perché Hashcat va veloce

Hashcat è scritto per **GPU parallel computing**. Crack di hash è "embarrassingly parallel" — ogni tentativo è indipendente, perfetto per migliaia di core GPU.

### Backend

- **CUDA** — NVIDIA, performance massime
- **OpenCL** — standard cross-vendor (AMD, Intel, anche CPU)
- **pocl** — implementazione OpenCL su CPU, fallback se non hai GPU

> [!abstract] Analogia CPU: 1 persona legge un libro pagina per pagina, velocità X. GPU: 3000 persone leggono ognuna una pagina contemporaneamente, velocità 3000X — se il problema è parallelizzabile. Crack di hash MD5 = ogni tentativo è una pagina indipendente → perfetto per GPU.

### Verificare il backend

```bash
hashcat -I             # info su device disponibili (GPU, CPU, drivers)
hashcat -b             # benchmark — velocità per ogni mode
hashcat -b -m 1000     # benchmark solo NTLM
```

---

## 9. Performance e ottimizzazione

|Flag|Significato|Quando usare|
|---|---|---|
|`-O`|Optimized kernel|Sempre, se password ≤ 32 char (boost 2-3x)|
|`-w 1\|2\|3\|4`|Workload profile|`-w 3` default, `-w 4` se vuoi massima velocità (PC inutilizzabile)|
|`--force`|Forza esecuzione|Bypassa warning su drivers/devices|
|`--status`|Mostra status periodico|Live monitoring|
|`--status-timer 10`|Aggiorna ogni 10s|Combinato col precedente|

```bash
# Esempio "production": ottimizzato + workload alto + status live
hashcat -m 18200 -a 0 hash.txt rockyou.txt -O -w 3 --status --status-timer 10
```

> [!warning] Optimized kernel limit Con `-O` la password massima è 32 caratteri (per la maggior parte dei mode). Se sospetti password lunghissime (passphrase 50+ char), non usare `-O`.

---

## 10. Output management

### Potfile — dove finiscono le password crackate

Hashcat salva tutto in `~/.local/share/hashcat/hashcat.potfile`. Una volta crackato, l'hash è "ricordato" per sempre.

```bash
# Vedere password crackate per un file di hash
hashcat -m 1000 hash.txt --show

# Vedere quali hash NON sono stati crackati
hashcat -m 1000 hash.txt --left

# Disabilitare il potfile (utile per CTF se vuoi rifare da zero)
hashcat -m 1000 hash.txt rockyou.txt --potfile-disable
```

### Output su file

```bash
hashcat -m 1000 hash.txt rockyou.txt -o cracked.txt
```

---

## 11. Esempi end-to-end

### AS-REP Roasting (Sauna playbook)

```bash
# Impacket produce hash nel formato giusto:
GetNPUsers.py corp.local/ -no-pass -usersfile users.txt -format hashcat -outputfile hash.txt

# Crack
hashcat -m 18200 -a 0 hash.txt /usr/share/wordlists/rockyou.txt -O
```

### Kerberoasting

```bash
# Impacket
GetUserSPNs.py corp.local/lowuser:password -dc-ip 10.0.0.1 -request -outputfile hash.txt

# Crack
hashcat -m 13100 -a 0 hash.txt rockyou.txt -r best64.rule -O
```

### NTLM dump SAM

```bash
# Dopo dump con secretsdump o mimikatz
hashcat -m 1000 -a 0 ntlm_hashes.txt rockyou.txt -O
```

### Linux /etc/shadow

```bash
# Estrai solo le righe con hash:
sudo grep -v '^[^:]*:[!*]' /etc/shadow > shadow_hashes.txt

# Crack — sha512crypt è LENTO, ridimensiona aspettative
hashcat -m 1800 -a 0 shadow_hashes.txt rockyou.txt
```

> [!warning] sha512crypt è progettato per essere lento 1800 (sha512crypt) ha velocità ridotte di **6 ordini di grandezza** rispetto a NTLM. È by design — Linux usa apposta un algoritmo "slow" per `/etc/shadow`. Su una RTX 3080: NTLM ≈ 80 GH/s, sha512crypt ≈ 100 kH/s.

### WiFi WPA2 handshake

```bash
# Cattura con aircrack-ng / hcxdumptool, converti in formato 22000
hcxpcapngtool -o handshake.22000 capture.pcapng

hashcat -m 22000 handshake.22000 rockyou.txt -O
```

---

## 12. Performance reali — tabella indicativa

|Algoritmo (mode)|Velocità RTX 3080|
|---|---|
|MD5 (0)|~60 GH/s|
|NTLM (1000)|~80 GH/s|
|SHA1 (100)|~20 GH/s|
|Kerberos AS-REP (18200)|~1.5 GH/s|
|Kerberos TGS-REP (13100)|~1.5 GH/s|
|NetNTLMv2 (5600)|~5 GH/s|
|sha512crypt (1800)|~100 kH/s|
|bcrypt (3200)|~50 kH/s|
|WPA2 (22000)|~700 kH/s|

> [!tip] Implicazione pratica Una password NTLM da 8 caratteri lower+digits si crackha in **secondi/minuti**. La stessa password come bcrypt richiede **anni**. Questo è il motivo per cui app moderne usano bcrypt/argon2 — fanno crollare la velocità degli attacchi.

---

## 13. Resume e checkpointing

Le sessioni lunghe possono essere salvate e riprese:

```bash
# Salva sessione (auto se nominata)
hashcat -m 1000 hash.txt rockyou.txt --session my_crack

# Resume
hashcat --session my_crack --restore
```

Ctrl+C salva automaticamente. Utile per crack che durano giorni.

---

## 14. Comandi quotidiani — cheatsheet

```bash
# Info su device disponibili
hashcat -I

# Benchmark di un mode specifico
hashcat -b -m 1000

# Crack basico dictionary
hashcat -m <mode> -a 0 hash.txt rockyou.txt -O

# Crack con rules
hashcat -m <mode> -a 0 hash.txt rockyou.txt -r best64.rule -O

# Brute force con mask
hashcat -m <mode> -a 3 hash.txt ?a?a?a?a?a?a -O

# Vedere risultati
hashcat -m <mode> hash.txt --show

# Esempio hash di un mode
hashcat -m 18200 --example-hashes

# Stop pulito (Ctrl+C salva)
# Resume:
hashcat --session <nome> --restore
```

---

## Takeaways

1. Hashcat è **offline** — opera su hash, non su servizi. Zero traffico verso il target
2. **`-m` + `-a` determinano tutto** — algoritmo + tipo di attacco
3. **Identifica il mode** via prefisso, hashid/nth, o output del tool che ha prodotto l'hash
4. **Attack mode 0** (dictionary) + **rules** = la combinazione che funziona nel 90% dei casi
5. **GPU = ordini di grandezza più veloce** — usa CUDA su NVIDIA, OpenCL altrove, pocl come fallback CPU
6. **Algoritmi "slow" by design** (bcrypt, sha512crypt, argon2) sono mitigazioni reali — abbattono la velocità di crack di 5-6 ordini di grandezza
7. **Potfile** salva tutto — `--show` per recuperare risultati senza ricrackare
8. **`-O`** quasi sempre (boost 2-3x, costa solo limit di 32 char)

---

## Wiki-links

- [[hydra]]
- [[medusa]]
- [[getnpusers_asrep_roasting]]
- [[kerberoasting]]
- [[htb_sauna]]
- [[password_attacks]]
- [[ntlm_hashes]]
- [[wordlists]]
- [[john_the_ripper]]
- [[responder]]