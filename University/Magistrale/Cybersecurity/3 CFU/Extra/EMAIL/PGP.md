# Mettere in sicurezza l'E-mail con PGP

**Pretty Good Privacy (PGP)** è uno standard creato da Phil Zimmermann nel 1991.

- È stato creato per "dare alle persone il potere di prendere la propria privacy nelle proprie mani".
    
- È ampiamente utilizzato dagli anni '90 e integra i migliori algoritmi crittografici disponibili (come RSA per l'asimmetrica e AES per la simmetrica) in un unico programma.
    
- Mentre l'originale PGP è ora di proprietà di Symantec, lo standard **OpenPGP** (definito nell'RFC 4880) è aperto, con implementazioni popolari come **Gnu Privacy Guard (GnuPG)**.
    

PGP fornisce due servizi principali, che possono essere usati separatamente o insieme:

1. Autenticazione (tramite Firma Digitale)
    
2. Riservatezza (tramite Crittografia)
    

---

### Autenticazione PGP (Solo [[Authentication]])
![[Pasted image 20251104175532.png]]

Questo processo fornisce **integrità del messaggio** (prova che non è stato alterato) e **autenticazione del mittente** (prova di chi lo ha inviato).

1. **Mittente:** Crea un messaggio (M).
    
2. **Hash:** Calcola un hash (un'impronta digitale) del messaggio (ad esempio, SHA-1 o SHA-256) H(M).
    
3. **Firma:** Crittografa (ovvero _firma_) l'hash utilizzando la **chiave privata ($PR_a$)** del mittente.
    
4. **Aggiunta:** Allega l'hash firmato al messaggio originale (che rimane in chiaro).
    
5. **Ricevente:** Riceve il messaggio e l'hash firmato.
    
6. **Decrittografa l'Hash:** Utilizza la **chiave pubblica ($PU_a$)** del mittente (che è pubblicamente disponibile) per decrittografare l'hash firmato e recuperare l'H(M) originale.
    
7. **Verifica:** Il ricevente calcola in modo indipendente l'hash del messaggio che ha ricevuto.
    
8. **Confronta:** Se i due hash corrispondono, il ricevente sa che il messaggio proviene dal mittente (autenticazione) e non è stato alterato (integrità).
    

---

### Riservatezza PGP (Solo [[Confidentiality]])
![[Pasted image 20251104175555.png]]
Questo processo assicura che solo il destinatario previsto possa leggere il messaggio. Utilizza un modello di **crittografia ibrida**, che combina l'efficienza della crittografia simmetrica (per il messaggio) con la sicurezza della crittografia asimmetrica (per la chiave).

1. **Mittente:** Crea un messaggio (M).
    
2. **Chiave di Sessione:** Genera una **chiave di sessione ($K_s$)** casuale e monouso (ad esempio, una chiave AES a 128 bit).
    
3. **Crittografia Messaggio:** Crittografa l'intero messaggio (M) utilizzando la chiave di sessione _simmetrica_ ($K_s$).
    
4. **Crittografia Chiave di Sessione:** Crittografa la chiave di sessione ($K_s$) utilizzando la **chiave pubblica ($PU_b$)** del _destinatario_.
    
5. **Aggiunta:** Allega la chiave di sessione crittografata al messaggio crittografato e invia.
    
6. **Ricevente:** Riceve il payload crittografato.
    
7. **Decrittografa Chiave di Sessione:** Utilizza la _propria_ **chiave privata ($PR_b$)** per decrittografare la chiave di sessione e recuperare $K_s$.
    
8. **Decrittografa Messaggio:** Utilizza la chiave di sessione recuperata ($K_s$) per decrittografare (simmetricamente) il messaggio (M).
    

---

### Confidentiality e Authentication
![[Pasted image 20251104175607.png]]

PGP può fornire entrambi i servizi sullo stesso messaggio. L'ordine delle operazioni è cruciale: **prima si firma, poi si crittografa**.

1. Il mittente crea una firma (hash firmato usando $PR_a$) e la allega al messaggio.
    
2. Il mittente crittografa _sia_ il messaggio originale _sia_ la sua firma utilizzando la chiave di sessione monouso ($K_s$).
    
3. Il mittente crittografa la chiave di sessione ($K_s$) usando la chiave pubblica del destinatario ($PU_b$) e la allega.
    

Il ricevente esegue i passaggi al contrario: prima decrittografa la chiave di sessione, poi decrittografa il pacchetto (messaggio+firma), e infine verifica la firma.

---

### Operazioni PGP

#### Compressione

- Di default, PGP **comprime** il messaggio _dopo_ la firma ma _prima_ della crittografia.
    
- Utilizza l'algoritmo di compressione ZIP.
    
- Questo permette di archiviare il messaggio non compresso e la firma per verifiche future.
    
- La compressione prima della crittografia è anche un'ottima pratica di sicurezza: riduce i pattern (schemi ripetitivi) nel testo in chiaro, rendendo più difficile l'analisi crittografica e gli attacchi all'algoritmo di crittografia.
    

#### Chiavi Pubbliche e Private PGP

- Un utente può avere molte coppie di chiavi. Per identificare quale chiave è stata usata, PGP usa un **Key ID**.
    
- Questo ID è (tipicamente) costituito dai **64 bit meno significativi della chiave pubblica** ed è altamente probabile che sia unico.
    
- Questo ID viene utilizzato nelle firme e nel componente della chiave di sessione crittografata, in modo che il ricevente sappia quale chiave privata (dal proprio portachiavi) utilizzare per la decrittografia.
    

---
### Formattazione dati per PGP
![[Pasted image 20251104180729.png]]

---
### Portachiavi PGP (Key Rings)

PGP non si affida a un server centrale per la ricerca delle chiavi. Invece, ogni utente mantiene una coppia di "portachiavi" (keyrings):

- **Portachiavi pubblico (public-key ring):** Un database locale contenente tutte le chiavi pubbliche di _altri_ utenti PGP note a questo utente, indicizzate per Key ID.
    
- **Portachiavi privato (private-key ring):** Contiene la/le coppia/e di chiavi (pubblica/privata) _dell'utente_. Le chiavi private in questo portachiavi sono esse stesse crittografate, protette da una chiave derivata da una **passphrase** (una password complessa) sottoposta ad hash.
    

La sicurezza delle chiavi private dipende quindi interamente dalla robustezza di questa passphrase.

---
### Generazione messaggi PGP
![[Pasted image 20251104180809.png]]

---
### Ricezione Messaggi PGP 
![[Pasted image 20251104180912.png]]

---

### Gestione delle Chiavi PGP (Web of Trust)

```
“As time goes on, you will accumulate keys from
other people that you may want to designate as
trusted introducers. Everyone else will each
choose their own trusted introducers. And
everyone will gradually accumulate and distribute
with their key a collection of certifying
signatures from other people, with the
expectation that anyone receiving it will trust
at least one or two of the signatures. This will
cause the emergence of a decentralized fault-
tolerant web of confidence for all public keys.” - Zimmermann
```

Il modello di gestione delle chiavi di PGP è la sua caratteristica più distintiva ed è in netto contrasto con il modello centralizzato S/MIME.

- PGP **non si affida a Certificate Authorities (CA)** centralizzate e fidate.
    
- Invece, **ogni utente è la propria CA**.
    
- Gli utenti **firmano le chiavi pubbliche** di altri utenti che conoscono direttamente, per _garantire_ la loro identità.
    
- Questo crea una **"rete di fiducia" (Web of Trust)** decentralizzata.
    

Puoi fidarti di una nuova chiave pubblica se:

1. L'hai firmata tu stesso (ti fidi completamente).
    
2. È stata firmata da qualcun altro di cui _ti fidi già_ per firmare altre chiavi.
    

Il portachiavi PGP include indicatori di "livello di fiducia" per gestire questo sistema. Questa "rete di fiducia tollerante ai guasti" consente a PGP di funzionare senza alcuna terza parte fidata centrale. Gli utenti possono anche emettere "certificati di revoca" per invalidare le proprie chiavi se vengono compromesse.