# RSAES (RSA Encryption Scheme)

**Tag:** #crittografia #RSA #standard #PKCS1 #sicurezza

## 1. Definizione
**RSAES** (RSA Encryption Scheme) è uno schema di cifratura completo basato sull'algoritmo RSA.
A differenza delle semplici primitive matematiche (come $c = m^e \pmod n$), RSAES definisce un protocollo sicuro che combina le operazioni RSA con uno **schema di padding** e conversioni standard di formato dati.

## 2. Componenti Fondamentali
Uno schema RSAES combina diverse primitive crittografiche per garantire la sicurezza:
- **Schema di Padding:** Aggiunge casualità e struttura al messaggio (es. [[OAEP]]).
- **Primitive di Conversione:**
* **[[OS2IP]]** (Octet-Stream to Integer Primitive): Converte il messaggio paddato in numero intero.
* **[[I2OSP]]** (Integer to Octet-Stream Primitive): Converte il risultato numerico della cifratura in byte.
- **Primitive RSA:**
	* **[[RSAEP]]** (RSA Encryption Primitive): L'operazione matematica $c = m^e \pmod n$.
	* **[[RSADP]]** (RSA Decryption Primitive): L'operazione matematica $m = c^d \pmod n$.

## 3. Varianti dello Standard
Esistono due varianti principali definite nello standard **PKCS#1**:

### A. RSAES-PKCS1-v1_5 (Legacy)
- **Stato:** Deprecato per nuovi sviluppi, ma ancora diffuso per compatibilità.
- **Padding:** Utilizza una struttura semplice con byte casuali non zero: `00 || 02 || PS || 00 || M`.
- **Sicurezza:** È vulnerabile ad attacchi di tipo **Chosen-Ciphertext (CCA)**, come l'attacco di Bleichenbacher (Padding Oracle).

### B. [[RSAES-OAEP]] (Moderno)
- **Stato:** Raccomandato per tutte le nuove applicazioni (PKCS#1 v2.2).
- **Padding:** Utilizza lo schema **OAEP** (Optimal Asymmetric Encryption Padding), che include funzioni hash (es. SHA-256) e una struttura a rete di Feistel.
- **Sicurezza:** Fornisce sicurezza provabile (IND-CCA2) ed è resistente agli attacchi Padding Oracle.

## 4. Processo di Cifratura (Generale)
Il flusso di cifratura in RSAES segue questi passi:
1. **Encoding (Padding):** Il messaggio $M$ viene trasformato in un messaggio codificato $EM$ (Encoded Message) usando lo schema di padding scelto (es. OAEP).
2. **Conversione (OS2IP):** $EM$ (in byte) viene convertito in un intero $m$.
3. **Cifratura (RSAEP):** Viene calcolato l'intero cifrato $c = m^e \pmod n$.
4. **Output (I2OSP):** L'intero $c$ viene convertito nel testo cifrato finale $C$ (in byte).

La decifratura segue il percorso inverso.

---
**Vedi anche:**
* [[RSA]]
* [[RSA-OAEP]]
* [[OS2IP]]
* [[I2OSP]]