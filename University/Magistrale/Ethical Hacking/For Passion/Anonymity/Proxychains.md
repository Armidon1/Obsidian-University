# Proxychains

## Cos'è

Proxychains è un tool che **intercetta le chiamate di rete** di qualsiasi programma a livello di sistema operativo e le forza attraverso uno o più proxy, senza che il programma sappia nulla.

Non è un servizio — è un **wrapper**. Si usa prependendolo al comando che si vuole anonimizzare.

---

## Come funziona

Proxychains aggancia le syscall di rete del processo tramite `LD_PRELOAD`, reindirizzandole attraverso il proxy configurato prima che raggiungano la rete reale.

```
proxychains [tool] → Tor (:9050) → Internet
```

Il tool non sa di passare per un proxy — proxychains lo fa in modo trasparente.

---

## Differenza con Privoxy

||Proxychains|Privoxy|
|---|---|---|
|Come funziona|Intercetta syscall di rete|Proxy HTTP separato|
|Il tool deve supportare proxy?|No, è trasparente|Sì (HTTP proxy)|
|Configurazione|`/etc/proxychains.conf`|`/etc/privoxy/config`|
|Uso tipico|Qualsiasi tool (nmap, curl, ecc.)|Browser, tool HTTP-aware|
|Avvio|Wrapper (non è un servizio)|Servizio (`systemctl start privoxy`)|

---

## Configurazione

File di configurazione: `/etc/proxychains.conf`

```ini
# Modalità (strict_chain, dynamic_chain, random_chain)
strict_chain

# Proxy DNS attraverso la catena (evita DNS leak)
proxy_dns

[ProxyList]
socks5  127.0.0.1  9050   # Tor
```

### Modalità

|Modalità|Comportamento|
|---|---|
|`strict_chain`|Tutti i proxy devono funzionare, in ordine|
|`dynamic_chain`|Salta i proxy non disponibili|
|`random_chain`|Ordine casuale ad ogni connessione|

---

## Utilizzo

Non è un servizio in background — si prepende al comando:

```bash
proxychains curl https://example.com
proxychains nmap -sT -Pn target.com
proxychains firefox
```

**Importante:** Tor deve essere avviato prima:

```bash
sudo systemctl start tor
proxychains [comando]
```

---

## Proxy chaining

Puoi concatenare più proxy nel `ProxyList` per aumentare l'anonimato:

```ini
[ProxyList]
socks5  127.0.0.1  9050    # Tor
socks5  proxy2.example.com 1080    # Secondo proxy
http    proxy3.example.com 8080    # Terzo proxy
```

Ogni nodo conosce solo quello prima e quello dopo — il target vede solo l'ultimo proxy della catena.

---

## Limitazioni

- **Lento** — ogni hop aggiunge latenza
- **No UDP** — proxychains supporta solo TCP (Tor stesso non supporta UDP)
- **No raw socket** — nmap in SYN scan (`-sS`) non funziona, usare `-sT` (TCP connect)
- **Google blocca Tor** — CAPTCHA continui se si usa Google attraverso Tor

---

## Nel footprinting / pentest

```bash
# Scansione anonima con nmap
proxychains nmap -sT -Pn target.com

# Curl anonimo
proxychains curl https://target.com

# Browser anonimo
proxychains firefox
```

⚠️ Per ricerche OSINT su fonti pubbliche l'anonimato non è strettamente necessario. Proxychains è utile quando non si vuole che il target rilevi la scansione nei suoi log.

---

## Architettura completa con Tor e Privoxy

```
Tool HTTP-aware → Privoxy (:8118) → Tor (:9050) → Internet
Qualsiasi tool  → Proxychains      → Tor (:9050) → Internet
```

---

## Related Notes

- [[Privoxy]]
- [[Tor]]
- [[Traceroute]]
- [[Obsidian-University/University/Magistrale/Ethical Hacking/For Passion/Scanning/Nmap]]
- [[OSINT & Footprinting]]

---

_References: man proxychains · https://github.com/haad/proxychains · Linux Basics for Hacking — OccupyTheWeb_