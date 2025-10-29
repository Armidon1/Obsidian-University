# **Timeliness (Tempestività)**  
> Capacità di un sistema di **elaborare e restituire i dati o i servizi entro un certo intervallo temporale specificato**.  
> **Definizione chiave:** il sistema deve rispondere in tempo utile, garantendo che le operazioni siano completate prima della scadenza prevista (es. una richiesta di pagamento dev’essere elaborata entro 2 secondi).  

> **Esempio:**  
> - Un sistema di controllo di traffico che deve processare i segnali in tempo reale per evitare incidenti.  
> - Una piattaforma di chat in tempo reale dove ogni messaggio deve essere visualizzato entro 100 ms dall’invio.

> **Minaccia tipica:**  
> - Ritardi nella trasmissione o elaborazione (latenza).  
> - Errori di sincronizzazione temporale.  
> - Attacchi che causano blocco o sovraccarico, impedendo la risposta tempestiva.

> **Relazione con altre proprietà:**  
> - Legata strettamente all’**[[Availability]]** e alla **[[Performance]]**, poiché anche un sistema disponibile può essere inefficace se non risponde in tempo.  
> - Interessa particolarmente i sistemi in tempo reale (real-time systems) e quelli distribuiti con vincoli temporali.

---

Questa proprietà è fondamentale in ambienti dove il **tempo di risposta** determina la correttezza o l’efficacia del sistema, come nei controlli industriali, nelle applicazioni mediche o nei servizi finanziari.  
È spesso considerata una componente chiave della **dependability**, soprattutto in contesti critici.

---

