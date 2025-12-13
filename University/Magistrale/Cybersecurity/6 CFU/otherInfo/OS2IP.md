# OS2IP (Octet-Stream to Integer Primitive)

**Tag:** #crittografia #RSA #primitive #PKCS1 #standard

## 1. Definizione

OS2IP (Octet-Stream to Integer Primitive) è una primitiva crittografica standard definita nello standard PKCS#1.

La sua funzione è convertire una stringa di ottetti (una sequenza di byte) in un numero intero non negativo.

## 2. Scopo e Contesto

Gli algoritmi a chiave pubblica come [[RSA]] operano matematicamente su grandi numeri interi (es. $c = m^e \pmod n$). Tuttavia, i dati nel mondo reale (testi, file, chiavi) sono rappresentati come sequenze di byte (octet strings).

- **OS2IP** fa da "ponte": converte il messaggio paddato (es. da [[RSAES-OAEP]]) dal formato byte al formato numero, permettendo l'esecuzione delle operazioni matematiche di RSA.
    

## 3. Funzionamento Matematico

La primitiva interpreta la sequenza di byte come un numero intero rappresentato in **base 256** con ordinamento **Big-Endian** (il primo byte è il più significativo).

Data una stringa di ottetti $X$ di lunghezza $k$ byte, dove $X_1$ è il primo byte e $X_k$ è l'ultimo:

$$x = \text{OS2IP}(X) = \sum_{i=1}^{k} X_i \cdot 256^{k-i}$$

In termini estesi:

$$x = X_1 \cdot 256^{k-1} + X_2 \cdot 256^{k-2} + \dots + X_k \cdot 256^0$$

## 4. Esempio Pratico

Supponiamo di avere una stringa di 4 byte: `01 02 03 04` (in esadecimale).

La conversione avviene così:

1. **Byte 1 (`0x01`):** $1 \times 256^3 = 16,777,216$
    
2. **Byte 2 (`0x02`):** $2 \times 256^2 = 131,072$
    
3. **Byte 3 (`0x03`):** $3 \times 256^1 = 768$
    
4. **Byte 4 (`0x04`):** $4 \times 256^0 = 4$
    

**Totale intero:** $16,777,216 + 131,072 + 768 + 4 = \mathbf{16,909,060}$

## 5. Operazione Inversa

L'operazione inversa, che converte un intero in una stringa di ottetti (usata dopo la decifratura RSA per ottenere il messaggio in byte), è chiamata:

- **[[I2OSP]]** (Integer to Octet-Stream Primitive).
    

---

**Vedi anche:**

- [[RSA]]
    
- [[RSA-OAEP]]
    
- [[PKCS#1]]