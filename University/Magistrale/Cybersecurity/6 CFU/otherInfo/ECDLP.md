# 🔒 Problema del Logaritmo Discreto su Curve Ellittiche (ECDLP)

### Definizione

Il **Problema del Logaritmo Discreto su Curve Ellittiche (ECDLP)** è il problema matematico **computazionalmente difficile** su cui si fonda l'intera sicurezza della **[[Elliptic Curve Cryptography - ECC|Crittografia a Curva Ellittica (ECC)]]**.

È un'analogia del [[Discrete Logarithm (DL) Problem|Problema del Logaritmo Discreto (DLP)]] standard, ma applicato al contesto dei _punti_ su una curva ellittica invece che ai _numeri_ in un gruppo moltiplicativo.

### La Funzione Unidirezionale (One-Way Function)

L'ECDLP definisce una funzione unidirezionale basata sull'operazione di **moltiplicazione scalare** (o "addizione ripetuta di punti") su una curva.

Dati:

- $G$: Un punto base pubblico (generatore della curva).
    
- $d$: Un numero intero segreto (la **chiave privata**).
    

È computazionalmente **FACILE** calcolare il punto $Q$ (la **chiave pubblica**) moltiplicando $G$ per $d$:

$$Q = d \times G \quad (\text{che significa } G + G + \dots + G \text{, } d \text{ volte})$$

Il **Problema del Logaritmo Discreto (ECDLP)** è il problema inverso: dati i punti pubblici $G$ e $Q$, è computazionalmente **INFATIBILE** trovare l'intero $d$.

$$d = \log_G(Q) \quad (\text{Trovare } d)$$

### Implicazioni Ingegneristiche

|**Caratteristica**|**Descrizione Tecnica**|
|---|---|
|**Fondamento di Sicurezza**|Tutta la sicurezza di **ECDH** (scambio chiavi) ed **ECDSA** (firme) dipende dal fatto che l'ECDLP sia un problema difficile da risolvere.|
|**Chiave Privata/Pubblica**|L'esponente $d$ è la chiave privata segreta. Il punto risultante $Q$ è la chiave pubblica che può essere condivisa.|
|**Efficienza (Vantaggio su RSA)**|L'ECDLP è considerato un problema "più difficile" del problema di fattorizzazione (alla base di RSA) e del DLP standard, a parità di dimensione.<br><br>  <br><br>**Questo è il motivo per cui l'ECC è così efficiente**: una chiave ECC da 256 bit offre una sicurezza paragonabile a una chiave RSA da 3072 bit.|