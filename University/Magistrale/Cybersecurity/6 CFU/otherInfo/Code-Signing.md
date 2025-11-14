# ✍️ Code-Signing (Firma del Codice)

### Definizione

Il **Code-Signing** (Firma del Codice) è un **processo di firma digitale** applicato a file software eseguibili, script, driver o applicazioni (es. `.exe`, `.dll`, `.ps1`, `.apk`, `.jar`).

Il suo scopo è fornire due garanzie di sicurezza fondamentali all'utente finale e al sistema operativo _prima_ che il codice venga eseguito:

1. **Autenticità ([[Authenticity]]):** Conferma l'identità dello sviluppatore o dell'azienda (il _publisher_) che ha rilasciato il software.
    
2. **Integrità ([[Integrity]]):** Assicura che il codice non sia stato alterato, corrotto o infettato da malware da quando è stato firmato dal publisher.
    

### Come Funziona (Processo Tecnico)

Il processo si basa sulla crittografia a chiave pubblica (PKI) ed è suddiviso in due fasi:

![Immagine di Code-Signing process diagram](https://encrypted-tbn1.gstatic.com/licensed-image?q=tbn:ANd9GcR0wK2J_gvpb96GOLD2cN-B_d1ZqOzU8OTgmzJasAqMJA0UxAMKpRM-h03FqMR32r-qmiSzMr3hQcwiCnxjyA_JJH_OBSVf1VP2AOck3ttWk9kXcsE)


#### 1. Fase di Firma (Lato Sviluppatore)

1. **Hashing:** Il file eseguibile viene processato con una funzione di **hash** (es. SHA-256) per creare un _digest_ (un'impronta digitale) unico del codice.
    
2. **Firma (Signing):** Lo sviluppatore usa la sua **Chiave Privata** (protetta, spesso su un token hardware o HSM) per **cifrare l'hash**. Questo hash cifrato è la **firma digitale**.
    
3. **Impacchettamento (Bundling):** La **firma digitale** E il **certificato digitale** dello sviluppatore (che contiene la sua chiave pubblica e la sua identità, verificata da una **Certificate Authority - CA** fidata come DigiCert o Sectigo) vengono allegati all'eseguibile.
    

#### 2. Fase di Verifica (Lato Utente / Sistema Operativo)

Quando l'utente tenta di eseguire il file:

1. **Estrazione:** Il sistema operativo (es. Windows, macOS) estrae la firma digitale e il certificato dal file.
    
2. **Verifica della Fiducia (Trust):** Il sistema controlla il certificato:
    
    - È stato emesso da una **CA fidata** presente nel _trust store_ del sistema operativo?
        
    - Il certificato è scaduto o è stato revocato (controllando via OCSP/CRL)?
        
3. **Verifica dell'Integrità (Hashing):** Il sistema operativo calcola un **nuovo hash** del file eseguibile (usando lo stesso algoritmo, es. SHA-256).
    
4. **Verifica dell'Integrità (Decifratura):** Il sistema usa la **Chiave Pubblica** (presa dal certificato) per decifrare la firma digitale e recuperare l'**hash originale** (quello calcolato dallo sviluppatore).
    
5. **Confronto:** Il sistema confronta i due hash:
    
    - **Se corrispondono:** L'integrità è confermata. Il sistema sa chi è il publisher e che il file non è stato alterato.
        
    - **Se NON corrispondono:** Il file è stato modificato (corrotto o infettato da malware). Il sistema blocca l'esecuzione o mostra un avviso grave.
        

### Implicazioni di Sicurezza per Ingegneri

|**Area**|**Descrizione Tecnica**|
|---|---|
|**Difesa dal Malware**|È la difesa primaria contro gli attacchi _Man-in-the-Middle_ sulla distribuzione del software. Impedisce a un aggressore di intercettare un download e iniettare un trojan senza che l'utente se ne accorga.|
|**Driver e Accesso Kernel**|Nei moderni sistemi operativi (es. Windows 64-bit), la firma del codice è **obbligatoria** per i **driver (kernel-mode)**. Un driver non firmato non viene caricato, impedendo l'installazione di rootkit.|
|**Fiducia dell'OS (UX)**|Il sistema operativo utilizza la firma per la sua **politica di fiducia**.<br><br>  <br><br>• **Firmato (Verificato):** Windows SmartScreen mostra il nome del publisher verificato.<br><br>  <br><br>• **Non Firmato:** Il sistema mostra un avviso di sicurezza **grave** ("Publisher Sconosciuto"), scoraggiando attivamente l'esecuzione.|
|**Certificati EV**|I certificati **Extended Validation (EV) Code Signing** richiedono una verifica aziendale molto più rigorosa e l'uso **obbligatorio di un token hardware (HSM)**. Questo fornisce una reputazione immediata con i filtri (come SmartScreen) ed è la best practice per il software commerciale.|