# Certification Authority (CA): Il Garante della Fiducia

**Tags:** #ingegneria #security #pki #ca #trust_model #gerarchia

## 1. Definizione e Ruolo

La Certification Authority (CA) è una Terza Parte Fidata ([[Trusted Third Party (TTP)]]) che ha il compito di garantire l'identità dei soggetti in una rete.

Il suo scopo principale è risolvere il problema della distribuzione delle chiavi pubbliche: come faccio a sapere che la chiave pubblica di Alice appartiene davvero ad Alice e non a un attaccante?

**La CA risponde firmando digitalmente un documento (Certificato) che lega:**

1. L'Identità del soggetto (Subject).
    
2. La Chiave Pubblica del soggetto.
    

> [!abstract] Visual Analysis
> 
> Immagina la CA come un "Notaio Digitale". Non protegge il canale (quello lo fa la crittografia), ma garantisce l'identità degli interlocutori.

### Responsabilità Chiave

- **Emissione (Issuance):** Generare e firmare certificati.
    
- **Validazione:** Verificare che chi richiede un certificato sia chi dice di essere (spesso delegato a una **Registration Authority - RA**).
    
- **Gestione Ciclo di Vita:** Rinnovare i certificati in scadenza.
    
- **Revoca:** Pubblicare le liste dei certificati non più validi (CRL) o fornire servizi di verifica stato (OCSP).
    

---

## 2. Architettura Gerarchica (Trust Hierarchy)

Per motivi di sicurezza e scalabilità, le CA non operano come un blocco unico, ma sono organizzate in una struttura ad albero.

### A. Root CA (Trust Anchor)

È il vertice della piramide.

- **Self-Signed:** Firma il proprio certificato da sola.
    
- **Offline:** La chiave privata è custodita in **HSM (Hardware Security Modules)** scollegati dalla rete (air-gapped) per evitare furti.
    
- **Trust Store:** Il suo certificato è pre-installato nei Sistemi Operativi e Browser. È l'assioma di fiducia.
    

**The logic of the Trust Anchor:**

$$\text{Trust}(\text{Root}) = \text{True (Assioma)}$$

### B. Intermediate CA

È un'autorità delegata dalla Root.

- **Chained:** Il suo certificato è firmato dalla Root (o da un'altra Intermediate).
    
- **Online:** È perennemente connessa per firmare i certificati degli utenti finali o dei server.
    
- **Scopo:** Proteggere la Root. Se l'Intermediate viene compromessa, si revoca solo quel ramo, salvando la radice.
    

![[SCREEN_SLIDE_HIERARCHY]]

> [!abstract] Visual Analysis
> 
> What to look at: La Root CA emette certificati solo per le Intermediate CA. Le Intermediate CA emettono certificati per gli End-Entities (siti web, utenti).
> 
> Meaning: Questo crea una Catena di Fiducia che permette di validare un certificato finale risalendo fino alla radice.

---

## 3. Identificazione Tecnica: Cosa rende una CA tale?

Un certificato X.509 non è una CA solo perché "si chiama" CA. Deve avere estensioni tecniche specifiche che abilitano i poteri di firma.

**Here is the exact extension configuration:**

Plaintext

```
BasicConstraints ::= SEQUENCE {
    cA                  BOOLEAN DEFAULT TRUE, -- DEVE essere TRUE
    pathLenConstraint   INTEGER OPTIONAL      -- Profondità massima dell'albero
}

KeyUsage ::= BIT STRING {
    keyCertSign (5), -- Permesso di firmare certificati
    crlSign (6)      -- Permesso di firmare liste di revoca
}
```

> [!abstract] Code Analysis
> 
> - **cA=TRUE:** Senza questo flag, qualsiasi software rifiuterà di usare questo certificato per validarne altri. È la distinzione fondamentale tra un certificato CA e un certificato Utente.
>     
> - **keyCertSign:** È il "bit del potere". Abilita la chiave privata a firmare crittograficamente altri certificati.
>     

---

## 4. Rischi e Compromissione

La CA è un **Single Point of Failure**. Se la chiave privata di una CA viene rubata, l'attaccante può generare certificati validi per _qualsiasi_ sito o utente, rendendo possibili attacchi Man-in-the-Middle perfetti.

> [!failure] Common Pitfall
> 
> Il caso DigiNotar (2011): Una CA olandese fu compromessa. Gli hacker emisero certificati falsi per *.google.com. I browser degli utenti in Iran, vedendo un certificato valido firmato da una CA fidata (DigiNotar), accettarono la connessione, permettendo al governo di intercettare le email di Gmail.
> 
> Risultato: DigiNotar fu rimossa da tutti i Trust Store globali e fallì in poche settimane.

### Mitigazione del Rischio

1. **HSM:** Uso di hardware dedicato per proteggere le chiavi.
    
2. **Cerimonie di Firma:** Procedure fisiche rigide per accedere alla Root CA (richiede più persone, testimoni, registrazioni video).
    
3. **Path Constraints:** Limitare tecnicamente cosa può fare una CA Intermedia (es. "Puoi emettere certificati solo per il dominio `.it`").