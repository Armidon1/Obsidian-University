guardare sempre prima [[CS 6cfu - Domande esame]]

Basandomi sulle dispense che hai caricato e incrociandole con i 50+ esami analizzati, ecco la **guida definitiva** su cosa devi sapere dei **Block Ciphers** per passare l'esame.

Questo argomento è il "cuore" della parte di crittografia simmetrica. Le domande sono spesso tecniche e richiedono ragionamento, non solo memoria.

---

### 1. Modalità Operative (ARGOMENTO CRUCIALE)

Questa è la parte più importante in assoluto. Non devi solo sapere le definizioni, devi capire le **differenze architetturali**. Troverai quasi sicuramente una domanda di confronto (es. "Confronta OFB e CTR") o uno scenario di errore.

Usa questa tabella mentale per rispondere:

|**Caratteristica**|**ECB**|**CBC (Il più chiesto)**|**OFB**|**CTR (Il moderno)**|
|---|---|---|---|---|
|**Tipo**|Block puro|Block (con catena)|Stream Sincrono|Stream Sincrono|
|**Parallelizzabile in Cifratura?**|Sì|**NO** (Sequenziale)|No (devi generare il keystream)|**SÌ** (puoi calcolare i counter)|
|**Parallelizzabile in Decifratura?**|Sì|**SÌ** (hai già tutti i blocchi $C$)|No|**SÌ**|
|**Pre-processing?**|No|No|**SÌ** (puoi generare il keystream prima)|**SÌ**|
|**Propagazione Errori** (Bit-flip)|1 blocco rotto|**Garbage + Bit specifico** (Vedi sotto)|Bit specifico|Bit specifico|

**Domande tipiche da saper gestire:**

- **Bit-Flipping in CBC:** "Se inverto il 3° bit del blocco cifrato $C_1$, cosa succede decifrando?"
    
    - **Risposta:** Il blocco $P_1$ diventa spazzatura (garbage) perché passa attraverso l'algoritmo di decifratura. Il blocco $P_2$ avrà **solo il 3° bit invertito** (perché $P_2 = D(C_2) \oplus C_1$). Dal blocco $P_3$ in poi, tutto torna normale.
        
- **OFB/CTR come Stream Cipher:** Devi sapere che trasformano un cifrario a blocchi in uno a flusso. Se riusi l'IV/Counter con la stessa chiave, succede il disastro dell'OTP (Two-time pad attack), perdendo la confidenzialità.
    

---

### 2. Meet-in-the-Middle (MITM)

Non confonderlo con _Man_-in-the-Middle! Questo è un attacco crittanalitico specifico contro i cifrari iterati come il **2DES**.

- **Il Concetto:** Invece di rompere una chiave doppia ($2^{112}$), l'attaccante usa uno spazio di memoria enorme per ridurre il tempo a $2^{57}$.
    
- **Come funziona (da saper descrivere):**
    
    1. Cifri il testo in chiaro $P$ con tutte le possibili chiavi $K_1$ e salvi i risultati in una tabella.
        
    2. Decifri il testo cifrato $C$ con tutte le possibili chiavi $K_2$.
        
    3. Se trovi un match tra il risultato del passo 2 e la tabella del passo 1, hai trovato la coppia $(K_1, K_2)$.
        
- **Conclusione:** Ecco perché usiamo **3DES** (o AES) e non 2DES.
    

---

### 3. AES (Struttura e Concetti)

Non ti chiederà di fare calcoli AES a mano (troppo lunghi), ma devi sapere la teoria per le domande a risposta multipla o "Vero/Falso".

- **Layer:** Devi sapere cosa fanno i 4 passaggi di un round:
    
    - **SubBytes:** L'unico passaggio **non-lineare** (Confusione). Usa le S-Box.
        
    - **ShiftRows & MixColumns:** Forniscono **Diffusione** (Avalanche Effect).
        
    - **AddRoundKey:** Inserisce la chiave segreta.
        
- **OpenSSL:** Se vedi `openssl enc -aes-128-cbc`, devi sapere che stai usando AES con chiave a 128 bit in modalità CBC.
    

---

### 4. Hardware Encryptors (Scenario Classico)

Questa è una domanda di logica che compare ciclicamente (es. 2015, 2022).

Scenario: "Alice e Bob hanno solo dispositivi hardware che sanno fare Encryption ($E_k$). Non hanno la funzione Decryption ($D_k$). Come possono comunicare in modo sicuro?"

Soluzione: Devono usare una modalità operativa che usa solo la funzione di cifratura anche per decifrare.

- **Risposta:** Usare **OFB** o **CTR**.
    
    - In queste modalità, il blocco cipher cifra solo l'IV/Counter per creare un keystream.
        
    - Il messaggio viene XORato con il keystream.
        
    - Per decifrare, si rigenera lo stesso keystream (usando la funzione _Encrypt_ sull'IV) e si fa di nuovo lo XOR. Non serve mai la funzione $D_k$ del chip.
        

### Sintesi dello Studio

1. Impara a memoria il diagramma di **CBC** (Decifratura) e **CTR**.
    
2. Studia l'attacco **Meet-in-the-Middle** (cos'è e perché uccide il 2DES).
    
3. Ricorda che **AES** usa S-Box per la non-linearità e ShiftRows/MixColumns per la diffusione.
    
4. Esercitati mentalmente sul **Bit-flipping** in CBC e OFB.