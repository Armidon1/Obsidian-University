# Rainbow Table

## 1. Definizione

Una **Rainbow Table** è una vasta tabella di dati precalcolati utilizzata per invertire funzioni di **[[Hashing]]** crittografiche (solitamente per recuperare password da un database rubato).

Rappresenta un classico esempio di **Time-Memory Tradeoff** (Compromesso Tempo-Memoria):

- Sacrifica **Memoria** (spazio su disco per salvare la tabella)...
    
- ...per guadagnare **Tempo** (craccare la password istantaneamente invece che calcolarla per ore).
    

## 2. Il Problema: Brute Force vs Lookup Table

Per capire la Rainbow Table, bisogna guardare agli estremi che cerca di bilanciare.

### Estremo A: Brute Force (Tempo)

L'attaccante prova ogni combinazione possibile (`aaaa`, `aaab`...) al momento dell'attacco.

- **Pro:** Richiede 0 spazio su disco.
    
- **Contro:** Richiede un tempo di calcolo enorme (CPU/GPU) per ogni singola password.
    

### Estremo B: [[Lookup Table (LUT)]] (Memoria)

L'attaccante pre-calcola _tutte_ le password possibili e salva le coppie `(Hash, Password)` in un file gigantesco.

- **Pro:** Il crack è istantaneo (basta un `SELECT` o una ricerca binaria).
    
- **Contro:** Impossibile per password lunghe. Una tabella con tutte le password alfanumeriche di 8 caratteri occuperebbe Petabyte o Exabyte di spazio.
    

### La Soluzione: Rainbow Table

La Rainbow Table è la via di mezzo intelligente.

Invece di salvare tutte le coppie, salva solo l'inizio e la fine di lunghe catene di hash, riducendo lo spazio occupato di migliaia di volte, mantenendo una velocità di cracking molto alta.

## 3. Come Funziona (La Catena)

Il cuore della Rainbow Table è la Funzione di Riduzione ($R$).

Questa funzione fa l'opposto dell'hash: prende un hash e lo trasforma in una stringa di testo valida (una "finta password").

**Il Ciclo della Catena:**

1. Si sceglie una **Password Iniziale** (Start Point).
    
2. Si calcola l'**Hash**.
    
3. Si applica la **Riduzione** all'hash per ottenere una nuova Password.
    
4. Si ripete il processo per migliaia di volte (es. 10.000 anelli).
    
5. Si salva su disco solo: **(Start Point, End Point)**.
    

$$\text{Start} \xrightarrow{H} h_1 \xrightarrow{R} p_1 \xrightarrow{H} h_2 \xrightarrow{R} p_2 \dots \xrightarrow{H} \text{End Point}$$

> [!abstract] La Magia della Compressione
> 
> Una catena può contenere 10.000 password intermedie, ma sul disco occupiamo spazio solo per 2 (Inizio e Fine). Abbiamo compresso lo spazio di un fattore 5.000!

## 4. L'Attacco (Lookup)

Quando l'attaccante ha un hash $H_{rubato}$ da craccare:

1. Applica la funzione di riduzione ($R$) a $H_{rubato}$, poi l'hash ($H$), poi $R$, poi $H$... creando una catena temporanea.
    
2. Controlla se uno dei risultati appare nella colonna **End Point** della sua tabella.
    
3. Se trova una corrispondenza, va a vedere lo **Start Point** corrispondente.
    
4. Rigenera quella specifica catena dall'inizio.
    
5. L'hash che precede $H_{rubato}$ nella catena corrisponde alla password in chiaro cercata.
    

## 5. Perché "Rainbow" (Arcobaleno)?

Il problema delle catene è la Collisione: se due catene diverse "sbattono" contro lo stesso hash intermedio, si fondono e diventano inutili (spreco di spazio).

Per evitare questo, si usano diverse funzioni di riduzione ($R_1, R_2, R_3 \dots$) in sequenza. Ogni funzione è considerata un "colore" diverso. Questo riduce drasticamente le collisioni e aumenta la copertura della tabella.

## 6. La Difesa Definitiva: Il Salt

Le Rainbow Tables hanno un tallone d'Achille fatale: sono statiche.

Una tabella è calcolata per un algoritmo specifico (es. MD5) e per password "nude".

L'uso del **[[Salt (Cryptographic)|Salt]]** distrugge completamente l'efficacia delle Rainbow Tables.

- Se la password è `Hash(Password + Salt)`, la tabella precalcolata per `Hash(Password)` è inutile.
    
- L'attaccante dovrebbe generare una _nuova_ Rainbow Table per _ogni singolo_ salt diverso presente nel database.
    
- Poiché generare una tabella richiede mesi o anni di calcolo, l'attacco diventa impraticabile.
    

> [!tip] Exam Focus
> 
> Se ti chiedono: "Come ci si difende dalle Rainbow Tables?"
> 
> La risposta è una sola: Usando il Salt. (E preferibilmente algoritmi lenti come Bcrypt o Argon2).

---

**Vedi anche:**

- [[Hashing]]
    
- [[Salt (Cryptographic)]]
    
- [[Pepper (Cryptography)]]
    
- [[Brute-force attack]]