# Network Discovery — Scansione LAN

**Categoria:** #recon #network #enumeration  
**Uso:** Scoprire host attivi sulla propria rete locale

---

## 📖 Cos'è

La network discovery è il processo di identificare quali dispositivi sono attivi su una rete locale. È il primo passo di qualsiasi attività di recon su una LAN.

---

## 🔍 Prima di tutto — trova il tuo IP e subnet

```bash
ip a
# oppure
ifconfig
```

Se il tuo IP è `192.168.1.105` la tua subnet è tipicamente `192.168.1.0/24`.

---

## 🛠️ Tool disponibili

### arp-scan (il più veloce e affidabile)

```bash
# Scansiona automaticamente la rete locale
sudo arp-scan -l

# Subnet specifica
sudo arp-scan 192.168.1.0/24

# Installazione
sudo apt install arp-scan
```

Mostra IP, MAC address e vendor del dispositivo. Usa ARP quindi funziona solo sulla rete locale (Layer 2).

---

### nmap — ping sweep

```bash
# Scansione base
nmap -sn 192.168.1.0/24

# Più veloce
nmap -sn --min-rate 5000 192.168.1.0/24
```

`-sn` = solo host discovery, nessuna port scan.

---

### netdiscover

```bash
# Attivo — scansiona la subnet
sudo netdiscover -r 192.168.1.0/24

# Passivo — ascolta il traffico ARP senza inviare pacchetti
sudo netdiscover -p
```

Utile in modalità passiva quando non vuoi generare traffico.

---

### fping — ping sweep veloce

```bash
fping -a -g 192.168.1.0/24 2>/dev/null

# Installazione
sudo apt install fping
```

`-a` = mostra solo host attivi, `-g` = genera range di IP.

---

## 📊 Confronto

|Tool|Velocità|Layer|Note|
|---|---|---|---|
|arp-scan|⚡⚡⚡|L2 (ARP)|Solo LAN, molto affidabile|
|nmap -sn|⚡⚡|L3 (ICMP)|Versatile, funziona anche fuori LAN|
|netdiscover|⚡⚡|L2 (ARP)|Ottima modalità passiva|
|fping|⚡⚡⚡|L3 (ICMP)|Veloce, solo ping|

---

## 📚 Lezioni apprese

- `arp-scan -l` è il comando più rapido per una LAN scan
- ARP-based tools (arp-scan, netdiscover) funzionano **solo sulla rete locale**
- nmap `-sn` è più versatile ma leggermente più lento
- La modalità passiva di netdiscover non genera traffico → più stealth
- Alcuni host bloccano ICMP (ping) → in quel caso ARP scan è più affidabile

---
## usarlo con altre interfacce di rete

Sì, ma con limitazioni. `tun0` è l'interfaccia VPN di HTB — è una rete punto-punto, non una LAN broadcast, quindi arp-scan funziona diversamente.

```bash
sudo arp-scan -I tun0 -l
```

Probabilmente non troverà nulla o pochissimo, perché ARP funziona su Layer 2 e `tun0` è Layer 3 (non c'è broadcast ARP su una VPN tunnel).

**Per scoprire host sulla rete HTB usa invece nmap:**

```bash
nmap -sn 10.129.0.0/16 --min-rate 5000
```

O se vuoi solo scansionare la subnet più vicina:

```bash
nmap -sn 10.129.43.0/24
```

In ambito HTB però la network discovery sulla VPN è raramente necessaria — le macchine target ti vengono date direttamente con il loro IP.


## 🔗 Riferimenti

- [nmap host discovery](https://nmap.org/book/man-host-discovery.html)
- [arp-scan man page](https://www.kali.org/tools/arp-scan/)

---

## Tags

#arp-scan #nmap #netdiscover #fping #network-discovery #lan #recon #enumeration