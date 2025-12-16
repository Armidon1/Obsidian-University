# Salt (Cryptographic)

## 1. Definizione

Il **Salt** (in italiano "sale") è una sequenza di bit generata in modo **casuale** che viene unita a un dato di input (come una password o un messaggio) prima di applicarvi una funzione crittografica (solitamente un [[Hashing]]).

A differenza di una chiave crittografica, il Salt **non deve essere necessariamente segreto**. Il suo scopo principale non è nascondere, ma **differenziare**.

$$\text{Output} = \text{Hash}(\text{Input} \ || \ \text{Salt})$$

## 2. A cosa serve? (Obiettivi)

L'uso del salt risolve tre problemi fondamentali legati alla natura deterministica degli algoritmi:

1. **Garantire l'Unicità:** Assicura che due input identici producano output diversi.
    
    - _Esempio:_ Se Alice e Bob hanno entrambi la password "pippo", senza salt i loro hash nel database sarebbero identici (`a1b2...`). Con salt diversi, gli hash saranno completamente diversi.
        
2. **Prevenire Attacchi a Dizionario / Rainbow Tables:** Se un attaccante ha una tabella pre-calcolata di hash delle password più comuni ("Rainbow Table"), il salt rende quella tabella inutile. L'attaccante dovrebbe ricalcolare l'intera tabella per _ogni singolo_ salt diverso.
    
3. **Probabilismo (in RSA-PSS):** Trasforma uno schema di firma deterministico in uno probabilistico.
    

> [!abstract] Visual Metaphor
> 
> Immagina di cucinare un piatto (l'input). Se segui la ricetta alla lettera (algoritmo deterministico), il sapore sarà sempre identico. Il Salt è quel pizzico di spezia casuale che butti dentro ogni volta: il piatto è lo stesso, ma il sapore finale è unico per quella specifica preparazione.

## 3. Utilizzo negli Schemi

Il salt è onnipresente nella crittografia moderna.

### A. Hashing delle Password

È l'uso più classico.

- Nel database si salva: `(username, salt, hash)`.
    
- Quando l'utente fa login, il sistema recupera il salt dell'utente, lo aggiunge alla password digitata, calcola l'hash e confronta.
    

### B. Firma Digitale ([[RSA-PSS]])

In RSA-PSS, il salt ha un ruolo cruciale per la sicurezza formale.

- **Funzionamento:** Durante l'encoding ([[EMSA-PSS]]), viene generato un salt casuale che viene inserito nell'hash intermedio $H'$.
    
- **Risultato:** Firmare lo stesso PDF due volte produce due firme digitali diverse (bit a bit), rendendo molto più difficile per un attaccante analizzare pattern o tentare attacchi di falsificazione.
    

## 4. Salt vs. Altri Concetti

Spesso si confonde con altri termini simili. Ecco le differenze:

|**Concetto**|**Segreto?**|**Unico?**|**Scopo Principale**|
|---|---|---|---|
|**Salt**|**NO**|Sì|Unicità dell'hash, prevenzione pre-computazione.|
|**Chiave ($K$)**|**SÌ**|-|Confidenzialità e Autenticazione.|
|**IV (Initialization Vector)**|No|Sì|Usato nella _cifratura a blocchi_ (es. AES-CBC) per randomizzare il primo blocco.|
|**Nonce**|No|Sì|"Number used Once". Usato per evitare attacchi di replay (es. in protocolli di rete).|

## 5. Best Practices

Per essere efficace, un Salt deve rispettare queste regole:

1. **Casualità Reale:** Deve essere generato da un [[CS-PRNG]] (Cryptographically Secure Pseudo-Random Number Generator).
    
2. **Lunghezza:** Deve essere sufficientemente lungo da rendere improbabili le collisioni (es. 128 bit o pari alla lunghezza dell'hash).
    
3. **Mai Riutilizzare:** Ogni utente/operazione deve avere il proprio salt unico.
    

---

**Vedi anche:**

- [[RSA-PSS]]
    
- [[Hashing]]
    
- [[MGF (Mask Generation Function)]]
    
- [[Rainbow Table]]