# Protocollo EKE (Encrypted Key Exchange)

Tags: #cryptography #authentication #protocols #key_exchange #EKE

Related: [[Diffie-Hellman Key Exchange]], [[Password Authentication]], [[Man-in-the-Middle (MITM)]]

## 1. Il Problema Iniziale

I protocolli di autenticazione classici soffrono di due grandi vulnerabilità quando si basano su password umane (che hanno bassa entropia):

1. **Diffie-Hellman (DH) Semplice:** Se usato "nudo e crudo" per scambiare una chiave, è vulnerabile agli attacchi _[[Man-in-the-Middle (MITM)]], poiché non c'è autenticazione dell'identità.
    
2. **Challenge/Response:** Se la password è debole, un attaccante che intercetta lo scambio può eseguire un **attacco a dizionario offline** per indovinarla.
    

**Obiettivo di EKE:** Permettere a due parti (Alice e Bob) di autenticarsi e stabilire una chiave di sessione forte condividendo _solo_ una password debole, rendendo impossibile l'attacco a dizionario offline.

---

## 2. Concetto Fondamentale

L'idea geniale di EKE è combinare lo scambio di chiavi Diffie-Hellman con una cifratura simmetrica basata sulla password debole.

Alice e Bob usano la password ($P$) per cifrare i messaggi dello scambio DH.

> [!TIP] Perché funziona?
> 
> Un attaccante che intercetta i messaggi vede dati cifrati con $P$. Se prova a decifrarli con una password a caso, ottiene un numero. Tuttavia, non ha modo di verificare se quel numero è valido (cioè se corrisponde davvero a $g^a \pmod p$) senza risolvere il problema del logaritmo discreto, che è computazionalmente intrattabile.

---

## 3. Il Protocollo Step-by-Step

### Setup

- **Alice ($A$)** e **Bob ($B$)** condividono un segreto debole $W$ derivato dalla password: $W = f(\text{password})$.
    
- Parametri pubblici DH: un numero primo grande $p$ e un generatore $g$.
    

### Flusso dello Scambio

1. Alice $\rightarrow$ Bob:
    
    Alice sceglie un numero casuale $a$ (privato). Calcola $g^a \pmod p$, lo cifra con $W$ e lo invia.
    
    $$A \rightarrow B : \text{"Alice"}, \; W\{ g^a \pmod p \}$$
    
2. Bob $\rightarrow$ Alice:
    
    Bob sceglie un numero casuale $b$ (privato) e genera un challenge $C_1$. Calcola $g^b \pmod p$, cifra tutto con $W$ e lo invia.
    
    $$B \rightarrow A : W\{ g^b \pmod p, \; C_1 \}$$
    
3. Calcolo della Chiave ($K$):
    
    Entrambi decifrano i valori ricevuti usando $W$. Ora possiedono i componenti DH ($g^a$ e $g^b$) e possono calcolare la chiave di sessione forte $K$:
    
    $$K = (g^b)^a \pmod p = (g^a)^b \pmod p = g^{ab} \pmod p$$
    
4. Verifica (Challenge/Response):
    
    Per confermare che entrambi hanno generato la stessa chiave $K$ (e quindi conoscevano la password corretta $W$), si scambiano dei challenge cifrati con la nuova chiave $K$.
    
    - Alice invia a Bob il challenge $C_1$ (ricevuto prima) e uno nuovo $C_2$.
        
        $$A \rightarrow B : K\{ C_1, C_2 \}$$
        
    - Bob risponde risolvendo il challenge $C_2$.
        
        $$B \rightarrow A : K\{ C_2 \}$$
        

---

## 4. Proprietà di Sicurezza

- **Resistenza agli attacchi a Dizionario:** Anche se la password è "123456", un attaccante non può confermare le sue ipotesi offline.
    
- **Perfect Forward Secrecy (PFS):** Se in futuro un attaccante scopre la password $W$, non potrà decifrare le sessioni passate perché la chiave $K$ è effimera e dipende dai valori casuali $a$ e $b$ che sono stati cancellati.
    
- **Autenticazione Mutua:** Entrambe le parti provano di conoscere la password.
    

---

## 5. Varianti di EKE

Esistono varianti che modificano la matematica dello scambio per ottenere lo stesso risultato:

### SPEKE (Simple Password Exponential Key Exchange)

Invece di cifrare il payload DH, usa il segreto $W$ come generatore al posto di $g$.

$$A \rightarrow B : W^a \pmod p$$

$$B \rightarrow A : W^b \pmod p$$

La chiave finale sarà $K = W^{ab} \pmod p$.

### PDM (Password Derived Moduli)

Il modulo $p$ (il numero primo) viene derivato dalla password, mentre il generatore $g$ è fisso (di solito $g=2$).

---

## 6. Il Limite: Augmentation

Il protocollo EKE base ha un difetto architetturale: il server deve conoscere $W$ (o la password in chiaro) per partecipare allo scambio.

Se il server viene compromesso, l'attaccante può impersonare l'utente.

Per risolvere questo problema, si usano protocolli Augmented EKE (come [[SRP (Secure Remote Password)]]), dove il server memorizza solo un verifier derivato dalla password, inutile per impersonare l'utente senza un attacco a dizionario aggiuntivo.