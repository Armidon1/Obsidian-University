# NetBIOS

## Cos'è

NetBIOS (Network Basic Input/Output System) è un'**API di rete** sviluppata da IBM negli anni '80 che permette alle applicazioni di comunicare su una rete locale. Originariamente progettato per reti LAN piccole, è ancora presente in ambienti Windows per compatibilità.

Non è un protocollo di routing — funziona solo sulla **rete locale (LAN)**, non su internet.

---

## Porte

| Porta   | Protocollo | Servizio                        |
| ------- | ---------- | ------------------------------- |
| **137** | UDP/TCP    | [[NetBIOS Name Service (NBNS)]] |
| **138** | UDP        | [[NetBIOS Datagram Service]]    |
| **139** | TCP        | [[NetBIOS Session Service]]     |

---

## I tre servizi

### Name Service (porta 137)

Risolve i **nomi NetBIOS** in indirizzi IP — funziona come un DNS locale. Ogni macchina Windows ha un nome NetBIOS (es. `DESKTOP-ABC123`).

### Datagram Service (porta 138)

Comunicazione **connectionless** — usata per messaggi broadcast sulla rete locale (es. "chi c'è in questa rete?").

### Session Service (porta 139)

Comunicazione **connection-oriented** — usata per trasferimento file e accesso a risorse condivise (cartelle, stampanti).

---

## Perché è interessante nel pentesting

NetBIOS è una **miniera di informazioni** sulla rete locale. Interrogando il servizio sulla porta 137 puoi ottenere:

- **Nome del computer**
- **Nome del dominio/workgroup**
- **Indirizzo MAC** della scheda di rete
- **Servizi attivi** sulla macchina
- **Utente loggato** in quel momento

Tutto questo senza autenticazione — è informazione pubblica sulla rete locale.

---

## Strumenti per interrogare NetBIOS

### nbtstat (Windows)

```
nbtstat -A 192.168.1.10      # Info NetBIOS di un IP specifico
nbtstat -n                   # Nomi NetBIOS della macchina locale
```

### nmblookup (Linux)

```bash
nmblookup -A 192.168.1.10    # Equivalente di nbtstat su Linux
```

### nmap

```bash
nmap -sU -p 137 192.168.1.0/24              # Scansiona porta 137 UDP
nmap --script nbstat.nse 192.168.1.10       # Script dedicato NetBIOS
```

---

## Lettura della tabella NetBIOS

L'output di nbtstat/nmblookup mostra una tabella con nomi e codici:

|Codice|Tipo|Significato|
|---|---|---|
|`00`|UNIQUE|Nome del computer o dominio|
|`03`|UNIQUE|Servizio Messenger (utente loggato)|
|`20`|UNIQUE|File and Print Sharing attivo|
|`1E`|GROUP|Browser Election (workgroup)|
|`1D`|UNIQUE|Master Browser della rete|

Il codice `20` è particolarmente interessante — indica che la macchina ha **condivisioni di rete attive**, potenzialmente accessibili.

---

## NetBIOS vs DNS

| |NetBIOS|DNS|
|---|---|---|
|Scope|Solo LAN|Internet e LAN|
|Porta|137 UDP|53 UDP/TCP|
|Autenticazione|Nessuna|Nessuna (per query base)|
|Sistema|Legacy Windows|Universale|

---

## NetBIOS over TCP/IP (NBT)

Originariamente NetBIOS non usava TCP/IP. Con l'espansione di internet fu incapsulato in TCP/IP — questa versione si chiama **NBT** o **[[NetBT]]**. È quella che trovi ancora oggi nei sistemi Windows.

---

## SMB e NetBIOS

**[[SMB]] (Server Message Block)** è il protocollo che usa NetBIOS per condividere file e stampanti. Nelle versioni moderne di Windows, SMB può girare direttamente su TCP porta **445** senza NetBIOS — ma la porta 139 è ancora supportata per compatibilità.

```
Versioni vecchie:  SMB → NetBIOS (139)
Versioni moderne:  SMB → TCP diretto (445)
```

---

## Rischi di sicurezza

- **Information disclosure** — rivela nomi macchine, utenti loggati, MAC address senza autenticazione
- **NBNS Spoofing** — un attaccante può rispondere a query broadcast fingendo di essere un host legittimo (base per attacchi MITM)
- **[[Null Session]]** — connessioni anonime alla porta 139 che in sistemi non patchati rivelano liste di utenti e condivisioni

---

## Mitigazioni

- Disabilitare NetBIOS se non necessario (pannello di controllo adattatori di rete → TCP/IP → Avanzate → WINS)
- Bloccare le porte 137-139 sul firewall perimetrale
- Usare SMB solo su porta 445 con versioni moderne (SMBv3)

Hai capito benissimo la struttura. Ora chiarisco il punto finale.

---

## Perché SMB diretto su 445 è più sicuro di SMB su NetBT/139

Non è che SMB stesso sia diventato più sicuro — è che **rimuovere NetBT elimina tre porte e tre superfici di attacco aggiuntive** che non hanno nulla a che fare con il file sharing in sé.

Quando usi SMB su NetBT hai:

```
UDP 137  →  esposto  →  NBNS spoofing, enumerazione nomi, hash capture
UDP 138  →  esposto  →  sniffing broadcast, enumerazione passiva
TCP 139  →  esposto  →  Null Session, enumerazione IPC$, attacchi legacy
TCP 445  →  esposto  →  SMB (EternalBlue, SMBGhost...)
```

Quando usi solo SMB diretto su 445 e disabiliti NetBT:

```
UDP 137  →  chiuso
UDP 138  →  chiuso
TCP 139  →  chiuso
TCP 445  →  esposto  →  solo SMB
```

---

## Il problema non era SMB — era il contorno

NetBT portava con sé tutto un ecosistema di protocolli anni '80 pensati per reti locali piccole e fidate, senza nessun concetto di autenticazione o sicurezza:

- **NBNS** non autentica le risposte → chiunque può rispondere a una query con un IP falso → Responder
- **Null Session** era una feature intenzionale di NetBT/IPC$ — serviva per bootstrappare la comunicazione prima dell'autenticazione → diventata vettore di enumerazione
- **Browser Service** broadcastava continuamente informazioni sulla rete → enumerazione passiva gratuita

SMB diretto su 445 si libera di tutto questo bagaglio. Parli solo SMB, con autenticazione obbligatoria, nessun broadcast, nessun named pipe anonimo.

---

## Analogia

Pensa a NetBT come a un palazzo vecchio dove per entrare nell'appartamento principale (SMB/file sharing) devi prima passare per tre ingressi secondari (137, 138, 139) — ognuno con la sua serratura difettosa. SMB su 445 è lo stesso appartamento ma con un ingresso diretto — le tre porte secondarie non esistono più.

---

## Una cosa però non cambia

SMB su 445 ha i suoi problemi indipendenti da NetBT — EternalBlue, SMBGhost, SMB relay. Disabilitare NetBT non risolve quelli. È solo che hai eliminato una superficie di attacco senza migliorare l'altra.

Per questo le contromisure moderne sono sempre in coppia:

- Disabilita NetBT → chiudi 137/138/139
- Mantieni SMB aggiornato e con signing obbligatorio → proteggi 445

---

## Related Notes

- [[Obsidian-University/University/Magistrale/Ethical Hacking/For Passion/Scanning/Nmap]]
- [[SMB]]
- [[Port Scanning]]
- [[Windows Enumeration]]
- [[MITM Attacks]]

---

_References: Hacking Exposed 7 · man nmblookup · https://learn.microsoft.com/en-us/windows/win32/netbios/netbios_