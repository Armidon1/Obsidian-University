# EMSA (Encoding Method for Signature with Appendix)

**Tags:** #crittografia #RSA #firma_digitale #standard #encoding #PKCS1

## 1. Definizione

**EMSA** (Encoding Method for Signature with Appendix) è il metodo di codifica specificato nello standard **[[PKCS1|PKCS#1]]** per preparare i dati prima che vengano firmati con la primitiva RSA.

Rappresenta la fase di **preprocessing** nel paradigma di firma "Hash-then-Sign". La sua funzione è trasformare il messaggio originale (o meglio, il suo hash) in un blocco di dati formattato (Encoded Message, $EM$) adatto ad essere processato matematicamente dalla chiave privata.

## 2. Ruolo nello Schema RSASSA

Uno schema di firma [[RSA]] completo (**[[RSASSA]]**) non applica mai la chiave privata direttamente al messaggio grezzo. La formula concettuale è:

$$\text{RSASSA} = \text{RSA (Primitiva Matematica)} + \text{EMSA (Schema di Encoding)}$$

L'EMSA è responsabile di garantire proprietà di sicurezza come:

- **Padding:** Adattare la lunghezza del messaggio alla lunghezza del modulo RSA.
    
- **Struttura:** Evitare attacchi matematici possibili su testi non strutturati.
    
- **Casualità (in PSS):** Introdurre elementi probabilistici (salt).
    

## 3. Varianti dello Standard

Esistono due principali metodi EMSA definiti in PKCS#1:

### A. [[EMSA-PKCS1-v1_5]] (Legacy)

È il metodo di codifica classico e deterministico.

- Struttura: Costruisce il blocco $EM$ concatenando metadati rigidi:
    
    $$EM = 0x00 \ || \ 0x01 \ || \ PS \ || \ 0x00 \ || \ T$$
    
    - **$PS$ (Padding String):** Byte `0xFF` per riempire lo spazio.
        
    - **$T$:** Struttura ASN.1 (DigestInfo) che contiene l'algoritmo di hash e l'hash del messaggio.
        
- **Caratteristica:** Essendo deterministico, lo stesso messaggio produce sempre lo stesso $EM$ e quindi la stessa firma.
    

### B. [[EMSA-PSS]] (Moderno)
Detto anche PSS

È il metodo di codifica probabilistico raccomandato per nuove applicazioni (PKCS#1 v2.1+).

- **Struttura:** Utilizza un **Salt** casuale e una Mask Generation Function (MGF) per "mascherare" l'hash del messaggio all'interno del blocco $EM$.
    
- **Caratteristica:** Due codifiche dello stesso messaggio produrranno bit diversi (a causa del salt), aumentando la robustezza contro attacchi e side-channel.
    

---

**Vedi anche:**

- [[RSASSA]] (Lo schema di firma completo)
    
- [[RSASSA-PSS]] (Dettagli sull'encoding probabilistico)
    
- [[Digital Signature]]
    
- [[PKCS1]]