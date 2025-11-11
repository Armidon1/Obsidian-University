# Selective Forgery (S) - Falsificazione Selettiva
È una classe specifica di [[Forgery]]. Ricordiamo che esistono [[Existential Forgery (E)]], [[Selective Forgery (S)]] ed [[Universal Forgery (U)]]
Questo è un attacco di livello intermedio.

- **Definizione:** L'avversario crea una coppia $(m, \sigma)$ valida, dove il messaggio $m$ è stato **scelto dall'avversario _prima_ dell'inizio dell'attacco**.
    
- **Caratteristiche:**
    
    - A differenza della falsificazione esistenziale, qui l'attaccante ha il pieno controllo sul messaggio $m$.
        
    - $m$ può essere scelto appositamente per avere proprietà matematiche interessanti che potrebbero facilitare l'attacco all'algoritmo di firma.
        
- **Relazione:** La capacità di condurre un attacco di falsificazione selettiva implica la capacità di condurne uno esistenziale.
    
    - $S \Rightarrow E$
        

### Gerarchia degli Attacchi e Obiettivo della Difesa

La gerarchia di potere degli attacchi è:

$$U \Rightarrow S \Rightarrow E$$

(L'attacco Universale implica il Selettivo, che implica l'Esistenziale)

Sfruttando la regola logica di base della **contrapposizione**, questa catena di implicazioni è logicamente equivalente a:

$$\neg E \Rightarrow \neg S \Rightarrow \neg U$$

(Non riuscire a compiere un attacco Esistenziale implica non riuscire a compiere un attacco Selettivo, che implica non riuscire a compiere un attacco Universale)

**Questo è il concetto fondamentale della difesa crittografica:** se possiamo progettare uno schema (come una firma digitale o un MAC) che sia sicuro contro la minaccia più deBole (l'attacco esistenziale, $\neg E$), allora abbiamo automaticamente protetto il sistema anche dalle minacce più forti (selettiva e universale).