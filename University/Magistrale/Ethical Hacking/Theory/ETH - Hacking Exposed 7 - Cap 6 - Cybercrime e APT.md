---
tags: [ethl, hacking-exposed-7, apt, cybercrime, forense, cap6]
capitolo: 6
data: 2026-07-04
collegamenti: ["[[ETHL - LAN Manager (LM) vs NTLM]]", "[[ETHL - LSASS Credential Dumping]]", "[[ETHL - SUID e Privilege Escalation]]", "[[ETHL - Rootkit e Persistenza]]", "[[ETHL 0x12 - Cap 4 Hacking Windows]]"]
---

# ETHL — Cap 6: Cybercrime e Advanced Persistent Threats

> [!abstract] Cos'è un APT
> Il nome è la definizione, una parola per proprietà. **Advanced**: metodi sofisticati, zero-day, exploit su misura. **Persistent**: l'attaccante ritorna, ha un obiettivo di lungo periodo e lavora per non farsi rilevare. **Threat**: dietro c'è un avversario organizzato, finanziato e motivato — non uno script lanciato a caso.

Il capitolo cambia registro rispetto ai precedenti. Fin qui abbiamo studiato *tecniche* isolate — scanning, enumeration, hacking Windows/Unix. Qui si guarda l'**avversario** nella sua interezza: chi lo finanzia, cosa vuole, come opera nel tempo. La tesi di fondo, che conviene tenere presente dall'inizio, è che gli APT **non inventano tecniche nuove**: assemblano i mattoni dei capitoli precedenti in una campagna organizzata e paziente. Tutto ciò che leggerai qui — pass-the-hash, cracking offline, rootkit, persistenza — l'hai già visto; la novità è l'orchestrazione.

---

## APT contro attacco opportunistico

La distinzione più importante del capitolo è tra l'attaccante opportunista e l'APT, perché cambia tutto: motivazioni, tempi, tecniche e difese.

L'attacco **non-APT** colpisce i *targets of opportunity*: l'attaccante scansiona la rete, trova un sistema vulnerabile, lo saccheggia e se ne va. È un modello **smash and grab** — mordi e fuggi. L'esposizione è breve, l'obiettivo è immediato (un database, qualche carta di credito), e la vittima è chiunque capiti di essere vulnerabile in quel momento.

L'**APT** ragiona all'opposto. Sceglie il bersaglio *prima* (una specifica azienda, un ministero, un settore), e una volta dentro **resta**, esfiltrando grandi quantità di dati per mesi o anni, lavorando attivamente per non essere scoperto. L'obiettivo non è distruggere né fare un colpo veloce: è **ottenere e mantenere l'accesso** all'informazione, tenendo aperto un rubinetto di dati che cola fuori lentamente.

> [!info] I due moventi
> **Crime**: rubare dati personali (PII) e finanziari per frode e furto d'identità — il movente puramente economico. **Espionage**: spionaggio industriale o *state-sponsored* — proprietà intellettuale, segreti industriali, codice sorgente, vantaggio competitivo o strategico. Il primo monetizza direttamente, il secondo ruba conoscenza. Entrambi condividono la logica del "accesso persistente", ma il bersaglio del dato è diverso.

---

## Il ciclo di vita dell'APT

Le fasi di un APT sono la sua *kill chain*: una sequenza che conviene tenere in fila perché ogni tappa riusa strumenti dei capitoli precedenti. Non sono rigidamente lineari — reconnaissance e lateral movement si ripetono a ogni nuovo host — ma l'ossatura è questa.

**1. Targeting.** L'attaccante studia il bersaglio: raccoglie informazioni (OSINT, struttura aziendale, dipendenti, tecnologie), fa vulnerability scanning e prepara il vettore d'ingresso. Qui nasce lo **spear-phishing**, cucito su misura per una persona specifica.

**2. Access / compromise.** Si entra. Tipicamente un utente clicca e installa il malware. L'attaccante prende piede sull'host, lo mappa, e — punto cruciale — comincia subito a **raccogliere credenziali** da riusare per le compromissioni successive. Il malware offusca il proprio intento per non essere riconosciuto.

**3. Reconnaissance.** Dall'interno, enumerazione di reti e sistemi: quali host esistono, quali servizi, dov'è l'Active Directory, dove stanno i dati che interessano. È l'enumeration del Cap. 3, ma fatta *dopo* essere entrati.

**4. Lateral movement.** Si salta da host a host, usando le credenziali raccolte, per avvicinarsi al dato-obiettivo e per moltiplicare i punti d'appoggio.

**5. Data collection & exfiltration.** Si stabiliscono punti di raccolta interni dove ammassare i documenti, e si esfiltra verso l'esterno — spesso attraverso proxy e canali cifrati per confondersi col traffico legittimo.

**6. Administration & maintenance.** Si mantiene l'accesso nel tempo: backdoor multiple, persistenza al reboot, pulizia dei log. L'APT investe per *restare*, non solo per entrare.

> [!info] Lo spear-phishing come porta
> L'ingresso di quasi ogni APT è lo spear-phishing: convincere un singolo utente ad aprire un allegato o cliccare un link che installa il malware. Non è un attacco tecnico al perimetro — è un attacco alla persona. Ecco perché il perimetro indurito non basta: il vettore aggira firewall e patch passando dall'utente.

---

## Come l'attaccante si nasconde

Un APT vive o muore sulla capacità di non essere ricondotto alla sua origine. Due meccanismi ricorrenti.

Il **cut-out** instrada l'attacco attraverso altri computer già compromessi, così che l'attaccante non appaia mai direttamente: il traffico rimbalza per una catena di macchine intermedie e la tracciabilità si spezza. È la stessa logica del back channel a catena vista altrove — chi indaga risale al massimo all'ultimo hop, non alla sorgente.

Il **dropper delivery service** è l'aspetto "industriale": l'infezione stessa è un servizio comprato da terzi. Esistono economie di *pay-per-install* e campagne *leased* dove chi vuole distribuire malware non lo consegna di persona, ma paga un operatore che ha già una rete di distribuzione. Altri vettori di consegna: **SQL injection** per iniettare malware in siti legittimi (così le vittime si infettano visitando un sito fidato), chiavette **USB infette** lasciate in giro deliberatamente, hardware o software compromesso a monte nella supply chain, impersonificazione, e — più raramente ma più efficace — **insider umani** reclutati o ricattati.

---

## Campagne storiche

I casi reali sono il cuore didattico del capitolo, perché mostrano le fasi teoriche in azione.

### Operation Aurora (2009-2010)

È il caso-scuola dell'APT moderno, e vale la pena seguirlo come narrazione perché contiene ogni fase in sequenza.

Tutto parte da un'**email** con un link a un sito ospitato a Taiwan, che serve **JavaScript malevolo**. Il codice sfrutta una vulnerabilità **zero-day di Internet Explorer**, invisibile all'antivirus perché nessuno la conosceva ancora. L'exploit scarica un **Trojan downloader**, che a sua volta installa una **backdoor RAT** la cui caratteristica distintiva è comunicare col C&C **via SSL** — traffico cifrato che si mimetizza nel normale HTTPS in uscita e passa i firewall.

Da lì comincia la parte "APT": reconnaissance della rete interna, furto di credenziali di **Active Directory**, e con quelle l'accesso agli *share* dove risiede la proprietà intellettuale — nel caso di alcune vittime, i repository del codice sorgente. I dati sono colati fuori per circa **sei mesi** prima della scoperta.

Le vittime furono Google, Juniper, Adobe e oltre 29 aziende. Sull'attribuzione, la nota epistemica è importante: il phishing e i downloader erano linkati a Taiwan, i server C&C furono tracciati a **due scuole in Cina**, e Google accusò pubblicamente la Cina — *ma senza prove* di sponsorizzazione governativa. È un pattern ricorrente in tutto il capitolo (Night Dragon, RSA Breach, Shady RAT sono "comunemente attribuiti" alla Cina, mai dimostrati): l'attribuzione degli APT è quasi sempre circostanziale, non provata.

Le slide elencano un *roster* più ampio di campagne storiche oltre ad Aurora: **Nitro**, **Shady RAT** e **Lurid** — spionaggio industriale prolungato — più due nomi a parte per natura, **Stuxnet** e **DuQu**. Questi ultimi non sono furto di dati ma **sabotaggio** *state-sponsored*: Stuxnet colpì i sistemi di controllo industriale (PLC/SCADA) delle centrifughe iraniane, DuQu è il tool di ricognizione a esso imparentato. Servono a ricordare che sotto l'ombrello "APT" cadono sia lo spionaggio sia il sabotaggio, non solo il furto.

### Anonymous (2011)

Natura completamente diversa, e serve come contrasto. Anonymous non è un'organizzazione finanziata con un movente economico, ma un **collettivo eterogeneo** di hacktivisti. L'obiettivo non è il lucro né l'accesso persistente: è **esporre** informazioni o **interrompere** servizi (DoS) per ragioni politiche o dimostrative. Le tecniche sono più opportunistiche — SQL injection, XSS, exploit di web service, social engineering (finti help desk per estorcere credenziali). Mettere Anonymous accanto ad Aurora chiarisce che "attacco sofisticato" e "APT" non sono sinonimi: manca la persistenza e manca l'organizzazione finanziata.

### Russian Business Network (RBN)

L'estremo cybercriminale puro. Basata a San Pietroburgo, la RBN gestisce **botnet** per spam, phishing e distribuzione malware, e affitta la propria piattaforma a terzi (*bulletproof hosting*). Il movente è cristallino: furto d'identità e denaro. È il volto "servizio" del cybercrime — l'infrastruttura come prodotto.

---

## Gh0st RAT e GhostNet

**GhostNet** (2008-2010) è la campagna di spionaggio condotta con il **Gh0st RAT** contro il Dalai Lama, il governo tibetano in esilio e le organizzazioni tibetane. È interessante per due ragioni: mostra un RAT maturo in azione, e la sua sequenza d'attacco è un compendio dell'intero capitolo.

> [!info] Cosa fa un RAT maturo
> La *Table 6-1* del testo cataloga le capacità di Gh0st: file manager, controllo dello schermo, **keystroke logger**, remote shell, intercettazione di **webcam e microfono**, cracking dei profili dial-up, blanking dello schermo (per nascondere l'attività), gestione della sessione (reboot/shutdown), download di binari, generazione di server custom. La voce più sottile è **"existing rootkit removal"**: azzera gli hook della **SSDT** — cioè bonifica la macchina dai rootkit *concorrenti*. Stessa SSDT dei rootkit Windows del Cap. 4: l'attaccante usa le tecniche rootkit anche per difendere il proprio territorio da altro malware.

La **sequenza dell'attacco Gh0st** vale come modello mentale completo: phishing → backdoor installata al click → il malware si nasconde e si registra per sopravvivere al reboot → stabilisce il canale C&C → enumera il dominio, crea account nuovi, usa **Terminal Server per saltare** ad altri host → modifica i file → comprime i documenti in archivi per l'esfiltrazione → installa un **secondo backdoor con netcat** come ridondanza → crea un altro account e un canale **FTP** → schedula un job che pulisce i log ogni giorno. Ogni singolo passo è una tecnica dei capitoli precedenti; la campagna è il loro assemblaggio.

Per la ricerca sull'origine delle email di phishing, gli strumenti citati sono **Whois**, **Robtex** e **Phishtank**.

---

## Incident response e forense

Quando si risponde a un APT, l'ordine con cui si raccolgono le prove non è un dettaglio: è la differenza tra avere le prove e perderle.

> [!info] Dove restano le tracce
> Prima ancora della forense a caldo, un APT lascia artefatti nei log ordinari, ed è lì che parte la detection: **email logs** (lo spear-phishing d'ingresso), tracce di **lateral movement** dall'abuso di credenziali o identità, e per l'esfiltrazione i log di **firewall e IDS**, **DLP** (Data Loss Prevention), **application history** e **web server**. Sapere in quali log guardare orienta tutta la raccolta successiva.

> [!warning] Ordine di volatilità
> Principio forense cardine: si acquisisce dal **più volatile al meno volatile**, perché ogni istante che passa i dati più effimeri svaniscono. L'ordine: memoria (RAM) → page/swap file → informazioni sui processi in esecuzione → dati di rete (porte in ascolto, connessioni attive) → Registry → log di sistema e applicazione → immagine forense del disco → supporti di backup. Invertire l'ordine (es. spegnere per fare l'immagine del disco) distrugge la RAM, che spesso è la prova più preziosa.

Il **memory dump è cruciale proprio per gli APT**, e il motivo è tecnico: molti impianti APT usano process injection e offuscamento, e cifrano i propri dati su disco e in rete. Ma per *funzionare*, in RAM devono per forza stare in chiaro — la memoria **garantisce i dati decifrati**. È l'analogo "a caldo" del dumping di LSASS del Cap. 4: la memoria di un processo privilegiato che cola fuori il suo contenuto. Lo strumento di riferimento è il **Volatility Framework** (open source), che estrae processi, connessioni, DLL dei processi sospetti ed esegue `strings` sulle DLL per far emergere le stringhe del malware. L'acquisizione si fa con FTK Imager (*Capture Memory*), HBGary FDPro o Mandiant Memoryze. Oltre alla RAM viva, tracce di memoria si recuperano anche *a freddo* da **`pagefile.sys`** (la memoria virtuale paginata su disco) e **`hiberfil.sys`** (l'immagine della RAM salvata all'ibernazione) — preziose quando la macchina è già stata spenta e la RAM volatile è persa.

Il **toolkit forense Windows** per l'analisi "File/Process Capture" — tipicamente su supporto read-only per non alterare il target — è un arsenale che vale la pena conoscere per nome, perché ogni tool risponde a una domanda precisa:

- **MFT** (Master File Table): metadati e timeline dei file.
- `netstat -aon`: connessioni attive con il PID che le ha aperte.
- **CurrPorts**: associa ogni porta aperta alla DLL che la usa.
- **Process Explorer**: processo, DLL referenziate, esecuzioni di `cmd.exe` sospette.
- **Process Monitor**: interazioni processo-kernel, per capire *come* il malware modifica il sistema.
- **VMMap**: mappa della memoria di un processo e stringhe nelle DLL — le stringhe del malware spesso tradiscono un RAT.
- `ipconfig /displaydns` (**DNS Cache**): rivela altri host contattati, possibilmente infetti.
- **File hosts**: controllare modifiche — un redirect statico verso host malevoli è un classico.
- `reg query` sulle chiavi **Run/RunOnce**, `at`/schtasks per i task schedulati.
- **psloglist**: Event log System e Security, dove restano tracce dei comandi degli attaccanti.
- **Prefetch**: gli ultimi 128 programmi eseguiti.
- **Autoruns**: enumera in un colpo tutti i punti di autostart (chiavi Run, servizi, task, driver) — dove un backdoor si aggancia per il reboot.
- **WinMerge**: *diff* della cartella `system32` contro una copia pulita per isolare i file cambiati dall'installazione (`.dll`, `.bat`, `.rar`, `.txt` sospetti).
- **Wireshark**: cattura e analisi del traffico host↔C&C, da cui derivare **firme per l'IDS** e scoprire altri host bersaglio.

Alcuni file meritano attenzione particolare: `ntuser.dat`, `index.dat` (gli URL richiesti dal browser), i `.rdp`, e soprattutto i **`.bmc`** — la *bitmap cache* delle sessioni RDP, che con un **BMC Viewer** permette di **ricostruire cosa ha visto sullo schermo l'attaccante**. Due trucchi anti-evasione: controllare le **esclusioni dell'antivirus**, che spesso lasciano passare PUP come `netcat`/`nc`; e sospettare il **packing** dei file, tecnica classica per eludere le firme.

---

## Persistenza al reboot

Un APT deve sopravvivere ai riavvii, e gli *indicators of compromise* che lo tradiscono sono gli stessi vettori di persistenza del Cap. 4: chiavi Registry **"Run"**, creazione di un nuovo servizio, hooking di un servizio esistente, **scheduled task**, e il mascheramento delle comunicazioni come traffico legittimo. Ai due estremi di aggressività ci sono la sovrascrittura dell'**MBR** o del **BIOS**, che garantiscono persistenza sotto il sistema operativo stesso. Nella catena APT completa, il backdoor si registra tipicamente in **NETSVCS** e adotta un **filename quasi identico** a un file legittimo di Windows: mimetismo puro, pensato per far scivolare l'occhio dell'analista.

---

## Scenario APT su Linux

Il capitolo include un caso Linux che vale la pena seguire perché intreccia parecchi fili del mondo Unix.

Il punto d'ingresso è un **Apache Tomcat** con credenziali deboli — spesso copiate pari pari da una pagina di esempio della documentazione. Attraverso Tomcat si sfrutta un exploit via **Metasploit**, si ottiene esecuzione, e un `cat /etc/passwd` rivela gli username (il file è world-readable). La privilege escalation a root passa da un utente con password ovvia (banalmente il cognome) o dal cracking del superuser.

Per la persistenza si carica un **backdoor PHP** e si crea una **SUID root shell** — un eseguibile con il bit SUID che ridà root anche se la password viene cambiata (rimanda a [[ETHL - SUID e Privilege Escalation]]). Con Metasploit l'host diventa un **pivot** verso il resto della rete senza installare tool aggiuntivi, e **Meterpreter gira interamente in RAM senza scrivere su disco**, lasciando pochissime tracce.

> [!warning] I comandi possono mentire
> Per la diagnosi si isola la macchina col firewall e si controllano `.bash_history`, i file aggiunti o modificati, i log per tracce di `sudo su -`, e `netstat -anlp` / `lsof -i -P` per porte e connessioni. Ma attenzione: un **rootkit può far mentire proprio questi comandi**, nascondendo processi e connessioni all'output. Non ci si può fidare di `netstat` su una macchina potenzialmente compromessa — è la stessa dinamica dei rootkit del mondo Unix.

Nascondigli tipici su Linux: **RAM drive** (`/dev/shm`, `ramfs` — spariscono al reboot, quindi non lasciano traccia a disco), lo *slack space* dei drive, la directory `/dev`, e le insidiose directory `".. "` (**dot-dot-spazio**, che a occhio sembrano la directory parent), oltre ai classici `/tmp` e `/var/tmp`. Un dettaglio utile sulla history: `.bash_history` vive nella home (~2000 righe di default), ma **HISTFILESIZE** controlla il file su disco mentre **HISTSIZE** è solo il buffer in RAM (configurati in `.bashrc`) — un attaccante accorto li azzera. E nei log di Tomcat, le richieste **PUT** sono un campanello: significano che qualcuno da Internet ha *deployato* un'applicazione.

---

## La catena canonica in 14 fasi

Il capitolo chiude con una sequenza "canonica" che unifica tutto. Vale la pena leggerla come la ricapitolazione di ogni tecnica vista, messa in ordine operativo.

1. **Spear-phishing** verso un utente specifico.
2. L'utente clicca; l'applicazione lo redirige a un indirizzo nascosto.
3. **Dropsite**: rileva la vulnerabilità del browser e droppa un downloader.
4. Il downloader invia istruzioni **codificate in base64** a un *secondo* dropsite, da cui installa il backdoor.
5. Il backdoor si installa in `system32` e si registra in **NETSVCS** per sopravvivere al reboot.
6. Adotta un **filename mimetico**, quasi identico a un file di sistema.
7. Stabilisce il **C&C via SSL**.
8. L'attaccante opera tramite **cut-out**, con traffico cifrato che nasconde l'origine.
9. Enumera Computername e account, esegue **pass-the-hash**, raccoglie info locali e di **Active Directory**.
10. Privilege escalation di servizio e recon di rete.
11. **Cracking offline** degli hash raccolti.
12. **Lateral movement** via RDP, `SC.exe`, `NET`.
13. Installa altri backdoor e ulteriori punti di *egress*.
14. Esfiltra i file rubati in archivi **ZIP/RAR rinominati `.GIF`** per non insospettire.

> [!info] Difese contro la catena
> Le contromisure non sono un singolo prodotto ma una difesa in profondità: audit delle modifiche al filesystem, alert (anche via SMS) sui login amministrativi, firewall che monitorano RDP/VNC/`CMD.EXE` in ingresso, AV/HIPS, integrity checking, **NIDS/NIPS** (Snort) e correlazione centralizzata via **SIEM**. Ogni difesa intercetta una fase diversa della catena — nessuna da sola basta.

---

## Malware "as a service"

Il capitolo insiste su un punto di modello di business: molto malware APT non è scritto ad hoc ma **noleggiato**.

**Poison Ivy** è un RAT dal sorgente pubblico, ricorrente in Aurora (2009), nel breach di RSA (2011) e in Nitro (2011), installato anche via zero-day di Internet Explorer. **TDSS/TDL (versioni 1-4)** è una famiglia rootkit/botnet che ha controllato circa **5 milioni di host**, con rootkit, file e comunicazioni cifrate e molti server C&C; ne derivano *ZeroAccess* e *Purple Haze*. Il modello è il **Malware-as-a-Service**: la botnet si affitta per DDoS, click fraud o installazione di Trojan — lo stesso principio dei dropper delivery service, visto però dal lato di chi *vende* la capacità offensiva.

---

## Il filo con i capitoli precedenti

> [!tip] L'APT assembla i mattoni
> Questo capitolo dimostra che gli APT non inventano nulla — orchestrano tecniche già viste. La mappa dei riusi: back channel/reverse a catena ↔ **cut-out** e C&C outbound su SSL; **pass-the-hash + cracking offline** (fasi 9 e 11) ↔ SAM/LM-NTLM/hashcat del Cap. 4; **SUID root shell** come backdoor ↔ SUID/EUID del mondo Unix; **rootkit che fa mentire `netstat`/`lsof`** e Gh0st che azzera gli hook SSDT ↔ rootkit Unix e Windows; **NETSVCS / chiavi Run** ↔ persistenza del Cap. 4; **memory dump in chiaro** ↔ dumping di LSASS. La regola trasversale, confermata ancora una volta: l'APT **abusa di ciò di cui il sistema si fida** — credenziali AD, servizi legittimi, canali cifrati — esattamente come la privilege escalation locale.

---

## Punti ancora aperti

> [!question] Da approfondire
> Fuori dalle slide: la meccanica fine del **pass-the-hash** (rimanda al punto aperto del Cap. 4, integra [[ETHL - LAN Manager (LM) vs NTLM]]); la struttura del **C&C over SSL** e perché l'outbound cifrato passa i firewall (collega al principio *reverse vs bind* — le connessioni in uscita sono quasi sempre permesse); gli interni di **Poison Ivy** e **TDSS/TDL4** (solo nominati); la differenza tra **encoding base64** (offuscamento, reversibile senza chiave) e vera cifratura, dato che le istruzioni al dropsite usano il primo. Da confermare lo scope d'esame: se il Cap. 6 rientra e con che peso rispetto a 2-3-4-5.

> [!todo] Prossimi obiettivi
> In ordine di resa: (1) **nota-ponte Unix vs Windows**, che ora ha un terzo pilastro (l'APT reale che fonde i due mondi); (2) scorporo **Buffer Overflow** ([[ETHL - Buffer Overflow e Stack Smashing]]); (3) le altre già linkate ([[ETHL - Rootkit e Persistenza]], [[ETHL - SUID e Privilege Escalation]]). Dalle sessioni precedenti restano: **nota Kerberos completa** (AS/TGS + tre roasting + PtT), **nota Device Driver Exploits**, e l'**Homework #2**. Formato invariato.
