---
title: Attacco al One Time Pad
tags:
  - cyberbootcamp
  - concetto
  - cryptography
  - attack
---

# Attacco al One Time Pad

> [!summary] In breve
> Riusare la stessa chiave `K` per due messaggi rompe l'OTP: `C1 ⊕ C2 = P1 ⊕ P2`, la chiave sparisce. Dai pattern dei testi reali si ricostruiscono i plaintext (*crib dragging*, *many-time pad*).

```
C1 = P1 ⊕ K ,  C2 = P2 ⊕ K
C1 ⊕ C2 = P1 ⊕ P2       # K eliminata
```
- I testi veri hanno **struttura** (spazi, lettere frequenti): basta per separare `P1` e `P2`.
- Con molti riusi (*many-time pad*) l'attacco è automatizzabile (es. tool MTP).
- Morale: chiave **sempre diversa** e lunga → motivazione dei [[Stream Cipher|cifrari a flusso]].

## Variante known-plaintext: se puoi scegliere il messaggio

Se il server cifra **anche messaggi tuoi** con la stessa chiave, non serve nemmeno il crib dragging. Lo XOR si annulla da solo (`x ⊕ x = 0`), quindi dal tuo plaintext e dal suo ciphertext ricavi direttamente la chiave:

```
C  = P ⊕ K            # P lo scegli tu, C te lo dà il server
K  = P ⊕ C            # chiave recuperata
F  = CF ⊕ K           # CF = flag cifrata con la stessa K
```

È un [[Known-Plaintext Attack (KPA)]], anzi un *chosen-plaintext*: il messaggio lo scegli tu. L'unico vincolo è che `P` sia lungo **almeno quanto la flag**, perché recuperi solo tanti byte di chiave quanti ne ha `P`.

## Challenge

### BitCrypt · OTP con chiave riusata tra i tuoi messaggi e la flag

Server: `cyberchallenge.diag.uniroma1.it` (la porta cambia tra le istanze). File: `exercices/crypto/BitCrypt/server.py` e `reverse.py`.

Il server genera all'avvio **una sola** chiave casuale di 500 byte e offre un menu: `1` cifra un messaggio stampabile tuo, `2` cifra la flag. La funzione `encrypt` sembra complicata, perché converte tutto in stringhe di `'0'`/`'1'` e confronta i bit uno per uno. In realtà è solo uno **XOR** byte per byte, con l'output in hex:

```python
# quello che fa encrypt(key, m), in una riga
bytes(k ^ x for k, x in zip(key, m)).hex()
```

Soluzione ripulita (quella originale è in `reverse.py`):

```python
from pwn import *

def xor(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

p = remote("cyberchallenge.diag.uniroma1.it", 5147)

# 1. cifra un plaintext noto e abbastanza lungo -> chiave
pt = b"A" * 100
p.sendlineafter(b"(1/2/3): ", b"1")
p.sendlineafter(b"encrypt: ", pt)
p.recvuntil(b"Encrypted message: ")
ct = bytes.fromhex(p.recvline().strip().decode())
key = xor(pt, ct)

# 2. chiedi la flag cifrata e toglile la chiave
p.sendlineafter(b"(1/2/3): ", b"2")
p.recvuntil(b"Encrypted FLAG: ")
flag_ct = bytes.fromhex(p.recvline().strip().decode())
print(xor(flag_ct, key))   # ccit{OTP_tw0_tim3s?!?!}
```

> [!warning] Correzione · gli errori incontrati lungo la strada
> - **Plaintext passato in hex e poi decodificato di nuovo.** `bytes.hex(pt.encode())` dà già una `str`, e il successivo `pt.decode()` fallisce con `AttributeError`. Quando poi si passa `pt.encode()`, cioè i byte veri, il `bytes.fromhex(pt.decode())` rimasto nella funzione dà `ValueError`: `"Succhiami..."` non è hex. Il plaintext scritto da te va solo `.encode()`-ato; `fromhex` serve solo per quello che il server stampa in hex. Schema completo in [[pycryptodome#Schema delle conversioni str, bytes e hex|pycryptodome]].
> - **`!=` al posto di `^`.** Indicizzare `bytes` dà interi: `a[i] != b[i]` produce un `'1'`/`'0'` per **byte** (diverso o no), non la chiave. Lo XOR è `a[i] ^ b[i]`.
> - **Plaintext troppo corto.** Con 18 caratteri si recuperano solo 18 byte di chiave, e la flag ne ha 23.
> - **`recvline()` legge l'avanzo del menu.** Dopo `Encrypted message: ...` il server ristampa il menu. Il `recvline()` successivo restituiva `b'Choose an option:\n'`, e `split()[2]` dava `b'option:'`: 7 byte di "flag" spazzatura. Indizio: la lunghezza del risultato non ha senso. Prima di leggere bisogna arrivare all'etichetta giusta con `recvuntil(b"Encrypted FLAG: ")`. Vedi [[pwntools#Prontuario di lettura e scrittura|pwntools]].
> - **XOR sul testo hex della flag.** Anche la flag arriva in hex: senza `bytes.fromhex` si fa lo XOR tra i caratteri `'0'-'f'` e la chiave.

## Collegamenti

- **Concetti correlati** (corso Cybersecurity): [[One-Time Pad (OTP)]] · [[Perfect Cipher]] · [[Stream Cipher]] · [[Known-Plaintext Attack (KPA)]]
- **Strumenti**: [[pwntools]] · [[pycryptodome#Schema delle conversioni str, bytes e hex|conversioni str / bytes / hex]]
- **Mappa**: [[MOC - CyberBootCamp]]

> [!info] Approfondimento
> - [[06 - CB - Crypto 1#Attacco: non riusare la chiave|Lezione 6 — Attacco: non riusare la chiave]]
