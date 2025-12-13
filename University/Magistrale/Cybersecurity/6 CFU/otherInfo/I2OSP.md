# I2OSP (Integer to Octet-Stream Primitive)

**Tag:** #crittografia #RSA #primitive #PKCS1 #standard

## 1. Definizione

I2OSP (Integer to Octet-Stream Primitive) è una primitiva crittografica standard definita nello standard PKCS#1.

La sua funzione è convertire un numero intero non negativo in una stringa di ottetti (una sequenza di byte) di una lunghezza specifica.

## 2. Scopo e Contesto

Dopo aver eseguito operazioni matematiche RSA (come la cifratura $c = m^e \pmod n$ o la firma), il risultato è un grande numero intero. Per poter trasmettere questo risultato su una rete o salvarlo in un file, esso deve essere riconvertito in una sequenza di byte.

- **I2OSP** assicura che il numero venga formattato in modo standardizzato (Big-Endian) e che abbia una lunghezza fissa (solitamente la lunghezza del modulo RSA in byte), aggiungendo zeri iniziali (padding) se necessario.
    

## 3. Funzionamento Matematico

La primitiva converte un intero $x$ in una stringa di ottetti $X$ di lunghezza $k$.

- **Input:**
    
    - $x$: Intero non negativo da convertire.
        
    - $k$: Lunghezza desiderata della stringa di output in byte.
        
- **Vincolo:** Se $x \ge 256^k$, la funzione restituisce un errore ("integer too large"), poiché l'intero non può essere rappresentato in $k$ byte.
    

La conversione decompone $x$ in base 256:

$$x = X_1 \cdot 256^{k-1} + X_2 \cdot 256^{k-2} + \dots + X_k \cdot 256^0$$

Dove $X_1 \dots X_k$ sono i byte risultanti, ordinati dal più significativo al meno significativo (**Big-Endian**).

## 4. Esempio Pratico

Supponiamo di voler convertire l'intero **84,281,096** in una stringa di **8 byte** ($k=8$).

1. Rappresentazione esadecimale dell'intero: `0x05060708` (ocupa 4 byte).
    
2. Poiché $k=8$, dobbiamo aggiungere 4 byte di zeri iniziali (padding a sinistra).
    

Risultato (Octet String):

00 00 00 00 05 06 07 08

## 5. Operazione Inversa

L'operazione inversa, che converte una stringa di byte in un intero (usata prima della cifratura RSA), è chiamata:

- **[[OS2IP]]** (Octet-Stream to Integer Primitive).
    

---

**Vedi anche:**

- [[RSA]]
    
- [[RSA-OAEP]]
    
- [[PKCS#1]]