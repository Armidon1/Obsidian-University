# 🤝 ECDH (Elliptic Curve Diffie-Hellman)

### Definizione

**ECDH (Elliptic Curve Diffie-Hellman)** è un **protocollo di accordo sulla chiave** (_key agreement protocol_). È l'analogo del protocollo [[Diffie-Hellman Key Exchange]] (DH) standard, ma implementato utilizzando la matematica della **[[Elliptic Curve Cryptography - ECC]]**.

Il suo unico scopo è permettere a due parti (es. Alice e Bob) di stabilire un **segreto condiviso** (che diventerà la chiave per la cifratura simmetrica, come [[AES]]) su un canale di comunicazione insicuro, anche se un avversario sta ascoltando.

**Importante:** Come DH, ECDH da solo _non_ cifra i dati e _non_ fornisce autenticazione (quindi non da solo non procura [[Confidentiality]] e [[Authentication]]).

### 🔑 Come Funziona (Il Processo)

Il protocollo sostituisce l'esponenziazione modulare (lenta) di DH con la **moltiplicazione scalare** (veloce) di ECC.

1. Parametri Pubblici Comuni:
    
    Alice e Bob si accordano pubblicamente su:
    
    - Una specifica **Curva Ellittica** (es. `Curve25519`).
        
    - Un **Punto Base $G$** (un punto pubblico noto su quella curva).
        
2. **Passaggi di Alice:**
    
    - Sceglie una **chiave privata $d_A$** (un numero intero casuale segreto).
        
    - Calcola la sua chiave pubblica $Q_A$ (un punto sulla curva) tramite moltiplicazione scalare:
        
        $$Q_A = d_A \times G$$
        
    - Invia il punto $Q_A$ a Bob.
        
3. **Passaggi di Bob:**
    
    - Sceglie una **chiave privata $d_B$** (un numero intero casuale segreto).
        
    - Calcola la sua chiave pubblica $Q_B$ (un punto sulla curva):
        
        $$Q_B = d_B \times G$$
        
    - Invia il punto $Q_B$ ad Alice.
        
4. **Creazione del Segreto Condiviso:**
    
    - Alice riceve $Q_B$ e usa la sua chiave privata $d_A$ per calcolare:
        
        $$S = d_A \times Q_B$$
        
    - Bob riceve $Q_A$ e usa la sua chiave privata $d_B$ per calcolare:
        
        $$S' = d_B \times Q_A$$
        
5. Il Risultato:
    
    Entrambi arrivano allo stesso identico punto $S$ sulla curva, perché la moltiplicazione scalare è associativa:
    
    - $S = d_A \times (d_B \times G) = (d_A \cdot d_B) \times G$
        
    - $S' = d_B \times (d_A \times G) = (d_B \cdot d_A) \times G$
        
    - $S = S'$
        
6. Fase Finale (KDF):
    
    Il "segreto" $S$ è un punto (una coppia di coordinate x, y). Non è una buona chiave crittografica. Alice e Bob usano la coordinata x del punto $S$ come input per una Key Derivation Function (KDF) (es. HKDF) per derivare la chiave simmetrica finale.
    

### Dettagli Tecnici e Implicazioni per Ingegneri

| **Caratteristica**                | **Descrizione Tecnica**                                                                                                                                                                                                                                                                                                                                |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Efficienza (Vantaggio su DH)**  | È il motivo principale per cui ECDH è preferito. Offre la stessa sicurezza di DH con **chiavi molto più piccole** (es. 256 bit vs 3072 bit), risultando in:<br><br>  <br><br>• Meno CPU (calcoli più veloci)<br><br>  <br><br>• Meno banda (handshake più piccoli)                                                                                     |
| **Sicurezza 🔒**                  | Si basa sulla difficoltà computazionale del **Problema del Logaritmo Discreto su Curve Ellittiche (ECDLP)**: dato $G$ e $Q_A$, è infattibile trovare $d_A$.                                                                                                                                                                                            |
| **Vulnerabilità (MitM)**          | Come DH, la versione "pura" di ECDH è vulnerabile a un attacco **Man-in-the-Middle (MitM)**, poiché le chiavi pubbliche $Q_A$ e $Q_B$ non sono autenticate.                                                                                                                                                                                            |
| **Autenticazione (La Soluzione)** | In pratica (es. TLS, SSH), ECDH non è mai usato da solo. È sempre **autenticato**: il server _firma_ i parametri dello scambio (es. $Q_B$) con la sua chiave privata a lungo termine (es. RSA o **ECDSA**) per dimostrare la sua identità.                                                                                                             |
| **Forward Secrecy (ECDHE)**       | La variante **[[ECDHE]]** è lo standard moderno in TLS. In ECDHE, le chiavi $d_A$ e $d_B$ sono **generate casualmente per ogni singola sessione** e poi distrutte. Questo garantisce la **Perfect Forward Secrecy (PFS)**: se la chiave privata a lungo termine del server viene rubata, le sessioni passate non possono essere decifrate. |