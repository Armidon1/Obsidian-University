# Pagodo — Passive Google Dork Automation

#linux #cybersecurity #osint #footprinting #google-dorks #linux-basics-for-hackers

---

## 🗂️ Overview

**Pagodo** (Passive Google Dork) è uno script Python open-source che **automatizza l'esecuzione dei Google Dork del GHDB** su un dominio target — è il successore moderno di SiteDigger, senza dipendere da API proprietarie.

```
SiteDigger (2004-2011)     Pagodo (2016-oggi)
─────────────────────      ──────────────────────
Google API (chiusa)   →    Google scraping diretto
Windows only          →    Python multipiattaforma
GHDB statico          →    GHDB aggiornato in tempo reale
GUI                   →    CLI + proxy + jitter
```

Pagodo automatizza le ricerche Google per pagine web e applicazioni potenzialmente vulnerabili su internet. Sostituisce l'esecuzione manuale dei Google Dork attraverso un browser GUI.

---

## 🏗️ Architettura — Due Componenti

Ci sono 2 parti: la prima è `ghdb_scraper.py` che recupera i Google Dork più recenti, e la seconda è `pagodo.py` che sfrutta le informazioni raccolte da `ghdb_scraper.py`.

```
ghdb_scraper.py          pagodo.py
───────────────          ─────────────────────────────
Scarica tutti i          Prende il file di dork
dork dal GHDB            e li esegue su Google
→ dorks.txt              filtrando per dominio target
                         → risultati.txt
```

---

## 🛠️ Installazione

```bash
# Clona il repository
git clone https://github.com/opsdisk/pagodo.git
cd pagodo

# Crea un virtual environment (consigliato)
python3 -m venv .venv
source .venv/bin/activate

# Installa le dipendenze
pip install -r requirements.txt

# Verifica
python3 pagodo.py --help
python3 ghdb_scraper.py --help
```

---

## 📥 Step 1 — Aggiornare i Dork dal GHDB

Prima di lanciare pagodo, aggiorna sempre la lista dei dork:

```bash
# Scarica tutti i dork aggiornati dal GHDB
python3 ghdb_scraper.py -s -d dorks/

# Flag utili:
# -s   → salva su file
# -d   → directory di destinazione
# -t   → numero di thread (default 3, max consigliato)
# -n   → numero minimo dork da cui partire (default 5)
# -x   → numero massimo dork (default 5000)
```

```bash
# Output nella cartella dorks/:
dorks/
├── all_google_dorks.txt       ← tutti i dork, uno per riga
├── all_google_dorks.json      ← versione JSON con metadati
├── Files_Containing_Passwords.dorks
├── Sensitive_Directories.dorks
├── Vulnerable_Files.dorks
├── Pages_Containing_Login_Portals.dorks
└── ...                        ← un file per categoria GHDB
```

---

## 🚀 Step 2 — Eseguire Pagodo sul Target

```bash
# Sintassi base
python3 pagodo.py -d TARGET_DOMAIN -g DORKS_FILE [opzioni]

# Esempio — cerca directory sensibili su target.com
python3 pagodo.py \
    -d target.com \
    -g dorks/Sensitive_Directories.dorks \
    -s \
    -e 37 \
    -l 20 \
    -j 1.5
```

---

## 📋 Opzioni Principali

|Flag|Significato|Default|
|---|---|---|
|`-d`|Dominio target|obbligatorio|
|`-g`|File con i dork da usare|obbligatorio|
|`-s`|Salva i risultati su file|no|
|`-e`|Delay minimo tra le ricerche (secondi)|30|
|`-j`|Jitter factor — randomizza il delay|1.5|
|`-l`|Numero massimo di risultati per dork|100|
|`-p`|Proxy da usare (HTTP/SOCKS5)|nessuno|

---

## 🎯 Uso per Categoria — File di Dork

I dork sono divisi per categoria — puoi scegliere quale eseguire:

```bash
# Cerca file con password esposte
python3 pagodo.py -d target.com \
    -g dorks/Files_Containing_Passwords.dorks -s -e 37

# Cerca directory con listing aperto
python3 pagodo.py -d target.com \
    -g dorks/Sensitive_Directories.dorks -s -e 37

# Cerca file vulnerabili esposti
python3 pagodo.py -d target.com \
    -g dorks/Vulnerable_Files.dorks -s -e 37

# Cerca pannelli di login esposti
python3 pagodo.py -d target.com \
    -g dorks/Pages_Containing_Login_Portals.dorks -s -e 37

# Cerca messaggi di errore con info interne
python3 pagodo.py -d target.com \
    -g dorks/Error_Messages.dorks -s -e 37

# Lancia TUTTI i dork (molto lento — ore)
python3 pagodo.py -d target.com \
    -g dorks/all_google_dorks.txt -s -e 37
```

---

## 🕵️ Come Funziona Internamente

```
Per ogni dork nel file:

1. Costruisce la query Google:
   dork + "site:target.com"
   es: intitle:"index of" ".env" site:target.com

2. Invia la query a Google
   (scraping diretto, non API)

3. Aspetta delay + jitter randomizzato
   per evitare il blocco di Google

4. Raccoglie gli URL risultanti

5. Salva i risultati su file
```

### Esempio di Output

```
[*] Dorking target.com with: intitle:"index of" ".env"
    [+] https://target.com/backup/.env
    [+] https://target.com/old/.env.bak

[*] Dorking target.com with: filetype:sql "password"
    [-] No results

[*] Dorking target.com with: inurl:"/phpmyadmin/"
    [+] https://target.com/phpmyadmin/
```

---

## ⚠️ Il Problema del Rate Limiting di Google

Google blocca lo scraping automatico — se le query sono troppo veloci ricevi CAPTCHA o ban temporaneo dell'IP.

```bash
# Troppo veloce → Google blocca
python3 pagodo.py -d target.com -g dorks.txt -e 5

# Corretto — delay generoso + jitter
python3 pagodo.py -d target.com -g dorks.txt -e 37 -j 1.5
# → attende tra 37 e 55.5 secondi tra ogni query
#   (37 * 1.5 = 55.5 = massimo jitter)
```

---

## 🔒 Usare Proxy per Evitare il Ban

Questa versione di pagodo supporta nativamente HTTP(S) e SOCKS5, senza più bisogno di wrapparlo in proxychains. Puoi specificare più proxy in modalità round-robin usando il flag `-p`.

```bash
# Proxy singolo
python3 pagodo.py -d target.com -g dorks.txt \
    -p socks5://127.0.0.1:9050    # via Tor

# Proxy multipli (round-robin)
python3 pagodo.py -d target.com -g dorks.txt \
    -p "socks5://127.0.0.1:9050,http://proxy2:8080"

# Con proxychains (metodo alternativo)
proxychains4 python3 pagodo.py -d target.com \
    -g dorks/sensitive_directories.dorks -s -e 37 -l 20 -j 1.5
```

---

## 🐍 Uso come Libreria Python

Pagodo può essere usato anche come modulo Python per integrazione in script personalizzati:

```python
import ghdb_scraper
import pagodo

# Recupera i dork aggiornati dal GHDB
dorks = ghdb_scraper.retrieve_google_dorks(save_all_dorks_to_file=True)
print(f"Totale dork: {dorks['total_dorks']}")
print(f"Categorie: {list(dorks['category_dict'].keys())}")

# Esegui pagodo sul target
pg = pagodo.Pagodo(
    google_dorks_file="dorks/all_google_dorks.txt",
    domain="target.com",
    max_search_result_urls_to_return_per_dork=3,
    save_pagodo_results_to_file=True,
    minimum_delay_between_dork_searches_in_seconds=37,
    jitter=1.5
)

results = pg.go()

# Analizza i risultati
for dork, data in results["dorks"].items():
    if data["urls_size"] > 0:
        print(f"\n[+] Dork: {dork}")
        for url in data["urls"]:
            print(f"    → {url}")
```

---

## 📊 Pagodo vs SiteDigger vs Dork Manuale

| |SiteDigger|Pagodo|Dork Manuale|
|---|---|---|---|
|**Stato**|❌ Morto (2011)|✅ Attivo|✅ Sempre|
|**API Google**|Richiesta (chiusa)|Scraping diretto|Browser|
|**Aggiornamento GHDB**|Manuale|Automatico|Manuale|
|**Proxy support**|❌|✅ nativo|Browser|
|**Rate limiting**|Gestito da API|Delay/jitter manuale|Umano|
|**OS**|Windows only|Multipiattaforma|Qualsiasi|
|**Velocità**|Veloce (API)|Lento (scraping)|Lentissimo|
|**Automazione**|✅|✅|❌|

---

## 🗺️ Nel Workflow di Footprinting

```
Footprinting passivo
        │
        ├── WHOIS, dig, crt.sh     → chi è il target
        ├── theHarvester           → email e sottodomini
        │
        ▼
        Pagodo                     → cosa è esposto e vulnerabile
        │
        ├── Trova file .env esposti     → credenziali
        ├── Trova directory listing     → struttura interna
        ├── Trova pannelli admin        → target per brute force
        ├── Trova error messages        → info su stack tecnologico
        └── Trova file SQL esposti      → dati del database
        │
        ▼
        Nmap + Nikto               → conferma attiva (su target autorizzato)
```

---

## ⚠️ Limitazioni

```
❌ Lento — il delay obbligatorio rende ogni scan molto lungo
❌ Google blocca — CAPTCHA frequenti senza proxy
❌ Google ha limitato molti dork pericolosi
❌ Scraping viola i ToS di Google
❌ Non è installato su Kali di default (installazione manuale)
❌ Richiede Python 3.6+
```

---

## 🔗 Command Cheat Sheet

```bash
# Installazione
git clone https://github.com/opsdisk/pagodo.git
cd pagodo && pip install -r requirements.txt

# Aggiorna dork dal GHDB
python3 ghdb_scraper.py -s -d dorks/

# Scan per categoria
python3 pagodo.py -d target.com -g dorks/Files_Containing_Passwords.dorks -s -e 37 -j 1.5
python3 pagodo.py -d target.com -g dorks/Sensitive_Directories.dorks -s -e 37 -j 1.5
python3 pagodo.py -d target.com -g dorks/Vulnerable_Files.dorks -s -e 37 -j 1.5
python3 pagodo.py -d target.com -g dorks/Pages_Containing_Login_Portals.dorks -s -e 37 -j 1.5

# Con proxy Tor
python3 pagodo.py -d target.com -g dorks/all_google_dorks.txt \
    -s -e 37 -j 1.5 -p socks5://127.0.0.1:9050

# Con proxychains
proxychains4 python3 pagodo.py -d target.com \
    -g dorks/sensitive_directories.dorks -s -e 37 -l 20 -j 1.5
```

---

## 🔗 Related Notes

- [[GHDB_Google_Hacking_Database]] ← il database di dork che usa
- [[SiteDigger]] ← il predecessore storico
- [[theHarvester]] ← OSINT complementare
- [[Tor]] ← proxy per evitare ban
- [[LinuxCommands/Nmap]] ← passo successivo dopo pagodo

---

_References: https://github.com/opsdisk/pagodo · https://www.exploit-db.com/google-hacking-database · Linux Basics for Hacking — OccupyTheWeb_