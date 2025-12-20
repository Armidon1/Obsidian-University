# 👤 Adversary

> [!ABSTRACT] Definizione
> In sicurezza informatica, un **adversary** (o Threat Actor) è un individuo, un gruppo o un'organizzazione che tenta di compromettere la riservatezza, l'integrità o la disponibilità di un sistema informativo agendo con intenzioni malevole.

---

# Modelli di Attaccante

**Tags:** #engineering #cybersecurity #authentication #threat_modeling #attacker_model

## 1. Perché modellare l'Attaccante?

Nel design di un sistema sicuro, non è sufficiente implementare tecnologie difensive in modo generico. È necessario definire chiaramente chi è il nemico attraverso la modellazione dell'attaccante. Questo processo serve a:

- **Chiarire l'ambito della protezione:** Definire esplicitamente contro chi il sistema si sta difendendo.
    
- **Migliorare il design del protocollo:** Selezionare metodi di autenticazione che rispondano ai rischi reali, evitando complessità inutili per scenari a basso rischio.
    
- **Guidare la strategia di mitigazione:** Prioritizzare i controlli di sicurezza per gli attacchi più probabili e dannosi.
    

> [!tip] Exam Focus
> 
> Concentrare le risorse su minacce realistiche è più efficace che cercare di coprire ogni singolo "edge case" teorico.

---

## 2. Profilazione: Le Dimensioni dell'Attaccante

Un attaccante non è un'entità astratta, ma viene classificato in base a cinque dimensioni principali:

1. **Motivazione:**
    
    - Guadagno finanziario (frode, furto).
        
    - Spionaggio (aziendale o politico).
        
    - Sabotaggio o interruzione dei servizi.
        
    - Vendetta personale o ideologica.
        
2. **Risorse:**
    
    - Potenza computazionale (cluster CPU/GPU per brute force, botnet).
        
    - Tempo e pazienza per campagne a lungo termine.
        
    - Budget per acquistare exploit o dati rubati.
        
3. **Competenze (Skills):**
    
    - **Script Kiddies:** Bassa competenza, utilizzano tool pre-fatti.
        
    - **Professionisti / APT (Advanced Persistent Threats):** Alta competenza, capacità di sviluppare attacchi su misura.
        
4. **Livello di Accesso:**
    
    - Fisico (accesso diretto al dispositivo o alla rete).
        
    - Rete Locale (LAN).
        
    - Remoto (accesso basato su Internet).
        
5. **Persistenza:**
    
    - Attacco opportunistico "una tantum".
        
    - Intrusione continua e mirata.
        

---

## 3. Livelli di Capacità (Cosa possono fare?)

Oltre al profilo, è fondamentale capire come l'avversario interagisce con il sistema:

- **Avversario Passivo:**
    
    - Osserva il traffico di rete senza alterarlo.
        
    - Colleziona metadati (timestamp, indirizzi IP) per inferire comportamenti.
        
- **Avversario Attivo:**
    
    - Inietta, modifica o cancella messaggi di autenticazione.
        
    - Esegue il replay di credenziali valide precedentemente catturate.
        
- **Insider Threat (Minaccia Interna):**
    
    - Possiede credenziali legittime o accessi privilegiati.
        
    - Può aggirare molte difese perimetrali esterne.
        
    - Potrebbe collaborare con attaccanti esterni (collusione).
        

---

## 4. Vettori di Attacco Principali

Queste sono le tecniche concrete utilizzate per violare i sistemi di autenticazione:

### Attacchi Generici

- **Furto di Credenziali:**
    
    - Phishing diretto agli utenti.
        
    - Malware o keylogger che registrano la digitazione.
        
    - Furto di credenziali salvate da dispositivi compromessi.
        
    - Riutilizzo di coppie username/password provenienti da vecchi data breach (Credential Stuffing).
        
- **Brute Force e Guessing:**
    
    - Tentativi online (spesso limitati da rate limits).
        
    - Cracking offline di database di password hashate rubati.
        
- **Replay Attacks:**
    
    - Cattura di dati di autenticazione validi e reinvio successivo.
        
    - Sfrutta la mancanza di controlli sulla freschezza della sessione.
        
- **Man-in-the-Middle (MITM):**
    
    - Intercettazione e modifica di sessioni di autenticazione in tempo reale.
        
    - Utilizzo di certificati falsi o router compromessi.
        

### Minacce Specializzate

- **Biometric Spoofing:** Creazione di impronte artificiali, modelli facciali 3D o uso di foto/video.
    
- **Token Cloning:** Duplicazione fisica di smartcard o copiatura dei "seed" (semi) per gli OTP. Sfrutta protezioni hardware deboli.
    
- **Session Hijacking:** Furto di cookie di sessione o token tramite malware o XSS per bypassare la ri-autenticazione.
    
- **Social Engineering:** Impersonare utenti legittimi chiamando il supporto IT o ingannare l'utente per farsi rivelare le credenziali.
    

---

## 5. Scenari Realistici ed Esempi

Esempi concreti di applicazione dei modelli di attacco:

1. **Wi-Fi Hotspot non sicuro:**
    
    - Un attaccante passivo cattura traffico non cifrato.
        
    - Un attaccante attivo inietta pagine di login false.
        
2. **Abuso di Insider Aziendale:**
    
    - Un amministratore accede ad aree riservate senza controlli di autorizzazione adeguati.
        
    - Manipola i log di audit per nascondere le proprie tracce.
        
3. **Dispositivo Mobile Compromesso:**
    
    - Il malware bypassa l'autenticazione biometrica facendo il replay di dati salvati.
        
    - L'utente non è consapevole che il dispositivo agisce da proxy per l'attaccante.
        

---

## 6. Mappatura: Minacce vs Difese

Questa sezione è cruciale per la progettazione: ad ogni attacco corrisponde una specifica contromisura tecnica.

La relazione tra attacco e difesa può essere schematizzata così:

**1. Contro [[Man-in-the-Middle (MITM)]]:**

- Utilizzo di **Autenticazione Mutua** (Client e Server si autenticano a vicenda).
    
- Protocollo **[[TLS]]** con _certificate pinning_.
    

**2. Contro [[Replay Attack]]:**

- Uso di **[[Nonce]]** (numeri usati una volta sola) e **Timestamp** nei messaggi.
    
- **OTP** (One-Time Passwords) e token a vita breve.
    

**3. Contro Furto di Credenziali:**

- Implementazione della **[[MFA (Multi-Factor Authentication)]]**.
    
- Uso di token hardware o app mobili sicure.
    

**4. Contro Brute Force:**

- **Rate limiting** (limitazione tentativi) e blocco account (account lockouts).
    
- Hashing delle password con **[[Salt (Cryptographic)]]** e iterazioni multiple (es. bcrypt, Argon2).
    

**5. Contro Biometric Spoofing:**

- **Liveness detection** (rilevamento della "vivezza") e challenge-response biometrici.
    

---

## 7. Presupposti di Sicurezza e Design

Quando si progetta un sistema, bisogna partire da assunzioni realistiche e spesso pessimistiche.

> [!failure] Common Pitfall
> 
> Mai assumere che la rete sia sicura o che l'utente si comporti perfettamente.

- **Le reti non sono fidate:** Assumere sempre che il traffico possa essere monitorato da parti non autorizzate.
    
- **Gli endpoint possono essere compromessi:** [[Malware-Based Attacks|Malware]], [[Rootkits]] o configurazioni errate dei dispositivi sono rischi reali.
    
- **Gli utenti sono fallibili:** Sono suscettibili a [[Phishing]] e ingegneria sociale.
    
- **Le implementazioni sono imperfette:** Bug software, generatori di numeri casuali deboli e configurazioni errate sono la norma.
    

### Conclusione sul Design

Non esiste una soluzione unica ("One size does not fit all"). Bisogna definire "chi, cosa, come" prima di progettare le difese e aggiornare regolarmente i modelli di minaccia, poiché il panorama degli attacchi evolve nel tempo.

La sicurezza dell'autenticazione è la somma di: solidità del protocollo + sicurezza dell'endpoint + resilienza del fattore umano.