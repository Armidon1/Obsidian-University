# Web of Trust (WoT): Il Modello di Fiducia Decentralizzato

**Tags:** #ingegneria #security #wot #pgp #trust_models #crittografia

## 1. Definizione e Filosofia

Il **Web of Trust (WoT)** è un modello di gestione della fiducia crittografica che rifiuta l'idea di un'autorità centrale (come le CA nella PKI).

In questo modello, ogni utente è una Certification Authority (CA).

La fiducia non scende dall'alto (gerarchica), ma emerge dal basso attraverso le interazioni tra pari (peer-to-peer). È il modello alla base di [[PGP]] (Pretty Good Privacy) e GPG.

---

## 2. Meccanismo di Funzionamento: Il Grafo Sociale

La fiducia si costruisce firmando le chiavi pubbliche degli altri utenti.

### La Logica Transitiva

Il principio cardine è la proprietà transitiva della fiducia, mitigata dal giudizio personale.

**The logic of transitive trust is:**

$$(\text{Io mi fido di } A) \land (A \text{ garantisce per } B) \implies (\text{Io posso fidarmi di } B)$$

> [!abstract] Visual Analysis
> 
> Immagina un Grafo Orientato:
> 
> - **Nodi:** Gli utenti (con le loro chiavi pubbliche).
>     
> - **Archi:** Le firme digitali (un utente firma la chiave di un altro).
>     
> - Per validare la chiave di uno sconosciuto, il software cerca un **percorso** (path) di firme che colleghi te a lui.
>     

### Key Signing Parties

Nel mondo reale, questo si traduceva in incontri fisici ("Key Signing Parties") dove le persone si mostravano i documenti di identità e si scambiavano le impronte digitali (fingerprint) delle chiavi per firmarle successivamente.

---

## 3. Livelli di Fiducia (Trust Levels)

In PGP/WoT, la fiducia non è binaria (Sì/No), ma sfumata. Un utente assegna due valori a una chiave importata:

1. **Validità:** La chiave appartiene davvero a quella persona? (Verificato tramite firma).
    
2. **Fiducia (Ownertrust):** Quanto mi fido di questa persona come "introduttore" di altri?
    
    - _Ultimate:_ (Io stesso).
        
    - _Full:_ Mi fido ciecamente delle sue firme.
        
    - _Marginal:_ Mi fido un po' (spesso servono 3 firme "marginali" per validare una chiave).
        
    - _None/Unknown:_ Non mi fido delle sue firme.
        

---

## 4. Analisi Critica: Pro e Contro

> [!tip] Exam Focus
> 
> È fondamentale saper confrontare WoT con PKI. Il WoT è teoricamente più robusto contro la censura, ma praticamente inusabile su larga scala.

### Vantaggi (Resilienza)

- **Nessun Single Point of Failure:** Non esiste una Root CA che, se compromessa, fa crollare l'intero sistema (come successe a DigiNotar).
    
- **Decentralizzazione:** Difficile da censurare o controllare da parte di governi o enti singoli.
    
- **Fiducia Personale:** La fiducia è basata su relazioni reali, non su un contratto commerciale con una CA.
    

### Svantaggi (Scalabilità e Usabilità)

- **Non Scala (Scalability Issue):** Funziona bene in piccoli gruppi o cerchie di hacker, ma è impossibile creare un percorso di fiducia tra due sconosciuti agli antipodi del mondo ("Small World Problem").
    
- **Soggettività:** Il concetto di "fiducia" è vago. Alice potrebbe firmare chiavi con leggerezza, mentre Bob è paranoico. Se mi fido di Alice, eredito la sua "leggerezza".
    
- **Complessità (UX):** Per l'utente medio, gestire keyring, livelli di fiducia e firme è troppo difficile (barriera d'ingresso alta).
    
- **Privacy:** Il grafo delle firme è pubblico. Analizzandolo, si può ricostruire la rete sociale degli utenti (chi conosce chi).
    

---

## 5. Sintesi: WoT vs PKI

|**Caratteristica**|**Web of Trust (WoT)**|**PKI (X.509)**|
|---|---|---|
|**Struttura**|Grafo decentralizzato (Mesh)|Albero gerarchico|
|**Garanzia**|Reputazione sociale|Autorità Terza (CA)|
|**Validazione**|Percorso di firme (Path finding)|Catena di certificati alla Root|
|**Ambito Ideale**|Email (PGP), Software Open Source|Web (HTTPS), Enterprise, eID|