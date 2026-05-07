# Privoxy — Privacy Enhancing Proxy

#linux #cybersecurity #anonymity #networking #linux-basics-for-hackers

---

## 🗂️ Overview

**Privoxy** is a non-caching **HTTP/HTTPS proxy** with advanced filtering capabilities. Unlike a simple proxy, Privoxy can:

- Filter and modify web traffic in transit
- Block ads, trackers, and unwanted content
- Strip identifying headers from HTTP requests
- Route traffic through Tor or other proxies

In a cybersecurity context, Privoxy is most commonly used as a **bridge between HTTP applications and Tor** — because Tor speaks SOCKS5, but many tools and browsers only speak HTTP proxies.

```
Your Tool (HTTP) → Privoxy (HTTP→SOCKS5) → Tor (SOCKS5) → Internet
```

> [!info] Key Difference from Proxychains Proxychains works at the **system call level** — it intercepts network calls from any application. Privoxy works at the **HTTP protocol level** — it only handles HTTP/HTTPS traffic, but does so with much more control and filtering capability.

---

## 🛠️ Installation

```bash
sudo apt update
sudo apt install privoxy -y
```

### Start / Stop / Status

```bash
sudo systemctl start privoxy
sudo systemctl stop privoxy
sudo systemctl restart privoxy
sudo systemctl status privoxy
sudo systemctl enable privoxy       # start on boot
```

### Verify it's running

```bash
ss -tlnp | grep 8118                # privoxy listens on 8118 by default
curl -x http://127.0.0.1:8118 https://check.torproject.org/api/ip
```

---

## ⚙️ Configuration — config

The main config file is at `/etc/privoxy/config`.

```bash
sudo nano /etc/privoxy/config
```

### Key options

```bash
# Listening address and port (default)
listen-address  127.0.0.1:8118

# Forward ALL traffic through Tor (SOCKS5)
forward-socks5t / 127.0.0.1:9050 .

# Forward only .onion addresses through Tor
forward-socks5  .onion 127.0.0.1:9050 .

# Log level (0 = minimal, higher = more verbose)
debug 0

# Toggle filtering on/off
toggle 1

# Enable/disable filtering for specific actions
enable-remote-toggle 0
enable-edit-actions 0
```

> [!warning] The dot `.` at the end of `forward-socks5t / 127.0.0.1:9050 .` is **not a typo** — it tells Privoxy to not use a secondary proxy for the final hop. Removing it breaks the configuration.

> [!warning] After every edit to the config file, restart Privoxy:
> 
> ```bash
> sudo systemctl restart privoxy
> ```

---

## 🔗 Privoxy + Tor — The Standard Setup

This is the most common use case — combining Privoxy and Tor to route HTTP traffic anonymously.

### Architecture

```
Browser / Tool
      │  HTTP proxy: 127.0.0.1:8118
      ▼
  Privoxy (:8118)
      │  forwards via SOCKS5
      ▼
  Tor (:9050)
      │  3-hop onion routing
      ▼
  Exit Node → Internet
```

### Step 1 — Ensure both services are running

```bash
sudo systemctl start tor
sudo systemctl start privoxy
```

### Step 2 — Configure Privoxy to forward to Tor

```bash
sudo nano /etc/privoxy/config
```

Add or uncomment:

```
forward-socks5t / 127.0.0.1:9050 .
```

### Step 3 — Point your tool/browser to Privoxy

```bash
# HTTP proxy:  127.0.0.1:8118
# HTTPS proxy: 127.0.0.1:8118
```

### Step 4 — Verify

```bash
curl -x http://127.0.0.1:8118 https://api.ipify.org
# Should return a Tor exit node IP, not your real IP
```

---

## 🌐 Configuring Applications to Use Privoxy

### Browser (Firefox / Chromium)

```
Settings → Network → Manual proxy configuration
HTTP Proxy:  127.0.0.1   Port: 8118
HTTPS Proxy: 127.0.0.1   Port: 8118
```

### curl

```bash
curl -x http://127.0.0.1:8118 https://target.com
```

### wget

```bash
http_proxy=http://127.0.0.1:8118 wget https://target.com
```

### apt (system-wide)

```bash
sudo nano /etc/apt/apt.conf.d/proxy.conf
```

```
Acquire::http::Proxy "http://127.0.0.1:8118";
Acquire::https::Proxy "http://127.0.0.1:8118";
```

### Environment variables (affects most CLI tools)

```bash
export http_proxy=http://127.0.0.1:8118
export https_proxy=http://127.0.0.1:8118
export HTTP_PROXY=http://127.0.0.1:8118
export HTTPS_PROXY=http://127.0.0.1:8118
```

---

## 🧹 HTTP Header Filtering

One of Privoxy's unique features — it can **strip or modify HTTP headers** that reveal information about you.

### Headers Privoxy can remove or modify

|Header|What it reveals|
|---|---|
|`User-Agent`|Browser type, OS, version|
|`Referer`|Which page you came from|
|`X-Forwarded-For`|Your real IP (in chain proxies)|
|`Accept-Language`|Your language / locale|
|`Cookie`|Session identifiers|
|`Via`|That you're using a proxy|

### Configure header filtering

```bash
sudo nano /etc/privoxy/user.action
```

```bash
# Remove User-Agent
{+hide-user-agent{Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/115.0}}
/

# Remove Referer
{+hide-referrer{forge}}
/

# Block tracking scripts
{+block{Tracking pixel}}
.google-analytics.com
.doubleclick.net
```

---

## 🚫 Ad and Tracker Blocking

Privoxy can block ads and trackers **before they reach your browser** — at the proxy level.

```bash
sudo nano /etc/privoxy/user.action
```

```bash
# Block all requests to tracking domains
{+block{Advertisement}}
.ads.example.com
.tracker.com
.analytics.com
.doubleclick.net
.googlesyndication.com
```

This is more effective than browser extensions because it works **for all applications**, not just browsers.

---

## 🔐 Privoxy + Tor + Proxychains — Full Stack

For maximum coverage, combine all three:

```
Any tool
    │
    ├── HTTP tool → Privoxy → Tor
    └── Any tool  → Proxychains → Tor
```

```bash
# /etc/proxychains4.conf
socks5  127.0.0.1  9050     # direct to Tor

# Or chain through Privoxy first
http    127.0.0.1  8118     # through Privoxy → Tor
```

---

## 📊 Privoxy vs Proxychains vs Tor Browser

||Privoxy|Proxychains|Tor Browser|
|---|---|---|---|
|**Protocol**|HTTP/HTTPS only|Any (TCP)|HTTP/HTTPS|
|**Header filtering**|✅|❌|✅ (built-in)|
|**Ad blocking**|✅|❌|Partial|
|**Works with any app**|HTTP apps only|Any app|Browser only|
|**Tor integration**|✅ via forward|✅ direct|✅ built-in|
|**Complexity**|Medium|Low|Very Low|
|**Speed overhead**|Low|Low|High (Tor)|
|**Pre-installed**|No|Sometimes|No|

---

## ⚠️ Limitations

```
❌ Only handles HTTP/HTTPS — not raw TCP, UDP, or other protocols
❌ Does not encrypt traffic by itself — needs Tor or VPN for that
❌ If Tor goes down and forward is set, traffic may fail silently
❌ Not a replacement for Tor — it is a complement to it
```

> [!warning] DNS Leaks If Privoxy is configured incorrectly, DNS queries may bypass the proxy and reveal your activity to your ISP. Always use `forward-socks5t` (with the `t`) — the `t` tells Privoxy to resolve DNS **through** the SOCKS5 proxy (Tor), not locally.
> 
> ```
> forward-socks5t / 127.0.0.1:9050 .   ← correct, DNS through Tor
> forward-socks5  / 127.0.0.1:9050 .   ← DNS resolved locally = leak
> ```

---

## 🔗 Command Cheat Sheet

```bash
# Install and manage
sudo apt install privoxy -y
sudo systemctl start privoxy
sudo systemctl restart privoxy
sudo systemctl status privoxy

# Config file
sudo nano /etc/privoxy/config

# Key config line — forward all HTTP through Tor
forward-socks5t / 127.0.0.1:9050 .

# Verify it works
curl -x http://127.0.0.1:8118 https://api.ipify.org

# Use with curl
curl -x http://127.0.0.1:8118 https://target.com

# Use with wget
http_proxy=http://127.0.0.1:8118 wget https://target.com

# Set globally for session
export http_proxy=http://127.0.0.1:8118
export https_proxy=http://127.0.0.1:8118

# Check listening port
ss -tlnp | grep 8118
```

---

## 🔗 Related Notes

- [[Tor]]
- [[Netcat]]
- [[Socat]]
- [[Anonymity Tools — VPN & Proxychains]]
- [[Obsidian-University/University/Magistrale/Ethical Hacking/For Passion/Scanning/Nmap]]

---

_References: https://www.privoxy.org/user-manual · https://book.hacktricks.xyz · Linux Basics for Hacking — OccupyTheWeb_