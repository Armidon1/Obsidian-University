# **Symmetric Encryption (Cifratura Simmetrica)**

> È un **metodo di cifratura** in cui **la stessa chiave segreta** viene utilizzata sia per **cifrare** sia per **decifrare** i dati.

---

**Caratteristiche principali:**

1. **Chiave unica:** mittente e destinatario devono condividere la stessa chiave.
    
2. **Veloce:** adatto per cifrare grandi quantità di dati.
    
3. **Modalità operative:** può essere applicata a **blocchi** (block cipher) o a **flussi** (stream cipher).
    

---

**Garantisce:**

- ✅ **[[Confidentiality]]** – i dati sono illeggibili senza la chiave.
    

**Non garantisce da sola:**

- ❌ **[[Integrity]]** – non rileva modifiche al messaggio.
    
- ❌ **[[Authenticity]]** – chiunque con la chiave può cifrare o decifrare.
    

---

**Esempi:**

- **[[AES]] (Advanced Encryption Standard)** – block cipher
    
- **[[DES]] / [[3DES]]** – block cipher
    
- **[[ChaCha20]]** – stream cipher
    

---

**Vantaggi:**

- Alta velocità ed efficienza.
    
- Adatto per dati di grandi dimensioni.
    

**Svantaggi:**

- Distribuzione sicura della chiave tra mittente e destinatario può essere complessa (in questo viene usato l'[[Asymmetric Encryption]]).
    
- Se la chiave viene compromessa, l’intera comunicazione è a rischio.
    

---

**In breve:**

> **Symmetric encryption** = cifratura veloce e segreta con **una sola chiave condivisa**,  
> fornisce **[[Confidentiality]]**, ma necessita di ulteriori meccanismi per [[Authenticity]] e [[Integrity]].

# Symmetric Encryption per l'Authentication
# Autenticazione a Chiave Simmetrica

**Tags:** #engineering #cybersecurity #authentication #symmetric_key #protocols #challenge_response

## 1. Concetti Fondamentali

In questo scenario, l'autenticazione si basa su un segreto condiviso.

- **Presupposto:** Alice e Bob condividono una chiave segreta simmetrica, denotata come $K_{Alice-Bob}$.
    
- **Meccanismo:** Per autenticarsi, una parte deve dimostrare di conoscere la chiave $K$ senza inviarla mai in chiaro sulla rete.
    

### Tipologie di Direzionalità

1. **One-way (Unilaterale):** Una parte (Alice) prova la sua identità all'altra (Bob). Bob rimane anonimo/non verificato.
    
2. **Two-way ([[Mutual Authentication]]):** Entrambe le parti si autenticano a vicenda. Alice prova di essere Alice, e Bob prova di essere Bob.
    
    - _Nota:_ L'autenticazione mutua è più robusta se avviene **quasi simultaneamente** piuttosto che come due autenticazioni unilaterali separate.
        

---

## 2. Protocollo Challenge-Response (Sfida-Risposta)

È il metodo standard per l'autenticazione basata su Nonce (numeri casuali usati una volta sola).

Il flusso logico (Unilaterale: Alice si autentica a Bob) è il seguente:

1. **Alice** dichiara di essere Alice.
    
2. **Bob** invia una sfida (Nonce $R$) ad Alice.
    
3. **Alice** cifra la sfida con la chiave condivisa e la rispedisce.
    

$$\begin{align} 1. \ A &\rightarrow B : \text{"I am Alice"} \\ 2. \ B &\rightarrow A : R \\ 3. \ A &\rightarrow B : K_{Alice-Bob}\{R\} \end{align}$$

> [!abstract] Math Analysis
> 
> Bob decifra il messaggio ricevuto. Se il risultato corrisponde a $R$, allora chi ha inviato il messaggio possiede necessariamente la chiave $K_{Alice-Bob}$.
> 
> Questo protocollo può essere implementato anche usando [[HMAC]] al posto della cifratura reversibile.

### Vulnerabilità: Password Guessing

Se la chiave $K_{Alice-Bob}$ è derivata da una password umana (quindi debole/breve), questo protocollo è vulnerabile.

- Un attaccante che ascolta (Eavesdropper) cattura la coppia $(R, K\{R\})$.
    
- Può tentare un attacco di forza bruta offline ([[Dictionary Attack]]) provando a cifrare $R$ con tutte le password possibili finché non ottiene l'output catturato. Questo è un attacco di tipo **[[Known-Plaintext Attack (KPA)]]**.
    

---

## 3. Autenticazione Basata su Timestamp

Per ridurre il numero di messaggi (da 3 a 1), si può usare il tempo al posto di una sfida interattiva.

Alice invia direttamente il Timestamp cifrato:

$$A \rightarrow B : \text{"I am Alice"}, \ K_{Alice-Bob}\{\text{Timestamp}\}$$

> [!tip] Vantaggi e Svantaggi
> 
> - **Pro:** Molto efficiente (nessuno stato intermedio, meno messaggi).
>     
> - **Contro:** Richiede che gli orologi di Alice e Bob siano **sincronizzati**. Bob deve accettare il messaggio solo se il timestamp rientra in una piccola "finestra temporale" (Clock Skew) per evitare i Replay Attack.
>     

---

## 4. Attacchi Avanzati e Difese

### A. [[Replay attack]] (Attacco a Ponte)

Un attaccante $T$ (Trudy) si posiziona tra Alice e Bob. $T$ non conosce la chiave, ma fa da "ponte" trasparente.

1. $T$ finge di essere Alice con Bob.
    
2. Quando Bob invia la sfida $R$, $T$ la gira ad Alice (fingendo di essere Bob o un server legittimo).
    
3. Alice risolve la sfida (cifra $R$) e la rispedisce a $T$.
    
4. $T$ gira la soluzione a Bob.
    
5. **Risultato:** Bob accetta $T$ come se fosse Alice.
    

> [!failure] Defense Strategy
> 
> Per prevenire il Relay Attack serve la Distance Bounding o il Channel Binding:
> 
> - Verifica della prossimità fisica.
>     
> - Legare la risposta a caratteristiche del canale che $T$ non può inoltrare.
>     
> - Autenticazione Mutua (Alice deve verificare che sta parlando con il vero Bob prima di rispondere alla sfida).
>     

### B. [[Reflection Attack]] (Attacco di Riflessione)

Questo attacco sfrutta i protocolli di Autenticazione Mutua Ottimizzata dove si cerca di risparmiare messaggi.

Se Alice e Bob usano lo stesso protocollo simmetrico, Trudy può ingannare Bob facendogli risolvere la sua stessa sfida.

**Scenario:** Trudy vuole impersonare Alice verso Bob.

1. Trudy inizia la **Sessione 1** con Bob: "Sono Alice".
    
2. Bob invia la sfida $R_1$.
    
3. Trudy (che non ha la chiave) apre una **Sessione 2** simultanea con Bob, fingendo di essere Alice o riflettendo il segnale.
    
4. Trudy invia $R_1$ a Bob (nella Sessione 2) come se fosse la _sua_ sfida.
    
5. Bob risolve $R_1$ (perché deve autenticarsi nella Sessione 2) e invia la soluzione $K\{R_1\}$ a Trudy.
    
6. Trudy prende $K\{R_1\}$ e la usa per chiudere la **Sessione 1**.
    

> [!abstract] Come prevenirlo?
> 
> L'attacco funziona perché la sfida da A$\to$B è identica alla sfida da B$\to$A. Bisogna rompere questa simmetria:
> 
> 1. **Chiavi diverse:** Usare $K_{AB}$ per una direzione e una chiave diversa (es. $-K_{AB}$ o $K_{AB}+1$) per l'altra.
>     
> 2. **Formato diverso:** Il "Challenger" usa numeri pari, il "Responder" usa numeri dispari. In questo modo Bob non accetterà mai di risolvere una sfida "pari" se lui stesso ne ha inviata una "pari".
>     

---

## 5. Autenticazione Mutua Ottimizzata

Per evitare di scambiare troppi messaggi (un approccio ingenuo ne richiederebbe 5), si possono accorpare i dati.

### Protocollo a 3 Messaggi

1. **Alice $\to$ Bob:** "Sono Alice", invia la sua sfida $R_A$.
    
2. **Bob $\to$ Alice:** Invia la sua sfida $R_B$ **E** la soluzione alla sfida di Alice $K\{R_A\}$.
    
3. **Alice $\to$ Bob:** Invia la soluzione alla sfida di Bob $K\{R_B\}$.
    

In questo modo, in soli 3 passaggi, entrambe le parti sono autenticate. Tuttavia, questo design deve essere attentamente analizzato per evitare le vulnerabilità di riflessione descritte sopra.

vedi anche
- [[Authentication]] 
- [[Trusted Third Party (TTP)]]
- [[Kerberos]]