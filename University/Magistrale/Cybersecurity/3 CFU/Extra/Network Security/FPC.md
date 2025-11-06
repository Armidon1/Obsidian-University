# Cattura Completa dei Pacchetti (FPC)

FPC significa catturare e archiviare l'**intero pacchetto**, incluso il **payload** (il contenuto) dei dati.

**Vantaggi:**

- È lo strumento definitivo per la **digital forensics** (informatica forense).
    
- Permette agli analisti di **ricostruire letteralmente l'attacco** passo dopo passo, analizzare i payload del malware o estrarre chiavi di crittografia.
    

**Limitazioni (Perché non è usato ovunque):**

- **Requisiti di archiviazione enormi:** Archiviare tutti i payload di un'azienda è estremamente costoso.
    
- **Overhead prestazionale:** Richiede hardware specializzato ad alta velocità per catturare il traffico al "line rate" (velocità massima della linea) senza perdere pacchetti.
    
- L'FPC è tipicamente implementato **selettivamente** (es. catturando solo i pacchetti che attivano un allarme) o su segmenti di rete ad altissimo valore e basso volume.
    
