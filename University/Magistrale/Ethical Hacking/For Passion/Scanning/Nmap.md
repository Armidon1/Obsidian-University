# Nmap — Network Mapper

#linux #cybersecurity #reconnaissance #networking #linux-basics-for-hackers

---

## 🗂️ Overview

**Nmap** (Network Mapper) is the industry-standard tool for **network reconnaissance**. It discovers hosts, open ports, running services, OS versions, and known vulnerabilities. It is almost always the **first active tool** used in a penetration test.

> [!warning] Legal Reminder Only run Nmap against systems you own or have **explicit written authorization** to test. Unauthorized scanning is illegal in most countries. Use HackTheBox or TryHackMe to practice safely.

---

## 🖥️ Host Discovery

Find which hosts are **alive** on a network before scanning ports.

```bash
nmap -sn 192.168.0.0/24          # scan all hosts in subnet (no port scan)
nmap -sn 192.168.0.1-50          # scan IP range
nmap -sn 192.168.0.1,5,10        # scan specific IPs
nmap 192.168.0.104                # scan single host
nmap -sn 192.168.0.0/24 --open   # show only hosts that responded
```

> [!tip] Hacking Note `-sn` (ping scan) sends ICMP echo requests without touching ports — fast and relatively quiet. It gives you a **map of live targets** before you start scanning ports.

---

## 🚪 Port Scanning

Discover which **ports are open** on a target.

```bash
nmap 192.168.0.102                # scan most common 1000 ports
nmap -p 80 192.168.0.102          # scan specific port
nmap -p 80,443,22 192.168.0.102   # scan multiple ports
nmap -p 1-65535 192.168.0.102     # scan all ports
nmap -p- 192.168.0.102            # shorthand for all ports
nmap -p 1-1024 192.168.0.102      # scan well-known ports only
nmap --top-ports 100 192.168.0.102 # scan top 100 most common ports
```

### Port States

|State|Meaning|
|---|---|
|`open`|Port is accepting connections — **interesting**|
|`closed`|Port is reachable but nothing is listening|
|`filtered`|Firewall is blocking — no response|
|`unfiltered`|Reachable but state is unclear (ACK scan)|
|`open\|filtered`|Can't tell — common in UDP scans|

---

## 🔬 Scan Types

Different TCP/UDP techniques with different **stealth and accuracy tradeoffs**.

```bash
nmap -sS 192.168.0.102            # SYN scan (stealth, requires sudo)
nmap -sT 192.168.0.102            # TCP connect scan (no sudo needed)
nmap -sU 192.168.0.102            # UDP scan
nmap -sA 192.168.0.102            # ACK scan (detect firewalls)
nmap -sN 192.168.0.102            # NULL scan (no flags set)
nmap -sF 192.168.0.102            # FIN scan
nmap -sX 192.168.0.102            # Xmas scan (FIN+PSH+URG flags)
```

### How They Work

|Scan|Sends|Open Response|Stealth|Needs Root|
|---|---|---|---|---|
|`-sS` SYN|SYN|SYN-ACK (then RST)|⭐⭐⭐ High|Yes|
|`-sT` TCP|SYN|Full handshake|⭐ Low|No|
|`-sU` UDP|UDP packet|No response|⭐⭐ Medium|Yes|
|`-sA` ACK|ACK|RST|⭐⭐ Medium|Yes|
|`-sN` NULL|Nothing|Silence|⭐⭐⭐ High|Yes|
|`-sF` FIN|FIN|Silence|⭐⭐⭐ High|Yes|
|`-sX` Xmas|FIN+PSH+URG|Silence|⭐⭐⭐ High|Yes|

> [!tip] Hacking Note **`-sS` is the default** when running as root and the most commonly used — it never completes the TCP handshake, so it's less likely to be logged by the target. **`-sT`** is what you use when you don't have root but leaves a full connection in logs.

> [!info] UDP Scan `-sU` is **slow** (no response = filtered or open) and often skipped, but critical services like DNS (53), SNMP (161), and DHCP (67/68) run on UDP — don't ignore it entirely.

---

## 🔎 Service and OS Detection

Identify **what** is running on open ports and **which OS** the target is using.

```bash
nmap -sV 192.168.0.102            # detect service versions on open ports
nmap -O 192.168.0.102             # detect operating system
nmap -A 192.168.0.102             # aggressive: OS + versions + scripts + traceroute
nmap -sV --version-intensity 9 192.168.0.102  # maximum version detection effort
```

### Example `-sV` Output

```
PORT    STATE  SERVICE  VERSION
22/tcp  open   ssh      OpenSSH 8.2p1 Ubuntu 4ubuntu0.5
80/tcp  open   http     Apache httpd 2.4.41
443/tcp open   ssl/http Apache httpd 2.4.41
3306/tcp open  mysql    MySQL 5.7.39
```

> [!tip] Hacking Note Service versions are **critical**. Once you know `Apache 2.4.41` or `OpenSSH 8.2p1`, you can search for CVEs directly:
> 
> ```bash
> searchsploit Apache 2.4.41
> searchsploit OpenSSH 8.2
> ```

---

## ⏱️ Speed Control

Control how fast Nmap scans — tradeoff between **speed** and **stealth**.

```bash
nmap -T0 192.168.0.102            # paranoid  — very slow, IDS evasion
nmap -T1 192.168.0.102            # sneaky    — slow, IDS evasion
nmap -T2 192.168.0.102            # polite    — slows down to reduce bandwidth
nmap -T3 192.168.0.102            # normal    — default
nmap -T4 192.168.0.102            # aggressive — faster, assumes good network
nmap -T5 192.168.0.102            # insane    — very fast, very noisy
```

|Template|Speed|Stealth|Use Case|
|---|---|---|---|
|`-T0` Paranoid|⚫ Slowest|⭐⭐⭐⭐⭐|Evading advanced IDS|
|`-T1` Sneaky|🔴 Very slow|⭐⭐⭐⭐|Evading most IDS|
|`-T2` Polite|🟠 Slow|⭐⭐⭐|Sensitive networks|
|`-T3` Normal|🟡 Medium|⭐⭐|Default, everyday use|
|`-T4` Aggressive|🟢 Fast|⭐|CTFs, trusted networks|
|`-T5` Insane|⚡ Fastest|❌|Lab environments only|

> [!warning] `-T5` can **crash unstable services** or **flood network devices**. Never use it on production systems or real targets.

---

## 📜 NSE Scripts — Nmap Scripting Engine

NSE scripts extend Nmap with **automation and vulnerability detection**. Scripts are located in `/usr/share/nmap/scripts/`.

```bash
nmap --script vuln 192.168.0.102          # scan for known vulnerabilities
nmap --script http-enum 192.168.0.102     # enumerate web directories
nmap --script smb-vuln* 192.168.0.102     # SMB vulnerabilities
nmap --script default 192.168.0.102       # run default scripts (same as -sC)
nmap -sC 192.168.0.102                    # shorthand for --script default
nmap --script ftp-anon 192.168.0.102      # check for anonymous FTP login
nmap --script ssh-brute 192.168.0.102     # SSH brute force
nmap --script http-title 192.168.0.102    # grab HTTP page titles
nmap --script banner 192.168.0.102        # grab service banners
```

### Script Categories

|Category|What It Does|
|---|---|
|`default`|Safe, commonly useful scripts (also `-sC`)|
|`vuln`|Check for known vulnerabilities|
|`auth`|Test authentication bypasses|
|`brute`|Brute-force credentials|
|`discovery`|Extra enumeration and info gathering|
|`exploit`|Actively exploit vulnerabilities|
|`safe`|Non-intrusive scripts|
|`intrusive`|May crash or affect the target|

```bash
# List all scripts in a category
ls /usr/share/nmap/scripts/ | grep smb
ls /usr/share/nmap/scripts/ | grep http

# Get help on a specific script
nmap --script-help http-enum
```

> [!warning] `--script exploit` and `--script intrusive` can **actively attack** and potentially crash services. Use only in authorized engagements or labs.

---

## 💾 Output Formats

Always save your scan results — you'll refer back to them constantly.

```bash
nmap -oN output.txt 192.168.0.102         # normal text (human readable)
nmap -oX output.xml 192.168.0.102         # XML (for tools like Metasploit)
nmap -oG output.gnmap 192.168.0.102       # greppable format
nmap -oA output 192.168.0.102             # save ALL formats at once ← recommended
```

### Greppable Output in Action

```bash
nmap -oG output.gnmap 192.168.0.0/24
grep "open" output.gnmap                  # extract all hosts with open ports
grep "80/open" output.gnmap               # find all hosts with port 80 open
```

> [!tip] Hacking Note Always use `-oA` on real engagements. You never know what you'll need to parse later — XML output can be imported directly into **Metasploit** (`db_import`), **Faraday**, and other frameworks.

---

## ⚙️ Other Useful Flags

```bash
nmap -v 192.168.0.102                     # verbose output
nmap -vv 192.168.0.102                    # very verbose
nmap -d 192.168.0.102                     # debug mode
nmap --open 192.168.0.102                 # show only open ports
nmap -n 192.168.0.102                     # no DNS resolution (faster)
nmap -R 192.168.0.102                     # always do DNS resolution
nmap --reason 192.168.0.102               # show why a port has its state
nmap -6 fe80::1                           # scan IPv6 address
nmap --exclude 192.168.0.1 192.168.0.0/24 # exclude specific host
nmap -iL targets.txt                      # read targets from a file
```

---

## 🔗 Common Combinations

```bash
# Full stealth scan — all ports, service detection, OS detection
sudo nmap -sS -sV -O -p- 192.168.0.102

# Aggressive scan on whole subnet
sudo nmap -A -T4 192.168.0.0/24

# Stealthy vulnerability scan
sudo nmap -sS -T2 --script vuln 192.168.0.102

# Full scan with all output formats saved
sudo nmap -sS -sV -sC -O -p- -oA full_scan 192.168.0.102

# Quick top-100 ports scan on a subnet
nmap --top-ports 100 -T4 192.168.0.0/24

# CTF standard scan (fast, comprehensive)
sudo nmap -A -T4 -p- 192.168.0.102
```

---

## 🗺️ The Progression in a Real Pentest

Each step builds on the previous — this is exactly the **reconnaissance phase** of a penetration test.

```bash
# Step 1 — Who is on the network?
nmap -sn 192.168.0.0/24

# Step 2 — What ports are open on the target?
nmap -p- 192.168.0.102

# Step 3 — What services are running on those ports?
nmap -sV -p 22,80,443 192.168.0.102

# Step 4 — What OS is the target running?
nmap -O 192.168.0.102

# Step 5 — Are there any known vulnerabilities?
nmap --script vuln 192.168.0.102
```

```
Host discovery → Port scan → Service detection → OS detection → Vuln scan
      │                │               │                │              │
  Who's alive?   What's open?   What's running?   What OS?    Any CVEs?
```

---

## 🔗 Command Cheat Sheet

```bash
# Host discovery
nmap -sn 192.168.0.0/24                               # ping sweep
nmap -sn 192.168.0.1-50                               # range sweep

# Port scanning
nmap 192.168.0.102                                    # top 1000 ports
nmap -p- 192.168.0.102                                # all 65535 ports
nmap -p 22,80,443 192.168.0.102                       # specific ports
nmap --top-ports 100 192.168.0.102                    # top 100 ports

# Scan types
sudo nmap -sS 192.168.0.102                           # SYN (stealth)
nmap -sT 192.168.0.102                                # TCP connect
sudo nmap -sU 192.168.0.102                           # UDP

# Detection
nmap -sV 192.168.0.102                                # service versions
sudo nmap -O 192.168.0.102                            # OS detection
sudo nmap -A 192.168.0.102                            # all-in-one aggressive

# Scripts
nmap -sC 192.168.0.102                                # default scripts
nmap --script vuln 192.168.0.102                      # vuln scan
nmap --script smb-vuln* 192.168.0.102                 # SMB vulns

# Speed
nmap -T2 192.168.0.102                                # polite (stealthy)
nmap -T4 192.168.0.102                                # aggressive (fast)

# Output
nmap -oA scan_results 192.168.0.102                   # all formats
nmap -oN output.txt 192.168.0.102                     # normal text

# Combinations
sudo nmap -sS -sV -sC -O -p- -oA full 192.168.0.102   # full pentest scan
sudo nmap -sS -T2 --script vuln -oA vuln 192.168.0.102 # stealthy vuln scan
```

---
## ARP Scanning

It also supports arp scanning with the `-PR` flag. for instance:
```bash
nmap -sn -PR 192.168.1.0/24
```
Simply does an ARP Scan of that specific subnet. Also the `-sn` flag simply blocks the port scanning, in this way nmap is being used just for host discovery. 

---
## Nmap `-f` — Packet Fragmentation

The `-f` flag tells Nmap to **split packets into tiny fragments** before sending them. The idea is that many firewalls and IDS reassemble packets before inspecting them — but older or misconfigured ones inspect each fragment individually and fail to recognize the scan.

### How it works

A normal SYN packet has a TCP header of **20 bytes**. With `-f`, Nmap splits the TCP header across multiple IP fragments of **8 bytes each**:

```
# Normal SYN packet
[ IP header | TCP header (20 bytes) | data ]

# With -f  (8-byte fragments)
Fragment 1:  [ IP header | TCP bytes  1-8  ]
Fragment 2:  [ IP header | TCP bytes  9-16 ]
Fragment 3:  [ IP header | TCP bytes 17-20 ]

# With -ff (16-byte fragments)
Fragment 1:  [ IP header | TCP bytes  1-16 ]
Fragment 2:  [ IP header | TCP bytes 17-20 ]
```

The target's OS **reassembles** the fragments back into the full packet before processing — so the scan works exactly the same from the target's perspective. The difference is only in what the network sees in transit.

### Variants

|Flag|Fragment size|Notes|
|---|---|---|
|`-f`|8 bytes|Maximum fragmentation|
|`-ff`|16 bytes|Less fragments, slightly faster|
|`--mtu <value>`|Custom (must be multiple of 8)|Full control, e.g. `--mtu 24`|

### What it evades

- **Stateless packet filters** that inspect single packets without reassembling — they see a fragment with no recognizable TCP flags and let it through
- **Older IDS signatures** that pattern-match on complete headers
- **Some older firewalls** that don't do fragment reassembly before applying rules

### What it does NOT evade

- **Stateful firewalls** (any modern firewall) — they reassemble fragments before inspection, exactly like the target OS does
- **Modern IDS/IPS** (Snort, Suricata) — they have fragment reassembly built in
- **Rate-based detection** — fragmentation doesn't hide the volume of packets

### Important caveat

Requires **root**, because it involves crafting raw IP packets. Also some network devices and older routers **drop fragmented packets** entirely, which can make your scan unreliable rather than stealthy.

### Combine with other flags

```bash
# Fragmented SYN scan
sudo nmap -sS -f <target>

# Fragmented + decoy (stack evasion techniques)
sudo nmap -sS -f -D RND:5 <target>

# Custom MTU
sudo nmap -sS --mtu 16 <target>
```

In practice, `-f` is mostly a historical technique — it was very effective in the late 90s/early 2000s against early firewalls and IDS. Against any modern infrastructure it's largely irrelevant, but it's still worth knowing for the exam since Hacking Exposed covers it and it illustrates the broader concept of **evasion through obfuscation at the packet level**.

---
## Nmap `-D` — Decoy Scan

The `-D` flag lets you **mix your real IP with a list of fake IPs (decoys)** in the scan traffic. The target sees SYN packets arriving from multiple sources simultaneously — it can't easily tell which one is the real attacker.

### How it works

Without `-D`, every probe packet has your real IP as the source:

```
Your IP  ──── SYN ────► Target
```

With `-D RND:5`, Nmap generates 5 random fake IPs and interleaves them with your real probes:

```
1.2.3.4   ──── SYN ────► Target  (decoy — fake)
9.8.7.6   ──── SYN ────► Target  (decoy — fake)
YOUR IP   ──── SYN ────► Target  (real probe)
5.5.5.5   ──── SYN ────► Target  (decoy — fake)
3.1.4.1   ──── SYN ────► Target  (decoy — fake)
```

The target sees all of them and **responds to all of them** — including the real SYN-ACKs back to you. From the target's logs, it looks like 6 different hosts are scanning simultaneously.

### Syntax variants

```bash
# Random decoys — Nmap picks the fake IPs
sudo nmap -sS -D RND:10 <target>

# Manual decoys — you specify them
sudo nmap -sS -D 1.2.3.4,5.6.7.8,9.10.11.12 <target>

# Manual decoys with ME to control your position in the list
sudo nmap -sS -D 1.2.3.4,ME,9.10.11.12 <target>

# Combine with fragmentation
sudo nmap -sS -f -D RND:5 <target>
```

`ME` explicitly places your real IP at a specific position in the decoy list. If you omit `ME`, Nmap inserts your real IP at a random position.

### The critical limitation

Nmap **crafts the SYN packets with spoofed source IPs**, but it **cannot receive the SYN-ACKs** that the target sends back to the decoys — those go to the fake IPs, which either don't exist or belong to random machines on the internet.

Your real IP is still the only one that **actually receives responses** and drives the scan logic. This means:

```
Target ──── SYN-ACK ────► 1.2.3.4    (decoy — packet goes nowhere / random host)
Target ──── SYN-ACK ────► YOUR IP    (you receive this — scan proceeds)
Target ──── SYN-ACK ────► 5.6.7.8    (decoy — same as above)
```

### What this does and doesn't hide

| |Result|
|---|---|
|Your IP in the target's logs|Still there — buried among decoys|
|Identifying which IP is real|Harder, but not impossible|
|Traffic actually sent by you|Detectable via upstream router logs|
|Effectiveness against simple log review|Good — analyst sees 10+ IPs, unclear which is real|
|Effectiveness against network forensics|Weak — ISP/router logs show only your real traffic|

### How the real IP can still be identified

A skilled analyst can narrow it down because **only your real IP receives the SYN-ACK responses**. If they correlate outbound SYN packets from the target with inbound traffic on your network, the decoys disappear — they never sent anything, so they never received anything either.

Also, if any of your randomly generated decoy IPs happen to be **unreachable or unroutable**, the target's router may generate ICMP errors that expose the scan pattern.

### Relationship to Idle Scan `-sI`

The `-D` flag is a **best-effort anonymity** technique — your IP is still in the traffic. The Idle scan (`-sI`) is the **true anonymity** solution: your IP never appears at all, because the zombie sends all the packets on your behalf. Think of `-D` as "hiding in a crowd" and `-sI` as "sending someone else to do it."

| |`-D` decoy|`-sI` idle|
|---|---|---|
|Your IP in target logs|Yes (hidden among others)|Never|
|Requires zombie host|No|Yes|
|Complexity|Low|High|
|True anonymity|No|Yes|
Great catch — this is exactly the right question to ask.

### Decoys hit the **same ports**, at the **same time**

For every single port probe, Nmap sends **one packet per decoy + one real packet**, all to the **same destination port**, in rapid succession:

```
# Nmap is probing port 80:

1.2.3.4  ──── SYN → port 80 ────► Target
9.8.7.6  ──── SYN → port 80 ────► Target
TUO IP   ──── SYN → port 80 ────► Target   ← real probe
5.5.5.5  ──── SYN → port 80 ────► Target
3.1.4.1  ──── SYN → port 80 ────► Target

# Then Nmap moves to port 443:

1.2.3.4  ──── SYN → port 443 ───► Target
9.8.7.6  ──── SYN → port 443 ───► Target
TUO IP   ──── SYN → port 443 ───► Target   ← real probe
...
```

So from the target's logs it looks like **6 hosts all scanning the exact same ports at the exact same moment** — which is already suspicious, but it's hard to tell who's the "real" one just from the port pattern.

### Your intuition is correct though

You're right that the real IP is "doing the real scan" — but an analyst looking **only at the target's logs** can't distinguish it, because:

- All IPs hit identical ports
- All IPs arrive at nearly identical timestamps
- All IPs use the same packet structure

The way to unmask the real IP is **not** by looking at port patterns — it's by looking at **who received SYN-ACKs back**:

```
Target ──── SYN-ACK → port 80 ────► 1.2.3.4   → this host responds RST
                                                  (got an unexpected SYN-ACK)
Target ──── SYN-ACK → port 80 ────► TUO IP    → you receive it, scan proceeds
Target ──── SYN-ACK → port 80 ────► 5.5.5.5   → this host responds RST
                                                  (same situation)
```

The decoy machines, if they exist and are online, receive unsolicited SYN-ACKs and their kernels **automatically fire back RST** — they never sent a SYN, so the SYN-ACK makes no sense to them. Only your machine silently absorbs the SYN-ACK and uses it.

An analyst with access to broader network traffic (not just the target's logs) can spot: _"all these IPs sent SYNs, but only one of them didn't fire back RSTs in response to the SYN-ACKs"_ — and that's you.


---
See also [[Nmap scan types]]
---
## 🔗 Related Notes

- [[Finding_Files]]
- [[Privilege Escalation Techniques]]
- [[Enumeration & Footprinting]]
- [[Metasploit Framework]]
- [[DNS Reconnaissance — dig]]

---

_References: https://nmap.org/book · https://book.hacktricks.xyz · Linux Basics for Hacking — OccupyTheWeb_