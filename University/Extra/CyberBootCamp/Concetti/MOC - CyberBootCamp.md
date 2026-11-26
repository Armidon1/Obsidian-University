---
title: MOC - CyberBootCamp
tags:
  - cyberbootcamp
  - moc
---

# MOC - CyberBootCamp

> [!abstract]
> Mappa del CyberBootCamp (CyberChallenge.IT, Sapienza): lezioni, concetti di ripasso e collegamenti con gli altri corsi del vault. Le note in `Concetti/` sono riassunti per il ripasso; i concetti già trattati altrove nel vault (HTTP, cookie, path traversal, ELF, …) sono collegati direttamente alle note esistenti.

## Lezioni

| # | Lezione | Argomenti |
|---|---|---|
| 1 | [[01 - CB - Web Insecurity 1]] | standard web, URL/URI, HTTP, cookie, autenticazione; IDOR, path traversal, SSTI, command injection |
| 2 | [[02 - CB - Reverse Engineering 1]] | ELF, dynamic linking, GOT/PLT, `strings`/`binwalk`, IDA, `.init_array`, export dei dati, struct |
| 3 | [[03 - CB - Assembly 101]] | assembly x86-64: registri, istruzioni, accesso memoria, controllo di flusso, stack frame, calling convention, caller/callee-saved, sintassi Intel/AT&T |
| 4 | [[04 - CB - Binary Exploitation 1]] | pwntools, `call`/`ret` e lo stack, buffer overflow, sovrascrittura del return address (ret2win) |
| 5 | [[05 - CB - Binary Exploitation 2]] | mitigazioni: stack canary, PIE, NX; workaround: leak, shellcode e Ret2Stack, ROP e gadget (`ropper`) |
| 6 | [[06 - CB - Crypto 1]] | confidenzialità/autenticazione, simmetrica vs asimmetrica; One Time Pad e cifrario perfetto, riuso della chiave; stream cipher e RC4; block cipher (AES/DES), PRF/PRP, modi ECB/CBC/CTR |
| 7 | [[07 - CB - Crypto 2]] | crittografia asimmetrica; gruppi e campi, aritmetica modulare, Eulero/Fermat, square and multiply; RSA e i suoi attacchi (fattorizzazione, common modulus, esponente piccolo, Håstad/CRT, malleabilità), padding; Diffie-Hellman, logaritmo discreto, Pohlig–Hellman, MITM, DDH e residui quadratici |

## Concetti

### Web: fondamenti
- [[URL e URI]] · [[Percent Encoding]] · [[HTTP Authentication]]
- Nel vault: [[HTTP]] · [[Cookie]] · [[DNS]] · [[Session Management]] · [[Authorization]] · [[Burp Suite]]

### Web: vulnerabilità
- [[Parser Differential]] · [[Null Byte Injection]] · [[Server-Side Template Injection]] · [[Out-of-Band Exfiltration]]
- Nel vault: [[Insecure Direct Object Reference]] · [[Path Traversal]] · [[Command Injection]] · [[SQL Injection]] · [[XSS]]

### Reverse: formato e linking
- [[Sezioni e Segmenti ELF]] · [[GOT e PLT]] · [[Avvio di un Binario ELF]] · [[init_array e fini_array]]
- Nel vault: [[ELF]] · [[Dynamic Linking]]

### Reverse: strumenti
- [[strings e binwalk]] · [[Scorciatoie IDA]] · [[Esportare Dati da IDA]] · [[Struct in IDA]] · [[pwndbg]] · [[Reimplementare codice decompilato in Python]]
- Nel vault: [[GDB]] · [[IDA Debugger]] · [[3 - MA - Basic Static Analysis]] · [[6 - MA - Advanced Static Analysis]]

### Assembly x86-64
- [[Codice Macchina e Assembly]] · [[Registri x86-64]] · [[Istruzioni x86-64]] · [[Controllo di Flusso in Assembly]] · [[Stack Frame x86-64]] · [[Calling Convention]] · [[Registri Caller-saved e Callee-saved]] · [[Sintassi Intel e AT&T]]
- Nel vault: [[2 - MA - X86 Assembly]] · [[Stack Frame]]

### Binary exploitation: le basi
- [[pwntools]] · [[call e ret]] · [[Buffer Overflow dello Stack]] · [[Sovrascrivere il Return Address]] · [[Signed e Unsigned (Integer Overflow)]]
- Nel vault: [[Buffer Overflow]]

### Binary exploitation: mitigazioni e workaround
- [[Canary dello Stack]] · [[PIE]] · [[NX]] · [[Shellcode]] · [[Ret2Stack]] · [[ROP]]
- Nel vault: [[Stack Canary]]

### Crittografia (Crypto 1)
> I concetti di crittografia sono trattati a fondo nel corso **Cybersecurity**: le note qui sotto rimandano direttamente a quelle, per non duplicarle. Le note proprie del CyberBootCamp hanno il taglio CTF: attacchi e strumenti.
- Taglio CTF: [[Attacco al One Time Pad]] · [[pycryptodome]] (AES in Python: ECB, CBC, CTR)
- Fondamenti (Cybersecurity): [[Symmetric Encryption]] · [[Asymmetric Encryption]] · [[One-Time Pad (OTP)]] · [[Perfect Cipher]]
- Cifrari (Cybersecurity): [[Stream Cipher]] · [[PRF (Pseudorandom Function)]] · [[Block Cipher]] · [[AES]] · [[DES]] · [[ECB]] · [[CBC]] · [[CTR]]

### Crittografia asimmetrica (Crypto 2)
- Matematica e strumenti: [[Gruppi, Anelli e Campi]] · [[Teorema Cinese del Resto]] · [[Residui Quadratici]] · [[SageMath]]
- Attacchi a RSA: [[Fattorizzare il Modulo RSA]] · [[RSA Common Modulus Attack]] · [[RSA con Esponente Piccolo]] · [[Håstad Broadcast Attack]] · [[Malleabilità di RSA]]
- Attacchi a Diffie-Hellman: [[Pohlig-Hellman]] · [[Man-in-the-Middle (MITM)]]
- Teoria (Cybersecurity e Mathematical definitions): [[Modular Arithmetic]] · [[Euler's totient function]] · [[Euler's Theorem]] · [[Fermat's Little Theorem]] · [[Modular Exponentiation]] · [[RSA]] · [[PKCS1]] · [[RSA-OAEP]] · [[Diffie-Hellman Key Exchange]] · [[Discrete Logarithm (DL) Problem]]

## Challenge

| Challenge | Categoria | Tecniche |
|---|---|---|
| [[Challenge 15+18]] | Reverse, Medium | flag come somma di due array globali, esca statica, costruttore nascosto in `.init_array`, lettura a runtime con pwndbg |
| Sn4k3 (in [[Reimplementare codice decompilato in Python#Esempio completo: Sn4k3\|Reimplementare codice decompilato]]) | Reverse | costruttore nascosto, tipi corretti con `Y`, reimplementazione in Python |
| GuessThePlaintext (in [[pycryptodome#GuessThePlaintext · AES in ECB, CBC e CTR con chiave scelta da te\|pycryptodome]]) | Crypto | AES in ECB, CBC e CTR con pycryptodome, conversione hex → byte, prompt con pwntools |
| BitCrypt (in [[Attacco al One Time Pad#BitCrypt · OTP con chiave riusata tra i tuoi messaggi e la flag\|Attacco al One Time Pad]]) | Crypto | OTP con chiave riusata, known-plaintext (`K = P ⊕ C`), conversioni str / bytes / hex, lettura del menu con pwntools |
| countme (in [[Attacco al One Time Pad#countme · AES-CTR con nonce fisso, cioè OTP con keystream riusato\|Attacco al One Time Pad]]) | Crypto | AES-CTR con chiave e nonce fissi → keystream riusato, `C_F ⊕ C_M ⊕ M = F`, prompt di `input()` senza `\n` |
| MysticTonguePoetry (in [[Attacco al One Time Pad#MysticTonguePoetry · many-time pad con crib dragging\|Attacco al One Time Pad]]) | Crypto | many-time pad: stessa chiave su 9 righe, crib `ccit{` allargato parola per parola, UTF-8 delle lettere accentate |
| progressivebar (in [[Signed e Unsigned (Integer Overflow)#progressivebar · signed/unsigned per saltare il limite di iterazioni\|Signed e Unsigned]]) | Pwn | integer overflow (signedness): `atoi("-1")` in `unsigned int` → `0xFFFFFFFF`, bypassa il limite di 9 cifre; canary come depistaggio |
| waterfall (in [[Sovrascrivere il Return Address#waterfall · ret2win con un gate sul contenuto del buffer\|Sovrascrivere il Return Address]]) | Pwn | ret2win classico (No PIE, No canary): overflow del buffer fino al return address → `win()`, con gate `"I am worthy"` sul contenuto |

## Percorsi trasversali

```mermaid
flowchart TD
    URL[URL e URI] --> PE[Percent Encoding]
    PE --> PD[Parser Differential]
    PD --> NB[Null Byte Injection]
    PE --> PT[Path Traversal]
    NB --> PT
    SSTI[Server-Side Template Injection] --> CI[Command Injection]
    CI --> OOB[Out-of-Band Exfiltration]
    ELF[Sezioni e Segmenti ELF] --> GOT[GOT e PLT]
    ELF --> AV[Avvio di un Binario ELF]
    AV --> INIT[init_array e fini_array]
    SB[strings e binwalk] --> IDA[Scorciatoie IDA]
    IDA --> EX[Esportare Dati da IDA]
    IDA --> ST[Struct in IDA]
    INIT --> IDA
    IDA --> PWN[pwndbg]
    EX --> PY[Reimplementare codice decompilato in Python]
    INIT --> CH[Challenge 15+18]
    PWN --> CH
    ASM[Registri x86-64] --> STK[Stack Frame x86-64]
    STK --> CR[call e ret]
    CR --> BOF[Buffer Overflow dello Stack]
    BOF --> RET[Sovrascrivere il Return Address]
    RET --> CAN[Canary dello Stack]
    RET --> PIEn[PIE]
    RET --> SC[Shellcode]
    SC --> R2S[Ret2Stack]
    R2S --> NX[NX]
    NX --> ROPn[ROP]
    OTP[One-Time Pad OTP] --> PERF[Perfect Cipher]
    OTP --> ATK[Attacco al One Time Pad]
    ATK --> STR[Stream Cipher]
    BLK[Block Cipher] --> PRP[PRF]
    BLK --> ECBn[ECB]
    ECBn --> CBCn[CBC]
    ECBn --> CTRn[CTR]
    EUL[Euler's Theorem] --> RSAn[RSA]
    RSAn --> FACT[Fattorizzare il Modulo RSA]
    RSAn --> SMALL[RSA con Esponente Piccolo]
    SMALL --> HAS[Håstad Broadcast Attack]
    CRTn[Teorema Cinese del Resto] --> HAS
    RSAn --> CMA[RSA Common Modulus Attack]
    RSAn --> MAL[Malleabilità di RSA]
    DLP[Discrete Logarithm] --> PH[Pohlig-Hellman]
    CRTn --> PH
    DHn[Diffie-Hellman] --> DLP
    DHn --> QR[Residui Quadratici]
```

- **Aggirare i filtri sui percorsi**: [[URL e URI]] → [[Percent Encoding]] → [[Parser Differential]] → [[Null Byte Injection]] → [[Path Traversal]]
- **Dall'input all'esecuzione di comandi**: [[Server-Side Template Injection]] → [[Command Injection]] → [[Out-of-Band Exfiltration]]
- **Come parte un binario**: [[Sezioni e Segmenti ELF]] → [[Avvio di un Binario ELF]] → [[init_array e fini_array]] → [[GOT e PLT]]
- **Risolvere una challenge di reversing**: [[strings e binwalk]] → [[Scorciatoie IDA]] → [[Struct in IDA]] → [[Esportare Dati da IDA]] → [[Reimplementare codice decompilato in Python]]
- **Dati modificati prima di main**: [[Sezioni e Segmenti ELF]] → [[init_array e fini_array]] → [[pwndbg]] → [[Challenge 15+18]]
- **Leggere l'assembly**: [[Codice Macchina e Assembly]] → [[Registri x86-64]] → [[Istruzioni x86-64]] → [[Controllo di Flusso in Assembly]] → [[Stack Frame x86-64]] → [[Calling Convention]]
- **Dallo stack all'exploit**: [[Stack Frame x86-64]] → [[call e ret]] → [[Buffer Overflow dello Stack]] → [[Sovrascrivere il Return Address]]
- **Aggirare le mitigazioni**: [[Sovrascrivere il Return Address]] → [[Canary dello Stack]] → [[PIE]] → [[Shellcode]] → [[Ret2Stack]] → [[NX]] → [[ROP]]
- **Dal One Time Pad ai cifrari reali** (Cybersecurity): [[One-Time Pad (OTP)]] → [[Perfect Cipher]] → [[Attacco al One Time Pad]] → [[Stream Cipher]]
- **Cifrari a blocchi e modi** (Cybersecurity): [[Block Cipher]] → [[PRF (Pseudorandom Function)]] → [[ECB]] → [[CBC]] → [[CTR]]
- **Rompere RSA** (CTF): [[Euler's Theorem]] → [[RSA]] → [[Fattorizzare il Modulo RSA]] → [[RSA Common Modulus Attack]] → [[RSA con Esponente Piccolo]] → [[Håstad Broadcast Attack]] → [[Malleabilità di RSA]]
- **Rompere Diffie-Hellman** (CTF): [[Diffie-Hellman Key Exchange]] → [[Discrete Logarithm (DL) Problem]] → [[Pohlig-Hellman]] → [[Teorema Cinese del Resto]] · [[Man-in-the-Middle (MITM)]] · [[Residui Quadratici]]
