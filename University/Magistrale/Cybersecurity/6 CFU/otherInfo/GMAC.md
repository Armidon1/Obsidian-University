Nella crittografia, **GMAC** è l'acronimo di **Galois Message Authentication Code**.

È una funzione crittografica di autenticazione che deriva direttamente dal molto più noto algoritmo **GCM (Galois/Counter Mode)**, ed è specificamente progettata per autenticare i dati **senza crittografarli**.

![[Pasted image 20251103095853.png]]

---

## 🧐 Caratteristiche Principali di GMAC

GMAC è essenzialmente una versione di [[GCM]] che esegue solo la parte di autenticazione.

### 1. Basato su [[GHASH]] e $GF(2^{128})$

- **Algoritmo di Base:** GMAC utilizza la stessa funzione hash ad alte prestazioni **GHASH** vista nei tuoi appunti.
    
- **Aritmetica:** Sfrutta l'aritmetica del **Campo di Galois $\mathbf{GF(2^{128})}$** (moltiplicazione carry-less e XOR) per calcolare l'**Authentication Tag** (MAC) di un messaggio.
    

### 2. Differenza con GCM (Focus sull'Autenticazione)

La distinzione cruciale tra **GMAC** e **GCM** è l'assenza del componente di cifratura (Counter Mode):

|**Caratteristica**|**GMAC (Galois MAC)**|**GCM (Galois/Counter Mode)**|
|---|---|---|
|**Funzione**|**Solo Autenticazione**. Genera un MAC per i dati di input.|**Cifratura e Autenticazione (AEAD)**. Cifra il testo e autentica il ciphertext + AAD.|
|**Input Principale**|Solo i **Dati Aggiuntivi Autenticati (AAD)**.|**Testo in Chiaro** e **AAD** (Dati Aggiuntivi Autenticati).|
|**Output**|Solo il **Tag di Autenticazione** (MAC).|**Testo Cifrato** (Ciphertext) + **Tag di Autenticazione**.|

**In pratica:**

- **GCM** viene utilizzato quando vuoi che i tuoi dati siano **segreti** (_Cifratura_) e che tu possa verificarne l'integrità (_Autenticazione_).
    
- **GMAC** viene utilizzato quando vuoi che i tuoi dati siano **in chiaro** (_non crittografati_), ma che tu possa verificarne l'integrità e l'autenticità.
    

### 3. Utilizzo nel Mondo Reale

GMAC è spesso specificato in protocolli che richiedono l'autenticazione di metadati o intestazioni di pacchetti che devono rimanere visibili per il routing o l'elaborazione.

Un esempio comune è il protocollo **IPsec**, dove l'algoritmo **AES-GMAC** può essere usato per garantire l'integrità delle intestazioni di rete senza crittografare l'intero pacchetto (a differenza dell'uso di AES-GCM che cifrerebbe tutto il payload).
