# 📈 Crittografia a Curva Ellittica (Elliptic Curve Cryptography - ECC)

### Definizione

La **Crittografia a Curva Ellittica (ECC)** è un approccio alla **crittografia a chiave pubblica** (PKC) basato sulla struttura algebrica delle curve ellittiche su campi finiti.

Non è un singolo algoritmo, ma una _famiglia_ di algoritmi che implementano la crittografia asimmetrica. La sua sicurezza si basa sulla difficoltà computazionale del **Problema del Logaritmo Discreto su Curve Ellittiche (ECDLP)**.

### Il Concetto Ingegneristico: "Perché ECC?"

L'unica e più importante ragione per cui ECC domina la crittografia moderna è l'**efficienza della dimensione della chiave**.

L'ECC offre lo **stesso livello di sicurezza** di sistemi più vecchi (come RSA) utilizzando **chiavi drasticamente più piccole**.

#### Confronto Sicurezza/Dimensione (Approssimativo)

|**Livello di Sicurezza (bit)**|**Dimensione Chiave ECC (bit)**|**Dimensione Chiave RSA (bit)**|
|---|---|---|
|80|160|1024|
|112|224|2048|
|**128**|**256**|**3072**|
|192|384|7680|
|256|521|15360|

Questo vantaggio non è lineare; la dimensione della chiave RSA cresce molto più rapidamente della dimensione della chiave ECC per mantenere la stessa sicurezza.

### Vantaggi Pratici per un Ingegnere

Chiavi più piccole si traducono direttamente in:

- **Minore Latenza (Velocità):** Meno calcoli necessari per la generazione delle chiavi e la creazione delle firme.
    
- **Minore Consumo di CPU:** Essenziale per server ad alto traffico e dispositivi a bassa potenza.
    
- **Minore Utilizzo di Memoria:** Meno RAM richiesta per le operazioni.
    
- **Minore Larghezza di Banda:** I certificati digitali e gli handshake (come in TLS) sono più piccoli e veloci.
    
- **Ideale per Dispositivi Vincolati:** È la scelta standard per **IoT**, **smartphone**, smart card e qualsiasi dispositivo con risorse limitate.
    

### Come Funziona (Concettualmente)

L'ECC sposta la crittografia dal "mondo" dei numeri interi (come RSA) al "mondo" dei **punti su una curva**.

1. La Curva: Si definisce una specifica curva ellittica (es. secp256k1 per Bitcoin, Curve25519 per TLS/SSH) su un campo finito. La curva è definita da un'equazione, tipicamente:
    
    $$y^2 = x^3 + ax + b$$
    
2. **Operazioni sui Punti:** Si definisce un'operazione "somma" (+) tra i punti. Dati due punti $P$ e $Q$ sulla curva, la loro somma $R = P + Q$ è un altro punto sulla curva.
    
3. **Chiavi (Analogo a RSA):**
    
    - **Chiave Privata ($d$):** È un **numero intero** (scalare) segreto, scelto casualmente.
        
    - **Punto Base ($G$):** È un punto pubblico, standardizzato e noto, definito dai parametri della curva (il "generatore").
        
    - **Chiave Pubblica ($Q$):** È un **punto** sulla curva.
        
4. Generazione della Chiave Pubblica:
    
    La chiave pubblica $Q$ è generata eseguendo l'operazione di "somma" sul punto base $G$ per $d$ volte. Questa operazione è chiamata moltiplicazione scalare:
    
    $$Q = d \times G \quad (\text{che significa } G + G + \dots + G \text{, } d \text{ volte})$$
    

### Il Problema Difficile (ECDLP)

La sicurezza di ECC si basa sul fatto che l'operazione di moltiplicazione scalare è una **funzione unidirezionale (trapdoor, [[OWF]])**:

- **Facile:** Conoscendo la chiave privata $d$ e il punto base $G$, è computazionalmente facile calcolare la chiave pubblica $Q$.
    
- **Infattibile:** Conoscendo la chiave pubblica $Q$ e il punto base $G$, è computazionalmente **infattibile** (impossibile con la tecnologia attuale) determinare $d$.
    

Questo è il **[[ECDLP|Problema del Logaritmo Discreto su Curve Ellittiche (ECDLP)]]**.

### Algoritmi Basati su ECC

L'ECC non è un algoritmo di cifratura in sé, ma la base per altri protocolli:

- **[[ECDH]]:** Utilizzato per l'**accordo di chiavi** (Key Agreement). È fondamentale in **TLS 1.3** per stabilire la chiave di sessione condivisa.
    
- **[[ECDSA]] (Elliptic Curve Digital Signature Algorithm):** Utilizzato per le **firme digitali**. È usato da Bitcoin, Ethereum e per autenticare gli aggiornamenti software.