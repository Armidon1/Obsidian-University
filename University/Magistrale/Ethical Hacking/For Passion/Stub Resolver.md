# Stub Resolver

#linux #cybersecurity #networking #dns #linux-basics-for-hackers

---

## 🗂️ Overview

Lo **Stub Resolver** è il componente DNS più vicino all'utente — il codice che gira direttamente sul computer e si occupa di fare le query DNS per conto di tutte le applicazioni. È chiamato "stub" (moncone) perché **non fa il lavoro pesante** — delega tutto al resolver ricorsivo esterno.

```
Browser / App
      │ "qual è l'IP di example.com?"
      ▼
Stub Resolver          ← gira sul TUO computer
      │ query UDP porta 53
      ▼
Resolver Ricorsivo     ← 8.8.8.8, 1.1.1.1, o il tuo router
      │ naviga tutta la gerarchia
      ▼
Root → TLD → NS Autoritativo
      │
      ▼
93.184.216.34 ✅
```

→ Vedi [[Recursive Resolver DNS]] per il dettaglio su cosa fa il resolver ricorsivo

---

## 🧩 Stub vs Full Resolver

```
Stub Resolver              Full Resolver (Ricorsivo)
──────────────────         ──────────────────────────
Gira sul client            Gira su server esterni
                           (8.8.8.8, 1.1.1.1, router...)

Fa UNA sola query          Naviga tutta la gerarchia DNS
al resolver ricorsivo      root → TLD → NS → risposta

Non conosce la             Conosce la gerarchia e sa
gerarchia DNS              come navigarla autonomamente

Cache piccola o assente    Cache enorme con milioni
                           di risposte salvate

Configurato in             Gestito da Google, Cloudflare,
/etc/resolv.conf           ISP, o il tuo server locale
```

---

## 📍 Dove Vive sul Sistema

### `/etc/resolv.conf` — La Configurazione Base

Il file più importante per lo stub resolver — dice a quale server mandare le query:

```bash
cat /etc/resolv.conf
```

```
nameserver 8.8.8.8        # primo resolver da usare (Google)
nameserver 1.1.1.1        # fallback se il primo non risponde
search local              # dominio di ricerca locale
options ndots:5           # quanti punti prima di considerare FQDN
```

### `systemd-resolved` — Lo Stub Resolver Moderno

Su sistemi Linux moderni (Ubuntu 20.04+, Kali, Parrot) il resolver è gestito da **systemd-resolved**:

```bash
# Status
systemctl status systemd-resolved

# Ascolta sempre su questo indirizzo fisso
# 127.0.0.53:53  ← tutte le query passano qui
#                   prima di andare al resolver esterno

# Configurazione dettagliata
resolvectl status

# Vedere quale server ha risposto a una query
resolvectl query example.com

# DNS attualmente in uso
resolvectl dns
```

---

## 🔄 Il Flusso Completo

```
Firefox vuole risolvere example.com
        │
        ▼
Chiede alla libreria C del sistema (glibc/libc)
        │
        ▼
glibc legge /etc/resolv.conf (o parla con systemd-resolved)
→ trova nameserver 8.8.8.8
        │
        ▼
Stub Resolver invia query UDP a 8.8.8.8:53
"dammi l'A record di example.com"
        │
        ▼
8.8.8.8 (resolver ricorsivo) fa il lavoro pesante
→ root server → TLD .com → NS autoritativo
        │ → vedi [[Recursive Resolver DNS]]
        ▼
8.8.8.8 risponde: "93.184.216.34, TTL 300"
        │
        ▼
Stub Resolver salva in cache locale (per il TTL)
Restituisce la risposta a Firefox
        │
        ▼
Firefox si connette a 93.184.216.34
```

---

## 🔧 Modificare `/etc/resolv.conf` — DNS Personalizzato

Puoi sostituire il resolver con qualsiasi server DNS — incluso uno tuo su Raspberry Pi.

### Caso d'uso: Raspberry Pi con DNS Personalizzato

```bash
# Il tuo Raspberry Pi ha IP fisso: 192.168.1.10
# Gira Pi-hole, AdGuard Home, o Unbound

# Modifica /etc/resolv.conf
sudo nano /etc/resolv.conf
```

```
# Metti il tuo Raspberry Pi come primo resolver
nameserver 192.168.1.10

# Mantieni un fallback esterno per sicurezza
nameserver 1.1.1.1

# Opzionale: dominio locale
search home.lan
```

> [!warning] Problema con systemd-resolved Su sistemi moderni `/etc/resolv.conf` è spesso un **symlink** gestito da systemd-resolved — modificarlo direttamente viene sovrascritto al prossimo riavvio.

```bash
# Verifica se è un symlink
ls -lah /etc/resolv.conf
# → /etc/resolv.conf -> ../run/systemd/resolve/stub-resolv.conf

# Soluzione 1 — Modifica systemd-resolved
sudo nano /etc/systemd/resolved.conf
```

```ini
[Resolve]
DNS=192.168.1.10          # tuo Raspberry Pi
FallbackDNS=1.1.1.1       # fallback Cloudflare
Domains=home.lan          # dominio locale
DNSSEC=no                 # disabilita se il tuo server non lo supporta
DNSOverTLS=no             # disabilita se il tuo server non lo supporta
```

```bash
# Riavvia per applicare
sudo systemctl restart systemd-resolved

# Verifica
resolvectl status
# → DNS Server: 192.168.1.10
```

```bash
# Soluzione 2 — Rompi il symlink e scrivi direttamente
sudo rm /etc/resolv.conf
sudo nano /etc/resolv.conf
# → scrivi il contenuto che vuoi
# → ma viene sovrascritto da network manager al riavvio

# Soluzione 3 — Rendi il file immutabile
sudo chattr +i /etc/resolv.conf
# → nessun processo può modificarlo
# per tornare a modificarlo:
sudo chattr -i /etc/resolv.conf
```

```bash
# Soluzione 4 — NetworkManager (Kali/Ubuntu con desktop)
sudo nano /etc/NetworkManager/NetworkManager.conf
```

```ini
[main]
dns=none          # dice a NetworkManager di non toccare resolv.conf
```

```bash
sudo systemctl restart NetworkManager
# ora puoi modificare /etc/resolv.conf liberamente
```

---

## 🏠 Lo Stub Resolver del Router

Il router di casa fa da **stub resolver intermedio** — è il resolver predefinito di tutti i dispositivi della rete.

```
Dispositivi della rete
(PC, telefono, tablet...)
        │ query DNS verso 192.168.1.1 (il router)
        ▼
Router (stub resolver locale)
        │ query verso il resolver del ISP
        │ oppure verso 8.8.8.8 / 1.1.1.1 se configurato
        ▼
Resolver ricorsivo esterno
        │
        ▼
Risposta → router → dispositivo
```

### Il Router come Cache DNS

Il router salva le risposte DNS in cache — se 5 dispositivi cercano google.com, il router risolve una volta sola e risponde agli altri dalla cache.

### Configurare il Router per Usare il Raspberry Pi

```
Nel pannello admin del router (192.168.1.1):
Settings → DNS → Primary DNS: 192.168.1.10

→ TUTTI i dispositivi della rete usano automaticamente
  il tuo Raspberry Pi come resolver
→ nessuna modifica necessaria sui singoli dispositivi
→ Pi-hole filtra ads per tutta la rete
```

### Il Rischio: Router come Vettore di Hijacking

```bash
# Se l'attaccante accede al router e cambia i DNS
# TUTTI i dispositivi della rete vengono reindirizzati

# Verifica i DNS configurati sul router
# Vai su http://192.168.1.1 (o l'IP del tuo router)
# Controlla la sezione DNS

# Da terminale — vedi il gateway (router)
ip route | grep default
# → default via 192.168.1.1 dev eth0

# Verifica i DNS che il router ti sta dando via DHCP
nmcli dev show | grep DNS
# → DNS: 192.168.1.1  ← il router stesso fa da DNS

# Confronta con i DNS dichiarati dal resolver
resolvectl status
```

→ Vedi [[Hijacking]] sezione DNS Hijacking per i dettagli sull'attacco

---

## 🔒 DNS Privacy — Opzioni Avanzate

### DNS over TLS (DoT)

```bash
# Cifra le query DNS con TLS
# Porta 853 invece di 53

# Configura in systemd-resolved
sudo nano /etc/systemd/resolved.conf
```

```ini
[Resolve]
DNS=1.1.1.1
DNSOverTLS=yes
```

### DNS over HTTPS (DoH)

```
Il browser moderno con DoH attivo:
→ bypassa COMPLETAMENTE lo stub resolver
→ bypassa /etc/resolv.conf
→ manda query cifrate via HTTPS direttamente
  a 1.1.1.1 o 8.8.8.8
→ il sistema operativo NON vede le query DNS

Vantaggio:  privacy totale dalle intercettazioni locali
Svantaggio: il tuo Pi-hole/Raspberry Pi non filtra nulla
            perché il browser bypassa il resolver locale
```

```bash
# Per forzare il browser a usare il tuo resolver
# disabilita DoH nel browser:
# Firefox → about:config → network.trr.mode = 5 (disabilitato)
# Chrome  → Settings → Privacy → Use secure DNS → OFF
```

---

## 🕵️ Rilevanza nel Cybersecurity

### 1. Vettore di attacco — modifica di `/etc/resolv.conf`

```bash
# Se un malware modifica il resolver
cat /etc/resolv.conf
# nameserver 10.0.0.1  ← server malevolo dell'attaccante

# Tutte le query vengono dirottate
# → phishing, credential harvesting, MITM

# Come rilevarlo
# Controlla che il DNS risponda correttamente
dig example.com @8.8.8.8 +short    # chiedi a Google
dig example.com +short              # chiedi al tuo resolver

# Se le risposte differiscono → possibile hijacking
```

### 2. DNS Leak con VPN

```bash
# Quando usi una VPN, le query DNS dovrebbero passare
# attraverso il tunnel cifrato

# Se lo stub resolver usa ancora il resolver ISP
# → DNS leak → l'ISP vede tutti i tuoi domini
# → la VPN non serve a niente per la privacy DNS

# Test DNS leak
# https://dnsleaktest.com
# oppure da terminale:
dig whoami.akamai.net +short
# → se mostra IP del tuo ISP invece della VPN → leak
```

### 3. `dig @server` — Bypassare lo Stub Resolver

```bash
# @ specifica il resolver da usare direttamente
# bypassando completamente lo stub resolver locale

dig @8.8.8.8 example.com A +short    # vai direttamente a Google
dig @1.1.1.1 example.com A +short    # vai direttamente a Cloudflare
dig @192.168.1.10 example.com        # vai direttamente al Raspberry Pi

# Utile quando sospetti che il resolver locale sia compromesso
# o quando vuoi confrontare risposte di server diversi
```

---

## 🔗 Command Cheat Sheet

```bash
# Stato e configurazione
cat /etc/resolv.conf                          # configurazione base
resolvectl status                             # stato systemd-resolved
resolvectl dns                                # DNS in uso
nmcli dev show | grep DNS                     # DNS da NetworkManager

# Test
resolvectl query example.com                 # query tramite stub resolver
dig example.com +short                       # query normale
dig @8.8.8.8 example.com +short             # bypassa resolver locale
dig @192.168.1.10 example.com +short         # usa Raspberry Pi

# Modifica DNS con systemd-resolved
sudo nano /etc/systemd/resolved.conf          # file di config
sudo systemctl restart systemd-resolved       # applica modifiche

# Modifica DNS manuale
sudo chattr -i /etc/resolv.conf               # rendi modificabile
sudo nano /etc/resolv.conf                    # modifica
sudo chattr +i /etc/resolv.conf               # blocca le modifiche

# Sicurezza
dig whoami.akamai.net +short                  # verifica DNS leak
```

---

## 🔗 Related Notes

- [[Recursive Resolver DNS]] ← nota futura: cosa fa il resolver ricorsivo
- [[DNS Reconnaissance — dig]]
- [[Hijacking]] ← sezione DNS Hijacking
- [[Top_Level_Domain]]
- [[WHOIS]]
- [[Tor]] ← DNS e anonimità

---

_References: man resolv.conf · man systemd-resolved · https://www.cloudflare.com/learning/dns · Linux Basics for Hacking — OccupyTheWeb_