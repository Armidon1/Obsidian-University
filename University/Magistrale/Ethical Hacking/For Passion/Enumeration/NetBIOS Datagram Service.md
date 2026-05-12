# NetBIOS Datagram Service (NBDS) — UDP 138

Tags: #networking #enumeration #netbios #windows #hacking-exposed

---

## Cos'è

NBDS è il secondo dei tre servizi NetBIOS. Gira su **UDP 138** e si occupa di **messaggi connectionless** — broadcast e multicast sulla rete locale. Non stabilisce connessioni, non garantisce la consegna, non aspetta risposta.

---

## Le tre porte NetBIOS — recap

|Porta|Protocollo|Servizio|Scopo|
|---|---|---|---|
|UDP 137|NetBIOS-NS|Name Service|Registrazione e risoluzione nomi|
|**UDP 138**|**NetBIOS-DGM**|**Datagram Service**|**Messaggi connectionless e broadcast**|
|TCP 139|NetBIOS-SSN|Session Service|Trasferimento dati reale (file/print sharing)|

---

## Come funziona

NBDS trasporta **datagrammi NetBIOS** — piccoli messaggi inviati senza stabilire una connessione. Tre modalità:

```
# Unicast — da uno a uno
MACCHINA-A → UDP 138 → MACCHINA-B

# Broadcast — da uno a tutti sulla subnet
MACCHINA-A → UDP 138 → 192.168.1.255  (broadcast)

# Multicast — da uno a un gruppo
MACCHINA-A → UDP 138 → gruppo multicast
```

Poiché usa UDP e broadcast, funziona **solo sulla stessa subnet** — i datagrammi non attraversano i router.

---

## A cosa serve nel contesto Windows

NBDS è il canale di trasporto per servizi Windows che usano broadcast sulla LAN:

|Servizio Windows|Cosa usa NBDS per|
|---|---|
|**Browser Service**|Annunci di presenza macchine sulla rete (`net view`)|
|**Messenger Service**|Messaggi `net send` tra utenti (Windows XP e precedenti)|
|**Logon Service**|Annunci del domain controller sulla subnet|
|**WINS replication**|Replica tra server WINS in reti grandi|

### Browser Service — il più importante

Il Browser Service usa NBDS per i **host announcements** — ogni macchina Windows broadcastava periodicamente il proprio nome e servizi:

```
DESKTOP-CORP01 → broadcast UDP 138 → "Sono online, offro questi servizi: file sharing, print..."
```

Questi annunci vengono raccolti dal **Master Browser** che costruisce la lista visibile con `net view`.

---

## Perché è interessante per l'enumerazione

NBDS in sé non è direttamente interrogabile come NBNS (non ha query/response). Il suo valore per l'attaccante è **passivo** — **sniffando il traffico UDP 138** si raccolgono informazioni senza inviare nulla:

```bash
# Cattura traffico NetBIOS Datagram con tcpdump
sudo tcpdump -i eth0 udp port 138

# Con Wireshark — filtra
udp.port == 138
```

### Cosa si vede sniffando UDP 138

- Nomi di tutte le macchine che si annunciano
- Dominio/workgroup di appartenenza
- Servizi offerti (file sharing, print sharing…)
- Nome del Master Browser della subnet
- Traffico del Domain Controller che annuncia la propria presenza

---

## NBDS e Responder

Come NBNS (UDP 137), anche NBDS è sfruttato da **Responder** per il poisoning. Responder ascolta i broadcast su UDP 138 e può rispondere a certi tipi di messaggi per indirizzare le vittime verso l'attaccante.

```bash
sudo responder -I eth0
# Responder ascolta sia UDP 137 (NBNS) che UDP 138 (NBDS)
# oltre a LLMNR (UDP 5355) e mDNS (UDP 5353)
```

> In pratica NBNS spoofing (137) è più diretto ed efficace per la cattura di hash. NBDS (138) è più utile per enumerazione passiva via sniffing.

---

## Differenza con NBNS

| |NBNS (UDP 137)|NBDS (UDP 138)|
|---|---|---|
|Tipo di comunicazione|Request/Response|Connectionless, broadcast|
|Interrogabile attivamente|Sì (query dirette)|No (solo sniffing passivo)|
|Scopo principale|Risoluzione nomi|Messaggi e annunci broadcast|
|Valore per enumerazione|Alto — query dirette|Medio — sniffing passivo|
|Sfruttabile con Responder|Sì|Parzialmente|

---

## Rilevanza oggi

Il Browser Service — il principale utilizzatore di NBDS — è **disabilitato di default** su:

- Windows 10 build 1709+
- Windows Server 2019+

Su reti moderne quasi tutto il discovery avviene via **DNS + Active Directory**, rendendo NBDS sempre meno rilevante. Rimane presente su:

- Reti legacy con Windows 7/8/Server 2012
- Reti miste con dispositivi embedded o stampanti di rete
- Macchine HTB che simulano ambienti datati

---

## Contromisure

- Disabilitare NetBIOS over TCP/IP dove non necessario
- Bloccare UDP 138 sul perimetro di rete
- Disabilitare il Browser Service su tutte le macchine moderne
- Monitorare broadcast anomali su UDP 138 con IDS

---

## Riferimenti

- _Hacking Exposed 7_ — Cap. Enumeration
- RFC 1002 — NetBIOS Protocol Standard
- `man tcpdump`
- Responder: https://github.com/lgandx/Responder
- → vedi anche: [[NetBIOS_NBNS]] (UDP 137)
- → vedi anche: [[NetBIOS_SSN]] (TCP 139)