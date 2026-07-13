---
tags: [ethl, hacking-exposed-7, remote-access, voip, vpn, dial-up, pbx, cap7]
capitolo: 7
data: 2026-07-13
collegamenti: ["[[ETHL - Cap 6 Cybercrime e APT]]", "[[ETHL - LAN Manager (LM) vs NTLM]]"]
---

# ETHL — Cap 7: Remote Connectivity e VoIP Hacking

> [!abstract] Il filo del capitolo
> Il perimetro non è solo il firewall. Questo capitolo raccoglie tutte le **porte laterali** di una rete — i canali di accesso remoto che aggirano o precedono il fronte internet-facing: le linee telefoniche (dial-up, PBX, voicemail), i tunnel cifrati (VPN) e la rete voce convergente su IP (VoIP). Due lezioni ricorrono a ogni sezione. La prima: la metodologia è sempre la stessa — *footprint → scan → enumerate → exploit* — applicata a un blocco di numeri di telefono esattamente come a un range di IP. La seconda: l'anello debole è quasi sempre l'**autenticazione** — password numeriche corte, single-factor, credenziali di default del vendor, o protocolli che lasciano trapelare il materiale d'autenticazione.

Il capitolo è, di fatto, un catalogo di vie d'ingresso "non convenzionali". Fin qui abbiamo attaccato host e servizi esposti sulla rete IP; qui si guarda a tutto ciò che *non* passa dalla porta principale. È anche il punto in cui il libro chiude un cerchio col capitolo precedente: il Cap. 6 finiva su Stuxnet e i sistemi SCADA, e il dial-up — apparentemente obsoleto — sopravvive esattamente lì, negli **Industrial Control System** e nei device di rete legacy, dove nessuno lo cerca più e dove quindi è più pericoloso.

---

## 1. Dial-up hacking

Il **dial-up** è un modo di connettersi a una rete remota usando la **linea telefonica analogica**: un modem converte i dati in segnali audio, compone un numero e stabilisce la connessione con un modem all'altro capo. È l'accesso remoto pre-Internet a banda larga — lento (fino a 56 kbps), e occupa la linea telefonica mentre è attivo.

Nel contesto del Cap. 7 conta perché, anche se soppiantato dalla VPN, **sopravvive** dove nessuno lo cerca più: vecchi server, apparati di rete e soprattutto sistemi di controllo industriale (ICS). Ed è proprio l'essere «dimenticato» a renderlo un vettore d'attacco reale.

Il dial-up è il capostipite dell'accesso remoto. Molte aziende lo tengono ancora acceso per raggiungere vecchi server, apparati di rete o ICS, e proprio perché "dimenticato" resta un vettore reale.

### Footprinting: trovare i numeri

Prima di attaccare bisogna procurarsi i numeri da comporre. Il footprinting telefonico consiste nell'**identificare blocchi di numeri** da dare in pasto a un wardialer, raccolti da elenchi telefonici, siti web del target, database di registrazione dei nomi Internet, o composizione manuale.

> [!info] Contromisure footprinting
> Richiedere una password per le richieste sugli account, sanitizzare le informazioni sensibili pubblicate e formare i dipendenti a non divulgarle. È lo stesso principio di igiene informativa che apre ogni capitolo: meno superficie pubblica, meno footprint.

### Wardialing

Il **wardialing** automatizza la scansione di interi blocchi di numeri per scoprire quali rispondono con un modem — è il compito del **wardialer**, distinto dal **demon dialer** che invece martella ripetutamente un singolo numero. Conta sia l'hardware sia il software.

Sul lato **hardware** l'efficienza dipende dal numero e dalla qualità dei modem. Ci sono poi due voci spesso trascurate: i **problemi legali** (le leggi che regolano identificazione delle linee, registrazione delle chiamate e spoofing del numero variano da giurisdizione a giurisdizione) e i **costi accessori** (chiamate a lunga distanza, internazionali o a tariffa nominale che si moltiplicano su migliaia di numeri).

Sul lato **software** contano scheduling automatico, facilità di setup e accuratezza. Strumenti di riferimento: **WarVOX, TeleSweep, PhoneSweep**.

### Brute-force scripting: i cinque domini

Dai risultati del wardialing si categorizzano le connessioni in **domini di penetrazione** — una classificazione che richiede esperienza con una grande varietà di server dial-up e sistemi operativi — in base a come il server gestisce l'autenticazione e i tentativi falliti. È la mappa che decide se e come vale la pena montare un attacco brute-force scriptato (con **ZOC, Procomm Plus** e il linguaggio di scripting **ASPECT**).

| Dominio | Caratteristica |
|---|---|
| **Low Hanging Fruit** | Password indovinabili o comunemente usate |
| **Single Auth, Unlimited Attempts** | UN solo fattore (password *o* ID); **non** disconnette dopo N fallimenti |
| **Single Auth, Limited Attempts** | UN solo fattore; disconnette dopo N fallimenti |
| **Dual Auth, Unlimited Attempts** | DUE fattori (password *e* ID); **non** disconnette dopo N fallimenti |
| **Dual Auth, Limited Attempts** | DUE fattori; disconnette dopo N fallimenti |

> [!tip] Come leggere la tabella
> Le due variabili sono *quanti fattori* e *se c'è lockout*. Il brute-force scala bene solo dove i tentativi sono illimitati; il lockout dopo N fallimenti è la contromisura che degrada un intero dominio da "attaccabile" a "impraticabile". È lo stesso ragionamento del lockout sugli account visto altrove.

### Contromisure: un ciclo, non una lista

Le misure di sicurezza dial-up sono dodici, ma il punto non è impararle a memoria: sono un **processo continuo** che si chiude tornando al passo 1. In sintesi tematica: inventariare le linee esistenti e **consolidarle** in un modem bank centrale posizionato come connessione *non fidata* fuori dalla rete interna; rendere le linee analogiche difficili da trovare e mettere in sicurezza fisica gli armadi delle telecomunicazioni; monitorare i log del software dial-up; **non rivelare informazioni identificative** sulle linee che servono clienti/business (niente banner che dica chi sei o che sistema è); imporre **autenticazione multi-fattore** e **dial-back** (il sistema richiama un numero noto); sensibilizzare l'help desk sul rischio di rilasciare o resettare credenziali; centralizzare il provisioning e stabilire policy ferme. Poi si ricomincia dall'inventario.

### Come si comporta l'attaccante

Ha senso che ti sembri alieno: sei abituato al mondo IP, e il dial-up gira su una logica **completamente diversa nel primo passo**. Ma la parte confusa è solo l'ingresso — una volta dentro, torna tutto familiare. Ti rimappo i concetti su quelli che già conosci.

Nel mondo IP hai un **indirizzo IP**, fai un **port scan**, trovi un **servizio aperto**, ti connetti **attraverso Internet** e ti autentichi. Nel dial-up cambia solo il livello di trasporto e indirizzamento:

- **numero di telefono** al posto dell'indirizzo IP
- **wardialing** al posto del port scan: componi in sequenza un blocco di numeri e ascolti _cosa risponde_. Persona → salti. Fax → annoti. **Tono di modem (carrier)** → jackpot, dall'altra parte c'è un computer. È discovery pura, come nmap che trova le porte aperte.
- il **modem che risponde con un prompt** è l'equivalente del servizio aperto: ti connetti e ti trovi davanti un login Windows RAS, una console Cisco, un getty Unix, un'interfaccia di manutenzione ICS o l'admin di un PBX. Il **banner** ti dice cos'è — è enumeration.
- poi **bruteforce scripting** delle credenziali (i cinque domini dicono se è praticabile), esattamente come forzeresti un login qualsiasi.

Fin qui è la solita catena _footprint → scan → enumerate → exploit_ che già padroneggi. **L'unica cosa che cambia è il tubo**: invece di pacchetti IP instradati su Internet, il tuo modem fa una **telefonata diretta** sulla rete telefonica (PSTN) fino al modem del bersaglio, e i due negoziano un collegamento punto-punto (quel rumore stridulo dell'handshake).

Ed è qui il punto che rende il dial-up _pericoloso_, non la tecnica in sé:![[Pasted image 20260713113145.png]]Questa è l'intera ragione d'essere del dial-up come vettore. Le difese perimetrali — firewall, IDS, VPN — stanno tutte **sul bordo IP**, perché è da lì che ci si aspetta il traffico. Un modem appeso a una porta seriale in uno sgabuzzino non passa da nessuna di quelle difese: è una **porta laterale che entra dritta nella rete interna**, e nessuno la sorveglia perché "tanto chi usa più il dial-up".

Quindi il modo tipico in cui un attaccante lo sfrutta, in una frase: **wardialing dei numeri del target per trovare un modem vivo e dimenticato, autenticazione (spesso banale, credenziali di default o deboli) contro quello che risponde, e da lì ci si ritrova con un piede _dentro_ la rete — bypassando completamente il firewall — da cui poi si fa il solito lateral movement IP che già conosci.**

Ecco perché le contromisure del capitolo sembrano ovvie ma sono esattamente mirate a questo: _inventaria le linee_ (non puoi difendere un modem che non sai di avere), _consolida i modem_ in un unico punto trattato come non fidato, _dial-back_ (il sistema richiama un numero noto, così non basta chiamare), _MFA_. Tutte cose che servono a chiudere quella porta laterale o almeno a metterci una guardia.

E il collegamento che ti fa scattare il "perché è ancora nel libro": negli **ICS/SCADA** questi modem legacy ci sono davvero ancora, ed è lo stesso mondo di infrastruttura critica-su-roba-vecchia che chiudeva il Cap. 6 con Stuxnet. Il canale obsoleto è pericoloso _proprio perché_ obsoleto — è l'unico pezzo di rete che nessuno ha aggiornato né sta guardando.


---

## 2. PBX hacking

Le connessioni dial-up verso i **PBX** (i centralini aziendali) esistono ancora, tipicamente usate dai vendor per la manutenzione. Attaccarli segue la stessa rotta del dial-up classico, e il tallone d'Achille sono le **credenziali di default** lasciate dai produttori.

| Sistema PBX | Nota d'attacco |
|---|---|
| **Octel Voice Network** | Login è un numero; default `9999` |
| **Williams / Northern Telecom** | Richiede numero utente + codice numerico a 4 cifre |
| **Meridian Links** | User ID/password di default (es. `maint/maint`) |
| **Rolm PhoneMail** | User ID/password di default (es. `sysadmin/sysadmin`) |
| **PBX protetto da RSA SecurID** | Dai un'occhiata e vai via: non si sconfigge |

> [!warning] La lezione dei default
> Quattro sistemi su cinque cadono per credenziali predefinite; il quinto, protetto da token RSA SecurID, semplicemente non si buca. È la dimostrazione compatta del capitolo: l'autenticazione forte, basata su token, è ciò che separa un bersaglio da un non-bersaglio.

> [!info] Contromisure PBX
> Ridurre le finestre temporali in cui i modem sono accesi e distribuire più forme di autenticazione.

---

## 3. Voicemail hacking

Un sistema di Voicemail o segreteria telefonica è un sistema centralizzato utilizzato nelle aziende per l’invio, l’archiviazione e il recupero di messaggi audio, proprio come farebbe una segreteria telefonica a casa. Questi sistemi rendono un sistema telefonico più flessibile e potente consentendo il passaggio di informazioni e messaggi tra gli utenti anche quando uno di essi non è presente.

Ogni interno di un [sistema telefonico](https://www.3cx.it/centralino/telefonico/) è normalmente collegato ad una Voicemail, quindi quando viene chiamato il numero e la linea non riceve risposta o è occupata, il chiamante ascolta un messaggio precedentemente registrato dall’utente. Questo messaggio può dare istruzioni al chiamante di lasciare un messaggio vocale o fornire altre opzioni disponibili. Le opzioni includono il paging dell’utente o il trasferimento a un altro interno o un receptionist. I sistemi di Voicemail forniscono inoltre notifiche agli utenti per informarli di nuovi messaggi vocali. I sistemi più moderni offrono agli utenti diversi modi per controllare la propria Voicemail, incluso l’accesso tramite PC, smartphone, telefoni fissi o persino tramite [App mobili](https://www.3cx.it/centralino/app-telelavoro/).![[Pasted image 20260713113006.png]]

Il brute-force della voicemail funziona come il dial-up. Servono tre ingredienti: il **numero** per accedere al sistema di voicemail, la **casella target** (3–5 cifre) e una **stima educata della password**, che di norma è composta solo da numeri — ed è proprio questo spazio ristretto a renderla fragile. Strumenti storici per sistemi vecchi e poco sicuri: **Voicemail Box Hacker 3.0** e **VrACK 0.51**, oltre allo scripting **ASPECT**.

#### Ma che ci fai?

Buona domanda, perché il "che ci fai con una segreteria telefonica" è proprio il punto che non è ovvio. Lo scopo non è la voicemail in sé — è ciò a cui dà accesso. Ci sono tre payoff, in ordine crescente di gravità.

Il primo è **intelligence**. Una casella vocale è una miniera di ricognizione: messaggi che nominano persone, numeri interni, progetti, "richiamami a questo numero riguardo alla fusione", chi è in ferie e chi copre. È lo stesso valore del footprinting, ma servito su un piatto — informazione sensibile che l'azienda non pensa di star esponendo. Lo scandalo _News of the World_ nel Regno Unito era esattamente questo: giornalisti che indovinavano il PIN di default per ascoltare i messaggi di celebrità e vittime.

Il secondo è l'eredità **phreaking / toll fraud**. I sistemi di voicemail vecchi, spesso integrati col PBX, una volta che sei autenticato ti lasciano fare outbound calling, call forwarding o "out-dial" dall'interno del sistema. L'attaccante usa la casella come trampolino per **telefonate internazionali o a numeri premium a spese della vittima**. È il motivo per cui voicemail e PBX stanno nello stesso capitolo: stesso mondo, stesso bottino.

Il terzo — e per te che vieni dalla sicurezza IP è quello che fa scattare il _click_ — è che la voicemail è un **buco nell'autenticazione telefonica**. Moltissimi servizi mandano codici di reset password o OTP con una **telefonata**, e se non rispondi il codice finisce... in segreteria. Chi controlla la tua voicemail (PIN debole) fa partire il "chiamami col codice", lascia squillare a vuoto, poi recupera l'OTP dal messaggio. Così **scavalca la 2FA basata sul telefono** e ti prende l'account vero. È il ponte tra il capitolo telefonico e il mondo che conosci: la vecchia casella vocale diventa la chiave per un account moderno.

E il motivo per cui vale la pena provarci è la stessa fragilità che il libro sottolinea: PIN **solo numerici**, corti, spesso lasciati di default. Keyspace minuscolo, brute-force banale — esattamente la stessa meccanica del dial-up, con questi tre payoff a giustificare lo sforzo.

> [!info] Contromisure voicemail
> Lockout dopo un numero di tentativi falliti e logging/osservazione delle connessioni alla voicemail.

---

## 4. VPN hacking

La VPN ha rimpiazzato il dial-up come meccanismo di accesso remoto, ma sposta il problema, non lo elimina: ora il bersaglio è il gateway, i suoi profili di configurazione e il modo in cui negozia le chiavi.

### Google hacking dei profili (PCF)

Il client VPN Cisco salva le impostazioni in file di profilo **`.pcf`**. Cercando `filetype:pcf` su Google si trovano PCF esposti pubblicamente: si scaricano, si importano nel client, ci si connette alla rete target e si lanciano attacchi ulteriori. Le password memorizzate nel PCF alimentano poi **attacchi di password reuse** (con **Cain**).

> [!info] Contromisure PCF
> User awareness, sanitizzazione delle informazioni sensibili sui siti e uso di **Google Alerts** per accorgersi quando materiale del genere finisce indicizzato. Collega al tema del riuso delle credenziali di [[ETHL - LAN Manager (LM) vs NTLM]].

### Probing dei server [[IPsec]]

**Basics of IPSec VPNs** 
Internet Protocol Security, or IPSec, is a collection of protocols that provide Layer 3 security through authentication and encryption. All VPNs (site-to-site, client-to-site) establish a private tunnel between two networks over a third, often less secure network. 

- **Site-to-site VPN**. With a site-to-site VPN, both endpoints are normally dedicated devices called VPN gateways that are responsible for a number of different tasks such as tunnel establishment, encryption and routing. Systems wishing to communicate to a remote site are forwarded to these VPN gateways on their local network, which, in turn, seamlessly direct the traffic over the secure tunnel to the remote site with no client interaction. 
- **Client-to-site VPN**. Client-to-site VPNs require users to have a software-based VPN client on their system that handles session tasks such as tunnel establishment, encryption and routing. Depending on the configuration, either all traffic from the client system will be forwarded over the VPN tunnel (split tunneling disabled) or only defined traffic will be forwarded while all other traffic takes the client’s default path (split tunneling enabled). One important note to make is that with split tunneling enabled and the VPN connected, the client’s system effectively bridges the corporate internal network and the Internet.  

This is why it is crucial to keep split tunneling disabled at all times unless it is absolutely required.

Prima si verifica che la porta del servizio sia raggiungibile (**UDP 500**), poi si fa identificazione della VPN IPsec e fingerprinting del gateway, individuando la **modalità di IKE Phase 1** e l'hardware del server remoto. Strumenti: **Nmap, NTA Monitor, IKEProber**.

> [!warning] Contromisura assente
> Contro il semplice probing non si può fare molto: il servizio, per funzionare, deve rispondere. La difesa si sposta a valle, sulla configurazione (vedi Aggressive Mode).

### Attacco all'[[15 CS Lower Level - TLS and IPSec#10. Internet Key Exchange (IKE)|IKE]] Aggressive Mode
IPSec uses the Internet Key Exchange(IKE) protocol for authentication as well as key and tunnel establishment. IKE is split into two phases,each of which has its own distinct purpose: 
1. Phase 1. Main Goal: authenticate the two communicating parties with each other and then set up a secure channel for IKE Phase 2. This can be done in two mode: 
	1. **Main Mode**. It uses three separate two-way handshake (total of six messages). This process first **establishes a secure channel** in which authentication information is exchanged securely between the two parties. 
	2. **Aggressive Mode**. In only three messages, Aggressive mode accomplishes the same overall goal of Main mode but in a faster, notably less secure fashion. **Aggressive mode does not provide a secure channel to protect authentication information**, which ultimately exposes it to eavesdropping attacks. 
2. Phase 2. IKE Phase 2’s final aim is to establish the IPSec tunnel, which it does with the help of IKE Phase 1.


Partiamo dal caso sicuro. In **Main Mode** i sei messaggi prima costruiscono il canale (negoziazione + scambio Diffie-Hellman), e solo _dopo_ — dentro il cifrato — viaggiano identità e hash di autenticazione:![[Pasted image 20260713130308.png]]Adesso l'**Aggressive Mode**: gli stessi obiettivi in tre soli messaggi, ma il prezzo è che l'hash di autenticazione (`HASH_R`) viaggia nel messaggio 2 _prima_ che esista un canale cifrato — quindi in chiaro. Qui vedi esattamente cosa mette in tasca l'attaccante che sta sniffando la linea:![[Pasted image 20260713130335.png]]Il pezzo che chiude il cerchio, e che è il vero motivo per cui la cattura è pericolosa, è **cosa se ne fa** l'attaccante di quella roba. `HASH_R` non è la password: è un hash calcolato a partire dalla **chiave pre-condivisa del gruppo (PSK)**, insieme ai valori Diffie-Hellman e ai nonce che sono passati anch'essi in chiaro nei primi due messaggi.

Quindi l'attaccante ha in mano _tutti gli ingredienti tranne la PSK_, più il risultato finale (`HASH_R`). Da lì monta un **attacco a dizionario/brute-force offline**: prova una PSK candidata, ricalcola l'hash che _dovrebbe_ uscire con quei DH e nonce, e lo confronta col `HASH_R` catturato. Quando i due coincidono, ha trovato la chiave pre-condivisa. Offline significa senza più toccare il server — nessun lockout, nessun rilevamento, tutta la potenza di calcolo che vuole.

Ed è esattamente ciò che il Main Mode impedisce: lì `HASH_R` e l'identità viaggiano nei messaggi 5-6, _dentro_ il canale già cifrato dallo scambio DH. L'attaccante che sniffa vede solo ciphertext — non ha il valore dell'hash da confrontare, quindi il crack offline della PSK non parte nemmeno. Stesso identico obiettivo di autenticazione, ma l'ordine "prima il canale, poi l'auth" è ciò che salva Main Mode e affonda Aggressive.

#### quando viene creata la chiave PSK?

Buona domanda, perché tocca un punto che il capitolo dà per scontato e che è proprio la radice della vulnerabilità. La risposta secca: la PSK **non viene creata durante l'handshake IKE** — esiste _già prima_, configurata a mano su entrambi i lati fuori banda.

Distinguiamo due chiavi diverse, perché è facile confonderle:

La **chiave Diffie-Hellman** (il segreto di sessione da cui nasce il canale cifrato) sì, quella viene generata _durante_ l'handshake, nei messaggi con `KE` e i nonce, ed è nuova a ogni connessione. È effimera.

La **PSK** (pre-shared key) invece è **pre-condivisa**, e "pre" vuol dire letteralmente _prima_: l'amministratore la sceglie e la inserisce manualmente nella configurazione del gateway VPN e in quella del client, prima ancora che avvenga qualsiasi connessione. Tipicamente al momento del setup della VPN. Non transita mai sul filo durante IKE — né in Main né in Aggressive Mode. Quello che passa nell'handshake è l'`HASH_R`, cioè un _derivato_ della PSK (un hash che la usa come ingrediente), mai la PSK stessa.

Ed è qui il nesso con l'attacco che hai appena visto: proprio perché la PSK è statica, decisa da un umano e riusata a ogni connessione, si presta a due debolezze. Primo, è spesso **debole o indovinabile** (scelta da una persona, non generata casualmente) — ed è ciò che rende praticabile il brute-force offline dell'`HASH_R`. Secondo, in molte configurazioni **è la stessa per tutto il gruppo** di utenti (group VPN): un solo segreto condiviso da tutti. Craccarne uno vale per tutti, e chiunque nel gruppo la conosce.

Quindi, per incastrare il tutto: la PSK nasce **a mano, in fase di configurazione, molto prima dell'handshake**; l'handshake non la crea e non la trasmette, ne trasmette solo un hash; e il fatto che sia statica e umana è esattamente ciò che permette all'attaccante di ritrovarla partendo da quell'hash. Se fosse una chiave casuale lunga generata da una macchina, la cattura dell'`HASH_R` in Aggressive Mode sarebbe molto meno utile — il brute-force offline non concluderebbe nulla in tempi ragionevoli.

---

È il cuore della sezione VPN. L'**IKE Phase 1 in modalità Aggressive** non fornisce un canale sicuro: l'handshake espone le informazioni d'autenticazione a **eavesdropping**. L'attacco ha due tempi: prima si verifica se il server supporta l'aggressive mode (**IKEProbe**), poi si avvia la connessione e si catturano i messaggi d'autenticazione da craccare offline (**IKECrack, Cain**).


> [!tip] Contromisure Aggressive Mode
> Dismettere l'uso dell'IKE Aggressive Mode e passare a uno schema d'autenticazione **token-based**. Di nuovo lo stesso pattern del PBX: il token chiude il buco che la password lascia aperto.

### Hacking della VPN Citrix

Citrix è una soluzione VPN **client-to-site** che dà accesso a desktop e applicazioni remote: un desktop Windows completo, applicazioni COTS o custom. L'attacco tipico è il **breakout**: dall'applicazione pubblicata si prova a *spawnare un altro processo* nell'ambiente Citrix remoto (`explorer.exe`, `cmd.exe`, PowerShell). Il libro elenca dieci categorie di applicazioni pubblicate da cui si tende a evadere: Help, Microsoft Office, Internet Explorer, giochi Microsoft e Calcolatrice, Task Manager, stampa, hyperlink, accesso a Internet, i testi delle EULA e Salva con nome / accesso al file system.

> [!info] Contromisure Citrix
> Collocare l'istanza Citrix in un ambiente segmentato, monitorato e limitato; autenticazione multi-fattore; valutare (assess) il sistema. La logica è contenere il breakout, non impedirlo del tutto.

---

## 5. VoIP attacks

La VoIP porta la voce sopra una rete IP, con protocolli di signaling **H.323** e **SIP**. Il prezzo di questa convergenza è che la voce **eredita gli attacchi classici della rete IP**: ARP spoofing, sniffing, DoS. È il ponte più chiaro coi capitoli sulle reti — le stesse tecniche, applicate a un flusso audio.

**Voice over IP (VoIP)** is a very generic term that is used to describe the transport of voice on top of an IP network. Most VoIP solutions rely on **multiple protocols**, at least **one for signaling** and **one for transport of the encoded voice traffic**. Most common open **signaling protocols are: H.323 and SIP** (TCP/UDP 5060) and their role is to **manage call setup, modification and closing**. SIP is similar in style to the HTTP protocol, and it implements different methods and response codes for session establishment and teardown. **The Real-time Transport Protocol (RTP) transports the encoded voice traffic**. The accompanying **Real-Time Control Protocol(RTCP) provides call statistics** (delay, packet loss, jitter,and so on) and control information for the RTP flow. It is mainly used to monitor data distribution and adjust quality of service(QoS) parameters. Difference between RTP and PBX: the RTP stream doesn’t have to cross any voice infrastructure device and it is exchanged directly between the endpoints.

#### Non ho capito però cosa trova effettivamente un attaccante quando farà ad esempio il SIP Scanning (paragrafo successivo). Facciamo finta che ci sia un applicazione come Discord o Skype, o qualsiasi altra cosa che utilizzi VoIP

Ottima cosa da chiarire, perché il pezzo che ti manca è **concettuale**, non tecnico, e senza quello il resto della sezione VoIP non ha senso. Partiamo dalla base che il libro dà per scontata.

**Prima cosa, la più importante: SIP non trasporta la voce.** SIP è il protocollo di _segnalazione_ — è lo strato che fa "squillare", che dice «l'utente A vuole chiamare l'utente B, trovami B, fai suonare il suo telefono, ok sono connessi, ora riaggancia». È il dialogo di _controllo_ della chiamata. L'audio vero e proprio viaggia in un flusso **separato**, l'RTP. Tienilo a mente perché è la chiave di tutto: SIP = il "come si imposta e gestisce la chiamata", RTP = "la voce che si sente".

**Cos'è un SIP proxy, con la tua analogia.** Immagina un sistema VoIP costruito su SIP (Discord e Skype in realtà usano protocolli proprietari loro, ma il _concetto_ è identico — SIP è la versione standard aperta, quella dei telefoni IP aziendali, dei PBX, dei softphone). Quando apri Discord e fai login, il tuo client dice al server «sono l'utente X, sono online, mi trovi qui»: nel mondo SIP quello è il **registrar**, il server dove i telefoni si _registrano_ dichiarando dove sono raggiungibili. Quando poi chiami un amico, il tuo client non sa dove sia fisicamente sulla rete: manda la richiesta di chiamata al server, che **localizza** il tuo amico e gli fa squillare il client. Quel server che riceve le richieste e le _instrada_ verso il destinatario è il **SIP proxy** — il centralino, lo smistatore, il "router delle chiamate". È il cervello dell'infrastruttura VoIP: ogni setup di chiamata ci passa attraverso.

Ecco l'architettura e cosa fa davvero il proxy:![[Pasted image 20260713145907.png]]Ora la tua domanda vera: **cosa trova l'attaccante col SIP scanning, in pratica?** Il proxy e gli altri device SIP "vivono" su una porta nota, la **5060** (UDP o TCP; la 5061 per la variante cifrata). Lo scanner — SiVuS, SIPVicious — spazza la rete cercando chi risponde su quella porta parlando SIP, e quello che ti restituisce è essenzialmente la **mappa dell'infrastruttura VoIP**:

- **i server SIP** — il proxy, il registrar, il PBX/IP-PBX. Cioè il _centralino_, il bersaglio grosso: il nodo da cui passa la segnalazione di tutte le chiamate.
- **gli endpoint** — i singoli telefoni IP e softphone che parlano SIP sulla rete.
- **marca, modello e versione firmware** di ognuno. E qui c'è un dettaglio che il libro sottolinea e che moltiplica il valore dello scan: **SIP è un protocollo testuale, leggibile** (assomiglia a HTTP). Le risposte dei device arrivano in chiaro come testo, spesso con tanto di banner che dichiara "sono un Cisco modello tale, firmware talaltro" — informazione servita su un piatto per cercare gli exploit noti di quel modello.

Quindi, tornando all'analogia: il SIP scanning è come se qualcuno, invece di usare Discord, scandagliasse la rete per trovare **i server di Discord**, capire dove sono, che versione girano e quali client sono connessi — senza fare nessuna chiamata, solo mappando l'impianto.

E il motivo per cui è il **primo** passo del capitolo VoIP è che è pura ricognizione, il _footprint→scan_ del mondo telefonico, e apre la strada a tutto il resto: trovato il proxy sai _dove_ enumerare gli utenti (svwar.py, prossima sezione), _cosa_ colpire con l'INVITE flood per il DoS, e _quale_ flusso intercettare. La contromisura, non a caso, è **segmentare** la rete VoIP da quella degli utenti: se lo scanner non raggiunge la 5060, non trova nulla da cui partire.

Ora il contrasto che ti serve per non confonderti — le app che avevi in mente **NON usano SIP**. Alcuni provider VoIP, come Skype, usano un protocollo proprietario (e Skype tra l'altro è stato dismesso da Microsoft nel 2025). Stessa cosa per **Discord** (basato su WebRTC), **FaceTime**, **WhatsApp**, **Zoom**, **Teams**: protocolli proprietari o WebRTC, non SIP standard. Il motivo è pratico — le app di consumo vogliono attraversare i NAT domestici e girare in un browser senza configurazione, mentre SIP è lo standard _aperto_ e interoperabile del mondo enterprise, dove serve che il telefono Cisco e il PBX Asterisk di due aziende diverse si parlino.

Ed è proprio questo che rende il SIP scanning un attacco _aziendale_: gli strumenti del capitolo (SiVuS, SIPVicious) cercano la porta 5060 di **PBX, telefoni IP e provider SIP** — l'impianto telefonico di un'organizzazione — non le app di messaggistica sul tuo telefono personale.

### SIP scanning

Si scoprono i proxy SIP e gli altri device con **SiVuS** e **SIPVicious**.

> [!info] Contromisura scanning
> Segmentazione di rete tra il segmento VoIP e quello di accesso utente.

### Saccheggio del TFTP

Molti telefoni SIP scaricano la configurazione da un **server TFTP**, e quei file possono contenere username e password per le funzioni amministrative. Prima si localizza il TFTP (**Nmap**: `nmap –sU –p 69 192.168.1.1/24`), poi si prova a indovinare il **nome del file** di configurazione (TFTP brute-force).

> [!info] Contromisura TFTP
> Restrizione degli accessi al server TFTP.

### Enumerazione degli utenti

Si sfruttano wardialing manuale/automatico e soprattutto il fatto che **SIP è un protocollo human-readable**: osservando le risposte del server si distinguono utenti esistenti e non. Utili anche i **Cisco Directory Services**. Strumenti automatici: **SIPVicious (`svwar.py`), SIPScan, Sipsak**.

> [!info] Contromisura enumerazione
> Segmentare reti VoIP e utente e distribuire sistemi **IDS/IPS**.

### Interception (l'attacco di intercettazione)

È l'attacco più articolato e quello che meglio mostra l'eredità IP della VoIP. Si intercetta prima il **protocollo di signaling** (SIP, SKINNY, UNIStim) e lo **stream media RTP**, tipicamente via **ARP spoofing** (**dsniff, arp-sk**) e sniffing (**tcpdump, Wireshark**). Poi si **identifica il codec** dal campo *Payload Type* o *Media Format*, e infine si **converte lo stream** in un file audio comune (**vomit, scapy**). Esiste un tool all-in-one con GUI, **UCSniff**; per l'analisi offline si usano **Wireshark** (dissector RTP e SKINNY di Cisco), **SIPdump** e **SIPcrack**.

#### Procedura
First, intercept the signaling protocol (SIP, SKINNY, UNIStim) and media RTP stream between the caller and the called person. To circumvent the switches, that are more used instead of hubs, we can use **ARP Spoofing**. 

1. On the interception server, you should first turn on routing, allow the traffic, turn off ICMP redirects, and then reincrement the TTL using iptables. 
2. At this point, after using `dsniff’s` `arpspoof` or `arp-sk` to corrupt the client’s ARP cache, you should be able to access the VoIP data stream using a sniffer (`tcpdump` or `Wireshark`). 
3. Once you have identified the RTP stream, you need to identify the codec that has been used to encode the voice this information is in the Payload Type (PT) field in the UDP stream or in the Media Format field in the SIP.
4. A tool such as `vomit` enables you to convert the conversation from G.711 voice codec to WAV based on a `tcpdump` output file. Similar tool is `scapy` and it sniff the live traffic. GUI and all-in-one interception and voice capture tools is `UCSniff`. It has two main main modes: Monitor (passive sniffer) and MiTM.

> [!warning] Perché conta
> Qui non si "buca" nulla di nuovo: ARP spoofing + sniff sono attacchi di rete già noti. La novità è che il payload è una **telefonata ricostruibile in un file audio**. La convergenza voce-dati trasforma un attacco di livello 2 in un'intercettazione telefonica.

>[!info] Countermeasures
>- Encryption is available in Secure RTP (SRTP), Transport Layer Security (TLS) and Multimedia Internet Keying (MIKEY). 
>- Firewalls can and should be deployed to protect the VoIP infrastructure core. Make sure it handles the protocols at the application layer. A stateful firewall isn’t often enough because the needed information is carried in different protocols’ header or payload data. 
>- The phones should only download signed configurations and firmware, and they should also use TLS to identify the servers,and vice versa. 
### Denial of Service

Si può negare il servizio all'infrastruttura o a un singolo telefono: inviando un grande volume di **segnalazione di setup fasulla** (SIP `INVITE`) oppure inondando il telefono di traffico indesiderato (unicast o multicast). Strumenti: **Inviteflood, hack_library**.

> [!info] Contromisure DoS
> Segmentazione di rete tra VLAN voce e dati, autenticazione e cifratura di tutte le comunicazioni SIP, e sistemi IDS/IPS.

---

## Contromisure trasversali

Il riepilogo del capitolo si condensa in pochi principi validi per *ogni* forma di accesso remoto. La **password policy** diventa ancora più critica quando l'ingresso è remoto, e va affiancata da **autenticazione a due fattori**. Servono **policy di provisioning** per qualunque tipo di accesso remoto e l'eliminazione del software di controllo remoto non autorizzato. Bisogna ricordarsi che il perimetro remoto non sono solo i modem: **PBX, fax server, sistemi di voicemail** sono superfici a sé. Infine: formare supporto ed end user, essere **estremamente scettici verso le dichiarazioni di sicurezza dei vendor** (i default di fabbrica del PBX insegnano) e definire una use policy stringente con audit di conformità.

---

## Punti aperti / collegamenti

> [!question] Da approfondire
> - **IKE Phase 1: Main vs Aggressive mode** — perché Main protegge l'identità e Aggressive no (numero di messaggi dell'handshake, quando l'auth viaggia in chiaro). È il meccanismo fine dietro l'attacco VPN e meriterebbe una nota-scheda a sé.
> - **RTP e codec** — come il *Payload Type* mappi al codec e perché questo basta a ricostruire l'audio.
> - **SKINNY / UNIStim** — protocolli di signaling proprietari solo nominati.
> - **ARP spoofing** — qui riusato per la VoIP: se non c'è già una nota-scheda nel vault, è il candidato naturale per un link (aggancia il tema sniffing/MITM dei capitoli di rete).

> [!info] Fili coi capitoli
> *footprint → scan → enumerate → exploit* è la stessa metodologia dei Cap. 1–3, qui applicata ai numeri di telefono. Il **password reuse** dei PCF e l'uso di **Cain** richiamano i temi credenziali dei Cap. 4–5. Il dial-up sugli **ICS/SCADA** riaggancia la chiusura del [[ETHL - Cap 6 Cybercrime e APT]] (Stuxnet).

---

## Esercizi (dal deck)

1. Trovare e scaricare via Google un file **PCF**, poi usare **Cain** per il password decoding. Screenshot dei risultati e spiegazione.
2. Usare **Nmap, NTA Monitor, IKEProbe** per stabilire se un VPN server target supporta l'**Aggressive mode**. Screenshot dei risultati "utili" e spiegazione.
3. Usare **SiVuS, SIPVicious** per scansionare un server **SIP** pubblico. Screenshot dei risultati "utili" e spiegazione.


## Domande Esame

- VoIP Attacks. Describe VOIP Enumeration, Denial of Service and other attacks against VoIP. Which tools are used? Write console commands. Which countermeasures? 
- Describe at least three attacks to a VoIP network. Include in your description at least the activities to be carried out, the tools, and the command lines to be used. What are the possible countermeasures for each of these attacks? For example, one of the possible VoIP attacks is the enumeration of VoIP users (this attack will not be considered if you discuss it in your answer). 
- Attacchi VoIP: User enumeration.
- Citrix vulnerabilities 
- VoIP attacks (no enum)