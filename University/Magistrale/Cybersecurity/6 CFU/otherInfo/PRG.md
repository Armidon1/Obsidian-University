# PRG (Generatori Pseudo-Casuali)

**Tag:** #crittografia #PRNG #CSPRNG #sicurezza #algoritmi #randomness

## 1. Definizione
Un **PRG** (Pseudo-Random Generator) o **PRNG** (Pseudo-Random Number Generator) è un algoritmo che produce lunghe sequenze di numeri apparentemente casuali, le quali sono però completamente determinate da un valore iniziale chiamato **Seed** (o chiave).

A differenza dei TRNG (True Random Number Generators) che misurano fenomeni fisici , i PRNG sono basati su computazioni deterministiche e quindi non possono generare "vera" casualità, ma solo espanderla.

## 2. Funzionamento Generale
Il processo tipico di un PRG è il seguente:
1. **Raccolta Entropia:** Si raccolgono dati dal sistema (clock, I/O, movimento mouse, pacchetti di rete) per creare un seed imprevedibile.
2. **Inizializzazione:** Il programma viene inizializzato con il seed.
3. **Espansione:** L'algoritmo espande il seed corto in una lunga sequenza di numeri.

> **Nota:** Se un attaccante conosce il seed e l'algoritmo, può predire l'intera sequenza. La sicurezza dipende interamente dalla segretezza e dall'entropia del seed iniziale.

## 3. PRNG vs CS-PRNG
Non tutti i generatori sono adatti per la crittografia. Esiste una distinzione fondamentale tra i PRNG standard e i **CS-PRNG** (Cryptographically Secure PRNG).

| Caratteristica | PRNG (Standard) | CS-PRNG (Sicuro Crittograficamente) |
| :--- | :--- | :--- |
| **Scopo** | Simulazioni, giochi, modelli. | Chiavi di sessione, nonces, IV. |
| **Controllo** | Test statistici (distribuzione uniforme). | Test statistici + resistenza alla crittoanalisi. |
| **Prevedibilità** | Se lo stato è noto, il futuro è noto. | Computazionalmente impossibile predire l'output futuro. |
| **Sicurezza** | Nessuna garanzia oltre la statistica. | Forward Secrecy e Backward Secrecy. |

## 4. Requisiti di Sicurezza (BSI e Next-Bit)
Per essere considerato crittograficamente sicuro, un generatore deve soddisfare requisiti specifici:

### Il "Next-Bit Test"
Dati i primi $k$ bit di una sequenza casuale, non deve esistere alcun algoritmo in tempo polinomiale in grado di predire il $(k+1)$-esimo bit con una probabilità di successo superiore al 50%.

### Criteri BSI (Bundesamt für Sicherheit in der Informationstechnik)
Il BSI classifica i generatori in 4 classi:
- **K1:** Bassa probabilità di sequenze identiche.
- **K2:** Indistinguibile dal "vero random" secondo test statistici (Monobit, Poker, Runs) .
- **K3:** Impossibile dedurre output passati/futuri o lo stato interno a partire dall'output.
- **K4:** Impossibile dedurre output o stati passati anche conoscendo lo stato interno attuale (Forward Secrecy).
> **Regola:** Per applicazioni crittografiche sono accettabili solo i generatori **K4**.

## 5. Esempi di Algoritmi

### Insicuri o Deprecati
- **Linear Congruential Generators (LCG):** Spesso usati nelle librerie standard dei linguaggi (`rand()`), passano i test statistici ma sono prevedibili.
- **Netscape 1.1 RNG:** Esempio storico di fallimento. Usava `time of day`, `pid` e `ppid` come seed. L'entropia reale era di soli 47 bit, rendendo le chiavi SSL facili da indovinare.
- **ANSI X9.31:** Basato su AES/3DES, deprecato nel 2016.

### Sicuri (CS-PRNG)
- **Blum Blum Shub (BBS):** Basato sulla difficoltà della fattorizzazione (residui quadratici modulo $n=p \cdot q$). Molto lento ma provabilmente sicuro.
- **CTR_DRBG:** Standard attuale (NIST). Usa AES in modalità Counter. Ad ogni richiesta aggiorna lo stato cifrando un contatore. Garantisce Forward & Backward secrecy (se viene fatto il reseeding).

## 6. Errori Comuni
1. **Seed Piccolo:** Un seed a 16 bit offre solo 65.536 combinazioni, vulnerabile al brute-force istantaneo.
2. **Uso del Tempo:** Usare solo l'orologio di sistema è rischioso perché il tempo è prevedibile o indovinabile con pochi tentativi.
3. **Mancanza di Entropia:** Il caso **Debian OpenSSL (2008)** mostra cosa succede rimuovendo le fonti di entropia dal codice: le chiavi generate erano prevedibili basandosi solo sul PID del processo.

---
**Vedi anche:**
* [[Generazione Numeri Casuali]]
* [[One-Time Pad (OTP)]] (Richiede generatori perfetti)
* [[RSA]] (Esempio di algoritmo che necessita di PRG sicuri per la generazione chiavi)