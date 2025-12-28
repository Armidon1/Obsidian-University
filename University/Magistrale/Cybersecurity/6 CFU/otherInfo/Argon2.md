# Argon2

## 1. Che cos'è?

Argon2 è un moderno algoritmo di hashing delle password (KDF - Key Derivation Function).

È stato il vincitore della Password Hashing Competition (PHC) nel 2015 ed è considerato lo standard di riferimento attuale per l'archiviazione sicura delle password, superando i precedenti standard come PBKDF2 e bcrypt.

## 2. Obiettivo e Difesa

L'obiettivo principale di Argon2 è contrastare il **password cracking offline**, rendendo computazionalmente costoso per un attaccante indovinare le password anche se possiede il database degli hash.

Le sue proprietà difensive chiave sono:

1. **Memory-Hardness:** L'algoritmo è progettato per richiedere una grande quantità di memoria RAM per essere calcolato. Questo limita drasticamente l'efficacia delle **GPU** e degli **ASIC** (hardware specializzato usato dagli attaccanti), che sono ottimizzati per la velocità di calcolo puro ma hanno una larghezza di banda di memoria limitata o costosa.
    
2. **Resistenza ai Side-Channel:** Dispone di varianti ottimizzate per evitare attacchi basati sulla tempistica (Side-Channel Attacks).
    
3. **Salt Integrato:** Include nativamente il supporto per il salt per prevenire attacchi basati su Rainbow Tables.
    

## 3. Parametri di Configurazione ($t, m, p$)

La forza unica di Argon2 risiede nella sua **alta configurabilità**. A differenza dei predecessori che scalavano solo sulle iterazioni, Argon2 permette di regolare il costo su tre dimensioni diverse per adattarsi all'hardware del difensore:

- **Time Cost ($t$):** Il numero di iterazioni (quanto tempo di CPU richiede).
    
- **Memory Cost ($m$):** La quantità di RAM che l'algoritmo deve riempire (es. 64MB, 1GB).
    
- **Parallelism ($p$):** Il numero di thread o core utilizzati per il calcolo.
    

> [!tip] Vantaggio Strategico
> 
> Questa flessibilità permette di massimizzare l'uso delle risorse del server. Se un server ha molta RAM libera ma poca CPU, si può aumentare $m$ e ridurre $t$. Per l'attaccante, replicare questa quantità di RAM su milioni di tentativi paralleli diventa economicamente insostenibile.

## 4. Varianti Principali

Esistono due versioni principali di Argon2:

- **Argon2d:** Ottimizzato per la resistenza contro le GPU (massima memory-hardness), ma vulnerabile ai side-channel attack (adatto per criptovalute, meno per password).
    
- **Argon2i:** Ottimizzato per resistere ai side-channel attack (accesso alla memoria indipendente dai dati segreti).
    
- **Argon2id:** (Raccomandato) Una versione ibrida che usa l'approccio di Argon2i per la prima passata e Argon2d per le successive. È la scelta di default per lo storage di password.
    

## 5. Confronto con altri Algoritmi

| **Algoritmo**  | **Tipo**      | **Resistenza GPU** | **Salt Built-in** | **Note**                                                  |
| -------------- | ------------- | ------------------ | ----------------- | --------------------------------------------------------- |
| **Argon2**     | Memory & Time | ✅✅ **Altissima**   | ✅ Sì              | Vincitore PHC. Configurabile in $t, m, p$.                |
| **scrypt**     | Memory-Hard   | ✅ Alta             | ✅ Sì              | Predecessore di Argon2, molto robusto ma meno flessibile. |
| **[[bcrypt]]** | CPU-bound     | ⚠️ Media           | ✅ Sì              | Standard storico (>25 anni). Non usa molta memoria.       |
| **PBKDF2**     | CPU Iterativo | ❌ Bassa            | ❌ No (Manuale)    | Veloce su GPU, obsoleto per password critiche.            |

## 6. Best Practices di Manutenzione

Poiché l'hardware degli attaccanti diventa più veloce ogni anno (Legge di Moore), i parametri di Argon2 non devono essere statici.

- **Tuning Dinamico:** La regola pratica suggerita è aumentare memoria e tempo affinché la verifica della password richieda un tempo percepibile ma accettabile per l'utente legittimo (es. circa **100 ms**).
    
- **Re-Hashing:** Se si decide di aumentare i parametri di sicurezza (es. passare da $m=64MB$ a $m=128MB$), il sistema deve ricalcolare l'hash (re-hashing) trasparentemente al prossimo login corretto dell'utente.