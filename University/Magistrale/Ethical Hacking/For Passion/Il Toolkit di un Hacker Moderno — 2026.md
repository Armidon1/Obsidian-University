# Il Toolkit di un Hacker Moderno — 2026

### La mentalità prima degli strumenti

Un hacker moderno non ha un "toolkit fisso" — ha una **metodologia**. Gli strumenti cambiano, la metodologia no:

```
Reconnaissance → Scanning → Exploitation → Post-Exploitation → Reporting
```

---

### 🔍 Reconnaissance (Passiva)

Nessun contatto con il target — solo fonti pubbliche.

|Tool|Cosa fa|
|---|---|
|**crt.sh**|Certificate Transparency → sottodomini|
|**Shodan**|Dispositivi, porte, versioni software esposte|
|**GHDB / Google Dorks**|File e directory sensibili via motori di ricerca|
|**WiGLE**|Mappa reti Wi-Fi fisiche|
|**theHarvester**|Email, sottodomini, IP da fonti OSINT|
|**Maltego**|Grafo visuale di relazioni tra entità|
|**OSINT Framework**|Raccolta link a tool OSINT categorizzati|
|**Recon-ng**|Framework modulare per OSINT automatizzato|

---

### 📡 Scanning (Attiva)

Primo contatto diretto con il target — richiede autorizzazione.

|Tool|Cosa fa|
|---|---|
|**nmap**|Port scanning, service detection, OS detection|
|**masscan**|Port scanning ultraveloce su larga scala|
|**nikto**|Vulnerability scanner per web server|
|**gobuster / ffuf**|Directory e file brute-force su web app|
|**wpscan**|Scanner specifico per WordPress|
|**subfinder / amass**|Enumerazione sottodomini attiva|

---

### 💥 Exploitation

|Tool|Cosa fa|
|---|---|
|**Metasploit**|Framework exploit — il più usato in assoluto|
|**sqlmap**|SQL injection automatizzata|
|**Burp Suite**|Intercept/modifica HTTP — standard per web app|
|**John the Ripper**|Password cracking|
|**Hashcat**|Password cracking GPU-accelerated — più veloce di John|
|**Hydra**|Brute force su servizi di rete (SSH, FTP, HTTP...)|
|**CrackMapExec**|Attacchi su reti Windows/Active Directory|

---

### 🏠 Post-Exploitation

Una volta dentro — privilege escalation, persistenza, lateral movement.

|Tool|Cosa fa|
|---|---|
|**LinPEAS / WinPEAS**|Enumerazione automatica per privesc|
|**BloodHound**|Mappa Active Directory → trova path verso Domain Admin|
|**Mimikatz**|Estrae credenziali da memoria Windows|
|**netcat / socat**|Reverse shell, pivoting|
|**Chisel / ligolo-ng**|Tunneling e pivoting moderno|
|**pspy**|Monitora processi senza root|

---

### 🕵️ Anonimità

|Tool|Cosa fa|
|---|---|
|**Tor + Proxychains**|Routing anonimo del traffico|
|**Privoxy**|Bridge HTTP → SOCKS5 verso Tor|
|**VPN no-log**|Primo layer di anonimizzazione|

---

### 🖥️ Ambienti

Un hacker moderno non lavora sul proprio PC — usa ambienti dedicati:

```
Kali Linux     → distro standard, tutto pre-installato
Parrot OS      → alternativa più leggera, ottima per OSINT
Black Arch     → per chi vuole ancora più tool
VM isolate     → ogni engagement in una VM fresca
```

---

### 🤖 AI nel 2026 — la novità

Questa è la vera differenza rispetto a 5 anni fa:

```
ChatGPT / Claude   → generare payload, spiegare codice,
                     scrivere script personalizzati

GitHub Copilot     → scrivere exploit e tool custom

Burp AI extensions → analisi automatica delle vulnerabilità

LLM per OSINT      → correlazione automatica di dati pubblici
```

> I pentester moderni usano AI per **accelerare** il lavoro manuale — generare varianti di payload, deobfuscare codice, scrivere report. Non sostituisce la conoscenza, la amplifica.

---

### La vera risposta

> Un hacker moderno non si distingue per **quanti tool conosce** — si distingue per **quanto capisce quello che sta facendo**.

Chiunque può lanciare `metasploit` o `sqlmap`. Pochissimi capiscono perché un exploit funziona, cosa sta succedendo a livello di protocollo, e come adattarsi quando gli strumenti automatici falliscono.

Quello che stai facendo tu — studiare `dig`, `chmod`, `find`, `netcat` dalla base — è esattamente il percorso giusto. I tool automatici vengono dopo.

# Modern Toolkit

This is the most useful mapping for your studies:

| Cain & Abel Feature (OLD)                   | Modern Replacement                                                  |
| ------------------------------------------- | ------------------------------------------------------------------- |
| **Hash cracking** (dictionary, brute force) | **Hashcat** (GPU-accelerated), **John the Ripper**                  |
| **Rainbow tables**                          | **RainbowCrack**, but mostly obsolete due to salting + GPU cracking |
| **Network sniffing**                        | **Wireshark** (gold standard), **tcpdump**                          |
| **ARP spoofing / MITM**                     | **Bettercap** (modern), **Ettercap**, **arpspoof**                  |
| **Credential extraction from memory**       | **Mimikatz**, **LaZagne**                                           |
| **Browser password recovery**               | **LaZagne**                                                         |
| **Wireless key recovery**                   | **Aircrack-ng** suite                                               |
| **VoIP sniffing**                           | **Wireshark + RTP decoder**, **UCSniff**                            |
| **Hash dumping from SAM**                   | **secretsdump.py** (Impacket), **mimikatz**                         |
| **Cisco password decoding**                 | Online decoders, **John the Ripper**                                |
| **Route table / network utilities**         | Built-in OS tools, **nmap**, **Wireshark**                          |


For **real engagements**:

```
2026 pentester reality:
─────────────────────────────────────
Wireshark      ← packet capture
Bettercap      ← MITM / ARP
mimikatz       ← Windows credentials
Hashcat        ← cracking
Impacket suite ← AD attacks
Responder      ← network credential capture
NetExec        ← lateral movement
```

---

## A Note on Responder

One tool worth knowing that essentially **replaced Cain's network sniffing role**: **Responder** by Laurent Gaffié.

```python
# Responder workflow (modern equivalent of Cain's sniffer)
sudo responder -I eth0 -wd

# Listens for LLMNR/NBT-NS/MDNS poisoning opportunities
# Captures NetNTLMv2 hashes from misconfigured Windows clients
# Then feed those hashes to hashcat
```

This is probably the **single most useful tool for network-level credential capture in 2026** — and it does what Cain's sniffer tried to do, but actually works on modern networks.

---
