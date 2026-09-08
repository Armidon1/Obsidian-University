---
title: "Hacking Exposed 7 — Cap. 9 — Audit fonti"
tags: [cybersecurity, hacking-exposed, capitolo-9, audit-fonti, metodo]
source: ["Libro", "Slide del docente"]
status: in-revisione
ultima-verifica: 2026-09-08
companion: "[[Hacking_Exposed_7_Cap9_Nota_di_studio]]"
---

# Scopo

Questa nota **non si studia**. Serve a rispondere a una domanda sola: *data un'affermazione sul capitolo 9, da dove viene e quanto posso fidarmi?*

Per studiare il capitolo: **[[Hacking_Exposed_7_Cap9_Nota_di_studio]]**.

> [!note] Come leggere l'attribuzione
> Il **libro** è la fonte tecnica primaria; le **slide** indicano le priorità didattiche e aggiungono materiale non presente nel testo. "Entrambe" significa che un contenuto compare in due documenti, **non** che abbia due conferme indipendenti: le slide derivano dal libro.

**Notazione.** `L###` = pagina stampata del libro. `S##` = pagina PDF delle slide. `E` = entrambe le fonti.

**Fonti.**

- **Libro:** `BOOK eth ch9.pdf` — capitolo 9, *Hacking Hardware*, da *Hacking Exposed 7: Network Security Secrets & Solutions*. Pagine stampate **497–526** = pagine PDF **1–30**. Relazione: **pagina PDF = pagina stampata − 496**.
- **Slide:** `9 - SLIDE Hacking_Exposed_7_ch9.pdf` — **60 pagine PDF**. "S##" indica la pagina PDF, comprese schermate e pagine di solo titolo.

Nessuna fonte esterna è stata consultata. Le schermate bibliografiche visibili nelle slide sono trattate come **contenuto delle slide**, non come documenti letti.

---

# 1. Corrispondenza fra le fonti

| Argomento | Libro | Slide |
| --- | --- | --- |
| Introduzione e struttura | 498, 526 | 1–2 |
| Serrature e accesso fisico | 498–500 | 3–7 |
| Carte magnetiche | 500–503 | 8–12 |
| RFID e contromisure | 503–504 | 13–19 |
| *(divisorio "Hacking Devices")* | — | 20 |
| Dischi e password ATA | 505–507 | 21–27 |
| USB / U3 | 507–509 | 28–43 |
| Configurazioni predefinite e Bluetooth | 509–511 | 44–51 |
| Componenti, bus e interfacce radio | 511–518 | 52–56 |
| Firmware, programmatori e debug | 518–526 | 57–58 |
| Esercizi del docente | *assenti dal capitolo* | 59–60 |

Pagine di solo titolo nelle slide: **20, 28, 32, 35, 38, 44, 52**.

---

# 2. Divergenze fra libro e slide

Le più rilevanti per il ripasso: dove le due fonti dicono cose diverse sullo stesso punto.

| Punto | Libro | Slide | Come trattarlo |
| --- | --- | --- | --- |
| **Tracce del bumping** | "seldom leave evidence of tampering" — raramente lascia tracce (L499) | "Bumping leaves no evidence behind" — nessuna traccia (S5) | La slide assolutizza. Sul **danno** invece la slide qualifica correttamente ("unless done many times, or clumsily"), in linea con la CAUTION del libro (L500): la divergenza riguarda **solo le tracce**. |
| **Contromisure alle serrature** | Elenco di controlli fisici compensativi: più dispositivi di chiusura, videosorveglianza, guardie, allarmi (L500) | Riformulati come *"two-factor authentication"* (S7) | Prestito lessicale dall'autenticazione informatica, assente dal libro. Utile come mnemonico, non citabile come terminologia del testo. |
| **Dati sulle carte magnetiche** | Dati codificati **in chiaro**, spesso in formato personalizzato da decodificare (L500–502) | "No security measures to protect data" + "Not clear encoding" (S12) | **Non è una contraddizione**: assenza di cifratura ≠ formato standard leggibile. Le due affermazioni descrivono aspetti diversi e vanno tenute insieme. |
| **Meccanismo U3** | "two separate devices are mounted: the U3 partition and the regular flash storage device" (L507) | "A Removable Disk" + **"a hidden CD drive named U3"**, ed è il CD che AutoRun esegue (S31) | Il dettaglio che **spiega** l'attacco è solo nelle slide. Da conservare, marcandolo come tale. |
| **Attacchi radio di livello 2** | Attacchi software di livello 2 possibili **se** è disponibile un dispositivo client; altrimenti serve ricognizione (L518) | "Layer 2 software attack, i.e. 802.11 Wi-Fi operates at the data link layer" (S55) | La slide trasforma un condizionale in una definizione. Il condizionale del libro è la formulazione corretta. |
| **Bluetooth** | Alcuni telefoni spediti con **modalità di rilevabilità attiva** per default (L510) | "Bluetooth supports encryption, but it's off by default, and the password is 0000 by default" (S49) | Affermazioni **diverse**, non equivalenti. Quella della slide è assente dal libro: vedi §3. |
| **Frequenze RFID** | 135 kHz o 13,56 MHz (L503) | 135 kHz o 13,56 MHz (S18), ma lo screenshot Wikipedia in S15 cita **125 kHz** / 13,56 MHz per lo stesso strumento | Incoerenza **interna alle fonti**. Da verificare prima di memorizzare la cifra: non fissare 135 kHz come dato certo. |
| **La cifra del 70%** | Due bump key aprono ~70% delle **serrature** su porte nordamericane (L500) | Medeco detiene ~70% del **mercato** delle serrature (screenshot S6) | Due statistiche **diverse** che si somigliano. Confonderle è l'errore più probabile del blocco. |
| **MIFARE, cronologia** | Richiamo sintetico all'attacco al sistema MIFARE (L504) | Cronologia articolata negli screenshot: CCC dicembre **2007** (reverse engineering parziale), Radboud marzo **2008** (completo), USENIX agosto 2008, articolo ACM **2015** (S15–16) | Le slide aggiungono profondità storica. La differenza 2007/2008 è quella fra reverse engineering parziale e completo. La schermata bibliografica **non è** il testo dell'articolo. |
| **Ambito della funzione ATA** | Non quantificato | "Virtually every hard drive made since 2000 has this feature" (S22) | Affermazione solo delle slide: vedi §3 e §5. |

---

# 3. Affermazioni presenti in una sola fonte

## 3a. Solo nelle slide

Da marcare sempre come tali: non hanno il supporto del testo.

| Affermazione | Rif. | Nota |
| --- | --- | --- |
| RFID "now required in passports" | S13 | Assente dal libro. Generalizzazione assoluta, dipendente dalla giurisdizione e dal tipo di documento. |
| Dati RFID "read at a distance, and is usually unencrypted" | S13 | Il libro dice che **molte** carte sono non protette e che sempre più impiegano crittografia (L503): formulazione più cauta. |
| "Virtually every hard drive made since 2000" ha la funzione ATA security | S22 | Non nel libro. Le fonti non trattano interfacce e meccanismi di protezione successivi a PATA/SATA. |
| Confronto PATA/IDE vs SATA | S21 | Contesto aggiunto dal docente, non nel capitolo. |
| Scenario di blocco del disco a scopo di riscatto tramite ATA security | S23 | Marcato dalla slide stessa come "only a theoretical attack **at the moment**". Conservare il qualificatore temporale, non trasferirlo al presente. |
| Vogon Password Cracker POD e *drive service area* | S25–26 | Assente dal libro. Il concetto di area del disco riservata e non accessibile all'utente è però solido e utile. |
| U3 si presenta come **unità CD nascosta** | S31 | È il dettaglio che spiega l'intervento di AutoRun. Vedi §2. |
| PocketKnife | S32–37 | Assente dal libro, che cita solo Universal_Customizer e i pacchetti Switchblade. |
| Blocco dei dispositivi USB via Group Policy; sigillatura fisica delle porte | S41 | Contromisure aggiunte dal docente. |
| IEEE 1667, implementato in Windows 7 | S42 | Assente dal libro. È l'unica contromisura **strutturale** del blocco USB. |
| Caso ATM 2008 (erogazione di banconote errate) e foto LayerOne | S47–48 | Episodi diversi dal caso Triton del libro: **non fonderli**. |
| Cifratura Bluetooth disattivata per default e PIN `0000` | S49 | Assente dal libro. Formulata come regola generale, verosimilmente legata all'esempio degli auricolari nell'immagine. |
| CRYPTO1, DES, KwickBreak, piattaforma FPGA Opal Kelly | S17 | Dettagli del caso Boston, assenti dal libro. |
| Esercizi (ROM 60 pt, editor esadecimale 20 pt, confronto PS3/PS4 20 pt) | S59–60 | Il confronto PS3/PS4 **non è svolto** nel capitolo allegato. |

## 3b. Solo nel libro

Contenuto tecnico che le slide non riportano: è dove la nota di studio ha dovuto attingere direttamente al testo.

| Contenuto | Rif. |
| --- | --- |
| Cifra del 70% delle serrature apribili con due bump key | L500 |
| Lucchetti a cavo (Kensington) aperti in meno di due minuti | L500 |
| Numeri degli standard ISO 7810, 7811, 7813 | L500 |
| Checksum a volte presente sulla carta ma **non verificato dal lettore** | L502 |
| "Magstripe systems are being deprecated in favor of RFID" | L503 |
| Caso HID / Chris Paget 2007 e lettera al datore di lavoro | L503 |
| OpenPICC come dispositivo di clonazione (distinto da OpenPCD lettore) | L503 |
| **Tailgating** come via più efficace di ingresso | L504 |
| Meccanismo del disallineamento di fiducia BIOS ↔ disco | L505 |
| Rimando al *cold boot* (Cap. 4) come limite della cifratura | L507 |
| Concatenazione di vulnerabilità sui router e dirottamento DNS | L510 |
| Caso Triton: codice amministrativo comune, registri con dati dei clienti | L510 |
| Phenoelit Default Password List | L509–510 |
| Imaging a raggi X come ispezione non distruttiva | L512 |
| Difficoltà di debug degli FPGA per mancanza di visibilità interna | L513 |
| Test point nascosti sotto pannelli o adesivi | L513 |
| Fuzzing dei pin hardware | L518 |
| Firmware ottenibile dal sito del produttore o su richiesta | L518 |
| Entry point a indirizzo fisso, ricavato dal datasheet | L518–519 |
| Chiavi e certificati nell'immagine (`priv.pem`) → impersonare un dispositivo fidato | L521 |
| Esempi di backdoor: Intel NetStructure, Palm OS Debug Mode, Sega Dreamcast | L521 |
| Backdoor del dispositivo medicale: secondo controllo nascosto sul numero di serie | L521–522 |
| Protezioni di lettura/scrittura dei chip; FIB, microposizionatori, microscopi a effetto tunnel | L523 |
| "Emulatore" come termine improprio per ICE | L523 |
| OpenOCD (per processori ARM), UrJTAG, integrazione Eclipse | L526 |
| Tutte le CAUTION legali e di sicurezza personale | L500, L502, L505–506, L509, L511–512, L515 |

---

# 4. Refusi e incoerenze testuali

| Punto | Evidenza | Valutazione |
| --- | --- | --- |
| **HDMI-HSCP** | Il libro stampa "HDMI-HSCP" (L515); la slide scrive "HDMI-HDCP" ed espande *High-bandwidth Digital Content Protection* (S54) | Refuso del libro. La forma della slide è quella coerente con l'espansione dell'acronimo. |
| **`autorun.ini` / `autorun.inf`** | L507 e S43 scrivono `autorun.ini`; L508 mostra l'esempio con estensione `.inf` | L'esempio concreto del libro usa `.inf`; le due occorrenze in prosa con `.ini` sono probabili refusi. Da non memorizzare in entrambe le forme. |
| **"cross-site response forgery"** | L510 | Quasi certamente refuso per *cross-site **request** forgery* (CSRF). Il meccanismo descritto — richiesta forgiata attraverso il browser autenticato della vittima — è quello del CSRF. |
| **"Hak9's PocketKnife"** | Titolo di S32; il libro cita `hak5.org` e `wiki.hak5.org` (L508–509) | Probabile refuso della slide per **Hak5**. |
| **135 kHz vs 125 kHz** | L503 e S18 vs screenshot S15 | Incoerenza fra le fonti, non risolvibile internamente. Vedi §2. |
| **80 canali Bluetooth** | L510, S51 | Dato da verificare in fonte primaria: la letteratura Bluetooth cita comunemente 79 canali per BR/EDR. |
| **Numerazione dei pin nella figura** | La figura 9-13 numera i pin da 0 a 21 (L514) | Convenzione insolita: gli integrati reali numerano i pin a partire da 1. Figura didattica, non riferimento. |
| **Terminologia challenge-response** | "encrypted and signed by the **private key** stored on the card" (L504, ripreso in S19) | Lessico asimmetrico applicato a un contesto (carte di accesso economiche) che suggerisce chiavi simmetriche. Il tipo di chiave non è specificato dalle fonti: non generalizzare. |

---

# 5. Contenuti datati o da verificare

> [!warning] Materiale storico
> Questa nota usa esclusivamente i due allegati. Date, prezzi, disponibilità, supporto dei prodotti e impostazioni predefinite restano riferiti ai materiali. Espressioni come "ora", "recentemente", "al momento" non descrivono il presente.

| Punto | Stato nelle fonti | Come trattarlo |
| --- | --- | --- |
| **TrueCrypt** | Elencato fra i prodotti di cifratura del disco (L506, S27) | **Il rischio più concreto della nota originale.** Lasciarlo in un elenco senza marcatura invita a leggerlo come raccomandazione. Verificare lo stato del progetto prima di qualunque uso come tale. |
| **BitLocker, SecurStar** | Stessa riga (L506, S27) | Elenco d'epoca. Da verificare separatamente, non da citare come panorama attuale. |
| **Proxmark3** | Il libro afferma che va assemblato dall'utente e che **"is no longer supported by the maker"** (L504) | Affermazione datata e potenzialmente fuorviante sullo stato del progetto. Non riportarla come descrizione attuale. |
| **Piattaforma U3** | Trattata come attuale in tutto il blocco (L507–509, S28–43) | **Caso storico.** Marcarlo fin dall'inizio del blocco, non solo in coda. |
| **AutoRun** | Le fonti stesse ne documentano la limitazione progressiva: aggiornamento Microsoft del 2011 (S39), IEEE 1667 in Windows 7 (S42) | Il vettore specifico è **storicamente collocato**; la lezione generale sui dispositivi USB non fidati (L509) no. |
| **Difese USB, cronologia** | Notizie del 2008 (S40) e 2011 (S39); IEEE 1667 riferito a Windows 7 (S42) | Non assumerne validità attuale. Stuxnet compare in S39 come caso culminante che motiva la reazione. |
| **Eee PC 701 / Xandros** | L509, S45 | Dispositivo e distribuzione fuori produzione. Il **ragionamento** sulla superficie di attacco resta valido e trasferibile. |
| **Phenoelit Default Password List** | L509–510; screenshot datato **2008-03-14** in S46 | Risorsa d'epoca. |
| **Vogon Password Cracker POD** | S25–26 | Prodotto storico; lo screenshot mostra un sito non cifrato ("Non sicuro" nella barra del browser). |
| **Prezzi** | Lettore magstripe ~$35 (S10); USRP ~$1.000 (L504); Ubertooth $120 (L510); programmatori EEPROM $200–$1.200 (L522); kit Thermo-Bond ~$300 (L516) | Tutti d'epoca. Utili solo come **ordini di grandezza relativi**. |
| **"Magstripe deprecato in favore di RFID"** | L503 | Affermazione **direzionale** del libro, cioè una previsione. Da registrare come tale. |
| **MIFARE Classic "most widely deployed"** | S14, e l'abstract del 2015 in S16 | Affermazione di mercato d'epoca. |
| **Frequenze e canali** | 135 kHz (L503, S18); 80 canali Bluetooth (L510, S51) | Vedi §4: entrambi da verificare. |
| **IEEE 1667 / Windows 7** | S42 | Ambito di implementazione riferito a una versione specifica. |

---

# 6. Inventario di tool e tecnologie

Nomi citati nel capitolo, come **oggetti di studio**: nessuna istruzione d'uso, nessuna raccomandazione. Classificazione rivista rispetto alla nota originale dove era imprecisa.

## Accesso fisico

| Nome | Categoria | Funzione nel capitolo | Fonte |
| --- | --- | --- | --- |
| Medeco | Serrature | Protezione con sidebar e pin angolati; il libro segnala che modelli più vecchi sono stati aperti da ricerca pubblica | E — L500; S6–7 |
| Assa Abloy | Serrature | Citata accanto a Medeco fra i produttori resistenti a bumping e picking | L500 |
| Kensington | Lucchetti a cavo per laptop | Esempio di bypass banale con oggetti comuni | L500 |

## Carte di accesso

| Nome | Categoria | Funzione nel capitolo | Fonte |
| --- | --- | --- | --- |
| Magstripe | Tecnologia | Carte a banda magnetica, tre tracce | E — L500–502; S8–12 |
| ISO 7810 / 7811 / 7813 | Standard | Dimensioni della carta e struttura delle tracce | L500 |
| Lettore/scrittore magstripe | Tool hardware | Lettura e scrittura dei dati di traccia | E — L500; S10 |
| Magnetic-Stripe Card Explorer | Software | Visualizzazione e manipolazione dei dati delle tracce | E — L501–503; S11–12 |
| RFID | Tecnologia | Identificazione a radiofrequenza; "proximity cards" | E — L503; S8, S13 |
| HID | Famiglia di prodotti | Carta RFID più diffusa nel testo; protocollo proprietario | L503 |
| MIFARE Classic | Famiglia di prodotti | Caso di studio sulla crittografia proprietaria | E — L504; S14–17 |
| CRYPTO1 | Algoritmo | Cifrario proprietario di MIFARE Classic, citato negli screenshot | S16–17 |
| DES | Algoritmo | Citato nello schema dello strumento di brute-force | S17 |
| KwickBreak | **Strumento di brute-force su FPGA** | Attacco con plaintext noto per recuperare la chiave; GUI + generatore di codice + piattaforma FPGA (Opal Kelly XEM3001) | S17 |
| OpenPCD | Progetto hardware | **Lettore** RFID | E — L503; S18 |
| OpenPICC | Progetto hardware | **Dispositivo che imita la carta** | L503 |
| Proxmark3 | Tool hardware | Analisi di protocolli RFID diversi tramite FPGA integrata | E — L504; S18 |
| USRP | Piattaforma SDR | Intercettazione dei segnali radio grezzi, da decodificare per protocollo | E — L504, L518; S18, S55 |
| WinRadio | Piattaforma SDR | Alternativa citata per il symbol decoding | E — L518; S55 |

## Dischi

| Nome | Categoria | Funzione nel capitolo | Fonte |
| --- | --- | --- | --- |
| ATA | Standard / interfaccia | Include il meccanismo di password discusso; non specifico di una marca | E — L505–506; S21–24 |
| PATA/IDE, SATA | Interfacce | Confronto introduttivo | S21 |
| Vogon Password Cracker POD | Pod hardware forense | Integrato in un sistema di imaging; opera sulla *drive service area* (area riservata a firmware e geometria, non accessibile all'utente) | S25–26 |
| BitLocker, TrueCrypt, SecurStar | Prodotti di cifratura | Citati come alternativa alla password ATA — **vedi §5** | E — L506; S27 |

## USB

| Nome | Categoria | Funzione nel capitolo | Fonte |
| --- | --- | --- | --- |
| U3 | Piattaforma su chiavetta | Partizione secondaria su unità SanDisk e Memorex | E — L507; S28–31 |
| Launchpad | **Interfaccia applicativa del dispositivo** | Menu che compare all'inserimento | S30 |
| AutoRun | **Funzione del sistema operativo ospite** | **Dove risiede la condizione sfruttata** | E — L507; S31, S39, S43 |
| Universal_Customizer | Utility di personalizzazione | Scrive un'immagine ISO sulla partizione U3 | E — L508; S36–37 |
| fgdump | Strumento di estrazione di credenziali | Citato come payload d'esempio; rimandato al Cap. 4 | E — L507–509; S37 |
| PocketKnife | Suite di strumenti | Caso didattico di abuso delle funzionalità U3 | S32–34, S37 |
| Group Policy | Gestione delle policy | Restrizione dei dispositivi USB | S41 |
| IEEE 1667 | Standard | Autenticazione dei dispositivi di memorizzazione transitori | S42 |

## Configurazioni predefinite

| Nome | Categoria | Funzione nel capitolo | Fonte |
| --- | --- | --- | --- |
| Eee PC 701 | Dispositivo | Caso di servizio vulnerabile attivo al primo avvio | E — L509; S45 |
| Xandros | Distribuzione Linux | Sistema preinstallato sull'Eee PC | E — L509; S45 |
| Samba | Servizio di condivisione file | Attivo per default, in versione vulnerabile | E — L509; S45 |
| Metasploit | **Framework di exploitation** (usato anche in test autorizzati) | Modulo standard sufficiente a ottenere root | E — L509; S45 |
| Phenoelit Default Password List | Risorsa informativa | Raccolta di credenziali predefinite per produttore | E — L509–510; S46 |
| Triton ATM | Dispositivo | Codice amministrativo comune a tutti gli esemplari | L510 |
| Bluetooth | Protocollo | Rilevabilità attiva per default su alcuni telefoni | E — L510; S49, S51 |
| Ubertooth | Tool hardware radio | Sniffing e riproduzione di frame Bluetooth; analisi di spettro | E — L510–511; S50–51 |

## Reverse engineering

| Nome | Categoria | Funzione nel capitolo | Fonte |
| --- | --- | --- | --- |
| IC | **Categoria generale** | Circuito integrato | E — L512; S53 |
| MCU | Tipo di IC | Microcontrollore: processore, poca memoria, memoria non volatile | L513 |
| EEPROM | Tipo di IC | Memoria non volatile; leggibile con programmatore comune, "generally does not have strong security" | L513 |
| FPGA | Tipo di IC | Logica riconfigurabile; debug difficile per mancanza di visibilità interna | E — L513; S18 |
| VHDL, Verilog | Linguaggi HDL | Descrizione della logica programmabile | L513 |
| Altera, Xilinx | Fornitori FPGA | Citati come produttori diffusi | L513 |
| Datasheet, pinout | Documentazione | Fonte primaria per capire un componente | E — L512–514; S53 |
| Newark, DigiKey | Cataloghi di componenti | **Canali di reperimento dei datasheet** | L512 |
| MG Chemicals 8310, Dremel, acido nitrico | **Rimozione di rivestimenti protettivi** | Accesso agli integrati sotto resine e coating | L511–512 |
| Imaging a raggi X | **Ispezione non distruttiva** | Alternativa alla rimozione fisica | L512 |
| ChipQuik | **Rimozione di componenti a montaggio superficiale** | Lega per dissaldatura | L512 |
| Thermo-Bond Cir-Kit (Pace) | **Riparazione delle piste del PCB** | Kit per portare fuori i contatti, ~$300 | L516 |
| Multimetro | Tool di misura | Funzione di continuità per mappare i collegamenti | E — L514; S53 |
| Analizzatore logico | Tool di misura | Registrazione dei segnali sul bus; decodificatori integrati | E — L515–517; S54 |
| I²C, SPI, seriale | Bus e interfacce | Protocolli di comunicazione fra componenti | E — L517; S54 |
| HDMI, HDCP, DRM | Interfaccia; protezione; categoria | Esempio di comunicazione **cifrata** da chip a chip | E — L513, L515; S53–54 — *refuso, vedi §4* |
| FCC ID | Identificativo regolatorio | Accesso a documentazione pubblica: frequenze e diagrammi interni | E — L518; S55–56 |
| SDR | Approccio radio | Elaborazione del segnale via software | E — L518; S55 |
| 010 Editor | Editor esadecimale | Ispezione dell'immagine firmware | E — L518; S57 |
| IDA Pro | Disassemblatore | Reversing del firmware; oltre 50 famiglie di processori | E — L518; S57 |
| strings | Utility Unix | Estrazione delle stringhe ASCII da un binario | E — L519; S57 |
| AES | Algoritmo | **Ipotizzato** dalle stringhe visibili nell'immagine, non dimostrato | E — L518; S57 |
| cramfs | Filesystem | Filesystem del firmware nell'esempio | L520 |
| Intel HEX | Formato | Rappresentazione di dati binari, in uso dagli anni '70 | L523 |
| Programmatori EEPROM | Tool hardware | Lettura e scrittura del firmware dei chip | E — L522; S57 |
| PICSTART Plus, ChipMax, B&K Precision 866B | Modelli | Fascia $200–$1.200 | L522 |
| ICSP | Interfaccia | Programmazione "in-circuit" senza rimuovere il chip | L522 |
| MPLAB IDE | Ambiente di sviluppo | Per microcontrollori Microchip PIC | E — L523; S58 |
| ICE | Tool di debug hardware | Finestra sul dispositivo in funzione; "emulatore" è termine improprio | E — L523–524; S58 |
| MPLAB ICE, AVR JTAGICE | Modelli ICE | Citati come esempi comuni | L524 |
| JTAG | Interfaccia | Nata per il collaudo post-produzione dei collegamenti; riusata per il debug | E — L524–525; S58 |
| Cavo USB–JTAG, "wiggler" | Adattatori | Collegamento fra PC e dispositivo; formati non standardizzati | L524–525 |
| OpenOCD | Tool software | Interfacciamento JTAG, **per processori ARM**; integrazione Eclipse | L526 |
| UrJTAG | Tool software | Progetto più ampio, supporta più interfacce e dispositivi | L526 |
| FIB, microposizionatori, microscopi a effetto tunnel | Strumentazione avanzata | Citati **oltre lo scopo del capitolo**, per aggirare le protezioni dei chip | L523 |

**Canali di documentazione e approvvigionamento citati dalle fonti**, non ripetuti sopra: makinterface.de (L500), openpcd.org (L503), hak5.org e wiki.hak5.org (L508–509), phenoelit.org (L509), SparkFun (L510), fcc.gov (L518), SweetScape (L518), yagarto.de e urjtag.org (L526).

---

# 7. Priorità didattiche delle slide

Dedotte dallo spazio dedicato agli argomenti e dagli esercizi assegnati. **Non** sono una previsione delle domande d'esame.

| Blocco | Estensione nelle slide | Osservazione |
| --- | --- | --- |
| Accesso fisico e carte | S3–19 (17 pagine) | Trattazione ampia e illustrata; il peso maggiore dell'intera presentazione dopo U3. |
| MIFARE Classic | S14–17 | Approfondimento sostanziale rispetto al richiamo sintetico del libro (L504). |
| ATA | S21–27 | Aggiunge PATA/SATA, lo scenario di riscatto e Vogon rispetto al libro. |
| USB / U3 | S28–43 (16 pagine) | Il blocco più esteso: funzionamento, PocketKnife e quattro pagine di difese. |
| Configurazioni predefinite | S44–51 | Eee PC, password predefinite, due casi ATM, Bluetooth. |
| Reverse engineering | S52–58 (7 pagine) | **Fortemente compresso**: 7 pagine di slide per 16 pagine di libro (L511–526). Protezioni fisiche, FPGA, immagini firmware protette e restrizioni di lettura/scrittura sono sintetizzate o omesse. |
| Esercizi | S59–60 | ROM hacking (60 pt), modifica con editor esadecimale (20 pt), ricerca comparativa PS3/PS4 sulla sicurezza hardware (20 pt) — quest'ultima **non svolta** nel capitolo. |

> [!warning] Squilibrio da compensare
> Il rapporto slide/libro si inverte fra la prima e la seconda metà del capitolo: le slide amplificano accesso fisico e USB, e comprimono il reverse engineering, che nel libro occupa più della metà delle pagine. Studiare solo sulle slide lascia scoperto il blocco L511–526.

---

Per il contenuto: **[[Hacking_Exposed_7_Cap9_Nota_di_studio]]**.
