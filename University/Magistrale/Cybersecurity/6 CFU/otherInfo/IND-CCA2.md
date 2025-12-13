# IND-CCA2 (Indistinguishability under Adaptive Chosen Ciphertext Attack)

**Tag:** #crittografia #sicurezza #teoria #definizioni #attacchi #standard

## 1. Definizione

IND-CCA2 (spesso abbreviato semplicemente come IND-CCA) sta per Indistinguishability under Adaptive Chosen Ciphertext Attack.

È la definizione di sicurezza più forte per gli schemi di cifratura a chiave pubblica. Un sistema è sicuro IND-CCA2 se un attaccante non riesce a distinguere quale di due messaggi è stato cifrato, anche avendo accesso a un oracolo di decifratura che può utilizzare in modo adattivo (cioè, anche dopo aver visto il testo cifrato da decifrare).

## 2. Lo Scenario di Attacco (Il "Gioco")

La differenza cruciale rispetto alle definizioni precedenti sta nel _quando_ l'attaccante può usare l'oracolo.

1. **Fase di Learning (Query 1):** L'avversario può decifrare qualsiasi testo cifrato a sua scelta.
    
2. **Sfida (Challenge):** L'avversario invia due messaggi ($m_0, m_1$) al Challenger. Riceve il testo cifrato di sfida $c^* = Enc(m_b)$.
    
3. **Fase Adattiva (Query 2):** Dopo aver visto $c^*$, l'avversario **può continuare a usare l'oracolo di decifratura**.
    
    - **Vincolo Unico:** Non può chiedere di decifrare esattamente $c^*$ (sarebbe banale), ma può chiedere di decifrare _qualsiasi_ altro testo, anche modifiche di $c^*$.
        
4. **Guess:** L'avversario deve indovinare $b$.
    

## 3. Perché "Adattivo"?

Il termine "adattivo" indica che l'attaccante può adattare le sue richieste di decifratura basandosi sul testo cifrato di sfida che ha appena visto.

Questo modella scenari reali in cui un attaccante può manipolare il testo cifrato (malleabilità) e osservare come il sistema reagisce (es. messaggi di errore, tempi di risposta), come nell'Attacco di Bleichenbacher contro RSA PKCS#1 v1.5.

## 4. Confronto e Gerarchia

|**Livello**|**Descrizione**|**Note**|
|---|---|---|
|**[[IND-CPA]]**|Chosen Plaintext|L'attaccante può solo cifrare. Base minima per la sicurezza (es. randomizzazione).|
|**[[IND-CCA1]]**|Chosen Ciphertext (Non-Adaptive)|L'attaccante può decifrare _solo prima_ di vedere la sfida ("Lunchtime Attack").|
|**IND-CCA2**|Chosen Ciphertext (Adaptive)|L'attaccante può decifrare _prima e dopo_ la sfida. È il livello più robusto.|

## 5. Esempi Reali

- **Sicuri (IND-CCA2):**
    
    - **[[RSA-OAEP]]**: Progettato specificamente per raggiungere questo livello.
        
    - **RSA-KEM**: Key Encapsulation Mechanism.
        
- **Insicuri (Non IND-CCA2):**
    
    - **RSA PKCS#1 v1.5**: Vulnerabile perché malleabile e suscettibile ad attacchi oracolo.
        
    - **Textbook RSA**: Deterministico e completamente malleabile.
        

---

**Vedi anche:**

- [[RSA-OAEP]]
    
- [[IND-CCA1]]
    
- [[IND-CPA]]
    
- [[Chosen-Ciphertext Attack (CCA)]]
- [[Differenza tra IND-CPA, IND-CCA1 e IND-CCA2]]
 