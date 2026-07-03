lezione precedente [[ETH - Hacking Exposed 7 - Cap 2 - Scanning]]
# Capitolo 3 — Enumeration

> [!example] Scanning vs enumeration 
> Lo scanning resta generico (host vivi, porte aperte); l'enumeration è il passo successivo: connessioni attive dirette al sistema con query mirate. Si distingue in due livelli: generico (banner grabbing, funziona su quasi tutti i servizi) e platform-specific (dipende dai risultati di port scan e OS detection). Le info raccolte includono nomi di account utente (utili per attacchi di password guessing successivi), file condivisi mal configurati, versioni software datate con vulnerabilità note (es. web server con buffer overflow remoti). Servizi tipicamente "fruttuosi": ftp (21), telnet (23), smtp (25), ecc.

## 1. Service fingerprinting

> [!info] Manuale vs automatico 
> Il fingerprinting di servizio rileva revisione/patch level associati alle porte aperte. Manuale = più stealth ma lento; automatico = più efficiente ma più rumoroso/rilevabile.

> [!example] Nmap version scanning (-sV) 
> Usa due database: `nmap-services` (mappa porte→servizi noti) e `nmap-service-probe` (risposte note di servizio → protocollo e versione specifici). Esempio: un servizio SSH nascosto come "Timbuktu" sulla porta TCP 1417 viene smascherato da `-sV` anche se `-sS` lo identifica solo genericamente come `timbuktu-srv1`.
> 
> ```
> nmap -sS target.com -p 1417   → PORT 1417/tcp open timbuktu-srv1
> nmap -sV target.com -p 1417   → PORT 1417/tcp open ssh OpenSSH 3.7
> ```

> [!tip] Amap Seconda opinione rispetto a Nmap: un'altra tecnica di pattern-matching sui servizi, utile per confermare o disambiguare i risultati di `-sV`.

## 2. Vulnerability scanners

> [!info] Database di firme note 
> Confrontano le porte/servizi rilevati con un database di vulnerabilità note. Free: Nessus, OpenVAS. Commerciali: McAfee, Qualys, Rapid7, nCircle, Tenable.

> [!info] Nessus 
> Di Tenable, scansione esaustiva, plug-in personalizzati in NASL (Nessus Attack Scripting Language). Era free e open source fino alla v3, poi proprietario closed source.

> [!warning] Contromisure 
> Nessus Auditarsi regolarmente con patch e configuration management efficaci. IDS/IPS che riconoscono i pattern di comportamento di Nessus, eventualmente rallentando le scansioni per dirottare l'attaccante verso bersagli più morbidi.

> [!info] Nmap vs Nessus 
> Nmap è più ampio ma meno potente nel vulnerability scanning; Nessus è più focalizzato. Nmap Scripting Engine (NSE) usa Lua e offre una libreria di script per network discovery, version detection, backdoor detection, sfruttamento di vulnerabilità.

## 3. Basic banner grabbing

> [!info] Concetto 
> I banner sono presenti nelle risposte alle richieste. Tecnica generica, funziona su molte applicazioni comuni su porte standard: HTTP (80), SMTP (25), FTP (21).

> [!example] Manuale — telnet
> 
> ```
> telnet www.example.com 80
> HTTP/1.1 400 Bad Request
> Server: Microsoft-IIS/5.0
> ```
> 
> Il banner rivela direttamente il server e la versione (qui IIS 5.0).

**ma telnet gira sopra http?** No, è il contrario — e la confusione è comprensibile perché nelle slide si vede `telnet www.example.com 80` e sembra strano.

Telnet è uno strumento che apre una connessione TCP grezza verso qualsiasi host e qualsiasi porta. Di default si connette alla porta 23 (il servizio Telnet vero e proprio), ma puoi dirgli di connettersi a qualsiasi porta tu voglia.

Quando fai `telnet www.example.com 80`, stai usando telnet come client TCP generico per connetterti alla porta 80. Una volta connesso, sei tu che parli HTTP a mano — scrivi la richiesta, il server risponde in HTTP, e nel mezzo della risposta compare il banner con `Server: Microsoft-IIS/5.0`.

Quindi telnet qui non ha nulla a che fare col protocollo Telnet: è solo un modo comodo per aprire una socket TCP verso una porta arbitraria e digitare manualmente qualsiasi protocollo testuale. Funziona bene per HTTP, SMTP, FTP — tutti protocolli testuali dove i comandi sono stringhe leggibili.

**Telnet vs telnet?** Hai ragione che suona strano, ma il punto è che il nome "telnet" si riferisce a due cose diverse che storicamente coincidevano.

Il programma `telnet` nasce per connettersi a server Telnet (porta 23) usando il protocollo Telnet, che prevede una negoziazione iniziale tra client e server (sequenze IAC per negoziare opzioni di terminale, echo, ecc.). In quel caso strumento e protocollo coincidono.

Ma il programma in sé non fa altro, sotto, che aprire una connessione TCP verso un host e una porta, e poi passarti la tastiera. Se gli dici `telnet host 80`, apre la connessione TCP verso la porta 80 e si mette in attesa — ma dall'altra parte c'è un server HTTP, non un server Telnet, quindi la negoziazione del protocollo Telnet non parte mai. Rimane una connessione TCP nuda, e tu ci scrivi sopra HTTP a mano.

È un po' come usare un cacciavite come leva: lo strumento è sempre quello, ma lo stai usando per uno scopo diverso da quello per cui è stato progettato. Il nome rimane "cacciavite".

Oggi per questo scopo si usa più spesso `netcat` o `curl`, proprio perché sono più espliciti nello scopo — ma telnet ha funzionato come strumento di debug TCP per decenni esattamente per questo motivo.

> [!example] Automatico — netcat 
> Si può reindirizzare un file di richieste a `nc` per catturare output più ricchi (header completi, cookie, contenuto HTML).
> 
> ```
> nc -nvv -o banners.txt 10.219.100.1 80 < nudge.txt
> ```
> 
> Da vendor e versione del software si risale a vulnerabilità note.

> [!warning] Contromisure banner grabbing 
> Disattivare i servizi non necessari, usare access control list, auditarsi regolarmente, disabilitare ove possibile la presentazione di vendor e versione nei banner.

## 4. Enumerazione servizi comuni

### FTP, TCP 21

> [!info] Caratteristiche 
> Ancora popolare per upload di contenuti web. Le password FTP viaggiano in chiaro. Esistono liste di siti FTP anonimi (es. ftp-sites.org). Quando ci si connette, appare un banner esplicito che informa l'esatta versione di [[FTP]]. FTP non contiene crittografia ed inoltre attenzione ad eventualy missconfigurations per l'accesso anonymous ancora peggio con world writtable files/directories (hacking linux). 

> [!tip] Google dorking 
> `intitle:"Index of ftp://"` per trovare server FTP esposti via indicizzazione web; spesso il banner HTTP/FTP associato rivela versioni di Apache, PHP, OpenSSL ecc.

> [!warning] Contromisure FTP 
> Le password in chiaro sono il problema principale. Alternative: SFTP (su SSH), FTPS (su SSL). I contenuti pubblici dovrebbero essere serviti via HTTP, non FTP. Attenzione all'FTP anonimo: disabilitare l'upload non ristretto.

### Telnet, TCP 23

> [!info] Banner ed enumeration account 
> Telnet espone banner di sistema (OS, versione, vendor, esplicito o implicito) prima del login. Permette anche enumeration di account via brute-force: username validi/non validi e password errate generano messaggi di errore diversi, da cui si ricava una lista di account validi. Password e dati viaggiano in chiaro.

> [!warning] Contromisure [[Telnet]] 
> Eliminarlo se possibile, usare [[Obsidian-University/University/Magistrale/Ethical Hacking/For Passion/Hacking Linux/SSH|SSH]] al suo posto. Se serve comunque, restringerlo a IP sorgente autorizzati o farlo passare per VPN. Modificare le info nel banner. Inserire un ritardo di riconnessione tra tentativi di login falliti.

### [[SMTP]], TCP 25

> [!example] VRFY ed EXPN via telnet 
> `VRFY` conferma nomi utente validi, `EXPN` rivela gli indirizzi di consegna reali di alias e mailing list. Tool automatico: `vrfy.pl` (specifica server SMTP e username da testare).
> 
> ```
> telnet 192.168.202.34 25
> vrfy root   → 250 root <root@bigcorp.com>
> expn adm    → 250 adm <adm@bigcorp.com>
> ```

> [!warning] Contromisure SMTP 
> Disabilitare i comandi EXPN e VRFY, o restringerli a utenti autenticati. Sendmail ed Exchange lo permettono nelle versioni moderne.

### [[DNS]], TCP/UDP 53

> [!info] Zone transfer 
> Un trasferimento di zona scarica l'intero contenuto dei file di zona di un dominio. Normalmente DNS gira su UDP 53; TCP 53 è usato per i trasferimenti di zona. Su server mal configurati si può fare enumeration via zone transfer (record A e HINFO) con `nslookup` (`ls -d <dominio>`) o `dig`. La maggior parte dei DNS server moderni lo restringe alle sole macchine autorizzate.

> [!example] BIND version e DNS cache snooping 
> `dig @IP version.bind txt chaos` rivela la versione del server BIND. Il DNS cache snooping con `+norecurse` esamina solo i dati locali della cache del DNS server: se ANSWER è 0 il dominio non era in cache (status REFUSED se la query ricorsiva non è permessa); una query normale (ricorsiva) lo aggiunge alla cache, dopodiché una seconda query con `+norecurse` lo trova già presente — questo rivela se quel dominio è stato risolto di recente da quel server, utile per dedurre pattern di traffico interno.

> [!tip] Tool di DNS enumeration 
> `dnsenum`: Google scraping per subdomain aggiuntivi, brute forcing di subdomain, elenco dei range di rete del dominio, WHOIS sui range trovati, correlazione delle informazioni con risorse web. `fierce.pl`: prova prima lo zone transfer, se fallisce passa al brute force classico dei subdomain (controllando anche i wildcard DNS), elenca i subnet trovati da probare con nmap. CentralOps.net offre tool online equivalenti (Domain Dossier, NsLookup, AutoWhois, ecc.).

> [!warning] Contromisure DNS 
> Usare server DNS interni ed esterni separati (non esporre target interni). Bloccare o restringere i trasferimenti di zona DNS. Restringere le query DNS per limitare il cache snooping.

### [[TFTP]], TCP/UDP 69

Trivial File Transfer Protocol (TFTP) è un servizio che gira su porta 69 ed è UDP-based. Inoltre non è come ftp che permette di eseguire comandi come `ls` sulla macchina target, ma l'attaccante deve sapere esattamente il nome del file e la sua directory per scaricarlo. Inoltre non è autenticato. Banalmente fa cagare ma almeno l'attaccante ha difficoltà a reperire informazioni perché non può leggere il file system. però può sempre fare `get /etc/passwd` ed otterrebbe tutti gli users.

> [!info] Insicurezza intrinseca 
> Gira in chiaro, nessuna autenticazione: basta conoscere il nome del file e chiunque può prenderlo (nei casi peggiori anche `/etc/passwd`). Usato da router e telefoni VoIP per aggiornare il firmware — cercare i file di configurazione.
> 
> ```
> tftp 192.168.202.34
> tftp> connect 192.168.202.34
> tftp> get /etc/passwd /tmp/passwd.cracklater
> ```

> [!warning] Contromisure TFTP 
> Restringere l'accesso con TCP Wrappers (è come un firewall software, permette solo a certi client di accedere al servizio). Limitare l'accesso alla directory /tftpboot. Bloccarlo al firewall perimetrale.

### Finger, TCP/UDP 79
finger era un utility banale ai tempi in cui internet era un posto piccolo ed amichevole. permetteva a chiunque, dato uno specifico indirizzo IP/hostname, di sapere in pratica il contenuto di /etc/passwd (senza password), nome dell'utente, informazioni extra (domanda per trovare la password) ed anche il tempo di IDLE dando l'idea all'attaccante di conoscere chi sono gli utenti e quanto in genere sono attenti.

> [!info] Utenti esposti 
> Mostra gli utenti collegati su sistemi locali o remoti, se abilitato — utile per social engineering (nomi reali, orari di login, idle time). Contromisura: bloccare l'accesso remoto a finger.

### [[HTTP]], TCP 80

> [!info] Banner grabbing e crawling Banner via telnet o netcat. 
> Per siti SSL-enabled: redirect a un proxy SSL (sslproxy) o uso di un client SSL (openssl). Crawling con utility come Sam Spade (gratuito per Windows): cerca email, link, immagini, valori di form nascosti, pattern via regex (es. "password", "admin").

> [!tip] Grendel-Scan 
> Tool automatico che esegue crawling del sito e segnala vulnerabilità (commenti nel codice, robots.txt, directory esposte ecc.). Molto lento.

> [!warning] Contromisure HTTP 
> Cambiare il banner dei web server (può ingannare malware automatizzato) — es. MS URLScan per IIS v4+, che usa filtri e permette banner personalizzati. IIS ha comunque storicamente molti exploit pronti all'uso.

### MSRPC endpoint mapper, TCP 135

Sì: una Remote Procedure Call è esattamente quello che hai detto. È il meccanismo per cui un programma chiama una funzione che in realtà viene eseguita su un'altra macchina, ma scritta in modo che _sembri_ una normale chiamata di funzione locale. Tu scrivi `risultato = fai_qualcosa(parametri)`, e sotto il cofano quella chiamata viene impacchettata, spedita via rete a un server, eseguita là, e il risultato ti torna indietro. L'idea è nascondere la rete: il programmatore chiama una funzione come se fosse locale, e l'infrastruttura RPC si occupa di serializzare argomenti, trasmetterli, eseguire e riportare la risposta. È un pattern vecchissimo e fondamentale — Unix ha il suo (ONC RPC, quello di NFS), Windows ha MSRPC.

Ora MSRPC. È l'implementazione Microsoft di questo meccanismo, ed è molto più pervasiva di quanto suggerisca il nome. Non è specificamente "RPC per Active Directory" — è l'infrastruttura di comunicazione generale su cui _tantissimi_ servizi Windows si appoggiano per parlare tra macchine. Active Directory ne è uno dei clienti, ma lo sono anche la gestione remota dei servizi, il task scheduler, la stampa, Exchange, la gestione degli account, e decine di altri sottosistemi interni. Quando due macchine Windows si scambiano operazioni di sistema tra loro, spessissimo sotto c'è MSRPC.

E qui arriva il pezzo che collega tutto all'endpoint mapper della porta 135, che è la parte che secondo me non era chiara. Il problema pratico di RPC è: se ci sono decine di servizi diversi che offrono funzioni remote, su quale porta ascolta ciascuno? Assegnare una porta fissa e nota a ognuno sarebbe ingestibile. La soluzione di Windows è avere un _registro centralizzato_: l'endpoint mapper, che sta sempre sulla porta 135. Il suo unico compito è tenere l'elenco di "quale servizio RPC è attivo su questa macchina, e su quale porta dinamica lo trovi".

Quindi il flusso normale è: un client vuole parlare col servizio X, contatta la 135 e chiede "dove trovo X?", l'endpoint mapper risponde "sulla porta 49xxx", e il client va lì. È una specie di centralino/elenco telefonico interno.

Ed è esattamente per questo che la 135 è oro per l'enumeration. Interrogandola con `epdump` o `rpcdump.py` non attacchi niente — chiedi solo al centralino la lista completa. E lui te la dà: quali servizi RPC girano, i loro identificatori (gli UUID che vedi nelle slide, tipo "Messenger Service"), e su quali endpoint sono raggiungibili. In un colpo ottieni una mappa dei sottosistemi attivi sulla macchina, che ti dice cosa c'è da attaccare dopo.

Sulla contromisura ora si capisce la tensione: bloccheresti volentieri la 135, ma alcuni servizi legittimi che passano da lì — Exchange classico in primis — hanno bisogno che client remoti la raggiungano. Da cui le alternative delle slide: incapsulare tutto in VPN, o usare Outlook Web Access via HTTPS, o le versioni di Exchange (2003+) che fanno "RPC over HTTP" — cioè trasportano lo stesso MSRPC dentro HTTPS sulla 443, così non devi esporre la 135 nuda su Internet.

Quindi per rispondere secco alle tue tre domande: RPC = sì, far eseguire una funzione a una macchina remota facendola sembrare locale. MSRPC = l'implementazione Windows di quel meccanismo, generale, non solo per AD (AD è solo uno dei tanti che la usano). E la 135 non è il servizio in sé, è l'elenco che ti dice dove stanno tutti gli altri servizi RPC. 

**Esempio di applicazione**
Ti do qualche esempio concreto, con l'accortezza che semplifico parecchio il "come" — i dettagli reali di ogni protocollo sono più complessi, ma l'idea di fondo è fedele.

Gestione remota dei servizi (il Service Control Manager). Quando un amministratore da una macchina avvia, ferma o interroga un servizio su un'altra macchina Windows, sotto c'è MSRPC. In termini di RPC: il client chiama qualcosa come "avvia il servizio chiamato Spooler" e quella funzione viene eseguita sul server remoto. Lo strumento `sc \\server start Spooler` fa esattamente questo. È lo stesso meccanismo che un attaccante sfrutta per eseguire codice da remoto una volta che ha le credenziali — dice al SCM remoto "crea e avvia questo servizio", e il servizio è il suo payload.

Gestione remota dei task pianificati. Creare o leggere un'attività nel task scheduler di un'altra macchina passa da MSRPC. Client: "aggiungi un task che esegue X ogni giorno alle 3"; il server lo registra. Anche questo è un classico vettore di esecuzione remota e di persistenza.

Autenticazione e account (i sottosistemi SAMR e LSA). Questi gestiscono le query sugli account utente e sui gruppi. Quando qualcosa chiede "dammi la lista degli utenti locali di questa macchina" o "risolvi questo SID in un nome", quella domanda viaggia su MSRPC verso i servizi SAMR/LSA. È il canale che sta sotto agli strumenti di enumeration utenti che hai visto — user2sid/sid2user in fondo chiedono al server, via RPC, di tradurre nomi e identificatori.

Active Directory / replica tra domain controller. Questo è il caso "AD" che immaginavi. Quando due domain controller sincronizzano le loro copie della directory, o quando un client fa certe query sulla struttura del dominio, usano protocolli RPC dedicati. È uno dei tanti clienti di MSRPC, importante ma non l'unico.

Exchange. Nella sua forma classica, il client Outlook parlava col server Exchange via MSRPC — da qui il problema della 135 di cui parlavamo, e la successiva soluzione di incapsularlo in HTTPS.

Lo schema comune, semplificato, è sempre lo stesso: c'è un'operazione di sistema che deve avvenire su una macchina diversa da quella dove sei tu (gestire un servizio, un account, un task, una casella di posta), la si esprime come "chiamata di funzione" verso quella macchina, MSRPC la trasporta, e la 135 è il centralino che all'inizio ti dice su quale porta trovare il sottosistema giusto. Cambia il servizio, cambia la funzione chiamata, ma l'impalcatura sotto è identica.

> [!info] Portmapper Windows 
> Interrogando questo servizio si ottengono informazioni su applicazioni e servizi disponibili sulla macchina target. Tool: `epdump` (Windows Resource Kit) mostra servizi associati a indirizzi IP, richiede un po' di interpretazione dei risultati; `rpcdump.py` produce risultati analoghi su Linux/Backtrack.

> [!warning] Contromisure MSRPC
> Bloccare la porta 135 al firewall, se possibile — ma alcune configurazioni di Exchange Server richiedono accesso remoto all'endpoint mapper. Alternative: VPN verso la rete interna, oppure Outlook Web Access (OWA) via HTTPS; Exchange 2003+ implementa RPC su HTTP.

### [[NetBIOS Name Service (NBNS)]], UDP 137

Hai già in mano il modello Linux, e la cosa migliore è appoggiarci sopra quello Windows perché la logica è parallela — solo che Windows ha un intero secondo binario di risoluzione (NetBIOS) che gli si affianca, ed è quello che rende la gerarchia più affollata. Ti ricostruisco tutto con calma.

Partiamo dal tuo modello Linux, così fissiamo il riferimento. Su Linux, quando devi risolvere un nome, l'ordine è governato da `/etc/nsswitch.conf`, ma nel caso classico è: prima `/etc/hosts` (file statico locale), poi il DNS configurato in `/etc/resolv.conf` (che nel 90% dei casi punta al router che fa da stub resolver verso il DNS del provider). Due tappe, in sostanza: file locale, poi DNS. Pulito e lineare.

Ora Windows. La prima cosa da capire è che ci sono _due famiglie di nomi_ che convivono, e questa è la radice di tutta la complicazione. Da un lato i nomi hostname/DNS (`server1.azienda.com`, gerarchici, con i punti, moderni). Dall'altro i nomi NetBIOS (`SERVER1`, piatti, senza gerarchia, massimo 15 caratteri, vecchio stile, ereditati dal networking Microsoft anni '80/'90). Windows può risolvere entrambi, e ha _due catene di risoluzione separate_, una per ciascuna famiglia, che vengono provate in cascata. Quando la tua nota elenca "metodi standard" e "metodi aggiuntivi", sta di fatto elencando prima la catena DNS-style e poi la catena NetBIOS-style.

Vediamo la **prima catena, quella dei nomi host/DNS**, che è quella che assomiglia a Linux:

Il primo controllo è il nome host locale della macchina stessa. Windows guarda se il nome che stai cercando è semplicemente sé stesso — il proprio hostname configurato. Questo è il "in più" che avevi notato: è un cortocircuito banale, "sto cercando me?". Se sì, risolve subito senza andare oltre.

Il secondo è il file hosts, che su Windows sta in `C:\Windows\System32\drivers\etc\hosts` ed è concettualmente identico al `/etc/hosts` di Linux: mappature statiche nome→IP scritte a mano. Stesso formato BSD, stessa funzione.

Il terzo è il server DNS, esattamente come `resolv.conf` + query al resolver. Windows manda la query al DNS configurato sulla scheda di rete, che poi risolve ricorsivamente. Fin qui è il gemello di Linux.

C'è però una tappa in mezzo che Windows rende esplicita e Linux tiene più nascosta: la **cache del resolver DNS**. È una tabella in RAM che conserva sia le voci del file hosts (caricate all'avvio) sia i nomi risolti di recente via DNS, per non doverli richiedere ogni volta. Su Linux una cache simile può esserci (systemd-resolved, nscd…) ma non è sempre presente; su Windows è un componente standard e sempre attivo — è quella che svuoti con `ipconfig /flushdns`. Nella pratica è la primissima cosa consultata, prima ancora di rifare la query DNS vera.

Se la prima catena non risolve — tipicamente perché il nome è un nome NetBIOS piatto tipo `SAMP4`, non un FQDN — Windows passa alla **seconda catena, quella NetBIOS**, ed è qui che entra tutto il materiale "in più" rispetto a Linux:

Prima la cache dei nomi NetBIOS, gemella in RAM della cache DNS ma per i nomi NetBIOS risolti di recente (la ispezioni con `nbtstat -c`).

Poi il server NBNS, che è l'analogo NetBIOS del server DNS: un server centrale a cui chiedere "chi è SAMP4?". L'implementazione Microsoft di questo server si chiama WINS. Concettualmente: WINS sta ai nomi NetBIOS come il server DNS sta ai nomi host.

Poi, se non c'è un WINS o non risponde, il broadcast locale: Windows urla sulla rete locale "chi di voi si chiama SAMP4? risponda!" (fino a tre tentativi di Name Query Request). Chi si riconosce risponde col proprio IP. Questo funziona _solo_ sul segmento di rete locale, perché i broadcast non attraversano i router — ed è una differenza concettuale importante rispetto al DNS, che invece funziona attraverso Internet.

Infine il file Lmhosts, che è il gemello NetBIOS del file hosts: un file statico locale (`...\etc\lmhosts`) che mappa nomi NetBIOS a IP, usato soprattutto per raggiungere nomi NetBIOS su subnet remote, dove il broadcast non arriverebbe.

Se metti insieme il quadro, la gerarchia Windows completa è: nome host locale → cache resolver DNS → file hosts → server DNS, e se ancora niente → cache NetBIOS → server WINS → broadcast locale → file Lmhosts. L'ordine esatto tra alcune di queste tappe può variare a seconda della configurazione e del "node type" NetBIOS impostato sulla macchina (che decide, per esempio, se provare prima il broadcast o prima WINS), ma la struttura generale è questa: prima si esaurisce il mondo DNS-style, poi si scende nel mondo NetBIOS-style.

Il collegamento col capitolo di enumeration, per chiudere il cerchio: tutta la seconda catena — NBNS, broadcast, la tabella dei nomi NetBIOS — è vecchia, chiacchierona e progettata in un'epoca senza preoccupazioni di sicurezza. Gira su UDP 137 e risponde volentieri a chi chiede. È esattamente per questo che strumenti come `nbtstat` e `nbtscan` riescono a estrarre nomi macchina, nomi dominio/workgroup e utenti interrogando quel servizio: stanno semplicemente parlando il protocollo della seconda catena, che è nato per rispondere senza fare domande.

**[[NetBIOS]] è lagacy?**
Sì, hai colto la traiettoria giusta, con un paio di sfumature che vale la pena precisare per non farti un'idea troppo netta.

È corretto che NetBIOS/NBNS è considerato legacy e che il meccanismo primario oggi è DNS. In una rete Windows moderna basata su Active Directory, la risoluzione nomi si appoggia su DNS — al punto che AD _richiede_ un'infrastruttura DNS per funzionare, perché i client trovano i domain controller e i servizi proprio tramite query DNS specifiche. WINS, il server NBNS di Microsoft, è di fatto deprecato: Microsoft ne raccomanda la dismissione da anni e nelle reti nuove non lo si installa più. Quindi il tuo istinto è giusto: il baricentro si è spostato completamente su DNS.

La sfumatura però è che "legacy" non significa "spento". La seconda catena di risoluzione — in particolare i meccanismi di broadcast locale — è ancora presente e spesso ancora _attiva di default_ su Windows, come fallback. Ci sono due protocolli in gioco qui: il vecchio NetBIOS Name Service (NBT-NS, la UDP 137 delle slide) e un suo successore più recente chiamato LLMNR, ma concettualmente fanno la stessa cosa — se il DNS non risolve un nome, la macchina ripiega sull'urlare sulla rete locale "chi si chiama così?". Restano lì proprio come rete di sicurezza per i casi in cui il DNS non copre un nome.

Ed è esattamente questo residuo che conta dal punto di vista security, ed è il motivo per cui vale la pena saperlo anche se è "vecchio". Quel fallback broadcast è la base di una delle tecniche di attacco più comuni ancora oggi nelle reti Windows reali: il **poisoning di LLMNR/NBT-NS**. L'idea è semplice — quando una macchina fa il broadcast "chi è SERVERXYZ?" perché il DNS ha fallito (magari per un banale errore di battitura o una share che non esiste più), l'attaccante sulla stessa rete risponde "sono io!", la vittima gli si connette e gli manda le proprie credenziali (in forma di hash), che poi vengono craccate o rilanciate. È il pane quotidiano di strumenti come Responder, ed è una delle prime cose che si fa in un pentest interno.

Quindi la sintesi corretta è: come _meccanismo di funzionamento normale_ sì, oggi è DNS e NetBIOS è archeologia; ma come _superficie d'attacco_ quel legacy è vivissimo, perché è rimasto attivo come fallback silenzioso su milioni di macchine, e la contromisura moderna è proprio disabilitarlo esplicitamente (via policy) quando non serve — che è la versione aggiornata del "blocca UDP 137" delle tue slide.

Ed è un buon esempio di quel discorso sui feedback del corso di prima: il tool `nbtstat` è vecchio, ma il _concetto_ — un servizio di risoluzione nomi chiacchierone che risponde a chi non dovrebbe — è esattamente ciò che sfrutti ancora oggi, solo con Responder al posto di nbtscan.

**Se è legacy, significa che adesso c'è un nuovo modo per risolvere i nomi [[NetBIOS]]-like. Come fa il DNS moderno di windows a risolvere tali nomi correttamente?**

Il meccanismo è il DNS suffix search list: quando digiti un nome corto senza punti (`server1`), il client Windows appende automaticamente uno o più suffissi DNS predefiniti — tipicamente il dominio a cui la macchina appartiene, es. `azienda.local` — trasformandolo in un FQDN completo `server1.azienda.local`, e poi manda _quello_ al DNS.

Quindi il DNS non riceve mai il nome corto: riceve sempre un nome pienamente qualificato. È il client che fa l'espansione prima di chiedere. Se hai più suffissi in lista, li prova in ordine finché uno risolve.

In sostanza è l'analogo del campo `search` in `/etc/resolv.conf` su Linux — stessa identica idea: "se il nome è corto, completalo con questi domini prima di interrogare il DNS".

**Dove il DNS sarebbe la macchina che in genere in un AD sarebbe il Coontroller**
Sì, esatto — in una rete Active Directory il DNS server a cui i client mandano le query è tipicamente il domain controller stesso.

Nella stragrande maggioranza dei deployment AD, il domain controller fa doppio ruolo: è sia il controller (autenticazione, directory degli utenti/gruppi, Kerberos) sia il DNS server della zona interna del dominio. Non è un obbligo tecnico assoluto — puoi separarli — ma è la configurazione standard, e Microsoft la integra così di default perché AD e DNS sono strettamente accoppiati.

Il motivo per cui devono stare insieme (o comunque strettamente collegati) è che AD _dipende_ dal DNS per funzionare: i client trovano il domain controller stesso tramite query DNS speciali (i record SRV, che dicono "il servizio Kerberos/LDAP di questo dominio sta su questo host"). Quindi quando una macchina si accende e deve autenticarsi al dominio, la prima cosa che fa è chiedere al DNS "dov'è il mio domain controller?" — e la risposta arriva dal DNS che gira, appunto, sul domain controller.

È anche il pezzo che chiude il discorso di prima sul Dynamic DNS: le macchine si registrano da sole nel DNS interno, e quel DNS interno è ospitato sul controller. Quindi il controller è contemporaneamente il posto dove le macchine si iscrivono e il posto che interroghi per ritrovarle.

**Quindi il DNS dell'AD funge anche da DNS principale degli host anche quando fanno un cache miss di www.example.com in locale**
Sì, esatto, e cogli un punto che spesso sfugge. Il DNS del domain controller non serve solo i nomi interni del dominio — è il DNS _tout court_ per quelle macchine, per qualsiasi nome, incluso `www.google.com`.

Il meccanismo è questo: i client del dominio hanno configurato come server DNS l'indirizzo del domain controller (di solito assegnato via DHCP). Quindi _ogni_ query DNS che non è già in cache locale va lì, indistintamente — che sia `server1.azienda.local` o `www.google.com`.

La differenza sta in cosa fa il DC con la query, a seconda del nome:

Se il nome appartiene alla zona interna che il DC gestisce (`.azienda.local`), risponde lui direttamente perché è autoritativo per quella zona — ha il record in casa.

Se il nome è esterno (`www.google.com`), il DC non lo conosce, quindi si comporta come un normale resolver ricorsivo: va a chiederlo lui per conto del client, risalendo la gerarchia DNS pubblica (o, più comunemente, inoltrando la query a un forwarder — tipicamente il DNS del provider o un resolver pubblico come 8.8.8.8). Poi restituisce la risposta al client e la mette in cache per le volte successive.

Quindi dal punto di vista del client c'è un unico DNS server per tutto; è il DC che smista internamente tra "questo lo so io" e "questo vado a chiederlo fuori". È lo stesso doppio ruolo di qualsiasi resolver aziendale: autoritativo per i nomi interni, ricorsivo/forwarder per tutto il resto.

Piccola nota che collega al capitolo di prima: è proprio questa la ragione per cui il DNS cache snooping ha senso come tecnica — un DNS che fa da resolver per i suoi client accumula in cache i nomi esterni che gli utenti hanno visitato, e interrogandolo con `+norecurse` puoi dedurre cosa è stato risolto di recente.

**se noi stiamo inviando una stringa in formato DNS-like, il server allora non userà mai il protocollo NetBIOS Name Resolution**
Hai messo il dito su una confusione reale, e vale la pena scioglierla perché stai mescolando due meccanismi diversi che ho descritto in momenti diversi. Ti separo i due, perché la tua domanda nasce proprio dal trattarli come se fossero lo stesso.

Prima una correzione di fondo che è la radice dell'equivoco: non esistono "due famiglie di DNS", una moderna e una legacy. Esistono due sistemi di risoluzione nomi _distinti e separati_ — il DNS da una parte, e il NetBIOS name resolution dall'altra. Non sono due versioni dello stesso protocollo: sono due protocolli diversi, con formati di nome diversi, che Windows prova in cascata. Il DNS non "mantiene una parte per retrocompatibilità"; il pezzo legacy è un sistema a sé, NetBIOS, che vive accanto al DNS, non dentro di esso.

Ora, i due meccanismi che stai fondendo insieme:

Il primo è il **DNS suffix search list** — l'espansione dei nomi corti. Quando digiti `server1` (nome corto, senza punti), il client lo completa in `server1.azienda.local` e lo manda al DNS. Questo è puramente un fatto di _formato del nome_: prendo un nome breve e lo rendo un FQDN valido. Ma attenzione — questo non ha niente a che vedere con NetBIOS. Un nome corto non è un "nome NetBIOS"; è solo un nome DNS incompleto. Qui NetBIOS non entra proprio in gioco. Questo è il meccanismo di cui parli quando dici "lo converte nel formato moderno", e la tua conclusione su _questo_ è corretta: se il nome viene espanso e risolto via DNS, stai usando DNS puro, NetBIOS non tocca palla.

Il secondo, completamente diverso, è la **catena di fallback NetBIOS**. Questa non converte niente. Scatta solo quando la catena DNS ha già _fallito_ — non ha trovato il nome. A quel punto Windows non "traduce il nome in formato moderno": prova un protocollo diverso, NetBIOS, con i suoi meccanismi (cache NetBIOS, WINS, broadcast). Qui il vecchio protocollo viene usato _davvero_, sul serio, perché il DNS non ha saputo rispondere.

Quindi la risposta secca alla tua domanda: la conversione di cui parli (nome corto → FQDN) e l'uso del protocollo NetBIOS sono due cose che non si incontrano mai. O il nome si risolve via DNS — e allora sì, è tutto DNS moderno, NetBIOS non viene usato — oppure il DNS fallisce e Windows ripiega su NetBIOS, e in quel caso non c'è nessuna conversione, si parla proprio il vecchio protocollo con i suoi pacchetti.

La domanda giusta da porsi, allora, è: _quando_ si finisce sul fallback NetBIOS, dato che oggi quasi tutto si risolve via DNS? La risposta è: quando cerchi un nome che nel DNS non esiste. Casi tipici — una vecchia macchina che non si è registrata nel DNS interno, un errore di battitura, una share che non c'è più, oppure una rete senza un DNS che copra quei nomi. In tutti questi casi il DNS dice "non lo conosco", e Windows, invece di arrendersi, urla sulla rete locale in NetBIOS "c'è qualcuno che si chiama così?". Ed è esattamente qui — in questo fallback che parla il protocollo vecchio per davvero — che vivono gli attacchi di poisoning (Responder) di cui parlavamo: l'attaccante risponde "sì, sono io" a quella richiesta NetBIOS che il DNS non ha saputo gestire.

Riassumendo il punto che ti sfuggiva: la retrocompatibilità NetBIOS non è "il DNS che converte formati". È un secondo protocollo separato che entra in scena solo dopo il fallimento del DNS, e quando entra in scena lo fa in pieno, senza conversioni. L'espansione dei nomi corti è tutt'altra faccenda, tutta interna al mondo DNS.

> [!info] NBNS e name resolution 
> NBNS è il servizio di risoluzione nomi di Microsoft, simile a DNS, disponibile solo su IPv4. Windows usa due sistemi: DNS (preferito) e NetBIOS Name Resolution (ancora usato da tutte le versioni). Metodi di risoluzione standard: nome host locale, file hosts, server DNS. Metodi aggiuntivi: cache resolver DNS, cache nomi NetBIOS, server NBNS (l'implementazione Microsoft è WINS), broadcast locale (fino a 3 messaggi Name Query Request), file Lmhosts.

> [!example] NET VIEW e altri tool 
> `net view /domain` elenca i domini; `net view /domain:nomedominio` elenca i server in quel dominio. NBNS normalmente funziona solo sul segmento di rete locale, ma è possibile instradarlo su TCP/IP per fare enumeration da remoto. Altri tool: `nltest`/`netdom` (trovano i domain controller), `netviewx` (trova servizi specifici), `nbtstat` (singolo sistema), `nbtscan` (intero range di indirizzi, dump della tabella nomi NetBIOS), `nmbscan` su Kali.
Questa sezione è essenzialmente il "come si sfrutta in pratica" della catena NetBIOS di cui abbiamo parlato — cioè cosa fai concretamente per estrarre informazioni da quel servizio chiacchierone sulla UDP 137. Ti spiego i pezzi.

`net view` è un comando built-in di Windows che sfrutta il browser service NetBIOS per elencare risorse. `net view /domain` ti dà la lista dei domini/workgroup visibili sulla rete; `net view /domain:nomedominio` scende dentro uno specifico dominio e ti elenca i server (le macchine) che ne fanno parte. È il primo passo di ricognizione: capire come è strutturata la rete Windows, quali raggruppamenti logici esistono e quali macchine ci sono dentro.

Il punto sul "NBNS normalmente funziona solo sul segmento locale, ma può essere instradato su TCP/IP" richiama quello che dicevamo sui broadcast: il meccanismo NetBIOS nasce per la rete locale (i broadcast non attraversano i router), ma incapsulandolo su TCP/IP — NetBIOS over TCP/IP, NBT — diventa raggiungibile e interrogabile anche da una macchina remota, il che è esattamente ciò che serve a un attaccante che non è fisicamente sulla stessa subnet.

Sui tool, la distinzione utile è per _granularità del bersaglio_:

`nltest` e `netdom` servono a trovare i domain controller — cioè le macchine chiave, quelle che ospitano AD e l'autenticazione. Individuarli è prezioso perché sono il bersaglio di più alto valore.

`netviewx` è più raffinato: cerca macchine che offrono _servizi specifici_, non solo la lista generica. Utile per filtrare "chi in questa rete fa X".

`nbtstat` interroga un _singolo sistema_ e ne estrae la tabella dei nomi NetBIOS — nome macchina, dominio/workgroup, e i "suffissi" che indicano quali ruoli/servizi quella macchina espone.

`nbtscan` è la versione su larga scala: fa la stessa cosa di nbtstat ma su un _intero range di indirizzi_ in un colpo solo, facendo il dump delle tabelle nomi di tutte le macchine che rispondono. È lo strumento da ricognizione di massa — lanci una subnet /24 e ti torna la mappa di chi c'è, con nomi e MAC address, come vedevi nello screenshot delle slide.

`nmbscan` è semplicemente l'equivalente disponibile su Kali Linux.

Sulle contromisure, il punto centrale è che tutte queste tecniche passano dalla stessa porta, UDP 137, quindi bloccarla (o restringerla a host fidati) taglia l'intera famiglia in un colpo. La disabilitazione dei servizi Alerter e Messenger è più specifica: quei due servizi facevano sì che comparissero _nomi utente_ nella tabella NetBIOS, quindi spegnerli riduce quanto un dump rivela. La nota finale è l'onesto trade-off che ritorna sempre in questo capitolo: bloccare la 137 rompe anche l'autenticazione dei nomi NBNS e alcune vecchie applicazioni che ci contano — cioè la sicurezza costa un po' di compatibilità, ed è il motivo per cui storicamente queste porte sono rimaste aperte più a lungo del dovuto.

Per legarlo al discorso di prima sul "legacy ma vivo": questi tool specifici sono in gran parte datati, ma il ruolo che svolgevano — mappare macchine, domini e servizi interrogando i protocolli di naming Windows — è esattamente ciò che oggi fai con strumenti moderni che interrogano DNS, LDAP e SMB. Cambia l'attrezzo, resta il concetto di battere la rete per costruire la mappa dei bersagli.

> [!warning] Contromisure NBNS 
> Bloccare UDP 137 al firewall o restringerlo a host specifici. Disabilitare i servizi Alerter e Messenger sui singoli host per evitare che i dati utente compaiano nei dump della tabella nomi NetBIOS. Bloccare UDP 137 disabilita anche l'autenticazione dei nomi NBNS e alcune applicazioni.

### NetBIOS Session, TCP 139 — [[Null Session]]

Ti ricostruisco la sezione con un'introduzione che spiega il _perché_ prima del _come_, poi un esempio commentato con output realistico.

Per l'introduzione, il concetto chiave da fissare è cosa sia davvero una null session. [[SMB]] (Server Message Block) è il protocollo con cui le macchine Windows condividono file, stampanti e comunicano tra loro per operazioni amministrative. Come ogni protocollo di condivisione, prima di darti accesso vuole sapere chi sei — normalmente ti autentichi con username e password. La null session è esattamente ciò che dice il nome: una sessione autenticata con credenziali _vuote_, utente nullo e password nulla. In pratica ti presenti al sistema dicendo "non sono nessuno", e sui sistemi vulnerabili (Windows NT e 2000) il sistema ti fa comunque entrare in una modalità anonima limitata — sufficiente però a fargli sputare una quantità imbarazzante di informazioni.

Il grimaldello specifico è una share speciale chiamata `IPC$` (Inter-Process Communication). Non è una cartella di file: è un canale nascosto pensato per la comunicazione tra processi e per le operazioni amministrative remote. Connettendoti anonimamente a `IPC$` apri un canale attraverso cui poi interrogare il sistema — chiedere la lista degli utenti, delle share, delle policy di password — senza aver mai fornito una credenziale valida. È questa la ragione per cui le null session sono "famigerate": trasformano un accesso anonimo in una miniera di intelligence sul bersaglio.

Ecco un esempio commentato di come si stabilisce e sfrutta, con output plausibile:

```
C:\> net view \\192.168.11.29
System error 5 has occurred.
Access is denied.
```

Primo tentativo diretto: negato. Senza autenticazione il sistema non mostra le risorse.

```
C:\> net use \\192.168.11.29\IPC$ "" /user:""
The command completed successfully.
```

Qui avviene il trucco: `net use` stabilisce la connessione alla share `IPC$` passando password vuota (`""`) e utente vuoto (`/user:""`). Il sistema accetta la sessione anonima.

```
C:\> net view \\192.168.11.29
Shared resources at \\192.168.11.29

Share name   Type   Used as  Comment
-------------------------------------------
NETLOGON     Disk            Logon server share
Test         Disk            Public test folder
Users        Disk
The command completed successfully.
```

Adesso lo stesso identico comando di prima funziona, perché la null session è aperta: il sistema rivela le share condivise, i loro nomi e i commenti (che a volte contengono indizi utilissimi, tipo "Backup finanza" o "Config router").

Da qui, con la sessione aperta, si passa agli strumenti di enumeration più profonda. Per esempio `enum` o DumpSec possono estrarre gli account:

```
C:\> enum -U 192.168.11.29
server: 192.168.11.29
setting up session... success.
getting user list (pass 1)... got 5.
  Administrator  Guest  krbtgt  mrossi  backup_svc
cleaning up... success.
```

Questa enumerazione è possibile se c'è RestrictAnonymous=0, ma se è impostata a 1, bisogna aggirarla. La coppia user2sid/sid2user permette di fare ciò e di scoprire il nome reale dell'Administrator anche se rinominato, giocando sul RID fisso 500:

```
C:\> user2sid \\192.168.202.33 "domain users"
S-1-5-21-8915387-1645822062-1819828000-513
...
C:\> sid2user \\192.168.202.33 5 21 8915387 1645822062 1819828000 500
Name is godzilla       ← l'Administrator è stato rinominato "godzilla",
Domain is ACME            ma il RID 500 lo tradisce
Type of SID is SidTypeUser
```

Il filo logico dell'intero attacco è: apri il canale anonimo via IPC$ → enumeri share, utenti e policy → identifichi l'account amministrativo reale via RID 500 → e ora hai un bersaglio preciso per la fase successiva (password guessing/brute force su un username che sai esistere davvero). Nota il collegamento con SMTP di prima: è sempre la stessa filosofia — ottenere una lista di account _validi_ per non tirare a indovinare.

**approfondimento importante per quanto riguarda user2sid/sid2user**
user2sid/sid2user e il RID cycling funzionano proprio _quando_ RestrictAnonymous è a 1, mentre l'enumerazione "diretta" degli utenti (chiedere gentilmente "dammi la lista utenti") è quella che richiede RestrictAnonymous a 0. Quindi non c'è nessun bypass nuovo introdotto da enum4linux — enum4linux automatizza esattamente la stessa tecnica user2sid/sid2user delle slide, che _già_ funzionava con RestrictAnonymous=1. Ricordavi invertito il rapporto.

Vale la pena capire _perché_ è così, perché è tutt'altro che ovvio ed è il cuore concettuale della cosa.

RestrictAnonymous controlla quanto un utente anonimo (la null session) può fare. Ma non è un interruttore unico "tutto o niente" — è a livelli, e la differenza tra livello 0 e livello 1 sta in _quali_ operazioni blocca:

Con **RestrictAnonymous = 0**, l'anonimo può fare l'enumeration diretta: esiste una chiamata SMB/RPC che dice sostanzialmente "elencami tutti gli utenti", e il sistema risponde con la lista completa. Facile, immediato, ma è proprio ciò che gli amministratori volevano bloccare.

Con **RestrictAnonymous = 1**, quella chiamata di enumerazione di massa viene bloccata: l'anonimo non può più dire "dammi la lista". _Ma_ — ed è qui il punto — resta aperta un'altra funzionalità, la traduzione nome↔SID (SID/Name translation). Questa non enumera niente: risponde solo a domande puntuali del tipo "qual è il SID di _questo_ nome?" o "qual è il nome dietro _questo_ SID?". Una domanda alla volta, mirata.

Ed è esattamente questa scappatoia che user2sid/sid2user (e quindi enum4linux col RID cycling) sfrutta. Il ragionamento è: se non posso chiedere la lista in blocco, aggiro il problema facendo _tante domande puntuali_. Prendo il prefisso di dominio (via user2sid su un nome che so esistere, come "domain users"), poi ciclo: "chi è il RID 500? chi è il 501? chi è il 1000? il 1001?"... una traduzione SID→nome alla volta. Ognuna è una richiesta lecita che RestrictAnonymous=1 non blocca, ma sommandole ricostruisco proprio quella lista utenti che il livello 1 pretendeva di proteggere.

In altre parole: RestrictAnonymous=1 chiude la porta grande dell'enumerazione di massa, ma lascia aperta la finestrella delle traduzioni singole, e il RID cycling passa dalla finestrella una richiesta per volta. È una falla concettuale nel livello 1 — protegge dal metodo ovvio ma non da quello paziente.

Ed è precisamente il motivo per cui le slide dicevano che la vera contromisura è **RestrictAnonymous = 2** (su Windows 2000 e successivi): il livello 2 è più restrittivo e chiude anche la SID/Name translation anonima, tappando la finestrella. Ma anche lì c'era l'avvertenza — impostare 2 può rompere applicazioni legittime che su quella traduzione anonima contavano, il solito trade-off sicurezza/compatibilità che attraversa tutto il capitolo.

Quindi per rispondere secco: non c'è un bypass moderno misterioso. enum4linux fa la stessa cosa delle slide, e "funziona con RestrictAnonymous=1" perché sfrutta la SID/Name translation, che il livello 1 non ha mai bloccato — solo il livello 2 lo fa.

**ma che cos'è "domain users" in users2sid?**
Buona domanda, perché è il pezzo che fa da grimaldello all'intero trucco e nell'esempio passa un po' sotto silenzio.

`"domain users"` è il nome di un **gruppo** predefinito di Windows — è il gruppo a cui appartengono automaticamente tutti gli account utente di un dominio. È un gruppo che esiste sempre, con quel nome standard, su qualsiasi dominio Windows. E questo è esattamente il motivo per cui viene usato qui.

Il problema che l'attaccante deve risolvere è: per usare `sid2user` e chiedere "chi ha il RID 500?", gli serve prima conoscere la parte iniziale del SID — quel lungo numero `S-1-5-21-8915387-1645822062-1819828000` che identifica _il dominio stesso_. Quella parte è unica per ogni dominio e non la conosce in anticipo. Gli serve un modo per estrarla.

Ed ecco il trucco in due mosse:

Nella prima riga, `user2sid` chiede "dammi il SID del gruppo `domain users`". Lo usa proprio perché è un nome che _sa con certezza esistere_ — è standard, c'è su ogni dominio, quindi la query funziona sempre. La risposta è `S-1-5-21-8915387-1645822062-1819828000-513`. Il `513` finale è il RID fisso del gruppo "Domain Users", ma la parte che interessa davvero all'attaccante è tutto ciò che sta _prima_: `S-1-5-21-8915387-1645822062-1819828000`, cioè l'identificatore del dominio. Ora ce l'ha.

Nella seconda riga, `sid2user` fa il percorso inverso: prende quel prefisso di dominio appena scoperto e ci attacca il RID `500` (Administrator), chiedendo "chi è l'account con _questo_ SID completo?". Il sistema risponde col nome reale — `godzilla` — anche se l'Administrator è stato rinominato per nasconderlo.

Quindi `domain users` non è il bersaglio: è solo il **punto d'appoggio noto** per estrarre il prefisso del dominio. Serve un nome che esista sicuramente per fare la prima traduzione nome→SID; una volta ottenuto il prefisso, si costruiscono a tavolino i SID degli account interessanti (500 per Administrator, 501 per Guest, ecc.) e si fa la traduzione inversa SID→nome. È l'equivalente di scoprire il prefisso telefonico di un'azienda partendo da un numero pubblico qualsiasi, per poi comporre gli interni che ti interessano.

**Quindi SBM si connette ad una macchina specifica inserendo banalmetne id e password e l'indirizzo ip target. Questo mi fa capire che non è necessario che sia legato ad una [[Active Directory (AD)]]**
Sì, la tua osservazione è corretta, e coglie una distinzione importante che vale la pena rendere esplicita.

SMB di per sé è un protocollo di condivisione file/risorse tra macchine, e non è intrinsecamente legato ad Active Directory. Nell'esempio delle slide stai facendo esattamente quello che descrivi: ti connetti a una _singola macchina specifica_ (`192.168.202.33`) con delle credenziali — nel caso della null session, credenziali vuote — e accedi alle share di _quella macchina_. È un rapporto uno-a-uno tra te e quell'host. Non c'è nessun dominio di mezzo, nessun domain controller: è pura condivisione SMB locale a quella macchina, che funziona anche su un Windows completamente standalone, fuori da qualsiasi dominio.

La distinzione da tenere è tra i due mondi in cui SMB può operare:

Nel caso _workgroup / standalone_ (quello delle slide), ogni macchina ha i propri account locali, e ti autentichi contro il database utenti _di quella specifica macchina_. Le share che vedi sono le sue, gli utenti che enumeri sono quelli locali suoi. Tutto self-contained.

Nel caso _dominio Active Directory_, SMB si appoggia ad AD per l'autenticazione — ti autentichi con un account di dominio e quello ti dà accesso alle share sulle varie macchine del dominio. Qui AD entra in gioco, ma come _fornitore di identità_, non come parte di SMB stesso.

Quindi hai ragione a scorporare le due cose: SMB è il protocollo di accesso alle risorse, AD è (eventualmente) il sistema di identità che gli sta dietro. Sono ortogonali. La confusione nasce dal fatto che nelle reti aziendali reali li trovi quasi sempre insieme, ma concettualmente — e nell'esempio didattico delle slide — SMB fa il suo lavoro anche completamente da solo, host per host, come stai vedendo tu.

Un dettaglio che chiude il cerchio: il motivo per cui la null session era così ghiotta è proprio che dava accesso anonimo a questo canale _senza_ passare da nessuna identità, né locale né di dominio. Bypassava del tutto la domanda "chi sei", ed è per questo che è stata chiusa di default da XP in poi.

**Quindi potenzialmente SBM potrebbe usare due metodi di autenticazione alternativi: locale oppure attraverso AD**
Esatto.
Dipende da _dove_ vivono gli account, e ci sono due database possibili, non uno solo:

Se la macchina è **standalone / in workgroup**, gli account stanno nel database _locale_ di quella macchina — si chiama SAM (Security Accounts Manager), ed è un file locale sulla macchina stessa. In questo caso non c'è nessun domain controller coinvolto: ti autentichi contro gli utenti locali di _quella_ macchina. L'esempio delle slide con `192.168.202.33` è tipicamente questo scenario — è la macchina stessa che verifica le credenziali, contro il proprio SAM.

Se la macchina è **membro di un dominio Active Directory**, allora sì, gli account di dominio stanno nel database del domain controller, e l'autenticazione viene validata contro quello.

Quindi la risposta secca è: l'utente deve esistere _in un_ database di account, ma quale database dipende dal contesto. Standalone → SAM locale della macchina. Dominio → directory del controller. Non è sempre il controller.

Anzi, spesso convivono entrambi sulla stessa macchina: un PC in dominio ha _sia_ i suoi account locali nel SAM (l'Administrator locale, per esempio) _sia_ la possibilità di autenticare account di dominio. Quando ti connetti via SMB puoi puntare all'uno o all'altro a seconda di come specifichi l'utente — `\\host\risorsa /user:MACCHINA\admin` (account locale) contro `/user:DOMINIO\utente` (account di dominio).

E per chiudere il collegamento con la null session: il motivo per cui era speciale è che _non_ richiedeva un utente in _nessuno_ dei due database. L'accesso anonimo scavalcava del tutto la verifica — né SAM locale né controller. Era esattamente questa la falla: un canale che ti faceva entrare senza corrispondere ad alcun account reale da nessuna parte.

#### Enum4Linux - unico tool non deprecato praticamente

Vero, hai colto nel segno — è ironicamente lo strumento più vivo di tutta la lista, anche se fa esattamente le cose vecchie di cui stiamo parlando. Lascia che verifichi lo stato attuale, perché è proprio il tipo di cosa dove la mia conoscenza potrebbe essere datata.Confermato che è vivo e vegeto — anzi, c'è pure la versione riscritta enum4linux-ng ancora aggiornata (l'ultima release è recente). Ti spiego cos'è e perché sopravvive dove gli altri sono morti.

Il punto centrale, che è anche la battuta implicita nella tua osservazione: enum4linux non è uno strumento _nuovo_ che fa cose nuove. È un wrapper — un unico comando comodo che sotto il cofano chiama quattro tool della suite Samba: `smbclient`, `rpcclient`, `net` e `nmblookup`. Tu lanci un solo comando e lui esegue tutta la batteria di interrogazioni SMB/NetBIOS che nelle slide vedi sparse tra dieci tool Windows diversi (nbtstat, user2sid, DumpSec, net view...), raccogliendo tutto in un output unico. In pratica è la versione Linux, consolidata e automatizzata, di tutto il capitolo che stai studiando.

Ed è proprio questa la ragione per cui non è deprecato mentre epdump e Winfingerprint lo sono: enum4linux è vecchio come _codice_ (scritto in Perl nel 2011 da Mark Lowe), ma i _protocolli_ che interroga — SMB e le sue interfacce RPC per l'enumeration — sono ancora quelli usati oggi. Finché Windows parla SMB, e lo parla ancora, lo strumento resta valido. Gira su Linux (Kali/Parrot lo hanno preinstallato), che è il motivo del "4linux": porta l'enumeration SMB dal lato attaccante Linux, senza bisogno di una macchina Windows.

Cosa estrae, in un colpo solo: enumerazione utenti locali e di dominio con i loro RID, enumeration delle share SMB, informazioni su OS e dominio, RID cycling e le impostazioni di password policy. Riconoscerai ogni singola voce dal capitolo — sono esattamente le stesse cose delle null session, solo raccolte automaticamente.

Il collegamento diretto con quello che abbiamo appena discusso è il **RID cycling**, che è la generalizzazione automatica del trucco user2sid/sid2user che hai appena capito. Invece di fare a mano "prendi il prefisso di dominio, attacca il RID 500, traduci", enum4linux cicla su un intervallo di RID (di default 500-550 e 1000-1050) e traduce ognuno in nome utente. Parte dal RID 500 (Administrator), passa per 501 (Guest), poi 1000, 1001... e ti costruisce la lista completa degli account. Il RID cycling estrae la lista utenti anche da host con RestrictAnonymous impostato a 1 — cioè bypassa esattamente la contromisura che le slide citano, con lo stesso meccanismo che ti ho spiegato prima.

Un esempio d'uso tipico. Il comando che troverai ovunque è la "full sweep":

```
enum4linux -a 192.168.11.29
```

dove `-a` significa "aggressive / tutto" — fa NetBIOS lookup, enumera utenti, gruppi, share, policy password e OS. Con credenziali (se ne hai) si aggiunge `-u utente -p password`. L'output, semplificato, ha una struttura a sezioni tipo:

```
[+] Got domain/workgroup name: ACME
 ============================
|    Users on 192.168.11.29  |
 ============================
user:[administrator] rid:[0x1f4]
user:[guest] rid:[0x1f5]
user:[backup_svc] rid:[0x3e8]

 ============================
|   Share Enumeration        |
 ============================
	Sharename   Type   Comment
	IPC$        IPC    Remote IPC
	NETLOGON    Disk   Logon server share
	Users       Disk

[+] Password Info for Domain: ACME
	Minimum password length: 7
	Account lockout threshold: none
```

Nota `rid:[0x1f4]` — è 500 in esadecimale, cioè l'Administrator, che salta fuori col suo RID fisso esattamente come nel discorso di prima. E `lockout threshold: none` è un'informazione d'oro per la fase successiva: se non c'è blocco account dopo tot tentativi falliti, puoi fare password spraying/brute force senza rischiare di bloccare gli account e farti notare.

Su cosa lo ha superato oggi, per completezza intellettuale: nei workflow moderni molti usano `netexec` (l'ex-CrackMapExec) o gli script [[Impacket]] (`samrdump.py`, `lookupsids.py`) perché danno subito una quantità di informazioni sull'host — hostname, dominio, versione OS, versione SMB e se il signing è abilitato e si integrano meglio in catene di attacco. Ma enum4linux resta il primo colpo di ricognizione SMB per antonomasia, specialmente in ambito didattico e CTF, proprio perché mette in fila in modo leggibile tutti i concetti che stai studiando.

Quindi la tua battuta è più profonda di quanto sembri: enum4linux è "non deprecato" precisamente perché è l'unico della lista che sta dal lato giusto della barricata — attacca i protocolli, non incarna i tool obsoleti — e quei protocolli SMB sono rimasti. È il ponte perfetto tra il capitolo storico che hai davanti e la pratica attuale.

#### Informazioni dalle slide:

> [!info] Le famigerate null session 
> Il protocollo [[SMB]] (Server Message Block) di Windows fornisce gratuitamente una grande quantità di informazioni. Le null session sono disattivate di default da Windows XP in poi, ma erano aperte in Windows 2000 e NT (non disponibili in Win 95/98/Me).

> [!example] Stabilire una null session
> 
> ```
> net use \\192.168.11.29\IPC$ "" /user:""
> net view \\192.168.11.29
> ```
> 
> Dopo l'autenticazione anonima via IPC$, `net view` rivela le risorse condivise (share name, tipo, commento).

> [!info] Informazioni esposte 
> Su Win 2000/NT le null session danno accesso a: share, account utente, policy delle password. DumpSec (free) le enumera insieme a permessi sui file e servizi.

> [!info] Registry remoto 
> Il registry può essere letto da remoto con `reg` (built-in Microsoft) o DumpSec, ma richiede privilegi di Administrator di default sui server Windows — non è ottenibile con una semplice null session. Nota storica: Gary McKinnon usò l'accesso remoto al registry per violare reti del Pentagono.

> [!info] SID e RID 
> Il SID (Security Identifier) è un identificatore unico e immutabile di un principal di sicurezza (utente, gruppo...), nel formato `S-1-5-21-...-RID`. Il RID (Relative Identifier) è la parte finale: 500 = Administrator, 501 = Guest, 1000+ = account creati successivamente. Cambiando le ultime cifre del SID di un altro account a 500 si può tentare di mappare l'account Administrator anche se rinominato.

> [!example] user2sid / sid2user 
> Recuperano nomi account e SID da remoto anche con `RestrictAnonymous` impostato a 1, trovando l'account Administrator anche se rinominato. Funzionano sulla famiglia NT, non su Windows XP SP2.
> 
> ```
> user2sid \\192.168.202.33 "domain users"
> sid2user \\192.168.202.33 5 21 ... 500
> ```

> [!tip] Tool all-in-one per null session 
> Winfingerprint (anche via Active Directory e WMI), Winfo, NBTEnum 3.3 — recuperano in un colpo solo info di sistema, dominio, password policy, sessioni e utenti loggati.

> [!warning] Contromisure SMB/null session 
> Bloccare TCP 139 e 445 al perimetro di rete. Impostare la chiave di registro `RestrictAnonymous` a 1 (o 2 su Win 2000+) in `HKLM\SYSTEM\CurrentControlSet\Control\LSA` — bypassabile però interrogando l'API `NetUserGetInfo` a livello 3 (NBTEnum e Userinfo lo fanno). Le impostazioni di accesso anonimo non si applicano all'accesso remoto al registry: va bloccato separatamente (vedi KB153183). Auditarsi con DumpSec.

### [[SNMP]], UDP 161

SNMP è un protocollo che vale la pena capire bene perché il concetto è elegante e il modello di sicurezza originale è così debole da essere quasi comico — da cui la battuta "Security Not My Problem". Andiamo pezzo per pezzo.

**Cos'è SNMP e a cosa serve**

SNMP (Simple Network Management Protocol) nasce per un problema pratico: in una rete grande hai centinaia di dispositivi — router, switch, stampanti, server — e un amministratore non può controllarli uno per uno fisicamente. Serve un modo standard per interrogarli e configurarli da remoto, tutti con lo stesso linguaggio. SNMP è questo linguaggio comune.

Il modello ha due lati. Da una parte c'è l'**agent**: un piccolo software che gira sul dispositivo gestito (il router, la stampante) e che espone informazioni su di sé e accetta comandi. Dall'altra c'è il **manager**: la console dell'amministratore, che interroga gli agent e riceve le loro risposte. L'agent ascolta sulla UDP 161. L'amministratore chiede "quanto traffico è passato su questa interfaccia?", "qual è la temperatura?", "riavviati", e l'agent risponde o esegue.

Il problema di sicurezza è che questo canale, pensato per gli amministratori, risponde a _chiunque_ sappia la parola d'ordine giusta — e la parola d'ordine è spesso banale, come vedremo.

**Le community string**

Qui sta la debolezza centrale. Il "sistema di autenticazione" di SNMP (nelle versioni v1 e v2, quelle storiche) è una singola stringa di testo chiamata **community string**, che funziona come una password condivisa. Se la conosci, hai accesso; se non la conosci, no. Punto. Non c'è username, non c'è utente individuale, non c'è nulla di più.

Ci sono due tipi che contano (il terzo, Trap, serve ai messaggi che l'agent manda spontaneamente al manager, e si usa poco):

La community string **Read-Only** ti permette di _leggere_ le informazioni dal dispositivo — interrogarlo, fare enumeration. È già abbastanza pericolosa perché rivela moltissimo.

La community string **Read-Write** ti permette anche di _modificare_ la configurazione del dispositivo. Questa è devastante: chi ce l'ha può riconfigurare un router, spegnerlo, deviare traffico.

Il disastro pratico è che queste stringhe sono lasciate quasi sempre ai valori di default di fabbrica: **"public"** per la lettura e **"private"** per la scrittura. Sono così universali che provarle è la prima cosa che fa chiunque. In più, dato che in SNMP v1/v2 la community string viaggia **in chiaro** sulla rete, un attaccante che riesce a sniffare il traffico con Wireshark la legge direttamente dai pacchetti, senza nemmeno doverla indovinare.

**Il MIB (Management Information Base)**

Se la community string è la chiave, il MIB è la stanza a cui la chiave dà accesso. Il MIB è il modo in cui i dati del dispositivo sono organizzati: una **struttura ad albero**, esattamente come il registro di Windows o come un filesystem con cartelle e sottocartelle. Ogni informazione che il dispositivo espone (numero di interfacce, nomi utente, tabelle di routing, servizi attivi) sta in un punto preciso di questo albero.

Ogni "foglia" dell'albero ha un indirizzo numerico chiamato **OID** (Object Identifier), che è quella sequenza puntata che vedi nell'esempio: `.1.3.6.1.4.1.77.1.2.25`. Leggilo come un percorso in un filesystem: `1.3.6.1` è la radice standard di Internet, poi si scende ramo per ramo fino ad arrivare al dato specifico. Ogni numero è un bivio nell'albero. Quindi un OID è semplicemente "il percorso per arrivare a questa specifica informazione dentro il MIB".

Il punto critico per l'enumeration è che i **vendor aggiungono i propri rami** al MIB standard. E qui Microsoft ha fatto un regalo agli attaccanti: memorizza i **nomi degli account utente Windows** dentro un ramo del MIB. Quindi se un sistema Windows ha l'agent SNMP attivo con community string "public", puoi camminare in quel ramo e leggere la lista degli utenti — la solita lista di account validi che insegue tutto il capitolo, ottenuta stavolta da un canale completamente diverso.

**Cosa si ottiene e con quali tool**

Camminando nel MIB si estraggono: servizi in esecuzione, nomi e percorsi delle share, commenti sulle share, username, nome del dominio — di nuovo la mappa completa del sistema.

L'operazione chiave si chiama **walk**: invece di chiedere un singolo OID (`snmpget`), il "walk" (`snmpwalk`) percorre automaticamente un intero ramo dell'albero dall'inizio alla fine, sputando fuori tutto ciò che contiene. È come dire "dammi ricorsivamente tutto quello che c'è sotto questa cartella". Nell'esempio:

```
snmputil walk 192.168.202.33 public .1.3.6.1.4.1.77.1.2.25
```

si legge come: cammina (`walk`) sul dispositivo `192.168.202.33`, usando la community string `public`, partendo dal ramo `.1.3.6.1.4.1.77.1.2.25` (che è il ramo dove Microsoft tiene gli username). Il risultato è la lista: Guest, Administrator, ecc. I tool sono `snmputil` (vecchio, Windows), `snmpget`/`snmpwalk` (suite net-snmp su Linux, ancora attualissimi), e IP Network Browser di Solarwinds per chi vuole un'interfaccia grafica.

**I rischi oltre l'enumeration**
Fin qui abbiamo parlato di _leggere_ (community Read-Only). Ma se un attaccante indovina o sniffa la community string di **scrittura** (la "private"), il gioco cambia da spionaggio a controllo. Con accesso in scrittura sul MIB di un router puoi modificarne la configurazione: causare un **DoS** (spegnere interfacce, deviare traffico, mandare in tilt il dispositivo), oppure — il classico su apparati Cisco — **copiare l'intera configurazione del router** su un server TFTP che controlli tu (è quello che fa il tool `copy-router-config.pl`). Una volta che hai il file di configurazione, contiene le password del dispositivo, spesso protette solo da codifiche deboli e reversibili, quindi le **decodifichi** e ottieni le credenziali vere. Da semplice enumeration sei arrivato al pieno controllo dell'infrastruttura di rete.

**Le contromisure**

Seguono direttamente dalle debolezze. Disabilitare gli agent SNMP dove non servono (se un dispositivo non ha bisogno di essere gestito via SNMP, l'agent è solo superficie d'attacco). Cambiare le community string dai default ovvi — non lasciare mai "public"/"private". Bloccare la porta 161 al perimetro, così l'agent non è raggiungibile da Internet. Restringere l'accesso agli agent ai soli IP delle console di management legittime (se solo l'IP dell'amministratore può parlare con l'agent, sniffare la stringa da fuori non basta). E soprattutto usare **SNMP v3**, che è la vera soluzione strutturale: a differenza di v1/v2 introduce autenticazione vera (utenti con credenziali, non una stringa condivisa) e **cifratura** del traffico, il che chiude sia il problema del default ovvio sia quello dello sniffing in chiaro.

Il filo conduttore da portare a casa: SNMP v1/v2 è un canale potentissimo — legge dati sensibili e può riconfigurare hardware — protetto da un'unica password condivisa, spesso di default, trasmessa in chiaro. È il motivo del soprannome, ed è il motivo per cui, come per NetBIOS, il concetto resta rilevante anche se i tool specifici sono datati: trovi ancora oggi apparati con "public" attivo, e `snmpwalk` è tuttora nel kit di ogni pentester.

**Perché è così poco nominato**
Non è affatto strano, ed è una reazione sensata — c'è una ragione precisa per cui SNMP resta invisibile a chi non fa amministrazione di rete o security.

SNMP vive interamente sul lato _gestione_ dell'infrastruttura, che è un piano separato da tutto ciò con cui interagisci normalmente. Quando usi un computer navighi, mandi email, usi applicazioni — tutto traffico "dati". SNMP invece è il canale con cui gli apparati vengono _monitorati e configurati_ dietro le quinte: lo parlano i router, gli switch, le stampanti di rete, i gruppi di continuità, i sistemi di monitoraggio tipo Nagios/Zabbix/PRTG che in un'azienda tengono d'occhio lo stato di centinaia di dispositivi. È roba che gira in sala macchine, non sulla scrivania. Se non hai gestito una rete aziendale o configurato apparati, semplicemente non hai avuto occasione di incrociarlo.

C'è anche un motivo "generazionale": SNMP è un protocollo anni '80-'90, nato in un mondo dove la rete era un ambiente fidato e chiuso. Oggi molti sistemi di monitoraggio moderni usano altri meccanismi (agent proprietari, API REST, protocolli come gRPC/telemetry sui dispositivi più nuovi), quindi anche chi entra ora nel campo può vederlo meno di quanto lo si vedeva vent'anni fa. È ancora ovunque negli apparati esistenti, ma non è più il protagonista scintillante.

E c'è la ragione più banale ma vera: è un argomento _noioso_. Il monitoraggio di rete non ha il fascino della crittografia o dell'exploitation; è "plumbing", tubature. Nei percorsi di computer science raramente lo si incontra, a meno di un corso specifico di reti o di amministrazione di sistemi — ed è proprio per questo che salta fuori in un corso di ethical hacking, dove lo guardi non come strumento di gestione ma come _superficie d'attacco_. Il che, ironicamente, è il modo più interessante per conoscerlo: lo incontri per la prima volta proprio nel momento in cui scopri che quel canale amministrativo sonnacchioso regala username e configurazioni a chiunque conosca la parola "public".

Quindi non è una lacuna tua — è che SNMP sta in una nicchia (network/sysadmin, security) che non intercetti finché non ci finisci dentro apposta. Il fatto che tu lo stia vedendo ora, dal lato offensivo, è in realtà uno degli angoli migliori da cui approcciarlo.

> [!info] "Security Not My Problem" 
> Pensato per gestione e monitoraggio di rete, fornisce informazioni interne su dispositivi, software e sistemi — usato dagli amministratori per gestire router e altri dispositivi da remoto.

> [!info] Community string 
> Il sistema di sicurezza minimale di SNMP: stringhe che fungono da password. Tre tipi: Read-Only, Read-Write, Trap (raramente usata). Spesso lasciate ai valori di default ovvi come "public" e "private". Gli attaccanti spesso le intercettano con Wireshark via packet inspection.

> [!info] MIB (Management Information Base) 
> Contiene i dati di un dispositivo SNMP in forma ad albero, come il registro di Windows. I vendor aggiungono dati al MIB; Microsoft vi memorizza i nomi degli account utente Windows.

> [!example] Dati ottenibili via SNMP 
> Servizi attivi, nomi e percorsi delle share, commenti sulle share, username, nome del dominio. Tool: `snmputil` (Windows NT Resource Kit), `snmpget`/`snmpwalk` (suite netsnmp su Linux), IP Network Browser (tool grafico Solarwinds).
> 
> ```
> snmputil walk 192.168.202.33 public .1.3.6.1.4.1.77.1.2.25
> → svUserName: Guest, Administrator
> ```

> [!warning] Rischi oltre l'enumeration 
> Indovinare la community string in scrittura (es. "private") permette il controllo remoto dei dispositivi di rete: attacchi DoS, oppure su reti Cisco copiare la configurazione su un server TFTP (tool `copy-router-config.pl`) e decodificarne le password.

> [!warning] Contromisure SNMP 
> Rimuovere o disabilitare gli agent SNMP non necessari. Cambiare le community string dai valori di default. Bloccare le porte TCP/UDP 161 (GET/SET) al perimetro di rete. Restringere l'accesso agli agent SNMP ai soli IP della console di management. Usare SNMP v3 (cifratura e autenticazione molto più solide di v1/v2). Modificare le chiavi di registro NT per renderlo meno pericoloso.

### [[BGP]], TCP 179

BGP è uno di quei protocolli che regge letteralmente Internet ma che quasi nessuno vede, quindi vale la pena capire prima _cosa fa_ e poi perché compare in un capitolo di enumeration. Ti costruisco il quadro dal basso.

**Cos'è un Autonomous System**
Internet non è una rete unica: è un insieme di tante reti separate che si interconnettono. Ognuna di queste grandi reti — gestita da una singola entità con una propria politica di routing — è un **Autonomous System (AS)**. Un provider come TIM è un AS, Google è un AS, una grande università o una multinazionale può essere un AS. Pensa a un AS come a un "territorio" della rete sotto un unico controllo amministrativo.

Ogni AS ha un identificatore numerico univoco a livello mondiale, l'**ASN** (Autonomous System Number). È esattamente l'analogia che fa la nota: come un indirizzo IP identifica univocamente una macchina, un ASN identifica univocamente un'organizzazione-rete. Sono assegnati dalle stesse autorità che gestiscono gli IP (i Regional Internet Registry), quindi sono pubblici e tracciabili.

**Cosa fa BGP**
Il problema che [[BGP]] risolve è: come fa il traffico a trovare la strada _tra_ questi territori? Dentro un AS ci sono protocolli di routing interni, ma tra AS diversi serve qualcosa che coordini "per raggiungere le reti dell'AS X, passa di qui". Questo è il **Border Gateway Protocol**: il protocollo con cui gli AS si annunciano a vicenda quali blocchi di indirizzi IP controllano e attraverso quali percorsi sono raggiungibili. È il "de facto" perché non c'è alternativa reale — è _il_ linguaggio con cui i confini di Internet si parlano.

Un'organizzazione usa BGP quando ha più **uplink**, cioè più connessioni verso l'esterno (magari verso due provider diversi, per ridondanza). Con un solo uplink non serve: mandi tutto da quell'unica parte. Con più uplink devi decidere e annunciare quale traffico entra ed esce da quale connessione, e BGP è ciò che rende possibile questa scelta. Per questo la presenza di un proprio ASN + BGP è un segnale che stai guardando un'organizzazione di una certa dimensione, con infrastruttura di rete seria.

**Perché sta in un capitolo di enumeration**
Qui arriva il punto offensivo, ed è più sottile degli altri servizi del capitolo. Tutti gli altri (SNMP, SMB, NetBIOS) sono cose che _interroghi attivamente_ su una macchina target. BGP invece lo sfrutti per **ricognizione passiva sulla scala dell'intera azienda**, non della singola macchina.

Il ragionamento è: gli annunci BGP sono pubblici per natura — devono esserlo, perché tutto Internet deve sapere quali reti appartengono a chi per instradare il traffico. Queste informazioni sono raccolte e consultabili (tramite i database dei Regional Internet Registry, servizi di **looking glass**, siti come bgp.he.net). Quindi, partendo dal nome di un'azienda, puoi risalire al suo ASN, e dall'ASN ottenere la **lista completa di tutti i blocchi di indirizzi IP che quell'azienda controlla e annuncia**.

Il valore per un attaccante è che questo definisce la **superficie d'attacco** a livello macro. Invece di sapere "l'azienda ha un server a questo IP", scopri "l'azienda possiede questi 15 blocchi /24, ecco tutte le sue reti pubbliche". Ora sai _dove guardare_ — quali range scansionare con nmap nelle fasi successive. È l'enumeration più a monte di tutte: prima ancora di toccare una singola macchina, disegni la mappa di tutto il territorio del bersaglio.

**Perché "non esiste contromisura"**
Questa è l'affermazione più interessante della nota, e va capita bene perché è vera solo in un senso preciso. BGP non può essere "bloccato" come blocchi la porta 161 di SNMP, per una ragione strutturale: gli annunci BGP _devono_ essere pubblici perché Internet funzioni. Se nascondessi quali reti controlli, il traffico non saprebbe come raggiungerti — smetteresti di essere su Internet. La pubblicità di quelle informazioni non è un bug da correggere, è il meccanismo stesso su cui si regge il routing globale.

Quindi la relazione tra l'azienda e questa esposizione è ineliminabile: non puoi avere reti pubbliche raggiungibili _e_ nascondere quali reti possiedi. Sono la stessa cosa vista da due lati.

Una precisazione onesta, però, perché "nessuna contromisura" è vero solo per _questo specifico aspetto_ (l'enumeration dei tuoi range via ASN). BGP come protocollo ha eccome problemi di sicurezza su cui esistono difese — il **BGP hijacking**, per esempio, in cui un AS malevolo annuncia falsamente di controllare reti altrui per dirottare traffico, e contro cui si sono sviluppati meccanismi come RPKI per validare gli annunci. Ma quello è un attacco _contro_ il routing, diverso dall'uso di BGP _per enumerare_. La nota parla del secondo: quello, essendo solo lettura di informazioni pubbliche per definizione, non si può impedire.

Il concetto da portare via: BGP è l'unico "servizio" del capitolo che non attacchi ma _consulti_, e ti dà la vista dall'alto — la mappa completa delle reti di un'organizzazione — sfruttando informazioni che devono restare pubbliche per far funzionare Internet. È reconnaissance a costo zero e senza toccare il bersaglio, il che lo rende anche invisibile: l'azienda non può nemmeno accorgersi che qualcuno ha guardato.

> [!info] Routing tra Autonomous System 
> Il Border Gateway Protocol è il protocollo di routing de facto tra Autonomous System; le organizzazioni con più uplink lo usano. Ogni AS è identificato da un AS-Number (ASN), univoco come un IP per organizzazioni grandi. BGP può essere usato per enumerare tutte le reti di una determinata azienda (tramite il suo ASN) — utile per ampliare i bersagli. Non esiste contromisura: BGP non può essere bloccato.

### [[Active Directory (AD)]] [[LDAP]], TCP/UDP 389 e 3268
Questo pezzo chiude il capitolo e vale la pena capirlo bene perché lega insieme diverse cose che hai già visto — AD, LDAP, l'enumeration di utenti — e le porta al loro livello più strutturato. Ti costruisco il quadro.

**Cos'è LDAP e come si lega ad Active Directory**
Riprendiamo un filo di prima. Avevamo detto che Active Directory è il database gerarchico degli oggetti aziendali: utenti, gruppi, computer, ognuno con i suoi attributi. **LDAP** (Lightweight Directory Access Protocol) è il _protocollo_ con cui si interroga quel database. La distinzione è la stessa che c'è tra un database e il linguaggio con cui gli fai le query: AD è il contenitore, LDAP è il modo standard per chiedergli le cose.

LDAP non è un'invenzione Microsoft — è uno standard aperto per interrogare qualsiasi directory service (anche OpenLDAP su Linux lo usa). Active Directory lo adotta come interfaccia principale di accesso. Quindi quando qualcosa vuole sapere "chi sono gli utenti del gruppo Amministratori?" o "qual è l'email di Mario Rossi?", pone la domanda in LDAP al domain controller, che risponde attingendo ad AD.

Le due porte che vedi hanno un significato preciso. La **389** è LDAP standard, e serve le query relative a un singolo dominio. La **3268** è il **Global Catalog**: in una foresta AD con più domini, il Global Catalog è un indice che contiene una versione parziale di _tutti_ gli oggetti di _tutti_ i domini della foresta. Serve per le ricerche che devono attraversare l'intera organizzazione, non solo un dominio. Semplificando: 389 = "chiedi a questo dominio", 3268 = "cerca in tutta la foresta".

**Perché è il bersaglio d'enumeration più ricco**
Qui sta il punto. Tutto il capitolo insegue la lista degli account validi, e l'hai vista ottenere da SMTP (VRFY), da SMB (null session, RID cycling), da SNMP (il ramo del MIB). LDAP su AD è la versione _definitiva_ di questo, perché non stai grattando informazioni da un canale laterale — stai interrogando direttamente la fonte autoritativa, il database che _contiene_ tutto.

Se riesci a interrogare LDAP, non ottieni solo i nomi utente: ottieni la struttura organizzativa completa. Utenti con tutti i loro attributi (nomi, email, descrizioni, a volte perfino password in campi mal configurati), gruppi e chi ne fa parte, computer del dominio, le unità organizzative che riflettono la struttura dei reparti, le policy. È la mappa completa dell'organizzazione Windows, non un frammento. Per un attaccante è il jackpot della fase di enumeration.

**Il problema della compatibilità legacy**
La frase chiave della nota è quella sulla compatibilità con versioni precedenti, ed è lo stesso identico meccanismo che hai visto con NetBIOS e con RestrictAnonymous — un pattern che ormai riconosci: _la retrocompatibilità apre buchi_.

Windows 2000 introdusse Active Directory. Ma molte aziende avevano ancora domini basati su Windows NT4, il sistema precedente, che gestiva utenti in modo più primitivo. Per non costringere tutti a migrare di colpo, Microsoft permise di far girare un dominio AD in una **modalità mista / legacy-compatible**, in cui il dominio "parla anche NT4" per convivere con domain controller e client vecchi.

Il prezzo di questa compatibilità è che il dominio si comporta secondo le regole di sicurezza più permissive del vecchio mondo. In pratica, come dice la nota, in modalità legacy-compatible _qualsiasi membro del dominio_ — e in certe configurazioni anche accessi con privilegi minimi o anonimi — può enumerare l'intero Active Directory via LDAP. Le protezioni più fini introdotte con AD non vengono applicate pienamente, perché devono restare compatibili con NT4 che quelle protezioni non le aveva. Lo strumento Microsoft `ldp.exe` è semplicemente un client LDAP grafico che permette di connettersi e sfogliare la directory in questo modo.

**Le contromisure**
Seguono direttamente dai due problemi. Sul lato rete: **filtrare le porte 389 e 3268 al perimetro**, così un attaccante esterno non può raggiungere il servizio LDAP del domain controller da Internet. LDAP dovrebbe essere raggiungibile solo dall'interno della rete aziendale, mai esposto fuori — un domain controller con la 389 aperta verso Internet è un errore grave.

Sul lato configurazione: usare domini in modalità **"Native"** (Windows 2000 e successivi) invece che mista, ed **evitare i domain controller NT4**. Passare a Native significa dire "non ho più bisogno di parlare NT4, applica tutte le regole di sicurezza moderne di AD". È l'equivalente esatto di impostare RestrictAnonymous a 2 invece di 1: chiudi la scappatoia rinunciando alla compatibilità col passato. E come sempre, il trade-off è proprio quello — puoi farlo solo quando non hai più sistemi legacy che dipendono dalla vecchia modalità.

**Il filo che chiude il capitolo**
Vale la pena notare, per legare tutto: le porte 389/3268 di [[LDAP]] sono la controparte "moderna e strutturata" delle porte 137/139 di NetBIOS che hai visto all'inizio. Entrambe espongono la stessa preda — utenti, gruppi, struttura del dominio — ma NetBIOS è il canale vecchio, piatto e chiacchierone, mentre LDAP è quello nuovo, gerarchico e autoritativo. È il motivo per cui, come dicevamo parlando dei tool moderni, oggi l'enumeration di AD si fa via LDAP e [[SMB]] (con strumenti come enum4linux-ng che controlla proprio se LDAP è raggiungibile, o [[BloodHound]] che mappa le relazioni AD via LDAP), mentre i vecchi tool NetBIOS del capitolo sono l'antenato storico della stessa attività. Stessa preda, canale evoluto.

> [!info] Cosa contiene 
> Active Directory contiene tutti gli account utente, gruppi e altre informazioni sui domain controller Windows. Se il dominio è reso compatibile con versioni precedenti (es. Win NT4 Server), qualsiasi membro del dominio può enumerare l'intero Active Directory. Tool Microsoft: `ldp.exe`.

> [!warning] Contromisure AD/LDAP 
> Filtrare l'accesso alle porte 389 e 3268 ai dispositivi perimetrali di rete. Usare domini in modalità "Native" (Win 2000+) ed evitare, se possibile, domain controller NT4 in modalità legacy-compatible.

### Altri servizi (riepilogo)

> [!info] Tabella riassuntiva 
> tool per servizio RPC endpoint mapper TCP 135 → epdump, rpcdump.py. NetBIOS name service UDP 137 → net view, nltest, nbtstat, nbtscan, nmbscan. NetBIOS session TCP 139/445 → net use, net view. SNMP UDP 161 → snmputil, snmpget, snmpwalk. BGP TCP 179 → telnet. LDAP TCP/UDP 389/3268 → Active Directory Administration Tool. UNIX RPC TCP/UDP 111/32771 → rpcinfo. rwho e rusers (enumeration utenti UNIX). SQL resolution service UDP 1434 → SQLPing. Oracle TNS TCP 1521/2483. NFS TCP/UDP 2049. IPsec/IKE UDP 500.

## 5. Riepilogo del capitolo

> [!success] Idea centrale L'enumeration serve a "sigillare le labbra" del software: ridurre le fughe di informazioni partendo dalle architetture OS fondamentali, bloccando o restringendo l'accesso a servizi come SNMP (la community string "public" di default regala dati a chiunque) e servizi "leaky" come finger e rpcbind. Le applicazioni custom (specialmente web) tendono a dare via ancora più informazioni. I firewall tappano i buchi che il software lascia aperto. Conviene auditarsi da soli con nmap, Nessus e strumenti analoghi.

> [!question] Punti da chiarire Differenza pratica tra `nmap-os-fingerprints` (Nmap) e `osprints.conf` (Siphon) per l'OS fingerprinting, e perché differiscono — è uno dei punti dell'homework. Da chiarire anche il funzionamento di `/etc/inetd.conf` su un host UNIX/Linux e quali servizi tipicamente espone.

> [!todo] Homework collegato (Cap. 2 & 3, 180 punti) Nmap su un dominio target: host discovery, port scanning, active stack fingerprinting, version scanning, vulnerability scanning su una porta selezionata (50pt). Confronto nmap-os-fingerprints vs osprints.conf di Siphon (20pt). Confronto nmap-services vs nmap-service-probe (20pt). Lista di /etc/inetd.conf su host UNIX/Linux e discussione dei servizi offerti (10pt). Metasploit con scan Nmap importati in database, mostrando host e porte trovate (30pt). Banner grabbing su un sito con telnet, netcat e grendel-scan a confronto (30pt). DNS enumeration automatica con dnsenum su un dominio target per trovare subdomain, server e IP (20pt).

lezione successiva [[ETH - Hacking Exposed 7 - Cap 4 - Hacking Windows]]