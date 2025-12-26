Ecco una struttura completa per una nota **Obsidian**, ottimizzata con tag, LaTeX per le formule e callout per i concetti chiave, basata sulla nostra discussione.

---

# Protocollo Needham-Schroeder (NS)

**Tags:** #cybersecurity #authentication #protocols #TTP #symmetric_encryption #kerberos

## 1. Introduzione

Il protocollo **Needham-Schroeder** è un protocollo di autenticazione basato su un [[Trusted Third Party (TTP)]] e crittografia simmetrica. È il protocollo fondamentale che ha gettato le basi per lo sviluppo di **Kerberos**.

* **Obiettivo:** Stabilire una **Chiave di Sessione** () fresca tra due utenti (Alice e Bob) che non condividono un segreto, ma si fidano entrambi di un'autorità centrale (Carole/TTP).
* **Innovazione:** Introduce i **Nonce** () per garantire la freschezza dei messaggi e prevenire i [[Replay Attack]].

---

## Flusso del protocollo

Questo è il protocollo fondamentale che risolve i problemi precedenti introducendo i **Nonce** (numeri casuali usati una volta sola) per garantire la freschezza della sessione.

I Passaggi del Protocollo 1

1. Richiesta: Alice invia alla TTP la richiesta per Bob e un Nonce ($N_A$).
    
    $$A \rightarrow C: A, B, N_A$$
    
2. Generazione Chiavi e Ticket: La TTP (Carole/C) genera la session key $K$. Invia ad Alice un messaggio cifrato contenente $K$, il nonce originale (per provare che la risposta è fresca) e un "Ticket" cifrato per Bob.
    
    $$C \rightarrow A: K_{AC}(N_A, B, K, \underbrace{K_{BC}(K, A)}_{\text{Ticket per Bob}})$$
    
3. Inoltro del Ticket: Alice decifra il messaggio, verifica $N_A$, estrae $K$ e invia il Ticket a Bob.
    
    $$A \rightarrow B: K_{BC}(K, A)$$
    
4. Sfida di Bob: Bob decifra il Ticket, ottiene $K$ e conosce l'identità di Alice. Per verificare che Alice sia viva ora (e non sia un replay), Bob genera un nuovo Nonce $N_B$ cifrato con $K$.
    
    $$B \rightarrow A: K(N_B)$$
    
5. Risposta di Alice: Alice decifra $N_B$ (Autenticazione di Bob avvenuta con successo), lo decrementa (o modifica in modo predicibile) e lo rimanda cifrato.
    
    $$A \rightarrow B: K(N_B - 1)$$
    

> [!abstract] Concetto Chiave
> 
> Il Passaggio 5 prova a Bob che Alice possiede la chiave di sessione $K$ adesso (autenticazione di Alice avvenuta con successo). Nessun attaccante potrebbe generare $K(N_B-1)$ senza conoscere $K$.
> 
> Il motivo per cui si manda il nonce decrementato di uno, è perché ovviamente Trudy potrebbe semplicemente catturare il pacchetto $K(N_B)$ inviato da Bob e rinviarlo indietro ([[Reflection Attack]]) banalmente.

---

## 5. L'Attacco a Needham-Schroeder (Attacco Denning-Sacco)

Nonostante l'uso dei Nonce, il protocollo originale ha una vulnerabilità critica scoperta nel 1981, legata alla compromissione di una vecchia chiave di sessione.

Scenario dell'Attacco 2

Supponiamo che Trudy abbia registrato una vecchia sessione tra Alice e Bob e che, in qualche modo, sia riuscita a scoprire la vecchia chiave di sessione $K'$ (compromessa).

1. Replay del Ticket: Trudy attende che Alice non sia connessa e invia a Bob il vecchio Ticket registrato (Passaggio 3 del protocollo originale).
    
    $$T(A) \rightarrow B: K_{BC}(K', A)$$
    
2. **Inganno di Bob:** Bob decifra il ticket. Essendo cifrato con la sua chiave segreta $K_{BC}$ (che non è cambiata), lo ritiene valido. Pensa che Alice voglia parlargli usando la chiave $K'$.
    
3. Sfida: Bob invia la sfida con un nuovo Nonce $N'$, cifrata con $K'$ (che Trudy conosce!).
    
    $$B \rightarrow T: K'(N')$$
    
4. Risposta: Trudy può facilmente decifrare $N'$, calcolare $N'-1$ e ricifrarlo con $K'$.
    
    $$T \rightarrow B: K'(N'-1)$$
    

Risultato: Bob è convinto di parlare con Alice su un canale sicuro, ma sta parlando con Trudy.

Causa: Bob non ha modo di verificare la freschezza del Ticket generato dalla TTP. Non sa se il ticket è stato creato 1 secondo fa o 1 anno fa.

---

## 6. Needham-Schroeder Espanso (o Variante)

Per risolvere l'attacco di replay, bisogna garantire la freschezza anche verso Bob. Ci sono due approcci principali che hanno portato allo sviluppo di protocolli moderni come **[[Kerberos]]**.

Variante con Timestamp 3

Si introducono timestamp ($t$) nei messaggi cifrati dalla TTP.

$$C \rightarrow A: K_{AC}(..., t, ...), \ K_{BC}(..., t, ...)$$

Bob accetta il ticket solo se il timestamp è recente (richiede orologi sincronizzati).

Variante con Handshake Espanso 4

Bob deve contattare la TTP o inviare un nonce alla TTP prima di accettare la chiave.

1. Alice dice "Voglio parlarti".
    
2. Bob invia un Nonce $N_B$ ad Alice e alla TTP.
    
3. La TTP include $N_B$ nel ticket per Bob.
    
4. Quando Bob riceve il ticket e trova il suo $N_B$ all'interno, ha la prova matematica che il ticket è stato generato _dopo_ che lui ha inviato la richiesta.
    
![[Pasted image 20251223191001.png]]
> [!tip] Exam Focus
> 
> Il protocollo Needham-Schroeder è la base teorica di [[Kerberos]], il sistema di autenticazione standard in Windows e Active Directory. Kerberos usa pesantemente i Timestamp per evitare i problemi di replay senza dover fare troppi scambi di messaggi (handshake).


---

## 3. Analisi di Sicurezza

> [!abstract] Perché ?
> Il decremento del nonce nel passaggio 5 è fondamentale per prevenire il **Reflection Attack**. Prova a Bob che Alice ha effettivamente decifrato il messaggio (quindi possiede ) e non sta semplicemente riflettendo il pacchetto cifrato catturato.

### Punti di Forza

* **Autenticazione Mutua:** Entrambe le parti verificano l'identità dell'altro.
* **Indipendenza del TTP:** Dopo il passaggio 2, il TTP non è più necessario per la sessione corrente.

### Vulnerabilità (L'attacco di Denning-Sacco)

Se una vecchia chiave di sessione  viene compromessa, un attaccante (Trudy) può riutilizzare un vecchio ticket del passaggio 3:

1. Trudy invia a Bob  registrato in passato.
2. Bob non ha modo di sapere se quel ticket è "fresco" perché non c'è un timestamp o un suo nonce dentro il ticket.
3. Trudy può ora impersonare Alice usando la chiave rubata.

> [!failure] Correzione
> Per risolvere questo problema, Kerberos introduce i **Timestamp** per limitare la validità temporale dei ticket.

---

## 4. Confronto Tecnico

| Feature | Needham-Schroeder | Challenge-Response Semplice |
| --- | --- | --- |
| **Scalabilità** | Alta (via TTP) | Bassa (chiavi pre-condivise) |
| **Resistenza Replay** | Alta (per Alice) | Bassa |
| **Chiavi usate** | Session Key (Temporanea) | Master Key (Permanente) |

---
