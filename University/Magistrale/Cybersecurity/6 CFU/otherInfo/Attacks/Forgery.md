# 🛡️ Cos'è la Forgery (Falsificazione)

Nel contesto della crittografia (in particolare per firme digitali e [[MAC]]), la **Forgery** (falsificazione) è un attacco in cui un avversario riesce a **creare una coppia messaggio/firma $(m, \sigma)$ valida**, tale che la firma $\sigma$ _non_ sia stata prodotta dal mittente legittimo (l'autore autorizzato).

L'obiettivo dell'attaccante è far sì che il ricevente accetti come autentico un messaggio che in realtà non lo è.

### Tipi di Forgery e Livelli di Minaccia

Esistono tre tipi principali di falsificazione, classificati in base al potere dell'avversario, dal più debole al più forte.

#### 1. Existential Forgery (E) - Falsificazione Esistenziale
[[Existential Forgery (E)]]
Questo è l'obiettivo **più debole** per un attaccante.

- **Definizione:** L'avversario riesce a creare _una qualsiasi_ coppia $(m, \sigma)$ valida, dove $\sigma$ non è stata prodotta dal mittente legittimo.
    
- **Caratteristiche:**
    
    - L'avversario **non ha alcun controllo** sul contenuto del messaggio $m$.
        
    - Il messaggio $m$ **non deve necessariamente avere un significato**; potrebbe essere una sequenza di byte casuali o senza senso (es. `a8$f!#_`).
        
- **Implicazione di Sicurezza:** Poiché questo è l'attacco più facile da realizzare, gli schemi crittografici più robusti sono quelli che prevengono questo livello minimo di attacco, definiti **"esistenzialmente non falsificabili"** (_existentially unforgeable_).
    

> Nota sull'attacco Esistenziale:
> 
> Una falsificazione esistenziale è considerata un successo anche se il messaggio falsificato è privo di senso. Il successo è definito dall'accettazione da parte del verificatore (il sistema convalida la firma), non dal valore semantico del messaggio. Il ricevente potrebbe interpretare i dati come cifrati, corrotti o semplicemente come una sequenza valida di numeri, compromettendo l'integrità del sistema.

#### 2. Selective Forgery (S) - Falsificazione Selettiva
[[Selective Forgery (S)]]
Questo è un attacco di livello intermedio.

- **Definizione:** L'avversario crea una coppia $(m, \sigma)$ valida, dove il messaggio $m$ è stato **scelto dall'avversario _prima_ dell'inizio dell'attacco**.
    
- **Caratteristiche:**
    
    - A differenza della falsificazione esistenziale, qui l'attaccante ha il pieno controllo sul messaggio $m$.
        
    - $m$ può essere scelto appositamente per avere proprietà matematiche interessanti che potrebbero facilitare l'attacco all'algoritmo di firma.
        
- **Relazione:** La capacità di condurre un attacco di falsificazione selettiva implica la capacità di condurne uno esistenziale.
    
    - $S \Rightarrow E$
        

#### 3. Universal Forgery (U) - Falsificazione Universale
[[Universal Forgery (U)]]
Questo è l'obiettivo **più forte** per un attaccante, equivalente a una rottura totale del sistema.

- **Definizione:** L'avversario è in grado di creare una firma (o tag) valida $\sigma$ per **qualsiasi messaggio $m$ dato**.
    
- **Caratteristiche:**
    
    - L'attaccante può, di fatto, sostituirsi completamente al mittente legittimo e firmare qualsiasi cosa.
        
- **Relazione:** È la minaccia più potente e implica la capacità di compiere anche gli altri due tipi di attacco.
    
    - $U \Rightarrow S \Rightarrow E$
        

### Gerarchia degli Attacchi e Obiettivo della Difesa

La gerarchia di potere degli attacchi è:

$$U \Rightarrow S \Rightarrow E$$

(L'attacco Universale implica il Selettivo, che implica l'Esistenziale)

Sfruttando la regola logica di base della **contrapposizione**, questa catena di implicazioni è logicamente equivalente a:

$$\neg E \Rightarrow \neg S \Rightarrow \neg U$$

(Non riuscire a compiere un attacco Esistenziale implica non riuscire a compiere un attacco Selettivo, che implica non riuscire a compiere un attacco Universale)

**Questo è il concetto fondamentale della difesa crittografica:** se possiamo progettare uno schema (come una firma digitale o un MAC) che sia sicuro contro la minaccia più deBole (l'attacco esistenziale, $\neg E$), allora abbiamo automaticamente protetto il sistema anche dalle minacce più forti (selettiva e universale).