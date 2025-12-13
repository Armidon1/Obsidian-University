# IND-CPA (Indistinguishability under Chosen Plaintext Attack)

**Tag:** #crittografia #sicurezza #teoria #definizioni #attacchi

## 1. Definizione

IND-CPA (Indistinguishability under Chosen Plaintext Attack) è una definizione formale di sicurezza per i sistemi di cifratura.

Un sistema è sicuro IND-CPA se un avversario, capace di cifrare qualsiasi messaggio a sua scelta (accesso a un oracolo di cifratura), non è in grado di distinguere quale di due messaggi in chiaro sia stato cifrato in un dato testo cifrato.

## 2. Il "Gioco" IND-CPA

La sicurezza viene definita tramite un gioco mentale tra un **Challenger** (il sistema) e un **Adversary** (l'attaccante):

1. **Fase di Learning:** L'avversario può generare un numero a piacere di messaggi e chiedere al Challenger di cifrarli.
    
2. **Sfida (Challenge):** L'avversario sceglie due messaggi di uguale lunghezza, $m_0$ e $m_1$, e li invia al Challenger.
    
3. **Cifratura:** Il Challenger lancia una moneta (sceglie un bit casuale $b \in \{0, 1\}$), cifra il messaggio corrispondente ($c = Enc(m_b)$) e invia il testo cifrato $c$ all'avversario.
    
4. **Guess:** L'avversario deve indovinare se $c$ è la cifratura di $m_0$ o di $m_1$.
    

**Condizione di Vittoria:** Il sistema è sicuro IND-CPA se l'avversario non può fare meglio di un semplice indovino casuale (probabilità di successo $\approx 50\%$). In termini matematici, il "vantaggio" dell'avversario deve essere **trascurabile**.

## 3. Implicazione Fondamentale: Cifratura Probabilistica

Affinché uno schema sia IND-CPA, la cifratura deve essere probabilistica.

Ciò significa che cifrare lo stesso messaggio due volte deve produrre due testi cifrati diversi.

- **Perché?** Se la cifratura fosse deterministica (come in **[[RSA]] Textbook** o **AES-[[ECB]]**):
    
    1. L'avversario invia $m_0, m_1$.
        
    2. Riceve $c$.
        
    3. L'avversario calcola autonomamente $Enc(m_0)$ (poiché ha accesso alla funzione di cifratura/chiave pubblica).
        
    4. Se $Enc(m_0) == c$, allora sa che il messaggio era $m_0$.
        
    5. Il sistema deterministico è rotto istantaneamente.
        

## 4. Esempi

### Schemi SICURI (IND-CPA)

- **[[RSA-OAEP]]**: Utilizza un _seed_ casuale nel padding.
    
- **AES-[[CBC]]**: Utilizza un _IV_ (Initialization Vector) casuale.
    
- **AES-[[CTR]]**: Utilizza un _nonce/counter_ unico.
    

### Schemi INSICURI (NON IND-CPA)

- **Textbook RSA**: $c = m^e \pmod n$ è deterministico.
    
- **AES-ECB**: Blocchi identici producono testi cifrati identici.
    

## 5. Gerarchia di Sicurezza

IND-CPA è un livello di sicurezza intermedio:

1. **IND-EAV (Eavesdropping):** Sicurezza contro un attaccante passivo (solo ascolto).
    
2. **IND-CPA (Chosen Plaintext):** Sicurezza contro un attaccante che può cifrare (es. crittografia asimmetrica pubblica).
    
3. **IND-CCA / CCA2 (Chosen Ciphertext):** Sicurezza contro un attaccante che può anche _decifrare_ testi scelti (es. accesso a messaggi di errore del server). **[[RSA-OAEP]]** raggiunge questo livello, che è il più forte.
    

---

**Vedi anche:**

- [[RSA-OAEP]] (Esempio di schema IND-CPA e IND-CCA)
    
- [[Block Cipher Modes]] (Confronto tra modi sicuri e insicuri)
    
- [[Chosen-Ciphertext Attack (CCA)]]
- [[Differenza tra IND-CPA, IND-CCA1 e IND-CCA2]]