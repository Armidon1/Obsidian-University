# Reflection Attack (Attacco di Riflessione)

**Tags:** #engineering #cybersecurity #network-security #kerberos #replay-attack

---

## 1. Cos'è un Reflection Attack?

Il **Reflection Attack** è una variante specifica del **Replay Attack**. In questo scenario, l'attaccante intercetta un messaggio inviato da una vittima e lo "riflette" (lo invia nuovamente) alla vittima stessa o a un'altra istanza dello stesso servizio che utilizza la medesima chiave.

L'obiettivo è indurre la vittima a credere che il messaggio provenga da un'entità autenticata, sfruttando il fatto che il sistema non distingue correttamente la direzione del messaggio o l'identità dell'istanza specifica.

---

## 2. Vulnerabilità in Sistemi Distribuiti

In ambito Kerberos, questa vulnerabilità emerge tipicamente in due casi:

1. **Istanze Multiple:** Quando molte istanze dello stesso server utilizzano tutte la stessa **Master Key**.
    
2. **Mancanza di Direzionalità:** Quando il protocollo non specifica se un messaggio è "da Client a Server" o "da Server a Client".
    

> [!failure] Common Pitfall
> 
> Se un attaccante intercetta un pacchetto cifrato inviato verso un server e lo rispedisce a un'altra istanza del server che condivide la stessa chiave, quest'ultima potrebbe accettarlo come valido, non accorgendosi che si tratta di una "riflessione" di un messaggio precedente.

---

## 3. Il Meccanismo nel Protocollo di Autenticazione

Immaginiamo Alice che cerca di autenticarsi presso un server. L'attaccante intercetta l'**Authenticator**:

### Logica Matematica dell'Attacco

L'invio originale di Alice è:

$$\text{Auth} = K_{AB} \{ \text{Alice}, t_A \}$$

L'azione dell'attaccante:

L'attaccante non può decifrare il pacchetto (perché non conosce la chiave di sessione $K_{AB}$), ma lo riflette verso un altro server (o verso il client stesso se il protocollo lo permette).

> [!abstract] Math Analysis
> 
> Senza un controllo di integrità o di direzionalità, il destinatario della riflessione vede un pacchetto cifrato correttamente con la chiave attesa e lo processa come se fosse una nuova richiesta legittima.

---

## 4. Prevenzione: Come Kerberos neutralizza l'attacco

Kerberos implementa diverse strategie per rendere inutile la riflessione dei messaggi.

### A. Incremento del Timestamp ($t_A + 1$)

Nella **Mutual Authentication**, per evitare che l'attaccante rifletta il timestamp di Alice facendolo passare per quello del server, il server è obbligato a modificarlo.

La risposta del server (AP_REP) deve essere:

$$\text{Risposta} = K_{AB} \{ t_A + 1 \}$$

> [!tip] Exam Focus
> 
> Se Alice riceve indietro esattamente $K_{AB} \{ t_A \}$, capisce immediatamente che si tratta di un attacco di riflessione. Solo ricevendo $t_A + 1$ ha la prova che il server ha effettivamente decifrato, elaborato e risposto in modo asimmetrico.

### B. Cache di Replay (Replay Caches)

I server mantengono una memoria temporanea (cache) di tutti gli Authenticator ricevuti recentemente.

- Se un server riceve un pacchetto identico a uno già presente in cache, lo scarta immediatamente.
    
- Questo blocca i tentativi di riflessione immediata.
    

### C. Uso di MAC (Message Authentication Code)

Nelle versioni più avanzate, viene aggiunto un codice di integrità ai dati per garantire che il corpo del messaggio non sia stato manipolato durante il transito.

---

## 5. Sintesi Visuale

![[SCREEN_SLIDE_REFLECTION_LOGIC]]

> [!abstract] Visual Analysis
> 
> What to look at: Lo schema mostra un messaggio che "rimbalza" verso l'origine o verso un'entità gemella.
> 
> Meaning: Senza la protezione del $+1$ o della cache, l'attaccante bypassa la necessità di conoscere la password cifrando "per riflesso".

---

> [!example] Professor's Example
> 
> Pensate a uno specchio: se io dico "Buongiorno" allo specchio, lo specchio mi risponde "Buongiorno". Se il protocollo di sicurezza non prevede che lo specchio debba rispondere "Buongiorno a te", io non posso distinguere se sto parlando con una persona reale o con il mio riflesso. Il $+1$ di Kerberos è quel "a te" che rompe la simmetria.
