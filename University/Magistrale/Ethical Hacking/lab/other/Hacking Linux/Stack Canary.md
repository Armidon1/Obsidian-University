# Stack Canary

> [!abstract] In una frase 
> Un valore casuale inserito dal compilatore **tra le variabili locali e il return address**: se un overflow lo corrompe, il programma viene terminato prima che `ret` venga eseguito. È una difesa contro il buffer overflow classico.

Collegamento: [[ETHL 0x07 — Binary Exploitation p1]] · [[Call Stack]] · [[Buffer Overflow]]

---

## 1. Perché esiste

Il bersaglio di un buffer overflow è il **return address**: se lo sovrascrivi, controlli `rip`, e quindi controlli l'esecuzione del programma.

Il problema per l'attaccante: per arrivare al return address, un overflow sulle variabili locali deve **attraversare tutta la memoria tra il buffer e il return address**. Il canary sta esattamente lì, nel mezzo, come un sensore d'allarme.

---

## 2. Dove sta sullo stack

![[Pasted image 20260616194406.png]]

```
indirizzo basso  (cima dello stack, RSP punta qui)
┌─────────────────────────────────┐
│   variabili locali / buffer     │ ← overflow parte da qui ↓
├─────────────────────────────────┤
│   CANARY  (8 byte)              │ ← [rbp - 0x8] — il guardiano
├─────────────────────────────────┤
│   saved RBP                     │ ← [rbp]
├─────────────────────────────────┤
│   return address                │ ← [rbp + 0x8] — bersaglio
└─────────────────────────────────┘
indirizzo alto
```

> [!warning] La posizione è intenzionale Un overflow lineare (scrittura continua oltre i limiti del buffer) **deve** attraversare il canary prima di raggiungere il return address. Non puoi saltarlo senza corromperlo.

---

## 3. Dove vive il valore originale: `fs:0x28`

`fs` è un **segment register** che punta alla **TLS** (Thread Local Storage) — un'area di memoria per thread, separata dallo stack.

All'avvio del programma, il kernel genera un valore casuale e lo deposita all'offset `0x28` di questa area. Questa è la **fonte di verità**: il canary sullo stack viene confrontato con questo valore nell'epilogo.

> [!tip] Perché in TLS e non sullo stack? Se il valore originale stesse anch'esso sullo stack, un overflow potrebbe sovrascrivere anche quello. Tenendolo in una zona separata (`fs:0x28`), il confronto è sempre affidabile.

---

## 4. Implementazione in assembly

### Prologo — piazza il canary

```asm
mov    rax, QWORD PTR fs:0x28    ; leggi il valore casuale dalla TLS
mov    QWORD PTR [rbp-0x8], rax  ; copialo sullo stack subito sotto rbp
xor    eax, eax                  ; azzera rax (non lasciare il canary in un registro)
```

In italiano:

1. Prendi il valore segreto dalla TLS → mettilo in `rax`
2. Copialo sullo stack a `[rbp - 0x8]` (subito sopra il saved RBP)
3. Azzera `rax` così il valore non rimane esposto in un registro

### Epilogo — verifica il canary

```asm
mov    rdx, QWORD PTR [rbp-0x8]  ; leggi il canary dallo stack
sub    rdx, QWORD PTR fs:0x28    ; sottrai l'originale
je     <fun+62>                   ; se zero (non cambiato) → tutto ok, continua
call   __stack_chk_fail@plt      ; se diverso → abort immediato
leave
ret
```

Il `sub` fa la differenza tra i due valori:

- Canary intatto → differenza = 0 → `je` salta al `leave`/`ret` normale
- Canary corrotto → differenza ≠ 0 → si cade in `__stack_chk_fail` → programma terminato

> [!danger] Il programma muore PRIMA di `ret` Questo è il punto chiave: l'overflow ha già corrotto il return address, ma il canary viene controllato **prima** che `ret` venga eseguito. Il controllo del flusso non viene mai ceduto all'attaccante.

---

## 5. Il flusso completo con un overflow

```
Situazione normale:
  buffer overflow → sovrascrive variabili locali
                 → sovrascrive CANARY   ← rilevato nell'epilogo → abort
                 → sovrascrive saved rbp
                 → sovrascrive return address  (non si arriva mai qui)

Situazione senza canary:
  buffer overflow → sovrascrive variabili locali
                 → sovrascrive saved rbp
                 → sovrascrive return address → ret → rip controllato dall'attaccante ✓
```

---

## 6. La proprietà NULL-terminated

> [!question] Trappola d'esame — perché il byte basso del canary è sempre `0x00`? Il canary su Linux è sempre nella forma `0x00XXXXXXXXXXXXXXXX`: il **byte meno significativo è zero**.
> 
> **Motivo**: molte vulnerabilità sfruttano funzioni su stringhe (`strcpy`, `gets`, `scanf`) che si fermano al byte null `\x00`. Se il canary inizia con `\x00`, queste funzioni non riescono a **leggere** il canary tramite un overflow di stringa — il byte null blocca la copia prima che arrivi al canary.
> 
> In pratica: rende più difficile fare un **leak** del canary usando le stesse funzioni vulnerabili, perché la lettura si fermerebbe al primo `\x00`.

---

## 7. Limiti — quando il canary non basta

Il canary protegge dagli **overflow lineari** (scrittura continua che sovrascrive tutto in sequenza). Non protegge da:

|Tecnica bypass|Come funziona|
|---|---|
|**Canary leak**|Si legge il valore del canary (via format string o out-of-bounds read), poi lo si riscrivi corretto nell'exploit|
|**Brute force su fork**|Se il processo non cambia il canary tra un fork e l'altro, si può indovinare byte per byte|
|**Overwrite parziale**|Vulnerabilità che permettono di scrivere a un offset arbitrario, saltando il canary|
|**Heap overflow**|Il canary protegge solo lo stack — heap e altri vettori sono fuori scope|

> [!note] Il canary protegge il return address, non le variabili locali Un overflow può comunque corrompere variabili locali e il saved RBP **prima** del canary, causando comportamenti indesiderati senza necessariamente triggerare il check.

---

## 8. Come riconoscerlo: `checksec`

```bash
checksec --file=./mioprogramma
```

Output tipico con canary:

```
Stack:    Canary found
```

Output senza:

```
Stack:    No canary found
```

In GEF (GDB Enhanced Features):

```
checksec      # mostra tutte le protezioni del binario corrente
```

---

## 9. Richiamo attivo

> [!question] Verifica (a libro chiuso)
> 
> 1. Dove sta il canary sullo stack rispetto a variabili locali, saved RBP e return address?
> 2. Perché il valore originale è in `fs:0x28` e non sullo stack stesso?
> 3. Cosa fa `sub rdx, QWORD PTR fs:0x28` nell'epilogo? Perché si usa `sub` e non `cmp`?
> 4. Perché il programma può rilevare l'overflow **prima** che `ret` venga eseguito?
> 5. Perché il byte basso del canary è `0x00`? Cosa impedisce esattamente?
> 6. Un overflow che corrompe solo le variabili locali (non il canary) viene rilevato?
> 7. Nomina due tecniche per bypassare il canary.