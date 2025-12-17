# Entropia (Informatica)

## 1. Definizione

In ambito informatico e crittografico, l'**Entropia** è la misura quantitativa dell'**incertezza** o dell'imprevedibilità di un'informazione.

Più formalmente, secondo la Teoria dell'Informazione di Claude Shannon, l'entropia misura la quantità media di informazione necessaria per descrivere lo stato di una variabile casuale.

In sicurezza, risponde alla domanda: "Quanto è difficile per un attaccante indovinare questo dato?"

- **Alta Entropia:** Dati completamente casuali, rumore, chiavi segrete forti.
    
- **Bassa Entropia:** Testo leggibile, pattern ripetuti, password deboli ("123456").
    

## 2. Unità di Misura: Il Bit di Entropia

L'entropia si misura in bit.

Attenzione: non confondere la lunghezza di una stringa con la sua entropia.

- **1 Bit di entropia** equivale all'incertezza del lancio di una moneta onesta (50/50).
    
- **$N$ Bit di entropia** significano che l'attaccante deve fare in media $2^{N-1}$ tentativi per indovinare il valore (brute force).
    

> [!example] Lunghezza vs Entropia
> 
> Confrontiamo due stringhe di 8 caratteri:
> 
> 1. **Stringa A:** `aaaaaaaa`
>     
>     - Lunghezza: 8 byte (64 bit).
>         
>     - Entropia: **~0 bit** (È perfettamente prevedibile).
>         
> 2. **Stringa B:** `7&xK9@mP`
>     
>     - Lunghezza: 8 byte (64 bit).
>         
>     - Entropia: **~52 bit** (Se generata casualmente).
>         
> 
> In crittografia, conta solo l'entropia, non lo spazio occupato.

## 3. La Formula di Shannon

Matematicamente, per una variabile $X$ con possibili valori $x_1, \dots, x_n$ e probabilità $P(x_i)$, l'entropia $H(X)$ è:

$$H(X) = - \sum_{i=1}^{n} P(x_i) \log_2 P(x_i)$$

Caso Ideale (Massima Sicurezza):

Se tutti i possibili valori sono equiprobabili (distribuzione uniforme), la formula si semplifica in:

$$H(X) = \log_2(N)$$

Dove $N$ è il numero totale di possibilità. Questo è l'obiettivo di ogni buon generatore di chiavi ([[CS-PRNG]]).

## 4. Ruolo nella Sicurezza

L'entropia è il "materiale grezzo" necessario per la sicurezza.

1. **Generazione Chiavi:** Una chiave AES a 128 bit è sicura _solo se_ è stata generata con 128 bit di vera entropia. Se il generatore era debole (es. entropia reale = 10 bit), l'attaccante deve provare solo $2^{10}$ chiavi, non $2^{128}$.
    
2. **Password:** Una password robusta deve avere alta entropia per resistere agli attacchi a dizionario.
    
3. **Seeding:** Il [[Seed]] di un PRNG deve avere entropia massima per garantire che la sequenza generata sia imprevedibile.
    

## 5. Raccolta dell'Entropia (Entropy Pool)

I computer sono macchine deterministiche e non producono entropia naturalmente. Devono "raccoglierla" dall'ambiente esterno tramite un [[TRNG]].

I Sistemi Operativi moderni gestiscono un **Entropy Pool** (una "vasca" di bit casuali):

- **Input:** Movimenti del mouse, timing della tastiera, interrupt hardware, rumore di rete.
    
- **Output:** Quando un programma chiede numeri casuali (es. `/dev/random` o `/dev/urandom` su Linux), il sistema preleva entropia dalla vasca.
    

> [!warning] Entropy Starvation
> 
> Se un server (specialmente una macchina virtuale senza mouse/tastiera) consuma numeri casuali più velocemente di quanto riesca a raccoglierli, la "vasca" si svuota.
> 
> In passato, questo bloccava i programmi (/dev/random bloccante). Oggi si usano i [[CS-PRNG]] per espandere quel poco di entropia vera in infiniti numeri pseudo-casuali sicuri.

---

**Vedi anche:**

- [[RNG (Random Number Generator)]]
    
- [[Seed]]
    
- [[TRNG (True Random Number Generator)]]
    
- [[CS-PRNG (Cryptographically Secure PRNG)]]