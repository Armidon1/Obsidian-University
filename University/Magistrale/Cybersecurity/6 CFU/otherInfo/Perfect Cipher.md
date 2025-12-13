# Perfect Cipher (Cifrario Perfetto)

**Tag:** #crittografia #teoria #shannon #sicurezza #OTP

## 1. Definizione

Un Cifrario Perfetto è un sistema di cifratura che garantisce la Sicurezza Incondizionata (o Perfect Secrecy).

Ciò significa che il testo cifrato non rivela alcuna informazione sul testo in chiaro, nemmeno a un attaccante con potenza di calcolo infinita.

## 2. Condizione di Shannon

Claude Shannon ha formalizzato matematicamente questo concetto nel 1949.

Un cifrario ha sicurezza perfetta se e solo se la probabilità che un certo messaggio $M$ sia stato cifrato, dato che è stato osservato il testo cifrato $C$, è identica alla probabilità che $M$ sia stato scelto a priori.

$$P(M | C) = P(M)$$

In parole semplici: **Intercettare il testo cifrato $C$ non cambia la conoscenza dell'attaccante sul messaggio $M$.** L'attaccante non può fare nulla di meglio che tirare a indovinare a caso.

## 3. L'Unico Esempio: One-Time Pad (OTP)

L'unico cifrario pratico che raggiunge la sicurezza perfetta è il **One-Time Pad (OTp)** (o Cifrario di Vernam).

### Funzionamento

- **Cifratura:** $C = M \oplus K$ (XOR bit a bit)
    
- **Decifratura:** $M = C \oplus K$
    

### Requisiti Rigorosi

Affinché sia davvero un Cifrario Perfetto, devono essere soddisfatte 3 condizioni **tassative**:

1. **Lunghezza Chiave:** La chiave $K$ deve essere **lunga almeno quanto** il messaggio $M$ ($|K| \ge |M|$).
    
2. **Casualità:** La chiave deve essere generata in modo **veramente casuale** (True Random) e uniforme. Non si possono usare [[PRNG]] (generatori pseudo-casuali).
    
3. **Monouso:** La chiave deve essere usata **una sola volta** e poi distrutta immediatamente (da qui "One-Time").
    

## 4. Perché non si usa sempre? (Il Problema della Gestione delle Chiavi)

Nonostante sia matematicamente inviolabile, il Perfect Cipher è impraticabile per la maggior parte delle applicazioni moderne a causa della gestione delle chiavi:

- Se devo scambiare in modo sicuro una chiave lunga 1GB per cifrare un file da 1GB, tanto vale scambiare direttamente il file su quel canale sicuro.
    
- La generazione di grandi quantità di numeri _veramente_ casuali è costosa e difficile.
    

## 5. Sicurezza Perfetta vs Sicurezza Computazionale

La crittografia moderna (es. [[RSA]], [[AES]]) rinuncia alla sicurezza perfetta in favore della **Sicurezza Computazionale**.

- **Perfect Secrecy:** Sicuro anche con tempo infinito. (Impossibile da rompere).
    
- **Computational Security:** Sicuro perché rompere il sistema richiederebbe un tempo irragionevole (es. miliardi di anni) con le tecnologie attuali. Schemi come [[RSA-OAEP]] puntano a livelli come [[IND-CCA2]], che sono computazionalmente sicuri ma non "perfetti" in senso teorico-informativo.
    

---

**Vedi anche:**

- [[RSA]] (Sicurezza Computazionale)
    
- [[Generazione Numeri Casuali]] (Requisito per OTP)
    
- [[IND-CPA]] (Livello di sicurezza standard per cifrari moderni)