guardare sempre prima [[CS 6cfu - Domande esame]]

Basandomi rigorosamente sugli esami che hai inviato (dal 2012 al 2025), ecco cosa chiede il professore su **ElGamal, DSA (Digital Signature Algorithm) e DSS**.

Questo argomento è meno frequente di RSA, ma quando esce, le domande sono molto specifiche e puniscono chi ha studiato solo la teoria generale senza capire la matematica sottostante.

Ecco i 4 pilastri dell'esame su questo tema:

### 1. La Vulnerabilità della Chiave Effimera $k$ (DOMANDA TOP)

Questa è la domanda più tecnica e frequente su DSA.

In DSA/ElGamal, per ogni firma si genera un numero casuale $k$ (spesso chiamato "chiave privata temporanea").

- **Domanda:** "In una firma DSS, se la chiave privata creata dal firmatario al momento della firma (il parametro $k$) viene compromessa, qual è l'effetto sulle firme passate e future?" oppure "Mostra perché la conoscenza di $k$ rompe la sicurezza".
    
- **Risposta da 30:**
    
    - Se l'attaccante scopre $k$, può calcolare immediatamente la **chiave privata a lungo termine** del firmatario ($x$) usando l'equazione della firma (semplice algebra lineare).
        
    - **Conseguenza:** Una volta ottenuta la chiave privata $x$, l'attaccante può falsificare firme **future** (Total Break). Le firme **passate** rimangono matematicamente valide, ma la loro "fiducia" è compromessa perché non si sa più chi le ha generate.
        

### 2. Esercizio Matematico: Calcolo di $\alpha$ (o $g$)

Come accennato nelle note, questo esercizio compare davvero negli esami scritti.

- **Domanda:** "Dati i due numeri primi $p=23$ e $q=11$, trova un intero $a > 1$ tale che $a^{11} \equiv 1 \pmod{23}$".
    
- **Come risolvere:**
    
    1. Stai cercando il generatore del sottogruppo di ordine $q$.
        
    2. La formula è: $a = h^{(p-1)/q} \pmod p$, dove $h$ è un intero qualsiasi $>1$.
        
    3. Calcoli l'esponente: $(23-1)/11 = 22/11 = 2$.
        
    4. Provi con $h=2$: $a = 2^2 \pmod{23} = 4$.
        
    5. Verifica: $4^{11} \equiv (2^2)^{11} \equiv 2^{22} \equiv 1 \pmod{23}$ (per il Piccolo Teorema di Fermat).
        
    6. **Risposta:** $a=4$.
        

### 3. Confronto ElGamal vs DSS (Tabella)

Richiesto esplicitamente nell'esame di Gennaio 2024.

- **Domanda:** "ElGamal signature vs. DSS (draw a table and be schematic)".
    
- **Tabella da memorizzare:**
    

|**Caratteristica**|**Firma ElGamal**|**Firma DSS (DSA)**|
|---|---|---|
|**Dimensione Firma**|Grande (2 numeri mod $p$)|**Piccola** (2 numeri mod $q$)|
|**Operazioni**|Lente (esponenziali grandi)|Più veloci (esponenziali su $q$)|
|**Sicurezza**|Discrete Log su intero campo|Discrete Log su sottogruppo|
|**Standard**|No (Storico)|**Sì** (NIST FIPS 186)|

### 4. OpenSSL Command Line (Trend 2025)

Nell'esame di Giugno 2025 è stato chiesto di analizzare:

openssl dgst -sha256 -verify public_key.pem -signature sign.bin message.txt

- **Risposta:**
    
    - `dgst -sha256`: Usa l'algoritmo di hash SHA-256.
        
    - `-verify public_key.pem`: Verifica la firma usando la chiave pubblica specificata (Nota: per verificare serve la Pubblica, per firmare la Privata).
        
    - `-signature sign.bin`: Il file che contiene la firma digitale da controllare.
        
    - `message.txt`: Il file originale di cui verificare l'integrità e autenticità.
        

### Vero/Falso da sapere (Esami 2017-2018)

- "DSA è un algoritmo di cifratura simmetrica" -> **FALSO** (È asimmetrico e solo per firma).
    
- "Due firme DSA fatte sullo stesso documento sono diverse con alta probabilità" -> **VERO** (Grazie al parametro casuale $k$).
    
- "RSA è più lento di DSS nella verifica della firma" -> **FALSO** (RSA ha $e$ piccolo, quindi verifica veloce; DSS richiede esponenziali pesanti per verificare).
    

### Sintesi per il Ripasso

1. Impara la formula per trovare $x$ se conosci $k$ (o almeno il concetto che $k$ noto = disastro).
    
2. Esercitati a calcolare il generatore $\alpha$ con numeri piccoli ($p=11, q=5$ oppure $p=23, q=11$).
    
3. Ricorda: **DSA firma modulo $q$** (piccolo), **ElGamal firma modulo $p$** (grande).