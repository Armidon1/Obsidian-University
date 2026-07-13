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

Il dial-up è il capostipite dell'accesso remoto. Molte aziende lo tengono ancora acceso per raggiungere vecchi server, apparati di rete o ICS, e proprio perché "dimenticato" resta un vettore reale.

### Footprinting: trovare i numeri

Prima di attaccare bisogna procurarsi i numeri da comporre. Il footprinting telefonico consiste nell'**identificare blocchi di numeri** da dare in pasto a un wardialer, raccolti da elenchi telefonici, siti web del target, database di registrazione dei nomi Internet, o composizione manuale.

> [!info] Contromisure footprinting
> Richiedere una password per le richieste sugli account, sanitizzare le informazioni sensibili pubblicate e formare i dipendenti a non divulgarle. È lo stesso principio di igiene informativa che apre ogni capitolo: meno superficie pubblica, meno footprint.

### Wardialing

Il **wardialing** automatizza la scansione di interi blocchi di numeri per scoprire quali rispondono con un modem. Conta sia l'hardware sia il software.

Sul lato **hardware** l'efficienza dipende dal numero e dalla qualità dei modem. Ci sono poi due voci spesso trascurate: i **problemi legali** (le leggi che regolano identificazione delle linee, registrazione delle chiamate e spoofing del numero variano da giurisdizione a giurisdizione) e i **costi accessori** (chiamate a lunga distanza, internazionali o a tariffa nominale che si moltiplicano su migliaia di numeri).

Sul lato **software** contano scheduling automatico, facilità di setup e accuratezza. Strumenti di riferimento: **WarVOX, TeleSweep, PhoneSweep**.

### Brute-force scripting: i cinque domini

Dai risultati del wardialing si categorizzano le connessioni in **domini di penetrazione**, in base a come il server dial-up gestisce l'autenticazione e i tentativi falliti. È la mappa che decide se e come vale la pena montare un attacco brute-force scriptato (con **ZOC, Procomm Plus** e il linguaggio di scripting **ASPECT**).

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

Le misure di sicurezza dial-up sono dodici, ma il punto non è impararle a memoria: sono un **processo continuo** che si chiude tornando al passo 1. In sintesi tematica: inventariare le linee esistenti e **consolidarle** in un modem bank centrale posizionato come connessione *non fidata* fuori dalla rete interna; rendere le linee analogiche difficili da trovare e mettere in sicurezza fisica gli armadi delle telecomunicazioni; monitorare i log del software dial-up; imporre **autenticazione multi-fattore** e **dial-back** (il sistema richiama un numero noto); sensibilizzare l'help desk sul rischio di rilasciare o resettare credenziali; centralizzare il provisioning e stabilire policy ferme. Poi si ricomincia dall'inventario.

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

Il brute-force della voicemail funziona come il dial-up. Servono tre ingredienti: il **numero** per accedere al sistema di voicemail, la **casella target** (3–5 cifre) e una **stima educata della password**, che di norma è composta solo da numeri — ed è proprio questo spazio ristretto a renderla fragile. Strumenti storici per sistemi vecchi e poco sicuri: **Voicemail Box Hacker 3.0** e **VrACK 0.51**, oltre allo scripting **ASPECT**.

> [!info] Contromisure voicemail
> Lockout dopo un numero di tentativi falliti e logging/osservazione delle connessioni alla voicemail.

---

## 4. VPN hacking

La VPN ha rimpiazzato il dial-up come meccanismo di accesso remoto, ma sposta il problema, non lo elimina: ora il bersaglio è il gateway, i suoi profili di configurazione e il modo in cui negozia le chiavi.

### Google hacking dei profili (PCF)

Il client VPN Cisco salva le impostazioni in file di profilo **`.pcf`**. Cercando `filetype:pcf` su Google si trovano PCF esposti pubblicamente: si scaricano, si importano nel client, ci si connette alla rete target e si lanciano attacchi ulteriori. Le password memorizzate nel PCF alimentano poi **attacchi di password reuse** (con **Cain**).

> [!info] Contromisure PCF
> User awareness, sanitizzazione delle informazioni sensibili sui siti e uso di **Google Alerts** per accorgersi quando materiale del genere finisce indicizzato. Collega al tema del riuso delle credenziali di [[ETHL - LAN Manager (LM) vs NTLM]].

### Probing dei server IPsec

Prima si verifica che la porta del servizio sia raggiungibile (**UDP 500**), poi si fa identificazione della VPN IPsec e fingerprinting del gateway, individuando la **modalità di IKE Phase 1** e l'hardware del server remoto. Strumenti: **Nmap, NTA Monitor, IKEProber**.

> [!warning] Contromisura assente
> Contro il semplice probing non si può fare molto: il servizio, per funzionare, deve rispondere. La difesa si sposta a valle, sulla configurazione (vedi Aggressive Mode).

### Attacco all'IKE Aggressive Mode

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

### SIP scanning

Si scoprono i proxy SIP e gli altri device con **SiVuS** e **SIPVicious**.

> [!info] Contromisura scanning
> Segmentazione di rete tra il segmento VoIP e quello di accesso utente.

### Saccheggio del TFTP

Molti telefoni SIP scaricano la configurazione da un **server TFTP**, e quei file possono contenere username e password per le funzioni amministrative. Prima si localizza il TFTP (**Nmap**), poi si prova a indovinare il **nome del file** di configurazione (TFTP brute-force).

> [!info] Contromisura TFTP
> Restrizione degli accessi al server TFTP.

### Enumerazione degli utenti

Si sfruttano wardialing manuale/automatico e soprattutto il fatto che **SIP è un protocollo human-readable**: osservando le risposte del server si distinguono utenti esistenti e non. Utili anche i **Cisco Directory Services**. Strumenti automatici: **SIPVicious (`svwar.py`), SIPScan, Sipsak**.

> [!info] Contromisura enumerazione
> Segmentare reti VoIP e utente e distribuire sistemi **IDS/IPS**.

### Interception (l'attacco di intercettazione)

È l'attacco più articolato e quello che meglio mostra l'eredità IP della VoIP. Si intercetta prima il **protocollo di signaling** (SIP, SKINNY, UNIStim) e lo **stream media RTP**, tipicamente via **ARP spoofing** (**dsniff, arp-sk**) e sniffing (**tcpdump, Wireshark**). Poi si **identifica il codec** dal campo *Payload Type* o *Media Format*, e infine si **converte lo stream** in un file audio comune (**vomit, scapy**). Esiste un tool all-in-one con GUI, **UCSniff**; per l'analisi offline si usano **Wireshark** (dissector RTP e SKINNY di Cisco), **SIPdump** e **SIPcrack**.

> [!warning] Perché conta
> Qui non si "buca" nulla di nuovo: ARP spoofing + sniff sono attacchi di rete già noti. La novità è che il payload è una **telefonata ricostruibile in un file audio**. La convergenza voce-dati trasforma un attacco di livello 2 in un'intercettazione telefonica.

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
