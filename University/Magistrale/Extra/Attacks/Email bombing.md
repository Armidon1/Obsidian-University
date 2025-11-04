# 💣 Email Bombing

### Definizione

L'**Email Bombing** è una forma di **attacco Denial of Service ([[DoS]])** che consiste nell'invio di un **volume enorme di messaggi di posta elettronica** a uno o più indirizzi specifici in un breve lasso di tempo. L'obiettivo dell'attacco è **sovraccaricare** il server di posta del destinatario, la casella di posta stessa o l'intera infrastruttura di rete, rendendo illeggibile la posta legittima e impedendo l'uso normale del servizio.

Il bombing di e-mail può essere utilizzato per scopi malevoli diretti, o come tattica diversiva (_distraction attack_) per nascondere attività più gravi (come intrusioni o esfiltrazione di dati).

### Tipologie Tecniche di Email Bombing

L'Email Bombing si manifesta principalmente in tre modi:

#### 1. Bombing Semplice (Mass Mail)

- **Tecnica:** L'aggressore utilizza un singolo account o un piccolo gruppo di account per inviare migliaia di e-mail identiche o leggermente variate a uno o pochi indirizzi di destinazione.
    
- **Implicazione Tecnica:** Sfrutta la **capacità di elaborazione del server** e la **quota di spazio** (storage quota) della casella di posta della vittima. Se l'aggressore ha accesso a un _botnet_ o a un _relay_ SMTP compromesso, può inviare volumi sproporzionati di traffico.
    

#### 2. List Linking / Subscription Bombing

- **Tecnica:** L'aggressore iscrive l'indirizzo e-mail della vittima a **centinaia o migliaia di newsletter, forum o servizi online** che richiedono una conferma di iscrizione via e-mail.
    
- **Implicazione Tecnica:** In questo caso, l'attaccante non invia direttamente le e-mail malevole, ma sfrutta i **server legittimi di terze parti** (che inviano i messaggi di conferma o benvenuto) per inondare la casella di posta della vittima. Questo è spesso più difficile da filtrare perché i messaggi provengono da _domini_ con buona reputazione.
    

#### 3. Bombing con Allegati Pesanti (Zip/Attachment Bombing)

- **Tecnica:** L'aggressore invia e-mail con **allegati di grandi dimensioni** (es. file video, immagini) o file compressi (ZIP, RAR) che contengono molte copie di file grandi.
    
- **Implicazione Tecnica:** L'obiettivo non è solo saturare la casella di posta, ma anche **esaurire le risorse di rete e di elaborazione** del server di posta (MTA) e del client (MUA) che devono processare o tentare di scaricare i file di grandi dimensioni. Un allegato compresso può essere progettato per espandersi a una dimensione enorme (es. **Zip Bomb**) causando un _crash_ del software antivirus o del client di posta.
    

### Dettagli Tecnici e Implicazioni di Cybersecurity

|**Aspetto**|**Impatto Tecnico**|**Misure di Mitigazione**|
|---|---|---|
|**Server di Posta (MTA) Overload**|Consumo eccessivo di CPU, RAM e spazio su disco, causando **latenza** o **fallimento** nella consegna di posta legittima.|Implementare **limitazioni di _rate_ (rate limiting)** basate su indirizzo IP mittente, dominio o numero di destinatari unici nell'unità di tempo.|
|**Difesa E-mail**|Un attacco di Email Bombing può essere usato per distrarre la vittima o il team di sicurezza mentre un'altra minaccia (es. una **violazione** o un **trasferimento di fondi fraudolento**) è in corso.|Utilizzare **filtri antispam** e **Gateway di Sicurezza E-mail (SEG)** che analizzano il volume e l'anomalia del traffico e-mail, e che possono applicare **greylisting** o liste nere dinamiche.|
|**Difesa Subscription Bombing**|Difficile da bloccare perché sfrutta domini legittimi (es. servizi di newsletter).|Utilizzare la **verifica CAPTCHA** o **Double Opt-In (DOI)** sul proprio sito web e, se possibile, richiedere ai fornitori di servizi di terze parti di implementare DOI per le iscrizioni.|
|**Difesa Allegati Pesanti**|Rischio di crash del client di posta o del sistema di scansione antivirus.|Impostare un **limite massimo di dimensione** per le e-mail e gli allegati a livello di MTA. Utilizzare scanner che possono identificare e bloccare le _Zip Bomb_ ricorsive.|

**In sintesi:** L'Email Bombing è un attacco di volume che non richiede grandi sofisticazioni, ma può avere un impatto devastante sull'operatività di un'azienda. La difesa è prevalentemente basata su **controlli di volume e di tasso di traffico** a livello di rete e di server di posta.

---

Vorresti approfondire le strategie di **rate limiting** che un ingegnere può implementare sui server SMTP per contrastare questi attacchi?