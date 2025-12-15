# RSASP1 (RSA Signature Primitive 1)

**Tags:** #ingegneria #crittografia #RSA #primitiva #matematica #PKCS1 #firma_digitale

## 1. Definizione e Scopo

**RSASP1** (RSA Signature Primitive 1) è la **primitiva crittografica** fondamentale definita nello standard **[[PKCS1|PKCS#1]]** per generare una firma digitale.

Come per la sua controparte di verifica, questa non è l'intera procedura di firma (non gestisce hash o padding), ma è la pura **operazione matematica** che applica la chiave privata ai dati. È il "cuore segreto" del processo di firma.

## 2. Definizione Matematica

La funzione prende in input la **Chiave Privata** e un numero intero (il messaggio già codificato/paddato) e produce la firma matematica.

**Inputs:**

- **$K$ (Chiave Privata):** La coppia $(n, d)$, dove $n$ è il modulo e $d$ è l'esponente privato.
    
- **$m$ (Message representative):** Il messaggio codificato (rappresentato come un intero tra $0$ e $n-1$). Questo $m$ è solitamente il risultato dell'encoding (es. EMSA-PSS o EMSA-PKCS1-v1_5).
    

**Formula:**

$$s = m^d \pmod n$$

**Output:**

- **$s$ (Signature representative):** La firma digitale, un numero intero della stessa lunghezza del modulo.
    

> [!abstract] Math Analysis
> 
> Matematicamente, questa operazione è identica alla decifratura "classica" (RSADP). Tuttavia, in crittografia è fondamentale distinguere l'intento: qui stiamo usando l'esponente privato $d$ non per nascondere o rivelare un messaggio, ma per attestare la provenienza di $m$.

## 3. Controlli di Validità (Pre-condizioni)

Prima di eseguire l'elevamento a potenza, la primitiva deve verificare che l'input sia matematicamente valido.

**Range Check:**

$$0 \le m < n$$

Se il messaggio rappresentativo $m$ è maggiore o uguale al modulo $n$, l'operazione non può essere eseguita e deve restituire un errore ("message representative out of range").

> [!failure] Common Pitfall
> 
> Perché questo limite?
> 
> In aritmetica modulare $\pmod n$, i numeri "vivono" solo tra $0$ e $n-1$. Se provassimo a firmare un numero $m \ge n$, l'operazione modulo ridurrebbe $m$ (perdendo informazioni) o creerebbe ambiguità durante la verifica. È compito dello schema di encoding (EMSA) assicurarsi che il messaggio formattato rientri in questo range.

## 4. Differenza tra RSASP1 e RSAEP

Spesso si dice che "la firma è l'inverso della cifratura", ma bisogna essere precisi sulle primitive.

|**Primitiva**|**Scopo**|**Chiave**|**Operazione**|
|---|---|---|---|
|**RSAEP** (Encryption)|Confidenzialità|Pubblica ($e$)|$c = m^e \pmod n$|
|**RSASP1** (Signature)|Autenticità|Privata ($d$)|$s = m^d \pmod n$|

In RSASP1, solo il possessore di $d$ può calcolare $s$. In RSAEP, chiunque abbia $e$ può calcolare $c$.

## 5. Integrazione in RSASSA

RSASP1 è l'ultimo passaggio della catena di firma completa (**RSASSA**).

**Flusso di Generazione:**

1. **Hash & Encode:** Il messaggio $M$ viene hashato e paddato (es. PSS) per creare il blocco $EM$.
    
2. **Conversione ([[OS2IP]]):** Il blocco di byte $EM$ viene convertito nel numero intero $m$.
    
3. **RSASP1 (Firma):** Si calcola $s = m^d \pmod n$.
    
4. **Output:** $s$ viene convertito in byte (I2OSP) e allegato al messaggio.
    

> [!tip] Exam Focus
> 
> Se ti chiedono: "RSASP1 firma il messaggio originale?"
> 
> La risposta corretta è NO. RSASP1 firma il "Message Representative" ($m$), che è il risultato dell'hashing e del padding del messaggio originale. Firmare direttamente il messaggio originale sarebbe insicuro (attacchi matematici) e inefficiente (messaggio troppo lungo per il modulo).