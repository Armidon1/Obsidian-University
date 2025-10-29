# **Performance (Prendibilità / Prestazione)**  

> Capacità di un sistema di **elaborare operazioni o servizi in modo efficiente, con un tempo di risposta minimo e un consumo di risorse (CPU, memoria, banda) ottimale**.  
> **Definizione chiave:** il sistema deve svolgere le sue funzioni con un’efficienza tale da soddisfare i requisiti di velocità, throughput e uso delle risorse.

> **Esempio:**  
> - Un'applicazione web che gestisce 10.000 richieste al minuto senza degradare la latenza media oltre i 200 ms.  
> - Un sistema di elaborazione in tempo reale che processa dati sensori in meno di 50 ms.

> **Misurazioni tipiche:**  
> - Tempo di risposta (latency)  
> - Throughput (numero di operazioni per unità di tempo)  
> - Utilizzo delle risorse (CPU, RAM, banda)  

> **Minaccia tipica:**  
> - Sovraccarico del sistema (overload).  
> - Conflitti di sincronizzazione o bottlenecks in un nodo specifico.  
> - Attacchi che provocano il blocco di processi (es. DoS che aumenta la latenza).  

> **Relazione con altre proprietà:**  
> - È strettamente legata all’**availability** e alla **timeliness**: un sistema può essere disponibile ma inefficiente se i tempi di risposta sono troppo elevati.  
> - Influisce direttamente sulla **scalabilità** (se il sistema non può mantenere la prestazione al crescere del carico).  
> - È cruciale per l’esperienza utente e l’affidabilità percepita.

---

✅ **Importanza in contesti critici:**  
In applicazioni come servizi finanziari, sistemi di telemedicina o piattaforme di IoT, una bassa performance può causare frustrazione degli utenti, errori operativi o persino ritardi che compromettono la sicurezza (es. un sistema che non risponde in tempo per elaborare transazioni).

> 🔍 **Nota**: Il termine "performance" non è sempre incluso tra le proprietà classiche della *dependability* come availability, reliability e safety, ma diventa fondamentale in contesti operativi reali, specialmente nei sistemi distribuiti dove il carico varia dinamicamente.

---

Se desideri, posso integrare questa proprietà nel framework completo delle **proprietà fondamentali dei sistemi distribuiti affidabili**, o fornire un confronto tra *performance*, *scalabilità* e *tempo di risposta (timeliness)*.