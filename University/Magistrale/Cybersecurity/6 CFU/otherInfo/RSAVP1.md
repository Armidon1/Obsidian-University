# RSAVP1 (RSA Verification Primitive 1)

**Tags:** #ingegneria #crittografia #RSA #primitiva #matematica #PKCS1

## 1. Definizione e Scopo

**RSAVP1** (RSA Verification Primitive 1) è la **primitiva crittografica** di base definita nello standard **PKCS#1** per la verifica di una firma.

Non è un protocollo di sicurezza completo, ma una pura **funzione matematica**. Il suo unico scopo è "invertire" l'operazione fatta dalla chiave privata, recuperando il numero originale (il messaggio rappresentativo o padding) a partire dalla firma digitale.

In termini semplici: è il motore matematico che calcola $x^e \pmod n$.

---

## 2. Definizione Matematica

La funzione prende in input la **Chiave Pubblica** e la **Firma** (sotto forma di numero intero) e restituisce un numero intero.

**Inputs:**

- **$K$ (Chiave Pubblica):** La coppia $(n, e)$, dove $n$ è il modulo RSA ed $e$ l'esponente pubblico.
    
- **$s$ (Signature representative):** La firma digitale da verificare, un numero intero compreso tra $0$ e $n-1$.
    

**Formula:**

$$m = s^e \pmod n$$

**Output:**

- **$m$ (Message representative):** Il risultato dell'elevamento a potenza. In uno schema reale (come RSASSA-PSS), questo valore $m$ corrisponde al messaggio codificato ($EM$).
    

---

## 3. Controlli di Validità

Prima di eseguire il calcolo, la primitiva deve effettuare un controllo fondamentale per evitare vulnerabilità matematiche.

**Range Check:**

$$0 \le s < n$$

Se la firma $s$ non rientra in questo intervallo, l'operazione deve fallire e restituire un errore "signature representative out of range".

> [!abstract] Math Analysis
> 
> Questo controllo è cruciale perché in aritmetica modulare esistono infiniti numeri che sono congruenti a $s \pmod n$. La firma valida deve essere quella canonica (la più piccola positiva).

---

## 4. Ruolo nello Schema Completo (RSASSA)

RSAVP1 non viene mai usata da sola perché non gestisce il padding o gli hash. È un componente interno dello schema di verifica completo (**RSASSA**).

**Flusso di Verifica:**

1. **RSAVP1 (Matematica):** Riceve la firma $S$ e calcola $EM = S^e \pmod n$.
    
2. **EMSA (Verifica Encoding):** Prende $EM$, controlla il padding (es. PKCS1-v1.5 o PSS), estrae l'hash e lo confronta con quello calcolato localmente.
    

> [!failure] Common Pitfall
> 
> Errore: Confondere RSAVP1 con la verifica della firma completa.
> 
> Realtà: RSAVP1 si limita a dire: "Se elevi questo numero $S$ alla potenza $e$, ottieni questo numero $m$". Non sa se $m$ è un messaggio valido, spazzatura o un attacco. È compito dello strato superiore (lo schema di encoding) interpretare $m$.

---

## 5. Corrispondenza con la Firma

RSAVP1 è l'operazione inversa della primitiva di firma **RSASP1** (RSA Signature Primitive 1).

|**Primitiva**|**Operazione**|**Chiave Usata**|
|---|---|---|
|**RSASP1**|Generazione ($s = m^d \pmod n$)|Chiave Privata ($d$)|
|**RSAVP1**|Verifica ($m = s^e \pmod n$)|Chiave Pubblica ($e$)|

> [!tip] Exam Focus
> 
> Se il prof chiede "Cosa fa esattamente RSAVP1?", la risposta precisa è: "Prende una firma intera $s$ e applica l'esponente pubblico $e$ modulo $n$ per recuperare il messaggio rappresentativo $m$. Non verifica l'integrità del padding."