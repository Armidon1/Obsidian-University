Basandosi sulle fonti fornite ("Web Security - Part I") e sulla nostra cronologia di conversazione (che copriva "Web Security - Part II"), il concetto di **framing** può essere spiegato sia dal punto di vista strutturale che come vettore di attacco.

**1. Definizione Tecnica (dalla cronologia)** Il framing è la tecnica che permette di includere un documento HTML all'interno di un altro, tipicamente utilizzando il tag `<iframe>`. Come abbiamo discusso in precedenza riguardo al modello di sicurezza del browser:

- **Embedded Frame:** È la risorsa (pagina) che viene caricata all'interno.
- **Embedder Frame:** È la pagina "genitore" che ospita il frame.

**2. Il Framing come Vettore di Attacco (dalle nuove fonti)** Nelle slide della "Part I", il framing viene evidenziato principalmente nel contesto delle minacce e delle vulnerabilità:

- **Il "Gadget Attacker":** Le fonti descrivono una variante di attaccante web ("Web Attacker") chiamata _gadget attacker_. Questo attaccante sfrutta il framing inserendo un `iframe` con contenuto malevolo all'interno di una pagina web altrimenti onesta visitata dall'utente.
- **Clickjacking:** Il framing è alla base del _[[Clickjacking]]_, una vulnerabilità citata nelle fonti come conseguenza di una "superficie di attacco non ristretta" (Unrestricted attack surface). In questo attacco, un sito malevolo incorpora un sito vittima (framing) rendendolo spesso invisibile, per intercettare i click dell'utente. Le statistiche mostrano che il Clickjacking rappresentava circa il 4.2% dei pagamenti nel programma di bug bounty di Google nel 2018.

In sintesi, mentre strutturalmente il framing è un meccanismo di inclusione di contenuti, dal punto di vista della sicurezza (trattato nella Part I) è un meccanismo critico che può essere abusato per attacchi come il Clickjacking o l'iniezione di contenuti malevoli tramite iframe,.