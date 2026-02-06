# Domain Generation Algorithm (DGA)

**Tags:** #CyberSecurity #Malware #DNS #Botnet #C2 **Fonte:** [[6 - CS Application Level - DNS Security]]

---

## 📌 Definizione

Il **Domain Generation Algorithm (DGA)** è un algoritmo deterministico utilizzato dai malware per generare periodicamente un ampio set di nomi di dominio pseudo-casuali. È una tecnica fondamentale per rendere le infrastrutture **[[Command-and-Control (C2)]])** resilienti e difficili da abbattere.

## 🛡️ Perché si usa (Vantaggi per l'attaccante)

L'obiettivo principale è l'evasione delle firme statiche e dei tentativi di takedown. Le slide evidenziano quattro vantaggi chiave:

1. **Resilienza:** Se un dominio viene abbattuto, il malware ne ha pronti altri migliaia.
2. **Anti-blacklisting:** È difficile mettere in blacklist domini che cambiano ogni giorno e non sono ancora stati registrati.
3. **Vantaggio Asimmetrico:** L'attaccante deve registrare solo _uno_ dei domini generati per quel giorno per riprendere il controllo; il difensore deve bloccarli o monitorarli _tutti_ (es. migliaia).
4. **Offuscamento:** Rende difficile individuare il vero server C2 tra il rumore.

---

## ⚙️ Funzionamento Tecnico

Il processo segue un ciclo continuo all'interno del codice del malware infetto:

1. **Input (Seeds):** L'algoritmo prende in input variabili variabili o segrete, come:
    - Data e ora correnti (Timestamp).
    - Chiavi "hard-coded" nel malware.
    - Semi per PRNG (Pseudo-Random Number Generator).
    - Parametri di sistema o funzioni crittografiche.
2. **Generazione:** Calcola una lista di domini candidati (spesso centinaia o migliaia al giorno).
3. **Risoluzione:** Il malware itera attraverso la lista e tenta di risolvere i domini via DNS.
4. **Connessione (Handshake):** Si connette al **primo dominio** che risponde con un IP valido (quello che l'attaccante ha effettivamente registrato per quel giorno).

---

## 🗂️ Tipologie di DGA

Le slide classificano i DGA in base alla complessità e al metodo di generazione:

### 1. Time-based DGA

- **Logica:** I domini sono generati basandosi sulla data o sull'ora del sistema.
- **Caratteristiche:** Facili da replicare per gli analisti di sicurezza (basta sapere la data), ma resilienti su larga scala.
- **Esempi:** _Conficker_, _Bebloh_.

### 2. [[PRNG (Pseudo-Random Number Generator)]]-based DGA

- **Logica:** Utilizzano generatori di numeri pseudo-casuali standard (es. Mersenne Twister, LCG).
- **Caratteristiche:** Offrono un ampio spazio di ricerca senza richiedere reverse engineering complesso.

### 3. Seed-and-Key (Cryptographic) DGA

- **Logica:** Integrano funzioni di hash o crittografiche (MD5, SHA-256, AES) usando una chiave segreta.
- **Caratteristiche:** Alta entropia. Sono molto difficili da prevedere per i difensori a meno che non si estragga la chiave dal malware.
- **Esempi:** _Bamital_, _Matsnu_.

### 4. Wordlist-based DGA

- **Logica:** I domini sono composti concatenando parole prese da un dizionario interno.
- **Caratteristiche:** Generano domini che sembrano legittimi ("human-readable") per ingannare gli amministratori che guardano i log. Spesso usati in approcci ibridi.
- **Esempi:** _Suppobox_, _Matsnu_.

---

## 🔗 Collegamenti

- [[Command-and-Control (C2)]]
- [[Botnet]]
- [[DNS Fast-Fluxing]] (Un'altra tecnica per nascondere il C2, spesso usata insieme ai DGA)
- [[DNS Tunneling]]