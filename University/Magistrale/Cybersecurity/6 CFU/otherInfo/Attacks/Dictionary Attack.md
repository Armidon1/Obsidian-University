# Dictionary Attack (Attacco a Dizionario)

## 1. Definizione

Il **Dictionary Attack** è una tecnica di indovinamento delle credenziali che, invece di provare tutte le combinazioni possibili di caratteri (come nel *Brute Force* puro), tenta di indovinare la password utilizzando un elenco predefinito di parole probabili (un "dizionario").

Questo approccio si basa sul fatto che gli utenti tendono a scegliere password deboli o mnemoniche, spesso presenti in elenchi di parole comuni o password trapelate in precedenti violazioni.

## 2. Tipologie di Esecuzione

### A. Attacco Online

L'attaccante tenta di effettuare il login direttamente sul sistema target provando diverse password.

*
**Limite:** I sistemi moderni implementano il *Rate Limiting* (limitazione dei tentativi) o il blocco dell'account dopo N errori.


*
**Evasione:** Gli attaccanti cercano di aggirare questi limiti rallentando i tentativi o distribuendoli su molti IP (botnet).



### B. Attacco Offline (Il più pericoloso)

L'attaccante ottiene i dati crittografici (hash dal database o messaggi cifrati dalla rete) e tenta di craccarli sul proprio computer.

*
**Vantaggio per l'attaccante:** Non c'è alcun limite ai tentativi al secondo, l'unica barriera è la potenza di calcolo (CPU/GPU).


*
**Scenario:** Tipico quando viene rubato un database di password hashate.



## 3. Vulnerabilità nei Protocolli (Challenge-Response)

Un caso specifico e critico di Dictionary Attack avviene nei protocolli di autenticazione **Challenge-Response** basati su chiavi simmetriche derivate da password.

Lo Scenario

1. **Intercettazione:** Un attaccante in ascolto (Eavesdropper) cattura lo scambio tra Alice e Bob.
* Vede la sfida in chiaro: R (Nonce).
* Vede la risposta cifrata: K_{Alice-Bob}\{R\}.


2. **Debolezza:** Se la chiave K_{Alice-Bob} è derivata da una password umana (es. l'hash della password), l'entropia è bassa.

### L'Attacco KPA (Known Plaintext Attack)

L'attaccante possiede sia il testo in chiaro (R) che il testo cifrato (C = K\{R\}).

1. L'attaccante prende una parola dal dizionario ("password123").
2. La trasforma in una chiave di prova K'.
3. Calcola K'\{R\}.
4. Se il risultato è uguale a C, ha trovato la password.



> [!failure] Vulnerabilità Critica
> Questo attacco è possibile anche nei protocolli di **Autenticazione Mutua** non ottimizzati o se Trudy riesce a ingannare Alice iniziando una connessione falsa per farsi inviare una risposta cifrata da analizzare offline.
>
>

## 4. Difese e Mitigazioni

Per difendersi dai Dictionary Attack, si applicano strategie su più livelli:

### Lato Utente (Policy)

* Uso di password lunghe e complesse (alta entropia) che non esistono nei dizionari.
* Evitare il riutilizzo delle password.



### Lato Sistema (Storage & Protocolli)

1. **Salting:** Aggiungere una stringa casuale unica (Salt) alla password prima dell'hashing. Questo impedisce l'uso di dizionari pre-calcolati (Rainbow Tables).


2.
**Iterated Hashing:** Usare funzioni lente (es. bcrypt, Argon2, PBKDF2) che richiedono molto tempo per calcolare un singolo hash, rallentando drasticamente l'attacco offline.


3. **Key Derivation Robusta:** Nei protocolli di rete, evitare di usare chiavi derivate direttamente da password deboli per cifrare le sfide, oppure usare protocolli resistenti (es. PAKE - Password Authenticated Key Exchange, anche se non citato esplicitamente nei testi, è la soluzione logica al problema descritto).
4.
**Rate Limiting:** Essenziale per bloccare gli attacchi online.



---

**Vedi anche:**

* [[Autenticazione: Modelli di Attaccante]]
* [[Autenticazione a Chiave Simmetrica]]
* [[Hashing]]