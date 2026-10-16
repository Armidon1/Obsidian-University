# CRUD

**CRUD** è l’acronimo delle quattro operazioni fondamentali per gestire i dati persistenti in un database:

|Operazione|Significato|Database relazionale|Graph database|
|---|---|---|---|
|**Create**|Inserire nuovi dati|Inserire righe con `INSERT`|Creare nodi e archi|
|**Read**|Leggere e interrogare dati|Recuperare righe con `SELECT`, eventualmente usando JOIN|Cercare nodi, leggere proprietà e attraversare relazioni|
|**Update**|Modificare dati esistenti|Modificare valori con `UPDATE`|Modificare proprietà o etichette di nodi e archi|
|**Delete**|Eliminare dati|Eliminare righe con `DELETE`|Eliminare archi e nodi|

> [!example] Esempio: gestione di una persona
> 
> - **Create**: inserire Alice nel database.
>     
> - **Read**: recuperare le informazioni di Alice.
>     
> - **Update**: modificare la sua età.
>     
> - **Delete**: eliminare Alice dal database.
>     

## Perché è importante

CRUD descrive il **ciclo di vita dei dati**: un’applicazione deve poterli inserire, consultare, aggiornare ed eliminare. È quindi un insieme di funzionalità di base, indipendente dal modello utilizzato per rappresentarli.

Nei **database relazionali** si opera principalmente su righe organizzate in tabelle; nei **graph database** si opera su nodi, archi e proprietà. Le operazioni hanno lo stesso scopo generale, ma cambiano la rappresentazione dei dati e i meccanismi con cui vengono eseguite.

> [!important] CRUD non basta a garantire la correttezza  
> Il DBMS deve anche gestire aspetti come autorizzazioni, vincoli di integrità e transazioni. Per esempio, eliminare una persona può richiedere di gestire le righe che la referenziano tramite chiavi esterne, oppure gli archi collegati al suo nodo.

## Collegamento alla definizione di graph database

Secondo la **definizione funzionale**, un sistema è un graph database se espone un modello a grafo e permette di eseguire operazioni CRUD su di esso, indipendentemente dallo storage sottostante.

Il supporto CRUD, da solo, **non implica storage nativo o index-free adjacency**: descrive le operazioni disponibili, non la loro implementazione fisica.

## Collegamento con [[ACID]]

Le operazioni **CRUD** descrivono **che cosa possiamo fare sui dati**; le proprietà **ACID** descrivono le garanzie offerte quando queste operazioni vengono eseguite all’interno di una transazione.

Una **transazione** può raggruppare più operazioni CRUD in un’unica unità di lavoro.

|Proprietà|Garanzia|
|---|---|
|**Atomicity — Atomicità**|Le modifiche della transazione vengono applicate tutte oppure nessuna.|
|**Consistency — Consistenza**|La transazione preserva i vincoli di integrità definiti nel database.|
|**Isolation — Isolamento**|L’interferenza tra transazioni concorrenti viene controllata secondo il livello di isolamento adottato.|
|**Durability — Durabilità**|Dopo il commit, le modifiche persistono anche in caso di guasto, secondo le garanzie del sistema.|

> [!example] Trasferimento di denaro  
> Un trasferimento richiede di leggere i saldi e aggiornare due conti: sottrarre denaro dal primo e aggiungerlo al secondo. Sono operazioni CRUD, ma devono appartenere alla stessa transazione: l’atomicità impedisce che venga registrato soltanto uno dei due aggiornamenti.

Le transazioni ACID possono essere supportate sia dai **database relazionali** sia dai **graph database**. Nel secondo caso, una transazione potrebbe creare due nodi e un arco che li collega, garantendo che tutte queste modifiche vengano confermate insieme oppure annullate.

> [!important] CRUD e ACID sono concetti distinti  
> Supportare CRUD non implica automaticamente offrire garanzie ACID. Inoltre, essere un database NoSQL o a grafo non significa rinunciare alle transazioni ACID: il supporto dipende dal DBMS.