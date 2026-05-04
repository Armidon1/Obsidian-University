# WiGLE

## Cos'è

WiGLE (Wireless Geographic Logging Engine) è un **database crowdsourced** di reti WiFi e celle mobili mappate fisicamente. Chiunque può contribuire aggiungendo reti e chiunque può interrogarlo.

Sito: https://wigle.net

---

## Come funziona

Ogni router WiFi ha un **MAC address unico e fisso**. WiGLE associa ogni MAC address a coordinate GPS — raccolte da utenti che girano con smartphone o antenne WiFi registrando le reti che incontrano (attività chiamata **wardriving**).

```
Utente gira con smartphone → rileva router vicini → carica MAC + GPS su WiGLE
```

Il risultato è una mappa globale che associa MAC address → posizione fisica.

---

## Utilizzo nel footprinting / OSINT

Se un attaccante conosce il MAC address del router di una vittima, può interrogare WiGLE per ottenerne la posizione fisica:

```
MAC del router → query WiGLE → coordinate GPS → posizione fisica
```

Questo è esattamente il meccanismo sfruttato da Samy Kamkar nella talk **"How I Met Your Girlfriend"** (BlackHat 2010), originariamente tramite le API di Google — oggi WiGLE è un'alternativa accessibile senza autenticazione obbligatoria.

---

## Differenza con le API Google/Apple

||WiGLE|Google/Apple|
|---|---|---|
|Accesso|Libero (account gratuito)|API key autenticata|
|Copertura|Centinaia di milioni di reti|Miliardi di reti|
|Monitoraggio abusi|Limitato|Attivo|
|Fonte dati|Crowdsourcing (wardriving)|Street View + dispositivi utenti|

---

## Wardriving

Il wardriving è la pratica di girare fisicamente con un'antenna WiFi (o semplicemente uno smartphone) registrando:

- SSID della rete
- MAC address del router (BSSID)
- Potenza del segnale
- Coordinate GPS nel momento del rilevamento

Non è illegale rilevare reti WiFi pubblicamente trasmesse — è illegale connettersi senza autorizzazione.

---

## Protezioni contro il tracking tramite WiGLE

- **MAC address randomization** — protegge i **client** (telefoni, laptop) ma non i router
- **Cambiare il MAC del router** — possibile ma raro, richiede configurazione manuale
- **Router mesh moderni** — alcuni supportano la rotazione periodica del BSSID

⚠️ Il MAC del router domestico è tipicamente **fisso per tutta la vita del dispositivo** — una volta mappato su WiGLE, la posizione è permanentemente associata a quel MAC.

---
## Perché casa tua non è mappata

WiGLE dipende interamente dal **crowdsourcing** — se nessun utente ha mai fatto wardriving in quella strada con l'app WiGLE attiva, il router non è nel database. Le zone periferiche o i quartieri residenziali tranquilli sono spesso poco coperti.

---

## Cosa vedi invece

Nota che sulla mappa vedi scritto **"DAILY LIMIT"** e **"INPUT ERROR"** ovunque — questo significa che hai raggiunto il limite di query giornaliere da utente non loggato. WiGLE limita le ricerche anonime proprio per scoraggiare l'uso automatizzato.

Con un account gratuito il limite è molto più alto.

---

## Le limitazioni pratiche di WiGLE

|Situazione|Copertura|
|---|---|
|Centro città / zone commerciali|Alta|
|Quartieri residenziali|Media|
|Zone rurali / periferia|Bassa o assente|
|Router installato di recente|Assente finché qualcuno non lo mappa|

---

## Il punto educativo

Questo dimostra che **nessuno strumento è infallibile**. Un attaccante reale combina più fonti — WiGLE, Google Geolocation API, Apple, database proprietari — per aumentare le probabilità di trovare il target. Se uno non ce l'ha, forse ce l'ha un altro.


## Related Notes

- [[Tor]]
- [[Proxychains]]
- [[OSINT & Footprinting]]
- [[How I Met Your Girlfriend — Samy Kamkar]]
- [[MAC Address Randomization]]

---

_References: https://wigle.net · Samy Kamkar — BlackHat 2010 · Linux Basics for Hacking — OccupyTheWeb_