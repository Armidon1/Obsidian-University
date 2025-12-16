# TRNG (True Random Number Generator)

## 1. Definizione

Un **TRNG** (True Random Number Generator) è un dispositivo hardware che genera numeri casuali sfruttando **fenomeni fisici imprevedibili** (processi stocastici).

A differenza dei [[PRNG (Pseudo-Random Number Generator)]], che usano algoritmi matematici deterministici, un TRNG è **non-deterministico**: non esiste alcun algoritmo o "stato interno" che permetta di calcolare il prossimo numero, nemmeno conoscendo tutta la storia passata del generatore.

## 2. Le Fonti di Entropia (Physical Noise)

Il cuore di un TRNG è la sua sorgente di rumore ("Noise Source"). Le fonti più comuni includono:

1. **Rumore Termico (Johnson-Nyquist Noise):** Misura le fluttuazioni di tensione causate dal movimento termico degli elettroni in un resistore.
    
2. **Effetto Valanga (Avalanche Noise):** Rumore generato in diodi Zener o giunzioni P-N in breakdown.
    
3. **Jitter del Clock:** Differenze microscopiche nei tempi di oscillazione di due quarzi indipendenti.
    
4. **Fenomeni Quantistici:** Decadimento radioattivo o rumore shot (fotonico).
    
5. **Interruzioni Hardware:** Timing tra pressioni di tasti, movimenti del mouse o arrivo di pacchetti di rete (in sistemi ibridi).
    

> [!abstract] Visual Mental Model
> 
> Immagina un PRNG come un libro di numeri già stampato: se sai a che pagina sei (Seed), sai cosa viene dopo.
> 
> Un TRNG è come lanciare una moneta o un dado ogni volta: il risultato è creato sul momento dalla fisica.

## 3. Il Problema del Bias e il "Whitening"

Le fonti fisiche grezze sono raramente perfette. Spesso hanno un **Bias** (es. producono leggermente più `1` che `0` a causa di asimmetrie hardware o temperatura).

Per correggere questo, i dati grezzi passano attraverso una fase di **Post-Processing** (o "Whitening"):

- **Correttore di Von Neumann:** Un algoritmo semplice che legge coppie di bit:
    
    - `01` $\to$ output `0`
        
    - `10` $\to$ output `1`
        
    - `00` o `11` $\to$ scarta.
        
- **Hashing:** Passare l'output grezzo attraverso una funzione [[Hashing]] (es. SHA-256) per uniformare la distribuzione statistica.
    

## 4. Utilizzo Principale: Il Seme

I TRNG sono generalmente **lenti** rispetto ai computer moderni (possono generare pochi kbit/sec contro i Gbit/sec dei PRNG).

Per questo motivo, in crittografia moderna si usa un **Approccio Ibrido**:

1. Si usa un **TRNG** per generare un **Seed** (seme) di altissima qualità (poca quantità, altissima entropia).
    
2. Si inietta questo Seed in un **[[PRNG|CSPRNG]]** (come CTR_DRBG AES).
    
3. Il CSPRNG espande velocemente quel seme in un flusso infinito di bit sicuri.
    

> [!tip] Exam Focus
> 
> Se ti chiedono "Perché non usiamo sempre i TRNG per tutto?", la risposta è: Performance e Scalabilità. I TRNG sono lenti e richiedono hardware dedicato. I PRNG crittografici sono velocissimi e girano su qualsiasi CPU, purché il seed iniziale venga da un TRNG.

## 5. Pro e Contro

|**Caratteristica**|**TRNG (Hardware)**|**PRNG (Software)**|
|---|---|---|
|**Sorgente**|Fisica (Entropia Reale)|Matematica (Seed)|
|**Prevedibilità**|Impossibile (teoricamente)|Deterministicamente prevedibile (senza seed segreto)|
|**Velocità**|Lenta|Molto Veloce|
|**Riproducibilità**|No (non puoi rigenerare la sequenza)|Sì (basta salvare il seed)|
|**Bias**|Possibile (richiede whitening)|Nullo (uniforme per design)|

---

**Vedi anche:**

- [[RNG (Random Number Generator)]]
    
- [[Pseudo-Random Number Generators (PRNG)]]
    
- [[Entropia (Informatica)]]
    
- [[Salt (Crittografia)]]