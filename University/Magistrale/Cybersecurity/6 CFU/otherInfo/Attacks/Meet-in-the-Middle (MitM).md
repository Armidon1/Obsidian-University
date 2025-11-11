# ⛓️ Meet-in-the-Middle (MitM) Attack

>[!Definizione]
>Il **Meet-in-the-Middle (MitM) Attack** è un tipo di **attacco crittanalitico** (specificamente, un attacco _brute-force_ ottimizzato) che mira a sistemi crittografici che utilizzano **cifrature multiple sequenziali** con chiavi indipendenti (come Double DES).

L'attacco è un classico _trade-off_ **tempo-memoria**: riduce drasticamente il tempo di calcolo necessario per trovare le chiavi, al costo di richiedere un'enorme quantità di memoria (spazio) per archiviare i risultati intermedi.

L'idea fondamentale è attaccare il sistema da entrambe le direzioni (cifrando il plaintext e decifrando il ciphertext) e cercare una "collisione" nel valore intermedio.

### Meccanismo dell'Attacco (Esempio: Double DES)

Questo attacco richiede che l'attaccante possieda almeno una coppia di **testo in chiaro e testo cifrato noto** ($P$ e $C$).

Consideriamo **Double DES (2DES)**, che non viene utilizzato proprio a causa di questo attacco:

- La cifratura della vittima è: $C = E_{K_2}(E_{K_1}(P))$
    
- Le chiavi $K_1$ e $K_2$ sono indipendenti (es. 56 bit ciascuna).
    
- Un attacco _brute-force_ ingenuo richiederebbe $2^{56} \times 2^{56} = 2^{112}$ tentativi.
    

L'attacco MitM riduce questa complessità a $2^{57}$:

1. **Fase 1: Forward (dall'inizio)**
    
    - L'attaccante prende il plaintext $P$.
        
    - Cifra $P$ con **ogni possibile chiave $K_1$** (2^56 tentativi).
        
    - Memorizza tutti i risultati intermedi ($M = E_{K_1}(P)$) in un'enorme _lookup table_ (es. hash table), mappando $M \rightarrow K_1$.
        
2. **Fase 2: Backward (dalla fine)**
    
    - L'attaccante prende il ciphertext $C$.
        
    - Decifra $C$ con **ogni possibile chiave $K_2$** (2^56 tentativi).
        
    - Per ogni risultato intermedio $M' = D_{K_2}(C)$, controlla se $M'$ esiste nella _lookup table_ creata nella Fase 1.
        
3. **Fase 3: Collisione (Il "Meet in the Middle")**
    
    - Se $M = M'$, significa che $E_{K_1}(P) = D_{K_2}(C)$.
        
    - L'attaccante ha trovato una coppia di chiavi candidate $(K_1, K_2)$ che _potrebbe_ essere quella corretta.
        

### Dettagli Tecnici e Implicazioni per Ingegneri

|**Caratteristica**|**Descrizione Tecnica**|
|---|---|
|**Complessità Computazionale**|Per 2DES, la complessità temporale non è $O(2^{k \cdot 2})$ (cioè $2^{112}$), ma $O(2^k + 2^k) = O(2^{k+1})$.<br><br>  <br><br>(es. $2^{56} + 2^{56} = 2 \times 2^{56} = 2^{57}$). Questo è un **guadagno esponenziale** che rende l'attacco fattibile.|
|**Complessità di Spazio (Memoria)**|Questo è il vero costo. L'attacco richiede $O(2^k)$ di memoria per archiviare la _lookup table_ della Fase 1. Per 2DES, $2^{56}$ voci sono un ostacolo enorme ma non teoricamente impossibile.|
|**Requisiti**|**Testo in chiaro noto** ($P, C$). Per eliminare i "falsi positivi" (coppie di chiavi che funzionano per caso solo su una coppia $P, C$), l'attaccante ha bisogno di una **seconda coppia** $(P', C')$ per validare le chiavi candidate trovate.|
|**Difesa (Contromisura)**|La difesa è **rompere la struttura** che permette l'attacco. È per questo che è stato inventato **Triple DES (3DES)**:<br><br>  <br><br>• Usa 3 chiavi in modalità **Encrypt-Decrypt-Encrypt (EDE)**: $C = E_{K_3}(D_{K_2}(E_{K_1}(P)))$.<br><br>  <br><br>• La fase di _Decrypt_ nel mezzo impedisce il semplice attacco MitM, costringendo l'attaccante a una complessità di $O(2^{2k})$ (circa $2^{112}$ per 3DES a 2 chiavi).|
# Man-in-the-Middle (MITM) vs Meet-in-the-Middle (MITM)
Sebbene i nomi siano molto simili (entrambi abbreviati in "MITM"), **Meet-in-the-Middle** e **[[Man-in-the-Middle (MITM)]]** sono due tipi di attacchi completamente diversi, che operano in contesti differenti.

La differenza fondamentale è:

- **Man-in-the-Middle (Uomo nel Mezzo):** È un attacco alla **sicurezza di rete**.1 Un aggressore si interpone _fisicamente_ o _logicamente_ nella comunicazione tra due parti.2
    
- **Meet-in-the-Middle (Incontro a Metà Strada):** È un attacco di **crittanalisi**.3 È una tecnica matematica usata per _rompere_ un algoritmo crittografico (come una cifratura a blocchi).
    

---

### 🕵️ Man-in-the-Middle (MITM)

Questo è un attacco **attivo** alla comunicazione.4 L'aggressore si posiziona segretamente tra due parti che credono di comunicare direttamente tra loro (ad esempio, tu e il sito della tua banca).5

- **Come funziona:**
    
    1. **Intercettazione:** L'aggressore intercetta il traffico tra la vittima (A) e il destinatario legittimo (B).6 Questo può avvenire in molti modi, come creare una rete Wi-Fi falsa ("evil twin"), usare DNS spoofing (dirottarti su un sito falso) o ARP poisoning.7
        
    2. **Impersonificazione:** L'aggressore impersona B agli occhi di A, e impersona A agli occhi di B.
        
    3. **Manipolazione:** Una volta "nel mezzo", l'aggressore può:
        
        - **Origliare:** Leggere tutte le comunicazioni (password, numeri di carte di credito, ecc.).8
            
        - **Modificare:** Alterare i messaggi scambiati (es. cambiare l'IBAN in una richiesta di bonifico).9
            
        - **Iniettare contenuti:** Inserire codice malevolo nelle pagine web che visiti.
            
- **Obiettivo:** Rubare dati sensibili, credenziali, denaro, o spiare la comunicazione.10
    
- **Contesto:** Sicurezza di rete, comunicazioni online.11
    

---

### 🧩 Meet-in-the-Middle (MITM)

Questo è un attacco **analitico** alla crittografia. Non intercetta la comunicazione in tempo reale, ma cerca di scoprire la chiave segreta usata per cifrare un messaggio.

- Come funziona:
    
    Si applica a sistemi di crittografia che usano chiavi multiple in sequenza, come il vecchio standard Double DES (che applicava la crittografia DES due volte con due chiavi diverse, K1 e K2).12
    
    L'idea ingenua per rompere Double DES sarebbe provare tutte le combinazioni possibili di K1 e K2 (un attacco brute-force).13
    
    L'attacco Meet-in-the-Middle è molto più furbo:
    
    1. **Fase 1 (Andata):** L'aggressore prende il messaggio in chiaro (P) e lo cifra con _ogni possibile_ chiave K1.14 Salva tutti i risultati intermedi (M) in una tabella.
        
    2. **Fase 2 (Ritorno):** L'aggressore prende il messaggio cifrato (C) e lo decifra con _ogni possibile_ chiave K2.15
        
    3. **Incontro:** Per ogni risultato della Fase 2, controlla se è presente nella tabella creata nella Fase 1.
        
    4. **Verifica:** Se trova una corrispondenza (un valore "in mezzo" M), la coppia di chiavi (K1, K2) trovata è molto probabilmente quella giusta.
        
- **Obiettivo:** Scoprire le chiavi segrete di un algoritmo crittografico, rendendolo insicuro.
    
- **Contesto:** Crittanalisi, design di algoritmi crittografici (è il motivo per cui Double DES è insicuro e si è passati a Triple DES).
    

---

### Riepilogo della Differenza

|**Caratteristica**|**👨‍💻 Man-in-the-Middle**|**🔑 Meet-in-the-Middle**|
|---|---|---|
|**Dominio**|Sicurezza di Rete|Crittanalisi (Matematica)|
|**Tipo**|Attacco attivo di intercettazione|Attacco analitico (offline)|
|**Obiettivo**|Rubare dati, spiare, modificare la comunicazione|Scoprire la chiave di cifratura|
|**Bersaglio**|La **comunicazione** tra due parti|L'**algoritmo** crittografico stesso|
|**Esempio**|Un hacker su una Wi-Fi pubblica che legge le tue password.|Un matematico che trova un modo per rompere Double DES.|