# DNSSEC (DNS Security Extensions)

**Tags:** #CyberSecurity #DNS #NetworkSecurity #Cryptography #Protocol 
**Fonte:** [[6 - CS Application Level - DNS Security]]

---

## 📌 Concetto Fondamentale

**DNSSEC** è un set di estensioni del protocollo DNS progettato per aggiungere **integrità** e **autenticità** crittografica al sistema, che nativamente ne è privo. Il suo scopo è garantire che le risposte DNS non siano state falsificate (spoofing) o modificate durante il transito.

> [!warning] Cosa NON fa DNSSEC È fondamentale distinguere cosa DNSSEC garantisce da cosa _non_ garantisce:
> 
> - 🔴 **NON fornisce Confidenzialità:** I dati viaggiano ancora in chiaro (cleartext). Chiunque può vedere quali domini stai risolvendo.
> - 🔴 **NON protegge dai DoS:** Anzi, **aumenta il rischio DDoS** (vedi [[DDoS Amplification]]) perché rende i pacchetti di risposta molto più grandi.

---

## 🛡️ Obiettivi di Sicurezza

DNSSEC soddisfa tre proprietà principali:

1. **Origin Authentication:** Prova che i dati provengono effettivamente dal proprietario della zona.
2. **Data Integrity:** Prova che i dati non sono stati alterati in transito.
3. **Authenticated Denial of Existence:** Prova crittografica che un nome di dominio **non esiste** (tramite record NSEC/NSEC3).

---

## 🔑 I Nuovi Record DNS

Per funzionare, DNSSEC introduce nuovi tipi di Resource Record (RR):

- **RRSIG (Resource Record Signature):** Contiene la firma crittografica di un set di record (RRset). In DNSSEC non si firma il singolo record, ma l'intero RRset (es. tutti i record A insieme).
- **DNSKEY:** Contiene la **chiave pubblica** usata dai resolver per verificare le firme RRSIG.
- **DS (Delegation Signer):** È il "collante" della catena di fiducia. Si trova nella zona "genitore" e contiene l'hash della KSK della zona "figlia".
- **NSEC / NSEC3:** Usati per provare l'inesistenza di un dominio.

---

## ⛓️ Chain of Trust (Catena di Fiducia)

Il DNSSEC si basa su una catena gerarchica di fiducia che parte dalla **Root (.)**.

1. **Trust Anchor:** Il resolver ha pre-installata la chiave pubblica della Root Zone (gestita da ICANN).
2. **Verifica a catena:**
    - Il _Genitore_ (es. `.com`) firma un record **DS** che garantisce la chiave del _Figlio_ (es. `example.com`).
    - Il resolver verifica l'hash nel DS del genitore contro la DNSKEY del figlio. Se corrispondono, la chiave del figlio è fidata.

### Gestione delle Chiavi (ZSK vs KSK)

Per motivi di sicurezza e operatività, si usano due tipi di chiavi:

|Tipo Chiave|Nome Completo|Funzione|Rotazione|
|:--|:--|:--|:--|
|**ZSK**|Zone Signing Key|Firma i dati della zona (RRsets). È più piccola per velocità.|Frequente (giorni/settimane).|
|**KSK**|Key Signing Key|Firma solo le DNSKEY. È la "radice" della fiducia della zona.|Rara (es. annuale). Richiede interazione col genitore (DS update).|

---

## 🚫 Authenticated Denial & Zone Enumeration

Come si firma il "nulla" per dire che un dominio non esiste?

- **NSEC:** Collega un dominio esistente al successivo in ordine alfabetico.
    - _Problema:_ Permette la **Zone Enumeration** (un attaccante può scaricare l'elenco di tutti i domini della zona seguendo la catena).
- **NSEC3:** Evoluzione di NSEC che usa gli **hash** dei nomi invece dei nomi in chiaro. Previene l'enumerazione della zona pur garantendo la prova di inesistenza.

---

## 🔗 Collegamenti

- [[DNS Cache Poisoning]] (Attacco prevenuto da DNSSEC)
- [[DDoS Amplification]] (Attacco aggravato da DNSSEC)
- [[DNS Tunneling]]