# RSA-PSS (Probabilistic Signature Scheme)

**Tag:** #crittografia #RSA #firma_digitale #standard #PKCS1 #sicurezza

## 1. Definizione

RSA-PSS (Probabilistic Signature Scheme) è uno schema di firma digitale probabilistico basato su RSA.

Definito nello standard PKCS#1 v2.1 (e successivi, come RFC 8017), è stato progettato per superare le debolezze del vecchio schema PKCS#1 v1.5.

## 2. Scopo

A differenza della cifratura, dove l'obiettivo è la confidenzialità, lo scopo di RSA-PSS è garantire:

- **Autenticità:** Il messaggio proviene davvero dal possessore della chiave privata.
    
- **Integrità:** Il messaggio non è stato modificato.
    
- **Non Ripudio:** Il firmatario non può negare di aver firmato il messaggio.
    

PSS offre una sicurezza dimostrabile nel modello dell'oracolo casuale, rendendo la firma robusta contro attacchi di falsificazione.

## 3. Caratteristiche Chiave

1. **Probabilistico:** Introduce un elemento casuale (salt). Firmare due volte lo stesso messaggio produce due firme digitali diverse, ma entrambe valide.
    
2. **Sicurezza:** Risolve i problemi di determinismo del vecchio standard v1.5, che era vulnerabile ad alcuni attacchi teorici.
    
3. **Flessibilità:** Permette di variare la lunghezza del salt e la funzione hash utilizzata.
    

## 4. Schema di Funzionamento

Il processo segue il paradigma **Hash-then-Sign**.

### Parametri

- $M$: Messaggio da firmare.
    
- $k$: Lunghezza del modulo RSA in byte.
    
- $hLen$: Lunghezza dell'output della funzione hash.
    
- $sLen$: Lunghezza del salt.
    

### Generazione della Firma (Semplificato)

1. **Hashing:** Si calcola l'hash del messaggio: $mHash = \text{Hash}(M)$.
    
2. **Salting:** Si genera un salt casuale e si concatena con $mHash$ e altri dati fissi, poi si calcola un nuovo hash $H'$.
    
3. Mascheramento (MGF): Si usa una Mask Generation Function (MGF) per mascherare il blocco dati (DB) che contiene il salt e il padding:
    
    $$maskedDB = DB \oplus \text{MGF}(H')$$
    
4. Encoding: Si costruisce il messaggio codificato $EM$:
    
    $$EM = maskedDB \ || \ H' \ || \ 0xbc$$
    
5. Firma (RSASP): Si applica la primitiva di firma RSA con la chiave privata $d$:
    
    $$S = EM^d \pmod n$$
    
    .
    

### Verifica della Firma

1. **Recupero (RSAVP):** Si usa la chiave pubblica $e$ per recuperare $EM$: $EM = S^e \pmod n$.
    
2. **Unmasking:** Si separa $EM$ per ottenere $maskedDB$ e $H'$. Si usa l'MGF per recuperare il $DB$ originale.
    
3. **Check:** Si estrae il salt dal $DB$ e si ricalcola l'hash $H'$ usando il messaggio originale $M$. Se l'hash calcolato coincide con quello estratto dalla firma, la firma è valida.
    

## 5. Confronto: PSS vs PKCS#1 v1.5

|**Caratteristica**|**PKCS#1 v1.5 (Legacy)**|**RSA-PSS (Moderno)**|
|---|---|---|
|**Tipo**|Deterministico (stesso mess. = stessa firma).|Probabilistico (stesso mess. = firma diversa).|
|**Sicurezza**|Manca di una prova formale di sicurezza.|**Provabilmente sicuro** (Random Oracle Model).|
|**Salt**|Non usato.|**Sì**, usa un salt casuale.|
|**Stato**|Ancora molto diffuso (es. certificati SSL legacy), ma sconsigliato per nuovi usi.|**Standard Raccomandato** (es. TLS 1.3, FIPS 186-5).|

---

**Vedi anche:**

- [[RSA]]
    
- [[Digital Signature Algorithm (DSA)]]
    
- [[PKCS#1]]
    
- [[Mask Generation Function (MGF)]]