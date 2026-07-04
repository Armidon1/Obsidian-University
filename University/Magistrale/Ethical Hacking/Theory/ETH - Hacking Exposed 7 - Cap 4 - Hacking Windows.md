# Cap 4: Hacking Windows

> [!abstract] Di cosa parla il capitolo 
> Come si attacca e si difende un sistema Windows. È il capitolo dove l'output dei due precedenti viene finalmente **usato**: Cap. 2 (Scanning) dava porte e OS, Cap. 3 (Enumeration) dava la lista di account validi, e qui quegli account e quelle porte diventano accesso reale. Il capitolo è costruito su tre blocchi netti: attacchi **non autenticati** (entrare da fuori senza credenziali), attacchi **autenticati** (cosa fa un attaccante una volta dentro), e le **security features** di Windows (le difese). Ogni tecnica offensiva è seguita dalle sue contromisure — è un testo difensivo travestito da manuale d'attacco.

---

## Mappa mentale del capitolo

> [!info] I tre blocchi 
> Il capitolo segue l'arco temporale di un'intrusione. **Unauthenticated attacks**: l'attaccante è fuori, senza credenziali, e cerca un varco (password deboli, servizi bucati, driver, l'utente stesso). **Authenticated attacks**: ha già un piede dentro (anche solo come Guest) e vuole diventare Administrator/SYSTEM, rubare password per andare più in profondità, piazzare backdoor, cancellare le tracce. **Windows security features**: il rovescio della medaglia, cosa Microsoft mette a disposizione per chiudere quei buchi. Tenere a mente questa scansione temporale è la chiave per non perdersi tra le decine di tool citati.

> [!info] Guessing vs Cracking vs Pass-the-Hash vs Sniffing 
> Quattro modi diversi di "avere a che fare con le password", spesso confusi. **Guessing (online)**: provo user/password contro un servizio vivo (SMB, RDP…); il lockout dell'account è un problema perché sto facendo rumore. **Cracking (offline)**: ho già l'hash e provo a invertirlo sulla mia macchina; il lockout è irrilevante, conta solo la potenza di calcolo. **Pass-the-Hash**: non cracko niente, uso l'hash _così com'è_ come credenziale. **Sniffing/Dumping**: non attacco la password, la intercetto sul filo o la estraggo dalla RAM/registro. Questo schema mentale ordina metà del capitolo.

---

## Perché Windows è così bucato

> [!info] Le cause strutturali 
> Le slide aprono con tre motivi: la **retrocompatibilità** (importantissima in azienda, abilitata di default, causa di enormi problemi di sicurezza), la **proliferazione di funzionalità** (più codice = più superficie d'attacco: da NT 3.51 a Windows 7 il codice è cresciuto di dieci volte), e il volume di vulnerabilità (~70 bollettini di sicurezza Microsoft l'anno). Il rischio è funzione di **popolarità × complessità**: Windows è insieme il più diffuso e uno dei più complessi, quindi il bersaglio ideale. Worm storici citati: Code Red, Nimda, Slammer, Blaster, Netsky, Gimmiv, EternalBlue, NotPetya.

> [!tip] Il filo rosso è già qui 
> La **retrocompatibilità = buco di sicurezza** era il pattern ricorrente di tutto il Cap. 3 (NetBIOS piatto vs LDAP gerarchico, RestrictAnonymous, modalità legacy NT4 di LDAP). Qui è letteralmente la _prima riga della prima slide_: la stessa idea che in enumeration lasciava trapelare utenti, in Windows lascia attivi protocolli di autenticazione deboli (LM) e sessioni null. Non è una coincidenza tematica, è il difetto architetturale di fondo dell'ecosistema.

> [!info] Prelude — le vulnerabilità 
> Due famiglie: quelle **banali da configurazione** (null session NetBIOS, buffer overflow IIS semplici) e quelle **complesse** (heap exploit, attacchi all'utente finale via Internet Explorer). Il focus degli attaccanti si è spostato nel tempo da servizi di rete → driver kernel → applicazioni. Miglioramenti recenti: meno servizi di rete attivi di default, firewall host abilitato di default, **UAC** (User Account Control).

---

## Parte 1 — Unauthenticated Attacks

> [!info] I quattro vettori 
> L'attacco da fuori passa da uno di quattro punti deboli: **Authentication Spoofing** (indovinare/aggirare le password), **Network Services** (bucare un servizio esposto), **Client Software Vulnerabilities** (l'applicazione dell'utente, es. browser/PDF), **Device Drivers** (i driver, che girano in kernel mode). Tutto il primo blocco è l'esplorazione ordinata di questi quattro.

### Authentication Spoofing — servizi bersaglio

|Servizio|Porta|Note|
|---|---|---|
|**SMB** (Server Message Block)|TCP 445 e 139|Bersaglio tradizionale; connessione a share enumerate (IPC$, C$). Disabilitato su 7/Vista, ma esposto sui domain controller|
|**MSRPC**|TCP 135|L'endpoint mapper visto nel Cap. 3|
|**Terminal Services** (RDP)|TCP 3389|Remote Desktop|
|**SQL Server**|TCP 1433, UDP 1434||
|**SharePoint / web services**|TCP 80, 443||

> [!info] Password guessing da riga di comando 
> Guessing **online** contro questi servizi. A mano si usa il ciclo `FOR` di Windows con `net use` e un file di coppie username/password (esistono DB online di password di default). Automatizzato con: **enum**, **Brutus**, **THC Hydra**, **Medusa**, **Venom**, e per la GUI di Terminal Services/RDP **TSGrinder** o Rdesktop patchato. Punto chiave: gli account **si bloccano** dopo troppi tentativi (lockout), quindi il guessing online è rumoroso e limitato.

```text
# Esempio dalle slide: guessing con enum contro l'host "mirage"
C:\> enum -D -u administrator -f Dictionary.txt mirage
...
(12) administrator | opensesame   password found: opensesame
```

> [!warning] Contromisure al guessing 
> Firewall di rete per limitare l'accesso a SMB (139/445); feature host-resident (filtri IPSec, Windows Firewall); disabilitare del tutto SMB se non serve; **policy di password forti/lunghe**; soglia di **account-lockout** — e assicurarsi che valga _anche per l'Administrator built-in_ (spesso escluso di default); audit dei logon falliti con revisione regolare degli Event Log; **defense in depth** (usarle tutte insieme). Strumenti: `SECPOL.MSC` per la Security Policy, Audit Policy, `dumpel` per analizzare i log, IDS/IPS.

```text
C:\> dumpel -e 529 -f seclog.txt -l security -n Security -t
```

### Sniffing dello scambio di password sulla rete

> [!info] Intercettare l'autenticazione 
> Invece di indovinare, si ascolta il traffico di autenticazione. **Cain** (il più usato) sniffa gli hash challenge-response di **LM**. Su rete switchata non basta stare in ascolto: serve **ARP spoofing/poisoning** per far passare il traffico dall'attaccante. Tre protocolli di autenticazione in gioco, in ordine di robustezza crescente: **LM** (LAN Manager, debolissimo), **NTLM** (con cifratura), **Kerberos** (chiave privata o opzionalmente pubblica). Tool: Cain, LCP, L0phtcrack, KerbSniff.

Buona memoria — e la tua intuizione su Responder coglie una cosa vera: i tool delle slide sono in gran parte **reperti storici**, e il modo in cui si fa sniffing/poisoning oggi (quello che usavi su HTB) è cambiato parecchio. Ti divido i due mondi.

**I tool delle slide, cosa sono e in che stato versano.**

- **Cain (Cain & Abel)** — il coltellino svizzero dell'epoca per Windows: ARP poisoning, sniffing, e cracking (dizionario, brute-force, rainbow table) tutto in una GUI. È **morto e sepolto**: sviluppo fermo da anni, non gira sui Windows moderni, l'antivirus lo segnala. Storicamente importante, operativamente reliquia.
- **L0phtCrack** — password auditor/cracker storico (nato dal collettivo L0pht). Ha avuto una vita travagliata: chiuso, riaperto, poi reso **open source nel 2021**. Esiste ancora ma non è ciò che usa nessuno oggi per craccare.
- **LCP** — clone gratuito di L0phtCrack, cracking di hash LM/NTLM. Abbandonato, di fatto scomparso.
- **KerbSniff / KerbCrack** — coppia storica per sniffare e brute-forzare la pre-auth Kerberos. Concetto ancora validissimo (è l'antenato di quello che oggi chiami **Kerberoasting/AS-REP roasting**), ma quei binari specifici non li usa più nessuno.

Il filo comune: sono tutti **tool GUI Windows dei primi 2000**, dal lato sbagliato della barricata — incarnano strumenti obsoleti invece di attaccare protocolli. È lo stesso pattern che avevi già isolato nel Cap. 3: enum4linux sopravvive perché è un wrapper sui protocolli ancora vivi, gli altri no.

**Dove entra Responder, e perché tu ricordi quello.**

Responder non fa esattamente la stessa cosa di Cain, ed è per questo che è il tool giusto del 2026. Cain faceva **ARP poisoning**: ti mettevi in mezzo al traffico a livello 2. Responder invece **avvelena la name resolution**: risponde alle query broadcast **LLMNR, NBT-NS e MDNS** che le macchine Windows sparano quando il DNS fallisce ("chi è \fileserver?"). Responder alza la mano — "sono io" — la vittima gli si autentica contro, e lui **cattura l'hash NetNTLMv1/v2** (cioè la challenge-response, non l'hash NT memorizzato). Quella la porti offline su **hashcat/John** per craccarla, oppure la **rilanci** senza craccarla con `ntlmrelayx` (di Impacket) — che è il MITM/relay moderno che ha preso il posto di SMBRelay.

Tradotto nella tabella mentale delle note: **Responder = il canale d'ingresso** (poisoning della risoluzione nomi + cattura), **hashcat = il cracking**, **ntlmrelayx = il relay**. Cain provava a fare tutto e tre insieme; oggi sono tre tool specializzati.

Ecco la mappa vecchio → nuovo, che è esattamente il tipo di aggiornamento che le note del corso servono a fissare:

|Concetto|Slide (storico)|Oggi (HTB / reale)|
|---|---|---|
|Mettersi in mezzo|Cain (ARP poisoning)|**Responder** (LLMNR/NBT-NS poisoning), mitm6 (IPv6/DNS)|
|Catturare la challenge-response|Cain sniffer|**Responder**, Inveigh (variante PowerShell/C#)|
|Relay senza craccare|SMBRelay, SMBProxy|**ntlmrelayx** (Impacket)|
|Cracking degli hash|LCP, L0phtCrack, Cain|**hashcat**, **John the Ripper** (Jumbo)|
|Attaccare la pre-auth Kerberos|KerbSniff/KerbCrack|**Kerberoasting / AS-REP roasting** (Rubeus, Impacket `GetUserSPNs`/`GetNPUsers`)|

Un paio di sfumature che vale la pena tenere a mente, così non fai confusione all'esame vs in lab:

- **Il concetto è identico, cambia il vettore.** Le slide poisonano il _layer 2_ (ARP); Responder poisona la _name resolution_ di fallback (LLMNR/NBT-NS), che è proprio la catena "NetBIOS-style" che avevi ricostruito nella nota del Cap. 3 (cache → WINS → broadcast → Lmhosts). Responder vive esattamente in quel gradino "broadcast locale": se il DNS interno risponde, non c'è query da avvelenare — motivo per cui la contromisura n.1 è _disabilitare LLMNR e NBT-NS_.
- **Attento al nome "hash".** Responder cattura il **NetNTLM** (la response sul filo), non l'hash NT del SAM. È craccabile o relay-abile, ma **non** è pass-the-hash-abile: è la distinzione a tre che avevamo fissato (hash memorizzato ≠ response sul filo ≠ password).


> [!info] Kerberos sniffing 
> Kerberos 5 invia un pacchetto di **pre-autenticazione** contenente un timestamp cifrato con una chiave derivata dalla password dell'utente. Se la password è debole, un attacco **offline** su quello scambio può recuperarla (Cain ha uno sniffer MSKerb5-PreAuth). Non c'è difesa semplice se non usare password lunghe e complesse — perché il materiale intercettato è già valido, il collo di bottiglia è solo la forza della password.

> [!warning] Contromisure allo sniffing 
> **Disabilitare l'autenticazione LM** (gli hash NTLM sono più duri da craccare); password complesse e non da dizionario; cifratura a chiave pubblica; usare **IPsec** built-in di Windows per autenticare e cifrare il traffico.

questa è una di quelle sezioni dove le slide dicono _cosa_ si fa ma non _cosa viaggia effettivamente sul filo_, ed è lì che sta tutta la comprensione. Ti ricostruisco il meccanismo da sotto.

**Il punto di partenza: cosa NON viene mai trasmesso.** Quando ti autentichi a un servizio Windows, la password in chiaro non attraversa mai la rete. E — sorpresa — nemmeno l'hash memorizzato nel SAM attraversa la rete così com'è. Quello che viaggia è una **challenge-response**: il server ti manda un numero casuale (la _challenge_ C, un nonce), e tu rispondi con quel numero trasformato usando una chiave derivata dal tuo hash. È esattamente la formula che hai già nella nota: $Response = E_{K_1}(C)|E_{K_2}(C)|E_{K_3}(C)$, dove le tre chiavi vengono da $H = MD4(pwd)$. Il senso di questo schema è che il server può verificarti (conosce il tuo hash e sa ricalcolare la stessa risposta) senza che tu spedisca mai il segreto.

**Perché allora sniffare serve a qualcosa?** Perché chi cattura la coppia (challenge, response) ha in mano tutto il necessario per un **attacco offline**. Il ragionamento dell'attaccante è: "provo una password candidata → ne derivo l'hash → ne derivo le chiavi → cifro la challenge che ho catturato → confronto con la response che ho catturato. Se combaciano, ho indovinato la password." È lo stesso loop del cracking del capitolo dopo, con una differenza cruciale: **è tutto offline**, quindi il lockout dell'account non esiste come problema. Sniffi una volta, poi macini candidati sulla tua macchina per giorni senza che il bersaglio se ne accorga. Ecco perché questa sezione è il ponte naturale verso il cracking: lo sniffing _procura il materiale_, il cracking lo _inverte_.

**Perché LM / NTLM / Kerberos non sono ugualmente sniffabili.** Sono tre generazioni dello stesso problema, con robustezza crescente:

- **LM** è il disastro. L'hash LM è costruito malissimo (password forzata in maiuscolo, spezzata in due metà da 7 caratteri hashate indipendentemente con DES). Questo significa che una challenge-response basata su LM si cracca offline in un lampo, perché stai attaccando due tronconi da 7 caratteri maiuscoli invece di una password intera. È _il_ motivo per cui Cain punta a sniffare proprio l'LM.
- **NTLM** usa l'hash NT (MD4 della password intera, case-sensitive, senza lo spezzettamento). La response è molto più dura da invertire — non impossibile con password debole, ma niente a che vedere con LM.
- **Kerberos** è un'altra bestia, e vale la pena guardarlo a parte.

**Il caso Kerberos.** Qui non c'è una challenge del server nel senso classico. In Kerberos 5, quando il client parte, invia nella richiesta iniziale un dato di **pre-autenticazione**: un timestamp cifrato con una chiave derivata dalla password dell'utente. Serve a provare "sono davvero io, guarda che so cifrare l'ora corrente con la mia chiave". Ma per l'attaccante che lo cattura (lo sniffer MSKerb5-PreAuth di Cain) diventa un oracolo offline: prova una password → deriva la chiave → decifra il pacchetto → è venuto fuori un timestamp valido e sensato? Se sì, password trovata. È lo stesso schema "materiale cifrato con una chiave che dipende dalla password" → brute force offline. Per questo le slide dicono che non c'è difesa semplice: il materiale intercettato è _già valido di suo_, l'unico muro che rimane è la forza della password.

**Il pezzo che le slide danno per scontato: la rete switchata.** "Sniffare" su un hub è banale, perché l'hub ripete ogni pacchetto su tutte le porte — sei in ascolto e senti tutto. Ma le reti moderne sono **switchate**, e lo switch manda il traffico solo alla porta del destinatario giusto: due macchine che dialogano tra loro non passano mai dalla tua porta. Ecco perché serve l'**ARP spoofing/poisoning**: avveleni la cache ARP delle vittime così che credano che _tu_ sia il gateway (o l'altro host), e il traffico viene deviato attraverso di te. A quel punto sei in posizione man-in-the-middle e lo sniffing torna possibile. È lo stesso ARP poisoning della sezione MITM subito successiva — non è una ripetizione, è che sniffing passivo e MITM attivo sono un continuum: una volta in mezzo, oltre a _leggere_ la challenge-response puoi anche **forzare un downgrade**, cioè convincere il client a usare il dialetto più debole (LM) per rendere il materiale il più facile possibile da craccare.

**Una distinzione che ti conviene fissare adesso**, perché è la fonte di confusione numero uno quando poi arrivi a pass-the-hash e relay. Ci sono tre cose diverse che vengono tutte chiamate "hash" a sproposito:

1. L'**hash memorizzato** (nel SAM o in RAM) → è quello che riusi _direttamente_ nel pass-the-hash.
2. La **challenge-response sul filo** (il "NetNTLM") → questa NON la puoi passare come un hash: o la **cracki** offline per risalire alla password, oppure la **rilanci live** verso un altro server (ed è esattamente l'attacco SMBRelay della sezione dopo).
3. La **password in chiaro** → il fine ultimo.

Sniffing ti dà il tipo 2. Pass-the-hash lavora sul tipo 1. Sono canali diversi verso prede diverse, anche se il capitolo li mette vicini.

**Le contromisure, lette attraverso il meccanismo** (così non sono una lista da memorizzare ma conseguenze logiche):

- _Disabilitare l'autenticazione LM_ toglie dal filo la response più facile da craccare — costringi l'attaccante a lavorare su NTLM, ordini di grandezza più duro.
- _Password lunghe e complesse_ sono la difesa vera contro Kerberos pre-auth e in generale contro tutto lo sniffing, perché ricordati che l'attacco finale è sempre un brute force offline: l'entropia della password è letteralmente il muro.
- _Cifratura a chiave pubblica e IPsec_ attaccano il problema alla radice: se il canale è cifrato e mutuamente autenticato, non c'è più una challenge-response in chiaro da catturare **e** l'ARP spoofing non ti mette più in mezzo in modo utile, perché non puoi decifrare né impersonare senza le chiavi.

Il filo conduttore, se lo vuoi in una frase: **lo sniffing non ruba la password, ruba una prova crittografica derivata dalla password, e la trasforma in un problema di brute force offline** — dove "offline" è la parola che rende l'attacco paziente e silenzioso, e "forza della password" è l'unica variabile che decide se ci riesce.

Se ti è utile, posso aggiungere alla nota un callout che rende esplicita quella distinzione a tre (hash memorizzato / response sul filo / password) — è il tipo di chiarimento "a voce" che nelle slide manca e che torna utile quando arrivi a SMBRelay e pass-the-hash.

#### Approfondimento [[Kerberos]]
vedi [[Kerberos#4. Il Flusso del Protocollo (Topic-by-Topic)]] per vedere esattamente come funziona il protocollo.
###### Domanda: in che fase avviene però lo sniffing del ticket in [[Kerberos]] quando si fa [[Kerberoasting]]?

Domanda giusta, e la risposta ti costringe a separare due attacchi che hai — comprensibilmente — impacchettato insieme. Nella tua domanda ci sono **due cose diverse** che avvengono in **due fasi diverse**: la pre-auth (di cui parla la slide, [[Kerberos#Fase A Login Iniziale (AS)]]) e il Kerberoasting (che ricordi da HTB). Non sono lo stesso attacco. Te li aggancio uno per uno al flusso che hai scritto — che, tra l'altro, è corretto.

**Prima cosa da correggere sul lessico:** "Kerberoasting" non è sniffing. Kerberoasting è _richiedere_ un ticket e poi craccarlo offline. Il termine giusto per l'attacco della slide (pre-auth) è **AS-REP roasting**. Sono cugini ma pescano in punti opposti del flusso.

**Fase 1 — AS exchange (AS-REQ / AS-REP). Qui vive l'attacco della slide.**

Nel tuo flusso è il primissimo passo: Alice chiede il TGT. Il dettaglio che ti manca è _cosa_ Alice allega alla AS-REQ. Per dimostrare di essere lei, allega il dato di **pre-autenticazione**: un **timestamp cifrato con la sua chiave** (derivata dalla password). Il KDC lo decifra con la chiave di Alice che ha nel DB; se ne esce un orario sensato, Alice è autentica e il KDC risponde con la AS-REP (session key + TGT).

L'attacco della slide (lo sniffer MSKerb5-PreAuth) intercetta **quel timestamp cifrato** nella AS-REQ. È materiale cifrato-con-chiave-derivata-da-password → oracolo offline: provo password → derivo la chiave → decifro → è un timestamp valido? sì = password trovata. Questo è **sniffing vero**, perché catturi qualcosa che transita. MSKerb5-PreAuth è morto ormai e non esistono tool moderni. Leggi [[Kerberos#Ma che si usa oggi al posto di MSKerb5-PreAuth per sniffare il pacchetto di autenticazione di Alice nella fase 1 con però il flag presente? (vedi Kerberos Fase A Login Iniziale (AS) )|qui]] il perché.

Ma — ecco il punto moderno — **AS-REP roasting** attacca la stessa fase _senza sniffare niente_. Se un account ha la flag **"non richiedere pre-autenticazione"** (`DONT_REQ_PREAUTH`), chiunque può mandare una AS-REQ _a nome di Alice_ senza conoscere la password, e il KDC risponde con una AS-REP che contiene un blob **cifrato con la chiave di Alice**. Quel blob lo cracchi offline identico. Non ti sei messo in mezzo al traffico: hai _chiesto tu_ al KDC. Per questo AS-REP roasting non è sniffing — è una richiesta legittima abusata.

**Fase 2 — TGS exchange (TGS-REQ / TGS-REP). Qui vive il Kerberoasting.**

Nel tuo flusso è quando Alice chiede al KDC il ticket per Bob, presentando il TGT. Guarda cosa torna il KDC nella TGS-REP: il **ticket per Bob**, e quel ticket è **cifrato con la chiave di Bob** (cioè con l'hash dell'account del _servizio_ Bob — quello che nel tuo schema chiami "la chiave di Bob").

[[Kerberoasting]] sfrutta esattamente questo: un utente autenticato qualsiasi chiede al KDC un ticket per un servizio (un account con un **SPN**), e il KDC glielo consegna cifrato con l'hash di quel service account. L'attaccante prende quel ticket e lo **cracca offline** per recuperare la password del _servizio_. Il KDC non verifica se Alice ha davvero il permesso di _parlare_ con Bob — quel controllo lo fa Bob dopo; il KDC consegna il ticket a chiunque abbia un TGT valido. Questa è la falla.

Quindi, rispondendo secco alla tua domanda "in che fase avviene lo sniffing con Kerberoasting":

- **Kerberoasting non fa sniffing.** Avviene nella **fase 2 (TGS-REP)** e non intercetta nulla: _richiede_ un service ticket e lo cracca. La preda è la **password del service account** (Bob).
- **L'attacco della slide (pre-auth) è nella fase 1 (AS)**. Nella variante storica _sniffa_ il timestamp della AS-REQ; nella variante moderna (**AS-REP roasting**) non sniffa, chiede la AS-REP. La preda è la **password dell'utente** (Alice).

La linea che le tiene distinte, e che vale la pena fissare: **cosa cracchi e con che chiave è cifrato.**

| |Fase nel tuo flusso|Cosa catturi|Cifrato con la chiave di|Sniffing?|
|---|---|---|---|---|
|Pre-auth (slide)|AS-REQ|timestamp di pre-auth|utente (Alice)|Sì, storicamente|
|AS-REP roasting|AS-REP|blob della AS-REP|utente (Alice)|No, lo richiedi|
|Kerberoasting|TGS-REP|service ticket|servizio (Bob/SPN)|No, lo richiedi|

Il filo comune con tutto il resto del capitolo resta identico: in ogni riga c'è **materiale cifrato con una chiave derivata da una password**, quindi ogni riga collassa in un **brute force offline** dove l'unico muro è la forza di quella password. Cambia solo _di chi_ è la password (utente vs servizio) e _dove_ la peschi nel protocollo. Ecco perché il Kerberoasting è così temuto: i service account spesso hanno password vecchie, lunghe ma mai cambiate, e a volte deboli — ed è un attacco che parte da un _qualsiasi_ utente di dominio autenticato, senza privilegi.

Un'ultima messa a punto sul tuo schema, che è quasi perfetto: quando dici che il TGT contiene "alice e la session key criptato con la chiave del TGT" — sì, la _krbtgt key_, l'hash dell'account krbtgt; è la stessa chiave che, se rubata, produce i **[[Golden Ticket]]**. E il ticket per Bob cifrato "con la chiave di Bob" è esattamente ciò che il Kerberoasting cracka. Avevi già in mano i due pezzi giusti, mancava solo mapparci sopra i nomi degli attacchi.

Se vuoi, ti preparo una nota Obsidian dedicata a Kerberos — flusso AS/TGS con diagramma di sequenza e la tabella dei tre attacchi (pre-auth / AS-REP roast / Kerberoast) mappati sulle fasi — così completi il terzetto LM → NTLM → Kerberos che avevamo lasciato in sospeso. La faccio?

### Man-in-the-Middle (MITM)

> [!info] Rilanciare l'autenticazione altrui 
> L'attaccante si mette in mezzo e **rilancia** lo scambio di autenticazione legittimo di un client per farsi passare per lui verso il server. **SMBRelay** e **SMBProxy** passano avanti gli hash di autenticazione ottenendo accesso autenticato. Varianti: SMB Credential **Reflection** e **Forwarding**. Cain fa ARP poisoning, poi **fa il downgrade** dei client a dialetti di autenticazione più deboli (più facili da sniffare) e può sniffare sessioni RDP rompendone la cifratura (XP / Server 2003). Tool: Cain, Squirtle, SMBRelay3.

> [!warning] Contromisure MITM 
> Se l'attaccante è **già sulla tua LAN**, è molto difficile difendersi. Usare protocolli autenticati e cifrati, imporli con Group Policy e regole firewall, verificare l'identità dei server remoti con autenticazione forte o terze parti fidate, **disabilitare NetBIOS Name Services e usare DNS**.

Poco di davvero nuovo a livello di _concetto_ — quasi tutto quello che c'è in questa slide l'hai già smontato nelle domande precedenti. Ma ci sono due o tre dettagli che aggiungono qualcosa, e uno che chiude un cerchio. Ti isolo solo il delta.

**Cosa NON è nuovo** (per non rileggere due volte lo stesso meccanismo): il relay in sé — "mi metto in mezzo e rilancio la response di un altro senza craccarla" — è esattamente ciò che avevamo definito come il gemello dello sniffing quando abbiamo distinto _cracking offline_ vs _replay live_ (replay live sarebbe proprio relay, che è diverso dal normale replay). E il downgrade ai dialetti più deboli (forzare LM per rendere la cattura facile) l'avevamo già visto come mossa MITM nella sezione sniffing. Quindi su questi due la slide ripete.

**Cosa aggiunge davvero:**

- **Reflection vs Forwarding**, la distinzione che vale la pena fissare. _Forwarding_ = prendo la response del client A e la rilancio verso un server B _diverso_ (movimento laterale classico). _Reflection_ = la rimando verso **la stessa macchina da cui viene** — il client si autentica involontariamente a sé stesso e l'attaccante ottiene accesso su quell'host. La reflection era la variante più insidiosa; Microsoft l'ha chiusa nel 2008 (MS08-068), ed è il motivo per cui oggi `ntlmrelayx` di default _non_ rilancia sull'origine e devi puntare a un target terzo. È il pezzo storico che spiega una regola operativa che magari su HTB davi per scontata.
    
- **Il caso RDP (XP / Server 2003)**: qui non si parla di NTLM ma di rompere _la cifratura del canale_ RDP di quelle versioni, che usavano una chiave statica sniffabile → l'attaccante decifra la sessione desktop in chiaro. È un vettore diverso dagli hash, ed è il motivo per cui è nato **NLA (Network Level Authentication)** come contromisura. Dettaglio da museo, ma è l'unico punto della slide che tocca RDP a questo livello.
    
- **Squirtle / SMBRelay3**: due nomi in più nella lista dei tool, entrambi nella stessa categoria "reperti" di SMBRelay — rimpiazzati oggi da `ntlmrelayx`. Nessun concetto nuovo, solo altri fossili per la mappa vecchio→nuovo.
    

**Il cerchio che si chiude** — ed è la cosa più interessante: guarda l'ultima contromisura. _"Disabilitare NetBIOS Name Services e usare DNS."_ È **letteralmente** la stessa raccomandazione che avevamo dato per Responder due domande fa. La slide la mette qui come difesa MITM generica senza spiegare il perché; tu ora sai il meccanismo completo: NBT-NS (e LLMNR) sono la catena di risoluzione nomi di fallback che un attaccante avvelena per _diventare_ il man-in-the-middle in primo luogo. Disabilitarli e affidarsi al DNS interno autoritativo toglie all'attaccante il gancio per mettersi in mezzo. Le slide del prof e Responder stanno descrivendo i due lati della stessa identica moneta — la slide dal lato difesa, HTB dal lato attacco.

Quindi il valore vero di questa slide, per le tue note, non è nuova teoria: è che **collega** il relay (che avevi capito), il downgrade (idem), e il poisoning della name resolution (Responder) in un unico quadro MITM, e giustifica a posteriori quella contromisura "usa DNS" che altrimenti sembra buttata lì.

**Il bullone che va stretto bene:** attento a non dire "sniffing tramite Responder" come se Responder ascoltasse passivamente. Responder **non sniffa**, avvelena la risoluzione nomi per _farsi arrivare_ l'autenticazione — è già un intervento attivo. Il "vero" sniffing passivo (stare zitti in ascolto) è quello di Cain su rete a hub, roba da museo. Nella pratica moderna la cattura è sempre attiva (poisoning). È una differenza che conta perché spiega perché la contromisura è "disabilita LLMNR/NBT-NS": togli il gancio che Responder usa per intromettersi.

E la biforcazione finale, quella da tenere ferma perché l'hai già incontrata tre volte:

- se **cracchi** la response → ottieni la **password** (e da lì fai quello che vuoi, incluso poi eventualmente pass-the-hash con l'hash NT, ma è un altro segreto);
- se **rilanci (relay)** la response → **non** ottieni né password né hash, ottieni **una sessione autenticata** su quel target, qui e ora.

Sono due prede diverse: il cracking ti dà un _segreto riusabile_, il relay ti dà un _accesso immediato e usa-e-getta_.

In una riga: **una posizione (in mezzo al traffico di auth), un materiale (la challenge-response), due destini — craccarla offline o rilanciarla live; e il rilancio è il relay, nelle sue due forme forwarding e reflection.**

Per la nota `LAN Manager vs NTLM` — rispettando i titoli corti — ti propongo di aggiungere un callout così:

> [!info] Reflection vs forwarding 
> Due modi di rilanciare la response catturata. **Forwarding**: verso un server _diverso_ da quello d'origine (movimento laterale). **Reflection**: verso _la stessa macchina_ che l'ha emessa — il client si autentica a sé stesso. La reflection è stata chiusa da MS08-068, motivo per cui `ntlmrelayx` oggi punta di default a un target terzo e non all'origine.

E, se vuoi legare esplicitamente i due lati della moneta:

> [!tip] Difesa = togliere il gancio 
> La contromisura "disabilita NBT-NS/LLMNR e usa DNS" è lo stesso punto visto con Responder, dall'altro lato: quei servizi di name resolution sono il canale che l'attaccante avvelena per _diventare_ il man-in-the-middle. Senza quel gancio, relay e downgrade non partono nemmeno.
> 
### Pass-the-Hash

> [!info] La credenziale è l'hash 
> Tecnica **post-exploitation** ma inserita qui perché è ciò che rende catastrofica una singola compromissione. Passi: (1) comprometti una macchina, (2) fai il **dump degli hash dalla RAM**, (3) li **riusi come credenziali** per servizi di rete — **senza mai craccarli**. Funziona perché in NTLM l'hash _è_ ciò che serve per autenticarsi: non c'è bisogno della password in chiaro. Con un solo host compromesso si arriva a compromettere l'intero **dominio**; se un Administrator si era loggato su quella macchina _prima_ della compromissione, anche le sue credenziali sono catturate. Tool: **Windows Credential Editor (WCE)**.

> [!info] Pass-the-Ticket L'analogo per Kerberos: si fa il dump dei **ticket** Kerberos presenti in RAM e li si riusa. WCE può replicare e riusare i ticket, ma bisogna sempre aver compromesso l'host prima. Le password sono cifrate, _ma le chiavi stanno in RAM_ — ed è lì che si va a prenderle.

> [!warning] Contromisure Pass-the-Hash NTLM è **vulnerabile by design**, non c'è una patch. L'unica vera difesa è **prevenire l'intrusione iniziale** (è una tecnica post-exploitation: se non entrano, non c'è hash da passare) e, dove possibile, usare **autenticazione a due fattori**.

In breve, i tre nomi che ricordi sono tre **fonti diverse** da cui si estraggono credenziali. Te li separo, perché è proprio la distinzione utile:

**[[SAM (Security Accounts Manager)]]** — il database degli account **locali** della macchina (`HKLM\SAM`, file lockato mentre gira l'OS). Contiene gli **hash NT** degli utenti locali. Da qui prendi le credenziali degli account locali (incluso l'Administrator locale). Serve privilegio SYSTEM per leggerlo. È la fonte "a disco/registro".

**[[LSASS Credential Dumping|LSASS]]** (Local Security Authority Subsystem Service) — **il processo `lsass.exe` in RAM**. È qui che sta la roba interessante per il pass-the-hash: mentre gli utenti sono loggati, LSASS tiene in memoria i loro **hash NT, i ticket Kerberos** (e, su sistemi vecchi/malconfigurati, WDigest teneva perfino la password in chiaro). È esattamente il "dump dalla RAM" del passo (2) della tua slide. Il dump si fa leggendo la memoria del processo lsass.

**[[LSA Secrets]]** — un ramo del registro (`HKLM\SECURITY\Policy\Secrets`) dove stanno segreti _persistenti_: password dei **service account** in chiaro, credenziali di scheduled task, password dell'account computer, ecc. Fonte diversa dal SAM (che sono utenti) e da LSASS (che è runtime).

**Come si fa, concretamente:**

Il dump di LSASS è la via regina per il PtH. Due modi: leggere direttamente la memoria del processo, oppure fare prima un **dump del processo** (es. con `procdump` o Task Manager → "Crea file di dump") e poi parsarlo offline. Il tool standard è **[[Mimikatz]]** (`sekurlsa::logonpasswords` per hash/password dalla RAM, `sekurlsa::tickets` per i ticket Kerberos). Su Linux/HTB tipicamente **`secretsdump.py`** di [[Impacket]], che da remoto tira fuori SAM + LSA Secrets + cache di dominio in un colpo. La slide del prof cita **WCE**, che è il predecessore storico di Mimikatz per lo stesso scopo.

Nota che tutto richiede **privilegi alti** (admin locale / SYSTEM): il dumping è _post_-escalation, non un modo per entrare.

La mappatura mentale, così la fissi:

|Fonte|Dove|Cosa contiene|Tool tipico|
|---|---|---|---|
|SAM|registro/disco|hash NT utenti **locali**|secretsdump, mimikatz `lsadump::sam`|
|LSASS|RAM (`lsass.exe`)|hash + **ticket** degli utenti loggati|mimikatz `sekurlsa::`, procdump|
|LSA Secrets|registro|password service account, task, computer|secretsdump, mimikatz `lsadump::secrets`|

Per il **pass-the-hash** in senso stretto la fonte è **LSASS** (o il SAM se ti basta un account locale): è da lì che esce l'hash NT che poi riusi. Per il **pass-the-ticket** sempre LSASS, ma prendi i ticket invece degli hash.

Contromisura moderna che chiude proprio questa strada: **Credential Guard**, che isola LSASS in un ambiente virtualizzato (VBS) così non ne dumpi più la memoria — è l'evoluzione difensiva rispetto al "non c'è patch" della tua slide, che era vero all'epoca di WCE.


### Remote Unauthenticated Exploits

> [!info] Bucare il software 
> Windows Sfruttare falle o misconfigurazioni nel software Windows stesso: servizi TCP/UDP, interfacce driver, applicazioni user-mode (MS Office, Internet Explorer, Adobe Reader). Strumento principe: **Metasploit** — framework + archivio di moduli exploit. Il flusso è: cercare il modulo, personalizzare i **parametri** (vendor/modello del software vittima), i **payload** (shell remota, creazione utenti, codice iniettato) e le **opzioni** (IP target, evasione IDS). Metasploit è tipicamente un paio di mesi indietro rispetto agli alert Microsoft; alternative commerciali più aggiornate ma costose sono CORE IMPACT e Canvas.

> [!example] Print Spooler → Stuxnet 
> Le slide citano il caso famoso: l'exploit del servizio **Print Spooler** incluso in Metasploit è quello usato da **Stuxnet** per colpire un reattore nucleare iraniano. Esempio di come un modulo "da laboratorio" e un'arma cyber-fisica reale condividano lo stesso bug.

> [!warning] Contromisure ai network service exploit 
> **Patchare in fretta**; workaround per le vulnerabilità non ancora patchate (disabilitare servizi deboli); audit/log/monitoraggio del traffico; avere un **piano di incident response** con un **CSIRT** (team che include security, IT, legale, HR, PR) che definisca la risposta dell'organizzazione a un attacco.

### End-user Application Exploits

> [!info] L'utente è l'anello debole 
> Gli utenti finali sono meno competenti in sicurezza e gestiscono male un ecosistema software ricco. I "worst offenders" citati sono **Adobe Flash Player** nel browser e **Adobe PDF Reader**. Metasploit ha moduli dedicati (es. ricerca `adobe flash`).

> [!warning] Contromisure end-user 
> Firewall per limitare le connessioni **in uscita**; patch; antivirus (specie sugli allegati email); **least privilege** — mai navigare come Administrator; opzioni di sicurezza software (es. leggere le email in solo testo); MS Office con sicurezza macro al massimo.

### Device Driver Exploits

> [!info] Bucare dal kernel 
> Ci sono stati buffer overflow nei driver **wireless** di Windows: basta trovarsi nel raggio fisico di un access point rogue che trasmette **beacon frame** malevoli — **nessuna connessione richiesta** da parte della vittima, si può compromettere ogni macchina vulnerabile nel raggio. La compatibilità Plug and Play significa una marea di driver di terze parti; girando in **kernel mode** ad alti privilegi, _un solo driver debole implica compromissione totale_. Metasploit ha moduli WiFi (es. beacon frame sovradimensionato → remote code execution).

> [!warning] Contromisure driver
> Patch del vendor; disabilitare il wireless in ambienti ad alta concentrazione di AP; **driver signing** (firme fidate sul codice kernel-mode) — con la nota polemica delle slide: Microsoft testa davvero a fondo i driver? (rif. EternalBlue). Adozione dello **User-Mode Driver Framework (UMDF)** v2, che sposta i driver fuori dal kernel.

Volentieri — questa sezione è breve nelle slide ma sotto c'è il concetto che rende i driver la superficie d'attacco più temuta di Windows, e vale la pena aprirlo perché tocca cose che abbiamo già visto (SYSTEM, rootkit, Credential Guard) e una parte moderna che le slide precedono.

**Perché "kernel mode" significa game over, e non solo "molti privilegi".** Il processore ha degli anelli di privilegio: le applicazioni normali girano in **ring 3** (user mode), isolate, con accesso mediato alla memoria e all'hardware; il kernel gira in **ring 0**, con accesso totale a tutta la memoria, a tutto l'hardware, a ogni istruzione. Un driver _è_ codice che gira in ring 0. Questo cambia la natura di un bug: la vulnerabilità di un'applicazione la contieni (c'è il kernel sopra che fa da autorità), ma la vulnerabilità di un driver **non ha nessuno sopra**. Chi compromette un driver non ottiene "Administrator" — ottiene qualcosa _sopra_ Administrator, lo stesso salto che nel capitolo era descritto con "SYSTEM > Administrator", ma ancora più in là: può disattivare l'antivirus e l'EDR (che pure girano in kernel), nascondere processi e file, installare un **rootkit**. È il motivo per cui i rootkit vivono lì. Ecco perché la slide dice "un solo driver debole implica compromissione totale": non è enfasi, è la conseguenza logica dell'anello 0.

**Perché il beacon frame è l'attacco più insidioso: lo "zero interaction".** Qui sta la parte davvero notevole, e conviene capire _perché_ "nessuna connessione richiesta". Gli access point Wi-Fi trasmettono in continuazione dei **beacon frame**: pacchetti di annuncio che dicono "esisto, mi chiamo questo SSID, supporto queste velocità". Il driver wireless della vittima **ascolta e interpreta quei beacon in automatico**, tutto il tempo — è così che il tuo laptop ti mostra la lista delle reti disponibili _prima_ che tu scelga di connetterti. Quindi il parsing di quei frame avviene **senza che l'utente faccia nulla**: né connettersi, né cliccare, né autenticarsi. Se il driver ha un buffer overflow nel modo in cui interpreta un campo malformato o sovradimensionato del beacon, all'attaccante basta **essere nel raggio radio** e trasmettere il frame velenoso. Il driver lo processa da solo, in kernel, e l'attaccante ottiene esecuzione ring 0 su _ogni_ macchina vulnerabile nel raggio, contemporaneamente. È pre-autenticazione, pre-associazione, pre-tutto. Il caso storico è il "Month of Kernel Bugs" del 2006 e l'overflow nei driver Broadcom (`BCMWL5.SYS`), con il modulo Metasploit relativo — esattamente ciò che la slide cita.

Nota come questo lo colloca nel posto giusto del capitolo: è nella sezione **attacchi non autenticati** perché è uno dei pochissimi vettori che ti dà compromissione totale _da esterno, senza credenziali e senza interazione_. Nella tabella mentale del capitolo è l'estremo opposto del pass-the-hash (che invece è tutto post-compromissione).

**Perché i driver sono una superficie enorme.** Il Plug and Play significa che Windows carica automaticamente driver di **terze parti** per ogni pezzo di hardware immaginabile — schede video, wireless, stampanti, chiavette. È codice scritto dai vendor, di qualità molto variabile, che finisce in kernel e che tipicamente è auditato molto meno del core di Windows. La superficie d'attacco non è "Windows", è "Windows più le centinaia di driver di chiunque abbia mai prodotto hardware compatibile". Ogni driver installato è un potenziale ring 0.

**Il driver signing e la polemica delle slide.** Da Windows a 64 bit (Vista in poi), i driver kernel devono essere **firmati digitalmente** (Kernel Mode Code Signing): l'idea è che solo codice fidato e firmato giri in ring 0. Il punto debole — ed è esattamente la polemica che le slide sollevano — è che **la firma certifica la provenienza, non la sicurezza**. Ti dice _chi_ ha scritto il driver, non _se ha bug_. Un driver firmatissimo e legittimo può avere un buffer overflow sfruttabile. La firma alza il muro contro il driver _palesemente_ malevolo, ma non contro quello vulnerabile.

Sul riferimento a **EternalBlue** nelle slide: attenzione, è tecnicamente un po' spostato ma difendibile. EternalBlue (MS17-010) era un bug in **SMB**, non in un driver Plug-and-Play. Però il server SMB di Windows (`srv.sys` / `srvnet.sys`) _è_ a tutti gli effetti un **driver kernel** — quindi come esempio di "bug in un componente kernel-mode → compromissione totale, per giunta wormabile (WannaCry, NotPetya)" regge. Il senso della citazione è: se persino un componente core di Microsoft ha avuto un buco kernel così devastante, la fiducia cieca nella "qualità testata" del codice ring 0 è mal riposta. Come riferimento sul _rigore dei test_ è calzante; solo, non è un driver di terze parti in senso stretto.

**UMDF: la soluzione strutturale.** Lo User-Mode Driver Framework sposta certe classi di driver (tipicamente periferiche USB, roba che non ha bisogno di accesso diretto a interrupt/hardware) **fuori dal kernel, in user mode**. Il guadagno di sicurezza è enorme e diretto: un bug in un driver UMDF compromette al massimo un processo host in ring 3 a bassi privilegi — _non_ il kernel. Non tutti i driver possono essere UMDF (chi deve toccare l'hardware a basso livello resta per forza in kernel), ma dove si può, si toglie codice rischioso dall'anello 0. È la stessa filosofia del least privilege applicata ai driver.

**La parte che le slide precedono — e che è il volto moderno di tutto questo: BYOVD.** Oggi lo scenario dominante non è il beacon frame (i driver wireless sono molto più solidi), ma il **Bring Your Own Vulnerable Driver**. Il ragionamento dell'attaccante: "il driver signing mi blocca il driver malevolo? Bene, allora ne porto uno **legittimo, firmato, ma vulnerabile**." L'attaccante — che ha già privilegi admin (caricare un driver richiede admin, quindi è _post_-exploitation) — installa un driver firmato con un bug noto, e sfrutta _quel_ bug per saltare da admin a ring 0. A cosa gli serve, se è già admin? A fare ciò che nemmeno l'admin può: **spegnere l'EDR/antivirus dal kernel**, installare rootkit, manomettere le protezioni. Casi celebri: il driver `capcom.sys`, vari driver di utility/GPU, tool come AuKill. La risposta di Microsoft è la **vulnerable driver blocklist** (la blocklist dei driver, legata a HVCI/Memory Integrity).

E qui si chiude un cerchio con la nota LSASS di prima: la difesa moderna del kernel è **HVCI/VBS** (Virtualization-Based Security), che isola il kernel dai driver malevoli con la virtualizzazione — ed è **la stessa tecnologia su cui poggia Credential Guard** che protegge LSASS. VBS è il tronco comune: da un lato protegge le credenziali in RAM (Credential Guard), dall'altro protegge l'integrità del kernel dai driver (HVCI). Due difese moderne, una radice.


---

## Parte 2 — Authenticated Attacks

### Privilege Escalation

> [!info] Da Guest a SYSTEM 
> Una volta loggati come Guest o Limited User, l'obiettivo è salire ad **Administrator** o **SYSTEM**. Exploit storici: `getadmin.exe` (DLL injection), buffer overrun MS03-013, e molti altri.

> [!info] SYSTEM > Administrator 
> Punto controintuitivo: l'account **SYSTEM è più potente dell'Administrator**. L'Administrator però può schedulare task che vengono eseguiti _come_ SYSTEM — quindi è il ponte per arrivarci (più complicato da Vista in poi, ma ancora possibile).

> [!warning] Prevenire l'escalation 
> Tenere le macchine patchate; **restringere il logon interattivo** ad account fidati via Security Policy (`secpol.msc` → Local Policies → User Right Assignment → _Deny log on locally_).

### Estrarre gli hash delle password

> [!info] Dove stanno gli hash 
> Due archivi. Utenti **locali**: nel **SAM** (Security Accounts Manager), su NT4 e precedenti — è la controparte Windows di `/etc/passwd` (collega al Cap. 3). Utenti di **dominio**: nell'**Active Directory** dei domain controller (Windows 2000+). Percorsi: SAM in `%systemroot%\system32\config\SAM` (lockato mentre l'OS gira, presente anche nella chiave di registro `HKLM\SAM`); AD in `%windir%\WindowsDS\ntds.dit`.

> [!info] Come prenderli 
> Via facile: **Cain** (tab Cracker → right-click → "Add to List"). Meccanismo: si **inietta una DLL** in un processo ad alti privilegi del sistema in esecuzione — così fanno pwdump, Cain, Ophcrack. Vie alternative: bootare un OS alternativo e copiare i file; copiare il backup del SAM del Repair Disk (ma è protetto da **SYSKEY**, molto più duro/impossibile da craccare); sniffare gli scambi di autenticazione.

> [!warning] Contromisure a pwdump & co. 
> Non c'è difesa contro pwdump2/3/4, Cain, Ophcrack ecc. **Ma** l'attaccante ha bisogno di **diritti amministrativi locali** per usarli — quindi la difesa è a monte: non farsi bucare come admin.

### Cracking degli hash

> [!info] Invertire l'hash offline 
> L'hash è pensato per essere difficilissimo da invertire. Gli hash **NTLM** sono duri; il problema sono gli **LM**, ancora usati da Windows XP e precedenti per **retrocompatibilità** (disabilitati di default da Vista/Win7). Il cracking offline funziona così: prendo una lista di candidati (dizionario), li hasho con lo stesso algoritmo, confronto con l'hash estratto — se combaciano, password trovata. Il **lockout non conta** perché è tutto offline.

> [!danger] Windows non usa il salt 
> Il difetto cruciale. Il **salt** è un valore casuale aggiunto alla password prima dell'hashing, così due utenti con la stessa password producono hash diversi. **Windows non salta** i suoi hash: due account con la stessa password danno lo _stesso_ hash. Questo rende praticabili le **rainbow table** (hash precomputati che barattano tempo con memoria). Linux invece salta i suoi hash. Es. dalle slide: "Project Rainbow Crack", tabella LM precomputata da 24 GB su 6 DVD per $120.

> [!info] NTLM usa MD4 (challenge-response) 
> Il meccanismo mostrato nelle slide: dalla password si deriva $H = MD4(pwd)$, poi $H$ viene spezzata (con padding di zeri) in tre chiavi $K_1, K_2, K_3$. Il server manda una **challenge** $C$; il client risponde con $C$ cifrata sotto le tre chiavi concatenate: $Response = E_{K_1}(C) | E_{K_2}(C) | E_{K_3}(C)$. È questo che rende possibile il pass-the-hash: chi ha $H$ può calcolare la risposta senza conoscere la password in chiaro.

> [!info] Hash veloci vs lenti 
> Regola generale: **tutti gli hash veloci sono sbagliati per le password** (SHA, MD, CRC), proprio perché sono veloci a calcolare in massa. Serve un algoritmo **lento** (Ubuntu e macOS hashano migliaia di volte in iterazione, per rallentare l'attaccante). Le due tecniche di cracking: **brute force** (tutte le combinazioni) e **dictionary** (parole di una lista, con varianti tipo `ABLE`, `Able`, `@bl3`).

> [!warning] Contromisure al cracking 
> Password forti (non da dizionario, lunghe, complesse); aggiungere caratteri ASCII non stampabili (es. NUM LOCK + ALT255 o ALT-129). Concetto chiave: **entropia** = imprevedibilità della password. Consigliati i **password manager** / generatori automatici. Nota critica delle slide: possiamo davvero fidarci dei vault?

> [!info] Accelerare il cracking 
> **Rainbow table** (barattano tempo con memoria) ed **Elcomsoft Distributed Password Recovery**, che usa molte macchine e le loro **GPU** insieme per craccare ~100× più veloce. Tool: John The Ripper Jumbo (CLI); LCP, Cain, Ophcrack, L0phtcrack, Elcomsoft (GUI).

### Dump delle credenziali in cache
ricorda: SAM contiene account locali, LSASS contiene account loggati nella sessione corrente, [[LSA Secrets]] contiene utenti e password dei servizi (docker ecc) mentre Previous Logon Cache gli ultimi 10 account collegati che vengono tenuti in caso il Controller non fosse raggiungibile. La distinzione è negli account locali (della macchina stessa), di dominio (AD) e dei servizi.

> [!info] Tre depositi diversi di credenziali 
> Oltre al SAM, Windows tiene credenziali in altri due posti, spesso confusi tra loro. **LSA Secrets**, **cache dei logon di dominio** e ciò che estrae **WCE** sono tre cose distinte — vale la pena tenerle separate.

> [!info] LSA Secrets 
> Il **Local Security Authority** conserva credenziali di logon _in chiaro_ per sistemi esterni, sotto `HKLM\SECURITY\Policy\Secrets`. Cifrate a macchina spenta, ma **decifrate e tenute in memoria dopo il login**. Contenuto: password di service account in plaintext (anche di domini esterni), hash in cache degli ultimi 10 utenti, password FTP/web in chiaro, credenziali RAS dial-up, password degli account computer per l'accesso al dominio.

> [!info] Previous Logon Cache 
> Se un membro del dominio non raggiunge il domain controller, fa un **logon offline** con credenziali in cache. Gli ultimi **10 logon di dominio** sono memorizzati cifrati e hashati. Il tool **CacheDump** inverte la cifratura e ottiene gli hash, che poi **John the Ripper** cracka con brute-force/dizionario.

> [!info] Windows Credential Editor (di nuovo) 
> Estrae la password di login **in chiaro dalla RAM**, senza bisogno di crackare nessun hash. **Limite**: prende solo gli utenti _attualmente loggati_ (o a volte quelli che si erano loggati e poi sconnessi).

> [!warning] Contromisure ai cached credentials 
> Poco da fare (Microsoft offre una patch, KB Q184017, ma aiuta poco). Serve comunque privilegio Administrator/SYSTEM per prenderli → **evitare di farsi bucare come admin**. Non usare account di dominio ad alti privilegi per loggarsi sulle macchine locali (es. per avviare servizi); i **Domain Admin dovrebbero evitare connessioni RDP**; si può cambiare il valore di registro per azzerare le credenziali in cache — ma allora gli utenti non potranno loggarsi quando il DC è irraggiungibile (il solito trade-off compatibilità/sicurezza).

### Remote Control e Back Doors

> [!info] Riprendere il controllo 
> Le backdoor sono servizi che abilitano il controllo remoto. **Netcat per Windows** in ascolto che esegue `cmd` (con `-d` per stealth mode, nessuna console interattiva); ci si connette da un'altra macchina via `telnet IP porta` ottenendo una shell — **remote control senza logon**, molto pericoloso. **PsExec** (SysInternals): esecuzione di codice remoto via SMB (139/445) con username e password. **Metasploit** ha un'ampia gamma di payload backdoor. Controllo remoto **grafico**: Terminal Services/RDP (3389, non attivo di default) e **VNC** (gratuito, installabile da remoto, avvio stealth via registro). **Port redirection** con **Fpipe** (McAfee).

```text
# Netcat in ascolto sulla 8080 che serve una shell (concetto dalle slide)
nc -L -p 8080 -d -e cmd.exe

# Dall'altra macchina
TELNET <IP> 8080
```

### Covering Tracks

> [!info] Cancellare le tracce 
> Ottenuti privilegi Administrator/SYSTEM, l'intruso nasconde le prove, installa backdoor e nasconde un toolkit per rientrare. **Disabilitare l'auditing**: `auditpol /disable` (e `/enable` per riattivarlo). **Svuotare l'Event Log**: `ELsave` (scritto per NT). **Nascondere file**: `attrib +h` (nasconde blandamente) e gli **Alternate Data Streams (ADS)** — nascondere un file _dentro_ un altro, feature NTFS nata per compatibilità con Macintosh.

> [!info] ADS in pratica 
> Meccanismo: si allega un file allo stream di un altro file. Per file binari serve il `cp` POSIX (Resource Kit). Rilevamento con **LADS** o **SFIND** di Foundstone; per cancellare un ADS si copia il file su una partizione **FAT** e poi di nuovo su NTFS (FAT non supporta gli stream, quindi lo perde).

```text
# Nascondere netcat nello stream di un file esca
C:\> cp nc.exe oso001.009:nc.exe
# Recuperarlo
C:\> cp oso001.009:nc.exe nc.exe
# Eseguirlo direttamente dallo stream
start oso001.009:nc.exe
```

> [!info] Rootkit 
> Il modo migliore per nascondere file, account, backdoor e connessioni di rete su una macchina. Trattati in un capitolo dedicato.

> [!warning] Contromisure alla compromissione autenticata 
> Regola d'oro: una volta compromesso con privilegi admin, **reinstallare da zero** — non si può mai essere certi di aver rimosso tutte le backdoor. Se proprio si vuole ripulire, coprire **quattro aree**: File, chiavi di Registro, Processi, Porte di rete. File sospetti: nomi noti come `nc.exe`, antivirus, Tripwire per rilevare modifiche ai file di sistema. Registro sospetto: chiavi di backdoor note (WINVNC3, NetBus Server), rimosse con `reg delete`; attenzione agli **ASEP** (Autostart Extensibility Points). Processi sospetti: alto uso CPU, `schtasks`/task scheduler. Porte sospette: `netstat -aon`.

---

## Parte 3 — Windows Security Features

> [!info] L'arsenale difensivo Il rovescio del capitolo: cosa Windows offre per chiudere tutto quanto sopra.

|Feature|Cosa fa|
|---|---|
|**Windows Firewall**|Metafora "exception" per le app permesse; tutte le connessioni in ingresso bloccate di default|
|**Automated Updates**|Patch automatiche|
|**Security Center**|Per consumatori, non per professionisti IT|
|**Security Policy / Group Policy**|Impostazioni di sicurezza per macchina singola o grandi parchi macchine (domini)|
|**Microsoft Security Essentials**|Antimalware gratuito (real-time, scan, anti-rootkit, network inspection), di default in Win 8|
|**EMET** (Enhanced Mitigation Experience Toolkit)|Gestisce le mitigazioni: **DEP** e **ASLR**|
|**EFS** (Encrypting File System)|Cifra cartelle: chiave simmetrica cifrata con la chiave pubblica dell'utente e salvata come attributo del file; decifrata dalla privata prima del file|
|**BitLocker**|Cifra l'intero disco; **BitLocker To Go** (Win 7) cifra le USB removibili|
|**WRP** (Windows Resource Protection)|Protegge file e valori di registro da modifiche tramite ACL|
|**Integrity levels**|**MIC** (Mandatory Integrity Control): lega azioni a privilegi|
|**DEP** (Data Execution Prevention)|Marca porzioni di memoria come non eseguibili → blocca i buffer overflow|
|**Windows service hardening**|Isolamento risorse, least privilege, refactoring, accesso di rete ristretto, **session 0 isolation**|
|**Enhancement del compilatore**|Feature compile-time non configurabili: buffer security check (**GS**), **ASLR**, **SafeSEH**|

> [!info] EFS e Recovery Agent 
> Punto di attenzione: EFS ha un **Recovery Agent** per recuperare i file cifrati (utile quando un dipendente lascia l'azienda, ma pone problemi di privacy). Su Win 2000 e Server 2003 il **Local Administrator era il Default Recovery Agent** — grave buco di sicurezza, corretto da Win XP. La vulnerabilità primaria di EFS resta l'account Recovery Agent.

> [!info] BitLocker e cold boot 
> BitLocker cifra tutto il volume e conserva la chiave in modo sicuro, proteggendo da boot di OS alternativi. Attacco **cold boot**: si raffreddano i chip DRAM per allungare il tempo prima che la chiave venga cancellata dalla memoria volatile, e la si legge. Contromisura: separare la chiave _fisicamente_ in un modulo esterno removibile.

> [!info] Least privilege 
> Problema culturale: la maggior parte degli utenti Windows usa un account **Administrator tutto il tempo**, e molti servizi girano con privilegi admin — comodo ma pessimo per la sicurezza. Su XP/2003 e precedenti: loggarsi come utente limitato e usare **run as** per elevare solo quando serve.

> [!info] CIS 
> Il **Center for Internet Security** (nonprofit) fornisce benchmark di configurazione di sicurezza Microsoft e tool di scoring gratuiti (cisecurity.org).

---

## Riepilogo finale (i 14 punti delle slide)

> [!summary] Best practice conclusive
> 
> 1. Usare i benchmark **CIS**. 2) Approfondire con _Hacking Exposed Windows_. 3) Seguire i tool e le best practice su microsoft.com/security. 4) Non dimenticare le esposizioni di _altri_ prodotti Microsoft (es. SQL). 5) **Le applicazioni sono molto più vulnerabili dell'OS**. 6) Minimizzare i servizi = più sicurezza. 7) Disabilitare print e altri servizi inutili (es. SMB). 8) Usare Windows Firewall. 9) Proteggere i server esposti su Internet. 10) Tenere aggiornati service pack e patch. 11) Limitare logon interattivo ed escalation. 12) Usare Group Policy per distribuire configurazioni. 13) Sicurezza **fisica** contro gli attacchi offline. 14) Iscriversi a pubblicazioni di sicurezza.

---

## Fili rossi col resto del corso

> [!tip] Cosa lega il Cap. 4 ai precedenti **Retrocompatibilità = buco**: il pattern del Cap. 3 (NetBIOS, RestrictAnonymous, LDAP legacy) qui è la causa radice dichiarata (LM ancora attivo, null session). **SAM = /etc/passwd**: già emerso in enumeration, qui è il bersaglio del cracking. **La preda si usa**: gli account validi raccolti nel Cap. 3 sono l'input del password guessing di questo capitolo. **MSRPC/135**: l'endpoint mapper del Cap. 3 riappare come servizio-bersaglio dell'authentication spoofing. **Il ciclo completo** recon → enumeration → exploitation → post-exploitation si chiude qui: Cap. 2 apriva le porte, Cap. 3 dava i nomi, Cap. 4 entra e resta.

---

## Punti ancora aperti

> [!question] Da chiarire / verificare Le slide restano vaghe su: il dettaglio del meccanismo challenge-response NTLM oltre alla formula (perché tre chiavi da 7 byte, ereditato da DES/LM); il funzionamento preciso di SYSKEY; cosa distingue operativamente MIC / integrity levels da UAC. Da confermare se il capitolo rientra nello scope d'esame (finora certi solo Cap. 2 e 3 + binary/heap exploitation del lab).

> [!todo] Prossimi obiettivi Resta in coda l'**Homework #2** (Cap. 2 & 3, 180 punti). Quando arrivano le slide del capitolo successivo, continuare con lo stesso formato: nota Obsidian + chiarimenti a voce + handoff di fine sessione.