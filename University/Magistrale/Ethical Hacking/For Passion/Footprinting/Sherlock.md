# Sherlock — Username Hunter

---

### Cos'è

Sherlock è uno strumento OSINT open-source progettato per trovare username su una vasta gamma di social network e siti web. Attualmente può verificare un dato username su 400+ siti e piattaforme, permettendo agli investigatori di determinare rapidamente dove uno username è attivo.

---

### Come Funziona

Quando fornisci a Sherlock uno username, il tool invia richieste automatizzate agli URL di registrazione di oltre 400 piattaforme. Se il server risponde con uno status "Found" (spesso HTTP 200 OK), Sherlock registra l'URL. Se il sito indica che la pagina non esiste (HTTP 404), passa al successivo.

```
Tu dai: "mario_rossi"
      │
      ▼
Sherlock costruisce:
  https://github.com/mario_rossi
  https://reddit.com/u/mario_rossi
  https://twitter.com/mario_rossi
  https://instagram.com/mario_rossi
  ... per 400+ siti
      │
      ▼
Controlla la risposta HTTP di ognuno
200 OK  → profilo trovato ✅
404     → non esiste ❌
      │
      ▼
Restituisce lista di URL trovati
```

---

### Installazione e Uso

```bash
# Installazione
pip install sherlock-project --break-system-packages

# oppure da GitHub
git clone https://github.com/sherlock-project/sherlock
cd sherlock
pip install -r requirements.txt --break-system-packages

# Uso base
sherlock username

# Più username contemporaneamente
sherlock username1 username2 username3

# Solo su siti specifici
sherlock username --site github --site twitter

# Salva output su file
sherlock username --output risultati.txt

# Esporta in CSV
sherlock username --csv

# Con Tor per anonimità
sherlock username --tor

# Timeout personalizzato (default 60s)
sherlock username --timeout 10

# Solo risultati trovati, no errori
sherlock username --print-found
```

---

### La Differenza Fondamentale con theHarvester

Questa è la distinzione chiave:

```
theHarvester              Sherlock
─────────────────         ──────────────────────
Input: DOMINIO            Input: USERNAME
"microsoft.com"           "mario_rossi"

Cerca:                    Cerca:
→ email aziendali         → profili social
→ sottodomini             → account su forum
→ IP e host               → account su gaming
→ infrastruttura          → account su GitHub
→ nomi dipendenti         → account su Reddit
                          → presenza digitale
                            personale

Target ideale:            Target ideale:
ORGANIZZAZIONE            PERSONA FISICA
```

---

### Quando Usarli

```
Stai facendo recon su un'AZIENDA?
→ theHarvester
  ti mappa l'infrastruttura tecnica
  trova email @azienda.com
  trova sottodomini e server

Stai cercando una PERSONA?
→ Sherlock
  tracci la presenza digitale personale
  trovi tutti gli account pubblici
  costruisci un profilo della persona
```

---

### Perché è Potente nel Pentesting

Sherlock si estende oltre i siti mainstream come Twitter, Facebook e Reddit, includendo piattaforme gaming come NameMC, Steam e Roblox, così come comunità di coding come Codecademy, GitHub e GitLab.

Nel contesto di un pentest o social engineering:

```
Trovi "m.nole" come username su LinkedIn (da theHarvester)
        │
        ▼
Lanci sherlock m.nole
        │
        ▼
Scopri che usa lo stesso username su:
  GitHub   → vedi il codice che ha scritto
  Reddit   → vedi i suoi interessi e opinioni
  Steam    → nome reale nel profilo
  Twitter  → post personali
  HackerNews → commenti tecnici
        │
        ▼
Profilo completo della persona →
social engineering, phishing mirato,
password guessing basato sugli interessi
```

---

### Importante

Sherlock non richiede API key o credenziali di login per i siti che controlla — costruisce semplicemente l'URL del profilo atteso per ogni sito e osserva la risposta. Questo significa che accede solo a informazioni pubblicamente disponibili e non può bypassare impostazioni di privacy o restrizioni sugli account.

---

### theHarvester + Sherlock — Workflow Combinato

```
1. theHarvester -d azienda.com -b linkedin
   → trova nomi dipendenti: "Mario Rossi", "Lucia Bianchi"

2. Costruisci username probabili:
   mario.rossi, mrossi, mario_rossi, rossi_mario...

3. sherlock mario.rossi mrossi mario_rossi
   → trova i loro profili personali

4. Da GitHub → trovano codice interno pubblicato per sbaglio
   Da Reddit → trovano info sulla cultura aziendale
   Da LinkedIn → organigramma completo
```

> [!tip] Sherlock è pre-installato su **Kali Linux** e **Parrot OS**. Se usi Kali puoi lanciarlo direttamente senza installazione.

---
# NEXT STEP 
Dipende da cosa vuoi ottenere. Ci sono due direzioni:

---

### Direzione 1 — Approfondire i profili trovati

Sherlock ti ha dato 5 URL. Il passo successivo è estrarre informazioni da quei profili:

```
YouTube → youtube-dl o yt-dlp
          scarica i metadati del canale
          data di creazione, descrizione, link esterni

          youtube-dl --get-description https://youtube.com/@username
          → spesso contengono email, altri social, sito personale

ArtStation → guarda i progetti pubblicati
             i file hanno metadati EXIF → GPS, software usato,
             data di creazione, nome reale nei metadati del file

Xbox Gamertag → siti come xboxgamertag.com
                mostrano giochi giocati, achievement, ore di gioco
                → rivela interessi, abitudini, orari di attività
```

---

### Direzione 2 — Trovare altri username collegati

Il profilo YouTube o ArtStation potrebbe rivelare un username diverso — e da lì rilanci Sherlock:

```bash
# Trovi che su YouTube si chiama "user_name" invece di "username"
sherlock user_name user username

# Prova varianti comuni dello stesso username
sherlock username user_name username user
```

---

### Direzione 3 — OSINT completo sulla persona

Combinazione classica nel social engineering:

```
Sherlock          → dove esiste l'username
      │
      ▼
theHarvester      → se ha un dominio personale
      │             username.com? username.dev?
      ▼
Google Dorks      → "username" site:linkedin.com
                    "username" filetype:pdf
                    "username" inurl:github
      │
      ▼
Maltego           → grafo visuale di tutte le connessioni
                    tra i profili trovati
      │
      ▼
EXIF tool         → metadati delle immagini pubblicate
                    → posizione GPS, dispositivo usato
```

---

### Il tool più utile da affiancare subito — [[Exiftool]]

```bash
# Installa
sudo apt install exiftool -y

# Scarica un'immagine dal profilo ArtStation
wget https://url-immagine-armidon22.jpg

# Estrai i metadati
exiftool immagine.jpg
```

Output possibile:

```
GPS Latitude  : 41.9028° N     ← dove è stata scattata
GPS Longitude : 12.4964° E     ← Roma
Camera Model  : iPhone 14 Pro  ← dispositivo
Software      : Lightroom 6.0  ← tool usati
Author        : Mario Rossi     ← nome reale
```

> [!tip] Le immagini pubblicate su ArtStation spesso **non vengono strippate dei metadati EXIF** — a differenza di Instagram e Facebook che li rimuovono automaticamente. È uno dei leak più sottovalutati.