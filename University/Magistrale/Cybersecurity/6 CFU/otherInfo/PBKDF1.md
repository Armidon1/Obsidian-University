
#### PBKDF1 (Obsoleto)

- **Definizione:** La prima versione dello standard [[PBKDF]]. Utilizzava una funzione di hash (come SHA-1) in modo iterativo.
    
- **Funzionamento:** Applicava ripetutamente l'hash alla concatenazione della password e del _salt_.
    
- **Limitazione Fatale:** La sua **lunghezza massima dell'output (chiave derivata) era limitata alla dimensione dell'output della funzione di hash sottostante**. Ad esempio, se usava SHA-1, non poteva produrre una chiave più lunga di 160 bit. Questo lo rende inadatto per molti algoritmi crittografici moderni che richiedono chiavi più lunghe (es. AES-256).
    