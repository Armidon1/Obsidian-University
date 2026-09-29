# WiFi — Agganciarsi a un Access Point specifico (BSSID pinning)

**Categoria:** #network #wifi #linux #networkmanager #802-11  
**Uso:** Forzare il client a connettersi a un AP preciso quando decine di AP condividono lo stesso SSID (reti universitarie, `eduroam`, `sapienza`, aziendali)  
**Contesto:** sessione del 28/09/2026 su Fedora, scheda Intel AX210, driver `iwlwifi`

---

## 📖 Il concetto di base: SSID ≠ BSSID

Questa è la distinzione da cui dipende tutto il resto.

| Sigla | Sta per | Cos'è davvero |
|---|---|---|
| **SSID** | Service Set Identifier | Il *nome* della rete (`sapienza`). È solo una stringa, la scrivono identica decine di AP diversi. |
| **BSSID** | Basic Service Set Identifier | Il **MAC address della singola radio** di un singolo AP. Unico, 6 byte. |
| **BSS** | Basic Service Set | Un AP + i client attaccati a lui. |
| **ESS** | Extended Service Set | *Tutti* i BSS che condividono lo stesso SSID = "la rete sapienza". |

> [!important] Il punto chiave
> Quando dici "connettiti a sapienza" stai nominando un **ESS**, non una macchina. Il tuo client sceglie *lui* a quale BSS agganciarsi. Per scegliere tu, devi parlare di BSSID.

### Un dettaglio che si vede benissimo nello scan reale

Guarda i BSSID catturati in aula:

```
C8:0C:C8:E5:84:10  eduroam    ch 52
C8:0C:C8:E5:84:12  SPV-Red    ch 52
C8:0C:C8:E5:84:14  dicea      ch 52
C8:0C:C8:E5:84:15  sapienza   ch 52
C8:0C:C8:E5:84:04  dicea      ch 1   (2.4 GHz)
```

Notare due cose:

1. I primi quattro differiscono **solo nell'ultimo nibble** e stanno tutti sul canale 52. Non sono quattro AP: è **un solo AP** che espone quattro **BSSID virtuali** (multi-SSID). Un AP fisico ha una radio per banda, e ogni radio può annunciare più reti logiche, ciascuna con il proprio BSSID derivato dal MAC base.
2. L'ultimo (`...:84:04`) è la radio 2.4 GHz **dello stesso apparato**. Stesso AP fisico, radio diversa, BSSID diverso.

Corollario pratico: se fissi un BSSID, ti stai legando a *una radio su una banda su un apparato*. Cambiare banda = cambiare BSSID.

---

## 🧠 Chi decide a quale AP ti attacchi?

**Il client, non l'infrastruttura.** E questo è il motivo per cui il problema esiste.

- L'algoritmo di selezione sta nel driver + `wpa_supplicant`, è largamente proprietario e nella pratica è **guidato dall'RSSI**: vince il segnale più forte, la congestione non entra quasi mai nell'equazione.
- Da qui il classico **sticky client problem**: ti agganci all'AP dell'ingresso, attraversi l'edificio, e resti incollato a lui a -85 dBm invece di passare a quello sopra la tua testa, perché il driver non fa roaming finché il link non è quasi morto.
- Gli standard che provano a rimediare (lato infrastruttura, se abilitati):
  - **802.11k** — *Radio Resource Measurement*: l'AP ti manda un "neighbor report", cioè la lista degli AP vicini della stessa rete, così non devi scansionare tutte le bande.
  - **802.11v** — *BSS Transition Management*: l'AP può **chiederti** di spostarti altrove (è così che i controller fanno load balancing).
  - **802.11r** — *Fast Transition*: rende il passaggio veloce senza rifare tutto l'handshake 802.1X.

> [!tip] Curiosità verificata sul campo
> Gli AP `sapienza` annunciano `RM enabled capabilities` e il flag `RadioMeasure` nelle capability → **802.11k c'è**. Quindi in teoria l'infrastruttura saprebbe suggerirti un vicino migliore. In pratica su un client Linux non succede nulla di automatico, e il pinning manuale resta lo strumento più diretto.

---

## 🔍 Fase 1 — Leggere lo scan

### Con NetworkManager (no root)

```bash
# Scan completo con le colonne che servono davvero
nmcli -f IN-USE,BSSID,SSID,CHAN,FREQ,RATE,SIGNAL,SECURITY dev wifi list --rescan yes

# Solo gli AP di una rete specifica
nmcli -f IN-USE,BSSID,SSID,CHAN,SIGNAL dev wifi list --rescan yes | grep -E "sapienza|IN-USE"

# Forza solo la riscansione
nmcli dev wifi rescan
```

`--rescan yes` obbliga una scansione fresca; senza, NM può servirti una cache vecchia anche di minuti (ed è il motivo per cui a volte "non vedi" un AP che c'è).

### Con `iw` (più grezzo, più informativo — e `scan dump` non richiede root)

```bash
# Legge la cache di scansione del kernel senza generare traffico
iw dev wlp1s0 scan dump | grep -E "^BSS|SSID:|signal:|freq:"

# Tutti gli Information Element di un AP preciso
iw dev wlp1s0 scan dump | awk '/^BSS c8:0c:c8:e5:84:15/,/^BSS [^c]/'

# Scansione attiva vera (questa sì richiede root e interrompe il traffico)
sudo iw dev wlp1s0 scan
```

> [!note] Workflow furbo
> `nmcli dev wifi rescan` (no root, popola la cache del kernel) seguito da `iw dev wlp1s0 scan dump` (no root, legge tutto il dettaglio). Ottieni l'output ricco di `iw` senza mai usare `sudo`.

---

## 📶 Fase 2 — Interpretare il segnale

La colonna `SIGNAL` di `nmcli` è una **percentuale di qualità** calcolata da NetworkManager: comoda per ordinare, inutile per ragionare. Il numero vero è il **dBm**, che trovi con `iw`.

```bash
iw dev wlp1s0 link           # segnale del link attuale
iw dev wlp1s0 station dump   # statistiche complete dell'associazione
```

Scala di riferimento (RSSI, valori negativi: **più vicino a zero = meglio**):

| dBm | Giudizio | Cosa ci fai |
|---|---|---|
| -30 … -50 | Eccellente | Sei praticamente sotto l'AP |
| -50 … -60 | Molto buono | Tutto, a piena velocità |
| -60 … -67 | Buono | **-67 dBm è la soglia di progetto per VoIP/video** |
| -67 … -70 | Sufficiente | Navigazione ok, videochiamate ballerine |
| -70 … -80 | Debole | Rate bassi, ritrasmissioni |
| -80 … -90 | Al limite | Funziona sulla carta, soffre |
| < -90 | Inutilizzabile | Sotto il rumore di fondo |

Il **noise floor** tipico in 5 GHz sta intorno a -95 dBm. Quello che conta davvero non è l'RSSI assoluto ma l'**SNR** = segnale − rumore: a -84 dBm con rumore a -95 hai ~11 dB di SNR, che basta a malapena per le modulazioni più lente.

---

## 🛠️ Fase 3 — Fissare il BSSID (quello che ho fatto)

NetworkManager espone la proprietà `802-11-wireless.bssid` sul profilo di connessione. Se è valorizzata, il supplicant **si associa solo a quel BSSID** e ignora tutti gli altri AP con lo stesso SSID.

```bash
# 1. Vedi com'è messo il profilo
nmcli -f connection.id,802-11-wireless.ssid,802-11-wireless.bssid,connection.autoconnect \
      con show "sapienza"

# 2. Fissa l'AP scelto
nmcli con mod "sapienza" 802-11-wireless.bssid 00:06:F4:D9:44:55

# 3. Attiva
nmcli con up "sapienza"
```

### Il pattern migliore: due profili

Invece di continuare a modificare e ripristinare un profilo solo, tienine due — ed è esattamente la situazione che avevi già sulla macchina:

| Profilo | BSSID | autoconnect | Ruolo |
|---|---|---|---|
| `sapienza` | fissato | `no` | Il "manuale": lo tiri su quando vuoi un AP preciso |
| `sapienza 1` | `--` (libero) | `yes` | Il normale: roaming automatico |

Per crearne uno nuovo da zero senza toccare l'esistente:

```bash
nmcli con clone "sapienza 1" sapienza-pin
nmcli con mod sapienza-pin 802-11-wireless.bssid 00:06:F4:D9:44:55
nmcli con mod sapienza-pin connection.autoconnect no
```

> [!warning] `autoconnect no` è importante sul profilo pinnato
> Se lo lasci a `yes`, NetworkManager proverà ad agganciare quel BSSID specifico ogni volta che accendi il laptop — anche in un altro edificio, dove quell'AP non esiste. Risultato: connessioni lente o fallite senza un motivo evidente. Il profilo pinnato deve essere attivato **a mano**.

Altre proprietà del profilo che vale la pena conoscere:

```bash
# Forza la banda: "a" = 5 GHz, "bg" = 2.4 GHz
nmcli con mod "sapienza 1" 802-11-wireless.band a

# Forza un canale specifico (richiede band impostata)
nmcli con mod "sapienza 1" 802-11-wireless.channel 100

# Priorità tra profili in autoconnect (numero più alto vince)
nmcli con mod "sapienza 1" connection.autoconnect-priority 10

# MAC randomizzato: utile per privacy, letale con i captive portal
# (ogni riconnessione ti fa sembrare un dispositivo nuovo → rifai il login)
nmcli con mod "sapienza 1" wifi.cloned-mac-address stable
```

`802-11-wireless.band a` è spesso l'alternativa **più intelligente** del pinning: ti tiene sui 5 GHz (meno affollati, celle più piccole) lasciandoti però il roaming libero.

---

## ✅ Fase 4 — Verificare che sia servito a qualcosa

Non fermarti a "risulta connesso". Guarda i numeri del link:

```bash
# A quale BSSID sono davvero attaccato?
iw dev wlp1s0 link

# Statistiche vere dell'associazione
iw dev wlp1s0 station dump

# Conferma dal lato NetworkManager (la riga con l'asterisco)
nmcli -f IN-USE,BSSID,SSID,CHAN,SIGNAL dev wifi list | grep '^\*'

# Latenza e jitter verso il primo hop (isola il tratto radio da Internet)
ping -c 20 $(nmcli -g IP4.GATEWAY dev show wlp1s0)
```

Le metriche da leggere in `station dump`:

- **`signal` / `signal avg`** — RSSI istantaneo e medio.
- **`tx bitrate` / `rx bitrate`** — il rate negoziato *adesso*. È la misura onesta della salute del link: crolla molto prima che la connessione cada.
- **`tx retries` vs `tx packets`** — il rapporto è il tuo indicatore di sofferenza. Sotto il 5% è fisiologico, sopra il 15% stai sprecando metà del tempo d'aria.
- **`beacon loss`** — se cresce, stai perdendo i beacon dell'AP: sei troppo lontano.

---

## 🧪 Case study: cosa è successo davvero

**Situazione di partenza.** Sei AP `sapienza` in portata. Il più forte (`C8:0C:C8:E5:84:15`, canale 52, qualità 62) è quello dell'aula, e risultava intasato. Il secondo migliore è `00:06:F4:D9:44:55` sul canale 100, qualità 30.

**Azione.**

```bash
nmcli con mod "sapienza" 802-11-wireless.bssid 00:06:F4:D9:44:55
nmcli con up "sapienza"
```

**Risultato dopo l'associazione:**

| Metrica | Valore | Lettura |
|---|---|---|
| BSSID | `00:06:f4:d9:44:55`, ch 100 (5.5 GHz) | ✅ pinning riuscito |
| IP | `10.2.75.231/19`, gw `10.2.64.1` | ✅ DHCP ok, `/19` = ~8000 host per subnet |
| Connettività NM | `full` | ✅ nessun captive portal a bloccare |
| Segnale | **-84 dBm** (avg) | ⚠️ molto debole |
| TX bitrate | **14.4 Mbit/s** (VHT-MCS 1) su 1170 nominali | ⚠️ modulazione al minimo |
| RX bitrate | 40.5 Mbit/s (VHT-MCS 2, 40 MHz, NSS 1) | ⚠️ una sola spatial stream |
| TX retries | **1979 su 9666 pacchetti ≈ 20%** | ❌ un pacchetto su cinque ritrasmesso |
| Ping gateway | avg **146 ms**, max 546 ms, jitter 231 ms | ❌ pessimo per essere il primo hop |

**Conclusione.** Il pinning ha funzionato tecnicamente, ma la scelta dell'AP era discutibile: quei 146 ms di media **verso il gateway** non sono congestione di rete, sono il tratto radio che ritrasmette. Ho scambiato un problema di contesa con un problema di SNR.

> [!abstract] La lezione
> Un ping alto **verso il gateway** accusa il link radio. Un ping basso verso il gateway ma alto verso Internet accusa la rete a monte. Misurare i due separatamente è il primo gesto diagnostico, sempre.

---

## ⚖️ Il trade-off vero: segnale vs congestione

Perché "AP più lontano ma meno affollato" non è gratis:

1. **Rate adaptation.** Il WiFi adatta la modulazione all'SNR. Segnale debole → MCS basso → da 1170 Mbit/s nominali scendi a 14. Non è una penalità lineare, è un crollo.
2. **Il costo delle ritrasmissioni.** Ogni frame non riscontrato viene rispedito, occupando di nuovo il canale. Al 20% di retry stai bruciando un quinto del tuo tempo d'aria in puro spreco.
3. **Il problema della stazione lenta** *(slow station / airtime anomaly)*. Questa è la parte controintuitiva: il mezzo è **condiviso nel tempo**, non in banda. Un client a 14 Mbit/s impiega ~80 volte più tempo d'aria di uno a 1170 Mbit/s per trasmettere gli stessi byte. Quindi:
   - **peggiori tu**, perché sei lento;
   - **peggiori tutti gli altri** su quell'AP, perché mentre parli tu nessun altro può trasmettere.

   In pratica, agganciarsi da lontano a un AP scarico è il modo più efficace per renderlo affollato.

> [!question] E allora qual è la scelta giusta?
> Nella maggior parte dei casi **l'AP vicino congestionato batte quello lontano libero**, perché la congestione degrada in modo graduale mentre l'SNR basso degrada in modo catastrofico. Il pinning su un AP distante ha senso solo quando quello vicino è *davvero* saturo — e "davvero saturo" va misurato, non supposto.

---

## 📏 Come misurare la congestione (e i limiti che ho trovato)

### Il metodo standard: BSS Load Element

Lo standard 802.11 prevede un IE (ID 11) nei beacon/probe response con esattamente quello che serve:

- `station count` — quanti client associati
- `channel utilisation` — occupazione del canale su scala 0–255 (oltre ~150 è saturo)
- `available admission capacity`

```bash
iw dev wlp1s0 scan dump | grep -A3 -i "BSS Load"
```

> [!failure] Sugli AP Sapienza non funziona
> Ho ispezionato tutti gli IE annunciati dagli AP `sapienza` e il **BSS Load non c'è**. Annunciano SSID, supported rates, DS Parameter, Country (IT), Power constraint, RM enabled capabilities, HT/VHT capabilities, Extended capabilities, Transmit Power Envelope, WMM — ma niente BSS Load. È opzionale nello standard e va abilitato sul controller; qui non lo è.

### L'altra strada che non funziona: survey dump

```bash
iw dev wlp1s0 survey dump   # channel active time / busy time
```

> [!failure] Vuoto su `iwlwifi`
> In teoria dà il *channel busy time* misurato dalla scheda, che è il dato migliore in assoluto. In pratica il driver Intel non espone queste statistiche a userspace: sull'AX210 l'output è vuoto. Su schede Atheros (`ath9k`/`ath10k`) invece funziona benissimo — buona ragione per tenersi una chiavetta USB Atheros se vuoi fare misure sul serio.

### Quello che resta: misura empirica

Dato che gli strumenti dichiarativi non ci sono, si misura per differenza. Metodo:

```bash
for AP in C8:0C:C8:E5:84:15 00:06:F4:D9:44:55; do
  nmcli con mod "sapienza" 802-11-wireless.bssid $AP
  nmcli con up "sapienza" >/dev/null
  sleep 5
  echo "=== $AP ==="
  iw dev wlp1s0 link | grep -E "signal|tx bitrate"
  ping -c 20 -i 0.2 -q $(nmcli -g IP4.GATEWAY dev show wlp1s0) | tail -2
done
```

Confronta `tx bitrate` (salute radio) e il jitter del ping (contesa + salute radio). L'AP che vince su entrambi è quello giusto.

---

## 📡 Canali, bande e DFS

Dallo scan, i canali `sapienza` in portata: 36, 48, 52, 60, 100, 132.

| Gruppo | Canali | Banda | DFS? |
|---|---|---|---|
| UNII-1 | 36–48 | 5.18–5.24 GHz | No |
| UNII-2A | 52–64 | 5.26–5.32 GHz | **Sì** |
| UNII-2C | 100–144 | 5.5–5.72 GHz | **Sì** |
| UNII-3 | 149–165 | 5.745–5.825 GHz | No |

**DFS** = *Dynamic Frequency Selection*. Su quei canali il WiFi è ospite: la banda è primariamente dei radar (meteo, militari, aviazione). L'AP deve monitorare, e se rileva un radar **deve liberare il canale entro 10 secondi** e spostarsi altrove.

Conseguenze pratiche che ti riguardano:

- I canali DFS sono in genere **meno affollati** (molti dispositivi consumer li evitano) → più interessanti per il pinning.
- Ma un evento radar ti disconnette di colpo. Se ti aggreghi a un AP su canale 100 (come in questo caso) e la connessione cade senza motivo apparente, il sospetto numero uno è un DFS event.
- L'AP su canale DFS deve fare *Channel Availability Check* per 60 s prima di trasmettere dopo un cambio: per questo a volte "sparisce" per un minuto.

Nota anche `Country: IT` e `Power constraint: 3 dB` negli IE: l'AP ti sta comunicando il dominio regolatorio e ti impone di ridurre la potenza di trasmissione di 3 dB. Il tuo client obbedisce — ed è un altro pezzo del perché il link lontano andava male.

---

## ↩️ Rollback

```bash
# Rimuovi il pinning, torna al roaming libero
nmcli con mod "sapienza" 802-11-wireless.bssid ""
nmcli con up "sapienza"

# Oppure torna semplicemente al profilo che roama già
nmcli con up "sapienza 1"
```

> [!danger] Non dimenticare che è pinnato
> Col BSSID fissato **il roaming è disattivato**. Cambi aula, il segnale scende, e il client resta agganciato finché il link non muore invece di passare all'AP accanto. È il sintomo classico da "WiFi che non va e non capisco perché" tre settimane dopo aver fatto questo esperimento.

---

## 📋 Cheatsheet

```bash
# --- Ricognizione ---
nmcli dev wifi rescan
nmcli -f IN-USE,BSSID,SSID,CHAN,FREQ,SIGNAL dev wifi list
iw dev wlp1s0 scan dump | grep -E "^BSS|SSID:|signal:|freq:"

# --- Stato attuale ---
iw dev wlp1s0 link
iw dev wlp1s0 station dump
nmcli dev show wlp1s0 | grep -E "IP4.ADDRESS|IP4.GATEWAY|GENERAL.DRIVER"
nmcli networking connectivity check

# --- Pinning ---
nmcli con mod "<profilo>" 802-11-wireless.bssid <BSSID>
nmcli con mod "<profilo>" 802-11-wireless.bssid ""        # rimuovi
nmcli con mod "<profilo>" 802-11-wireless.band a          # solo 5 GHz
nmcli con mod "<profilo>" connection.autoconnect no
nmcli con up "<profilo>"
nmcli con down "<profilo>"

# --- Profili ---
nmcli con show
nmcli con clone "<sorgente>" <nuovo-nome>
nmcli -f all con show "<profilo>"                         # ogni singola proprietà

# --- Diagnostica ---
ping -c 20 $(nmcli -g IP4.GATEWAY dev show wlp1s0)        # link radio
ping -c 20 1.1.1.1                                        # rete a monte
journalctl -u NetworkManager -f                           # log live (roaming, DFS, auth)
wpa_cli -i wlp1s0 status                                  # stato del supplicant
```

---

## 🧭 Da approfondire (esperimenti per imparare)

- [ ] **Neighbor report 802.11k.** Gli AP lo supportano. Prova `wpa_cli -i wlp1s0 neighbor_rep_request` mentre sei connesso: se risponde, hai la lista degli AP vicini *secondo l'infrastruttura*, che è molto più affidabile del tuo scan.
- [ ] **Leggere i beacon con Wireshark.** Metti la scheda in monitor mode (`iw dev wlp1s0 set monitor control`) e filtra `wlan.fc.type_subtype == 8`. Vedi gli IE dal vivo e capisci cosa un AP annuncia davvero. ⚠️ In monitor mode perdi la connessione.
- [ ] **Confrontare `iwlwifi` e `ath9k`** su `survey dump`, per toccare con mano quanto la visibilità dipenda dal driver.
- [ ] **Capire perché `sapienza` è aperta** (`SECURITY: --`) mentre `eduroam` è `WPA2 802.1X`. Che implicazioni ha per il traffico? (spoiler: su rete aperta senza OWE **non c'è cifratura a livello 2**, chiunque in portata con una scheda in monitor mode legge tutto ciò che non è già cifrato sopra — usa `eduroam`, o una VPN).
- [ ] **`wpa_supplicant` bgscan.** Si può configurare il roaming aggressivo (`bgscan="simple:30:-65:300"`) per far cercare al client un AP migliore quando scende sotto -65 dBm. Alternativa intelligente al pinning manuale.
- [ ] **Airtime fairness.** Approfondire come il kernel Linux (`mac80211`) implementa lo scheduler AQL/airtime e perché mitiga il problema della stazione lenta.

---

## 🔗 Collegamenti

- [[Network Discovery — Scansione LAN]]
