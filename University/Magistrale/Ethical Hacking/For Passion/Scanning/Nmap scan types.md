# Nmap — Tipi di Scan

Tags: #nmap #scanning #networking #hacking-exposed

---

## Prerequisiti rapidi

|Privilegio richiesto|Perché|
|---|---|
|**root / sudo**|Può forgiare raw packets (SYN, FIN, Xmas…)|
|**utente normale**|Solo syscall `connect()` del SO → solo `-sT`|

> Default con root → `-sS` | Default senza root → `-sT`

---

## 1. TCP Connect Scan `-sT`

**Privilegio**: utente normale (o root) **Risultato**: connessione completa — **appare nei log applicativi**

```
# Porta APERTA
Nmap ──── SYN ────────────► Target
Nmap ◄─── SYN-ACK ──────── Target
Nmap ──── ACK ────────────► Target   ← handshake completo
Nmap ──── RST/FIN ────────► Target   ← chiude subito

# Porta CHIUSA
Nmap ──── SYN ────────────► Target
Nmap ◄─── RST+ACK ───────── Target
```

|Stato|Risposta|
|---|---|
|Aperta|SYN-ACK|
|Chiusa|RST|
|Filtrata|Silenzio (timeout)|

---

## 2. TCP SYN Scan (Half-Open) `-sS`

**Privilegio**: root **Risultato**: handshake incompleto — **non appare nei log applicativi**

```
# Porta APERTA
Nmap ──── SYN ────────────► Target
Nmap ◄─── SYN-ACK ──────── Target
Nmap ──── RST ────────────► Target   ← non completa mai l'handshake

# Porta CHIUSA
Nmap ──── SYN ────────────► Target
Nmap ◄─── RST+ACK ───────── Target
```

|Stato|Risposta|
|---|---|
|Aperta|SYN-ACK|
|Chiusa|RST|
|Filtrata|Silenzio (timeout)|

> ⚡ Lo scan più veloce e comune. Default con root.

---

## 3. TCP FIN Scan `-sF`

**Privilegio**: root **Funziona su**: Linux/BSD — **NON su Windows**

```
# Porta APERTA (RFC 793)
Nmap ──── FIN ────────────► Target
                             [silenzio — lo stack ignora]

# Porta CHIUSA (RFC 793)
Nmap ──── FIN ────────────► Target
Nmap ◄─── RST ───────────── Target
```

|Stato|Risposta|
|---|---|
|Aperta|Silenzio|
|Chiusa|RST|
|Filtrata|Silenzio|

> ⚠ Aperta e Filtrata sono indistinguibili → Nmap riporta `open|filtered`

---

## 4. TCP NULL Scan `-sN`

**Privilegio**: root **Funziona su**: Linux/BSD — **NON su Windows**

Manda un pacchetto **senza nessun flag** impostato.

```
# Porta APERTA
Nmap ──── [no flags] ─────► Target
                             [silenzio]

# Porta CHIUSA
Nmap ──── [no flags] ─────► Target
Nmap ◄─── RST ───────────── Target
```

|Stato|Risposta|
|---|---|
|Aperta|Silenzio|
|Chiusa|RST|

---

## 5. TCP Xmas Scan `-sX`

**Privilegio**: root **Funziona su**: Linux/BSD — **NON su Windows**

Manda un pacchetto con **FIN + URG + PSH** tutti accesi ("albero di Natale").

```
# Porta APERTA
Nmap ──── FIN+URG+PSH ────► Target
                             [silenzio]

# Porta CHIUSA
Nmap ──── FIN+URG+PSH ────► Target
Nmap ◄─── RST ───────────── Target
```

|Stato|Risposta|
|---|---|
|Aperta|Silenzio|
|Chiusa|RST|

---

## 6. TCP ACK Scan `-sA`

**Privilegio**: root **Scopo**: **non** rivela porte aperte — mappa le **regole del firewall**

```
Nmap ──── ACK ────────────► Target

# Porta non filtrata (firewall assente o stateless)
Nmap ◄─── RST ───────────── Target   → UNFILTERED

# Porta filtrata (firewall blocca il pacchetto)
                             [silenzio o ICMP unreachable] → FILTERED
```

|Risposta|Interpretazione|
|---|---|
|RST|Porta **unfiltered** (raggiungibile)|
|Silenzio / ICMP|Porta **filtered** (firewall presente)|

> 📌 Non dice se la porta è aperta o chiusa — dice solo se c'è un firewall davanti.

---

## 7. TCP Window Scan `-sW`

**Privilegio**: root **Scopo**: come ACK scan, ma sfrutta il **valore del campo Window** nel RST

Alcuni stack TCP impostano un Window Size > 0 nel RST se la porta è aperta, 0 se è chiusa. Comportamento OS-dipendente.

```
Nmap ──── ACK ────────────► Target
Nmap ◄─── RST ───────────── Target

# Window > 0  →  porta APERTA
# Window = 0  →  porta CHIUSA
```

> ⚠ Inaffidabile su molti sistemi moderni.

---

## 8. TCP Maimon Scan `-sM`

**Privilegio**: root

Manda un pacchetto **FIN + ACK**. Su alcuni sistemi BSD, le porte aperte non rispondono (come FIN/NULL/Xmas). Oggi quasi nessun sistema si comporta così.

```
Nmap ──── FIN+ACK ────────► Target

# Porta APERTA (su certi BSD)
                             [silenzio]

# Porta CHIUSA
Nmap ◄─── RST ───────────── Target
```

> 🕰 Scan storico, raramente utile oggi.

---

## 9. UDP Scan `-sU`

**Privilegio**: root **Lento**: nessuna risposta attesa → dipende dai timeout ICMP

```
# Porta APERTA
Nmap ──── UDP payload ────► Target
                             [silenzio o risposta UDP]   → open

# Porta CHIUSA
Nmap ──── UDP payload ────► Target
Nmap ◄─── ICMP port unreachable ── Target               → closed

# Porta FILTRATA
Nmap ──── UDP payload ────► Target
                             [silenzio o ICMP filtered]  → open|filtered
```

|Risposta|Stato|
|---|---|
|Risposta UDP|Aperta|
|ICMP port unreachable (type 3 code 3)|Chiusa|
|Altri ICMP unreachable|Filtrata|
|Silenzio|open\|filtered|

> ⏱ Molto lento: usa `-sU --top-ports 100` per limitare i tempi.

---

## 10. Idle / Zombie Scan `-sI <zombie>`

**Privilegio**: root **Caratteristica**: il tuo IP reale **non appare mai** nel traffico verso il target

Sfrutta un host "zombie" con IP ID incrementale prevedibile.

```
# Fase 1 — campiona l'IP ID dello zombie
Nmap ──── SYN+ACK ───────► Zombie
Nmap ◄─── RST (IP ID=N) ── Zombie

# Fase 2 — manda SYN al target spacciandosi per lo zombie
Nmap ──── SYN (src=Zombie) ──────────► Target

  [Se porta APERTA]
  Target ◄─── SYN+ACK ──────────────── → Zombie   ← zombie riceve SYN-ACK
  Zombie ──── RST (IP ID=N+2) ─────── → Target    ← zombie risponde con RST e incrementa ID

  [Se porta CHIUSA]
  Target ◄─── RST ──────────────────── → Zombie   ← zombie ignora
  IP ID zombie rimane N+1

# Fase 3 — ricampiona IP ID dello zombie
Nmap ──── SYN+ACK ───────► Zombie
Nmap ◄─── RST (IP ID=?) ── Zombie

  IP ID = N+2  →  porta TARGET APERTA
  IP ID = N+1  →  porta TARGET CHIUSA
```

> 🕵️ Lo scan più stealth esistente. Richiede uno zombie con IP ID incrementale (sempre più raro).

---

## 11. SCTP INIT Scan `-sY`

**Privilegio**: root **Protocollo**: SCTP (alternativa a TCP usata in VoIP/telecomunicazioni)

```
# Porta APERTA
Nmap ──── INIT ───────────► Target
Nmap ◄─── INIT-ACK ──────── Target
Nmap ──── ABORT ──────────► Target   ← non completa l'handshake 4-way

# Porta CHIUSA
Nmap ──── INIT ───────────► Target
Nmap ◄─── ABORT ─────────── Target
```

---

## 12. SCTP COOKIE-ECHO Scan `-sZ`

**Privilegio**: root

```
# Porta APERTA
Nmap ──── COOKIE-ECHO ────► Target
                             [silenzio]

# Porta CHIUSA
Nmap ──── COOKIE-ECHO ────► Target
Nmap ◄─── ABORT ─────────── Target
```

> 🔇 Più silenzioso dell'INIT scan ma aperta e filtrata sono indistinguibili.

---

## 13. IP Protocol Scan `-sO`

**Scopo**: non scansiona porte ma **protocolli IP** supportati dall'host (TCP=6, UDP=17, ICMP=1, OSPF=89…)

```
Nmap ──── IP header (proto=X, no payload) ──► Target

# Protocollo supportato
  risposta qualsiasi   → OPEN

# Protocollo non supportato
  ICMP proto unreachable (type 3 code 2)  → CLOSED

# Filtrato
  silenzio o altri ICMP → FILTERED
```

---

## 14. Ping Scan (Host Discovery) `-sn`

**Scopo**: scoprire quali host sono **vivi** nella rete, senza scansionare porte

```
Nmap ──── ICMP echo request ──► Host
Nmap ◄─── ICMP echo reply ──── Host   → host UP

# (con root aggiunge anche ARP su LAN e TCP SYN su 443/80)
```

> 🔍 Usato spesso prima dello scan vero: `nmap -sn 192.168.1.0/24`

---

## Riepilogo generale

|Flag|Nome|Privilegio|Windows|Stealth|Scopo|
|---|---|---|---|---|---|
|`-sT`|TCP Connect|utente|✅|❌|Default senza root|
|`-sS`|SYN (Half-Open)|root|✅|⭐|Default con root|
|`-sF`|FIN|root|❌|⭐⭐|Evasione IDS|
|`-sN`|NULL|root|❌|⭐⭐|Evasione IDS|
|`-sX`|Xmas|root|❌|⭐⭐|Evasione IDS|
|`-sA`|ACK|root|✅|⭐|Firewall mapping|
|`-sW`|Window|root|parziale|⭐|Firewall mapping|
|`-sM`|Maimon|root|❌|⭐|Storico|
|`-sU`|UDP|root|✅|-|Porte UDP|
|`-sI`|Idle/Zombie|root|✅|⭐⭐⭐|Anonimato totale|
|`-sY`|SCTP INIT|root|❌|⭐|Reti VoIP/telecom|
|`-sZ`|SCTP COOKIE|root|❌|⭐⭐|Reti VoIP/telecom|
|`-sO`|IP Protocol|root|✅|-|Protocolli IP host|
|`-sn`|Ping/Discovery|entrambi|✅|-|Host discovery|

---

## Riferimenti

- _Hacking Exposed 7_ — Cap. Scanning
- `man nmap` — sezione "SCAN TECHNIQUES"
- Nmap Book: https://nmap.org/book/man-port-scanning-techniques.html
- RFC 793 — Transmission Control Protocol