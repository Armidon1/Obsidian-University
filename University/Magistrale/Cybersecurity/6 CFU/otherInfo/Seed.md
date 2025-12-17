# Seed (Seme)

## 1. Definizione

Il **Seed** (o _Seme_) è il valore iniziale utilizzato per inizializzare un generatore di numeri pseudo-casuali (**[[PRNG (Pseudo-Random Number Generator)]]**).

Poiché un PRNG è un algoritmo completamente **deterministico**, non può creare casualità dal nulla. Il Seed funge da "punto di ingresso" o "innesco": determina l'intera sequenza di numeri che il generatore produrrà da quel momento in poi.

$$\text{PRNG}(Seed_A) \rightarrow \{x_1, x_2, x_3, \dots \}$$

## 2. La Regola d'Oro (Determinismo)

La proprietà fondamentale del Seed è:

A parità di Seed, un PRNG produrrà sempre l'esatta stessa sequenza di numeri.

- **Se $Seed_A = Seed_B$ $\Rightarrow$ Sequenza A = Sequenza B.**
    
- **Se $Seed_A \neq Seed_B$ $\Rightarrow$ Le sequenze saranno (idealmente) completamente diverse.**
    

> [!example] Esempio Intuitivo: Minecraft
> 
> Se hai mai giocato a videogiocchi generati proceduralmente (come Minecraft o No Man's Sky), conosci già il concetto.
> 
> Se inserisci lo stesso "Seed del mondo" del tuo amico, il gioco genererà le stesse montagne, gli stessi fiumi e gli stessi villaggi nelle stesse identiche posizioni. Il computer sta usando quel seed per alimentare il PRNG che "costruisce" il mondo.

## 3. Il Seed nella Sicurezza (Entropia)

In crittografia, la sicurezza di un PRNG dipende quasi interamente dalla **segretezza** e dall'**imprevedibilità** del Seed.

Se un attaccante riesce a indovinare il Seed, ha "clonato" il tuo generatore: può calcolare tutte le chiavi crittografiche che hai generato o che genererai in futuro.

### Da dove arriva un buon Seed?

Per essere sicuro, il Seed deve provenire da una fonte di vera casualità ([[TRNG (True Random Number Generator)]]), ovvero deve avere un'alta [[Entropy]].

Le fonti tipiche per il "Seeding" includono:

1. **Hardware:** Rumore termico, interrupt di sistema.
    
2. **Sistema Operativo:** Il _Kernel Entropy Pool_ (es. `/dev/urandom` su Linux o `CryptGenRandom` su Windows), che raccoglie eventi casuali come movimenti del mouse, timing dei pacchetti di rete, etc.
    

> [!failure] Vulnerabilità Storica
> 
> Il caso Netscape (1996) è l'esempio classico di Bad Seeding.
> 
> Il browser usava come seed: Tempo Corrente + Process ID.
> 
> Un attaccante poteva facilmente indovinare l'orario (approssimativo) e provare i pochi PID possibili. Risultato: cifratura SSL violata in minuti.

## 4. Differenza tra Seed, Salt e Key

Spesso confusi, hanno ruoli diversi:

| **Termine**             | **Contesto**                                    | **Scopo**                                                         | **Stato**                                                                     |
| ----------------------- | ----------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| **Seed**                | [[PRNG (Pseudo-Random Number Generator)\|PRNG]] | Inizializzare un generatore per produrre una _sequenza_ infinita. | Stateful (cambia lo stato interno).                                           |
| **[[Salt (Crittografia) | Salt]]**                                        | [[Hashing]] / [[RSASSA-PSS]]                                      | Variare l'input di una funzione hash per rendere l'output unico _una tantum_. |
| **Key**                 | Cifratura ([[AES]]/[[RSA]])                     | Parametro segreto per trasformare (cifrare/decifrare) i dati.     | Persistente per la sessione.                                                  |

## 5. Reseeding (Rinfrescare il Seme)

Un [[CS-PRNG (Cryptographically Secure PRNG)|CS-PRNG]] (Secure PRNG) non dovrebbe usare lo stesso seed per sempre. Se lo stato interno venisse compromesso, l'attaccante potrebbe prevedere i numeri futuri.

Il Reseeding è la procedura periodica in cui il generatore:

1. Prende nuova entropia fresca dall'ambiente ([[TRNG (True Random Number Generator)|TRNG]]).
    
2. La mescola con lo stato interno attuale.
    
3. Crea un nuovo stato interno imprevedibile (garantendo la _Forward Secrecy_).
    

---

**Vedi anche:**

- [[PRNG (Pseudo-Random Number Generator)]]
    
- [[TRNG (True Random Number Generator)]]
    
- [[RNG (Random Number Generator)]]
    
- [[Entropy]]