# Hacking Hardware (Cap. 9 — Hacking Exposed 7)

> [!abstract] Di cosa parla
> Il capitolo sposta l'attenzione dalle minacce logiche al software verso le minacce **fisiche e hardware**. I controlli di accesso fisico e la sicurezza degli endpoint vengono spesso incontrati dall'attaccante *molto prima* di arrivare a un access point di rete o a un prompt di login. Si parte dal bypass delle serrature, si passa alla clonazione delle card di accesso, poi all'attacco ai dispositivi (hard disk, USB) e si chiude con un'introduzione al **reverse engineering** dell'hardware.
> Dispositivi embedded ben connessi (smartphone, tablet) sono ovunque e usano gli stessi mezzi — GSM, Wi-Fi, Bluetooth, RFID — creando un rischio significativo per aziende e privati.

guarda anche la nota gemella [[Hacking_Exposed_7_Cap9_Nota_di_studio]]

**Struttura del capitolo:**

1. Physical Access: Getting In The Door
2. Hacking Devices
3. Reverse Engineering Hardware

---

## 1. Physical Access: Getting In The Door

Attaccare un dispositivo hardware richiede, ovviamente, **accesso fisico** ad esso. Qui si esaminano le tecniche per bypassare il meccanismo di controllo d'accesso più comune di tutti: la porta chiusa a chiave.

### 1.1 Lock Bumping (apertura serrature)

#### La chiave normale

![[Pasted image 20260908121936.png]]

> [!info] Come funziona una serratura
> La serratura è una delle forme più antiche di sicurezza fisica: protegge porte, rack, case e praticamente tutto il resto. Blocca un meccanismo tramite una serie di **pin** disposti su due file:
> - **Driver pin** (blu): sospesi da molle, spingono verso il basso.
> - **Key pin** (rossi): quelli su cui agisce la chiave.
>
> Quando si inserisce la chiave corretta, i key pin spingono i driver pin fino ad allineare il gap tra le due file esattamente sul bordo del plug, chiamato **shear line** (linea di taglio, in giallo). A quel punto il meccanismo è libero e la serratura può ruotare.

#### La bump key
s
<iframe width="560" height="315" src="https://www.youtube.com/embed/r3cuVPSySZw?si=oyrlZGhpbkL-XvCh" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

> [!example] Cos'è una bump key
> È una chiave costruita appositamente, con i denti tutti alla **stessa altezza minima** (i key pin scendono al punto più basso). Sfrutta la fisica newtoniana:
> 1. La bump key viene inserita nella serratura.
> 2. La si colpisce ("bumping") con un cacciavite o qualsiasi oggetto che dia un colpo secco e fermo, creando shock meccanici.
> 3. Ogni tip della chiave trasferisce la forza ai key pin, che "saltano" verso l'alto e passano *brevemente* attraverso la shear line.
> 4. In quella frazione di secondo di allineamento, la serratura può essere ruotata e aperta.

> [!warning] Risultati dell'uso della bump key
> - Un "bumper" esperto apre la serratura **veloce quanto** chi ha la chiave giusta.
> - Il bumping **non danneggia** la serratura (a meno di ripetizioni eccessive o esecuzione maldestra).
> - **Non lascia tracce** di manomissione.
> - Bersagli tipici: porte, rack, case dei PC, lucchetti dei cavi dei laptop, ecc.

> [!note] Caso reale — White House / Medeco
> A DefCon 2007 alcuni ricercatori mostrarono di poter fare bump e picking anche dei nuovi lucchetti high-security **Medeco M3**, usati alla Casa Bianca, al Pentagono e in ambasciate. Medeco detiene circa il **70%** del mercato delle serrature. Morale: anche le serrature "sicurissime" possono essere aperte.

#### Contromisure al bump key

> [!success] Difese
> - Poche serrature sono progettate contro il bumping. Due bump key aprono circa il **70%** delle serrature usate in Nord America.
> - Alcune marche resistono meglio: **Medeco** e **Assa Abloy**. Medeco aggiunge un **sidebar** (pin aggiuntivo che deve essere allineato *e* ruotato all'angolo corretto) più pin angolati, rendendo picking e bumping difficili. → Ma non fidarsi troppo delle loro dichiarazioni (i modelli più vecchi sono comunque stati aperti).
> - **Non affidarsi solo alle serrature**: usare autenticazione a due fattori e controlli compensativi — tastierino PIN, lettore di impronte, guardia di sicurezza, video sorveglianza, allarmi antintrusione.
> - I **cable lock** dei laptop sono ancora più vulnerabili: un lucchetto Kensington è stato aperto in meno di 2 minuti con un tubo di penna di plastica e un rotolo di carta igienica.

> [!caution] Attenzione legale
> Il bumping ripetuto può danneggiare o distruggere una serratura. Usare bump key solo su serrature di pratica e su quelle che si è autorizzati a testare — in alcune giurisdizioni possederle o portarle può essere illegale.

> [!question] Domande di ripasso — Lock Bumping
> 1. Che cos'è la *shear line* e perché è cruciale per aprire una serratura?
> 2. Descrivi passo per passo il funzionamento fisico di una bump key.
> 3. Perché il bumping è particolarmente pericoloso dal punto di vista forense/investigativo?
> 4. Cos'è il *sidebar* delle serrature Medeco e quale attacco cerca di prevenire?
> 5. Quale principio di sicurezza suggerisce di non affidarsi mai a una singola serratura?

### 1.2 Clonazione delle Card di Accesso

Molte strutture sicure richiedono una card di accesso oltre ad altre misure. Le card sono di due tipi: **magnetic stripe** (*magstripe*) o **RFID** (spesso dette *proximity card*). L'obiettivo dell'attacco: creare un clone della card e sostituire le informazioni chiave con dati custom per ottenere accesso fisico.

#### Card a banda magnetica (Magstripe)
![[Pasted image 20260908122036.png]]
> [!info] Caratteristiche della magstripe
> - Gli standard ISO (**7810, 7811, 7813**) definiscono dimensioni e specificano **tre tracce** di dati (track 1, 2, 3).
> - Contengono dati come ID number, serial number, nome, indirizzo, SSN, saldi conto…
> - La **maggioranza non usa alcuna misura di sicurezza**: i dati sono in chiaro (nessuna cifratura) e spesso in una codifica non standard.
> - Risultato: sono **banali da clonare e riutilizzare**.
>
> *Esempio Track 1, Format B:* start sentinel (`%`), format code (`B`), Primary Account Number/PAN (fino a 19 caratteri), field separator (`^`), nome (2–26 caratteri), field separator, data di scadenza (YYMM).

> [!example] Strumenti — Reader/Writer e Card Explorer
> - Un **reader/writer per magstripe** (es. da makinterface.de) con connettore USB, costo ~**35$**. Chiunque può leggere, scrivere e clonare card. vedi immagine di sopra
> - Software **Magnetic-Stripe Card Explorer**: mostra i dati in formato Char, Binary o ISO.![[Pasted image 20260908122608.png]]
> - **Read**: leggere più card dello stesso tipo per individuare quali bit cambiano.
> - **Write**: determinare quale checksum è usato → ricalcolare quello nuovo prima di scrivere. Alcune card hanno un checksum che però il reader non controlla.

> [!tip] Analisi con diff — predire l'ID
> Molte access card contengono semplicemente un ID sequenziale. Leggendo più card dello stesso tipo e usando un tool di **diff** si vede quali bit differiscono. Esempio (in grassetto i bit diversi):
> ```
> Card 1: Track 1: 0010000001111000100101010110001111100110000001001
> Card 2: Track 2: 0010000001111000100101011000001111100110000001001
> ```
> Le due card sono **sequenziali** → si può predire il valore della card successiva o precedente e fare brute-force.

> [!caution] Rischio in scrittura
> Riscrivere i dati su una magstripe può corrompere la card sorgente e renderla inutilizzabile o malfunzionante. Usare solo card usa-e-getta per test/lettura.

#### Hacking delle card RFID

> [!info] Cos'è RFID
> - **RFID** = Radio Frequency Identification: usa **segnali radio** invece del magnetismo.
> - Ormai richiesto anche nei **passaporti**.
> - I dati possono essere letti **a distanza** e sono di solito **non cifrati**.
> - Le card operano su due spettri principali: **125/135 kHz** o **13.56 MHz**.
> - La card RFID più comune è di **HID Corp** (protocollo proprietario). La ricerca iniziale per clonarle fu fatta da **Chris Paget (2007)**, mai pubblicata pienamente dopo una lettera di HID che lo accusava di violazione di brevetto.

> [!example] MiFare Classic — "don't roll your own crypto"
> - **MiFare** è il brand di chip RFID "sicuri" più diffuso al mondo (prodotto da NXP), usa il cifrario stream proprietario **CRYPTO1** con chiave a **48 bit**.
> - Nel **2008** i ricercatori della **Radboud University Nijmegen** fecero un reverse-engineering completo, clonando e manipolando il contenuto di una OV-Chipkaart, usando il device **Proxmark** (125 kHz / 13.56 MHz).
> - Pubblicarono 4 paper (*A Practical Attack on the MIFARE Classic*, *Dismantling MIFARE Classic*, *Wirelessly Pickpocketing a MIFARE Classic Card*, *Ciphertext-only Cryptanalysis on Hardened MIFARE Classic Cards*).
> - **Lezione**: non inventarsi crittografia proprietaria ("don't roll your own crypto!").

> [!note] Caso reale — Boston Subway Hack
> La **MBTA** (Massachusetts Bay Transportation Authority) sosteneva di aver reso sicure le sue MiFare Classic aggiungendo cifratura proprietaria. Alcuni studenti di **Ron Rivest** al **MIT** le violarono comunque, "sniffando" il tornello e usando una piattaforma di brute-force su **FPGA** (KwickBreak) contro Crypto-1.

> [!example] Strumenti hardware per RFID
> - Kit e device pre-assemblati per reader e card comuni da **openpcd.org**.
> - **Proxmark3** con FPGA on-board: decodifica diversi protocolli RFID (richiede assemblaggio, non per principianti/budget ridotto).
> - **USRP (Universal Software Radio Peripheral)**: intercetta le onde radio grezze RFID → cattura e replay dei segnali. Costo ~**1000$**, software di decodifica da scrivere per ogni protocollo.

> [!success] Contromisure alla clonazione delle card
> - **Prima**: i vendor volevano solo abbassare i costi → tecnologia RFID il più economica possibile, sicurezza trascurata.
> - **Ora**: sistemi con **challenge-response crittografico** completo per prevenire cloning e replay:
>   1. La card RFID, energizzata dal reader, riceve un **challenge**.
>   2. Risponde con un valore cifrato/firmato con la **chiave privata memorizzata sulla card**.
>   3. Il **reader valida** la risposta prima di concedere l'accesso.
> - Anche intercettando l'intera conversazione, l'attaccante **non può riusare** la stessa risposta.
> - Alcuni usano algoritmi aperti, altri proprietari (questi ultimi sono un campanello d'allarme).

> [!caution] Tailgating
> Il metodo più efficace per entrare in molte aree sicure resta il **tailgating**: seguire fisicamente una persona con credenziali valide. Nessuna crittografia lo ferma.

> [!question] Domande di ripasso — Card di accesso
> 1. Quali sono i due tipi di card di accesso e come si chiamano informalmente le RFID?
> 2. Perché le card magstripe sono "banali da clonare"? Cosa manca a livello di sicurezza?
> 3. Spiega come l'analisi con *diff* di più card permette di predire l'ID di una card sequenziale.
> 4. Cosa dimostrò la Radboud University sulla MiFare Classic e qual è la lezione crittografica?
> 5. Descrivi il meccanismo challenge-response e perché rende inutile il replay di una risposta intercettata.
> 6. Perché il tailgating è considerato la minaccia più difficile da bloccare?

---

## 2. Hacking Devices

Assunto che l'attaccante abbia già bypassato i controlli basati su serratura, l'attenzione passa ai **dispositivi che memorizzano informazioni sensibili**.

### 2.1 Bypass della ATA Password Security

#### Interfacce ATA e cos'è la ATA Security

> [!info] Interfacce ATA per hard disk
> Esistono due tipi di interfaccia **ATA (Advanced Technology Attachment)**:
> - **PATA (Parallel ATA)** — l'IDE ora si chiama PATA.
> - **SATA (Serial ATA)** — più recente e veloce.

> [!info] ATA Security
> - Richiede una **password per accedere all'hard disk**, digitata prima che il BIOS possa accedervi.
> - Presente praticamente in **ogni hard drive prodotto dal 2000**.
> - Fa parte della **specifica ATA** → non è legata a un brand o dispositivo specifico.
> - **Non cifra** il disco: ne impedisce solo l'accesso → sicurezza minima. I contenuti restano leggibili se si aggira il controllo.

L'ATA Security è una funzione di sicurezza che sta dentro il firmware dei dischi (sia SATA meccanici che SSD SATA e M.2 SATA). In pratica è una password che blocca il disco _a livello hardware_, cioè direttamente nel controller del disco, non nel sistema operativo e non nel BIOS.

L'idea è semplice: se imposti questa password, all'accensione il disco parte in stato "bloccato" e rifiuta di leggere o scrivere qualsiasi dato finché non riceve la password corretta. Non è come una cartella protetta da password in Windows: qui è il disco stesso che si rifiuta di collaborare.

**Come funziona a grandi linee**

Ci sono due password possibili: una "User" (quella che serve per usare il disco tutti i giorni) e una "Master" (una specie di password di riserva/amministratore). E ci sono due livelli, "High" e "Maximum", che cambiano cosa puoi fare con la Master password se dimentichi quella User — nel livello Maximum, se perdi la User password, l'unico modo per riusare il disco è cancellarlo completamente.

**Perché sul tuo desktop non l'hai mai visto**

Due motivi principali. Primo: è disattivata di default. Nessuno la attiva a meno che tu non lo faccia di proposito con un programma apposta (tipo `hdparm` su Linux, o l'opzione "HDD Password" nel BIOS di molti portatili). Secondo, e più importante per te: la maggior parte delle schede madri desktop, all'avvio, manda al disco un comando chiamato **SECURITY FREEZE LOCK**. Questo "congela" lo stato della sicurezza per tutta la sessione, in modo che nessuno — nemmeno un malware — possa impostare una password a tua insaputa mentre il PC è acceso. Ecco perché nei desktop la cosa passa completamente inosservata: c'è, ma è congelata e nascosta.

Sui portatili invece è molto più visibile, perché la voce "password del disco" nel BIOS sfrutta proprio l'ATA Security.

**Il punto che ti interessa: gli adattatori USB**

Qui c'è una cosa importante da sapere. I comandi dell'ATA Security sono comandi ATA "nativi". Quando colleghi un disco tramite un adattatore USB, non stai parlando direttamente in ATA: l'adattatore fa da traduttore tra USB e SATA (la traduzione si chiama SAT, SCSI/ATA Translation). Molti di questi ponticelli USB **non lasciano passare** i comandi di sicurezza ATA.

Le conseguenze pratiche:

- Tramite USB spesso non riesci a _gestire_ l'ATA Security (impostarla, toglierla, ecc.), anche volendo.
- Se un disco è _già bloccato_ con ATA Security e lo colleghi via USB, rischia di apparire inaccessibile e non riesci a sbloccarlo, perché l'adattatore non trasmette il comando di sblocco. Per gestirlo devi collegarlo direttamente alla porta SATA/M.2 della scheda madre.
- Alcuni adattatori di qualità supportano il "pass-through" dei comandi ATA, altri no. È molto variabile.

Quindi il fatto che tu abbia sempre usato quei dischi via adattatore senza problemi è del tutto normale: erano dischi senza ATA Security attiva, e l'adattatore semplicemente leggeva e scriveva dati come al solito.

Un'ultima nota utile: su molti SSD moderni l'ATA Security è collegata alla cifratura hardware. Questi dischi cifrano _sempre_ i dati internamente, e la password ATA serve a sbloccare la chiave di cifratura. Su un HDD meccanico più vecchio, invece, spesso è solo un "lucchetto" logico e i dati grezzi sul piatto restano in chiaro — motivo per cui su quei dischi la protezione è meno robusta di quanto sembri.

Se ti interessa, posso mostrarti i comandi concreti per vedere lo stato dell'ATA Security del tuo disco (per esempio con `hdparm -I` su Linux) senza rischiare di attivarla per sbaglio.

#### L'attacco Hot-Swap (Fool BIOS)

> [!example] Hot-swap attack — passi
> ATA security è usata per scoraggiare l'uso di un laptop rubato. Il metodo di bypass più comune e semplice: **hot-swap** dell'unità in un sistema con ATA security disabilitata. Il problema nasce da un *disconnect* tra BIOS e drive: molti drive assumono che il BIOS abbia già autenticato la password e accettano il comando `SECURITY SET PASSWORD` senza aver prima ricevuto quella corrente.
> 1. Trovare un computer capace di impostare password ATA e un drive **sbloccato**.
> 2. Avviare il computer con il drive sbloccato ed entrare nel **BIOS**, andando nel menu che permette di impostare la password.
> 3. Rimuovere con cura il drive sbloccato e inserire il drive **bloccato**.
> 4. Impostare la password hard-disk tramite il BIOS → il drive **accetta** la nuova password.
> 5. Riavviare: il BIOS chiede di sbloccare il drive, e la nuova password funziona, **bypassando** quella vecchia.
> 6. La password può poi essere rimossa dal sistema se non desiderata.
> 
> Un chiarimento tecnico: quell'attacco non sfruttava una proprietà universale dell'ATA security, ma un _bug di firmware_ di certi drive specifici, che accettavano `SECURITY SET PASSWORD` senza aver mai verificato quella corrente. Non tutti i drive erano vulnerabili nemmeno all'epoca. I drive moderni ben fatti non lo sono, ma "moderno" non è una garanzia — dipende dalla singola implementazione del firmware. Aggiungi che il SATA hot-plug fisico su hardware desktop è sempre stato rischioso (il libro stesso avvisa che puoi cuocere la scheda logica), il che lo rendeva più un trucco da laboratorio che una tecnica pulita.

> [!caution] Rischi dell'hot-swap
> Cortocircuitare i lead dell'hard disk tipicamente causa il reboot del computer e può danneggiare la scheda logica. L'hot-swap può danneggiare drive, file system, computer o l'operatore. Procedere a proprio rischio.

> [!warning] "Virus" della password ATA (teorico)
> - ATA Security è usata su hard drive di Xbox e su laptop, **ma** il BIOS delle macchine desktop spesso **ignora** l'ATA security.
> - Un attaccante potrebbe **attivare** ATA security e di fatto **distruggere** un hard drive o tenerlo in ostaggio (ransom): la macchina non farebbe boot e nessun comando BIOS potrebbe aiutare.
> - Al momento è solo un **attacco teorico**.
> - inoltre orami il mondo si è spostata alla tecnologia **nvme** perciò vaffanculo ai SATA

> [!example] Bypass professionale — Vogon Password Cracker POD
> - Cambia la password da una semplice **GUI**.
> - Permette alle forze dell'ordine di **immaging** del drive e poi ripristinare la password originale, così il proprietario non si accorge di nulla.
> - Funziona accedendo alla **drive service area**: area speciale del disco per firmware, informazioni sulla geometria, ecc., **inaccessibile all'utente**.

Erano le **forze dell'ordine** (polizia forense) — le slide dicono "law enforcement". Lasciami cercare qualche dettaglio concreto, perché Vogon è un nome un po' di nicchia e voglio darti informazioni accurate.Confermato: era per **forze dell'ordine / investigazione forense**, non per i militari (anche se la loro pubblicità parlava di "lotta al crimine e al terrorismo globale", da qui forse la confusione).

**Chi era Vogon**

Vogon International era un'azienda britannica, nata nel recupero dati e poi specializzata in strumenti forensi per la polizia. La loro gamma andava da singoli moduli software fino a workstation forensi complete. Il Password Cracker POD è stato lanciato intorno al **2004**, quindi parliamo di roba pensata per gli hard disk meccanici dei portatili di vent'anni fa.

**Cosa faceva e come**

Il nome "Password Cracker" è in realtà fuorviante: non "craccava" niente per forza bruta. Identificava e rimuoveva le password dai dischi "platter-locked" dei laptop, e veniva presentato come un grosso risparmio di tempo nelle indagini sotto copertura. Il meccanismo è quello che hai già visto nelle slide: accedeva alla drive service area, l'area speciale del disco usata per firmware e informazioni sulla geometria, dove il disco stesso tiene memorizzata la password ATA. In pratica non indovinava la password: se la andava a _leggere_ direttamente dov'era scritta.

**La password nella service area.** Il disco deve confrontare la password che digiti con qualcosa. Quel "qualcosa" è memorizzato nella service area. Il difetto non è che _esiste_ — è inevitabile che esista — ma che è memorizzata in chiaro o mal protetta, così chi ha lo strumento giusto la legge invece di indovinarla. È pigrizia ingegneristica e taglio dei costi, non una porta di servizio nascosta.

**I firmware update non autenticati.** Il disco accetta un nuovo firmware senza verificare bene chi glielo manda. Anche questo è un problema di design vecchio stile (l'autenticazione crittografica del firmware costa progettazione e chip più capaci), non un canale segreto. Anzi, un vero backdoor governativo _non_ vorrebbe un meccanismo così, perché lo può usare chiunque, criminali compresi.

**Il punto più vicino a un "backdoor": la Master password.** Qui la tua intuizione tocca qualcosa di reale, ma il colpo di scena è che _non è segreto_. La specifica ATA prevede ufficialmente una Master password, ed è documentata pubblicamente. Il problema è che molti produttori spedivano i dischi con Master password di default note o banali (a volte 32 spazi, o stringhe tipo il nome del vendor). Non è una porta nascosta per i governi: è una porta lasciata aperta _per tutti_, descritta nel manuale. Chiunque legga la spec la conosce.

**Il dettaglio interessante (e inquietante) per un investigatore**

La caratteristica di punta era la reversibilità silenziosa. Lo strumento si collegava tramite l'interfaccia nativa del disco, usava un piccolo database per conservare la password catturata mentre accedeva al drive, e dopo aver fatto l'immagine del disco poteva rimettere a posto le password originali "in maniera evidenzialmente valida", riportando il disco alle condizioni di partenza. Tutto questo senza dover avvisare l'utente che una password era stata bypassata.

Il motivo per cui a un forense questo importa così tanto: la **catena di custodia**. Devono poter dimostrare in tribunale che non hanno alterato la prova. Come spiega bene un altro strumento moderno equivalente, riportare il disco a uno stato leggibile non cambia il suo valore di hash, perché la password ATA è tenuta nella service area del firmware, che non viene mai inclusa nel calcolo dell'hash. Quindi l'immagine del disco resta identica bit-per-bit e il sospettato, riavendo indietro il portatile, non si accorge di nulla.

**Il collegamento con la tua tesi "è deprecato"**

Qui torna il discorso di prima. Vogon come prodotto è effettivamente sparito da un pezzo, ma la _categoria_ è vivissima. Oggi lo stesso lavoro lo fa gente come **Atola Insight Forensic**: legge la credenziale che il disco stesso conserva nella sua area firmware e riporta il disco a uno stato leggibile in meno di due minuti, con pochi clic, sia per il livello High che Maximum. Il recupero automatico funziona per moltissimi drive Seagate, WD, Toshiba, Hitachi, Samsung, Fujitsu, Maxtor SATA e IDE.

Il che conferma esattamente il punto: l'ATA security non è mai stata una barriera seria. Come riassume il centro sicurezza di UT Austin, la password ATA può essere aggirata in vari modi — firmware modificati che la rimuovono, dispositivi hardware e software che la superano con brute force o password backdoor dei produttori, o servizi di recupero dati che leggono direttamente i piatti del disco.

Quindi il tuo istinto è giusto ma con una sfumatura: non è che l'ATA security _era_ vulnerabile e _ora_ è stata risolta. È sempre stata debole, e gli strumenti per sfruttarla si sono solo evoluti (da Vogon a Atola) mentre il mondo passava a difese vere come la full disk encryption. Vogon è il fossile; il predatore è ancora in circolazione.

> [!success] Contromisure ATA
> - **Miglior difesa**: *evitare* di affidarsi ad ATA security per proteggere i drive da manomissione o per proteggerne i contenuti — è banale da bypassare e dà un falso senso di sicurezza.
> - **Alternativa**: usare **full disk encryption** per proteggere l'intero contenuto o le partizioni sensibili — **BitLocker**, **TrueCrypt**, **SecurStar**.
> - (Nota: esiste anche l'attacco *cold boot*, trattato nel Cap. 4, che aggira certe implementazioni di disk encryption.)

La lezione di fondo delle slide non solo regge, ma è persino peggiorata. Il punto della contromisura — "non affidarti all'ATA security, ti dà un falso senso di sicurezza" — è più vero che mai.

E c'è un dettaglio importante che il libro del 2012 non poteva avere: nel 2018 Meijer e van Gastel ("Self-encrypting deception") hanno dimostrato che la cifratura hardware di molti SSD diffusi (anche marchi grossi) era implementata malissimo, bypassabile senza conoscere la password. E siccome BitLocker, di default, si _fidava_ della cifratura hardware quando il drive la dichiarava, in pratica migliaia di macchine "cifrate" erano scardinabili. Microsoft ha dovuto cambiare i default e spingere verso la cifratura software. Quindi la storia dei "lucchetti hardware che non sono vera protezione" non è finita nel 2012: è tornata più forte.

> [!question] Domande di ripasso — ATA Password
> 1. La ATA security cifra il disco? Cosa fa esattamente?
> 2. Spiega perché il "disconnect" tra BIOS e drive rende possibile l'attacco hot-swap.
> 3. Elenca i passi dell'hot-swap attack.
> 4. In che senso l'ATA security potrebbe essere usata come "virus"/ransomware?
> 5. Perché la miglior difesa è *non* affidarsi ad ATA security, e quale alternativa si propone?

### 2.2 U3 Drives e USB U3 Hack

> [!info] U3: software su una flash drive
> - Standard **U3**: una **partizione secondaria** inclusa in alcune chiavette USB (SanDisk, Memorex). Permette di portare dati *e applicazioni* in tasca — "come un mini-laptop".
> - Appena inserita, la **Launchpad** appare: si eseguono le proprie applicazioni sulla macchina di chiunque e si portano via tutti i dati.

> [!example] Come funziona U3 (il trucco)
> - La chiavetta U3 si presenta come **due dispositivi** in "Risorse del computer":
>   1. Un **Removable Disk** (storage normale).
>   2. Un **CD drive nascosto** chiamato "U3" (partizione read-only).
> - La partizione U3 esegue **automaticamente** ciò che è configurato nel file `autorun.inf`, sfruttando la funzione **Autorun** di Windows.
> - Il produttore fornisce un tool per **sovrascrivere** la partizione U3 con un ISO custom → ci si può inserire un programma malevolo che gira nel contesto dell'utente loggato.


**La sottigliezza che le slide non spiegano bene: perché U3 era "speciale"**

Questo è il concetto che vale davvero la pena capire. Le slide dicono che la chiavetta si presenta come due dispositivi, uno dei quali è un "CD drive nascosto". Non è un dettaglio estetico: è _il cuore del trucco_. Windows trattava (e tratta) l'Autorun in modo diverso a seconda del tipo di dispositivo. Per le unità removibili "normali" l'esecuzione automatica era già più restrittiva; per le unità **CD/DVD**, invece, l'autorun restava pieno e affidabile.

U3 sfruttava proprio questo: emulava un lettore CD-ROM read-only, così Windows lo trattava come un disco ottico e ne eseguiva il contenuto automaticamente, con un'affidabilità che una semplice chiavetta non aveva. Quindi dire genericamente "funziona grazie ad Autorun" è vero ma impreciso — funzionava grazie all'**Autorun via emulazione CD-ROM**, che è ciò che aggirava le restrizioni già presenti sulle chiavette normali. Le slide questo lo saltano, e senza di esso non si capisce perché U3 fosse più pericoloso di una USB qualsiasi.

> [!example] U3 PocketKnife
> **PocketKnife** è una suite di potenti tool di hacking che vive sulla partizione disco della U3, e gira come le altre applicazioni. Tra le cose che fa:
> - Rubare **password** (Firefox, IE, mail, MSN, network…) e **product key**.
> - **Dump** della SAM di Windows (FGDUMP / PWDUMP), LSA secrets, cache.
> - Rubare file (slurp user files), cronologia URL, hash password WiFi, IP esterno.
> - **Killare l'antivirus**, **disabilitare il firewall** di Windows, port scan, e altro.

> [!example] Custom Launchpad — esecuzione automatica
> - Con il **U3 Customizer** si crea un file custom da eseguire quando la U3 viene inserita.
> - **Universal_Customizer.exe** scrive un ISO contenente lo **script Fgdump** sulla flash disk; il launcher U3 custom lancia PocketKnife.
> - Risultato: password e file vengono rubati e messi automaticamente sulla flash drive appena inserita.
>
> Passi (da libro): creare un `autorun.inf` custom (`open= go.cmd`), un `go.cmd` che lancia `fgdump.exe`, poi impacchettare i file nella cartella U3CUSTOM con `ISOCreate.cmd` e scrivere l'ISO con Universal_Customizer.exe.

**Perché U3 è morto e sepolto**

U3 era una joint venture tra SanDisk e M-Systems, lanciata intorno al 2005. SanDisk ha annunciato la fine del supporto nel 2009 e il sito con i tool di customizzazione è sparito intorno al 2010. Quindi non è "un po' datato": è un ecosistema estinto da ~15 anni. Non trovi più chiavette U3 né gli strumenti ufficiali per riscriverne la partizione.

E soprattutto è morto il meccanismo che lo faceva funzionare: l'**Autorun da chiavetta USB**. Con l'aggiornamento di Microsoft del febbraio 2011 (KB971029), Autorun è stato disabilitato per i supporti removibili non ottici su tutte le versioni di Windows allora in uso. Da lì in poi, infilare una USB non lancia più automaticamente niente. L'intera premessa del PocketKnife — "la inserisci e parte da sola" — è caduta.


> [!caution] Attenzione
> Il device U3 **non distingue** tra computer: infetta/compromette qualsiasi macchina in cui è inserito. Attenzione a non infettare se stessi.

##### Difesa

> [!success] Contromisure all'U3 Hack
> L'attacco funziona grazie ad **Autorun**. Si contrasta in due modi:
> - **Disabilitare Autorun** sul sistema (vedi KB Microsoft 953252).
> - Tenere premuto **SHIFT** prima di inserire la USB (impedisce l'avvio del programma di default, uso per-inserimento).
> - Anche con Autorun disabilitato, un device malevolo può infettare con **altri meccanismi**: in caso di dubbio, **non inserire mai** un device non fidato.

> [!info] Difese aggiuntive e news
> - **Microsoft ha limitato Autorun** (fix opzionale in Windows Update, feb 2011) — spinto anche dal worm **Stuxnet**.
> - Il **militare USA ha bandito le chiavette USB** (nov 2008) per fermare gli "adversary attacks".

**Il riferimento a Stuxnet è impreciso**

Le slide legano il fix di Autorun del 2011 a Stuxnet. È una connessione traballante: Stuxnet si propagava via USB ma sfruttava soprattutto la **vulnerabilità dei file .LNK** (MS10-046), non il classico `autorun.inf`. Il worm che ha davvero abusato di Autorun in modo massiccio, e che ha spinto Microsoft a chiuderlo, è **Conficker** (2008-2009). Se ti serve l'esempio "giusto" di malware da autorun, è Conficker, non Stuxnet.

Il bando delle USB nell'esercito USA (novembre 2008), invece, è corretto ma anch'esso ha un trigger preciso che le slide non nominano: il worm **Agent.btz**, che aveva infettato reti militari classificate (l'operazione di bonifica si chiamò Buckshot Yankee).


> [!tip] Riduzione immediata del rischio
> - Bloccare tutti i device USB via **Group Policy**.
> - Disabilitare **AutoRun**.
> - **Incollare** fisicamente le porte USB.

> [!success] Soluzione migliore — IEEE 1667
> - Standard: *Standard Protocol for Authentication in Host Attachments of Transient Storage Devices*.
> - I device USB possono essere **firmati e autenticati** → solo device autorizzati sono ammessi.
> - Implementato in **Windows 7**.

**IEEE 1667 come "soluzione migliore": promessa mancata**

Qui le slide sono ottimiste in modo datato. IEEE 1667 (Enhanced Storage) è stato effettivamente supportato in Windows 7, ma nella pratica **non è mai diventato la difesa che prometteva**. Richiedeva hardware specifico che quasi nessuno produceva, è rimasto confinato a nicchie enterprise e oggi è di fatto irrilevante come contromisura generale. Presentarlo come "la soluzione migliore" è invecchiato malissimo: la difesa reale che ha vinto è tutt'altra roba (controllo dei dispositivi via policy, e per l'HID injection le protezioni tipo controlli sui nuovi dispositivi di input).


**Cosa è invece vivissimo: la minaccia USB "cattivo"**

Le slide chiudono con una frase profetica — "anche con Autorun disabilitato, un device malevolo può infettare con altri meccanismi". È esattamente lì che è andata la storia. L'attacco USB non è morto, ha solo smesso di dipendere da Autorun:

- **USB Rubber Ducky** e simili: il dispositivo non si finge una chiavetta, si finge una **tastiera**. Windows si fida ciecamente delle tastiere, e il device "digita" comandi a velocità sovrumana appena inserito. Nessun Autorun coinvolto, quindi disabilitarlo non serve a niente.
- **BadUSB** (Karsten Nohl / SRLabs, 2014): riprogrammazione del firmware del controller USB. Un dispositivo apparentemente innocuo può ridichiararsi qualcos'altro (tastiera, scheda di rete). È a livello di firmware, sotto il sistema operativo, difficilissimo da rilevare.
- Cavi malevoli tipo **O.MG cable**: l'attacco dentro un cavo di ricarica dall'aspetto normale.

Quindi la morale, di nuovo, è la stessa dell'ATA security e regge benissimo oggi: il PocketKnife su U3 è un fossile, ma il principio "non inserire mai un dispositivo USB non fidato" è più valido che mai — anzi peggiorato, perché contro un Rubber Ducky le contromisure delle slide (disabilitare Autorun, tenere premuto Shift) non fanno _nulla_. L'unica difesa che ha attraversato indenne tutti questi anni è la più rozza e la più radicale che le slide citano quasi per scherzo: il controllo fisico e per-policy delle porte.

> [!question] Domande di ripasso — U3 / USB
> 1. Come si presenta una chiavetta U3 al sistema operativo (quanti e quali dispositivi)?
> 2. Quale funzione di Windows sfrutta l'U3 hack per eseguire codice automaticamente?
> 3. Cosa fa la suite PocketKnife? Cita almeno quattro azioni.
> 4. Come si contrasta l'attacco a livello di sistema e a livello di singolo inserimento?
> 5. Cosa introduce lo standard IEEE 1667 e in che sistema operativo è stato implementato?

### 2.3 Default Configurations

Una delle minacce più trascurate sono le **impostazioni di fabbrica** (out-of-the-box), pensate per mostrare funzionalità ma spesso insicure.

**Il principio: intramontabile, anzi peggiorato**

L'idea centrale — "le configurazioni di fabbrica insicure sono la minaccia più trascurata" — non è affatto deprecata. È il contrario: con l'esplosione dell'IoT (telecamere, router, videocitofoni, lampadine smart, termostati) il problema è oggi _ordini di grandezza_ più grave di quando fu scritto il libro. Il caso simbolo è la **botnet Mirai (2016)**: ha infettato centinaia di migliaia di dispositivi IoT proprio usando una lista di ~60 coppie utente/password di default, ed è stata usata per attacchi DDoS storici (Dyn, che mise offline mezzo internet USA). È esattamente il "Standard/Default Passwords" delle slide, scalato a livello planetario. Quindi su questo capitolo il tuo istinto "è deprecato" **non** vale: il concetto è più attuale che mai.

C'è anche stata una risposta normativa che il libro non poteva prevedere: diverse giurisdizioni hanno **vietato per legge** le password di default identiche sui dispositivi. La California (SB-327, in vigore dal 2020) e soprattutto il Regno Unito con il **PSTI Act (2024)** obbligano i produttori a non spedire più device con password comuni preimpostate. Il problema è stato preso così sul serio da diventare oggetto di legge.

> [!example] Owned Out of the Box — ASUS Eee PC
> - L'**Eee PC 701** era spedito con **Xandros Linux** custom.
> - Il servizio di file-sharing **Samba** era **attivo di default** (per facilità d'uso verso utenti poco tecnici).
> - Era una versione vulnerabile, **rootabile** con un modulo Metasploit standard, con quasi nessuno sforzo. → *"Easy to learn, easy to work, easy to root."*
> - Se Samba fosse stato off di default, la superficie d'attacco sarebbe stata molto ridotta.

**Gli esempi specifici: quasi tutti fossili**

L'**ASUS Eee PC 701** con Xandros Linux e Samba aperto è del 2007-2008. Quel modello, quella distro, quel modulo Metasploit: tutto storia. Vale zero come minaccia oggi, ma resta un buon _esempio didattico_ del principio "servizio attivo di default = superficie d'attacco". La frase "easy to learn, easy to work, easy to root" era un gioco sullo slogan ufficiale ASUS "easy to learn, easy to work, easy to play".

La **Default Password List di Phenoelit** esiste ancora concettualmente, ma quel dominio/URL è di fatto morto. Oggi il riferimento vivo è **RouterPasswords.com**, i database dentro strumenti come Metasploit, o le liste integrate in scanner come **Shodan** (il "motore di ricerca dei dispositivi esposti" che è diventato lo strumento chiave per trovare device con credenziali di default esposti su internet — roba che nel 2012 era agli inizi).

Gli **ATM Triton** con codice admin condiviso: il caso reale è del 2008 (Derrick Shoemaker), e riguardava i Triton RL2000 che uscivano di fabbrica con lo stesso master password nel manuale. Ancora oggi ci sono ATM vulnerabili, ma il vettore moderno è più il **jackpotting** con malware (Ploutus, attacchi "black box") che il semplice codice di default. Reggono come principio, ma la tecnica è evoluta.

> [!warning] Standard / Default Passwords
> - Ogni device che richiede login ha il problema "chicken-and-egg" di comunicare la password iniziale all'utente → molti usano **password standard** o impostazioni insicure.
> - Esiste una **Default Password List** mantenuta da Phenoelit (phenoelit.org/dpl/dpl.html).
> - I peggiori offender sono i **router embedded**, che spesso condividono la stessa password su intere linee di prodotto; molti hanno amministrazione remota e password di default ancora attiva su Internet.
> - Abilita **vulnerability chaining**: un attaccante usa una cross-site request forgery [[CSRF]] per loggarsi nel router e reindirizzare gli utenti verso DNS malevoli.
> - **ATM Triton**: spediti tutti con lo stesso codice di accesso amministrativo → chiunque col codice può stampare il transaction log (che rivelava numeri di conto e nomi dei clienti) o eseguire funzioni amministrative.

> [!note] Casi reali — ATM
> - **2008**: due uomini usarono le **password di default** per riprogrammare gli ATM in modo da erogare banconote da 20$ come se fossero da 1$ (primo arresto per "ATM reprogramming scam").
> - Un ATM alla conferenza **LayerOne** venne compromesso e mostrava messaggi custom sullo schermo.

> [!example] Bluetooth Attacks
> - Il **Bluetooth** è "l'eterna sorgente" di insicurezza dei cellulari: sync, chiamate, trasferimento dati, tethering.
> - Alcuni telefoni sono spediti con la **discovery mode attiva di default** → chiunque può scoprirli e connettersi.
> - Il Bluetooth **supporta la cifratura**, ma è **off di default** e la password di default è **0000**.
> - Ha permesso per quasi un decennio di penetrare reti, rubare contatti e fare social engineering (es. eavesdropping sugli auricolari Bluetooth).
> - Strumento off-the-shelf: **Ubertooth** (ubertooth.sourceforge.net), ~**120$** da SparkFun: sniffing e playback dei frame Bluetooth su tutti gli **80 canali** della banda ISM 2.4 GHz, più spectrum analysis.

**Errori/imprecisioni da segnalare**

C'è un punto da correggere con attenzione nella parte Bluetooth, perché le slide mescolano due cose:

Dire che "il Bluetooth supporta la cifratura ma è off di default e la password di default è 0000" è **impreciso e in parte sbagliato** per il Bluetooth classico. Lo 0000 (e 1234) non è una "password di cifratura disattivata": è il **PIN di default per il pairing** di dispositivi senza interfaccia (auricolari, vivavoce, altoparlanti) che non possono far digitare un codice all'utente. La cifratura in Bluetooth, una volta stabilito il legame, non è banalmente "off" — il problema vero era la debolezza del PIN corto, che rendeva il legame _forzabile_. È una sfumatura, ma il libro la appiattisce in modo fuorviante.

Poi c'è il grande assente temporale: il libro parla di **Bluetooth classico** (BR/EDR). Tutto il mondo si è spostato su **Bluetooth Low Energy (BLE)**, che ha un modello di sicurezza completamente diverso e una storia di vulnerabilità sua (il pairing "Just Works" senza autenticazione, gli attacchi KNOB del 2019, BLESA, ecc.). Le minacce Bluetooth non sono sparite, ma quelle descritte nelle slide appartengono a un'epoca del protocollo che oggi conta poco.

**Ubertooth: ancora vivo, ma superato**

Questo è il dettaglio più utile che ho verificato. L'Ubertooth One esiste ancora (di Great Scott Gadgets, la stessa gente dell'HackRF), ma è invecchiato tecnicamente. Il suo radio-chip, il CC2400, ha un limite hardware serio: può sniffare un solo canale di advertising alla volta, su tre, perché ha una sola radio a banda stretta. E soprattutto, supporta il BLE fino alla specifica 4.0 con copertura limitata della 4.2: nel momento in cui due dispositivi negoziano LE Secure Connections (introdotte in BLE 4.2), l'Ubertooth mostra payload cifrati senza poterli decifrare, anche avendo catturato il pairing.

Oggi lo standard di fatto per catturare BLE non è più l'Ubertooth: è il **dongle Nordic nRF52840** con il firmware nRF Sniffer gratuito, che alimenta direttamente Wireshark ed è ormai lo strumento di riferimento sia per hobbisti che professionisti, a un costo bassissimo e con supporto completo al BLE 5.2, incluse le modalità 2 Mbps e long-range PHY che l'Ubertooth non riesce nemmeno a ricevere. Quindi il prezzo "~120$ da SparkFun" nelle slide è ancora nell'ordine di grandezza giusto per l'Ubertooth, ma non è più la scelta ovvia che era.

**In sintesi**

Il principio (default insicuri = disastro) è il più attuale del capitolo, tanto da essere diventato legge. Gli esempi (Eee PC, Triton, Bluetooth classico, Phenoelit) sono datati ma didatticamente ancora validi come illustrazioni. Le imprecisioni da correggere: lo 0000 è un PIN di pairing, non una "password di cifratura off"; e tutto il discorso Bluetooth va mentalmente aggiornato da BR/EDR a BLE, con Ubertooth ormai affiancato/superato dall'nRF52840.

A questo punto abbiamo coperto un bel pezzo di capitolo. Vuoi che ti prepari la nota Obsidian di ripasso che ti offrivo, con tutto — ATA/hot-swap/Vogon, U3, default config — e dei callout che marcano esplicitamente cosa è "storico/deprecato", cosa è "errore da correggere" e cosa "regge ancora oggi"?

> [!question] Domande di ripasso — Default Configurations
> 1. Perché il caso ASUS Eee PC è un esempio di rischio da configurazione di default?
> 2. Perché i router embedded sono considerati i "peggiori offender" per le default password?
> 3. Cos'è il *vulnerability chaining* nel contesto dei router?
> 4. Qual è la password di default del Bluetooth e la cifratura è attiva di default?
> 5. Cosa permette di fare il device Ubertooth e su quale banda opera?

---

## 3. Reverse Engineering Hardware

Fino a qui si sono visti attacchi a dispositivi COTS (*Commercial Off-The-Shelf*) come drive ATA e chiavette USB. Quando l'attaccante affronta device più custom e complessi, deve fare **reverse engineering** per sbloccare le informazioni all'interno.

### 3.1 Mapping the Device e Identificazione dei Chip

> [!info] Mappare il dispositivo
> - Il primo passo è **rimuovere il coperchio** per accedere alla circuiteria interna: di solito basta svitare qualche vite. Se il device è incollato, si usano heatgun e leva; se è sigillato ermeticamente, il case va (delicatamente) distrutto; per le viti di sicurezza speciali i bit si trovano facilmente online.
> - Molti device usano componenti COTS ben documentati nei **datasheet** del produttore (funzioni, pinout, specifiche operative).

> [!warning] Rimuovere le protezioni fisiche
> Su una PCB possono esserci **epossidica**, conformal coating o altre protezioni che nascondono i chip (IC):
> - L'epossidica si rimuove con un processo all'**acido nitrico (HNO₃)** — pericoloso, solo per chi conosce la de-encapsulation e le procedure di sicurezza.
> - Il conformal coating si rimuove con MG Chemicals 8310 Stripper, o (con cautela) un Dremel.
> - Alternativa quasi non invasiva: **X-ray imaging**.

> [!example] Identificare i chip integrati (IC)
> - Cercare il **part number** su Google o su rivenditori (Newark, DigiKey) per trovare il **datasheet** (packaging, caratteristiche elettriche, pin diagram, note applicative).
> - I chip **DIP** sono comodi, ma nei sistemi moderni prevalgono i **surface mount**.
> - Il top di un IC è marcato con un punto o una tacca; i pin si numerano in **senso antiorario** da quel segno.
> - Rimozione: i DIP con solder wick; i surface mount con ChipQuik o una hot air station.

> [!info] Identificare i pin importanti
> - La **tacca** in alto allinea con la tacca del chip fisico (dice quale pin è il pin 0/21); per chip quadrati si usa un cerchio o triangolo.
> - Pin più interessanti per il reverse engineer: **TX e RX** (bus seriale). Altri: **DL** (digital lines), **AD** (analog/digital lines), oltre a **PWR** e **GND**.
> - Le board moderne sono **multilayer** (da 4 a 64 strati) → tracciare le connessioni a vista è difficile.
> - Per creare la mappa completa di componenti e bus si usa un **multimetro con funzione di continuità (toning)**: manda corrente tra i due lead e **emette un beep/flash** quando un filo è connesso, confermando la connessione anche se il percorso non è visibile.

> [!caution] Attenzione col multimetro
> Alcuni device non tollerano la corrente fornita dalla funzione di toning: troppa potenza sui componenti sbagliati può danneggiare o distruggere il device.

> [!question] Domande di ripasso — Mapping & IC
> 1. Quali metodi si usano per rimuovere epossidica e conformal coating dai chip?
> 2. Come si trova il datasheet di un IC e cosa contiene di utile?
> 3. Come si numerano i pin di un IC e quale segno indica il punto di partenza?
> 4. Perché le board multilayer complicano il reverse engineering?
> 5. Come funziona la funzione di *toning* di un multimetro per mappare il bus?

Questa è la sezione **meno deprecata di tutto il libro**, e per un motivo semplice: è fisica, non software. La chimica della de-encapsulation, la numerazione dei pin, il test di continuità con il multimetro — queste cose non invecchiano, perché non dipendono da una versione di Windows o da un protocollo che cambia. Un datasheet si legge oggi come nel 2012. Quindi qui il tuo istinto "è deprecato?" per una volta va quasi tutto verso il "no".

Detto ciò, ci sono un paio di **errori** da correggere nella tua nota e soprattutto una grossa parte _mancante_ (la tecnica non è deprecata, ma il libro si ferma a metà strada rispetto a come si lavora oggi).

**Errori da sistemare nella nota**

Il più netto è nel callout "Identificare i pin importanti": scrivi che la tacca _"dice quale pin è il pin 0/21"_. Questo è sbagliato — la numerazione dei pin negli IC parte da **pin 1**, non da pin 0. Non esiste una convenzione "pin 0" negli integrati standard. Quel "0/21" è quasi certamente un residuo corrotto (OCR o copia mal riuscita) del testo originale: la frase corretta è semplicemente "indica qual è il **pin 1**".

Sul "senso antiorario" invece sei nel giusto, ma manca una precisazione importante che è proprio il tipo di trabocchetto da esame: la numerazione è antioraria **guardando il chip dall'alto** (lato componenti). Se lo guardi da sotto (lato saldature, come capita con i BGA), l'immagine è specchiata e il verso si inverte. Vale la pena aggiungerlo, perché è l'errore classico che fa saldare il pin sbagliato.

Un'imprecisione più lieve: "DL (digital lines), AD (analog/digital lines)" sono sigle vaghe e non standard. I pin _davvero_ ghiotti per chi fa reverse, oltre a TX/RX, hanno nomi precisi: le interfacce di debug **JTAG** (TCK, TMS, TDI, TDO) e **SWD** (SWDIO, SWCLK), e i bus **I²C** (SDA/SCL) e **SPI** (MOSI/MISO/SCK/CS). Se nella nota metti questi al posto del generico "DL/AD", hai qualcosa di molto più utile e corretto.

(Minore: "da 4 a 64 strati" è tecnicamente possibile ma fuorviante come tipico — la stragrande maggioranza delle board di consumo sta sui 4-12 strati; 64 è roba da backplane esotici.)

**Cosa il libro salta — la parte che oggi conta di più**

Il capitolo descrive il reverse _fisico_ (aprire, identificare, tracciare col multimetro) ma si ferma prima del pezzo che nel 2012 era già la vera scorciatoia e oggi è centrale: **le interfacce di debug integrate**. Quasi ogni dispositivo ha una JTAG o una SWD sulla board — spesso solo dei pad o dei fori non popolati. Trovarle e collegarcisi ti dà accesso diretto alla CPU: puoi fermare il processore, leggere/scrivere la memoria, dumpare il firmware. È molto più efficiente che tracciare bus a mano.

E qui c'è un'ironia che vale la pena conoscere: lo strumento simbolo per _scovare_ automaticamente una JTAG nascosta è il **JTAGulator**, creato da **Joe Grand** (alias Kingpin, del gruppo L0pht) — che è proprio uno degli autori del materiale di hardware hacking da cui derivano queste slide. Il libro descrive il metodo manuale; l'evoluzione naturale è il suo stesso tool.

Insieme al JTAGulator, la cassetta degli attrezzi moderna che il libro non poteva avere pienamente:

- **Logic analyzer USB economici** (i cloni Saleae da poche decine di euro): oggi "vedere" cosa passa su un bus seriale costa quasi niente, mentre nel 2012 era attrezzatura costosa.
- **Bus Pirate** e **Flipper Zero**: multi-tool per parlare a I²C/SPI/UART al volo.
- **Chip-off**: dissaldi direttamente la memoria flash/eMMC e la leggi con un programmatore esterno. È diventata _la_ tecnica principe della forense su smartphone e IoT — bypassa tutta la parte di tracciamento.
- L'**X-ray** che il libro cita come "quasi non invasivo" oggi è arrivato fino al **CT scanning** delle PCB: ricostruisci in 3D tutti gli strati interni senza toccare nulla. Esattamente la risposta al problema "multilayer difficile da tracciare a vista".

Quindi la sintesi: la sezione è **valida e ancora insegnabile così com'è** (a differenza di U3 o dell'hot-swap), ma è _incompleta_ — fotografa il reverse manuale e si ferma prima di JTAG/SWD, chip-off e strumenti economici, che sono il cuore del lavoro reale odierno.

### 3.2 Sniffing dei Bus Data

> [!info] Sniffing del bus
> - Come le reti, i **bus** hardware trasmettono dati da un componente all'altro: una rete può essere vista come un "bus multi-computer".
> - Le informazioni sul bus sono generalmente **non protette** → suscettibili di **intercept, replay e man-in-the-middle**.
> - **Eccezione**: sistemi **DRM** come **HDMI-HDCP** (*High-bandwidth Digital Content Protection*), che cifrano le informazioni chip-to-chip.

> [!example] Uso del logic analyzer
> - Una buona ricognizione identifica quali linee fanno parte del bus da intercettare e a quale **clock rate** viaggiano i dati.
> - Un **logic analyzer** permette di vedere e registrare i segnali sul bus (1 e 0) che verranno decodificati dopo.
> - Per l'attacco di sniffing: collegare i **logic probe** ai vari contatti di chip/pin e impostare l'analyzer per ricevere i segnali.
> - Alcuni logic analyzer hanno **decoder integrati** per protocolli comuni: **I2C, SPI, Serial**.
> - Lead grandi possono richiedere microscopio stereo, PCB trace repair kit e micro-saldature (kit ~300$).

> [!question] Domande di ripasso — Bus Data
> 1. A quali attacchi è vulnerabile un bus non protetto?
> 2. Qual è un esempio di bus cifrato e perché lo è?
> 3. A cosa serve un logic analyzer nello sniffing?
> 4. Quali protocolli di bus comuni possono essere decodificati automaticamente da alcuni analyzer?

### 3.3 Sniffing dell'Interfaccia Wireless

> [!info] Attacco all'interfaccia wireless
> - Se possibile si fa un attacco **layer 2 software** (es. **802.11 Wi-Fi**, che opera al data link layer). Altrimenti serve ricognizione.
> - Primo passo: identificare l'**FCC ID** del device. Ogni device che opera in radiofrequenza negli USA deve avere un FCC ID (stampato sul device, sulla confezione o nel manuale).
> - L'ID è composto da un **grantee code** di 3 caratteri + caratteri variabili. Cercandolo su **fcc.gov/oet/ea/fccid/** si ottengono documenti utili: **frequenze radio** operative e diagrammi interni.

> [!example] Symbol decoding
> - Conoscendo le frequenze radio e il **tipo di modulazione**, si può fare il **symbol decoding**: decodificare i bit di più basso livello dal canale wireless (analogo ai dati di un bus fisico).
> - Datasheet di un IC, manuale utente o FCC search confermano le frequenze RF usate.
> - Strumento: **Software-Defined Radio (SDR)** — es. **WinRadio** o **USRP**. Anche con un SDR può servire molta programmazione software per arrivare allo stream di simboli.

> [!question] Domande di ripasso — Wireless
> 1. Cos'è l'FCC ID e quali informazioni utili permette di ottenere?
> 2. In cosa consiste il *symbol decoding*?
> 3. Quali strumenti Software-Defined Radio vengono citati?

Come la 3.1, queste due sezioni sono **fisica e radio**, quindi invecchiano bene nella sostanza. Ma ci sono un paio di punti dove il libro è ormai fuori data e uno dove è tecnicamente impreciso. Lascia che verifichi due dettagli che sono cambiati dal 2012.Bene, ho confermato il dettaglio che sospettavo. Anche qui la sostanza regge (è fisica e radio), ma ci sono due punti datati e uno da precisare.

**Un errore fattuale ormai vero: il grantee code non è più "3 caratteri"**

La tua nota dice "grantee code di 3 caratteri". Era vero quando fu scritto il libro, ma **è cambiato proprio nel 2012** (ironia della sorte, lo stesso anno di Hacking Exposed 7). La FCC stava esaurendo le combinazioni a 3 caratteri e dal maggio 2013 ha iniziato a emettere codici a **5 caratteri**. La regola attuale è precisa e vale la pena saperla, perché è il tipo di cosa che un esame ama: il grantee code è di 3 caratteri se inizia con una **lettera** (A-Z), di 5 caratteri se inizia con un **numero** (2-9). Lo zero e l'uno non si usano mai, per non confonderli con le lettere O e I. Quindi la formulazione corretta oggi è "grantee code di 3 **o** 5 caratteri". I vecchi codici a 3 caratteri restano validi a vita, quindi ne trovi ancora tantissimi in giro — ma la tua nota, così com'è, è tecnicamente incompleta.

(Nota minore sull'URL: il libro cita `fcc.gov/oet/ea/fccid/`. La pagina di ricerca vive ancora lì, ma esistono mirror di terze parti molto più comodi da usare — **fccid.io** e **fcc.report** — che aggregano foto interne, test report e diagrammi in modo più navigabile. Utile saperlo perché è proprio da lì che un reverse engineer parte davvero.)

**Il pezzo più datato: gli strumenti SDR**

Qui c'è il classico "invecchiamento da prezzi". Il libro cita **WinRadio** e **USRP** come strumenti SDR. Il problema non è che siano sbagliati — l'USRP (di Ettus Research) è tuttora l'apparato professionale di riferimento — ma che nel 2012 fare SDR costava **centinaia o migliaia di dollari**, ed era roba da specialisti. Nel frattempo è successa una piccola rivoluzione che il libro non poteva avere:

- **RTL-SDR**: intorno al 2012 si scoprì che certi sintonizzatori TV USB da ~20-30$ potevano essere usati come ricevitori SDR a banda larga. Ha democratizzato completamente il campo — oggi chiunque può fare ricognizione radio con una chiavetta da pochi euro. Questo _è_ il cambiamento più importante rispetto alle slide.
- **HackRF One** (di Michael Ossmann, lo stesso dell'Ubertooth): ~150$, e a differenza dell'RTL-SDR _trasmette_ anche, non solo riceve. È diventato lo strumento simbolo dell'hardware/RF hacking hobbistico.
- **Flipper Zero**: multi-tool RF sub-GHz alla portata di tutti, oggi il volto pop di questa disciplina.

Quindi il concetto di "usare un SDR per il symbol decoding" è validissimo e attuale, ma la lista di strumenti va mentalmente aggiornata: da "USRP costoso" a "RTL-SDR economico + HackRF". Da segnalare nella nota.

**HDCP: l'"eccezione cifrata" che è stata bucata**

Questo è il punto più gustoso della 3.2. Il libro cita **HDMI-HDCP** come esempio virtuoso di bus cifrato, l'eccezione alla regola "i bus non sono protetti". Ecco il colpo di scena storico: la **master key di HDCP (v1) è trapelata nel 2010** ed è stata confermata autentica da Intel. Da quella chiave si possono derivare tutte le chiavi dei dispositivi, il che ha reso HDCP 1.x sostanzialmente rotto: sono comparsi splitter/stripper hardware che rimuovono la protezione al volo. In più esiste da sempre l'"analog hole" e, per HDCP 2.2, l'attacco HDCP-2.2 su alcune implementazioni.

Non è che l'esempio sia _sbagliato_ — HDCP resta un bus cifrato, quindi illustra bene il concetto. Ma presentarlo come baluardo di sicurezza è invecchiato male: è l'ennesima conferma della tesi di fondo del libro (i meccanismi DRM/hardware danno spesso falsa sicurezza). Vale la pena annotare che l'esempio del "bus cifrato robusto" si è poi rivelato bucabile — è coerente con tutto il resto del capitolo.

**Cosa invece regge perfettamente**

Tutta la parte metodologica è solida e ancora insegnata così: la logica dell'intercept/replay/MITM sui bus, l'uso del logic analyzer con decoder di protocollo per I²C/SPI/UART, la ricognizione via FCC ID per scoprire frequenze e diagrammi interni, il concetto di symbol decoding. Anzi, il flusso di lavoro "trova l'FCC ID → scarica il test report → leggi frequenze e foto interne → sniffa con l'SDR" è _esattamente_ come si lavora oggi in RF reversing. Solo gli strumenti si sono abbassati di prezzo.

**Sintesi per le tue note:** correggi il grantee code in "3 o 5 caratteri", aggiungi RTL-SDR/HackRF accanto a USRP/WinRadio, e nota che HDCP 1.x è stato bucato nel 2010. Il resto è metodo intramontabile.

### 3.4 Firmware Reversing

> [!info] Perché reversare il firmware
> La maggior parte dei device embedded ha un **firmware** custom, spesso **field-upgradable** e scaricabile dal sito del produttore o su richiesta. Al suo interno c'è "una pletora di informazioni succose":
> - **Password di default**, porte amministrative, **backdoor** non intenzionali, interfacce di debug.

> [!example] Hex editor e comando strings
> - Modo più rapido di ispezionare il firmware: un **hex editor** (Hex → ASCII). Tool citati: **010 Editor** (SweetScape) e **IDA Pro**.
> - Dai decode nell'editor si può **indovinare** la cifratura usata (es. si vede che è usato **AES**), password, ecc.
> - **IDA Pro** supporta oltre 50 famiglie di processori (centinaia di processori); spesso il firmware è caricato direttamente dal microcontroller e l'esecuzione parte da un indirizzo fisso (come un file COM MS-DOS) → l'entry point si trova col datasheet.
> - Comando UNIX **`strings`**: stampa tutte le stringhe ASCII di un binario → spesso rivela password hard-coded, chiavi, config (es. `baudrate`, `bootcmd`, `ipaddr`…).

> [!example] Esplorare il file system del firmware
> - Dall'output di `strings` si può capire il **file system** (es. `cramfs`) e montarlo con `mount -o loop -t cramfs`.
> - Con **`find`** si cercano file sensibili come chiavi: `find /tmp/cram -name *key` / `*cert` / `*pem` → trovare `ca.pem`, `clientca.pem`, `priv.pem`. Con chiave pubblica e privata si può **forgiare una connessione SSL** e fingersi un device fidato.
> - **Backdoor**: cercare codice che bypassa la sicurezza con dati di autenticazione hard-coded o una sequenza speciale di input (esempi reali: Intel NetStructure, Palm OS Debug Mode, Sega Dreamcast). Es. in un device medicale un secondo controllo del serial number `0x12 0x34 0x56` fungeva da backdoor per ottenere controllo completo.

> [!example] EEPROM programmers
> - **EEPROM** = Electrically Erasable Programmable Read-Only Memory: memoria non volatile per piccole quantità di dati, spesso il firmware di un microcontroller/CPU. Generalmente **senza forte sicurezza**.
> - Il modo più facile per ottenere il firmware di molti chip è un **universal EEPROM programmer** (da ~200$ per un PICSTART/ChipMax fino a ~1200$ per un B&K Precision 866B).
> - Si identifica il chip (di solito un **microcontroller/MCU**), lo si inserisce nel socket e si lancia il comando **`read`**. Per i surface mount si usa un adattatore o un'interfaccia **ICSP** (In-Circuit Serial Programming).
> - Con un file HEX si riscrive il firmware col comando **`write`**. Il formato **Intel HEX** è usato dagli anni '70. Alcuni chip hanno read/write security (blocca la lettura finché non si fa un erase).

> [!info] Microcontroller Tools, ICE e JTAG
> - **MCU (microcontroller)**: piccola CPU/sistema su singolo IC (processore + poca memoria + Flash non volatile). Molti sono leggibili con un EEPROM programmer con poche protezioni.
> - **FPGA**: gate array riconfigurabile programmato in **HDL** (VHDL, Verilog). Difficile da debuggare per la scarsa visibilità interna → i nodi si routano su pin da analizzare con logic analyzer, oppure via **JTAG**.
> - **Microcontroller dev tools**: es. **MPLAB IDE** per i PIC di Microchip (emulatore software, debugger, assembler, compilatore C).
> - **ICE (In-Circuit Emulator)**: hardware debugger che dà una finestra sul funzionamento dell'hardware in-circuit. Termine che si sovrappone a JTAG. Contattare il produttore per l'ICE disponibile.
> - **JTAG (Joint Test Action Group)**: interfaccia di test tra i componenti su PCB, nata per verificare l'assemblaggio post-produzione. È il tipo di interfaccia ICE più comune sui sistemi embedded moderni → ottima risorsa quando il reversing semplice non basta. **"One size does not fit all"**: pin count da 8 a 20, configurazioni diverse (ARM, Altera, MIPS, Atmel). Progetti open: **OpenOCD** e **UrJTAG**.

Questa è la sezione **più solida e più attuale di tutto il capitolo** — al punto che è la disciplina che oggi è cresciuta di più rispetto al 2012, non diminuita. Il firmware reversing è diventato un campo enorme proprio grazie all'esplosione dell'IoT. Quindi qui la risposta alla domanda "è deprecato?" è un secco no. Ma c'è un tool centrale che manca completamente, e un paio di aggiornamenti importanti sugli strumenti.

**La grande assenza: `binwalk`**

Questo è il buco più vistoso della nota, e non è colpa tua — è che il libro descrive il flusso di lavoro _manuale_ (apri con hex editor → `strings` → indovina il filesystem → monta a mano con `mount -o loop`). Nel frattempo è arrivato lo strumento che ha reso quasi tutto questo automatico: **binwalk**. Fai `binwalk firmware.bin` e ti scansiona l'immagine cercando le "firme" di formati noti (filesystem, kernel, immagini, chiavi), poi con `binwalk -e` **estrae automaticamente** i filesystem incapsulati. È il primo comando che chiunque lancia oggi su un firmware, e ha soppiantato in gran parte il montaggio manuale che descrive il libro. Va assolutamente aggiunto alla nota: il procedimento `strings` → capisci il filesystem → `mount` è ancora valido concettualmente, ma nella pratica lo fa binwalk in un colpo.

Nella stessa famiglia, per il filesystem: il libro cita `cramfs`. Oggi lo standard di fatto nei device embedded è **SquashFS** (con `unsquashfs` per estrarlo). cramfs esiste ancora ma è molto meno comune — vale la pena affiancarli nella nota.

**L'aggiornamento più importante sugli strumenti: Ghidra**

Il libro cita **IDA Pro** come disassembler, ed è corretto — IDA resta lo standard commerciale di riferimento. Ma è sempre stato costoso (licenze da migliaia di euro), il che lo teneva fuori dalla portata di molti. Il cambiamento epocale che il libro non poteva avere: nel **2019 la NSA ha rilasciato Ghidra**, un framework di reverse engineering completo, gratuito e open source, con decompiler incluso. Ha democratizzato il disassembly esattamente come l'RTL-SDR ha fatto con la radio. Oggi la coppia "IDA Pro / Ghidra" va citata insieme, e per chi studia (o per un hobbista) Ghidra è spesso il punto di partenza. Un'ironia che si sposa col capitolo: è proprio la NSA — l'agenzia che uno immaginerebbe voler _nascondere_ certe capacità — ad aver messo in mano a tutti lo strumento.

**Le backdoor hard-coded: la parte più profetica e più viva**

Il callout sulle backdoor (dati di autenticazione hard-coded, sequenze speciali di input) è concettualmente perfetto e oggi _più_ rilevante che mai. Gli esempi del libro (Intel NetStructure, Palm OS Debug Mode, Sega Dreamcast) sono datati, ma il fenomeno è esploso: si trovano regolarmente credenziali hard-coded in router, telecamere IP, DVR. Il caso emblematico post-libro sono le **backdoor nei router D-Link** (2013): un ricercatore scoprì che se lo user-agent del browser era una certa stringa bizzarra (`xmlset_roodkcableoj28840ybtide` — che letto al contrario contiene "edit by 04882 joel backdoor"), si bypassava del tutto l'autenticazione. È _esattamente_ la "sequenza speciale di input" descritta nel libro, trovata in natura su hardware di massa. Se vuoi un esempio moderno da mettere in nota accanto ai tre storici, questo è perfetto.

Aggiungo il collegamento a quanto dicevi sui backdoor governativi qualche messaggio fa: nota che quasi tutte queste backdoor reali si sono rivelate **residui di debug lasciati dagli sviluppatori** (comode in fabbrica, dimenticate in produzione), non porte per i governi. Ennesima conferma del rasoio di Hanlon.

**Un paio di precisazioni tecniche minori**

Nel callout dell'hex editor: attenzione a "dai decode si può indovinare la cifratura usata (es. si vede che è usato AES)". La formulazione è un po' fuorviante — non "vedi" AES guardando i byte cifrati (il ciphertext AES è indistinguibile dal rumore casuale, è il suo scopo). Quello che realmente trovi con `strings`/hex editor sono le **stringhe in chiaro** che _nominano_ l'algoritmo (nomi di librerie, costanti, riferimenti a "aes", "openssl"), oppure zone ad alta entropia che _suggeriscono_ che qualcosa è cifrato/compresso. La distinzione è sottile ma importante: indovini l'uso di AES dai metadati e dai simboli, non decifrando a occhio.

Su **UrJTAG**: è uno dei due progetti open citati per JTAG, ma è ormai in gran parte abbandonato/dormiente. Quello vivo e universale è **OpenOCD**, che è diventato lo standard de facto per parlare a JTAG/SWD. Nella nota li puoi lasciare entrambi ma segnare che OpenOCD è quello attuale.

E un collegamento utile per la tua nota complessiva: qui il libro finalmente introduce **JTAG** in modo esteso — è lo stesso JTAG che ti segnalavo come "grande assente" nella sezione 3.1 sul mapping. Quindi le due sezioni si parlano: il mapping fisico (3.1) e il firmware reversing (3.4) convergono proprio sulla JTAG come porta d'accesso privilegiata. Il **JTAGulator di Joe Grand** che citavo prima è il ponte tra le due: serve a _trovare_ i pin JTAG che poi userai con OpenOCD per fare il dump del firmware.

**Cosa regge senza riserve**

Tutto il resto è metodo intramontabile: il concetto di firmware field-upgradable come miniera di segreti, `strings` come primo comando (validissimo, anzi eterno), la forgiatura di connessioni SSL rubando chiavi dal filesystem, gli EEPROM programmer con `read`/`write`, l'Intel HEX (in uso dagli anni '70 e ancora oggi), la distinzione MCU/FPGA, ICE vs JTAG, il "one size does not fit all". Niente di deprecato qui — semmai il panorama si è arricchito.

**Sintesi per la nota:** aggiungi `binwalk` come primo tool del workflow, affianca **Ghidra** a IDA Pro, affianca **SquashFS** a cramfs, segna **OpenOCD** come lo standard JTAG vivo (UrJTAG dormiente), correggi la frase su AES ("indovini dall'entropia e dai simboli, non decifri a occhio"), e valuta la backdoor D-Link 2013 come esempio moderno.



> [!question] Domande di ripasso — Firmware Reversing
> 1. Che tipo di informazioni sensibili si possono trovare dentro un firmware?
> 2. A cosa serve il comando UNIX `strings` nel reversing?
> 3. Descrivi come, trovando chiavi pubbliche e private nel firmware, si può fingersi un device fidato.
> 4. Cos'è una EEPROM e come si estrae il firmware con un EEPROM programmer?
> 5. Qual è la differenza/relazione tra ICE e JTAG? Perché "one size does not fit all" per JTAG?

---

## Summary (riassunto generale)

> [!abstract] In sintesi
> Nonostante la transizione ai formati digitali, le informazioni restano custodite dietro **serrature tradizionali** e dentro **dispositivi hardware**, ultimo baluardo di riservatezza, integrità e disponibilità. Il capitolo invita a ripensare il programma di protezione includendo le **minacce fisiche** accanto a quelle logiche.
>
> **Filo conduttore — tre livelli di attacco fisico:**
> 1. **Getting in the door**: serrature aperte con **bump key** (senza tracce), card di accesso **magstripe** clonate perché in chiaro, card **RFID** (MiFare/HID) clonate o intercettate; difese = 2FA, challenge-response crittografico, controlli compensativi. Il **tailgating** resta la via più efficace.
> 2. **Hacking devices**: la **ATA password** non cifra e si bypassa con **hot-swap** (→ usare full disk encryption: BitLocker/TrueCrypt/SecurStar); le chiavette **U3** sfruttano **Autorun** per lanciare **PocketKnife** e rubare hash/password (→ disabilitare Autorun, IEEE 1667); le **configurazioni di default** (Samba, password router, ATM, Bluetooth 0000) espongono i sistemi appena accesi.
> 3. **Reverse engineering**: mappare device e IC (datasheet, multimetro/toning), **sniffare i bus** (logic analyzer, I2C/SPI/Serial) e l'**interfaccia wireless** (FCC ID, symbol decoding, SDR), e reversare il **firmware** (hex editor/010/IDA Pro, `strings`, `find` per chiavi, EEPROM programmer, ICE/JTAG).
>
> **Lezioni ricorrenti**: la sicurezza per oscurità e la crittografia proprietaria falliscono ("don't roll your own crypto"); i dati in chiaro su card/bus/firmware sono banali da estrarre; le impostazioni di default insicure sono un rischio sistematico; la difesa efficace è **stratificata** (defense in depth) e usa **cifratura reale** e autenticazione forte.

## Domande di ripasso generale

> [!question] Verifica finale su tutto il capitolo
> 1. Descrivi i **tre macro-argomenti** del capitolo e collega ciascuno a un attacco rappresentativo.
> 2. Confronta **magstripe** e **RFID**: come sono clonate e quali contromisure esistono per ciascuna?
> 3. Spiega perché il messaggio *"don't roll your own crypto"* emerge sia dal caso **MiFare Classic** sia dalla Boston Subway sia dai sistemi RFID proprietari.
> 4. La **ATA password** e la **cifratura full-disk** proteggono i dati in modo diverso: spiega la differenza e perché la prima dà un "falso senso di sicurezza".
> 5. Spiega il ruolo di **Autorun** nell'U3 hack e le tre principali contromisure (sistema, per-inserimento, standard).
> 6. Perché le **default configuration** (password, servizi attivi, Bluetooth) sono definite "una delle minacce più trascurate"? Porta almeno due esempi reali.
> 7. Metti in ordine le fasi del **reverse engineering hardware**, dall'apertura del case fino all'estrazione del firmware.
> 8. Quali strumenti citeresti per: (a) mappare un bus, (b) sniffare un'interfaccia wireless, (c) leggere un firmware da un microcontroller?
> 9. Cos'è **JTAG** e perché è così utile per il reverse engineer? Cosa significa "one size does not fit all" in questo contesto?
> 10. Individua nel capitolo almeno **quattro casi in cui la sicurezza per oscurità (security through obscurity) è fallita**.
