[[5 - CS Application Level - Web Security Part II|Previous Lesson]]
# DNS Security

**Tags:** #ingegneria #cybersecurity #DNS #sicurezza_reti #sapienza

---

## 1. Introduzione e DNS Namespace

Il **Domain Name System (DNS)** implementa un database distribuito fondamentale per il funzionamento di Internet.

### Struttura Gerarchica

Il DNS è una **gerarchia rigorosa** che inizia dalla radice (**Root**):

- **Root (.):** Costituita da 13 Logical Clusters (A-M), gestiti da IANA.
    
- **TLD (Top Level Domain):** Domini come `.com`, `.edu`. Sono gestiti dai **Registries** (es. Verisign).
    
- **SLD (Second Level Domain):** Domini come `example.com`. Sono gestiti dai **Registrars** o dai proprietari.
    

### Concetto di Delega

Il sistema è basato sul concetto di **delega**:

- La "parent zone" (zona genitore) **non contiene i dati**.
    
- Contiene invece dei puntatori, chiamati **NS records**, che indirizzano ai server autoritativi della "child zone" (zona figlia).
    

![[Pasted image 20260206141959.png]]

> [!abstract] Visual Analysis
> 
> **What to look at:** Lo schema ad albero che parte dal "DNS Server" in alto e scende verso i sottodomini.
> 
> **Meaning:** Mostra come la risoluzione scenda gerarchicamente:
> 
> 1. **Root server** (il punto di partenza).
>     
> 2. **TLD server** (es. server per `.com`, `.org`, `.edu`).
>     
> 3. **Authoritative server** (es. `google.com`, `un.org`).
>     
> 4. **Sub-domain** (il server finale, es. `www.google.com` o `blogs.american.edu`).
>     

---

## 2. Il Formato del Pacchetto DNS (RFC 1035)

Per comprendere gli attacchi, è necessario capire i "bit sul cavo" (bits on the wire). I pacchetti viaggiano solitamente su protocollo **UDP**.

### Campi Fondamentali

- **Transaction ID (16-bit):** È l'unico meccanismo nel DNS originale per abbinare le query (domande) alle risposte.
    
- **Flags:**
    
    - **QR:** Query/Response.
        
    - **AA:** Authoritative.
        
    - **RD:** Recursion Desired.
        
- **Counts (Conteggi):** Numero di domande, risposte, autorità e record addizionali.
    

![[Pasted image 20260206142014.png]]

> [!abstract] Visual Analysis
> 
> **What to look at:** La tabella che rappresenta l'Header del pacchetto.
> 
> **Meaning:** Si nota che i primi 16 bit (0-15) sono dedicati interamente all'**ID**. Seguono i flag e i conteggi (QDCOUNT, ANCOUNT, NSCOUNT, ARCOUNT).

---

## 3. Processo di Risoluzione dei Nomi

La risoluzione coinvolge diversi attori in una sequenza specifica.

**La sequenza standard:**

1. **User:** Invia una DNS Query (es. "example.com").
    
2. **Recursive DNS Resolver:** Riceve la richiesta dall'utente e inizia a interrogare la gerarchia.
    
3. **Root DNS Server:** Risponde indicando i server TLD.
    
4. **TLD Name Server:** Risponde indicando i server autoritativi.
    
5. **Authoritative DNS Resolver:** Fornisce l'indirizzo IP finale.
    
6. **Recursive Resolver:** Inoltra la risposta all'utente.
    

![[Pasted image 20260206142029.png]]

> [!abstract] Visual Analysis
> 
> **What to look at:** Le frecce numerate da 1 a 8 tra Utente, Recursive Resolver e i vari server (Root, TLD, Authoritative).
> 
> **Meaning:** Il Recursive Resolver fa il "lavoro sporco": interroga sequenzialmente Root, TLD e Authoritative per ottenere l'IP (192.0.0.16) e restituirlo all'utente.

---

## 4. Vulnerabilità nel DNS

Lo stato della sicurezza DNS viene analizzato secondo la triade CIA:

### Confidentiality (Riservatezza)

- **Status:** Inesistente nel DNS standard.
    
- **Threat (Minaccia):** Sorveglianza passiva (**Passive surveillance**). ISP, governi e attaccanti locali possono vedere ogni dominio richiesto.
    

### Integrity (Integrità)

- **Status:** Debole (basata solo sull'ID).
    
- **Threat (Minaccia):**
    
    - **Cache Poisoning:** Gli attaccanti possono modificare le risposte in transito o iniettare dati falsi nelle cache.
        
    - **Spoofing:** Non si può provare che una risposta provenga realmente dal proprietario della zona.
        

### Availability (Disponibilità)

- **Status:** Generalmente alta (grazie all'Anycast), ma vulnerabile.
    
- **Threat (Minaccia):**
    
    - **[[DDoS Amplification]]**.
        
    - [[NXDOMAIN floods]].
        
    - [[Phantom Domain attacks]].
        

---

## 5. Spoofing e Poisoning

Il DNS non include meccanismi di autenticazione. L'integrità è fornita debolmente solo tramite il **Transaction ID**.

### Criteri di Accettazione

Un resolver accetta una risposta solo se:

1. L'**IP Sorgente** corrisponde all'IP di destinazione della query.
    
2. La **Porta di Destinazione** corrisponde alla Porta Sorgente.
    
3. Il **Transaction ID** corrisponde.
    

### Race Condition

Se un attaccante riesce a inondare il resolver con tentativi ("guesses") prima che arrivi la risposta del server reale, può avvelenare (**poison**) la cache del resolver.

### Elementi che l'Attaccante deve indovinare/controllare

1. **Transaction ID (TXID):**
    
    - Campo a 16-bit → 65,536 possibilità.
        
    - I vecchi resolver usavano TXID prevedibili o sequenziali.
        
2. **Source Port (Porta Sorgente):**
    
    - Se non randomizzata, è facile da indovinare.
        
    - Con la randomizzazione della porta, l'entropia aumenta drasticamente.
        

#### Matematica dell'Entropia

Con la randomizzazione di porta e TXID, le combinazioni aumentano:

$$\sim 2^{16} \times 2^{16} \approx 4 \text{ miliardi di combinazioni}$$

3. **Query Name:**
    
    - L'attaccante innesca il resolver richiedendo un dominio sotto il suo controllo.
        
4. **Race Timing:**
    
    - La risposta falsificata deve arrivare **prima** della risposta reale autoritativa.
        

---

## 6. Dinamica dell'Attacco (Visual Sequence)

Le slide illustrano passo dopo passo come avviene l'attacco di **Cache Poisoning**.

### **Fase 1: Preparazione**

- L'attaccante forza il **Recursive Name Server** a interrogare un dominio (query per sottodomini casuali per causare "Cache miss").
    
- Il Resolver è costretto a interrogare il Nameserver Autoritativo.
    

### **Fase 2: L'Attacco (Flooding)**

- Mentre il Resolver attende la risposta dal server legittimo (es. Bank of America), l'attaccante invia migliaia di risposte DNS false.
    

**Il Payload dell'Attaccante:**

Le risposte false contengono:

- TXID indovinato.
    
- Porta sorgente indovinata.
    
- **Poison Payload:** Un record NS falso per il dominio target (es. `bank.com`).
    

**Implementazione del Payload Falso:**

Ecco come appare il record malevolo iniettato:

```
bank.com NS ns.evil.com
ns.evil.com A <attacker-IP>
```

### **Fase 3: Avvelenamento e Hijack**

- Se una risposta falsificata corrisponde ai criteri, il resolver **memorizza nella cache** il record NS malevolo.
    
- **Risultato:** Tutte le query future per `bank.com` vengono instradate ai server controllati dall'attaccante. Si tratta di un **Full Domain Hijack**.
    

> [!abstract] Visual Analysis
> ![[Pasted image 20260206142125.png]]![[Pasted image 20260206142140.png]]![[Pasted image 20260206142145.png]]![[Pasted image 20260206142149.png]]![[Pasted image 20260206142154.png]]
> **What to look at:** Il flusso tra Attacker, Recursive Name Server e User.
> 
> **Meaning:** L'attaccante sfrutta il tempo di attesa del server (frecce arancioni) per inserire la sua risposta falsa (blocco blu con codice) prima che arrivi quella vera. Una volta entrata nella cache, l'utente viene diretto verso l'attaccante.

---

## 7. Condizioni che facilitano il Poisoning

L'attacco ha più successo se sono presenti queste condizioni:

- **TXID randomization** debole o assente.
    
- Nessuna randomizzazione della **Source Port**.
    
- **Open Resolvers** raggiungibili su Internet.
    
- **Long TTLs** (TTL lunghi): se l'attacco riesce una volta, l'effetto persiste per molto tempo.
    
- Il Resolver accetta record **out-of-bailiwick** nelle sezioni Additional/Authority.
    

---

## 8. DDoS Amplification con DNS

Gli attacchi DDoS possono usare il servizio DNS per amplificare la risposta.

### Banda Asimmetrica (Asymmetric Bandwidth)

- **Richiesta (Request):** Piccola, circa 60 bytes (UDP).
    
- **Risposta (Response):** Grande, 3000+ bytes (usando EDNS0, query ANY).
    

### Fattore di Amplificazione

$$\text{Amplification Factor}: \sim 50x - 70x$$

![[Pasted image 20260206142219.png]]

> [!abstract] Visual Analysis
> 
> **What to look at:** La dimensione delle frecce rosse.
> 
> **Meaning:** Una piccola richiesta (Small spoofed DNS Request) genera molteplici risposte enormi (Amplified DNS Response) che convergono tutte sulla vittima, saturandola.

spiegazione più chiara [[Spigeazione  DDoS Amplification DNS|qui]]

---

## 9. DNS Tunneling

Il **DNS Tunneling** è una tecnica che codifica dati (comandi, informazioni esfiltrate) all'interno di query e risposte DNS.

**Perché si usa:**

- Il malware lo usa per aggirare firewall, restrizioni proxy e monitoraggio di rete.
    
- Il traffico DNS è solitamente considerato "fidato" e permesso.
    

### Approcci Possibili

1. **Dati codificati nel nome del dominio:**
    
    - Esempio: `h398lhd09JW78$.evil.com`
        
2. **Dati codificati nei campi di risposta:**
    
    - Uso di indirizzi IP restituiti.
        
    - Valori di ritorno di query TXT.
        
3. **Timing Channel:** Dati codificati nelle latenze di risposta.
    

### Flusso di Comunicazione (Communication Flow)

1. Il malware genera una query per un dominio con il payload.
    
2. La query raggiunge il server autoritativo dell'attaccante.
    
3. Il server decodifica il payload e risponde con una risposta DNS.
    
4. Il malware esegue il comando o continua il ciclo di esfiltrazione.
    

**Tipi di Query Usate:**

- **TXT records:** Per memorizzare testo arbitrario nelle risposte.
    
- **A/AAAA records:** Per codificare dati come indirizzi IP.
    
- **CNAME/MX:** Occasionalmente usati per offuscamento.

Spiegazione più chaira [[DNS Tunneling|qui]]

# DNS Security: DGA, Fast-Fluxing e DNSSEC

**Tags:** #ingegneria #cybersecurity #DNS #malware #DGA #FastFlux #DNSSEC

---

## 1. Domain Generation Algorithm (DGA)

Un **[[Domain Generation Algorithm (DGA)]]** è un algoritmo deterministico utilizzato dai malware per calcolare periodicamente grandi insiemi di nomi di dominio pseudo-casuali (**pseudo-random domain names**).

### Obiettivo Principale

L'obiettivo è identificare dinamicamente gli endpoint di **[[Command-and-Control (C2)]]**, evadendo al contempo le firme statiche (**static signatures**) e gli sforzi di rimozione (**takedown efforts**).

### Perché i malware usano i DGA?

Le slide elencano quattro motivazioni principali:

- **Resilience** (Resilienza).
    
- **Anti-blacklisting**.
    
- **Asymmetric advantage** (Vantaggio asimmetrico).
    
- **Obfuscation** (Offuscamento).
    

---

## 2. Funzionamento del DGA

Il processo operativo del codice DGA segue un ciclo specifico:

1. Genera una lista di domini (**domain list**).
    
2. Itera attraverso di essi.
    
3. Tenta la risoluzione DNS (**DNS resolution**).
    
4. Si connette al primo dominio che risponde.
    

### Inputs / Seeds

Gli elementi utilizzati per generare i domini includono:

- Timestamp corrente.
    
- Hard-coded keys.
    
- PRNG seeds.
    
- System parameters (parametri di sistema).
    
- Pseudo-random functions.
    

### Output

Il risultato è un grande insieme di **candidate domains** (es. centinaia o migliaia al giorno).

---

## 3. Tipologie di DGA

Le slide classificano i DGA in quattro categorie principali basate sulla tecnica di generazione.

### Time-based DGAs

- **Meccanismo:** Domini generati usando la data o l'orario di sistema.
    
- **Caratteristiche:** Facili da replicare per gli analisti, ma resilienti su larga scala.
    
- **Esempi:** Conficker, Bebloh.
    

### PRNG-based DGAs

- **Meccanismo:** Uso di generatori di numeri pseudo-casuali (**[[PRNG (Pseudo-Random Number Generator)]]**).
    
- **Algoritmi citati:** LCG, Mersenne Twister, xorshift.
    
- **Seeds:** Possono essere statici, condivisi o derivati da valori esterni.
    
- **Vantaggi:** Forniscono un ampio spazio di ricerca (**large search space**) e bassa prevedibilità senza reverse engineering.
    

### Seed-and-Key DGAs (Cryptographic DGAs)

- **Meccanismo:** Integrano funzioni crittografiche per generare domini.
    
- **Funzioni:** [[HMAC]], [[SHA-2]], [[AES]] o CRC.
    
- **Caratteristiche:** Alta entropia, difficili da prevedere senza la chiave.
    
- **Utilizzo:** Famiglie di malware avanzate (es. Bamital, Matsnu).
    

### Wordlist-Based DGAs

- **Meccanismo:** Domini composti concatenando parole da un dizionario (**dictionary words**).
    
- **Hybrid DGAs:** Combinano wordlists con PRNG o seeds.
    
- **Esempi:** Matsnu, Suppobox.
    

spiegazione più chiara [[Spiegazione DGA|qui]]

---

## 4. DNS Fast-Fluxing

Il **[[DNS Fast-Fluxing]]** è una tecnica di evasione e resilienza usata da [[Botnet]] e infrastrutture cybercriminali.

**Scopo:** Nascondere e proteggere servizi malevoli (es. server C2) dietro indirizzi IP che cambiano rapidamente (**rapidly changing IP addresses**).

**Principio:** Sfrutta le funzionalità del sistema DNS per far sì che un singolo dominio malevolo si risolva in molti IP diversi in intervalli di tempo molto brevi.

#### Esempio di Risoluzione

**Here is the exact implementation shown in the slides:**

```
malicious-domain.com
$TTL=60$ seconds
-> 45.12.33.10
   89.23.14.55
   102.44.12.19
   77.192.1.50
```

> [!abstract] Visual Analysis
> 
> **What to look at:** La lista di IP associata a un singolo dominio con un TTL molto basso.
> 
> **Meaning:** Un singolo dominio punta a quattro IP diversi, e questa associazione è valida solo per 60 secondi.

### Caratteristiche Tecniche

1. **Rapid IP Rotation (Rotazione rapida degli IP):**
    
    - Un singolo dominio malevolo è associato a centinaia o migliaia di host compromessi (**bots**).
        
    - I record A del DNS cambiano ogni pochi minuti o secondi.
        
    - Ogni risposta restituisce un sottoinsieme diverso di IP dei bot.
        
2. **Extremely Short TTL Values (TTL estremamente brevi):**
    
    - I valori TTL sono impostati intenzionalmente molto bassi.
        
    - Forza client e resolver a interrogare nuovamente il server DNS frequentemente.
        
    
    **The mathematical definition provided is:**
    
    $$TTL = 60 \text{ sec. or less}$$
    
3. **Use of Compromised Machines as Proxies:**
    
    - Gli IP restituiti appartengono solitamente a host compromessi che agiscono come **reverse proxies**.
        
    - Questi inoltrano il traffico a un piccolo numero di server backend nascosti (**hidden backend servers**).
        

---

## 5. Varianti del Fast-Fluxing

Le slide distinguono due varianti principali di questa tecnica.

### Single-Flux

- Cambiano rapidamente solo i **record A** (mappatura dominio $\to$ IP).
    
- La rotazione degli IP nasconde i nodi front-end.
    

### Double-Flux

- Ruotano sia i **record A** che i **record NS** (name server).
    
- **Conseguenza:** Molto più difficile da abbattere (**take down**) perché l'infrastruttura DNS stessa è in flusso ("fluxing").
    

> [!abstract] Visual Analysis
> 
> **What to look at:** La distinzione testuale tra Single e Double Flux.
> 
> **Meaning:** Nel Single-Flux cambia la destinazione (IP), nel Double-Flux cambia anche chi fornisce l'informazione (NS), creando un doppio livello di indirezione dinamica.

Spiegazione più chiara [[Spiegazione Fast Fluxing|qui]]

---

## 6. DNSSEC: Design Goals

**[[DNSSEC]] (DNS Security Extensions)** è un insieme di estensioni del protocollo che aggiungono integrità crittografica e autenticità al DNS.

**Riferimenti normativi:** RFCs 4033/4/5, 5155, 6781, 8145.

### Obiettivo

Assicurare che le risposte DNS non possano essere manomesse o falsificate (**tampered with or forged**), risolvendo attacchi come **cache poisoning** e **spoofing**.

### Cosa Fornisce (Provides)

1. **Origin Authentication:** Prova che i dati provengono dal proprietario della zona.
    
2. **Data Integrity:** Prova che i dati non sono stati modificati durante il transito.
    
3. **Authenticated Denial of Existence:** Prova che un dominio non esiste.
    

### Cosa NON Fornisce (DOES NOT provide)

1. **Confidentiality:** I dati sono ancora in testo in chiaro (**cleartext**).
    
2. **DoS Protection:** In realtà aumenta il rischio di DDoS!
    

---

## 7. Record DNSSEC

DNSSEC aggiunge tipi di record DNS addizionali per gestire la sicurezza crittografica:

- **RRSIG (signature):** Una firma crittografica su un set di record di risorse DNS (**RRset**).
    
- **DNSKEY:** La chiave pubblica (**public key**) usata per verificare le firme.
    
- **DS (Delegation Signer):** Collega la chiave della zona figlia alla chiave della zona genitore (formando una catena di fiducia, **chain of trust**).
    
- **NSEC/NSEC3:** Negazione autenticata dell'esistenza (prova che "quel nome non esiste").



# DNS Security: DNSSEC, NSEC e Protocolli Sicuri

**Tags:** #ingegneria #cybersecurity #DNS #DNSSEC #crittografia #protocolli

---

## 1. Resource Record Signature (RRSIG)

Il protocollo DNSSEC introduce il record **RRSIG** (signature). Si tratta di una firma crittografica applicata non al singolo record, ma a un **RRset** (Resource Record Set).

### Concetto di RRset

In DNSSEC:

- Non si firmano i record individuali.
    
- Si firma l'**RRset**, ovvero l'insieme di tutti i record dello stesso tipo per un determinato nome.
    

#### Esempio di Bundling

Tutti i record di tipo "A" per "www" vengono raggruppati ("bundled") e firmati insieme.

**Here is the exact implementation shown in the slides:**

```
www.example.com. 3600    IN    A    192.0.2.1
www.example.com. 3600    IN    A    192.0.2.2
- - - - - - - - - - - - - - - - - - - - -
All A records for "www" are bundled and signed
together
```

> [!abstract] Code Analysis
> 
> **Significato:** Se un resolver riceve un RRset con un record mancante (ovvero un sottoinsieme dei dati reali), la verifica della firma fallirà. Questo garantisce l'integrità completa del set di dati.

---

## 2. Struttura del Record RRSIG

Il record RRSIG contiene diversi campi fondamentali per la validazione:

- **Covered RRset Type:** Specifica quale tipo di record è stato firmato (es. A, AAAA, MX, TXT). Assicura che la firma sia valida solo per quel determinato RRset.
    
- **Algorithm:** L'algoritmo crittografico usato per creare la firma (es. RSA/SHA-256, ECDSA).
    
- **Labels:** Il numero di etichette nel nome di dominio originale (es. `www.example.com` → 3 labels). Usato per prevenire alcuni tipi di attacchi di replay.
    
- **Original TTL:** Il TTL dell'RRset al momento della firma.
    
- **Signature Expiration:** Data/ora dopo la quale la firma è considerata invalida.
    
- **Signature Inception:** Data/ora da cui la firma diventa valida.
    
- **Key Tag:** Identificatore della **DNSKEY** che può essere usata per verificare questa firma.
    
- **Signer Name:** Il nome di dominio della zona che ha generato la firma.
    
- **Signature Data:** La firma crittografica vera e propria.
    

---

## 3. DNSKEY: The Public Key

Il record **DNSKEY** contiene la Chiave Pubblica (**Public Key**) necessaria per verificare le RRSIG della zona.

**Here is the exact implementation shown in the slides:**

```
example.com. 3600 IN DNSKEY
256 3 8
(AwEAAagAIK1VZrpC6Ia7gEzahOR+9W29euxhJhVVLOyQbF5+...)
```

> [!abstract] Code Analysis
> 
> Analisi dei campi numerici mostrati nell'esempio:
> 
> - **256:** Flags (indica il tipo di chiave).
>     
> - **3:** Protocol (sempre 3 per DNSSEC come da RFC 4034).
>     
> - **8:** Algorithm (indica l'algoritmo crypto usato, es. RSA/SHA-256).
>     
> - **(Stringa Base64):** La chiave pubblica codificata.
>     

### Analisi dei Flags

- **256:** Indica una **Zone Signing Key (ZSK)**.
    
- **257:** Indica una **Key Signing Key (KSK)**.
    

---

## 4. ZSK vs. KSK

In DNSSEC si utilizzano due tipi di chiavi con ruoli distinti:

### ZSK (Zone Signing Key)

- Firma i resource records (RRsets) nella zona (es. A, TXT, ma **non** il DNSKEY).
    
- Protegge l'integrità e l'autenticità dei dati della zona.
    
- Viene ruotata frequentemente (giorni o settimane) per limitare l'esposizione in caso di compromissione.
    
- È più piccola della KSK per velocizzare la firma e la verifica.
    

### KSK (Key Signing Key)

- Firma l'**RRset DNSKEY** stesso.
    
- Stabilisce un **trust anchor** (ancora di fiducia) per la zona, collegandola alla zona genitore tramite il record **DS**.
    
- La KSK è essenzialmente la radice della fiducia ("root of trust") per quella zona.
    

---

## 5. DS: Delegation Signer

Il record **DS** è usato per collegare la chiave di una zona figlia alla zona genitore, formando parte della **chain of trust** (catena di fiducia).

### Funzionamento

1. Permette a un resolver di verificare che la DNSKEY della zona figlia sia autentica, usando la zona genitore come trust anchor.
    
2. Quando una zona figlia viene delegata (es. `example.com` sotto `.com`), il genitore memorizza un **hash** della KSK del figlio in un record DS.
    

### Verifica

Il resolver validante può:

- Partire dalla zona genitore (già fidata o validata).
    
- Verificare la KSK della zona figlia confrontando il suo hash con il record DS.
    
- Usare la KSK del figlio per validare le firme (RRSIG) di tutti gli altri record nella zona figlia.
    

> [!NOTE] Nota Operativa
> 
> - Puoi cambiare la **ZSK** localmente senza parlare con la Parent Zone (Registrar).
>     
> - Devi parlare con la Parent Zone solo quando esegui il rolling della **KSK**.
>     

---

## 6. Processo di Verifica DS (Esempio)

Supponiamo la catena: **Root (.)** $\to$ **TLD (.com)** $\to$ **example.com**.

1. Il Resolver si fida della chiave pubblica della root (trust anchor preconfigurata).
    
2. Il Resolver interroga `.com` per `example.com`.
    
3. La zona `.com` restituisce:
    
    - Record NS per `example.com`.
        
    - Record **DS** che punta alla KSK di `example.com`.
        
4. Il Resolver scarica l'RRset **DNSKEY** di `example.com`.
    
5. Il Resolver calcola l'hash della KSK usando il tipo di digest specificato nel DS.
    
6. Il Resolver confronta l'hash calcolato con il record DS in `.com`.
    
    - **Match:** la KSK del figlio è fidata.
        
    - **Mismatch:** la validazione fallisce.
        
7. Il Resolver ora può usare la KSK del figlio per verificare le RRSIG per il resto della zona.
    

---

## 7. Chain of Trust

La catena di fiducia si basa su una sequenza di validazioni che parte dalla Root fino al record desiderato.

![[Pasted image 20260206142537.png]]

> [!abstract] Visual Analysis
> 
> **What to look at:** La tabella che mostra la gerarchia Root $\to$ .edu $\to$ berkeley.edu.
> 
> **Meaning:**
> 
> - La **Root ZSK** firma il record **DS** per `.edu`.
>     
> - Il record **DS** contiene l'hash della **KSK** di `.edu`.
>     
> - Questo schema si ripete: il genitore firma l'hash della KSK del figlio, garantendo la continuità della fiducia fino all'Answer record finale (es. l'indirizzo A).
>     

### Gestione delle Chiavi Root

- Sono gestite da **ICANN**.
    
- Vengono ruotate periodicamente attraverso una "**Key signing ceremony**" pubblica.
    
- Le cerimonie sono verificabili online.
    

![[Pasted image 20260206142556.png]]

> [!abstract] Visual Analysis
> 
> **What to look at:** Le immagini delle casseforti ("SAFE 2") e degli schermi con i log delle operazioni.
> 
> **Meaning:** Dimostra la sicurezza fisica e la trasparenza procedurale con cui viene gestita la chiave privata della Root Zone di Internet.

---

## 8. NSEC: Authenticated Denial of Existence

**NSEC** risponde alla domanda: "Come possiamo certificare l'**assenza** di un nome di dominio?". In pratica, come si firma il "nulla"?

### Funzionamento

Un record NSEC collega un nome di dominio al **prossimo nome di dominio valido** nella zona, seguendo l'ordine canonico (**canonical order**).

**Here is the exact implementation shown in the slides:**

Plaintext

```
bar.example.com. 3600 IN NSEC foo.example.com. A MX RRSIG
```

> [!abstract] Code Analysis
> 
> Interpretazione del record:
> 
> 1. La zona non contiene nomi di dominio tra `bar` e `foo`.
>     
> 2. Il dominio `bar.` possiede solo i record A, MX e RRSIG; qualsiasi altro tipo non esiste.
>     
> 3. Il record è firmato da un RRSIG, quindi è verificato crittograficamente.
>     

### Vulnerabilità: Zone Enumeration

La ricerca viene eseguita fino alla fine della zona e ricomincia dall'inizio ("wraps-around").

**Effetto collaterale:** Permette la **Zone Enumeration for free** (un attaccante può scoprire tutti i domini presenti nella zona seguendo la catena NSEC).

---

## 9. NSEC3

**NSEC3** è un miglioramento di NSEC progettato per prevenire la **zone enumeration** pur fornendo la negazione autenticata dell'esistenza.

### Meccanismo

Invece di esporre i nomi di dominio in chiaro (**plain domain names**):

1. I nomi dei proprietari ("owner names") vengono hashari usando una funzione di hash crittografica (solitamente SHA-1).
    
2. I record NSEC3 collegano i nomi hashari al prossimo nome hashato nell'**ordine di hash** ("hashed order").
    
3. Il resolver esegue l'hash del nome richiesto e controlla la catena NSEC3.
    

Il record definisce dettagli come:

- Algoritmo di hash da usare.
    
- Salt.
    
- Iterazioni.
    

---

## 10. Altre Opzioni di Sicurezza DNS

Oltre a DNSSEC, esistono protocolli per proteggere la privacy e l'integrità del trasporto.

### DNS over TLS (DoT) - RFC 7858

- **Porta:** 853 (TCP).
    
- **Encryption:** Avvolge i pacchetti DNS in un tunnel **TLS**.
    
- **Pros:** Fornisce confidentiality, integrity e authentication.
    
- **Cons:**
    
    - Deve viaggiare su TCP.
        
    - Utilizzo di risorse maggiore (**Larger resource usage**).
        
    - Ritardi maggiori (**Larger delays**).
        
    - Può essere bloccato da alcuni firewall.
        

### DNS over HTTPS (DoH) - RFC 7858

- **Porta:** 443 (TCP).
    
- **Encryption:** Mescola le query DNS con il normale traffico HTTP.
    
- **Pros:**
    
    - Fornisce confidentiality, integrity e authentication.
        
    - Molto difficile da censurare/bloccare senza bloccare il web.
        
- **Cons:**
    
    - Controllo limitato da parte degli amministratori di rete.
        
    - Un canale disponibile per gli attaccanti (es. canali C2).