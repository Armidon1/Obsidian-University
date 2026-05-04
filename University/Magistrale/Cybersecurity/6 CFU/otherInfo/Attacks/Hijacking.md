# Hijacking — Tecniche di Dirottamento

#linux #cybersecurity #osint #networking #linux-basics-for-hackers

---

## 🗂️ Overview

**Hijacking** (dirottamento) è una categoria di attacchi in cui un attaccante prende il controllo di qualcosa che appartiene a qualcun altro — una sessione, un dominio, un DNS, una connessione di rete, o un browser.

Il termine copre tecniche molto diverse tra loro, accomunate dall'idea di **interporsi** tra due parti o **prendere il controllo** di una risorsa altrui.

```
Legittimo:   Utente A ←→ Server
                │
                │ attaccante si interpone
                ▼
Hijacking:   Utente A ←→ Attaccante ←→ Server
             (o Attaccante prende il posto di Utente A)
```

---

## 🌐 1. Domain Hijacking

Il Domain Hijacking è la presa di controllo di un dominio altrui — il dominio viene sottratto al legittimo proprietario.

### Come avviene

**Via scadenza del dominio:**

```
Il proprietario dimentica di rinnovare example.com
        │
        ▼
Grace Period (30gg)   → può ancora rinnovare
Redemption (30gg)     → solo con penale elevata
Released              → chiunque può registrarlo
        │
        ▼
L'attaccante lo registra immediatamente
→ eredita reputazione email, link, storico SEO
→ può ricevere email destinate all'organizzazione
→ può reindirizzare il sito a contenuti malevoli
```

**Via compromissione del Registrar:**

```
L'attaccante accede all'account del Registrar
(phishing delle credenziali, password debole,
 MFA non attivato)
        │
        ▼
Cambia i nameserver del dominio
→ tutto il traffico va ai server dell'attaccante
→ può intercettare email, credenziali, sessioni
```

**Via social engineering al Registrar:**

```
L'attaccante chiama il supporto del Registrar
finge di essere il proprietario
convinces il supporto a trasferire il dominio
```

### Come difendersi

```bash
# Controlla la scadenza dei tuoi domini
whois tuodominio.com | grep -i "expir"

# Attiva il Domain Lock (Registrar Lock)
# → impedisce trasferimenti non autorizzati
# → deve essere disattivato manualmente per trasferire

# Attiva MFA sull'account Registrar
# → GoDaddy, Aruba, Namecheap supportano tutti 2FA

# Monitora i tuoi domini
# → servizi come DomainTools Alert, SecurityTrails
```

---

## 🔀 2. DNS Hijacking

Il DNS Hijacking reindirizza le query DNS verso server controllati dall'attaccante — l'utente digita il dominio corretto ma finisce su un server malevolo.

### Tipi di DNS Hijacking

**Local DNS Hijacking:**

```
Malware modifica il file /etc/resolv.conf
o le impostazioni DNS del router
        │
        ▼
Tutte le query DNS passano per il server
dell'attaccante → risponde con IP falsi
```

**Router DNS Hijacking:**

```
L'attaccante accede al router (password di default)
Cambia i DNS del router in quelli malevoli
        │
        ▼
Tutti i dispositivi della rete usano i DNS malevoli
→ attacco silenzioso e invisibile all'utente
```

**DNS Cache Poisoning:**

```
L'attaccante inietta record DNS falsi
nella cache del resolver
        │
        ▼
Tutti gli utenti che usano quel resolver
vengono reindirizzati al sito malevolo
fino allo scadere del TTL
```

**Rogue DNS Server:**

```
L'attaccante risponde alle query DNS
prima del server legittimo (race condition)
→ tecnica avanzata, richiede posizione
  privilegiata nella rete
```

### Come vederlo

```bash
# Verifica i tuoi DNS attuali
cat /etc/resolv.conf

# Confronta la risposta di DNS diversi
dig example.com @8.8.8.8 +short      # Google DNS
dig example.com @1.1.1.1 +short      # Cloudflare DNS
dig example.com @resolver_locale +short

# Se le risposte differiscono → possibile hijacking

# Controlla il DNS del router
ip route | grep default
# → trova l'IP del gateway (router)
# poi naviga su http://IP_ROUTER e controlla i DNS configurati
```

### DNSSEC — La Difesa

```bash
# Verifica se un dominio usa DNSSEC
dig example.com DNSKEY +short
dig example.com DS +short

# Se DNSSEC è attivo → i record DNS sono firmati
# → il DNS hijacking è molto più difficile
# → qualsiasi modifica invalida la firma crittografica
```

---

## 🍪 3. Session Hijacking

Il Session Hijacking è la presa di controllo di una sessione HTTP autenticata — l'attaccante ruba il cookie di sessione e si sostituisce all'utente senza conoscerne la password.

### Come Funziona

```
Utente effettua il login
        │
        ▼
Il server genera un Session Token (cookie)
es. SESSIONID=abc123xyz
        │
        ▼
L'attaccante ruba questo token
        │
        ▼
L'attaccante invia richieste con il token rubato
→ il server lo considera l'utente legittimo
→ nessuna password necessaria
```

### Come Ruba il Token

```
1. Sniffing di rete (HTTP non cifrato)
   → Wireshark su rete Wi-Fi pubblica
   → intercetta il cookie in chiaro

2. Cross-Site Scripting (XSS)
   → inietta JavaScript malevolo nel sito
   → document.cookie → invia il cookie all'attaccante

3. Man-in-the-Middle (MITM)
   → si interpone tra client e server
   → intercetta tutto il traffico

4. Malware sul client
   → accede direttamente ai cookie salvati
   → il browser li salva in chiaro o con crittografia debole

5. Fixation
   → forza l'utente a usare un Session ID
     già noto all'attaccante
```

### Tool

```bash
# Burp Suite → intercetta e modifica cookie
# Wireshark  → sniffa traffico HTTP
# Ettercap   → MITM su rete locale
# BeEF       → XSS framework → ruba cookie via browser
```

### Come Difendersi

```
✅ HTTPS ovunque → cifra il traffico → no sniffing
✅ HttpOnly flag → JavaScript non può accedere al cookie
✅ Secure flag   → cookie solo su HTTPS
✅ SameSite flag → protegge da CSRF
✅ Session timeout → sessioni brevi riducono la finestra
✅ Rigenera il Session ID dopo il login
```

---

## 🖥️ 4. BGP Hijacking

Il BGP (Border Gateway Protocol) Hijacking è uno degli attacchi più devastanti — reindirizza il traffico internet a livello di routing globale.

### Come Funziona

```
BGP è il protocollo che annuncia quali router
possiedono quali blocchi di IP

Router A dice: "io raggiungo 8.8.0.0/8"
        │
        ▼
Un attaccante con accesso a un router BGP
annuncia falsamente: "io raggiungo 8.8.8.0/24"
(range più specifico = ha la precedenza)
        │
        ▼
Il traffico verso 8.8.8.8 (Google DNS)
viene reindirizzato al router dell'attaccante
→ intercetta miliardi di query DNS
→ può modificare le risposte
```

### Casi Reali Famosi

```
2010 → China Telecom annuncia per 18 minuti
        il 15% di tutto il traffico internet
        → traffico USA, Europa, Australia
          passava per server cinesi

2018 → Attacco contro Amazon Route53
        → crypto rubate dalle wallet online

2019 → ISP europeo reindirizza traffico Google
        attraverso la Russia (Rostelecom)
```

### Perché È Difficile da Difendersi

```
BGP si basa sulla fiducia tra router
Non c'è autenticazione crittografica nativa
→ chiunque abbia accesso a un router BGP
  può fare annunci falsi

Soluzione moderna: RPKI
(Resource Public Key Infrastructure)
→ firma crittografica degli annunci BGP
→ adozione ancora parziale nel 2026
```

---

## 🖱️ 5. Clickjacking

Il Clickjacking inganna l'utente a cliccare su elementi nascosti — crede di cliccare su qualcosa ma in realtà clicca su qualcos'altro.

### Come Funziona

```html
<!-- Sito malevolo -->
<html>
  <body>
    <!-- Iframe invisibile del sito target -->
    <iframe src="https://banca.com/trasferisci-denaro"
            style="opacity:0; position:absolute; top:0; left:0">
    </iframe>

    <!-- Pulsante visibile innocuo -->
    <button style="position:absolute; top:0; left:0">
      Clicca per vincere!
    </button>
  </body>
</html>

L'utente clicca su "Clicca per vincere!"
→ in realtà clicca sul pulsante nascosto della banca
→ autorizza il trasferimento di denaro
```

### Difesa

```
X-Frame-Options: DENY
→ header HTTP che impedisce al sito
  di essere incluso in un iframe

Content-Security-Policy: frame-ancestors 'none'
→ versione moderna di X-Frame-Options
```

---

## ✈️ 6. URL / Typosquatting Hijacking

L'attaccante registra domini simili al target per intercettare utenti che digitano male l'URL:

```
example.com     → legittimo
examp1e.com     → typosquatting (1 al posto di l)
examle.com      → lettera mancante
example.co      → TLD simile
example-login.com → subdomain fake
```

### Combinazione con Phishing

```
L'attaccante registra examp1e.com
Crea una copia identica del sito example.com
Invia email di phishing con link a examp1e.com
        │
        ▼
L'utente non nota la differenza
Inserisce le credenziali
→ l'attaccante le raccoglie
```

---

## 🔗 Hijacking nel Footprinting — Come Usarlo in Difensiva

Nel pentesting autorizzato, riconoscere i vettori di hijacking aiuta a:

```bash
# 1. Controllare scadenza dominio target
whois example.com | grep -i "expir"
→ dominio in scadenza = possibile vector

# 2. Verificare DNSSEC
dig example.com DNSKEY +short
→ assenza DNSSEC = vulnerabile a cache poisoning

# 3. Trovare typosquatting registrato
# Strumenti: dnstwist
pip install dnstwist --break-system-packages
dnstwist example.com
→ lista di varianti già registrate
→ potenziali siti di phishing attivi

# 4. Verificare X-Frame-Options
curl -sI https://example.com | grep -i "x-frame\|frame-ancestors"
→ assenza = vulnerabile a clickjacking

# 5. Verificare HSTS (protegge da SSL stripping)
curl -sI https://example.com | grep -i "strict-transport"
→ assenza = vulnerabile a downgrade attack
```

---

## 📊 Tabella Riepilogativa

|Tipo|Target|Tecnica|Impatto|
|---|---|---|---|
|**Domain**|Dominio intero|Scadenza, compromissione Registrar|⭐⭐⭐⭐⭐|
|**DNS**|Query DNS|Cache poisoning, rogue server|⭐⭐⭐⭐⭐|
|**Session**|Sessione HTTP|XSS, sniffing, MITM|⭐⭐⭐⭐|
|**BGP**|Routing globale|Annunci BGP falsi|⭐⭐⭐⭐⭐|
|**Clickjacking**|Click utente|iframe nascosto|⭐⭐⭐|
|**Typosquatting**|Utenti distratti|Dominio simile|⭐⭐⭐|

---

## 🔗 Command Cheat Sheet

```bash
# Domain Hijacking — monitoraggio
whois example.com | grep -i "expir"        # scadenza
whois example.com | grep -i "name server"  # NS cambiati?

# DNS Hijacking — verifica
cat /etc/resolv.conf                        # DNS attuali
dig example.com @8.8.8.8 +short            # risposta Google
dig example.com @1.1.1.1 +short            # risposta Cloudflare
dig example.com DNSKEY +short              # DNSSEC attivo?

# Typosquatting
dnstwist example.com                        # varianti registrate
dnstwist --registered example.com           # solo quelle attive

# Header di sicurezza
curl -sI https://example.com | grep -iE \
  "x-frame|frame-ancestors|strict-transport|content-security"
```

---

## 🔗 Related Notes

- [[WHOIS]]
- [[Top Level Domain (TLD)]]
- [[Dig]]
- [[Tor]]
- [[LinuxCommands/Nmap]]
- [[Privilege Escalation Techniques]]

---

_References: Hacking Exposed 7 — McClure, Scambray, Kurtz · https://book.hacktricks.xyz · https://owasp.org/www-community/attacks · Linux Basics for Hacking — OccupyTheWeb_