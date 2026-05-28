# Sample Files

> [!abstract] In una riga File e applicazioni **d'esempio** installati dal server per dimostrarne le funzioni, spesso pieni di buchi e **dimenticati in produzione**.

## Cos'è

Storicamente i server web venivano installati con un corredo di **sample application, script di esempio e documentazione** per mostrare agli amministratori cosa il prodotto sapeva fare. Il problema è duplice:

1. Quei sample sono scritti per **dimostrare**, non per essere sicuri → spesso contengono vulnerabilità.
2. Gli amministratori **dimenticano di rimuoverli** prima di andare in produzione.

## Come si sfrutta

Molti script d'esempio prendono un **parametro con un nome di file** e ne mostrano il contenuto. Combinandoli con un [[Canonicalization|directory traversal]] (`../`) si leggono file arbitrari del sistema:

```
http://target/iissamples/sdk/asp/.../showcode.asp?source=/../../../../boot.ini
```

## Esempi storici

- **IIS:** `showcode.asp` e `codebrws.asp` (lettura di file arbitrari), le cartelle `/iissamples`, `/msadc` (Remote Data Service / MDAC).
- **Apache / Tomcat:** servlet di esempio tipo `snoop` che rivelano variabili d'ambiente e configurazione.

## Difese

- **Rimuovere TUTTO** ciò che è d'esempio, demo o documentazione dai server di produzione.
- Partire da un'installazione **minimale** e aggiungere solo ciò che serve.
- Verificare con uno scanner (es. **Nikto**) che cerca proprio questi path noti.

## Collegamenti

- ⬆️ [[Web Server Hacking]]
- ↔️ [[Source Code Disclosure]] · [[Input Validation]]