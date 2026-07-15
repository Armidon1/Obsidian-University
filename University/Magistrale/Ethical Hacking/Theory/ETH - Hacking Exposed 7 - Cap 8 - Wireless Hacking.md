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

Le reti Wi-Fi lavorano nelle bande ISM (Industrial, Scientific, Medical) non licenziate. A 2.4 GHz stanno 802.11 b/g/n con canali 1–14 di cui solo 1, 6 e 11 non si sovrappongono; a 5 GHz stanno 802.11 a/n con canali 36–165, tutti non sovrapposti. La distinzione conta perché tool e attaccante saltano di canale per coprire lo spettro. 

#### Ma la distinzione a/b/c/d è perché i frame sono proprio diversi?
Sì, ottima intuizione da separare bene: le lettere **a/b/g/n non sono protocolli diversi**, sono _emendamenti_ allo stesso standard 802.11, e ciò che cambia è quasi tutto al **livello fisico (PHY)** — banda, modulazione, velocità, numero di antenne — non l'identità del protocollo. Ecco il quadro:

|Standard|Anno|Banda|Modulazione|Velocità max|Novità|
|---|---|---|---|---|---|
|802.11b|1999|2.4 GHz|DSSS/CCK|11 Mbps|prima diffusione di massa|
|802.11a|1999|5 GHz|OFDM|54 Mbps|OFDM, sale a 5 GHz|
|802.11g|2003|2.4 GHz|OFDM|54 Mbps|OFDM a 2.4 GHz, retrocompatibile con b|
|802.11n|2009|2.4 + 5 GHz|OFDM + **MIMO**|~600 Mbps|più antenne, canali da 40 MHz, aggregazione|

(Poi ac e ax/Wi-Fi 6 proseguono su questa strada: canali più larghi, MU-MIMO, OFDMA.)

**E il frame? Qui la risposta è a due strati**, ed è il cuore della tua domanda. Quello che va sull'aria non è un blocco unico: è un frame MAC (comune) avvolto in un involucro PHY (che cambia).![[Pasted image 20260714162736.png]]Quindi, per rispondere secco: la **struttura del frame MAC** — l'header con Frame Control, Duration, gli indirizzi, la sequenza, e la tassonomia management/control/data — è **la stessa** in a/b/g/n. È una scelta deliberata, serve all'interoperabilità e al fatto che i dispositivi condividano lo stesso metodo di accesso al mezzo (CSMA/CA). Quello che cambia davvero «sul filo» è l'**involucro PHY**: preambolo e header fisico sono diversi (preambolo DSSS per b, preambolo OFDM con campo SIGNAL per a/g, preambolo HT con training MIMO per n), perché è lì che si segnala al ricevitore _come_ demodulare. L'unica eccezione che tocca il MAC è l'802.11n, che **aggiunge** roba retrocompatibile (il campo HT Control, l'aggregazione di più frame, i block ACK) — ma il frame di base resta riconoscibilmente lo stesso.

Il collegamento con l'ethical hacking chiarisce perché nel capitolo si parla di «management frame 802.11» senza specificare la lettera: quei frame (beacon, probe, deauth) stanno al livello MAC **comune**, quindi un attacco come il deauth o lo sniffing dell'SSID funziona uguale su b, g o n. I due vincoli pratici sono altrove: la scheda in monitor mode deve saper **demodulare quel PHY** (una vecchia scheda b/g non cattura ac/ax), e la **banda** diversa (2.4 vs 5 GHz) è proprio il motivo per cui i tool fanno channel hopping su entrambe.

Se ti è utile, infilo questa tabella a/b/g/n + la distinzione PHY-involucro / MAC-comune come [!info] «a/b/g/n: cosa cambia» nella sezione «Le basi 802.11» del Cap. 8 — è un chiarimento che a un esame vale, e resta agganciato al punto dei canali.

#### Ripasso: fisicamente che cos'è un onda radio 2.4GHz
Ottima domanda — è il salto che i corsi saltano sempre. Provo a darti un'immagine fisica solida.

**Cos'è un'onda radio.** Un'onda radio è la _stessa_ cosa della luce: un'onda elettromagnetica. La differenza con un'onda del mare o con il suono è cruciale: qui non oscilla nessuna materia. Non c'è nulla che «sale e scende» fisicamente — non aria, non acqua. Quello che oscilla è il **campo elettromagnetico**: in ogni punto dello spazio c'è un'intensità di campo elettrico, e al passaggio dell'onda quell'intensità cresce, torna a zero, si inverte, ricresce dall'altra parte, e così via. Proprio perché non ha bisogno di un mezzo, un'onda radio attraversa anche il vuoto (è così che la luce del Sole ci arriva). E si muove a una sola velocità: quella della luce, ~300.000 km/s.

Quindi quando disegno un'ondina sinusoidale, l'altezza della curva **non è una posizione nello spazio** — è l'intensità (e il verso) del campo elettrico in quel punto e in quell'istante. Il «+» in alto e il «−» in basso sono il campo che punta in un verso o nell'altro; lo zero è il campo nullo.

**Cos'è la frequenza (2.4 GHz).** La frequenza è semplicemente _quante volte al secondo_ il campo completa un ciclo su-e-giù completo. 1 Hz = 1 ciclo al secondo; 2.4 GHz = 2,4 **miliardi** di cicli al secondo. Al tuo router il campo elettrico si inverte avanti e indietro 2.400.000.000 di volte ogni secondo — un tremolio velocissimo. C'è un'ancora concreta: siccome l'onda viaggia a velocità della luce, in un ciclo percorre una certa distanza, la **lunghezza d'onda** (λ = velocità della luce ÷ frequenza). Per 2.4 GHz viene ~12,5 cm. È il motivo per cui le antenne Wi-Fi sono lunghe pochi centimetri. Prova a muovere lo slider qui sotto: alza la frequenza e vedrai l'onda «stringersi» e la λ accorciarsi.![[Screencast From 2026-07-13 17-14-14.mp4]]**Dove sta 2.4 GHz.** Se metti in fila tutte le onde elettromagnetiche per frequenza crescente: radio AM ~1 MHz, radio FM ~100 MHz, poi il Wi-Fi a 2,4 e 5 GHz, e molto più su la luce visibile (~500.000 GHz). Il Wi-Fi vive nella regione delle **microonde** — e non è un caso che il forno a microonde lavori a ~2,45 GHz, praticamente lì accanto: è una frequenza a cui l'acqua assorbe bene energia. Alzare la frequenza (5 GHz, λ ~6 cm) dà onde più corte: penetrano peggio i muri ma lasciano più spazio per i dati.

**E i canali, adesso.** Quella «2.4 GHz» in realtà non è _una_ frequenza esatta, è una **banda**: un intervallo che va da ~2400 a ~2483 MHz. Un canale è una fetta di quella banda — una frequenza centrale precisa dove un apparecchio parcheggia il suo segnale, esattamente come le stazioni FM (88.5, 92.3, 100.1…) sono frequenze diverse per non pestarsi. Il canale 1 è centrato a 2412 MHz, il 6 a 2437, l'11 a 2462.

Il pezzo che chiude il cerchio con lo schema di prima: un segnale Wi-Fi **non è infinitamente sottile**. Per trasportare dati veloci deve _allargarsi_ su un intervallo di frequenze (~22 MHz), non stare su un singolo valore — più dati spingi, più «largo» diventa (è il senso letterale di _banda larga_/bandwidth). Ecco perché ogni canale occupa una fetta larga ~22 MHz attorno al suo centro, e perché in una banda da soli ~83 MHz ci stanno appena tre fette che non si toccano: **1, 6, 11**. La frequenza dice _dove_ sei sul quadrante; la larghezza dice _quanto spazio occupi_ — ed è la larghezza che causa la sovrapposizione.

 Guarda qui [[ETH - Onde radio, frequenza e canali]]

#### Ma perché esiste l'overlapping?
Buona domanda: è uno dei punti dove la slide dice «non-overlapping: 1, 6, 11» senza spiegare il _perché_.

Il nocciolo è uno scarto tra due numeri. I **numeri di canale** a 2.4 GHz sono spaziati di 5 MHz l'uno dall'altro (canale 1 = 2412 MHz, canale 2 = 2417, … canale 11 = 2462). Ma un canale Wi-Fi reale non è largo 5 MHz: occupa **circa 20–22 MHz** di banda attorno alla sua frequenza centrale. Larghezza maggiore della spaziatura significa che canali con numeri vicini si **sovrappongono fisicamente** nello spettro: il canale 1 e il canale 2 sono quasi completamente accavallati.

Il "senso" quindi è che l'overlapping non è una funzione utile — è un **effetto collaterale** dello schema di numerazione. E conta perché due AP su canali sovrapposti si fanno **interferenza**. Attenzione alla distinzione: due AP sullo _stesso_ canale si «sentono» e si alternano educatamente via CSMA/CA (condivisione ordinata, degradata ma pulita); due AP su canali _diversi ma sovrapposti_ (es. 1 e 3) **non riescono a decodificarsi** a vicenda, quindi non si coordinano affatto — si limitano ad alzarsi il rumore di fondo, con frame corrotti, ritrasmissioni e crollo del throughput. Paradossalmente l'interferenza da canale adiacente-sovrapposto è spesso _peggiore_ di quella da stesso canale.

Da qui la terna **1, 6, 11**: sono distanti 5 numeri di canale = 25 MHz, quanto basta perché tre canali da ~22 MHz stiano affiancati _senza_ toccarsi. Sono gli unici tre canali «puliti» in tutta la banda 2.4 GHz, che infatti è cronicamente affollata. A **5 GHz** invece la canalizzazione è progettata già non-sovrapposta (ogni canale da 20 MHz sta nel suo slot separato: 36, 40, 44, 48…) e i canali sono molti di più — motivo per cui i 5 GHz reggono molto meglio negli ambienti densi.Per _vederlo_, ecco lo spettro 2.4 GHz: le tre gobbe pulite sono 1, 6 e 11; la gobba intrusa mostra cosa succede scegliendo un canale intermedio.![[Pasted image 20260713170547.png]]Nota per l'esame: la larghezza reale del canale (~22 MHz) contro la spaziatura dei numeri (5 MHz) è tutto il trucco della domanda — è _da lì_ che nasce la terna 1/6/11. E c'è un aggancio col resto del capitolo: è anche il motivo per cui i tool di discovery e cattura _saltano di canale_ (channel hopping) — per coprire canali che si sovrappongono devono comunque campionarli uno a uno.

---
Una rete può essere in modalità *infrastructure* (tutto passa da un access point, il caso comune) o *ad hoc* (i dispositivi si parlano peer-to-peer, come un cavo crossover). Noi ci concentriamo su Infrastructure.

La **connessione** (in generale, non si intende solo l'autenticazione) è un rituale in tre passi, ed è il primo «meccanismo con un movimento» del capitolo. Il client manda una **probe request** per l'SSID che cerca, la ripete su ogni canale e attende una **probe response**. Segue l'**autenticazione** (si veda paragrafo successivo), che può essere *open* (l'AP accetta chiunque) o *shared-key* (quasi mai usata, e solo con WEP). Infine l'**association**: il client manda una association request e l'AP risponde con una association response. Due cose da fissare: l'SSID compare in praticamente tutti questi frame — quindi la scoperta è inevitabile — e questa «autenticazione» non è cifratura: i meccanismi WPA non toccano questa fase, agiscono dopo.

### Distinzione connessione con autenticazione
Ottima domanda, e la confusione è tutta in **una parola usata a due livelli**. I tuoi appunti sono corretti, ma bisogna leggerli bene: dicono che _la connessione_ è un rituale a tre passi — **probe → authentication → association** — non che «l'autenticazione» sia fatta di tre passi. In quel rituale «authentication» è il **nome del passo di mezzo**, uno dei tre, non il concetto intero.

E qui sta il nodo. Esistono due cose diverse che si chiamano entrambe «autenticazione», a due strati distinti:

Il passo 2 del rituale è l'**autenticazione 802.11 di link layer**: è la vecchia Open / Shared-Key di cui parlavamo. In una rete moderna è Open, cioè banale — l'AP dice «sì» a tutti. Serve solo a far avanzare la macchina a stati per arrivare all'association. Non c'entra con WPA.

Il **4-way handshake** invece **non è uno dei tre passi**: è una fase separata che parte _dopo_ l'association, e solo se la rete è WPA2/3. È lì che avviene l'autenticazione crittografica vera (prova della PMK, derivazione della PTK). Ecco perché negli appunti non compare tra i «tre passi»: appartiene a un momento successivo.

Quindi la sequenza completa reale è:![[Pasted image 20260714133201.png]]In sintesi: gli appunti non stanno descrivendo «l'autenticazione», stanno descrivendo il **rituale di connessione 802.11**, che ha tre passi — e uno di quei tre _si chiama_ authentication, ma è quello debole/nominale. Il 4-way handshake è un'altra fase, successiva. La parola sovraccarica è tutta la difficoltà.


## Autenticazione con un AP

**vediamo un po' meglio come funziona l'autenticazione con un AP:** qui «algoritmo di autenticazione» ha un senso tecnico preciso: nel frame 802.11 c'è proprio un campo _authentication algorithm number_, che vale 0 per **Open System** o 1 per **Shared Key**. Sono i due unici algoritmi di questa fase. Vediamoli.

**Open System** è banale: è uno scambio di due soli frame. Il client manda una authentication request, l'AP risponde con una authentication response e status «success». Nessuna credenziale viene verificata — l'AP accetta _chiunque_. Non è una vera autenticazione, è più un passaggio formale della macchina a stati 802.11 per passare allo stato «autenticato» e poter poi fare l'association. Tutta la sicurezza vera, in una rete WPA moderna, arriva _dopo_ (4-way handshake per PSK, EAP/802.1X per Enterprise). Per questo la nota dice che questa «autenticazione» non è cifratura.

**Shared Key** è quello interessante: un challenge-response a quattro frame basato su WEP. Il client chiede di autenticarsi; l'AP gli manda un **challenge**, cioè 128 byte casuali _in chiaro_; il client li cifra con la chiave WEP (keystream RC4 da chiave + IV) e li rimanda cifrati; l'AP decifra, confronta con l'originale e, se combaciano, risponde «success». L'idea è: dimostri di conoscere la chiave riuscendo a cifrare correttamente il challenge, senza mai trasmettere la chiave stessa.![[Pasted image 20260714131536.png]]Ed ecco il paradosso che rende Shared Key **peggiore** di Open, nonostante sembri più sicuro. Un attaccante che ascolta vede sia il challenge in chiaro $P$ (frame 2) sia la sua versione cifrata $C$ (frame 3). Siccome in WEP $C = P \oplus \text{keystream}$, basta uno XOR per ricavare $\text{keystream} = P \oplus C$. Ora ha un keystream valido (per quell'IV) e può cifrare da sé un challenge futuro, autenticandosi **senza aver mai conosciuto la chiave WEP**. In pratica Shared Key regala a chiunque ascolti una coppia testo-chiaro/testo-cifrato — cioè proprio ciò che serve per attaccare WEP. Per questo il corso dice «quasi mai usata»: aggiunge una vulnerabilità invece di toglierla, e Open + cifratura WEP finisce per essere più sicuro di Shared Key + WEP.

Il punto da portare a casa: entrambi questi algoritmi vivono al **livello MAC 802.11** e sono roba d'epoca WEP. In una rete WPA2/3 la fase di authentication usa sempre Open System (che dice «sì» a tutti), e l'autenticazione crittografica vera avviene più tardi — il 4-way handshake con la PSK, o EAP/RADIUS in Enterprise. È esattamente la frase della nota: _i meccanismi WPA non toccano questa fase, agiscono dopo_.

## Il paesaggio crittografico

Prima di parlare del 4 way handshake, parliamo degli algoritmi crittografici usati.
Lo standard 802.11i definisce la cifratura. WPA ne implementa solo una parte (TKIP); WPA2/3 la implementano tutta (TKIP **e** AES). Le opzioni concrete sono tre: WEP usa RC4 ed è banalmente sfruttabile; TKIP fu il rimpiazzo rapido di WEP (gira su hardware vecchio, usa ancora RC4, nessuna vulnerabilità maggiore nota ma ormai legacy); AES è il più sicuro e raccomandato, con CCMP su WPA2 e GCM (con SHA-384 come HMAC) su WPA3.

| Standard | Cifrario | Algoritmo / modo | Stato |
|---|---|---|---|
| WEP | RC4 | keystream da WEP key + IV | rotto, crackabile in ~5 min |
| WPA | RC4 | TKIP | transitorio, legacy; nessuna vuln maggiore nota |
| WPA2 | AES | CCMP | robusto (KRACK 2017 colpisce l'handshake) |
| WPA3 | AES | GCM, SHA-384 come HMAC | il più recente e sicuro |
WPA2 e 3 non si distinguono solo dal fatto che cifrano i dati (dopo il 4 way handshake) con [[AES-GCM]] od altro, ma anche da come ci si deriva quello che poi sarà il PMK (vedi dopo). Noi tratterremo solo il WPA2 che usa il PMKDF2 per trovarsi hashare una password in modo crittografico.

Sul fronte della gestione delle chiavi si distinguono due mondi. In **WPA-Personal (PSK)** una sola password vale per tutti, sta memorizzata sui client e va cambiata a mano ovunque quando cambia sull'AP; l'accesso non è gestibile per singolo utente e il rischio è che basti *un* utente a divulgare la PSK. In **WPA-Enterprise (802.1x)** il client presenta le proprie credenziali aziendali a un server RADIUS via EAP (EAP-TTLS, PEAP, EAP-FAST); l'utente non tocca mai le chiavi di cifratura, quindi l'attaccante non può estrarle dai client e l'accesso è revocabile per singolo utente.
### 4 way handshake: la vera crittografia dell'Open System Auth
Il quadro: in una rete WPA2-Personal la sequenza è _Open System auth_ (l'AP dice sì a tutti) → _association_ → **4-way handshake**, ed è quest'ultimo l'autenticazione crittografica vera. Vediamo come funziona davvero. A seguito un esempio di calcolo della PMK con WPA2-Personal ed anche un confronto con WPA3-Personal![[Pasted image 20260714173758.png]]

Il presupposto è che le due parti condividano già un segreto **prima** che il handshake cominci. La passphrase non viene usata direttamente: da essa si ricava la **PMK** (Pairwise Master Key), con `PMK = PBKDF2(passphrase, SSID, 4096 iterazioni, 256 bit)` — è l'«hashata 4096 volte con l'SSID» del capitolo. In WPA2-PSK sia il client sia l'AP conoscono la passphrase, quindi calcolano entrambi la stessa PMK per conto proprio. (In Enterprise la PMK arriva invece dallo scambio EAP/RADIUS, ma il handshake da qui in poi è identico.) Il punto chiave: **la PMK non viene mai trasmessa**. Il 4-way handshake non trasporta la chiave — serve a _dimostrare_ che entrambi la possiedono e a _derivare_ chiavi di sessione fresche.

Gli ingredienti sono due numeri casuali usa-e-getta (i **nonce**) e i due indirizzi MAC. L'AP genera l'**ANonce**, il client genera l'**SNonce**; combinando `PMK + ANonce + SNonce + MAC del client + MAC dell'AP` entrambi derivano la stessa **PTK** (Pairwise Transient Key), la chiave di sessione. Ecco perché due client con la _stessa_ passphrase ottengono comunque PTK diverse: i nonce sono diversi ogni volta. La prova di possesso passa da un **MIC** (Message Integrity Code) calcolato con una parte della PTK: se il MIC torna, vuol dire che l'altro lato ha derivato la stessa PTK, quindi ha la stessa PMK, quindi conosce la passphrase — senza averla mai spedita.![[Pasted image 20260714132706.png]]Un paio di dettagli che chiudono la logica. La PTK non è una chiave unica ma un mazzo: si spezza in **KCK** (calcola e verifica i MIC del handshake), **KEK** (cifra la GTK quando l'AP la consegna nel messaggio 3) e **TK** (la chiave vera con cui poi si cifra il traffico dati via CCMP/AES). La **GTK** (Group Temporal Key) è la chiave condivisa per broadcast/multicast, e viaggia cifrata proprio perché il canale non è ancora protetto. Il messaggio 3, avendo un MIC valido dall'AP, autentica _anche_ l'AP verso il client: è così che il handshake è **mutuo** e il client capisce di non stare parlando con un rogue AP che la passphrase non ce l'ha.

Il collegamento con l'attacco (già nel riquadro rosso) è il cuore per l'esame: catturato il handshake — spontaneamente, o forzato con un **deauth** che stacca un client e lo fa riconnettere — l'attaccante ha nonce, MAC e MIC. Da lì il crack è **offline**: prova passphrase su passphrase ricalcolando PMK→PTK→MIC finché il MIC combacia. Non decifra nulla: _verifica ipotesi_. Ed è per questo che le contromisure sono quelle: passphrase ad alta entropia (spazio di ricerca enorme), SSID unico (annulla le rainbow table di coWPAtty, legate all'SSID via PBKDF2) e le 4096 iterazioni che rendono costoso ogni singolo tentativo.

Nota a margine, l'aggancio al «fino al 2017» del capitolo: **KRACK** non attacca la passphrase, ma abusa della _ritrasmissione_ del messaggio 3 per forzare la reinstallazione di una PTK già in uso, azzerando i contatori di nonce e aprendo a replay/decifratura. È un difetto del protocollo, non della chiave — infatti si è risolto con una patch, non cambiando password.

Se vuoi, aggiungo alla nota del Cap. 8 un [!info] «4-way handshake» con questa meccanica (PMK→PTK, i MIC come prova, GTK, crack offline) sotto la sezione WPA-PSK — è il secondo dei candidati Excalidraw che avevo segnato, e ora hai il diagramma pronto da ricalcare.

## Difese deboli — e perché non reggono

> [!warning] Difese di facciata
> **MAC filtering**: ogni indirizzo va inserito a mano nella lista degli approvati (alto sforzo, bassa sicurezza); l'attaccante sniffa i MAC dei client legittimi e li spoofa — su Windows con SMAC, dal Device Manager della scheda, o con Bwmachak per le vecchie Orinoco.
> **SSID nascosto**: si omette l'SSID dai beacon, ma l'SSID viaggia comunque in probe e association request; basta un frame di deauth per forzare una riassociazione e leggerlo. Paradosso segnalato da Microsoft: nascondere l'SSID rende *il client* meno sicuro, perché continua a spammare probe request cercando la rete e si espone all'impersonation dell'AP.

La risposta è che **non** bisogna proteggerlo, ed è proprio quello il punto del passaggio.

Il malinteso di fondo è considerare l'SSID una specie di password. Non lo è: l'SSID è solo il **nome** della rete (`WiFi-Casa`, `FRITZ!Box-7530`…), un'etichetta per distinguerla dalle altre. Non è una credenziale. Conoscere il nome di una rete non ti fa entrare, esattamente come sapere il nome di un condominio non ti apre il portone: ti serve comunque la chiave vera (la passphrase WEP/WPA). Quindi il fatto che l'SSID «compaia in tutti quei frame» non è un buco da tappare — è semplicemente la constatazione che il nome gira in chiaro, come è normale che sia.

Da qui il senso del passaggio: siccome qualcuno _pensa_ di potersi difendere **nascondendo** l'SSID (lo «SSID nascosto» che il corso elenca fra i meccanismi di sicurezza di base), il punto è mostrare che è inutile. È la callout «Difese di facciata» della stessa nota. Nascondere l'SSID significa ometterlo dai beacon, ma il nome riappare comunque nelle probe e nelle association request: basta aspettare che un client legittimo si colleghi, o mandargli un deauth per forzare la riassociazione, e lo leggi. Peggio: un dispositivo configurato per una rete nascosta è costretto a **cercarla attivamente per nome ovunque vada**, spifferando il nome della rete e diventando bersaglio dell'impersonation dell'AP (evil twin). Sicurezza per oscurità che, in più, ritorce contro.

La sicurezza vera non sta nel nascondere il nome, ma nel **cifrare** (WPA2/3-AES) con una chiave forte. È lì che si difende una rete.

Una sfumatura che collega ai punti più avanti nella nota: l'SSID _entra_ nella derivazione della chiave WPA (PSK + SSID), ed è per questo che un **SSID unico** è una mitigazione — rende inutili le rainbow table precalcolate di coWPAtty, che sono legate a un SSID specifico. Ma è un discorso diverso dal tenerlo «segreto»: serve a rendere più dura la password, non a nascondere il nome.

Il motivo comune è uno solo: i management frame non sono cifrati, e gli indirizzi sorgente/destinazione degli 802.11 sono sempre in chiaro. Basta questo perché i tool mappino le associazioni tra client e AP senza rompere nulla.



> [!info] Four-way handshake
> Sia PSK sia Enterprise usano un handshake a quattro vie per derivare la **PTK** (Pairwise Transient Key, per l'unicast) e la **GTK** (Group Temporal Key, per multicast/broadcast). Meccanica della PTK: l'AP manda un numero casuale (**ANonce**) al client; il client risponde col suo (**SNonce**); l'AP calcola la PTK dai due nonce e invia un messaggio cifrato; il client lo decifra con la PTK. Perché conta per l'attacco: la derivazione è alimentata da PSK + SSID, quindi catturare l'handshake apre al **crack offline** della PSK. Non serve restare connessi — un deauth forza la riconnessione e quindi un nuovo handshake da catturare.

## Equipaggiamento e ricognizione

Il **driver** del chipset è il vero collo di bottiglia, più della radio in sé: è lui a decidere se puoi mettere la scheda in monitor mode e iniettare pacchetti, e la maggior parte dei driver delle schede consumer non espone affatto queste funzioni — così la NIC diventa inutile per l'hacking wireless anche quando l'hardware radio ne sarebbe capace. Per questo si citano schede con chipset **Atheros** (Ubiquiti SRC) o **Ralink** (Alfa AWUS050NH): hanno driver aperti e ben supportati che permettono monitor e injection, sono **USB** (così puoi passarle a una macchina virtuale), coprono entrambe le bande **2.4 e 5 GHz** e montano un connettore per l'**antenna esterna**. Il prerequisito che rende tutto possibile è la **monitor mode**, e vale la pena capire cosa cambia davvero. In funzionamento normale (managed) la scheda ti consegna solo i frame indirizzati a te e ti nasconde l'intestazione 802.11; in monitor mode, invece, riporta _ogni_ frame grezzo che sente su un canale — intestazioni comprese, e inclusi i management e control frame delle reti altrui. È esattamente la materia prima della scoperta e della cattura degli handshake: senza monitor mode vedi solo il traffico di livello superiore e resti cieco a tutto il resto. Sul fronte software, **Linux** e **Kali** sono molto avanti a Windows, dove la monitor mode di norma non è nemmeno supportata e servono hardware dedicati (AirPcap) o strumenti a pagamento (OmniPeek) per ottenere qualcosa di serio; Kali gira dentro una VM soltanto se la scheda è **USB** — che si può inoltrare alla macchina virtuale — mentre con schede integrate o PCIe tocca andare su bare metal, chiavetta avviabile o LiveCD. Le **antenne**, infine, spostano il problema della portata: quelle direzionali (Cantenna, Yagi, patch/panel, biquad dish) concentrano l'energia in una sola direzione e ti fanno raggiungere un AP da lontano — è la fisica dietro lo scenario del parcheggio — mentre un GPS abbinato al software di wardriving geolocalizza gli AP e li riversa in mappe e archivi collaborativi come WiGLE.

La **scoperta** ha due modalità speculari. Quella **attiva** trasmette broadcast probe request e registra chi risponde: è rapida, ma proprio perché _trasmette_ è rumorosa e rilevabile, e le sfugge ogni AP configurato per ignorare le probe di broadcast (è l'approccio di NetStumbler). Quella **passiva**, al contrario, non trasmette nulla: si limita ad ascoltare canale per canale e ad annotare ogni AP che vede col suo MAC, leggendo i beacon e i frame che passano. È più lenta — devi sostare su ogni canale e poi saltare al successivo — ma è silenziosa e più completa, perché prima o poi cattura anche le reti che non si annunciano; è ciò che fanno Kismet e airodump-ng, ed è la tecnica migliore. Da lì in poi è questione di **sniffing**: se il traffico non è cifrato è banalmente leggibile, gli attacchi MITM sono comuni e facili (ma possono violare le leggi sulle intercettazioni), Kismet salva tutto in file **PCAP** e Wireshark serve a sviscerare i frame uno per uno.

Un mattone che ritorna in quasi tutti gli attacchi è il **deauth DoS**. La disconnessione forzata è prevista dallo standard 802.11 come operazione legittima — un AP o un client possono annunciare «ci stiamo disconnettendo» per motivi validi, come chiave errata, sovraccarico o roaming. Il difetto è che nel 802.11 classico questi frame di deautenticazione **non sono autenticati**: nessuno verifica che vengano davvero dall'AP, quindi l'attaccante ne forgia uno mettendo il MAC dell'AP come mittente, e il client lo onora e cade. Con **aireplay-ng** si lancia una raffica — il pattern tipico è 64 deauth all'AP a nome del client e 64 al client a nome dell'AP. Oltre al DoS puro, cioè tenere una vittima costantemente disconnessa, il vero valore è come **leva** per altri attacchi: forzare una riconnessione costringe il client a rimandare le probe request (rivelando l'SSID di una rete nascosta) e a rifare il 4-way handshake, che tu catturi per il crack WPA offline. La contromisura moderna è il **Protected Management Frame** (802.11w), che autentica i management frame e rende inefficace il deauth spoofato — ed è obbligatorio proprio in WPA3.

## Guadagnare accesso — gli attacchi

**WEP è rotto per costruzione.** L'IV (Initialization Vector) è pseudocasuale per ogni frame e viaggia *in chiaro* nell'header; il keystream RC4 nasce da WEP key + IV. In trasmissione si fa XOR tra plaintext e keystream per ottenere il ciphertext; in ricezione si rigenera il keystream da WEP key + IV (letto dall'header) e si fa di nuovo XOR per tornare al plaintext.

![[Pasted image 20260714190426.png]] 

Il difetto: gli IV sono corti, quindi si ripetono; due frame con lo stesso IV, confrontando i ciphertext, lasciano indovinare il keystream e da lì la WEP key. I frame ARP, quasi identici tra loro, moltiplicano gli IV duplicati. Il brute-force dello spazio chiavi sarebbe settimane anche a 40 bit, ma raccogliere IV rende tutto rapidissimo. Due modalità: l'**attacco passivo** cattura abbastanza data frame, ne estrae gli IV e deduce la chiave (~60.000 IV per una chiave a 104 bit) — airodump-ng cattura in PCAP, aircrack-ng analizza statisticamente e si ferma su «KEY FOUND»; l'**ARP replay con fake authentication** è la via attiva (~5 min): si spoofa il MAC di un client valido con un fake authentication attack (open auth, senza inviare dati reali), poi si rigioca una ARP request così che l'AP ribroadcasti con un IV nuovo ogni volta, e gli IV si accumulano in fretta. 
La sequenza è airodump-ng (cattura) → aireplay-ng (fake auth) → aireplay-ng in un'altra finestra (ARP replay) → aircrack-ng (crack). Tool storici sul difetto IV: AirSnort, WEPAttack, DWEPCrack.

> [!danger] Mai usare WEP
> La contromisura è una sola ed esclusiva: non usare WEP, mai. Passare a WPA2/3 con AES.

**WPA-PSK cade con passphrase debole.** WPA non aveva vulnerabilità maggiori «fino al 2017» (il riferimento è a KRACK, che colpisce il 4-way handshake). Il punto debole resta la PSK: condivisa fra tutti gli utenti, lunga 8–63 caratteri, hashata 4096 volte insieme all'SSID — se è lunga e casuale servono trilioni di tentativi. L'attacco è **offline**: si cattura il 4-way handshake (aspettando, o forzandolo con un deauth) e poi si bruteforza in locale. Tool: aircrack-ng (dizionario + PCAP), coWPAtty (rainbow table specifiche per SSID, ~40 GB, generate sui top 1000 SSID di WiGLE), Pyrit (hashing scaricato su GPU). Mitigazione: PSK complessa e SSID unico (le rainbow table sono legate all'SSID) — ma basta un utente a divulgare la chiave.

**WPA-Enterprise: si attacca l'EAP.** Qui lo scenario cambia: non esiste una passphrase unica condivisa da tutti, ma ogni utente ha le proprie credenziali, verificate da un server **RADIUS** tramite 802.1X/EAP. Non c'è quindi una singola «chiave di rete» da catturare e bruteforzare offline come in WPA-PSK — il bersaglio si sposta sul **protocollo EAP** e su come tratta le credenziali. Il primo passo dell'attaccante è capire _quale_ EAP è in uso: cattura l'handshake, Wireshark ne mostra il tipo, e la cosa comoda è che l'identità esterna (lo **username**) viaggia in chiaro nella prima risposta EAP verso il RADIUS, così sa già chi sta attaccando.

Il caso peggiore è **[[LEAP]]**, protocollo proprietario Cisco del 2000, uno schema 802.1X su RADIUS nato per rimediare a WEP. Il suo peccato originale è appoggiarsi interamente a **[[MS-CHAPv2]]** come challenge-response, esponendone lo scambio sull'aria senza protezione — e MS-CHAPv2 è fragile per costruzione. Funziona a botta-e-risposta: il server manda una sfida, il client risponde calcolando qualcosa a partire dall'**hash NT** (hash pezzotto di [[LM-Lan Manager]]) della password. I difetti si sommano. L'hash NT **non è salato**, quindi la stessa password dà sempre lo stesso hash e le **rainbow table** precalcolate (DB da ~4 GB) funzionano; la risposta si ottiene spezzando l'hash NT in tre chiavi DES, e la terza è riempita di zeri lasciando appena **2 byte reali**, banali da forzare; e lo username è in chiaro. Il risultato è che basta catturare sfida e risposta per un attacco a dizionario/forza bruta offline, reso rapidissimo dalle rainbow table. Cisco sostiene che LEAP sia sicuro solo con password casuali da ≥10 caratteri — che quasi nessuno usa — quindi in pratica cade in giorni o minuti. Lo strumento è **asleap**, che estrae e cracca le password LEAP deboli ed è integrato con **Air-Jack** per buttare giù gli utenti già autenticati: alla riautenticazione forzata lo scambio viene risniffato e crackato. Verdetto: evitarlo come WEP. (È lo stesso mondo degli hash NT senza salt di [[LM-Lan Manager]]; e Microsoft stessa sconsiglia PPTP/MS-CHAP dopo la CloudCracker di Moxie Marlinspike — che riduce MS-CHAPv2 alla fatica di _una sola_ chiave DES-56, quindi ~200 $ e 24 h a prescindere da quanto è forte la password — raccomandando PEAP, L2TP/IPsec, IPSec+IKEv2 o SSTP.)
<svg width="100%" viewBox="0 0 860 1120" xmlns="http://www.w3.org/2000/svg" font-family="Inter, Segoe UI, system-ui, sans-serif">
<rect x="0" y="0" width="860" height="1120" rx="16" fill="#1f2023"/>
<text x="30" y="40" text-anchor="start" font-size="18" fill="#e8eaed" font-weight="700">MS-CHAPv2 — handshake e costruzione della NT Response</text>
<line x1="250" y1="70" x2="250" y2="560" stroke="#4b5563" stroke-width="1" stroke-dasharray="4 5"/>
<line x1="610" y1="70" x2="610" y2="560" stroke="#4b5563" stroke-width="1" stroke-dasharray="4 5"/>
<text x="430" y="87" text-anchor="middle" font-size="12.5" fill="#e8eaed" font-weight="400">1. Avvio / Identity (username)</text>
<line x1="258" y1="95" x2="602" y2="95" stroke="#9aa0a8" stroke-width="1.4"/>
<polygon points="602,95 596,91 596,99" fill="#9aa0a8"/>
<text x="430" y="120" text-anchor="middle" font-size="12.5" fill="#e8eaed" font-weight="400">2. Authenticator Challenge — 16 byte</text>
<line x1="602" y1="128" x2="258" y2="128" stroke="#9aa0a8" stroke-width="1.4"/>
<polygon points="258,128 264,124 264,132" fill="#9aa0a8"/>
<rect x="55.0" y="148" width="430" height="30" rx="6" fill="#3a3115" stroke="#a98b3a" stroke-width="1.4" opacity="1"/>
<text x="270" y="167.375" text-anchor="middle" font-size="12.5" fill="#f0e2b8" font-weight="400">3. Peer Challenge — 16 byte (generata dal client)</text>
<rect x="55.0" y="186" width="430" height="30" rx="6" fill="#3a3115" stroke="#a98b3a" stroke-width="1.4" opacity="1"/>
<text x="270" y="205.2" text-anchor="middle" font-size="12" fill="#f0e2b8" font-weight="400">4. Challenge Hash  C = SHA1(Peer + Auth + User) → 8 byte</text>
<rect x="55.0" y="224" width="430" height="30" rx="6" fill="#3a3115" stroke="#a98b3a" stroke-width="1.4" opacity="1"/>
<text x="270" y="243.375" text-anchor="middle" font-size="12.5" fill="#f0e2b8" font-weight="400">5. NT hash = MD4(password) → 16 byte</text>
<rect x="55.0" y="262" width="430" height="30" rx="6" fill="#3a3115" stroke="#a98b3a" stroke-width="1.4" opacity="1"/>
<text x="270" y="281.025" text-anchor="middle" font-size="11.5" fill="#f0e2b8" font-weight="400">6. NT Response = DES(C,K1)+DES(C,K2)+DES(C,K3) → 24 byte</text>
<text x="430" y="312" text-anchor="middle" font-size="12.5" fill="#e8eaed" font-weight="400">7. Peer Challenge + NT Response + Username</text>
<line x1="258" y1="320" x2="602" y2="320" stroke="#9aa0a8" stroke-width="1.4"/>
<polygon points="602,320 596,316 596,324" fill="#9aa0a8"/>
<rect x="420.0" y="344" width="380" height="30" rx="6" fill="#3a3115" stroke="#a98b3a" stroke-width="1.4" opacity="1"/>
<text x="610" y="363.375" text-anchor="middle" font-size="12.5" fill="#f0e2b8" font-weight="400">8. Ricalcola col proprio hash NT e verifica</text>
<text x="430" y="397" text-anchor="middle" font-size="12.5" fill="#e8eaed" font-weight="400">9. Success + Authenticator Response</text>
<line x1="602" y1="405" x2="258" y2="405" stroke="#9aa0a8" stroke-width="1.4"/>
<polygon points="258,405 264,401 264,409" fill="#9aa0a8"/>
<rect x="25.0" y="428" width="460" height="38" rx="6" fill="#3a3115" stroke="#a98b3a" stroke-width="1.4" opacity="1"/>
<text x="255" y="444.0" text-anchor="middle" font-size="12.5" fill="#f0e2b8" font-weight="400">10. Il client verifica l'Authenticator Response</text>
<text x="255" y="460.0" text-anchor="middle" font-size="11" fill="#f0e2b8" font-weight="400">→ server autenticato (autenticazione MUTUA)</text>
<rect x="185.0" y="505" width="130" height="46" rx="6" fill="#232a4d" stroke="#3b4a7a" stroke-width="1.4" opacity="1"/>
<text x="250" y="533.25" text-anchor="middle" font-size="15" fill="#c7d2fe" font-weight="400">Client</text>
<rect x="545.0" y="505" width="130" height="46" rx="6" fill="#232a4d" stroke="#3b4a7a" stroke-width="1.4" opacity="1"/>
<text x="610" y="532.725" text-anchor="middle" font-size="13.5" fill="#c7d2fe" font-weight="400">Server (RADIUS)</text>
<line x1="200" y1="600" x2="660" y2="600" stroke="#4b5563" stroke-width="3"/>
<text x="30" y="646" text-anchor="start" font-size="15" fill="#9ca3af" font-weight="400">Dove il Response è il seguente:</text>
<rect x="180.0" y="672" width="180" height="46" rx="6" fill="#12564c" stroke="#2ea88f" stroke-width="1.4" opacity="1"/>
<text x="270" y="692.0" text-anchor="middle" font-size="13" fill="#c9f2e6" font-weight="400">Hash NT — 16 byte</text>
<text x="270" y="708.0" text-anchor="middle" font-size="11" fill="#c9f2e6" font-weight="400">fa da chiave</text>
<rect x="525.0" y="672" width="190" height="46" rx="6" fill="#5a4517" stroke="#c69a3a" stroke-width="1.4" opacity="1"/>
<text x="620" y="692.0" text-anchor="middle" font-size="12.5" fill="#f2e2b0" font-weight="400">Challenge Hash C — 8 byte</text>
<text x="620" y="708.0" text-anchor="middle" font-size="11" fill="#f2e2b0" font-weight="400">fa da testo in chiaro</text>
<rect x="200.0" y="738" width="140" height="36" rx="6" fill="#12564c" stroke="#2ea88f" stroke-width="1.4" opacity="1"/>
<text x="270" y="760.55" text-anchor="middle" font-size="13" fill="#c9f2e6" font-weight="400">Pad → 21 byte</text>
<rect x="145.0" y="800" width="130" height="44" rx="6" fill="#12564c" stroke="#2ea88f" stroke-width="1.4" opacity="1"/>
<text x="210" y="826.55" text-anchor="middle" font-size="13" fill="#c9f2e6" font-weight="400">K1 — 7 byte</text>
<rect x="335.0" y="800" width="130" height="44" rx="6" fill="#12564c" stroke="#2ea88f" stroke-width="1.4" opacity="1"/>
<text x="400" y="826.55" text-anchor="middle" font-size="13" fill="#c9f2e6" font-weight="400">K2 — 7 byte</text>
<rect x="525.0" y="800" width="130" height="44" rx="6" fill="#12564c" stroke="#2ea88f" stroke-width="1.4" opacity="1"/>
<text x="590" y="819.0" text-anchor="middle" font-size="13" fill="#c9f2e6" font-weight="400">K3 — 7 byte</text>
<text x="590" y="835.0" text-anchor="middle" font-size="11" fill="#c9f2e6" font-weight="400">2 byte reali + 5 zeri</text>
<rect x="145.0" y="876" width="130" height="44" rx="6" fill="#33383f" stroke="#6b7280" stroke-width="1.4" opacity="1"/>
<text x="210" y="895.0" text-anchor="middle" font-size="13" fill="#e5e7eb" font-weight="400">DES</text>
<text x="210" y="911.0" text-anchor="middle" font-size="11" fill="#e5e7eb" font-weight="400">cifra C con K1</text>
<rect x="335.0" y="876" width="130" height="44" rx="6" fill="#33383f" stroke="#6b7280" stroke-width="1.4" opacity="1"/>
<text x="400" y="895.0" text-anchor="middle" font-size="13" fill="#e5e7eb" font-weight="400">DES</text>
<text x="400" y="911.0" text-anchor="middle" font-size="11" fill="#e5e7eb" font-weight="400">cifra C con K2</text>
<rect x="525.0" y="876" width="130" height="44" rx="6" fill="#33383f" stroke="#6b7280" stroke-width="1.4" opacity="1"/>
<text x="590" y="895.0" text-anchor="middle" font-size="13" fill="#e5e7eb" font-weight="400">DES</text>
<text x="590" y="911.0" text-anchor="middle" font-size="11" fill="#e5e7eb" font-weight="400">cifra C con K3</text>
<rect x="190.0" y="952" width="420" height="46" rx="6" fill="#3f356e" stroke="#7c6bc4" stroke-width="1.4" opacity="1"/>
<text x="400" y="972.0" text-anchor="middle" font-size="13.5" fill="#e6ddff" font-weight="400">Response — 24 byte</text>
<text x="400" y="988.0" text-anchor="middle" font-size="11" fill="#e6ddff" font-weight="400">i tre output DES concatenati (3 × 8)</text>
<line x1="270" y1="718" x2="270" y2="738" stroke="#2ea88f" stroke-width="1.3"/>
<polygon points="270,738 266,732 274,732" fill="#2ea88f"/>
<line x1="270" y1="774" x2="210" y2="800" stroke="#2ea88f" stroke-width="1.3"/>
<polygon points="210,800 206,794 214,794" fill="#2ea88f"/>
<line x1="270" y1="774" x2="400" y2="800" stroke="#2ea88f" stroke-width="1.3"/>
<polygon points="400,800 396,794 404,794" fill="#2ea88f"/>
<line x1="270" y1="774" x2="590" y2="800" stroke="#2ea88f" stroke-width="1.3"/>
<polygon points="590,800 586,794 594,794" fill="#2ea88f"/>
<line x1="210" y1="844" x2="210" y2="876" stroke="#2ea88f" stroke-width="1.3"/>
<polygon points="210,876 206,870 214,870" fill="#2ea88f"/>
<line x1="400" y1="844" x2="400" y2="876" stroke="#2ea88f" stroke-width="1.3"/>
<polygon points="400,876 396,870 404,870" fill="#2ea88f"/>
<line x1="590" y1="844" x2="590" y2="876" stroke="#2ea88f" stroke-width="1.3"/>
<polygon points="590,876 586,870 594,870" fill="#2ea88f"/>
<line x1="620" y1="718" x2="620" y2="858" stroke="#c69a3a" stroke-width="1.3"/>
<line x1="210" y1="858" x2="620" y2="858" stroke="#c69a3a" stroke-width="1.3"/>
<line x1="210" y1="858" x2="210" y2="876" stroke="#c69a3a" stroke-width="1.3"/>
<polygon points="210,876 206,870 214,870" fill="#c69a3a"/>
<line x1="400" y1="858" x2="400" y2="876" stroke="#c69a3a" stroke-width="1.3"/>
<polygon points="400,876 396,870 404,870" fill="#c69a3a"/>
<line x1="590" y1="858" x2="590" y2="876" stroke="#c69a3a" stroke-width="1.3"/>
<polygon points="590,876 586,870 594,870" fill="#c69a3a"/>
<line x1="210" y1="920" x2="400" y2="952" stroke="#6b7280" stroke-width="1.3"/>
<line x1="400" y1="920" x2="400" y2="952" stroke="#6b7280" stroke-width="1.3"/>
<line x1="590" y1="920" x2="400" y2="952" stroke="#6b7280" stroke-width="1.3"/>
<polygon points="400,952 396,946 404,946" fill="#6b7280"/>
<rect x="185" y="1016" width="490" height="44" rx="8" fill="none" stroke="#7c6bc4" stroke-width="1.2" opacity="1"/>
<text x="430" y="1034" text-anchor="middle" font-size="12" fill="#cdbff5" font-weight="400">K3 ha solo 16 bit e i tre DES cifrano lo stesso C noto:</text>
<text x="430" y="1051" text-anchor="middle" font-size="12" fill="#cdbff5" font-weight="400">la sicurezza crolla a una singola chiave DES-56 → crack garantito.</text>
<rect x="250" y="1082" width="14" height="14" rx="3" fill="#12564c" stroke="#2ea88f" stroke-width="1.2" opacity="1"/>
<text x="272" y="1093" text-anchor="start" font-size="12" fill="#9ca3af" font-weight="400">chiave (dall'hash)</text>
<rect x="430" y="1082" width="14" height="14" rx="3" fill="#5a4517" stroke="#c69a3a" stroke-width="1.2" opacity="1"/>
<text x="452" y="1093" text-anchor="start" font-size="12" fill="#9ca3af" font-weight="400">testo in chiaro (la challenge)</text>
</svg>

Stanno meglio **EAP-TTLS e PEAP**, e conviene capire _perché_. Invece di esporre un challenge-response debole all'aria aperta, prima costruiscono un **tunnel TLS** — con il server RADIUS autenticato da un **certificato** — e solo dentro quel tunnel fanno girare l'autenticazione interna, che resta spesso debole (MS-CHAPv2, EAP-GTC a password monouso, o addirittura in chiaro). Chi ascolta vede solo byte cifrati da TLS: niente attacco a dizionario offline sull'auth interna, ed è questo il salto di qualità. La cifratura TLS, di per sé, non si rompe. Il punto debole si sposta sulla **fiducia**: TLS protegge davvero solo se il client verifica il certificato del server RADIUS. Se il client è mal configurato e **non valida il certificato** (o accetta qualunque certificato), si apre la via dell'**AP impersonation / MITM**. L'attaccante monta un finto AP e un finto RADIUS — **hostapd** per fare da access point, **FreeRADIUS-WPE** che accetta qualunque connessione e logga tutto — e il supplicant della vittima costruisce il tunnel TLS verso il RADIUS _dell'attaccante_ (perché non ha controllato il certificato). A quel punto l'attaccante è il terminatore del tunnel: legge l'autenticazione interna in chiaro e la bruteforza offline con asleap. Tutta la sicurezza di PEAP/TTLS poggia quindi su una casella — **«Validate server certificate»** attivata su _tutti_ i client, meglio ancora indicando la CA attesa e il nome del server e non «un certificato qualsiasi». Con quella spunta il certificato del RADIUS-canaglia non passa la verifica, il supplicant rifiuta, e l'attacco muore sul nascere.

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
