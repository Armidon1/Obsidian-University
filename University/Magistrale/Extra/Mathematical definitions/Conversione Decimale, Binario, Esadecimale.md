# Decimale - Binario
## Da Decimale a Binario
Per convertire un numero decimale in binario, il metodo più comune è quello delle **divisioni successive per 2**.

È un processo semplice che si basa sul prendere nota dei resti di ogni divisione.

### ⚙️ Come Funziona (Metodo della Divisione)

1. **Dividi per 2:** Prendi il tuo numero decimale e dividilo per 2.
    
2. **Annota il resto:** Scrivi da parte il **resto** (che sarà sempre 0 o 1).
    
3. **Ripeti:** Prendi il **quoziente** (il risultato della divisione) e ripeti il processo: dividilo di nuovo per 2 e annota il resto.
    
4. **Continua:** Continua a dividere i quozienti successivi per 2 finché non ottieni un quoziente pari a **0**.
    
5. **Leggi il risultato:** Il numero binario è la sequenza di tutti i resti che hai annotato, letti **dall'ultimo al primo** (dal basso verso l'alto).
    

---

### 💡 Esempio Pratico: Convertire il numero 25

Proviamo a convertire il numero decimale **25** in binario:

- 25 / 2 = 12 con **resto 1**
    
- 12 / 2 = 6 con **resto 0**
    
- 6 / 2 = 3 con **resto 0**
    
- 3 / 2 = 1 con **resto 1**
    
- 1 / 2 = 0 con **resto 1**
    

Adesso, leggi i resti **dal basso verso l'alto**: 11001.

Quindi, **25** (in decimale) è uguale a **11001** (in binario).

---

## Da Binario a Decimale

Per convertire un numero binario in decimale, si usa il **metodo delle potenze di 2**.

È un processo che "pesa" ogni cifra (bit) del numero binario in base alla sua posizione.

### ⚙️ Come Funziona (Metodo delle Potenze)

1. **Scrivi il numero:** Prendi il tuo numero binario (ad esempio, 11001).
    
2. **Assegna le potenze:** A ogni cifra binaria, partendo da **destra**, assegna una potenza di 2 crescente, iniziando da $2^0$ (che vale 1).
    
3. **Moltiplica e somma:** Moltiplica ogni cifra binaria (che sarà 1 o 0) per il valore della sua potenza di 2 corrispondente.
    
4. **Somma i risultati:** Somma tutti i prodotti che hai ottenuto. Il totale è il tuo numero decimale.
    

---

### 💡 Esempio Pratico: Convertire il numero 11001

Usiamo lo stesso numero dell'esempio precedente, **11001**:

1. Scrivi il numero e assegna le potenze da destra a sinistra:
    
| **Cifra Binaria** | **1** | **1** | **0** | **0** | **1** |
| ----------------- | ----- | ----- | ----- | ----- | ----- |
| Potenza di 2      | $2^4$ | $2^3$ | $2^2$ | $2^1$ | $2^0$ |
| Valore Potenza    | 16    | 8     | 4     | 2     | 1     |

1. Ora, moltiplica ogni cifra binaria per il valore della sua potenza e somma i risultati:
    
    $(1 \times 16) + (1 \times 8) + (0 \times 4) + (0 \times 2) + (1 \times 1)$
    
2. Calcola la somma:
    
    $16 + 8 + 0 + 0 + 1 = 25$
    

Quindi, **11001** (in binario) è uguale a **25** (in decimale).

---

# Decimale - Esadecimale

Certamente! Il principio è molto simile a quello binario, ma invece di usare la base 2, si usa la **base 16**.

Un punto chiave da ricordare è che l'esadecimale (spesso abbreviato "hex") usa 16 simboli:

- I numeri da **0 a 9**
    
- Le lettere da **A a F** (per rappresentare i valori da 10 a 15)
    

> **🔢 Tabella di Riferimento Rapida:**
> 
> - A = 10
>     
> - B = 11
>     
> - C = 12
>     
> - D = 13
>     
> - E = 14
>     
> - F = 15
>     

---
## Da Decimale a Esadecimale

Si usa lo stesso metodo delle divisioni successive, **ma si divide per 16**.

1. **Dividi per 16:** Prendi il tuo numero decimale e dividilo per 16.
    
2. **Annota il resto:** Scrivi il resto. **Se il resto è tra 10 e 15, convertilo nella lettera corrispondente (A-F).**
    
3. **Ripeti:** Prendi il quoziente e dividilo di nuovo per 16.
    
4. **Continua:** Ripeti finché non ottieni un quoziente pari a 0.
    
5. **Leggi il risultato:** Leggi la sequenza dei resti (con le lettere) **dall'ultimo al primo** (dal basso verso l'alto).
    

#### 💡 Esempio Pratico: Convertire il numero 495

Proviamo a convertire il numero decimale **495**:

- 495 / 16 = 30 con **resto 15** (che corrisponde a **F**)
    
- 30 / 16 = 1 con **resto 14** (che corrisponde a **E**)
    
- 1 / 16 = 0 con **resto 1**
    

Ora, leggi i resti **dal basso verso l'alto**: 1, E, F.

Quindi, **495** (in decimale) è uguale a **1EF** (in esadecimale).

---

## Da Esadecimale a Decimale

Si usa il metodo delle potenze, ma si usano**le potenze di 16** (invece che di 2).

1. **Scrivi il numero:** Prendi il tuo numero esadecimale (es. 1EF).
    
2. **Assegna le potenze:** A ogni cifra, partendo da **destra**, assegna una potenza di 16 crescente, iniziando da $16^0$.
    
3. **Converti e Moltiplica:** Converti ogni lettera (A-F) nel suo valore numerico (10-15). Moltiplica ogni valore per la sua potenza di 16 corrispondente.
    
4. **Somma i risultati:** Somma tutti i prodotti.
    

#### 💡 Esempio Pratico: Convertire il numero 1EF

Usiamo lo stesso numero, **1EF**, per verificare:

1. Scrivi il numero e assegna le potenze da destra a sinistra:
    
| **Cifra Esadecimale** | **1**  | **E (vale 14)** | **F (vale 15)** |
| --------------------- | ------ | --------------- | --------------- |
| Potenza di 16         | $16^2$ | $16^1$          | $16^0$          |
| Valore Potenza        | 256    | 16              | 1               |
    
2. Moltiplica ogni cifra (convertita) per il valore della sua potenza e somma i risultati:
    
    $(1 \times 256) + (14 \times 16) + (15 \times 1)$
    
3. Calcola la somma:
    
    $256 + 224 + 15 = 495$
    

Quindi, **1EF** (in esadecimale) è uguale a **495** (in decimale).

---

# Binario - Esadecimale

Questo è il trucco più comodo e veloce perché esiste una relazione diretta tra i due sistemi: **$2^4 = 16$**.

Questo significa che **ogni cifra esadecimale corrisponde esattamente a un gruppo di 4 cifre binarie (bit)**.

Non c'è bisogno di passare dal sistema decimale. Basta usare questa tabella di conversione diretta:

|**Esadecimale**|**Binario (4-bit)**|
|---|---|
|0|0000|
|1|0001|
|2|0010|
|3|0011|
|4|0100|
|5|0101|
|6|0110|
|7|0111|
|8|1000|
|9|1001|
|A (10)|1010|
|B (11)|1011|
|C (12)|1100|
|D (13)|1101|
|E (14)|1110|
|F (15)|1111|

---

## Da Binario a Esadecimale

Questo metodo consiste nel **"raggruppare"** i bit.

1. **Parti da destra:** Prendi il tuo numero binario e dividilo in gruppi di 4 bit, partendo da destra.
    
2. **Aggiungi zeri (Padding):** Se il gruppo più a sinistra non ha 4 bit, aggiungi degli zeri all'inizio (a sinistra) finché non arriva a 4.
    
3. **Converti ogni gruppo:** Usa la tabella qui sopra per convertire ogni singolo gruppo di 4 bit nella sua cifra esadecimale corrispondente.
    

#### 💡 Esempio Pratico: Convertire 110101101

1. Numero: `110101101`
    
2. Dividi in gruppi di 4 da destra: `1` `1010` `1101`
    
3. Aggiungi zeri al gruppo di sinistra: `0001` `1010` `1101`
    
4. Converti ogni gruppo:
    
    - `0001` = **1**
        
    - `1010` = **A**
        
    - `1101` = **D**
        

Quindi, **110101101** (in binario) è uguale a **1AD** (in esadecimale).

---

## Da Esadecimale a Binario

Questo è il processo inverso, ancora più semplice (**Espansione**).

1. **Prendi ogni cifra:** Considera ogni cifra del tuo numero esadecimale singolarmente.
    
2. **Converti in 4 bit:** Usa la tabella per convertire ogni cifra esadecimale nel suo blocco _esatto_ di 4 bit (assicurati di mantenere gli zeri iniziali, ad esempio 5 è `0101`, non `101`).
    
3. **Unisci i blocchi:** Metti tutti i blocchi di 4 bit uno dopo l'altro.
    

#### 💡 Esempio Pratico: Convertire 1AD

1. Numero: `1AD`
    
2. Converti ogni cifra in 4 bit:
    
    - `1` = **0001**
        
    - `A` = **1010**
        
    - `D` = **1101**
        
3. Unisci i blocchi: `000110101101`
    

Puoi rimuovere gli zeri iniziali se vuoi (il `0001` può diventare `1`), quindi: **110101101**.

Come vedi, **1AD** (in esadecimale) è uguale a **110101101** (in binario).

---
