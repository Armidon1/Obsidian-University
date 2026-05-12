# NetBT — NetBIOS over TCP/IP

Tags: #networking #enumeration #netbios #windows #hacking-exposed

---

## Cos'è

NetBT (NetBIOS over TCP/IP) è il **layer di trasporto** che permette ai tre servizi NetBIOS di funzionare su reti TCP/IP moderne. È definito negli **RFC 1001 e RFC 1002** (1987).

NetBT non è un servizio separato — è il **collante** che mappa i servizi NetBIOS sulle porte TCP/IP:

```
Applicazione Windows (file sharing, browser service...)
         ↓
    NetBIOS API
         ↓
      NetBT          ← questo layer
         ↓
     TCP/IP
         ↓
      Rete
```

---

## Perché esiste

NetBIOS nasce nel 1983 per reti locali IBM — non era pensato per TCP/IP, lavorava su protocolli proprietari come NBF (NetBEUI). Quando le reti aziendali migrarono verso TCP/IP negli anni '90, Microsoft aveva bisogno di far girare NetBIOS su questa infrastruttura senza riscrivere tutto. NetBT è la soluzione — un adapter layer.

---

## Il mapping porte

NetBT mappa i tre servizi NetBIOS su porte TCP/IP standard:

|Servizio NetBIOS|Porta NetBT|Protocollo|
|---|---|---|
|Name Service (NBNS)|**UDP/TCP 137**|Query nomi, registrazione|
|Datagram Service (NBDS)|**UDP 138**|Broadcast, messaggi connectionless|
|Session Service (NBSS)|**TCP 139**|Connessioni dati, SMB legacy|

---

## NetBT vs SMB diretto (porta 445)

Questa è la distinzione più importante da capire:

```
Architettura legacy (Windows NT/2000/XP):
┌─────────────────────┐
│   SMB (applicazione)│
├─────────────────────┤
│   NetBIOS Session   │
├─────────────────────┤
│       NetBT         │  ← necessario
├─────────────────────┤
│      TCP/IP         │
└─────────────────────┘
      porta 139

Architettura moderna (Windows 2000+):
┌─────────────────────┐
│   SMB (applicazione)│
├─────────────────────┤
│      TCP/IP         │  ← SMB diretto, NetBT non necessario
└─────────────────────┘
      porta 445
```

| |NetBT + SMB (139)|SMB diretto (445)|
|---|---|---|
|NetBIOS richiesto|Sì|No|
|Introdotto|Windows NT|Windows 2000|
|Uso oggi|Legacy/compatibilità|Standard moderno|
|Disabilitabile|Sì (consigliato)|No (SMB core)|

---

## Risoluzione nomi con NetBT

Quando una macchina Windows deve risolvere un nome (es. `\\FILESERVER`), NetBT segue un ordine preciso:

```
1. Cache locale NetBIOS
         ↓ (miss)
2. WINS server (se configurato)
         ↓ (miss o assente)
3. Broadcast UDP 137 sulla subnet
         ↓ (miss)
4. File LMHOSTS (C:\Windows\System32\drivers\etc\lmhosts)
         ↓ (miss)
5. DNS
         ↓ (miss)
6. File HOSTS
```

> Questo ordine è rilevante per gli attacchi: un attaccante sulla stessa subnet può rispondere al broadcast (step 3) prima del server legittimo → **NBNS spoofing**

---

## Abilitare e disabilitare NetBT

### Verificare lo stato

```cmd
# Da Windows — verifica nelle proprietà di rete
ipconfig /all | findstr "NetBIOS"

# Con PowerShell
Get-WmiObject Win32_NetworkAdapterConfiguration | Select-Object -Property Description, TcpipNetbiosOptions
```

`TcpipNetbiosOptions`:

- `0` = Default (usa impostazione DHCP)
- `1` = Abilitato
- `2` = **Disabilitato**

### Disabilitare NetBT (contromisura consigliata)

```
Pannello di controllo
→ Centro connessioni di rete
→ Modifica impostazioni scheda
→ Proprietà connessione
→ TCP/IPv4 → Proprietà → Avanzate
→ Tab WINS
→ "Disabilita NetBIOS su TCP/IP"
```

```powershell
# PowerShell — disabilita su tutti gli adapter
$adapters = Get-WmiObject Win32_NetworkAdapterConfiguration
foreach ($adapter in $adapters) {
    $adapter.SetTcpipNetbios(2)
}
```

---

## Rilevamento con Nmap

```bash
# Scan base delle porte NetBT
nmap -p 137,138,139 192.168.1.50

# UDP scan per 137 e 138
sudo nmap -sU -p 137,138 192.168.1.50

# Scan completo con versione e script
sudo nmap -sU -sS -p U:137,138,T:139,445 -sV 192.168.1.50

# NSE — enumerazione NetBIOS
nmap --script nbstat 192.168.1.50
```

### Output tipico `--script nbstat`

```
Host script results:
| nbstat:
|   NetBIOS name: DESKTOP-CORP01
|   NetBIOS user: JOHN
|   NetBIOS MAC: 00:0c:29:aa:bb:cc (VMware)
|   Names:
|     DESKTOP-CORP01<00>  Flags: <unique><active>
|     CORPORATE<00>       Flags: <group><active>
|     DESKTOP-CORP01<20>  Flags: <unique><active>
```

---

## Attacchi che sfruttano NetBT

|Attacco|Porta|Descrizione|
|---|---|---|
|**NBNS Spoofing**|UDP 137|Risponde a broadcast con IP falso|
|**NBDS Sniffing**|UDP 138|Cattura annunci broadcast passivamente|
|**Null Session**|TCP 139|Connessione IPC$ senza credenziali|
|**SMB Relay**|TCP 139/445|Relay di autenticazione NTLM|
|**Responder**|137+138|Poisoning combinato NBNS+LLMNR|

---

## NetBT e LLMNR — il duo Responder

NetBT non lavora mai da solo in un ambiente moderno — si affianca a **LLMNR (Link-Local Multicast Name Resolution, UDP 5355)** che svolge un ruolo simile. Entrambi vengono sfruttati insieme da Responder:

```bash
sudo responder -I eth0
# Ascolta e avvelena:
# → UDP 137  (NBNS)
# → UDP 138  (NBDS)
# → UDP 5355 (LLMNR)
# → UDP 5353 (mDNS)
```

Quando una macchina cerca un nome che non trova in DNS, cade su LLMNR o NBNS → Responder risponde → cattura hash NTLMv2.

---

## Contromisure

|Contromisura|Effetto|
|---|---|
|Disabilitare NetBT su tutti gli adapter|Elimina UDP 137, 138, TCP 139|
|Disabilitare LLMNR (Group Policy)|Rimuove il fallback LLMNR|
|Bloccare UDP 137/138 e TCP 139 sul firewall|Impedisce exploit da rete esterna|
|Usare DNS interno affidabile|Riduce i casi in cui si cade su NBNS/LLMNR|
|Monitorare broadcast anomali su 137/138|Rileva Responder in esecuzione|

> Disabilitare NetBT **e** LLMNR insieme è la contromisura più efficace contro Responder.

---

## Rilevanza oggi

NetBT è tecnicamente obsoleto su reti pure Windows moderne — SMB diretto su 445 non ne ha bisogno. Tuttavia rimane abilitato di default su Windows per compatibilità con:

- Dispositivi legacy (stampanti di rete, NAS vecchi)
- Applicazioni che usano ancora le API NetBIOS
- Ambienti misti con sistemi datati

Su HTB trovi NetBT abilitato quasi sempre — è parte integrante dell'enumerazione Windows classica.

---

## Riferimenti

- _Hacking Exposed 7_ — Cap. Enumeration
- RFC 1001 — NetBIOS over TCP/IP: Concepts and Methods
- RFC 1002 — NetBIOS over TCP/IP: Detailed Specifications
- Responder: https://github.com/lgandx/Responder
- → vedi anche: [[NetBIOS_NBNS]] (UDP 137)
- → vedi anche: [[NetBIOS_NBDS]] (UDP 138)
- → vedi anche: [[NetBIOS_NBSS]] (TCP 139)