# 3. Universal Forgery (U) - Falsificazione Universale
È una classe specifica di [[Forgery]]. Ricordiamo che esistono [[Existential Forgery (E)]], [[Selective Forgery (S)]] ed [[Universal Forgery (U)]].
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