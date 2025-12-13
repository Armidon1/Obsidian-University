# RSADP (RSA Decryption Primitive)

**Tag:** #crittografia #RSA #primitive #PKCS1 #standard

## 1. Definizione

RSADP (RSA Decryption Primitive) è l'operazione matematica fondamentale di decifratura definita nell'algoritmo [[RSA]].

È specificata nello standard [[PKCS1]] e rappresenta il meccanismo inverso di [[RSAEP]].

## 2. Scopo

La primitiva prende un numero intero (che rappresenta il testo cifrato) e lo trasforma nel numero intero originale (il messaggio o la chiave) utilizzando la **chiave privata** del ricevente.

- **Nota di Implementazione:** Come per la cifratura, il risultato di RSADP non è ancora il messaggio in chiaro utilizzabile. È un numero che deve essere successivamente convertito in byte (tramite [[I2OSP]]) e poi sottoposto a verifica e rimozione del padding (es. [[RSAES-OAEP]]) per ottenere il vero messaggio.
    

## 3. Parametri

- **Input:**
    
    - $K$: La chiave privata RSA. Può essere rappresentata in due forme:
        
        1. **Coppia semplice:** $(n, d)$.
            
        2. **Rappresentazione CRT** (per efficienza): $(p, q, dP, dQ, qInv)$.
            
    - $c$: Il rappresentante intero del testo cifrato (un numero compreso tra $0$ e $n-1$).
        
- **Output:**
    
    - $m$: Il rappresentante intero del messaggio.
        

## 4. Funzionamento Matematico

L'operazione base consiste in una **esponenziazione modulare** usando l'esponente privato $d$:

$$m = \text{RSADP}(K, c) = c^d \pmod n$$

### Ottimizzazione CRT (Teorema Cinese del Resto)

In pratica, calcolare $c^d \pmod n$ è computazionalmente costoso perché $d$ è un numero enorme. Le implementazioni reali (come in OpenSSL o Java) usano il **Chinese Remainder Theorem (CRT)** per velocizzare l'operazione di circa 4 volte.

Invece di un calcolo su modulo $n$, si eseguono due calcoli su moduli più piccoli $p$ e $q$:

1. $m_1 = c^{dP} \pmod p$ (dove $dP = d \pmod{p-1}$)
    
2. $m_2 = c^{dQ} \pmod q$ (dove $dQ = d \pmod{q-1}$)
    
3. Si combinano i risultati: $h = (m_1 - m_2) \cdot qInv \pmod p$
    
4. $m = m_2 + q \cdot h$
    

## 5. Gestione Errori

- **Ciphertext Representative Out of Range:** Se l'input $c \ge n$, l'operazione deve fallire, poiché un tale testo cifrato non può essere stato generato legittimamente con il modulo $n$.
    

## 6. Operazione Inversa

L'operazione inversa, che ha generato il testo cifrato $c$ dal messaggio $m$ usando la chiave pubblica $(n, e)$, è chiamata:

- **[[RSAEP]]** (RSA Encryption Primitive).
    

---

**Vedi anche:**

- [[RSA]]
    
- [[RSAES]] (Lo schema completo di cifratura)
    
- [[RSA-OAEP]] (Il padding che segue RSADP)
    
- [[I2OSP]] (Conversione del risultato $m$ in byte)