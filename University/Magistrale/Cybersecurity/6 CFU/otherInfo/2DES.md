# Cifratura doppia con due chiavi (2DES)

Si potrebbe pensare di aumentare la sicurezza del [[DES]] semplicemente cifrando due volte, ma utilizzando due chiavi diverse e indipendenti, $K_1$ e $K_2$.

Processo di Cifratura 2DES:

$\text{Testo in chiaro} \xrightarrow{E \text{ con } K_1} \text{Intermedio} \xrightarrow{E \text{ con } K_2} \text{Testo cifrato}$

La domanda ovvia è: questo schema è crittograficamente forte come un cifrario con una chiave a 112 bit (56 + 56)?

La risposta è no. Sebbene un attacco di forza bruta diretto richiederebbe di indovinare entrambe le chiavi ($2^{112}$ tentativi), esiste un attacco più efficiente che vanifica questo vantaggio.

### L'attacco "Meet-in-the-Middle" (MITM)

Questo schema è vulnerabile a un attacco noto come **[[Meet-in-the-Middle (MitM)]]** (MITM). Questo attacco riduce il tempo necessario per rompere 2DES a circa il doppio del tempo necessario per rompere il DES singolo (circa $2^{57}$ operazioni invece di $2^{112}$).

Tuttavia, l'attacco MITM ha un costo: richiede una quantità di memoria "alquanto irragionevole".

Come funziona l'attacco MITM:

Supponiamo che l'attaccante disponga di alcune coppie di testo in chiaro e testo cifrato noti (ad esempio $\langle m_1, c_1 \rangle$, $\langle m_2, c_2 \rangle$, ecc.).

1. **Tabella A (Cifratura):** L'attaccante crea la Tabella A. Cifra il testo in chiaro $m_1$ con _ogni_ possibile chiave $K$ (tutte $2^{56}$ chiavi). Salva ogni risultato $r_K$ e la chiave $K$ che lo ha prodotto: $\langle K_A, r_K \rangle$. Questa tabella viene poi ordinata in base ai risultati $r_K$.
    
2. **Tabella B (Decifratura):** L'attaccante crea la Tabella B. Decifra il testo cifrato $c_1$ con _ogni_ possibile chiave $K$ (tutte $2^{56}$ chiavi). Salva ogni risultato $s_K$ e la chiave $K$ che lo ha prodotto: $\langle K_B, s_K \rangle$. Anche questa tabella viene ordinata, in base ai risultati $s_K$.
    

**Trovare le Corrispondenze:** L'attaccante cerca una corrispondenza $t$ (un valore intermedio) che appaia in entrambe le tabelle.

- Se $r_K = s_K = t$, significa che l'attaccante ha trovato una $K_A$ che mappa $m_1 \rightarrow t$ e una $K_B$ che mappa $t \rightarrow c_1$.
    
- Questa coppia $\langle K_A, K_B \rangle$ è una coppia di chiavi candidata per $\langle K_1, K_2 \rangle$.
    

**Verifica dei Falsi Positivi:** Questo processo troverà quasi certamente molteplici corrispondenze (circa $2^{48}$ "impostori" secondo il documento). Per trovare la coppia di chiavi corretta, l'attaccante testa semplicemente ogni coppia candidata $\langle K_A, K_B \rangle$ sulla seconda coppia di test $\langle m_2, c_2 \rangle$. La probabilità che una coppia di chiavi errata funzioni anche per la seconda coppia di test è estremamente bassa (circa $1 \text{ su } 2^{64}$).

A causa di questa vulnerabilità teorica all'attacco [[Meet-in-the-Middle (MitM)]] (che scambia un problema di tempo $2^{112}$ con un problema di tempo $2^{57}$ e memoria $2^{56}$), la doppia cifratura 2DES non è generalmente considerata sufficientemente sicura e non viene utilizzata. Questo è il motivo per cui è stato scelto il [[3DES]] (tripla cifratura).