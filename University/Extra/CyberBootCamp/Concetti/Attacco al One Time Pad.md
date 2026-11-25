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

### countme · AES-CTR con nonce fisso, cioè OTP con keystream riusato

Server: `cyberchallenge.diag.uniroma1.it` (la porta cambia tra le istanze). File: `exercices/crypto/countme/server.py` e `reverse.py`.

Il menu ha due opzioni: `1` cifra la flag, `2` cifra un messaggio tuo. Tutte e due usano [[AES]] in modalità [[CTR]], ma `encrypt` legge **chiave e nonce fissi** dalle variabili d'ambiente e crea un cifrario nuovo a ogni chiamata:

```python
key   = os.getenv("KEY", ...)     # sempre la stessa
nonce = os.getenv("NONCE", ...)   # sempre lo stesso
cipher = AES.new(key.encode(), AES.MODE_CTR, nonce=nonce.encode())   # contatore ripartito da 0
```

CTR non cifra il messaggio: cifra la sequenza `nonce‖0, nonce‖1, …` e mette il risultato, il *keystream* `KS`, in XOR con il plaintext. Se chiave, nonce e contatore iniziale sono sempre gli stessi, anche `KS` è sempre lo stesso. AES diventa irrilevante, e quello che resta è un OTP con la chiave riusata, esattamente come in BitCrypt:

```
C_M = M ⊕ KS ,  C_F = F ⊕ KS
C_F ⊕ C_M = F ⊕ M        # KS eliminato
F = C_F ⊕ C_M ⊕ M        # M lo hai scelto tu
```

> [!important] Il nonce serve proprio a questo
> Il nome dice *number used once*: deve cambiare a ogni messaggio, mentre la chiave può restare la stessa. Con un nonce fisso CTR perde ogni sicurezza, come dice la flag stessa: `s4m3_n0nc3_s4m3_pr0bl3m`.

Soluzione ripulita (quella originale è in `reverse.py`):

```python
from pwn import *

def xor(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

p = remote("cyberchallenge.diag.uniroma1.it", 5254)

# 1. cifra un messaggio noto, lungo almeno quanto la flag
m = b"A" * 100
p.sendlineafter(b"Enter your choice: ", b"2")
p.sendlineafter(b"encrypt: ", m)
p.recvuntil(b"Encrypted User Text: ")
c_m = bytes.fromhex(p.recvline().strip().decode())

# 2. chiedi la flag cifrata
p.sendlineafter(b"Enter your choice: ", b"1")
p.recvuntil(b"Encrypted Flag (as hex): ")
c_f = bytes.fromhex(p.recvline().strip().decode())

print(xor(xor(c_f, c_m), m))   # ccit{s4m3_n0nc3_s4m3_pr0bl3m}
```

> [!warning] Correzione · gli errori incontrati lungo la strada
> - **`ModuleNotFoundError: No module named 'Crypto.Util.Padding'` lanciando il server in locale.** Il server è scritto per pycryptodome, ma sul PC di Simone `import Crypto` carica il vecchio PyCrypto (vedi [[pycryptodome#Quale libreria importi davvero|pycryptodome]]). Per provarlo in locale basta una copia che importa `Cryptodome`: `sed 's/from Crypto\./from Cryptodome./' server.py > server_local.py`, e nello script `process(["python3", "server_local.py"])`.
> - **`recvuntil` con un `\n` che non arriva mai.** Il prompt `"Enter the message you want to encrypt: "` viene da `input()`, che non va a capo. Aspettare `...encrypt: \n` blocca tutti e due: lo script aspetta il `\n`, il server aspetta il messaggio (deadlock). La stringa di `recvuntil` deve finire esattamente dove finisce l'output del server: confrontala con il log `[DEBUG] Received`.
> - **Riga vuota prima del risultato.** Il server stampa `f"\nEncrypted User Text: ..."`: il primo `recvline()` restituisce solo `b"\n"`. Si può saltarla con un `recvline()` in più, oppure andare direttamente all'etichetta con `recvuntil(b"Encrypted User Text: ")`.
> - **`fromhex` solo su uno dei due ciphertext.** La flag era stata convertita in byte veri, il ciphertext del messaggio no: lo XOR veniva fatto con i codici ASCII di `'d'`, `'a'`, `'5'`… e il risultato era spazzatura. Si riconosce dalla stampa: `b'da526ca9...'` è testo hex, `b'\xfdTv\xb4...'` sono byte veri. Stessa trappola di BitCrypt.

## Collegamenti

- **Concetti correlati** (corso Cybersecurity): [[One-Time Pad (OTP)]] · [[Perfect Cipher]] · [[Stream Cipher]] · [[CTR]] · [[AES]] · [[Known-Plaintext Attack (KPA)]]
- **Strumenti**: [[pwntools]] · [[pycryptodome#Schema delle conversioni str, bytes e hex|conversioni str / bytes / hex]]
- **Mappa**: [[MOC - CyberBootCamp]]

> [!info] Approfondimento
> - [[06 - CB - Crypto 1#Attacco: non riusare la chiave|Lezione 6 — Attacco: non riusare la chiave]]
