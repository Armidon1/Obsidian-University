# Mask Generation Function (MGF)

**Tag:** #crittografia #RSA #primitive #PKCS1 #hash #OAEP #PSS

## 1. Definizione

Una **Mask Generation Function (MGF)** è una funzione crittografica deterministica che accetta in input una stringa di lunghezza arbitraria (il _seed_) e restituisce un output di lunghezza variabile desiderata (la _maschera_).

Formalmente:

$$\text{MGF}(seed, length) \rightarrow mask$$

## 2. Scopo

Le normali funzioni hash (come [[SHA-256]]) producono un output di lunghezza fissa (es. 256 bit).

In molti schemi crittografici (come [[RSA-OAEP]]), abbiamo bisogno di generare stringhe pseudo-casuali di lunghezze specifiche (es. 1024 bit, 2048 bit) per mascherare i dati tramite operazione [[XOR]].

L'MGF colma questa lacuna espandendo un input (seed) in una stringa più lunga, comportandosi in modo simile a un [[PRG]] deterministico o a una KDF (Key Derivation Function).

## 3. Lo Standard: MGF1

Lo standard più diffuso e definito in [[PKCS#1]] è MGF1.

MGF1 è costruito sopra una funzione hash sottostante (es. SHA-1, SHA-256, SHA-512).

### Algoritmo di MGF1

Per generare una maschera di lunghezza $L$ a partire da un seed $Z$:

1. Si inizializza un contatore $C = 0$ (intero a 32 bit).
    
2. Si esegue un ciclo concatenando l'hash del seed e del contatore:
    
    $$T = T \ || \ \text{Hash}(Z \ || \ \text{I2OSP}(C, 4))$$
    
3. Si incrementa il contatore: $C = C + 1$.
    
4. Si ripete finché $T$ non raggiunge la lunghezza $L$.
    
5. Si tronca $T$ ai primi $L$ byte e si restituisce l'output.
    

## 4. Utilizzo in RSA

L'MGF è un componente critico per la sicurezza degli schemi moderni:

- In [[RSA-OAEP]]:
    
    Viene usata per istanziare le funzioni G e H nella rete di Feistel.
    
    - $G$ espande il seed casuale per mascherare il messaggio.
        
    - $H$ espande il messaggio mascherato per mascherare il seed.
        
- In RSA-PSS (Firma):
    
    Viene usata per generare la maschera che copre il blocco dati ("DB") contenente il salt e il padding.
    

## 5. Proprietà di Sicurezza

Poiché è basata su funzioni hash crittografiche:

- **Deterministica:** Lo stesso seed produce sempre la stessa maschera (necessario per permettere la decifratura/verifica).
    
- **Imprevedibile:** Senza conoscere il seed, la maschera appare come una stringa di bit completamente casuale (simile a un Oracolo Random).
    

---

**Vedi anche:**

- [[RSA-OAEP]]
    
- [[Hashing]]
    
- [[PKCS#1]]
    
- [[XOR]]