# Tor — The Onion Router

#linux #cybersecurity #anonymity #networking #linux-basics-for-hackers

---

## 🗂️ Overview

**Tor** (The Onion Router) is a free, open-source anonymity network that routes your internet traffic through a series of volunteer-operated **relays**, encrypting it at each step. Originally developed by the **U.S. Naval Research Laboratory** in the mid-1990s, it is now maintained by the non-profit **Tor Project**.

The name "onion routing" comes from the **layered encryption** — like the layers of an onion, each relay peels off one layer of encryption, knowing only where it received the traffic from and where to send it next.

```
You → [Relay 1 (Guard)] → [Relay 2 (Middle)] → [Relay 3 (Exit)] → Destination
       encrypts 3 layers     peels 1 layer        peels 1 layer      sees plaintext
```

> [!info] Key Property No single relay knows both **who you are** and **what you're accessing**. The Guard node knows your IP but not the destination. The Exit node knows the destination but not your IP.

---

## 🧅 How Onion Routing Works

### Step by step

```
1. Tor client downloads a list of available relays from a Directory Server

2. Tor client builds a 3-hop circuit:
   Guard node  → knows YOUR real IP, does NOT know destination
   Middle node → knows neither your IP nor destination
   Exit node   → knows destination, does NOT know your IP

3. Data is encrypted in 3 layers BEFORE leaving your machine:
   Encrypt for Exit   → Encrypt for Middle → Encrypt for Guard
   └─────────────────────────────────────────────────────────┘
                        sent to Guard node

4. Each relay decrypts ONE layer and forwards the rest:
   Guard  → decrypts outer layer → forwards to Middle
   Middle → decrypts middle layer → forwards to Exit
   Exit   → decrypts inner layer → sends to destination
```

### Why 3 hops minimum

- **1 hop** → relay knows both you and destination → no anonymity
- **2 hops** → if Guard and Exit collude → deanonymized
- **3 hops** → colluding Guard + Exit still doesn't reveal Middle → much harder to correlate

---

## 🛠️ Installation

### Kali / Parrot / Debian / Ubuntu

```bash
sudo apt update
sudo apt install tor -y
```

### Start / Stop / Status

```bash
sudo systemctl start tor
sudo systemctl stop tor
sudo systemctl status tor
sudo systemctl enable tor      # start on boot
```

### Verify it's running

```bash
ss -tlnp | grep 9050           # tor listens on port 9050 by default
curl --socks5 127.0.0.1:9050 https://check.torproject.org/api/ip
```

---

## ⚙️ Configuration — torrc

The main config file is at `/etc/tor/torrc`. By default most options are commented out.

```bash
sudo nano /etc/tor/torrc
```

### Key options

```bash
# Socks proxy port (default — already active)
SOCKSPort 9050

# Control port (needed for tools like proxychains, nyx)
ControlPort 9051

# Log level
Log notice file /var/log/tor/notices.log

# Use specific entry/exit countries (2-letter ISO code)
EntryNodes {it},{de}
ExitNodes {nl},{se}
StrictNodes 1              # enforce the above — don't use others

# Exclude specific countries
ExcludeExitNodes {us},{gb},{au}    # avoid Five Eyes countries

# Run as relay (contribute to the network)
ORPort 9001
Nickname MyRelay
ContactInfo your@email.com
```

> [!warning] After editing `torrc`, always restart tor:
> 
> ```bash
> sudo systemctl restart tor
> ```

---

## 🔗 Proxychains — Route Any Tool Through Tor

By default, only applications configured to use a SOCKS5 proxy can use Tor. **Proxychains** forces **any** tool through Tor transparently.

### Configure Proxychains

```bash
sudo nano /etc/proxychains4.conf
```

```bash
# At the bottom of the file, ensure this line exists:
socks5  127.0.0.1  9050

# Recommended settings at the top:
dynamic_chain          # skip dead proxies automatically
proxy_dns              # route DNS through Tor (prevent DNS leaks)
```

### Use Proxychains with any tool

```bash
proxychains nmap -sT -Pn 192.168.0.1         # nmap through Tor
proxychains curl https://example.com          # curl through Tor
proxychains firefox                           # browser through Tor
proxychains sqlmap -u http://target.com       # sqlmap through Tor
proxychains ssh user@target.com               # SSH through Tor
proxychains python3 exploit.py               # any script through Tor
```

> [!warning] `nmap -sS` (SYN scan) does **NOT** work through Tor — raw packets can't travel through a SOCKS proxy. Always use `-sT` (TCP connect scan) with proxychains.

> [!tip] Hacking Note Combining Proxychains + Tor routes your tool's traffic through the Tor network transparently — the target sees only the **Tor exit node IP**, not yours.

---

## 🌐 Tor Browser

The easiest way to use Tor for web browsing — a pre-configured Firefox with:

- Tor network built-in
- NoScript enabled by default
- Canvas fingerprinting blocked
- WebRTC disabled (prevents IP leaks)

```bash
# Download from official site only
https://www.torproject.org/download/

# Or on Kali
sudo apt install torbrowser-launcher
torbrowser-launcher
```

> [!warning] Never install browser extensions on Tor Browser — they can deanonymize you. Never maximize the window — screen resolution is a fingerprinting vector.

---

## 🧅 Hidden Services — .onion Addresses

Tor allows servers to operate as **hidden services** — accessible only within the Tor network via `.onion` addresses. Neither the client nor the server reveals their real IP.

```
Facebook:  facebookwkhpilnemxj7ascrwwwg5yvmrygmwlnhqopxqyyzxpqxrknyd.onion
DuckDuckGo: duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion
```

### Create your own hidden service

```bash
sudo nano /etc/tor/torrc
```

```bash
# Add these lines
HiddenServiceDir /var/lib/tor/hidden_service/
HiddenServicePort 80 127.0.0.1:8080
```

```bash
sudo systemctl restart tor

# Tor generates your .onion address automatically
sudo cat /var/lib/tor/hidden_service/hostname
# → youraddress.onion
```

---

## 📊 Tor vs VPN vs Proxychains

||Tor|VPN|Proxychains|
|---|---|---|---|
|**Anonymity**|⭐⭐⭐⭐⭐|⭐⭐⭐|⭐⭐|
|**Speed**|🐢 Slow|🟢 Fast|🟡 Depends|
|**Encryption**|Multi-layer|Single tunnel|None (by itself)|
|**Trust required**|No one|VPN provider|Proxy operators|
|**Hides from ISP**|✅|✅|❌|
|**Hides from destination**|✅|✅|✅|
|**Cost**|Free|Usually paid|Free|
|**Works with any tool**|Via proxychains|Yes (system-wide)|Yes|
|**Latency**|500–700ms|10–50ms|Variable|

---

## ⚠️ Tor Limitations & Attack Vectors

Tor is powerful but **not magic**. You can still be deanonymized by:

### Traffic correlation attacks

If an adversary controls both the Guard node and monitors your ISP, they can **correlate timing** of packets entering and leaving the network.

```
NSA/GCHQ level threat — not relevant for most scenarios
```

### Exit node eavesdropping

The Exit node sees **plaintext traffic** if you're not using HTTPS. A malicious exit node can read or modify unencrypted traffic.

```bash
# Always use HTTPS — never send credentials over plain HTTP through Tor
```

### Browser fingerprinting

JavaScript, screen resolution, fonts, plugins — all can fingerprint your browser even through Tor.

```
Solution: Use Tor Browser with default settings. Never maximize the window.
```

### AI deanonymization (2026)

Recent research shows LLMs can match **writing style** across platforms with up to 67% accuracy — tools don't protect you if your writing is distinctive.

```
Solution: Compartmentalize identities completely. Never reuse usernames or writing style.
```

### Operational security (OPSEC) failures

Most Tor users are deanonymized not by breaking the protocol, but by **human mistakes**:

- Logging into personal accounts while on Tor
- Reusing usernames across clearnet and darknet
- Buying things with traceable payment methods
- Tor running but one app bypassing it (DNS leak)

---

## 🔧 Useful Tools

```bash
# Nyx — terminal monitor for Tor (bandwidth, circuits, logs)
sudo apt install nyx
nyx

# Check your Tor IP
curl --socks5 127.0.0.1:9050 https://api.ipify.org

# Force a new Tor circuit (new IP)
sudo systemctl restart tor
# or via control port:
echo -e 'AUTHENTICATE ""\r\nSIGNAL NEWNYM\r\nQUIT' | nc 127.0.0.1 9051
```

---

## 🔗 Command Cheat Sheet

```bash
# Install and manage
sudo apt install tor -y
sudo systemctl start tor
sudo systemctl status tor
sudo systemctl restart tor

# Verify
ss -tlnp | grep 9050
curl --socks5 127.0.0.1:9050 https://check.torproject.org/api/ip

# Proxychains + Tor
proxychains nmap -sT -Pn target_ip
proxychains curl https://target.com
proxychains sqlmap -u http://target.com

# New circuit
echo -e 'AUTHENTICATE ""\r\nSIGNAL NEWNYM\r\nQUIT' | nc 127.0.0.1 9051

# Hidden service hostname
sudo cat /var/lib/tor/hidden_service/hostname

# Monitor
nyx
```

---

## 🔗 Related Notes

- [[Socat]]
- [[LinuxCommands/Nmap]]
- [[Anonymity Tools — VPN & Proxychains]]
- [[OSINT & Footprinting]]
- [[Privilege Escalation Techniques]]

---

_References: https://www.torproject.org · https://book.hacktricks.xyz · https://nymproject.org · Linux Basics for Hacking — OccupyTheWeb_