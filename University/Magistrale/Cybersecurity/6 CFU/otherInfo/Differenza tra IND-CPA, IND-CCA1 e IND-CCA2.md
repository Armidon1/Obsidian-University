Ecco le differenze principali tra i tre livelli di sicurezza crittografica, basate sui documenti forniti:

### 1. IND-CPA (Indistinguishability under Chosen Plaintext Attack)

- **Nome completo:** Indistinguibilità sotto Attacco a Testo in Chiaro Scelto.
    
- **Capacità dell'Attaccante:** L'attaccante può chiedere di cifrare qualsiasi messaggio a sua scelta ("Chosen Plaintext") per vedere il risultato. Questo equivale ad avere accesso alla chiave pubblica o a un oracolo di cifratura.
    
- **Obiettivo:** L'attaccante non deve essere in grado di distinguere quale di due messaggi (scelti da lui) corrisponda a un dato testo cifrato.
    
- **Limite:** Questo modello non permette all'attaccante di decifrare nulla.
    

### 2. IND-CCA1 (Indistinguishability under Chosen Ciphertext Attack - Non-Adaptive)

- **Nome completo:** Indistinguibilità sotto Attacco a Testo Cifrato Scelto (non adattivo).
    
- **Capacità dell'Attaccante:** Oltre a poter cifrare, l'attaccante ha accesso a un **oracolo di decifratura**, ma con un limite temporale preciso: può decifrare testi cifrati arbitrari solo **prima** di ricevere la "sfida" (il testo cifrato target che deve indovinare).
    
- **Scenario:** Spesso chiamato "Lunchtime Attack" (l'attaccante usa il computer della vittima mentre è in pausa pranzo, poi perde l'accesso).
    

### 3. IND-CCA2 (Indistinguishability under Adaptive Chosen Ciphertext Attack)

- **Nome completo:** Indistinguibilità sotto Attacco a Testo Cifrato Scelto Adattivo.
    
- **Capacità dell'Attaccante:** È il livello più forte. L'attaccante può accedere all'oracolo di decifratura sia **prima che dopo** aver ricevuto la sfida.
    
- **Vincolo:** L'unica cosa che l'attaccante non può chiedere di decifrare è il testo cifrato della sfida stessa (altrimenti il gioco sarebbe banale).
    
- **Importanza:** Questo modello difende contro attacchi in cui l'avversario manipola il testo cifrato per vedere come reagisce il sistema (come l'attacco di Bleichenbacher contro RSA PKCS#1 v1.5). Gli schemi moderni come **RSA-OAEP** sono progettati per garantire proprio questo livello di sicurezza (IND-CCA2).
    

In sintesi, la differenza sta nel potere dell'attaccante rispetto alla decifratura:

- **IND-CPA:** Solo cifratura.
    
- **IND-CCA1:** Decifratura solo _prima_ della sfida.
    
- **IND-CCA2:** Decifratura _prima e dopo_ la sfida (Adattivo).