Certamente. Ecco una sintesi delle principali vulnerabilità trattate nelle slide "4 - Web Security (part I)", organizzata con definizioni brevi e citazioni alle fonti.

### 1. Vulnerabilità di Accesso ai File

- **Path Traversal (o Directory Traversal):** Una vulnerabilità che si verifica quando un'applicazione web utilizza input non controllati dell'utente per costruire percorsi di file. Questo permette a un attaccante di "risalire" la gerarchia delle directory (usando sequenze come `../`) ed uscire dalla _webroot_ per accedere a file sensibili del sistema operativo (es. `/etc/passwd`) o file di configurazione,.

### 2. Injection Attacks (Iniezioni di Codice)

- **Command Injection:** Si verifica quando l'input dell'utente viene passato senza validazione a funzioni che eseguono comandi di sistema (come `system` in PHP). L'attaccante può aggiungere caratteri speciali (come `;` o `&&`) per eseguire comandi arbitrari sul server con i privilegi dell'applicazione web,,.
- **Code Injection:** Simile alla precedente, ma l'input viene passato a funzioni che valutano dinamicamente una stringa come codice del linguaggio di programmazione stesso (es. `eval` in PHP). Questo permette all'attaccante di eseguire codice arbitrario all'interno dell'interprete dell'applicazione,.

### 3. SQL Injection (SQLi)

- **SQL Injection (Classica):** Una vulnerabilità di validazione dell'input dove dati non fidati vengono concatenati direttamente in una query SQL. L'attaccante può alterare la logica della query per accedere a dati non autorizzati, modificare l'integrità del database o, in alcuni casi, cancellare tabelle,.
    - _Esempio:_ Bypassare il login manipolando la query con `' OR 1=1 --`,.
    - _Stacked Queries:_ L'attaccante aggiunge intere nuove query separate da `;` (es. per fare `DROP TABLE`) se il database lo supporta.
- **Second-Order SQL Injection:** L'attacco avviene in due fasi: il payload malevolo viene prima salvato legittimamente nel database (fase 1). Successivamente, viene letto dal database e utilizzato in una query non sicura (fase 2), attivando l'attacco. È insidiosa perché i dati provenienti dal database sono spesso considerati "fidati".
- **Blind SQL Injection:** Si verifica quando l'applicazione è vulnerabile ma non mostra direttamente i risultati della query o gli errori. L'attaccante deduce le informazioni (es. password) osservando il comportamento del server:
    - _Conditional behavior:_ La risposta cambia (es. mostra o meno un elemento) in base a una condizione Vero/Falso iniettata.
    - _Conditional error:_ Si forza un errore SQL (es. divisione per zero) per testare una condizione.
    - _Time delay:_ Si inietta un comando che fa attendere il database (es. `WAITFOR DELAY`) se una condizione è vera, misurando il tempo di risposta,.

### 4. Server-Side Request Forgery (SSRF)

- **Definizione:** Una vulnerabilità che permette a un attaccante di indurre il server a effettuare richieste HTTP verso destinazioni inattese. Poiché la richiesta parte dal server stesso (che spesso gode di fiducia nella rete interna), l'attaccante può bypassare firewall per scansionare la rete locale, accedere a servizi interni non autenticati o leggere metadati sensibili (es. metadati cloud AWS),.
- **Blind SSRF:** Simile alla Blind SQLi, il server esegue la richiesta ma non restituisce il contenuto all'utente. L'attaccante può comunque inferire informazioni misurando i tempi di risposta o innescando azioni nella rete interna.