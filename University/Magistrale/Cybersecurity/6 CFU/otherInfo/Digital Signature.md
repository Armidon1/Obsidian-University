# Firma Digitale (Digital Signature)

**Tags:** #ingegneria #crittografia #sicurezza #firma_digitale #RSA #non_ripudio

## 1. Concetto Fondamentale

La **Firma Digitale** è il meccanismo crittografico che garantisce tre proprietà fondamentali di un documento elettronico:

1. **[[Authenticity]]:** Il mittente è chi dice di essere.
    
2. **[[Integrity]]:** Il messaggio non è stato modificato dopo la firma.
    
3. **[[Non-Repudiation]]:** Il mittente non può negare di aver firmato.
    

### Meccanismo RSA (Inversione dei Ruoli)

Nella cifratura standard RSA, si cifra con la Pubblica e si decifra con la Privata.

Nella Firma Digitale, il processo è invertito:

- **Firma (Generazione):** Si usa la **Chiave Privata** del mittente ($d$).
    
- **Verifica:** Chiunque può verificare usando la **Chiave Pubblica** del mittente ($e$).
    

> [!example] Professor's Example
> 
> Pensate alla firma autografa su un assegno: è unica e riconducibile solo a voi. La firma digitale è l'equivalente matematico. Usando la vostra chiave privata (che avete solo voi), stampate un "timbro matematico" indelebile sul file.

---

## 2. Il Paradigma "Hash-then-Sign"

In pratica, non firmiamo mai l'intero messaggio $M$ (sarebbe troppo lento se il file fosse grande 1GB). Firmiamo solo la sua "impronta digitale".

**Passaggi Logici:**

1. Si calcola l'hash del messaggio: $H = \text{Hash}(M)$.
    
2. Si applica un'operazione di **Encoding** (padding).
    
3. Si applica la funzione RSA all'hash codificato.
    

### Definizione Matematica

La generazione della firma $S$ è definita come:

$$S = EM^d \pmod n$$

Dove:

- $EM$: Messaggio codificato (che contiene l'hash).
    
- $d$: Esponente privato.
    
- $n$: Modulo RSA.
    

---

## 3. Standard Legacy: PKCS#1 v1.5

Questo è lo schema classico, ancora supportato ma considerato "Legacy".

### Struttura dell'Encoding (EMSA-PKCS1-v1_5)

Prima di firmare, l'hash viene inserito in una struttura rigida e deterministica:

Plaintext

```
EM = 0x00 || 0x01 || PS || 0x00 || T
```

- **0x00**: Byte iniziale (garantisce valore < modulo).
    
- **0x01**: Tipo di blocco (indica "Firma").
    
- **PS**: Padding String (byte `0xFF` per riempire).
    
- **T**: DigestInfo (contiene l'algoritmo Hash usato + l'Hash vero e proprio).
    

> [!abstract] Visual Analysis
> 
> ![[Pasted image 20251213184149.png]]
> 
> What to look at: Nota la struttura a blocchi. L'Hash è una piccola parte in fondo (dentro T).
> 
> Meaning: La maggior parte dei dati firmati è "riempitivo" (Padding) standardizzato.

### Verifica della Firma

Il destinatario esegue questi passi:

1. Decifra la firma $S$ con la chiave pubblica $e$: $EM' = S^e \pmod n$.
    
2. Calcola autonomamente l'hash del messaggio originale che ha ricevuto.
    
3. Ricostruisce la struttura $EM_{expected}$.
    
4. Confronta: Se $EM' == EM_{expected}$, la firma è valida.
    

---

## 4. Standard Moderno: RSA-PSS

Definito in [[PKCS1]] v2.1 (RFC 8017), è lo standard raccomandato oggi.

### Perché passare a PSS?

- **Problema della v1.5:** È **deterministica**. Lo stesso messaggio genera sempre la stessa firma.
    
- **Soluzione PSS:** È **probabilistico**. Introduce un elemento casuale (**Salt**).
    

### Costruzione PSS

1. **Salt:** Si genera una stringa casuale.
    
2. **[[MGF]] (Mask Generation Function):** Si usa una funzione maschera per "mescolare" l'hash e il salt.
    
3. **XOR:** Si applica l'operazione XOR per legare crittograficamente i dati.
    

**La struttura logica diventa:**

$$H' = \text{Hash}(Padding \ || \ mHash \ || \ salt)$$

> [!tip] Exam Focus
> 
> Una domanda classica è: "Qual è la differenza principale tra firma v1.5 e PSS?"
> 
> - **v1.5:** Deterministica (niente casualità).
>     
> - **PSS:** Probabilistica (usa un Salt casuale). Due firme dello stesso file saranno diverse byte per byte, ma entrambe valide.
>     

---

## 5. RSASSA (Terminologia Formale)

Lo standard definisce lo schema completo di firma come **RSASSA** (RSA Signature Scheme with Appendix).

**La Formula dello Standard:**

$$\text{RSASSA} = \text{RSA (Math)} + \text{EMSA (Encoding)}$$

- **RSA:** La pura matematica ($x^d \pmod n$).
    
- **EMSA:** Il metodo di preparazione dei dati (v1.5 o PSS).
    

> [!failure] Common Pitfall
> 
> Errore: Pensare che la firma digitale nasconda il contenuto del messaggio.
> 
> Realtà: La firma digitale garantisce l'autenticità, NON la segretezza. Il messaggio $M$ viaggia spesso in chiaro insieme alla firma $S$. Se volete anche segretezza, dovete poi cifrare tutto il pacchetto.