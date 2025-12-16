# Pseudo-Random Function (PRF)

**Tags:** #engineering #cryptography #PRF #algorithm #security

## 1. Definizione Formale

Una **Pseudo-Random Function (PRF)** è un algoritmo deterministico efficiente che mappa un **input** $x$ (di lunghezza arbitraria o fissa) e una **chiave segreta** $k$ in un **output** $y$ (di lunghezza fissa), in modo tale che l'output sia **indistinguibile** da quello di una funzione veramente casuale per chiunque non conosca la chiave $k$.

In termini matematici, una famiglia di funzioni $F: K \times X \to Y$ è una PRF se, per una chiave $k$ scelta a caso dallo spazio $K$, la funzione $F_k(x)$ "sembra" una funzione casuale pescata dall'insieme di _tutte_ le possibili funzioni che mappano $X$ in $Y$.

$$y = F_k(x)$$

Dove:

- $k$: Chiave segreta (l'elemento di entropia).
    
- $x$: Messaggio o input.
    
- $y$: Output pseudo-casuale (spesso chiamato _tag_ o _digest_ a seconda del contesto).
    

---

## 2. Il Concetto di "Indistinguibilità" (Il Test di Sicurezza)

Per un ingegnere, capire _come_ si definisce sicura una PRF è cruciale. Non si tratta di "sembrare casuale" a occhio nudo, ma di superare un test teorico preciso, spesso chiamato **Gioco dell'Indistinguibilità** o **Oracolo**.

Immagina un avversario (Adversary) che interagisce con una "Scatola Nera" (Oracolo). La scatola può essere in due stati:

1. **Mondo Reale (PRF):** La scatola contiene la funzione PRF $F_k$ con una chiave segreta $k$. Quando l'avversario invia un input $x$, la scatola calcola e restituisce $F_k(x)$.
    
2. **Mondo Ideale (Random Function):** La scatola contiene una funzione _veramente_ casuale $f$ (immagina una gigantesca tabella di lookup dove ogni input possibile è associato a un output generato lanciando una moneta).
    

La sfida: L'avversario può inviare quanti input vuole e vedere gli output. Alla fine, deve indovinare se sta parlando con la PRF o con la Funzione Random.

Una PRF è sicura se nessun avversario computazionalmente limitato può distinguere i due casi con una probabilità significativamente superiore al 50% (lancio di una moneta).

---

## 3. Proprietà Fondamentali

1. **Deterministica:** A differenza dei TRNG (True Random Number Generators), una PRF darà **sempre** lo stesso output per lo stesso input e la stessa chiave.
    
    - $F_k(text) \to \text{output\_A}$
        
    - $F_k(text) \to \text{output\_A}$ (Sempre!)
        
2. **Efficienza:** Deve essere possibile calcolare $F_k(x)$ in tempo polinomiale.
    
3. **Avalanche Effect (Effetto Valanga):** Cambiare anche un solo bit dell'input $x$ o della chiave $k$ deve produrre un output $y$ completamente diverso e non correlato al precedente.
    
4. **Assenza di Pattern:** Non devono esserci correlazioni evidenti tra input e output. Se conosco $F_k(x)$, non devo poter prevedere $F_k(x+1)$.
    

---

## 4. PRF vs PRG (Generatori Pseudo-Casuali)

È comune confondere PRF e [[RNG (Random Number Generator)]] (che hai visto nei tuoi appunti precedenti), ma hanno scopi diversi:

|**Caratteristica**|**PRG (Generator)**|**PRF (Function)**|
|---|---|---|
|**Input**|Un seme iniziale (_Seed_)|Una chiave segreta ($k$) + un input variabile ($x$)|
|**Output**|Un flusso continuo di bit (_Stream_)|Un blocco di bit di lunghezza fissa|
|**Obiettivo**|Espandere una piccola entropia in una lunga sequenza|Mappare un input specifico in un output "casuale"|
|**Esempio**|Generazione di chiavi di sessione|HMAC, Block Cipher|

> [!tip] Relazione
> 
> È possibile costruire un PRG usando una PRF. Ad esempio, la modalità CTR_DRBG (vista nei tuoi appunti al punto 7.D) usa AES (che agisce come una PRF) in modalità contatore per creare un flusso di numeri casuali (PRG).

---

## 5. Applicazioni Pratiche in Ingegneria

Le PRF sono i "mattoni" (primitives) fondamentali per costruire sistemi complessi:

1. **MAC (Message Authentication Codes):**
    
    - L'esempio classico è **HMAC** (Hash-based Message Authentication Code).
        
    - Qui, la PRF prende la chiave segreta e il messaggio. L'output serve come "firma" simmetrica per garantire integrità e autenticità.
        
    - $Tag = PRF_k(Message)$
        
2. **Derivazione delle Chiavi (KDF):**
    
    - Protocolli come **TLS** o **WPA2** usano PRF per trasformare un "segreto condiviso" (magari risultante da uno scambio Diffie-Hellman) in più chiavi operative (chiave di cifratura, chiave MAC, vettore di inizializzazione).
        
    - Esempio: `PBKDF2` usa una PRF per "stirare" una password in una chiave crittografica.
        
3. **Cifrari a Blocchi (Modellazione):**
    
    - Algoritmi come **AES** (Advanced Encryption Standard) sono idealmente modellati come **PRP (Pseudo-Random Permutations)**, che sono una sottoclasse speciale di PRF dove la funzione è invertibile (necessario per decifrare).
        
4. **Protocolli Challenge-Response:**
    
    - Per l'autenticazione: Il server invia un numero casuale (Challenge $N$). Il client risponde con $R = PRF_k(N)$. Il server fa lo stesso calcolo e confronta. Nessuno trasmette la password, ma entrambi provano di conoscerla.

## Vedi anche

- [[Differenza tra PRF e PRNG]]