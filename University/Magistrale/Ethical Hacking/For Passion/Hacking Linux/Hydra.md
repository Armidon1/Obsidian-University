---

tags:

- tools
- password-attack
- brute-force
- hydra
- online-attack
- hacking-exposed-7 aliases:
- THC-Hydra
- online brute force
- password spraying

---

# Hydra — Online Password Attack

## 1. Cos'è e perché esiste

Hydra (THC-Hydra) è uno strumento per **attacchi a password su servizi di rete attivi**. Automatizza il tentativo di login su protocolli di rete, provando combinazioni di username/password fino a trovare credenziali valide.

> [!warning] Distinzione fondamentale — Online vs Offline Questa è la differenza più importante da interiorizzare:
> 
> |Tipo|Strumento|Dove avviene|Limite di velocità|Rischio lockout|
> |---|---|---|---|---|
> |**Offline**|hashcat, john|Localmente su hash rubati|Solo la tua GPU|No|
> |**Online**|Hydra, Medusa|Sul servizio remoto live|La rete + il server|Sì|
> 
> Con Sauna hai fatto **offline**: hai rubato l'hash AS-REP e lo hai crackato in locale senza toccare il DC. Hydra lavora sull'opposto — colpisce il servizio direttamente, ogni tentativo è una connessione di rete reale.

---

## 2. Protocolli supportati

Hydra supporta oltre 50 protocolli. I più rilevanti in contesto pentest:

| Categoria          | Protocolli                                                                                                                     |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| **Accesso remoto** | [[Obsidian-University/University/Magistrale/Cybersecurity/6 CFU/otherInfo/SSH\|SSH]], [[RDP (ms-wbt-server)]], [[Telnet]], VNC |
| **Windows / AD**   | [[SMB]], WinRM                                                                                                                 |
| **Web**            | HTTP-GET, HTTP-POST, HTTP-Form, HTTPS                                                                                          |
| **Database**       | MySQL, PostgreSQL, MSSQL, Oracle                                                                                               |
| **Mail**           | SMTP, POP3, IMAP                                                                                                               |
| **File transfer**  | FTP, SFTP                                                                                                                      |
| **Altri**          | LDAP, SIP, IRC, Redis, MongoDB                                                                                                 |

---

## 3. Sintassi base

```bash
hydra [opzioni] <target> <protocollo>
```

### Flags principali

|Flag|Significato|Esempio|
|---|---|---|
|`-l`|Singolo username|`-l admin`|
|`-L`|Lista di username da file|`-L /usr/share/wordlists/users.txt`|
|`-p`|Singola password|`-p Password123`|
|`-P`|Lista di password (wordlist)|`-P /usr/share/wordlists/rockyou.txt`|
|`-t`|Thread paralleli (default 16)|`-t 4`|
|`-f`|Stop al primo match trovato|`-f`|
|`-s`|Porta non standard|`-s 2222`|
|`-V`|Verbose — mostra ogni tentativo|`-V`|
|`-o`|Salva output su file|`-o risultati.txt`|
|`-e nsr`|Prova anche: null, same, reverse|`-e nsr`|

> [!note] `-e nsr` spiegato
> 
> - `n` — prova password vuota
> - `s` — prova username come password (es. user: admin, pass: admin)
> - `r` — prova username al contrario (es. user: admin, pass: nimda) Veloce da provare, coglie configurazioni pigre.

---

## 4. Esempi comuni

### SSH

```bash
# Username noto, wordlist password
hydra -l mario -P /usr/share/wordlists/rockyou.txt ssh://192.168.1.10

# Lista utenti + lista password
hydra -L users.txt -P passwords.txt ssh://192.168.1.10 -t 4 -f
```

> [!warning] SSH e thread SSH ha un limite di connessioni simultanee. Tieni `-t` basso (4–8) per evitare di essere bloccato o di triggerare fail2ban troppo presto.

### HTTP form (login web)

```bash
hydra -l admin -P rockyou.txt 192.168.1.10 http-post-form \
  "/login:username=^USER^&password=^PASS^:Invalid credentials"
#                    ^parametri form^           ^stringa di fallimento^
```

Il terzo campo del modulo HTTP è la **stringa che indica fallimento** nella risposta — Hydra la usa per capire se il login è andato a buon fine.

### WinRM (rilevante post-Sauna)

```bash
hydra -l administrator -P passwords.txt winrm://192.168.1.10
```

### RDP

```bash
hydra -l administrator -P rockyou.txt rdp://192.168.1.10 -t 4
```

---

## 5. Password Spraying vs Brute Force

> [!abstract] Distinzione importante per ambienti AD

|Tecnica|Logica|Rischio lockout|
|---|---|---|
|**Brute force**|Molte password su un utente|Alto — l'account si blocca|
|**Password spraying**|Una password su molti utenti|Basso — ogni account riceve pochi tentativi|

In Active Directory il brute force classico è **autolesionista** — la policy di lockout (tipicamente 5 tentativi sbagliati → account bloccato per X minuti) ti rende la vita impossibile e fa partire un alert.

Il password spraying è il modo corretto di operare in AD:

```bash
# Spraying: una password, lista di utenti
hydra -L utenti_dominio.txt -p "Password2024!" smb://192.168.1.10
```

La logica: molti utenti usano password stagionali (`Password2024!`, `Autunno2024`, ecc.). Provi quella password su tutti — ogni account riceve un solo tentativo, mai si blocca.

---

## 6. Wordlist consigliate

|Wordlist|Percorso Kali|Uso|
|---|---|---|
|**rockyou.txt**|`/usr/share/wordlists/rockyou.txt`|Password generale, 14M entries|
|**SecLists passwords**|`/usr/share/seclists/Passwords/`|Raccolta specializzata per contesto|
|**SecLists usernames**|`/usr/share/seclists/Usernames/`|Username comuni, nomi, pattern AD|
|**Common-Credentials**|`/usr/share/seclists/Passwords/Common-Credentials/`|Top 100/1000 password — per spraying rapido|

```bash
# Su Kali, se SecLists non è installato:
sudo apt install seclists
```

---

## 7. Rilevamento e contromisure

|Difesa|Come funziona|Limiti|
|---|---|---|
|**Account lockout**|Blocca l'account dopo N tentativi|Non funziona contro password spraying lento|
|**fail2ban**|Banna IP dopo N fallimenti SSH/FTP|Si bypassa con IP rotation|
|**Rate limiting**|Rallenta le risposte dopo N tentativi|Rallenta Hydra ma non lo ferma|
|**MFA**|Secondo fattore richiesto|Neutralizza completamente i credential attacks|
|**Logging + SIEM**|Alert su pattern di fallimenti|Detection, non prevention|
|**Honeypot account**|Account fake che non esiste — chi lo prova è un attaccante|Dipende dalla configurazione|

> [!tip] Dal lato del difensore Event ID Windows da monitorare:
> 
> - **4625** — Failed logon (ogni tentativo Hydra su SMB/WinRM)
> - **4648** — Logon with explicit credentials
> - Molti 4625 in poco tempo dallo stesso IP = alert immediato

---

## 8. Hydra vs altri tool

|Tool|Punto di forza|Quando usarlo|
|---|---|---|
|**Hydra**|Molti protocolli, attivamente mantenuto|Default per la maggior parte dei casi|
|**Medusa**|Più stabile su connessioni parallele massive|Quando Hydra crasha con molti thread|
|**CrackMapExec / NetExec**|Integrazione AD nativa, spraying, PTH|Ambienti Windows/AD — più contesto di Hydra|
|**Burp Suite Intruder**|Attacchi su HTTP con logica complessa|Web app con token CSRF, workflow multi-step|

> [!note] CrackMapExec → NetExec CrackMapExec è il tool AD per eccellenza per spraying + post-exploitation su SMB/WinRM. È stato rinominato **NetExec** (`nxc`) nelle versioni recenti. Più potente di Hydra per ambienti AD ma meno generico.

---

## 9. Connessione con Sauna

Su Sauna hai ottenuto `fsmith` via AS-REP Roasting — **offline**, senza toccare il DC. Se non avessi trovato l'hash via Kerberos, un'alternativa sarebbe stata password spraying su WinRM o SMB con una lista di utenti (quella costruita con username-anarchy) e password stagionali comuni.

```bash
# Quello che avresti potuto provare su Sauna (se AS-REP non avesse funzionato):
hydra -L candidati.txt -p "Password2023!" winrm://10.10.10.175 -t 4
hydra -L candidati.txt -P /usr/share/seclists/Passwords/Common-Credentials/10-million-password-list-top-1000.txt \
      smb://10.10.10.175 -t 4 -f
```

Il motivo per cui AS-REP è preferibile: **unauthenticated, silenzioso, offline**. Hydra genera molto rumore (4625 per ogni tentativo).

---

## Takeaways

1. Hydra è per attacchi **online** — ogni tentativo è una connessione di rete reale, lenta e rumorosa
2. Differenza fondamentale: **offline (hashcat) = veloce, silenzioso, no lockout** — **online (Hydra) = lento, rumoroso, lockout risk**
3. In AD usa sempre **password spraying** (una password, molti utenti) — mai brute force su un singolo account
4. `-e nsr` è un quick win gratuito da includere sempre
5. Per ambienti AD, **NetExec/CrackMapExec** è più potente di Hydra
6. Ogni tentativo Hydra su Windows genera **Event ID 4625** — facilmente rilevabile

---

## Wiki-links

- [[hashcat_modes]]
- [[password_attacks]]
- [[password_spraying]]
- [[getnpusers_asrep_roasting]]
- [[htb_sauna]]
- [[netexec_crackmapexec]]
- [[active_directory]]
- [[winrm]]
- [[wordlists]]