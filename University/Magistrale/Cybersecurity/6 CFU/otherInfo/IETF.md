# IETF (Internet Engineering Task Force)

**Tag:** #standard #internet #RFC #organizzazione #protocolli #networking

## 1. Definizione

L'IETF (Internet Engineering Task Force) è il principale organismo internazionale aperto che si occupa dello sviluppo e della promozione degli standard di Internet.

Non è una corporazione o un ente governativo, ma una grande comunità internazionale aperta di progettisti di rete, operatori, venditori e ricercatori.

## 2. Missione

La missione dell'IETF è descritta con la frase: "To make the Internet work better".

Si occupa principalmente dei livelli superiori dell'architettura di rete (dal livello TCP/IP in su), definendo protocolli cruciali come:

- **IP** (Internet Protocol)
    
- **TCP/UDP** (Transport)
    
- **HTTP** (Web)
    
- **TLS** (Sicurezza/Crittografia)
    

## 3. Il Prodotto: Le RFC

Il documento ufficiale prodotto dall'IETF è la RFC (Request for Comments).

Le RFC sono documenti tecnici che descrivono specifiche, protocolli, procedure ed eventi. Una volta che una specifica diventa uno standard IETF, le viene assegnato un numero di RFC immutabile.

- _Esempio pertinente:_ Lo standard **[[PKCS#1]]** (originariamente di RSA Security) è stato adottato dall'IETF e pubblicato come **RFC 8017**.
    

## 4. Filosofia: "Rough Consensus and Running Code"

A differenza di altri enti di standardizzazione (come ISO o ITU) che procedono per votazioni formali burocratiche, l'IETF si basa su un approccio pragmatico riassunto dalla celebre frase di David Clark (1992):

> _"We reject: kings, presidents and voting. We believe in: rough consensus and running code."_

1. **Rough Consensus (Consenso approssimativo):** Non serve l'unanimità, ma il senso prevalente del gruppo di lavoro deve essere d'accordo. Si evitano stalli burocratici.
    
2. **Running Code (Codice funzionante):** Uno standard non viene approvato solo sulla carta. Deve esserci un'implementazione dimostrabile e funzionante che provi la fattibilità della teoria.
    

## 5. Struttura Operativa

Il lavoro è diviso in **Working Groups (WG)**, organizzati per aree tematiche (es. Security Area, Transport Area).

- **Security Area:** È l'area che si occupa di standard come IPsec, [[TLS]], Kerberos, e algoritmi crittografici (inclusi gli aggiornamenti a [[RSA]] e curve ellittiche).
    

## 6. Importanza per la Crittografia

Molti standard crittografici nascono nel mondo accademico o aziendale (come RSA Labs), ma diventano standard globali inter-operabili solo quando passano attraverso l'IETF.

- L'IETF deprecata vecchi algoritmi (es. RC4, MD5, SSLv3) e raccomanda i nuovi parametri di sicurezza (es. lunghezza chiavi, padding [[RSA-OAEP]]).
    

---

**Vedi anche:**

- [[PKCS#1]] (Standard RSA mantenuto da IETF come RFC)
    
- [[TLS]] (Transport Layer Security - Standard IETF)
    
- [[RSA-PSS]] (Standardizzato in RFC 8017)