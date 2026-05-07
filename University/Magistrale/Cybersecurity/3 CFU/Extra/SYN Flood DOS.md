# SYN Flood & SYN Cookies

Tags: #networking #dos #tcp #nmap #hacking-exposed

---

## Il Three-Way Handshake (recap)

Per stabilire una connessione TCP, client e server eseguono:

```
Client  →  SYN          →  Server    (voglio connettermi)
Client  ←  SYN-ACK      ←  Server    (ok, aspetto conferma)
Client  →  ACK           →  Server    (connessione stabilita)
```

Il server, dopo aver risposto con SYN-ACK, **alloca una struttura in memoria** per tracciare la connessione in attesa di ACK. Queste connessioni parziali vivono nella **backlog queue** (coda delle half-open connections).

---

## SYN Flood — il meccanismo dell'attacco

Un attaccante manda un volume massiccio di pacchetti SYN **senza mai completare l'handshake**:

```
Attaccante  →  SYN (IP spoofato)  →  Server
Attaccante  ←  SYN-ACK            ←  Server   ← questo non arriva mai a nessuno
             [slot occupato in backlog]
             [timeout dopo ~75s]
             [slot liberato — ma ne arrivano altri 1000]
```

Il risultato:

- La backlog queue si **riempie completamente**
- Il server non riesce più ad accettare connessioni legittime
- **DoS effettivo** — non serve crashare il server, basta saturare la coda

### Perché lo spoofing è centrale

Se l'attaccante usa il suo IP reale, il kernel del server risponde con RST a ogni SYN-ACK non atteso, oppure i SYN-ACK tornano all'attaccante che li chiude. Con IP spoofati i SYN-ACK vanno nel vuoto → gli slot rimangono occupati per tutto il timeout.

---

## SYN Flood e Nmap — il caso specifico

Il SYN scan di Nmap (`-sS`) manda SYN e risponde con **RST** al SYN-ACK ricevuto, liberando lo slot:

```
Nmap  →  SYN       →  Target
Nmap  ←  SYN-ACK  ←  Target
Nmap  →  RST       →  Target   ← libera lo slot
```

### Quando Nmap può comunque stressare il target

Nmap parallelizza le probe su molte porte **contemporaneamente**. Prima che i RST vengano processati, decine di slot sono già occupati. Con flag aggressivi il rischio aumenta:

|Flag|Effetto|
|---|---|
|`-T5` (Insane)|Massima parallelizzazione, nessuna attesa|
|`--min-parallelism 100`|Forza almeno 100 probe simultanee|
|`-p-` (tutte le 65535 porte)|Volume totale enorme|
|Target con backlog piccolo|Si satura prima|
|RST perso/filtrato|Lo slot non viene mai liberato|

> ⚠️ Con timing default (`-T3`) il rischio è trascurabile. Con `-T5` su sistemi datati/non protetti può diventare reale.

---

## SYN Cookies — la contromisura

Inventati da **Daniel J. Bernstein** (djb) e **Eric Schenk** nel 1996. Oggi abilitati di default su Linux, FreeBSD, Windows Server moderni.

### Il problema che risolvono

La backlog queue ha dimensione fissa. Senza SYN cookies, ogni SYN ricevuto alloca subito una struttura in memoria → attaccabile per esaurimento.

### Come funzionano

L'idea chiave: **non allocare nulla finché l'handshake non è completo**.

Il server codifica tutto lo stato necessario **dentro il numero di sequenza del SYN-ACK** usando un hash crittografico:

```
ISN = hash(src_ip, src_port, dst_ip, dst_port, timestamp, secret)
      └── "cookie" — contiene tutto quello che serve
```

Flusso con SYN cookies:

```
Client   →  SYN                    →  Server
Client   ←  SYN-ACK (ISN=cookie)  ←  Server   ← NESSUNA allocazione di memoria
Client   →  ACK (cookie+1)         →  Server
              └── server verifica il cookie
                  se valido → alloca la struttura → connessione stabilita
```

Se l'ACK finale non arriva mai (flood), **non è stato allocato niente** → la backlog queue non si riempie mai.

### La verifica del cookie

Quando arriva l'ACK, il server:

1. Prende `ACK_number - 1` (che è l'ISN inviato)
2. Ricalcola l'hash con gli stessi parametri
3. Se coincide → ACK legittimo → crea la connessione
4. Se non coincide → scarta silenziosamente

### Limitazioni dei SYN cookies

|Limitazione|Dettaglio|
|---|---|
|**Opzioni TCP perse**|Window scaling, SACK, timestamps non possono essere negoziati (non c'è stato salvato) — alcune implementazioni moderni codificano 3 bit di opzioni nel cookie|
|**CPU overhead**|L'hash va calcolato per ogni SYN e ogni ACK, ma è trascurabile su hardware moderno|
|**Non proteggono da tutto**|Un flood sufficientemente grande può saturare la CPU o la banda comunque|

### Verificare se SYN cookies sono attivi (Linux)

```bash
# Controlla il valore (0=off, 1=on sotto pressione, 2=sempre on)
cat /proc/sys/net/ipv4/tcp_syncookies

# Abilitarli temporaneamente
sysctl -w net.ipv4.tcp_syncookies=1

# Abilitarli permanentemente
echo "net.ipv4.tcp_syncookies = 1" >> /etc/sysctl.conf
```

---

## Altre mitigazioni al SYN Flood

|Tecnica|Meccanismo|
|---|---|
|**SYN cookies**|Non allocare prima dell'ACK|
|**Firewall rate limiting**|Limita SYN/s per IP sorgente|
|**Backlog queue aumentata**|`net.ipv4.tcp_max_syn_backlog` — tampone, non soluzione|
|**TCP timeout ridotto**|Libera gli slot prima → `tcp_synack_retries`|
|**Anycast / scrubbing center**|Distribuisce/filtra il traffico upstream (DDoS enterprise)|

---

## Riferimenti

- _Hacking Exposed 7_ — Cap. Scanning, sezione TCP/IP attacks
- RFC 4987 — TCP SYN Flooding Attacks and Common Mitigations
- Daniel J. Bernstein — SYN cookies (https://cr.yp.to/syncookies.html)
- `man 7 tcp` — `tcp_syncookies`, `tcp_max_syn_backlog`