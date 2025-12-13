# RSAEP (RSA Encryption Primitive)

**Tag:** #crittografia #RSA #primitive #PKCS1 #standard

## 1. Definizione
**RSAEP** (RSA Encryption Primitive) è l'operazione matematica fondamentale di cifratura definita nell'algoritmo [[RSA]].
È specificata nello standard [[PKCS1]] e rappresenta il "cuore" del processo di cifratura asimmetrica.

## 2. Scopo
La primitiva prende un numero intero (che rappresenta il messaggio o una chiave simmetrica) e lo trasforma in un altro numero intero (il testo cifrato) utilizzando la **chiave pubblica** del destinatario.

- **Non è sicura da sola:** RSAEP è deterministica. Se usata direttamente su un messaggio (Textbook RSA), è vulnerabile a vari attacchi (es. attacchi a messaggi piccoli, attacchi di malleabilità). Per questo motivo, deve essere sempre utilizzata all'interno di uno schema di cifratura completo come [[RSAES-OAEP]] che include il padding.

## 3. Parametri
- **Input:**
* $(n, e)$: La chiave pubblica RSA.
* $n$: Il modulo RSA (prodotto di due grandi primi $p$ e $q$).
* $e$: L'esponente pubblico (solitamente $65537$).
* $m$: Il messaggio da cifrare, rappresentato come un intero compreso tra $0$ e $n-1$.
- **Output:**
* $c$: Il rappresentante intero del testo cifrato.

## 4. Funzionamento Matematico
L'operazione consiste in una **esponenziazione modulare**:

$$c = \text{RSAEP}((n, e), m) = m^e \pmod n$$

### Dettagli Algoritmici
Sebbene la formula sia semplice, l'implementazione pratica richiede efficienza e sicurezza:
- **Algoritmo Square-and-Multiply:** Utilizzato per calcolare l'esponenziazione $m^e$ in modo efficiente (complessità logaritmica rispetto all'esponente), evitando di calcolare numeri enormi prima del modulo.
- **Controllo del Range:** Prima di cifrare, si deve verificare che $0 \le m < n$. Se $m \ge n$, l'operazione fallisce ("message too long").

## 5. Operazione Inversa
L'operazione inversa, che recupera il messaggio originale $m$ dal testo cifrato $c$ utilizzando la chiave privata $(n, d)$, è chiamata:
- **[[RSADP]]** (RSA Decryption Primitive).

---
**Vedi anche:**
* [[RSA]]
* [[RSAES]] (RSA Encryption Scheme)
* [[RSA-OAEP]]
* [[OS2IP]] (Conversione Byte -> Intero prima di RSAEP)
* [[I2OSP]] (Conversione Intero -> Byte dopo RSAEP)