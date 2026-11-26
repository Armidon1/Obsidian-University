---
title: Allineamento dello Stack (movaps)
tags:
  - cyberbootcamp
  - concetto
  - pwn
  - rop
---

# Allineamento dello Stack (movaps)

> [!summary] In breve
> La ABI x86-64 richiede che `rsp` sia allineato a **16 byte** al momento di una `call`. Funzioni di libc come `system` (dentro `do_system`) usano istruzioni SSE tipo `movaps XMMWORD PTR [rsp], xmm` che **falliscono** (SIGSEGV) se `rsp` non è allineato. Nei ret2win/ret2libc fatti a mano l'allineamento spesso salta di 8 byte: il rimedio è aggiungere un **`ret` gadget** nella catena.

## Il sintomo

L'exploit sembra giusto, salti alla funzione vittoria o a `system("/bin/sh")`, ma crashi con SIGSEGV **dentro la libc**, su un'istruzione del genere:

```
→ movaps XMMWORD PTR [rsp], xmm1      # do_system+0x65
```

`movaps` (move *aligned* packed single) pretende che l'indirizzo sia multiplo di 16. Se `rsp` finisce in `...8` invece che `...0`, l'accesso non allineato fa fault. Lo vedi nel backtrace: `#0 do_system`, `#1 win`/tua funzione.

## Perché succede

Alla `call` di una funzione, la ABI garantisce `rsp ≡ 0 (mod 16)`; subito **dopo** la `call` (dentro la funzione) `rsp ≡ 8 (mod 16)`, per via dell'indirizzo di ritorno appena pushato. Il compilatore conta su questo.

Quando sei tu a costruire lo stack con un overflow, il tuo indirizzo di ritorno può lasciare `rsp` "sfasato" di 8 rispetto a quello che la libc si aspetta. Da lì il primo `movaps` esplode.

## Il rimedio: un `ret` gadget

Un singolo `ret` fa una `pop` dallo stack (sposta `rsp` di +8) e salta dove quella pop punta. Infilato **prima** della funzione target, inverte la parità dell'allineamento senza fare altro:

```python
ret = ROP(exe).find_gadget(['ret'])[0]      # indirizzo di una singola istruzione 'ret' (byte 0xc3)
payload += p64(ret) + p64(exe.symbols['win'])
#          ^ riallinea     ^ ora system() dentro win non crasha
```

Il return address della funzione vulnerabile punta al `ret` gadget; subito dopo, nello stack, metti l'indirizzo vero. Catena: `ret_vulnerabile → ret_gadget → target`, con `rsp` di nuovo allineato a 16.

> [!tip] Regola pratica
> SIGSEGV su `movaps`/`movups [rsp]` dentro `do_system`/`printf`/`memcpy` durante un ret2win o ret2libc → quasi sempre **stack non allineato**. Aggiungi un `ret` gadget (o togli/aggiungi 8 byte di padding prima del return) e riprova.

## Collegamenti

- **Concetti correlati**: [[Sovrascrivere il Return Address]] · [[ROP]] · [[Ret2Stack]] · [[Calling Convention]]
- **Challenge**: [[pwntools#pngret2win · ret2win con validazioni PNG, NUL e allineamento movaps|pngret2win]]
- **Mappa**: [[MOC - CyberBootCamp]]
