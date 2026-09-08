---
title: "Hacking Exposed 7 — Cap. 9 — Nota di studio"
tags: [cybersecurity, ethical-hacking, hacking-exposed, capitolo-9, hardware, sicurezza-fisica, rfid, firmware, usb]
source: ["Libro", "Slide del docente"]
status: in-revisione
ultima-verifica: 2026-09-08
companion: "[[Hacking_Exposed_7_Cap9_Audit_fonti]]"
---
# Come usare questa nota

Il capitolo è una raccolta di **sei casi**. Ogni caso è costruito sulle stesse tre domande, ed è così che va ripassato:

> [!note] Le tre domande
> **1.** Che cosa protegge il meccanismo? **2.** Quale condizione permette il rischio descritto? **3.** Quale limite resta dopo la contromisura?
> La terza è quella che si dimentica, ed è quella che distingue chi ha capito il caso da chi ha memorizzato il nome dell'attacco.

Notazione: **L###** = pagina stampata del libro; **S##** = pagina PDF delle slide. `[solo slide]` e `[solo libro]` marcano ciò che compare in una fonte sola.

Per la provenienza di ogni affermazione, le divergenze fra libro e slide, i refusi e i contenuti datati: **[[Hacking_Exposed_7_Cap9_Audit_fonti]]**. Qui si studia; lì si verifica.

Nessuna procedura operativa: i meccanismi sono descritti al livello del principio, che è quello che serve per difendersi e per rispondere a una domanda d'esame.

---

# Caso 1 — Serrature e lock bumping

| Domanda | Risposta |
| --- | --- |
| Che cosa protegge | L'accesso fisico a porte, rack, armadi, casse — cioè tutto ciò che sta **prima** di qualunque controllo di rete o di login. |
| Che cosa lo rompe | Una chiave sagomata in modo da spingere simultaneamente tutti i pin oltre la linea di taglio per una frazione di secondo. Non serve conoscere la combinazione della serratura: serve conoscerne il **tipo**. |
| Che cosa resta dopo | Serrature resistenti (sidebar, pin angolati) alzano il costo ma non chiudono il problema: il libro segnala che modelli Medeco più vecchi sono stati aperti da ricerca pubblica. Il controllo compensativo resta necessario. |

**Da ricordare.** Due bump key aprono quasi il **70% delle serrature usate sulle porte in Nord America** (L500). È la cifra che rende il caso: non si tratta di una vulnerabilità di nicchia, ma della condizione ordinaria.

**Le contromisure del libro sono organizzative, non meccaniche** (L500): più dispositivi di chiusura in serie (tastierino o lettore d'impronta *in aggiunta* alla serratura), videosorveglianza, guardie, allarmi antintrusione. Le slide riformulano questo elenco come *"two-factor authentication"* `[solo slide, S7]`: è un prestito lessicale dall'autenticazione informatica, comodo ma non presente nel testo.

**Il caso dei lucchetti a cavo** (L500): un lucchetto Kensington è stato aperto in meno di due minuti con un tubo di cartone e il corpo di una penna. Non è bumping — è un bypass di altra natura, e serve a dire che la categoria "lucchetto" non garantisce niente di per sé.

---

# Caso 2 — Clonazione delle carte di accesso

Due tecnologie, stesso schema di fondo: **la carta dichiara un'identità, il lettore le crede.**

## 2a. Banda magnetica

| Domanda | Risposta |
| --- | --- |
| Che cosa protegge | Nulla, nella maggior parte dei casi. La banda è un **supporto di memorizzazione**, non un meccanismo di sicurezza. |
| Che cosa lo rompe | La maggioranza delle carte codifica i dati **in chiaro** (L500): leggerli e riscriverli è banale, e l'attrezzatura è economica. |
| Che cosa resta dopo | Non esiste una contromisura *sulla carta magnetica*: il libro non ne propone. La via d'uscita è cambiare tecnologia, non irrobustire la banda. |

**La distinzione che vale l'intero caso — tre cose diverse:**

- **Codifica** = come i dati sono rappresentati. Spesso in formato personalizzato, quindi *non immediatamente leggibile*. Questo non è protezione: è solo un formato da decodificare.
- **Checksum** = valore di controllo per rilevare errori o danneggiamenti del supporto. Non protegge da un attaccante, che può ricalcolarlo. E il libro aggiunge il dettaglio più istruttivo: **a volte il checksum è presente sulla carta ma il lettore non lo verifica affatto** (L502) — un controllo che esiste sulla carta e non esiste nel sistema.
- **Protezione crittografica** = assente qui, presente in parte nei sistemi RFID moderni (caso 2b).

Attenzione al confronto fra fonti: il libro dice che i dati sono "in chiaro", la slide S12 scrive "Not clear encoding". Non è una contraddizione: **assenza di cifratura ≠ formato standard leggibile**. I dati sono non cifrati *e* in formato proprietario.

## 2b. RFID

| Domanda | Risposta |
| --- | --- |
| Che cosa protegge | Nei sistemi più recenti: l'identità della carta, tramite autenticazione crittografica invece che semplice lettura di un numero. |
| Che cosa lo rompe | Molte carte in campo restano **non protette** e clonabili come le magnetiche (L503). Dove la crittografia c'è, il punto debole storico è la **crittografia proprietaria**: MIFARE Classic ne è il caso di scuola. |
| Che cosa resta dopo | Il challenge-response impedisce il riuso di una conversazione intercettata, ma non dice nulla su *chi* tiene in mano la carta — e non copre il tailgating (sotto). |

**Challenge-response, perché risolve il replay.** Il lettore invia una sfida diversa ogni volta; la carta risponde con un valore che dipende **dalla sfida e da un segreto** che non transita. Chi registra l'intera conversazione ottiene una risposta valida per *quella* sfida e inutile per la successiva (L504).

> [!warning] Crittografia proprietaria
> Il libro è esplicito: schemi crittografici sviluppati internamente "should raise significant concerns among buyers" — *don't roll your own crypto* (L504, S14). MIFARE Classic è l'esempio: cifrario proprietario CRYPTO1, smontato da ricerca accademica pubblica, e la MBTA di Boston aveva a sua volta aggiunto cifratura proprietaria sopra, senza esito `[S14–17]`. Il nome di un meccanismo non è una prova della sua sicurezza.

> [!warning] Il tailgating batte tutto
> Il libro chiude la sezione sulle carte con una nota che ne ridimensiona l'intera trattazione: seguire una persona con credenziali valide **resta la via più efficace di ingresso in molte aree protette** (L504). Qualunque discussione sulla robustezza delle credenziali va letta con questo limite davanti.

**Nota sulla ricerca.** Due episodi nelle fonti mostrano la pressione legale sulla divulgazione, con esiti opposti: la ricerca di Chris Paget sulla clonazione delle carte HID (2007) non fu pubblicata dopo una lettera del produttore al suo datore di lavoro (L503); NXP tentò di bloccare la pubblicazione dell'articolo su MIFARE e l'ingiunzione fu **respinta**, con la corte che valorizzò l'informare il pubblico su un problema del chip `[S15]`.

---

# Caso 3 — Password ATA sui dischi

| Domanda | Risposta |
| --- | --- |
| Che cosa protegge | L'**accesso** al disco tramite BIOS. Nient'altro. |
| Che cosa lo rompe | Il disco delega l'autenticazione a un componente che non controlla. Molte unità accettano il comando di *impostazione* della password senza aver prima ricevuto quella corrente, perché presumono che il BIOS abbia già autenticato l'utente (L505). |
| Che cosa resta dopo | La cifratura dell'intero disco protegge il **contenuto**, ma non è assoluta: il libro rimanda al Cap. 4 per l'attacco *cold boot*, che aggira certe implementazioni di cifratura (L507). |

> [!note] Distinzione centrale
> **Impedire l'accesso non è cifrare.** La password ATA controlla una porta; non trasforma i dati. Un disco protetto solo da password ATA, estratto dal sistema, contiene dati in chiaro. Il libro parla esplicitamente di "false sense of security" (L506).

**Il meccanismo generalizzato — vale ben oltre l'ATA.** Il difetto non è crittografico: è di **fiducia mal riposta fra due componenti**. Il disco assume che il BIOS abbia fatto un controllo, il BIOS è sotto il controllo di chi ha in mano la macchina, e nessuno dei due verifica l'assunzione dell'altro. È lo stesso schema che si ritrova in qualunque architettura dove un componente si fida di un'affermazione fatta da un altro senza poterla verificare.

**Una funzione di sicurezza come superficie di attacco** `[solo slide, S23]`: su molti BIOS desktop la funzione ATA è ignota al firmware. Chi la attiva dall'esterno può rendere un disco inutilizzabile o chiederne il riscatto, e nessun comando del BIOS aiuta. La slide qualifica lo scenario come *teorico al momento della lezione* — va conservato quel qualificatore, ma il principio resta: **una protezione che il legittimo proprietario non sa di avere è una leva per chi la scopre.**

**Contromisure.** Non affidarsi alla password ATA; usare cifratura del volume (L506, S27). I prodotti citati dalle fonti sono d'epoca — vedi l'audit prima di trattarli come raccomandazioni.

**Curiosità utile** `[solo slide, S26]`: gli strumenti forensi operano sulla *drive service area*, un'area del disco riservata a firmware e informazioni di geometria e non accessibile all'utente. Un disco contiene più di ciò che il sistema operativo mostra.

---

# Caso 4 — U3 e AutoRun

| Domanda | Risposta |
| --- | --- |
| Che cosa protegge | Nulla: U3 è una **funzionalità di comodità**, non una protezione. È il caso in cui la superficie di attacco nasce da una feature. |
| Che cosa lo rompe | Due condizioni **congiunte**: (a) la chiavetta si presenta al sistema come due dispositivi, di cui uno è un'**unità CD** `[solo slide, S31]`; (b) l'host ha AutoRun attivo, e AutoRun interviene su quel tipo di supporto. La partizione può essere riscritta con gli strumenti di personalizzazione forniti dal produttore, e il programma sostituito viene eseguito **nel contesto dell'utente collegato** (L507). |
| Che cosa resta dopo | Disattivare AutoRun interrompe *questo* meccanismo. Il libro è esplicito: un dispositivo malevolo può infettare **con altri meccanismi** (L509). La contromisura chiude una porta, non il problema. |

> [!note] Dove sta il difetto
> Non nella chiavetta: nella **funzione dell'host**. AutoRun è una funzionalità del sistema operativo ospite; U3 e il suo Launchpad sono software sul dispositivo. Chi colloca la vulnerabilità nel dispositivo non ha capito il caso — ed è la ragione per cui la contromisura è una configurazione dell'host, non un divieto sul modello di chiavetta.

**Contromisure, in ordine di ambito** (L509, S41–43):

- Disattivare AutoRun sul sistema (la via principale).
- Tenere premuto SHIFT prima di inserire il supporto: impedisce il lancio automatico, ma è per singolo uso e dipende dall'operatore.
- Restrizioni sui dispositivi USB via Group Policy `[solo slide, S41]`.
- **IEEE 1667** `[solo slide, S42]`: standard di autenticazione dei dispositivi di memorizzazione transitori — i dispositivi vengono firmati e autenticati, così solo quelli autorizzati sono ammessi. È l'unica contromisura strutturale del blocco: sposta il problema da "cosa fa il supporto" a "questo supporto è autorizzato".
- Sigillare fisicamente le porte `[solo slide, S41]` — misura brutale, citata per completezza.

**Perché il vettore importa storicamente.** Le stesse slide documentano la reazione: divieto militare dei supporti USB rimovibili (2008) e limitazione progressiva di AutoRun da parte di Microsoft, motivata dalla diffusione di malware via USB e culminata nel caso **Stuxnet** `[S39–40]`. Il vettore specifico è quindi **collocato nel tempo**; la lezione generale — non inserire dispositivi non fidati — no.

---

# Caso 5 — Configurazioni predefinite

Il tema unificante: **la comodità iniziale è una scelta di sicurezza fatta da qualcun altro al posto tuo.**

| Domanda | Risposta |
| --- | --- |
| Che cosa protegge | Niente. È la categoria in cui la vulnerabilità è presente **al primo avvio**, prima di qualunque uso improprio. |
| Che cosa lo rompe | Servizi attivi per impostazione predefinita e credenziali predefinite condivise. |
| Che cosa resta dopo | Cambiare la password non elimina la vulnerabilità del servizio; disattivare il servizio non lo corregge. Riducono la finestra, non il difetto. |

**Eee PC 701** (L509, S45). Distribuzione Xandros con Samba attivo per impostazione predefinita, in versione vulnerabile a un modulo standard di Metasploit: root con sforzo minimo, appena estratto dalla scatola. Il ragionamento del libro va imparato per intero, perché è la parte trasferibile: *se Samba fosse stato disattivato per default, o se la configurazione avesse richiesto all'utente di abilitarlo, **la vulnerabilità sarebbe comunque esistita**, ma la superficie di attacco sarebbe stata molto ridotta in attesa di una correzione.* Ridurre la superficie di attacco e correggere un difetto sono due azioni distinte, con tempi distinti.

**Router e credenziali condivise** (L510). Il caso peggiore non è la password debole: è la **stessa password amministrativa su un'intera linea di prodotto**. Da qui il libro deriva una classe di attacchi per concatenazione: una richiesta forgiata attraverso il browser della vittima consente di autenticarsi al router e modificarne le impostazioni, per esempio dirottando il DNS verso un server controllato. È l'unico punto del capitolo in cui un default insicuro diventa un attacco **remoto** al client, e va ricordato come schema: *credenziale nota + fiducia del browser nella rete locale → riconfigurazione dell'infrastruttura.*

**ATM Triton** (L510). Tutti gli sportelli spediti con lo stesso codice amministrativo: chi lo conosce può stampare il registro delle transazioni o eseguire altre funzioni amministrative. L'impatto notevole è di **riservatezza**: il registro esponeva numeri di conto e nomi dei clienti. Un default insicuro non produce solo perdita di controllo, ma anche esposizione di dati personali di terzi.

**Bluetooth** (L510). Il difetto che il libro descrive è preciso: alcuni telefoni sono ancora **spediti con la modalità di rilevabilità attiva**, il che consente a chiunque di individuarli e tentare una connessione. La slide S49 afferma invece che la cifratura è disattivata per impostazione predefinita e che il PIN è `0000` `[solo slide]`: è un'affermazione assente dal libro, formulata come regola generale e verosimilmente legata all'esempio degli auricolari mostrato nell'immagine. **Non trattarla come proprietà del protocollo.**

---

# Caso 6 — Reverse engineering hardware

Qui lo schema a tre domande si applica in modo diverso: non c'è un singolo meccanismo di protezione da rompere, ma **una scala di livelli**, ciascuno con la propria domanda difensiva. È metà del capitolo (L511–526) e va studiata come progressione, dall'esterno verso l'interno.

## Livello 1 — Mappare il dispositivo

Aprire il contenitore, identificare i circuiti integrati, ricostruire i collegamenti. Il punto concettuale: **la maggior parte dei dispositivi è costruita con componenti commerciali documentati pubblicamente**. Il numero di modello stampato su un chip porta al datasheet, e il datasheet contiene pinout, funzioni e caratteristiche operative (L512). L'oscurità del progetto non è una protezione, perché il progetto è per lo più assemblaggio di parti note.

Strumenti concettualmente distinti: rimozione dei rivestimenti protettivi (resine, coating); **imaging a raggi X**, che il libro segnala come via **non distruttiva** per guardare sotto i rivestimenti (L512); multimetro con funzione di continuità per ricostruire la mappa dei collegamenti su schede multistrato (L514).

**Interfacce esterne = vettori** (L513): periferiche standard, rete, seriale, HDMI, USB, wireless, **e i test point di un JTAG**. Il libro aggiunge il dettaglio operativamente rilevante per un difensore: alcuni test point sono **nascosti sotto un pannello o un adesivo**. Nascondere non è disabilitare.

## Livello 2 — Bus fra componenti

| Domanda | Risposta |
| --- | --- |
| Che cosa protegge | Di norma niente: "una rete potrebbe essere considerata un bus multicomputer" (L515), e il traffico su un bus hardware è **generalmente non protetto**. |
| Che cosa lo rompe | Se i dati passano in chiaro fra due chip, sono soggetti a intercettazione, replay e man-in-the-middle — esattamente come su una rete. |
| Che cosa resta dopo | L'eccezione citata sono i sistemi DRM (HDMI-HDCP), che **cifrano da chip a chip**: dimostrazione che il problema è risolvibile per progetto, quando c'è un incentivo commerciale a risolverlo. |

Un analizzatore logico registra i segnali; alcuni modelli hanno decodificatori integrati per I²C, SPI e seriale (L517). Il libro segnala anche il **fuzzing dell'hardware**: inviare ai pin segnali arbitrari o malformati per provocare un guasto, "nello stesso modo in cui si fa il fuzzing applicativo e di protocollo" — con la conseguenza possibile di rendere il dispositivo inservibile (L518). È l'unico ponte esplicito del capitolo fra sicurezza software e hardware.

## Livello 3 — Interfaccia radio

Il concetto da portare via è **l'FCC ID** (L518, S55–56): ogni dispositivo che trasmette in radiofrequenza negli Stati Uniti deve averne uno, stampato sul dispositivo, sulla confezione o nel manuale. Da quel codice si accede a documentazione pubblica con le frequenze operative e i diagrammi interni. *La documentazione regolatoria obbligatoria è una fonte di informazione tecnica sul prodotto* — e non è aggirabile, perché è un obbligo di legge.

Il limite, che le slide non riportano: il *symbol decoding* è **il livello più basso** della decodifica wireless, analogo alla lettura di un bus fisico. Arrivarci non significa aver capito il protocollo: sopra restano i livelli superiori, e il libro avverte che serve comunque una quantità significativa di programmazione (L518).

## Livello 4 — Firmware

| Domanda | Risposta |
| --- | --- |
| Che cosa protegge | Nel caso studiato, niente: l'immagine non aveva "packing, encoding o encryption" (L521). Quando queste protezioni ci sono, la difficoltà va dal banale all'estremo. |
| Che cosa lo rompe | Il firmware è **aggiornabile sul campo** e spesso scaricabile dal sito del produttore o ottenibile su richiesta (L518). Spesso non serve possedere il dispositivo per analizzarne il software. |
| Che cosa resta dopo | Le protezioni di lettura/scrittura del componente (livello 5) alzano il costo, ma vanno abilitate consapevolmente in fase di progetto. |

**Che cosa si cerca in un'immagine firmware** (L518, S57): password predefinite, porte amministrative, interfacce di diagnostica, codice di sviluppo dimenticato.

**Il reversing di firmware è diverso dal reversing ordinario** (L518–519): l'immagine è caricata direttamente dal microcontrollore e l'esecuzione parte da un **indirizzo fisso**, senza loader né metadati di formato. L'entry point si ricava dal datasheet del microcontrollore, non dal file.

> [!warning] Segreti nel firmware
> Nell'esempio del libro l'analisi trova chiavi e certificati (`ca.pem`, `clientca.pem`, `priv.pem`) e la conclusione è esplicita: si può **impersonare un dispositivo fidato** sulla rete privata (L521). La lezione trasferibile: una chiave privata inclusa in un'immagine firmware non è il segreto di *un* dispositivo, è un segreto **condiviso da tutti gli esemplari del prodotto**. Comprometterne uno li compromette tutti, e la revoca è un problema di aggiornamento del parco installato.

**Backdoor** (L521–522). La forma tipica non è codice esotico ma un **secondo controllo nascosto dopo quello legittimo**: nell'esempio del dispositivo medicale, terminate le verifiche normali sul numero di serie, un ulteriore confronto su un valore fisso concede il pieno controllo. È un anti-pattern riconoscibile in revisione del codice. Il libro le definisce "(hopefully) unintentional" e le colloca in luoghi ricorrenti: interfacce fisiche nascoste, interfacce di debug, porte diagnostiche e seriali, codice di sviluppo non rimosso. La distinzione **backdoor intenzionale / residuo di sviluppo** conta per la responsabilità, non per l'impatto.

## Livello 5 — Protezioni del componente e debug

**Le protezioni esistono e sono una scelta di progetto** (L523): alcuni chip bloccano la lettura del firmware finché non si esegue una cancellazione, oppure vietano scritture successive alla prima. Il datasheet è dove si verifica se il componente le offre. È l'unica **contromisura di progetto** dell'intera sezione di reverse engineering, ed è il punto da ricordare dal lato difensivo. Il libro nota che aggirarle richiederebbe strumentazione molto costosa (FIB, microposizionatori, microscopi a effetto tunnel), fuori dallo scopo del testo.

Attenzione a una tensione interna al libro: a L513 dice che EEPROM e molti microcontrollori sono leggibili con un programmatore comune e "generalmente non hanno una sicurezza forte"; a L523 dice che alcuni chip hanno protezioni di lettura e scrittura. Entrambe sono vere — **la protezione esiste come opzione e spesso non viene attivata**.

**ICE e JTAG** (L523–526):

- **ICE** (in-circuit emulator): "emulatore" è un termine improprio — l'hardware non viene quasi più emulato; l'ICE **fa il lavoro di un debugger**, offrendo una finestra sul funzionamento del dispositivo. Serve perché i sistemi embedded non hanno tastiera e schermo.
- **JTAG**: nato per **verificare che i collegamenti fra componenti fossero assemblati correttamente dopo la produzione**. È un'interfaccia di collaudo che finisce nei prodotti spediti, e da lì consente di inviare e ricevere segnali verso i singoli integrati. Non è standardizzata nella forma fisica: "one size does not fit all" — numero di pin e disposizione variano.

> [!warning] Asimmetria delle fonti
> Per le interfacce di debug esposte le fonti descrivono l'accesso ma **non propongono contromisure**. La copertura del capitolo non è simmetrica, e questa è una lacuna delle fonti, non della nota: annotarlo evita di concludere che una contromisura non esista.

---

# Principi trasversali

Sono le affermazioni che sopravvivono ai singoli casi e alle loro date.

1. **L'accesso fisico precede tutto il resto.** Controlli fisici ed endpoint sono incontrati dall'attaccante molto prima di un punto di accesso di rete o di un prompt di login (L498). Il capitolo si chiude sulla stessa idea: l'hardware è "the ultimate protector" di riservatezza, integrità e disponibilità (L526).
2. **Codifica ≠ checksum ≠ crittografia.** Tre funzioni distinte, confuse di continuo. Solo la terza resiste a un avversario. → Caso 2a.
3. **Impedire l'accesso ≠ proteggere il contenuto.** → Caso 3.
4. **La fiducia non verificata fra componenti è un difetto architetturale.** BIOS/disco, lettore/carta, host/dispositivo USB: tre istanze dello stesso schema.
5. **La comodità predefinita è superficie di attacco.** AutoRun, servizi attivi al primo avvio, credenziali condivise, rilevabilità Bluetooth. → Casi 4 e 5.
6. **Ridurre la superficie di attacco ≠ correggere la vulnerabilità.** Il ragionamento su Samba (L509) è il modello.
7. **Ogni contromisura ha un ambito, e va enunciato con essa.** Disattivare AutoRun non neutralizza ogni dispositivo USB malevolo; la cifratura del disco non rende irrilevanti le altre condizioni (cold boot). Dire cosa *non* copre una difesa fa parte del saperla.
8. **Il nome non è la proprietà.** "RFID", "password", "cifrato", "JTAG" non descrivono da soli né una vulnerabilità né una protezione. Vale in particolare per la crittografia proprietaria.
9. **Il fattore umano scavalca la tecnologia delle credenziali.** → Il tailgating, caso 2.
10. **La documentazione pubblica è parte della superficie informativa.** Datasheet dei componenti, archivi FCC: informazione tecnica ottenibile senza toccare il dispositivo.

---

# Cautele delle fonti

Il libro accompagna quasi ogni tecnica con un avvertimento. Sono contenuto del capitolo, non contorno.

- **Legale**: possedere o portare con sé bump key può essere illecito a seconda della giurisdizione (L500).
- **Integrità delle prove e dei supporti**: scrivere su una carta magnetica può corromperla in modo permanente; usare solo supporti sacrificabili (L502).
- **Danno all'hardware**: manipolare dischi sotto tensione può danneggiare unità, file system, macchina o operatore (L505–506); la funzione di continuità di un multimetro può distruggere componenti sensibili (L515); il fuzzing dei pin può rendere il dispositivo inservibile (L518).
- **Rischio per chi opera**: un dispositivo U3 preparato non distingue le macchine e compromette **qualunque** sistema in cui viene inserito, incluso il proprio (L509).
- **Sicurezza personale**: la rimozione delle resine con acido nitrico è raccomandata solo a chi conosce le procedure di manipolazione (L511–512).

---

# Glossario minimo

Solo i termini necessari ai meccanismi sopra. L'inventario completo dei nomi citati sta nell'audit.

| Termine | Definizione essenziale |
| --- | --- |
| **Clonazione** | Riproduzione dei dati o del comportamento di una credenziale, in modo che il lettore non distingua la copia dall'originale. |
| **Replay** | Riutilizzo di una comunicazione precedentemente acquisita per ottenere di nuovo lo stesso effetto. |
| **Challenge-response** | Autenticazione in cui il verificatore invia una sfida variabile e la risposta dipende dalla sfida **e** da un segreto che non transita. Contrasta il replay. |
| **Checksum** | Valore di controllo per rilevare errori o danneggiamenti dei dati. Ricalcolabile: non è una protezione contro un avversario. |
| **Full disk encryption** | Cifratura del contenuto del volume, distinta dal controllo di accesso al disco. |
| **Superficie di attacco** | Insieme delle funzionalità e interfacce esposte attraverso cui un sistema può essere attaccato. Si riduce disattivando ciò che non serve; è indipendente dalla presenza di una vulnerabilità. |
| **Firmware** | Codice che governa il funzionamento di un dispositivo; aggiornabile sul campo, spesso distribuito pubblicamente. |
| **Datasheet / pinout** | Scheda tecnica di un componente; disposizione e funzione dei suoi terminali. Fonte primaria per capire un sistema embedded. |
| **Bus** | Canale di comunicazione fra componenti hardware. Concettualmente assimilabile a una rete, e per default altrettanto poco protetto. |
| **SDR** | Radio in cui l'elaborazione del segnale è svolta dal software, il che consente di adattarla a protocolli diversi. |
| **Backdoor** | Percorso che aggira i controlli ordinari; nella forma tipica, un secondo controllo nascosto dopo quello legittimo. Spesso residuo di sviluppo. |
| **ICE** | Dispositivo che fornisce una finestra di debug sull'hardware in funzione. "Emulatore" è termine improprio. |
| **JTAG** | Interfaccia nata per il collaudo dei collegamenti dopo la produzione, riutilizzata per il debug embedded — e disponibile a chi apre il dispositivo. |

---

# Domande di ripasso

**1. Perché la sicurezza fisica appartiene alla sicurezza delle informazioni?**

<details><summary>Mostra risposta</summary>

L'accesso fisico si incontra prima di qualunque controllo di rete o applicativo, e chi lo ottiene può aggirare i livelli logici invece di attaccarli. Il capitolo apre e chiude su questa idea: i dispositivi hardware sono il protettore ultimo di riservatezza, integrità e disponibilità. — L498, L526

</details>

**2. Distingui codifica, checksum e protezione crittografica nel caso delle carte.**

<details><summary>Mostra risposta</summary>

La codifica rappresenta i dati e può essere in formato proprietario: richiede decodifica, non è protezione. Il checksum rileva errori o danneggiamenti del supporto ed è ricalcolabile da chi modifica i dati — e a volte non viene nemmeno verificato dal lettore. Solo la protezione crittografica, presente in parte nei sistemi RFID recenti, resiste a un avversario. — L500–502, L504

</details>

**3. Perché il challenge-response contrasta il replay?**

<details><summary>Mostra risposta</summary>

Perché la risposta dipende dalla sfida ricevuta, che cambia a ogni transazione, e da un segreto che non viene trasmesso. Una conversazione registrata contiene la risposta a una sfida ormai passata e non serve per la successiva. Le proprietà effettive dipendono però dallo schema implementato: la crittografia proprietaria è il punto debole ricorrente. — L504

</details>

**4. Perché una password ATA non sostituisce la cifratura del disco?**

<details><summary>Mostra risposta</summary>

Controlla l'accesso al disco senza cifrarne il contenuto: estratto dal sistema, il disco contiene dati in chiaro. Il difetto sottostante è di fiducia — l'unità presume che l'autenticazione sia già avvenuta nel BIOS, cioè in un componente controllato da chi ha la macchina in mano. La contromisura è la cifratura del volume, che a sua volta ha un limite (cold boot). — L505–507

</details>

**5. Da quale condizione dipende il caso U3, e perché la sua contromisura non risolve ogni rischio USB?**

<details><summary>Mostra risposta</summary>

Da due condizioni congiunte: il supporto si presenta al sistema anche come unità CD, e l'host ha AutoRun attivo su quel tipo di supporto. Il difetto sta nella funzione dell'host, non nel dispositivo. Disattivare AutoRun interrompe questo meccanismo, ma il libro avverte esplicitamente che un dispositivo malevolo può usarne altri: la contromisura è specifica del vettore, non della categoria. — L507–509, S31

</details>

**6. Quale lezione offre il caso Eee PC sulle configurazioni iniziali?**

<details><summary>Mostra risposta</summary>

Che un servizio vulnerabile attivo per impostazione predefinita espone il dispositivo dal primo avvio. Il ragionamento del libro è la parte da ricordare: disattivare il servizio per default non avrebbe eliminato la vulnerabilità, ma avrebbe ridotto molto la superficie di attacco in attesa della correzione. Ridurre l'esposizione e correggere il difetto sono azioni distinte. — L509

</details>

**7. Perché una credenziale predefinita condivisa su una linea di prodotto è un problema diverso da una password debole?**

<details><summary>Mostra risposta</summary>

Perché non richiede di indovinare nulla: il valore è noto e vale per tutti gli esemplari, quindi il costo dell'attacco non cresce col numero di bersagli. Il libro ne deriva due conseguenze: la concatenazione di vulnerabilità sui router (autenticazione attraverso il browser della vittima e dirottamento del DNS) e il caso Triton, dove il codice comune esponeva anche dati personali dei clienti nei registri. — L510

</details>

**8. Perché una chiave privata trovata in un'immagine firmware ha un impatto diverso da una password trovata nella stessa immagine?**

<details><summary>Mostra risposta</summary>

Perché non è il segreto di un singolo dispositivo ma di tutti gli esemplari che condividono quell'immagine, e consente di impersonare un dispositivo fidato invece di accedere a un account. Sostituire una password è un'operazione locale; revocare una chiave distribuita nel firmware è un problema di aggiornamento dell'intero parco installato. — L521

</details>

**9. In che cosa differiscono analizzatore logico, analisi del firmware e ICE/JTAG?**

<details><summary>Mostra risposta</summary>

Osservano cose diverse: l'analizzatore logico registra i segnali che transitano su un bus fra componenti; l'analisi del firmware esamina codice e dati a riposo, spesso ottenuti senza il dispositivo; ICE e JTAG danno visibilità e controllo sul dispositivo **in funzione**. Sono prospettive complementari, con compatibilità e accessibilità che variano da prodotto a prodotto. — L515–526

</details>

**10. Cita due esempi in cui le slide non vanno generalizzate oltre il libro.**

<details><summary>Mostra risposta</summary>

Bluetooth: S49 afferma che la cifratura è disattivata per default e il PIN è `0000`; il libro parla invece della modalità di rilevabilità attiva su alcuni telefoni. Bumping: S5 dice che non lascia alcuna traccia, il libro dice che raramente ne lascia. Un terzo esempio: S13 sostiene che l'RFID è "ora richiesto nei passaporti", affermazione assente dal libro e dipendente dalla giurisdizione. — L499, L510 vs S5, S13, S49

</details>

---

Fonti, attribuzione puntuale e stato di aggiornamento dei contenuti: **[[Hacking_Exposed_7_Cap9_Audit_fonti]]**.
