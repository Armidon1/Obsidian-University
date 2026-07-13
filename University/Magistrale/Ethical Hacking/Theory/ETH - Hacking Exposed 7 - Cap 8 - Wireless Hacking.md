---
tags: [ethl, hacking-exposed-7, wireless, wifi, 802-11, wep, wpa, cap8]
capitolo: 8
data: 2026-07-13
collegamenti: ["[[ETHL - Cap 7 Remote Connectivity e VoIP Hacking]]", "[[ETHL - Cap 6 Cybercrime e APT]]", "[[ETHL - LAN Manager (LM) vs NTLM]]"]
---

# ETHL — Cap 8 · Wireless Hacking

> [!abstract] Il filo del capitolo
> Il wireless rompe il perimetro con la fisica: le onde radio escono dai muri, quindi si attacca dal parcheggio (wardriving). Da qui due assi. **Primo**: la scoperta è inarrestabile, perché i management frame 802.11 (beacon, probe, association) viaggiano *sempre in chiaro* — perciò ogni difesa basata sul nascondere (SSID nascosto, MAC filtering) è teatro. **Secondo**: l'unica barriera vera è la crittografia, e vale quanto la sua chiave più debole. WEP è rotto per costruzione, WPA-PSK cade con passphrase deboli, LEAP/MS-CHAPv2 è carta velina; regge solo WPA2/3-AES con segreti forti, e PEAP/EAP-TTLS *solo se* il client valida il certificato del server. Aggancio al Cap. 7: di nuovo «il perimetro non è il firewall» e «l'anello debole è l'autenticazione».

## Le basi 802.11

Le reti Wi-Fi lavorano nelle bande ISM (Industrial, Scientific, Medical) non licenziate. A 2.4 GHz stanno 802.11 b/g/n con canali 1–14 di cui solo 1, 6 e 11 non si sovrappongono; a 5 GHz stanno 802.11 a/n con canali 36–165, tutti non sovrapposti. La distinzione conta perché tool e attaccante saltano di canale per coprire lo spettro. Una rete può essere in modalità *infrastructure* (tutto passa da un access point, il caso comune) o *ad hoc* (i dispositivi si parlano peer-to-peer, come un cavo crossover).

La connessione è un rituale in tre passi, ed è il primo «meccanismo con un movimento» del capitolo. Il client manda una **probe request** per l'SSID che cerca, la ripete su ogni canale e attende una **probe response**. Segue l'**autenticazione**, che può essere *open* (l'AP accetta chiunque) o *shared-key* (quasi mai usata, e solo con WEP). Infine l'**association**: il client manda una association request e l'AP risponde con una association response. Due cose da fissare: l'SSID compare in praticamente tutti questi frame — quindi la scoperta è inevitabile — e questa «autenticazione» non è cifratura: i meccanismi WPA non toccano questa fase, agiscono dopo.

## Difese deboli — e perché non reggono

> [!warning] Difese di facciata
> **MAC filtering**: ogni indirizzo va inserito a mano nella lista degli approvati (alto sforzo, bassa sicurezza); l'attaccante sniffa i MAC dei client legittimi e li spoofa — su Windows con SMAC, dal Device Manager della scheda, o con Bwmachak per le vecchie Orinoco.
> **SSID nascosto**: si omette l'SSID dai beacon, ma l'SSID viaggia comunque in probe e association request; basta un frame di deauth per forzare una riassociazione e leggerlo. Paradosso segnalato da Microsoft: nascondere l'SSID rende *il client* meno sicuro, perché continua a spammare probe request cercando la rete e si espone all'impersonation dell'AP.

Il motivo comune è uno solo: i management frame non sono cifrati, e gli indirizzi sorgente/destinazione degli 802.11 sono sempre in chiaro. Basta questo perché i tool mappino le associazioni tra client e AP senza rompere nulla.

## Il paesaggio crittografico

Lo standard 802.11i definisce la cifratura. WPA ne implementa solo una parte (TKIP); WPA2/3 la implementano tutta (TKIP **e** AES). Le opzioni concrete sono tre: WEP usa RC4 ed è banalmente sfruttabile; TKIP fu il rimpiazzo rapido di WEP (gira su hardware vecchio, usa ancora RC4, nessuna vulnerabilità maggiore nota ma ormai legacy); AES è il più sicuro e raccomandato, con CCMP su WPA2 e GCM (con SHA-384 come HMAC) su WPA3.

| Standard | Cifrario | Algoritmo / modo | Stato |
|---|---|---|---|
| WEP | RC4 | keystream da WEP key + IV | rotto, crackabile in ~5 min |
| WPA | RC4 | TKIP | transitorio, legacy; nessuna vuln maggiore nota |
| WPA2 | AES | CCMP | robusto (KRACK 2017 colpisce l'handshake) |
| WPA3 | AES | GCM, SHA-384 come HMAC | il più recente e sicuro |

Sul fronte della gestione delle chiavi si distinguono due mondi. In **WPA-Personal (PSK)** una sola password vale per tutti, sta memorizzata sui client e va cambiata a mano ovunque quando cambia sull'AP; l'accesso non è gestibile per singolo utente e il rischio è che basti *un* utente a divulgare la PSK. In **WPA-Enterprise (802.1x)** il client presenta le proprie credenziali aziendali a un server RADIUS via EAP (EAP-TTLS, PEAP, EAP-FAST); l'utente non tocca mai le chiavi di cifratura, quindi l'attaccante non può estrarle dai client e l'accesso è revocabile per singolo utente.

> [!info] Four-way handshake
> Sia PSK sia Enterprise usano un handshake a quattro vie per derivare la **PTK** (Pairwise Transient Key, per l'unicast) e la **GTK** (Group Temporal Key, per multicast/broadcast). Meccanica della PTK: l'AP manda un numero casuale (**ANonce**) al client; il client risponde col suo (**SNonce**); l'AP calcola la PTK dai due nonce e invia un messaggio cifrato; il client lo decifra con la PTK. Perché conta per l'attacco: la derivazione è alimentata da PSK + SSID, quindi catturare l'handshake apre al **crack offline** della PSK. Non serve restare connessi — un deauth forza la riconnessione e quindi un nuovo handshake da catturare.

## Equipaggiamento e ricognizione

Il driver del chipset limita quanto controllo hai sulla NIC, e la maggior parte delle schede non serve per l'hacking wireless. Le schede citate come valide sono USB con chipset Atheros (Ubiquiti SRC) o Ralink (Alfa AWUS050NH), dual band 2.4/5 GHz e antenna esterna. Il vero prerequisito è la **monitor mode**: senza, vedi solo traffico di livello superiore ma non i management frame 802.11 — cioè niente scoperta e niente cattura handshake. Per i tool, Linux e Kali stanno molto avanti a Windows (dove senza AirPcap o OmniPeek gli strumenti sono pochi e deboli); Kali gira in VM solo con NIC USB, altrimenti va su bare metal, USB o LiveCD. Antenne direzionali (Cantenna, Yagi, patch/panel, biquad dish) allungano la portata, e GPS + software di wardriving mappano gli AP, con archivi collaborativi come WiGLE.

La scoperta ha due modalità. Quella **attiva** manda broadcast probe request e registra le risposte, ma manca gli AP configurati per ignorarle (è ciò che fa NetStumbler). Quella **passiva** ascolta ogni canale e registra ogni AP visto col suo MAC: tecnica migliore, usata da Kismet e airodump-ng. Lo sniffing è facile se il traffico non è cifrato, gli attacchi MITM sono comuni (e possono violare le leggi sulle intercettazioni); Kismet salva tutto in PCAP e Wireshark serve a ispezionare i frame.

Un mattone che ricorre in tutti gli attacchi è il **deauth DoS**. La disconnessione forzata è un meccanismo 802.11 legittimo, ma i frame di deauth non sono autenticati: l'attaccante ne spoofa uno che sembra venire dall'AP. Con aireplay-ng si mandano 64 deauth all'AP a nome del client e 64 al client a nome dell'AP. Oltre al DoS puro, serve soprattutto a forzare riconnessioni per leggere l'SSID dalle probe request o per catturare il 4-way handshake WPA.

## Guadagnare accesso — gli attacchi

**WEP è rotto per costruzione.** L'IV (Initialization Vector) è pseudocasuale per ogni frame e viaggia *in chiaro* nell'header; il keystream RC4 nasce da WEP key + IV. In trasmissione si fa XOR tra plaintext e keystream per ottenere il ciphertext; in ricezione si rigenera il keystream da WEP key + IV (letto dall'header) e si fa di nuovo XOR per tornare al plaintext. Il difetto: gli IV sono corti, quindi si ripetono; due frame con lo stesso IV, confrontando i ciphertext, lasciano indovinare il keystream e da lì la WEP key. I frame ARP, quasi identici tra loro, moltiplicano gli IV duplicati. Il brute-force dello spazio chiavi sarebbe settimane anche a 40 bit, ma raccogliere IV rende tutto rapidissimo. Due modalità: l'**attacco passivo** cattura abbastanza data frame, ne estrae gli IV e deduce la chiave (~60.000 IV per una chiave a 104 bit) — airodump-ng cattura in PCAP, aircrack-ng analizza statisticamente e si ferma su «KEY FOUND»; l'**ARP replay con fake authentication** è la via attiva (~5 min): si spoofa il MAC di un client valido con un fake authentication attack (open auth, senza inviare dati reali), poi si rigioca una ARP request così che l'AP ribroadcasti con un IV nuovo ogni volta, e gli IV si accumulano in fretta. La sequenza è airodump-ng (cattura) → aireplay-ng (fake auth) → aireplay-ng in un'altra finestra (ARP replay) → aircrack-ng (crack). Tool storici sul difetto IV: AirSnort, WEPAttack, DWEPCrack.

> [!danger] Mai usare WEP
> La contromisura è una sola ed esclusiva: non usare WEP, mai. Passare a WPA2/3 con AES.

**WPA-PSK cade con passphrase debole.** WPA non aveva vulnerabilità maggiori «fino al 2017» (il riferimento è a KRACK, che colpisce il 4-way handshake). Il punto debole resta la PSK: condivisa fra tutti gli utenti, lunga 8–63 caratteri, hashata 4096 volte insieme all'SSID — se è lunga e casuale servono trilioni di tentativi. L'attacco è **offline**: si cattura il 4-way handshake (aspettando, o forzandolo con un deauth) e poi si bruteforza in locale. Tool: aircrack-ng (dizionario + PCAP), coWPAtty (rainbow table specifiche per SSID, ~40 GB, generate sui top 1000 SSID di WiGLE), Pyrit (hashing scaricato su GPU). Mitigazione: PSK complessa e SSID unico (le rainbow table sono legate all'SSID) — ma basta un utente a divulgare la chiave.

**WPA-Enterprise: si attacca l'EAP.** Qui non c'è una chiave condivisa da rubare, quindi il bersaglio è il protocollo EAP. Prima si identifica il tipo: si cattura l'handshake EAP, Wireshark ne mostra il tipo e lo username viaggia in chiaro verso il RADIUS. Il caso peggiore è **LEAP** (Cisco, 2000): schema 802.1X su RADIUS nato per rimediare a WEP, ma con zero resistenza al dizionario offline perché si appoggia solo a MS-CHAPv2. E MS-CHAPv2 è fragile — niente SALT negli hash NT, chiave DES debole da 2 byte, username in chiaro — così le rainbow table (DB da ~4 GB) rendono il crack efficiente. Cisco sostiene che LEAP sia sicuro solo con password ≥10 caratteri random, che quasi nessuno usa, quindi in pratica si cracca in giorni o minuti. Tool: asleap estrae e cracca le password LEAP deboli, ed è integrato con Air-Jack per buttare giù gli utenti autenticati; alla riautenticazione la password viene sniffata e crackata. Verdetto: evitarlo come WEP. (È lo stesso mondo degli hash NT senza salt di [[ETHL - LAN Manager (LM) vs NTLM]]; e Microsoft stessa sconsiglia PPTP/MS-CHAP dopo la CloudCracker di Moxie Marlinspike — ~200 $ in 24 h — raccomandando PEAP, L2TP/IPsec, IPSec+IKEv2 o SSTP.)

Meglio stanno **EAP-TTLS e PEAP**, che incapsulano un protocollo di autenticazione interno — spesso debole (MS-CHAPv2, EAP-GTC a password monouso, o cleartext) — dentro un tunnel TLS. La cifratura TLS non si rompe direttamente, ma resta la via dell'**AP impersonation / MITM**: se il client è mal configurato e non valida il certificato del server RADIUS, l'attaccante tira su un finto AP/RADIUS (hostapd per fare da AP, FreeRADIUS-WPE che accetta qualunque connessione e logga tutto), fa da terminatore del tunnel TLS e legge l'autenticazione interna, poi la bruteforza offline con asleap. La contromisura decisiva è spuntare «Validate server certificate» su *tutti* i client.

| Bersaglio | Come si buca | Tool | Contromisura |
|---|---|---|---|
| WEP | IV in chiaro + riuso → keystream → chiave; passivo o ARP replay + fake auth (~5 min) | airodump-ng, aireplay-ng, aircrack-ng | non usarlo mai → WPA2/3-AES |
| WPA / WPA2-PSK | cattura 4-way handshake (deauth per forzarlo) → dizionario offline | aircrack-ng, coWPAtty, Pyrit | PSK lunga e casuale + SSID unico |
| WPA-Ent. LEAP | MS-CHAPv2 senza salt → dizionario offline | asleap, Air-Jack | abbandonarlo (come WEP) |
| WPA-Ent. PEAP/TTLS | AP impersonation/MITM se il certificato non è validato | hostapd, FreeRADIUS-WPE, asleap | validare il certificato del server su tutti i client |

> [!summary] Gerarchia delle difese
> WEP: passivo o ARP replay, ~5 min, da non usare mai. WPA-PSK: bruteforzabile offline, regge solo con passphrase ad alta entropia, e una PSK per tutti è un rischio da singolo utente. WPA-Enterprise: LEAP da abbandonare; EAP-TTLS/PEAP relativamente sicuri grazie alla cifratura multilivello, ma esposti ad AP impersonation/MITM → validare *sempre* il certificato del server. Filo conduttore: nascondere non protegge (management frame in chiaro), protegge solo cifrare bene con segreti forti.

> [!tip] Candidati Excalidraw
> Due meccanismi «con un movimento» da ridisegnare a mano (non liste da riconoscere): il **keystream WEP** — IV + WEP key → RC4 → XOR, evidenziando il riuso dell'IV come punto di rottura; e il **4-way handshake** — ANonce/SNonce → PTK, marcando dove l'attaccante cattura per il crack offline e dove si inserisce il deauth. Timer 3–4 minuti, tenerli grezzi.

> [!todo] Homework #5
> Copre Cap. 6–8, formato «problema, soluzione con spiegazione, screen dump». Item wireless: **#5** (30 pt) — allestire client + AP senza cifratura e sniffare/decodificare i data frame con Wireshark o airodump-ng; **#6** (50 pt) — crackare una WEP key con la suite aircrack-ng passando per cattura frame → fake authentication → ARP replay → key cracking. Da tenere d'occhio anche l'**#4** (20 pt, Aggressive mode VPN con Nmap/NTA Monitor/IKEProbe), che aggancia il Cap. 7.
