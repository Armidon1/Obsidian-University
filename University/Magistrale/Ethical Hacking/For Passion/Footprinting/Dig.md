# Using the `dig` Command

`dig` (Domain Information Groper) is a DNS lookup tool — essential for **network reconnaissance** in cybersecurity. It queries DNS servers to gather information about domains.

---

## Basic Syntax

```bash
dig [options] [domain] [record type]
```

---

## Common Usage Examples

### 1. Basic Domain Lookup (A record)

```bash
dig google.com
```

Returns the **IPv4 address** of the domain. The answer section is what matters most.

### 2. Query a Specific Record Type

```bash
dig google.com MX      # Mail servers
dig google.com NS      # Name servers
dig google.com TXT     # Text records (SPF, DMARC, etc.)
dig google.com AAAA    # IPv6 address
dig google.com CNAME   # Canonical name (alias)
dig google.com ANY     # All available records
```

### 3. Query a Specific DNS Server

```bash
dig @8.8.8.8 google.com      # Use Google's DNS
dig @1.1.1.1 google.com      # Use Cloudflare's DNS
```

Useful for comparing results or bypassing your default resolver.

### 4. Reverse DNS Lookup

```bash
dig -x 142.250.74.46
```

Resolves an **IP address back to a hostname** — great for recon.

### 5. Short / Clean Output

```bash
dig google.com +short
```

Prints only the answer — no extra noise.

### 6. Trace the Full DNS Path

```bash
dig google.com +trace
```

Shows every step from root servers down to the answer. Excellent for understanding how DNS resolution works.

### 7. Zone Transfer (AXFR) — Classic Recon Technique

```bash
dig @ns1.target.com target.com AXFR
```

Attempts to **dump all DNS records** from a nameserver. Most modern servers block this, but misconfigured ones still leak records — a goldmine in pentesting.

---

## Reading the Output

```
;; ANSWER SECTION:
google.com.     274    IN    A    142.250.74.46
```

|Field|Meaning|
|---|---|
|`google.com.`|Domain queried|
|`274`|TTL (seconds until cache expires)|
|`IN`|Internet class|
|`A`|Record type|
|`142.250.74.46`|The actual answer|

---

## Why It Matters in Hacking

|Use Case|What You're Looking For|
|---|---|
|**Recon**|Subdomains, mail servers, nameservers|
|**Footprinting**|IP ranges tied to a target org|
|**Misconfig hunting**|Open zone transfers (AXFR)|
|**Bypass detection**|Query external DNS to avoid local filtering|

---

## Pro Tip

Combine `dig` with tools like `nmap`, `whois`, and `fierce` for a full DNS reconnaissance workflow — exactly what OccupyTheWeb covers in the later chapters. Mastering `dig` first gives you a strong foundation for all of them.

[[Dig Example for FootPrinting]]