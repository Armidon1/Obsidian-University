## tags: [ethical-hacking, he7, ch5, post-exploitation, rootkit, network]

# Sniffer

> Componente di [[rootkits]] — HE7 Ch.5, sezione "Sniffers". Qui c'è anche la parte moderna: su questo argomento il libro è _fortemente_ datato (è il mondo pre-switch e pre-TLS).

## Concetto

Uno sniffer è un'utility di **network eavesdropping**: cattura, interpreta e immagazzina i pacchetti che attraversano una rete. È nato **come tool di debugging** — `tcpdump` e Wireshark sono strumenti legittimi da network engineer — ed è stato poi sovvertito a fini offensivi. È dual-use, come quasi tutto in questo capitolo.

Nel contesto di [[rootkits]] lo sniffer ha un ruolo unico: è il componente che **estende il raggio d'azione oltre la macchina compromessa**. Gli altri tre componenti (`[[trojan_binaries]]`, `[[backdoors]]`, `[[log_cleaning]]`) riguardano _quella_ box. Lo sniffer raccoglie credenziali e dati da **ogni host che parla con quella box** e da chiunque condivida il segmento — host del tutto ignari di essere spiati. È per questo che HE7 lo definisce _"perhaps the worst outcome"_ di una compromissione.

## Come funziona — la modalità promiscua

Una NIC Ethernet, in funzionamento normale, **filtra in hardware per indirizzo MAC**: tiene i frame destinati al proprio MAC (+ broadcast/multicast iscritti) e scarta tutto il resto.

Lo sniffer mette la scheda in **modalità promiscua**: il filtro MAC viene disattivato e la NIC consegna al sistema operativo **tutti** i frame che riceve fisicamente, non solo i propri. Da lì il software di sniffing cattura e analizza.

Limite intrinseco del meccanismo: uno sniffer sente solo il proprio **dominio di collisione/broadcast** — non vede traffico oltre router e switch. Da cui il corollario operativo di HE7: il **piazzamento conta**. Uno sniffer su un backbone o un punto di aggregazione vede ordini di grandezza più traffico di uno su un segmento isolato.

> [!tip] Filo conduttore — la portata _è_ il limite Il potere dello sniffer e il suo confine sono **lo stesso fatto**: sente tutto ciò che è "a portata d'orecchio", nulla fuori. Ogni evoluzione di questo argomento è una mossa su quel confine:
> 
> - l'**attaccante allarga l'orecchio** → ARP spoofing per dirottargli il traffico, piazzamento sul backbone;
> - il **difensore restringe l'orecchio** → switch (un dominio di collisione per host), VLAN, microsegmentazione SDN. E quando il payload diventa cifrato, la battaglia si sposta di nuovo: da "catturare i dati" a "catturare i metadati" o "rompere/aggirare la cifratura". **Sniffing → MITM.**

## Hub vs switch — perché lo sniffing passivo è cambiato

| |Shared Ethernet (hub)|Switched Ethernet|
|---|---|---|
|Inoltro|ogni frame a **tutti**|CAM table: frame solo alla **porta giusta**|
|Domini di collisione|uno solo, condiviso|uno **per porta**|
|Sniffer passivo sente|tutto|solo il proprio traffico + broadcast/multicast + unknown-unicast flooding|

Su uno switch lo sniffing passivo rende poco. Per sentire il traffico altrui bisogna passare **all'attivo**:

- **ARP spoofing** (HE7 lo chiama _arpredirect_, è `arpspoof` di dsniff; moderni: ettercap, bettercap) — avveleni la cache ARP della vittima così instrada i frame verso il _tuo_ MAC.
- **MAC flooding** (`macof`) — saturi la CAM table dello switch, che va in _fail-open_ e si comporta come un hub, floodando tutto.

HE7 rimanda al Ch.8 per il dettaglio → [[wireless_hacking]].

## Cosa cattura

L'esempio di HE7 è una sessione **telnet** (porta 23): lo sniffer ricostruisce login `guest/guest` _e_ l'intera cronologia dei comandi. I protocolli in chiaro perdono tutto — credenziali, mail, trasferimenti file.

La suite **dsniff** di Dug Song automatizza l'estrazione: `dsniff` (parsing credenziali per decine di protocolli), `urlsnarf`/`mailsnarf`/`msgsnarf`, più i tool MITM `arpspoof`/`macof`/`dnsspoof`/`sshmitm`/`webmitm`.

|Tool|Note|
|---|---|
|`tcpdump`|il classico, portato ovunque|
|`snoop`|sniffer incluso in Solaris|
|`dsniff`|suite offensiva, auto-estrazione credenziali|
|Wireshark / `tshark`|analisi con decoder per centinaia di protocolli|
|`bettercap`|il successore moderno di dsniff (MITM + sniffing)|
|Zeek, Suricata, Arkime|sniffer **difensivi** (NSM / full packet capture)|

## Countermeasures

HE7 dà tre approcci:

1. **Topologia switched** — toglie il broadcast generalizzato. Ma è aggirabile (ARP spoofing, MAC flooding) → mitiga lo script kiddie, non l'attaccante serio.
2. **Detection dello sniffer**:
    - _host-based_: verificare la modalità promiscua (`cpm` su UNIX; oggi `ip link` mostra il flag `PROMISC`); cercare il processo con `ps`/`lsof`; i log dello sniffer crescono molto. Limite: un intruso accorto maschera processo e nasconde i log.
    - _network-based_: Anti-Sniff (L0pht), sniffdet. Oggi più rilevanti **Dynamic ARP Inspection (DAI)**, **DHCP snooping** e **802.1X** sugli switch.
3. **Cifratura** (SSH, IPSec) — _"the long-term solution"_. È la risposta vera: se il payload è cifrato, lo sniffer cattura ciphertext.

## Stato moderno (2026)

Il mondo che HE7 descrive — hub, telnet, password in chiaro — non esiste più. Mappa aggiornata:

- **Shared Ethernet estinto.** Lo sniffing _passivo_ del payload su una LAN moderna è quasi inutile: vedi solo il tuo traffico + ciphertext altrui.
- **Lo sniffing si è spostato sull'attivo.** Non "ascolto", ma "mi metto in mezzo": ARP poisoning, DHCP spoofing, e il classico Windows **LLMNR/NBT-NS poisoning** (Responder) → ATT&CK T1557.
- **La cifratura ovunque ha ucciso l'harvest di credenziali in chiaro.** TLS è il default (HTTPS via Let's Encrypt, HSTS, HTTP/2-3), SSH ha rimpiazzato telnet/rlogin, la mail usa STARTTLS/TLS implicito.
- **Risposta dell'attaccante alla cifratura:**
    - _TLS stripping_ — `sslstrip` (Moxie Marlinspike) declassava HTTPS→HTTP. Oggi quasi morto grazie a **HSTS**, HSTS preload e browser che vanno in HTTPS di default.
    - _TLS interception_ — presentare un certificato falso: fallisce contro la validazione del cert **a meno che** il client non si fidi della tua CA. È esattamente ciò che fanno (legittimamente) i proxy MITM aziendali; offensivamente serve una CA canaglia o un cert rubato.
- **Anche con TLS, i metadati colano:** lo **SNI** è in chiaro nell'handshake TLS (rivela il dominio → in arrivo **ECH**, Encrypted Client Hello), le query **DNS** sono in chiaro (→ DoH/DoT, vedi [[dns_attacks]]), e l'analisi di dimensioni/timing dei pacchetti dice molto. Sniffare oggi è più _metadata e traffic analysis_ che payload.
- **WiFi:** la **monitor mode** è l'analogo wireless della modalità promiscua. Su WiFi aperto tutto è visibile; su WPA2 puoi decifrare se hai la PSK e il 4-way handshake catturato → ponte diretto col Ch.8 [[wireless_hacking]].
- **Cloud / virtualizzazione — il modello HE7 non si applica proprio.** Non c'è un "filo" fisico. I vSwitch (es. VMware) **rifiutano la modalità promiscua di default**; su AWS la rete è SDN e _non ti consegna proprio_ il traffico di altre istanze — non puoi sniffare il vicino. Il packet capture esiste solo come funzione **sanzionata** (VPC Traffic Mirroring). Il "pianta uno sniffer sul segmento" non ha più un segmento su cui atterrare.
- **Conclusione difensiva:** la difesa è convergente su _"assumi la rete ostile"_ → zero-trust, cifratura end-to-end, mTLS, certificate pinning. La contromisura di rete (switch) è sempre stata parziale; la difesa vera è la cifratura — più la topologia che si dissolve dentro l'SDN.

## Mapping MITRE ATT&CK

|Tecnica|ID|
|---|---|
|Network Sniffing|T1040|
|Adversary-in-the-Middle|T1557|
|— LLMNR/NBT-NS Poisoning & SMB Relay|T1557.001|
|— ARP Cache Poisoning|T1557.002|
|— DHCP Spoofing|T1557.003|

## Collegamenti

- Nota-hub: [[rootkits]]
- ARP spoofing / sovversione dello switch — dettaglio nel Ch.8: [[wireless_hacking]]
- La cifratura come risposta vera: [[openssh_security]] · [[openssl_security]]
- ARP spoof + DNS spoof = combo classica di Ettercap; metadati DNS in chiaro: [[dns_attacks]]