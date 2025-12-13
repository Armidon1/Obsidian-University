# RSASSA (RSA Signature Scheme with Appendix)

**Tags:** #crittografia #RSA #firma_digitale #standard #PKCS1 #sicurezza

## 1. Definizione

RSASSA (RSA Signature Scheme with Appendix) è la famiglia di schemi di firma digitale definita nello standard PKCS#1.

Rappresenta il metodo completo per generare e verificare firme digitali RSA in modo sicuro.

Il termine "with Appendix" significa che la firma è un'entità separata che viene allegata (appendice) al messaggio originale, e non serve a recuperare il messaggio stesso (come avviene invece negli schemi di firma con recupero del messaggio). Il messaggio $M$ è necessario in chiaro per verificare la firma.

## 2. Composizione dello Schema

Un algoritmo RSASSA non è solo l'operazione matematica RSA. È composto dalla combinazione di due elementi fondamentali:

$$\text{RSASSA} = \text{RSA} + \text{EMSA}$$

1. **RSA (Primitive):** Le operazioni matematiche di base.
    
    - **RSASP1:** Primitive di generazione firma ($s = m^d \pmod n$).
        
    - **RSAVP1:** Primitive di verifica firma ($m = s^e \pmod n$).
        
2. **EMSA (Encoding Method for Signature with Appendix):** Lo schema di codifica (padding e hashing) che prepara il messaggio prima di applicare la primitiva RSA. Questo è cruciale per la sicurezza.
    

## 3. Varianti dello Standard

Esistono due principali implementazioni di RSASSA definite in PKCS#1:

### A. RSASSA-PKCS1-v1_5 (Legacy)

È lo schema classico, basato sul paradigma **Hash-then-Sign** con padding deterministico.

- **Funzionamento:**
    
    1. Calcola $H = \text{Hash}(M)$.
        
    2. Codifica $EM = 0x00 \ || \ 0x01 \ || \ PS \ || \ 0x00 \ || \ T$ (dove $T$ contiene l'OID dell'hash e l'hash stesso).
        
    3. Firma $S = EM^d \pmod n$.
        
- **Stato:** Ancora ampiamente usato (es. certificati SSL vecchi, PDF signing), ma considerato **Legacy** per nuovi sviluppi a causa di potenziali vulnerabilità se implementato male (assenza di casualità).
    

### B. RSASSA-PSS (Probabilistic Signature Scheme)

È lo schema moderno e raccomandato (da PKCS#1 v2.1 in poi).

- **Funzionamento:** Utilizza un encoding probabilistico (PSS) che include un **Salt** casuale e una Mask Generation Function (MGF).
    
- **Vantaggi:**
    
    - **Probabilistico:** Due firme dello stesso messaggio sono diverse.
        
    - **Sicurezza:** Ha una prova di sicurezza formale più forte rispetto alla v1.5.
        
    - **Robustezza:** Elimina le vulnerabilità legate alla struttura deterministica del padding.
        

## 4. Confronto Sintetico

|**Caratteristica**|**RSASSA-PKCS1-v1_5**|**RSASSA-PSS**|
|---|---|---|
|**Tipo**|Deterministico|Probabilistico (Salt)|
|**Encoding**|EMSA-PKCS1-v1_5|EMSA-PSS|
|**Sicurezza**|Accettabile (con rischi impl.)|**Alta (Provabile)**|
|**Raccomandazione**|Compatibilità Legacy|**Nuovi Sistemi**|

---

**Vedi anche:**

- [[RSA-PSS]] (Dettagli sull'encoding PSS)
    
- [[Digital Signature]]
    
- [[PKCS#1]]
    
- [[Non-Repudiation]]