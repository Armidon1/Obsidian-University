# Existential Forgery (E)

È una classe specifica di [[Forgery]]. Ricordiamo che esistono [[Existential Forgery (E)]], [[Selective Forgery (S)]] ed [[Universal Forgery (U)]].
Questo è l'obiettivo **più debole** per un attaccante.

- **Definizione:** L'avversario riesce a creare _una qualsiasi_ coppia $(m, \sigma)$ valida, dove $\sigma$ non è stata prodotta dal mittente legittimo.
    
- **Caratteristiche:**
    
    - L'avversario **non ha alcun controllo** sul contenuto del messaggio $m$.
        
    - Il messaggio $m$ **non deve necessariamente avere un significato**; potrebbe essere una sequenza di byte casuali o senza senso (es. `a8$f!#_`).
        
- **Implicazione di Sicurezza:** Poiché questo è l'attacco più facile da realizzare, gli schemi crittografici più robusti sono quelli che prevengono questo livello minimo di attacco, definiti **"esistenzialmente non falsificabili"** (_existentially unforgeable_).
    

> Nota sull'attacco Esistenziale:
> 
> Una falsificazione esistenziale è considerata un successo anche se il messaggio falsificato è privo di senso. Il successo è definito dall'accettazione da parte del verificatore (il sistema convalida la firma), non dal valore semantico del messaggio. Il ricevente potrebbe interpretare i dati come cifrati, corrotti o semplicemente come una sequenza valida di numeri, compromettendo l'integrità del sistema.

### Gerarchia degli Attacchi e Obiettivo della Difesa

La gerarchia di potere degli attacchi è:

$$U \Rightarrow S \Rightarrow E$$

(L'attacco Universale implica il Selettivo, che implica l'Esistenziale)

Sfruttando la regola logica di base della **contrapposizione**, questa catena di implicazioni è logicamente equivalente a:

$$\neg E \Rightarrow \neg S \Rightarrow \neg U$$

(Non riuscire a compiere un attacco Esistenziale implica non riuscire a compiere un attacco Selettivo, che implica non riuscire a compiere un attacco Universale)

**Questo è il concetto fondamentale della difesa crittografica:** se possiamo progettare uno schema (come una firma digitale o un MAC) che sia sicuro contro la minaccia più deBole (l'attacco esistenziale, $\neg E$), allora abbiamo automaticamente protetto il sistema anche dalle minacce più forti (selettiva e universale).