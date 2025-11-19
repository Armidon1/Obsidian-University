![[Pasted image 20251117152018.png]]

Capisco. Hai ragione, il caso specifico di Moodle (identificato come **CVE-2018-1133**) è un esempio perfetto e molto interessante di questa vulnerabilità.

Come suggerito dal titolo nell'immagine che hai caricato, "Evil Teacher", l'attacco richiedeva che l'utente malintenzionato avesse un ruolo specifico, quello di "Insegnante", all'interno di un corso Moodle.

Ecco i dettagli tecnici di come funzionava.

---

### 1. Il Componente Vulnerabile: "Calculated Questions" (Domande Calcolate)

All'interno di Moodle, un insegnante può creare dei quiz. Uno dei tipi di domanda disponibili è la "Domanda Calcolata" (che nell'immagine vedi sotto "Math-Quiz / Question bank").

Questa funzione è pensata per creare domande di matematica dinamiche, ad esempio:

Quanto fa {x} + {y}?

L'insegnante definisce la formula per la risposta corretta (es. `{x} + {y}`). Quando uno studente svolge il quiz, Moodle sostituisce le variabili `{x}` e `{y}` con numeri casuali (es. 5 e 3) e poi **calcola** il risultato (8) per verificare la risposta.

### 2. La Funzione Pericolosa: `eval()`

Per "calcolare" la formula fornita dall'insegnante, il codice di Moodle (scritto in PHP) utilizzava una funzione chiamata **`eval()`**.

La funzione `eval()` è notoriamente una delle più pericolose in molti linguaggi di programmazione. Prende una stringa di testo e la esegue come se fosse codice.

- **Uso previsto (innocuo):** `eval("return 5 + 3;")` -> restituisce 8
    
- **Uso malevolo (pericoloso):** `eval("return 5 + 3; system('ls -la');")` -> restituisce 8 E INOLTRE esegue il comando `ls -la` sul server, elencando tutti i file.
    

### 3. Il Tentativo di Difesa (fallito)

Gli sviluppatori di Moodle sapevano che `eval()` era pericolosa. Per questo, prima di passare la formula a `eval()`, la filtravano attraverso una funzione di validazione (chiamata `qtype_calculated_find_formula_errors()`).

Questa funzione doveva controllare la formula dell'insegnante e bloccare qualsiasi cosa che non fosse una semplice espressione matematica (bloccando comandi come `system()`, `exec()`, ecc.). In pratica, funzionava come una **blacklist**.

### 4. L'Attacco: Il Bypass del Filtro

I ricercatori di sicurezza di Ripstech (l'azienda del blog post nella tua immagine) hanno scoperto che questa funzione di validazione poteva essere ingannata.

Il trucco (come menzionato nell'articolo) era **annidare le variabili** (i "wildcards" nell'immagine).

Semplificando molto, l'attacco funzionava così:

1. **Formula Normale:** `{x}`
    
    - Il validatore la controlla, dice "OK, è una variabile".
        
    - `eval()` la riceve e la elabora.
        
2. **Formula Malevola Semplice:** `system('ls')`
    
    - Il validatore la controlla, vede "system" e **la blocca**. L'attacco fallisce.
        
3. **Formula Malevola Annidata (Il Bypass):** `{x{y}}`
    
    - L'insegnante "malintenzionato" inseriva una formula che non era semplicemente `{x}` ma conteneva un comando malevolo nascosto in una variabile annidata, ad esempio: `{x}; system('id')`
        
    - Il validatore, nel tentativo di processare la formula, si confondeva. Analizzava prima la parte interna, ma non riusciva a "vedere" e bloccare correttamente il comando malevolo che veniva iniettato.
        
    - Di conseguenza, una stringa di testo contenente il comando `system('id')` (che mostra l'utente con cui è in esecuzione il server, es. `www-data`) veniva passata direttamente alla pericolosa funzione `eval()`.
        

A quel punto, l'attaccante aveva ottenuto la **Remote Code Execution (RCE)**. Poteva eseguire comandi arbitrari sul server che ospitava Moodle, con gli stessi permessi dell'applicazione web. Questo gli permetteva di leggere file sensibili, rubare dati degli studenti o persino prendere il pieno controllo del server.