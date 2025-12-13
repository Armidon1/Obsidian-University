# IND-CCA1 (Indistinguishability under Chosen Ciphertext Attack - Non-Adaptive)

**Tag:** #crittografia #sicurezza #teoria #definizioni #attacchi

## 1. Definizione
**IND-CCA1** (Indistinguishability under Chosen Ciphertext Attack - Non-Adaptive) è una definizione di sicurezza per i sistemi di cifratura che modella un attaccante capace di decifrare testi cifrati arbitrari, ma solo per un periodo di tempo limitato.

È considerato un livello di sicurezza **più forte di [[IND-CPA]]** ma **più debole di [[IND-CCA2]]** (o semplicemente IND-CCA).

## 2. Il "Gioco" IND-CCA1
Lo scenario di attacco si svolge in fasi distinte tra un **Challenger** e un **Adversary**:

1. **Fase di Learning (Query 1):** L'avversario ha accesso a un **oracolo di decifratura**. Può inviare qualsiasi testo cifrato $C$ e ottenere il corrispondente messaggio $M$.
2. **Sfida (Challenge):** L'avversario sceglie due messaggi, $m_0$ e $m_1$, e li invia al Challenger. Il Challenger sceglie un bit casuale $b$, cifra $m_b$ e restituisce il **testo cifrato di sfida** $c^*$.
3. **Fase di Guess (Query 2 - Negata):** Qui sta la differenza fondamentale. Dopo aver ricevuto $c^*$, l'avversario **PERDE** l'accesso all'oracolo di decifratura. Non può più chiedere di decifrare nulla.
4. **Guess:** L'avversario deve indovinare se $c^*$ contiene $m_0$ o $m_1$.

## 3. L'Analogia del "Lunchtime Attack"
Questo scenario è spesso chiamato "Lunchtime Attack" (Attacco della Pausa Pranzo) o "Midnight Attack":
* Immagina che un attaccante abbia accesso al computer della vittima (e alla sua smart card di decifratura) mentre la vittima è in pausa pranzo.
* L'attaccante può decifrare molti messaggi passati per capire la struttura o le chiavi (**Fase di Learning**).
* Quando la vittima torna dal pranzo, l'attaccante viene cacciato e non ha più accesso alla smart card (**Accesso revocato dopo la sfida**).
* L'attacco ha successo se le informazioni raccolte durante il pranzo gli permettono di decifrare un nuovo messaggio cifrato (la sfida) che intercetta successivamente.

## 4. Confronto con altri livelli
La differenza principale risiede nel *quando* l'attaccante può usare l'oracolo di decifratura:

| Livello | Nome Completo | Capacità dell'Attaccante |
| :--- | :--- | :--- |
| **[[IND-CPA]]** | Chosen Plaintext | Può solo cifrare messaggi. Non può mai decifrare. |
| **IND-CCA1** | Chosen Ciphertext (Non-Adaptive) | Può decifrare testi cifrati **solo prima** di vedere la sfida. |
| **[[IND-CCA2]]** | Chosen Ciphertext (Adaptive) | Può decifrare testi cifrati **prima e dopo** aver visto la sfida (tranne la sfida stessa). |

## 5. Rilevanza Odierna
Sebbene sia un concetto teorico importante, nella pratica crittografica moderna si punta direttamente a **IND-CCA2**. Se un sistema è vulnerabile a IND-CCA2 (come [[PKCS#1]] v1.5), è considerato insicuro, anche se resiste a IND-CCA1.
Schemi come **[[RSA-OAEP]]** sono progettati per soddisfare il livello più alto (IND-CCA2).

---
**Vedi anche:**
* [[IND-CPA]]
* [[IND-CCA2]] (Attacco adattivo)
* [[RSA-OAEP]]
* [[Differenza tra IND-CPA, IND-CCA1 e IND-CCA2]]