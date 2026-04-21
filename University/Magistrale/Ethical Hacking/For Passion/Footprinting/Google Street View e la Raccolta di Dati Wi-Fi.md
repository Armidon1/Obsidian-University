# Google Street View e la Raccolta di Dati Wi-Fi

---

### Cosa è successo — la storia

Le auto di Google Street View, mentre fotografavano le strade di tutto il mondo, erano equipaggiate con antenne Wi-Fi che **scansionavano automaticamente le reti wireless circostanti** e registravano:

- **SSID** (nome della rete Wi-Fi)
- **MAC address** del router (BSSID)
- **Intensità del segnale**
- **Posizione GPS** al momento della rilevazione

Google dichiarò inizialmente che raccoglieva questi dati per migliorare la **geolocalizzazione** — i MAC address dei router sono usati come punti di riferimento per localizzare dispositivi senza GPS, tramite database come quello di Google Location Services.

Nel 2010 emerse però che le auto avevano anche **catturato payload — dati reali trasmessi su reti Wi-Fi aperte** — inclusi email, password, e frammenti di navigazione. Questo scatenò indagini in decine di paesi.

---

### Come funziona tecnicamente

```
Auto Google Street View passa per una strada
        │
        ▼
Antenna Wi-Fi scansiona tutte le reti visibili
        │
        ▼
Registra:  BSSID (MAC address router)
           SSID  (nome rete)
           RSSI  (potenza segnale)
           GPS   (coordinate esatte)
        │
        ▼
Dati inviati ai server Google → database geolocalizzazione
```

Il MAC address di un router è **univoco e persistente** — non cambia mai (a meno che non venga modificato manualmente). Questo lo rende un identificatore perfetto per la geolocalizzazione.

---

### Il database che ne risulta

Google (e altri come Wigle.net) hanno costruito enormi database che mappano:

```
MAC address  →  coordinate GPS precise
00:1A:2B:3C:4D:5E  →  Via Roma 14, Milano, 45.4654°N 9.1859°E
```

Questo significa che se conosci il MAC address di un router, puoi **trovare la sua posizione fisica** — e viceversa, se sei in una zona, puoi vedere quali router esistono lì.

---

### WiGLE.net — il database pubblico

**WiGLE (Wireless Geographic Logging Engine)** è un database pubblico e consultabile che raccoglie esattamente questo tipo di informazioni, contribuite da chiunque faccia **wardriving** (girare in auto con uno sniffer Wi-Fi attivo). https://wigle.net

Puoi cercare per:

- Indirizzo fisico → vedere tutte le reti Wi-Fi in quella zona
- SSID → trovare dove è stata rilevata quella rete
- MAC address → trovare la posizione del router

---

### Implicazioni per l'OSINT e il Pentesting

|Informazione di partenza|Cosa puoi ricavare|
|---|---|
|Indirizzo fisico target|Reti Wi-Fi presenti, nomi router, MAC address|
|Nome rete (SSID)|Posizione fisica approssimativa|
|MAC address router|Posizione GPS precisa storica|
|Tipo di router (dal MAC)|Vendor del dispositivo → vulnerabilità note|

Il **vendor** del dispositivo è ricavabile dai primi 3 byte del MAC address (OUI — Organizationally Unique Identifier):

```
MAC:  00:1A:2B:3C:4D:5E
      └──┬──┘
    primi 3 byte = OUI
    → identifica il produttore (es. Cisco, Netgear, TP-Link)
```

```bash
# Su Linux, cercare il vendor da un MAC
curl https://api.macvendors.com/00:1A:2B
# → Cisco Systems
```

---

### Il Dumpster Diving — contesto fisico

Combinando queste informazioni con il **dumpster diving** (rovistare nella spazzatura aziendale), un attaccante può costruire un profilo fisico completo:

```
Google Maps Street View
   → layout fisico dell'edificio, ingressi, telecamere visibili

WiGLE / Google Location Services
   → reti Wi-Fi interne, vendor dei router

Dumpster diving
   → documenti interni, vecchi hard disk, badge scaduti,
     manuali di configurazione, topology di rete stampate
```

Insieme questi tre vettori fanno parte del **physical pentesting** — una branca del penetration testing che valuta la sicurezza fisica di un'organizzazione, non solo quella digitale.

---

### Come difendersi

```
✅ Cambia l'SSID di default (non rivelare il modello del router)
✅ Opt-out dal database Google: aggiungi "_nomap" all'SSID
   es. "HomeNetwork_nomap"
✅ Distruggi fisicamente i documenti (trita tutto)
✅ Politiche di smaltimento sicuro per hardware dismesso
✅ Controlla cosa è visibile da Google Street View
   (puoi richiedere la rimozione di immagini sensibili)
```

> [!tip] Nota `_nomap` alla fine del nome rete è uno standard riconosciuto da Google e Microsoft per escludere il router dai loro database di geolocalizzazione — ma non da WiGLE o altri database privati.