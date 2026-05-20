---

tags:

- tools
- password-attack
- brute-force
- medusa
- online-attack aliases:
- medusa brute force
- medusa password attack

---

# Medusa — Online Password Attack

## 1. Cos'è

Medusa è uno strumento per **attacchi a password su servizi di rete attivi**, concettualmente identico a [[hydra]]. La distinzione principale è architetturale: Medusa è progettata per essere più **stabile e affidabile con alti livelli di parallelismo** — molti host e molti thread simultanei.

> [!note] Concetti condivisi con Hydra Online vs offline, password spraying vs brute force, lockout risk, wordlist, Event ID 4625 — tutto già coperto in [[hydra]]. Questa nota si concentra su sintassi e differenze.

---

## 2. Differenze rispetto a Hydra

|Aspetto|Hydra|Medusa|
|---|---|---|
|**Manutenzione**|Attivamente sviluppato|Meno aggiornato ma stabile|
|**Protocolli**|50+|~20 principali|
|**Parallelismo**|Thread per singolo target|Thread per host + host concorrenti simultanei|
|**Stabilità a molti thread**|Può crashare / perdere tentativi|Più affidabile sotto carico|
|**Sintassi**|Flag corti, concisa|Più verbosa, esplicita|
|**Architettura**|Monolitica|Modulare — ogni protocollo è un modulo `.mod`|
|**Output**|Minimo|Più strutturato, log dettagliato|

> [!tip] Quando scegliere Medusa Preferisci Medusa quando Hydra crasha o perde tentativi con `-t` alti, oppure quando attacchi **molti host in parallelo** (scan di rete, non singolo target). Per uso quotidiano su un singolo target, Hydra va benissimo.

---

## 3. Protocolli supportati (moduli principali)

```bash
# Lista moduli disponibili
medusa -d
```

|Modulo|Protocollo|
|---|---|
|`ssh`|SSH|
|`ftp`|FTP|
|`smb`|SMB (Windows shares)|
|`http`|HTTP Basic Auth|
|`web-form`|HTTP form login|
|`rdp`|RDP (richiede freerdp)|
|`telnet`|Telnet|
|`mssql`|Microsoft SQL Server|
|`mysql`|MySQL|
|`postgres`|PostgreSQL|
|`smtp`|SMTP|
|`pop3`|POP3|
|`imap`|IMAP|
|`vnc`|VNC|
|`ldap`|LDAP|

---

## 4. Sintassi base

```bash
medusa -h <host> -u <user> -P <wordlist> -M <modulo>
```

### Flags principali

|Flag|Significato|Esempio|
|---|---|---|
|`-h`|Host singolo|`-h 192.168.1.10`|
|`-H`|File con lista di host|`-H hosts.txt`|
|`-u`|Username singolo|`-u admin`|
|`-U`|File con lista username|`-U users.txt`|
|`-p`|Password singola|`-p Password123`|
|`-P`|Wordlist password|`-P rockyou.txt`|
|`-M`|Modulo (protocollo)|`-M ssh`|
|`-t`|Thread per host|`-t 4`|
|`-T`|Host concorrenti simultanei|`-T 10`|
|`-f`|Stop al primo match (globale)|`-f`|
|`-b`|Stop al primo match per host|`-b`|
|`-n`|Porta non standard|`-n 2222`|
|`-s`|Forza SSL|`-s`|
|`-v`|Verbosità (0–6)|`-v 4`|
|`-O`|Output su file|`-O risultati.txt`|

> [!note] `-t` vs `-T` `-t 4` = 4 thread su un singolo host. `-T 10` = 10 host attaccati contemporaneamente. Combinati: `-t 4 -T 10` = 40 connessioni totali. Questo è il vantaggio principale di Medusa in scan di rete ampi.

---

## 5. Esempi comuni

### SSH

```bash
medusa -h 192.168.1.10 -u mario -P /usr/share/wordlists/rockyou.txt -M ssh -t 4
```

### SMB — password spraying su AD

```bash
# Una password, lista utenti
medusa -h 192.168.1.10 -U utenti.txt -p "Password2024!" -M smb -t 2
```

### FTP

```bash
medusa -h 192.168.1.10 -u admin -P passwords.txt -M ftp -f
```

### HTTP form login

```bash
medusa -h 192.168.1.10 -u admin -P rockyou.txt -M web-form \
  -m "FORM:/login:user=^USER^&pass=^PASS^:Login failed"
#        ^path^  ^parametri^               ^stringa fallimento^
```

### Attacco su più host in parallelo

```bash
# Attacca tutti gli host in hosts.txt, 4 thread per host, 5 host simultanei
medusa -H hosts.txt -U users.txt -P passwords.txt -M ssh -t 4 -T 5 -O output.txt
```

---

## 6. Confronto sintassi Hydra vs Medusa

Stesso attacco SSH scritto nei due tool:

```bash
# Hydra
hydra -l mario -P rockyou.txt ssh://192.168.1.10 -t 4 -f

# Medusa
medusa -h 192.168.1.10 -u mario -P rockyou.txt -M ssh -t 4 -f
```

La logica è identica, la sintassi è speculare. Il protocollo in Hydra è nel target URI (`ssh://`), in Medusa è nel flag `-M`.

---

## Takeaways

1. Medusa e Hydra fanno la stessa cosa — la scelta dipende dalla **stabilità sotto carico**
2. Medusa è preferibile con **molti host simultanei** (`-T`) o quando Hydra è instabile ad alto parallelismo
3. Architettura **modulare** — ogni protocollo è un file `.mod` separato, più facile da ispezionare/debuggare
4. Sintassi più verbosa ma anche più esplicita — ogni parametro ha un flag dedicato
5. Per AD, come per Hydra, la regola è sempre **spraying lento**, non brute force aggressivo

---

## Wiki-links

- [[hydra]]
- [[netexec_crackmapexec]]
- [[password_spraying]]
- [[password_attacks]]
- [[wordlists]]
- [[active_directory]]
- [[smb]]