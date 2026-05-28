
preso da [[4 - CS Applitcation Level - Sintesi Web Security Part I]]
# Code Injection

La **Code Injection** è simile, ma invece di eseguire comandi del sistema operativo, l'attaccante inietta codice che viene interpretato ed eseguito dall'applicazione stessa (es. codice PHP, Python, JavaScript).

**Esempio vulnerabile (`calc.php`):**
```PHP
<?php
// Vulnerabilità: eval() esegue la stringa come codice PHP
eval("echo " . $_GET["expr"] . ";");
?>
```

_Arricchimento: Funzioni come `eval()` sono estremamente pericolose perché permettono di fare qualsiasi cosa il linguaggio supporti.
![[Pasted image 20251117150531.png]]_

#### L'Attacco

Richiesta: GET /calc.php?expr=file_get_contents('/etc/passwd')

Il server esegue: eval("echo file_get_contents('/etc/passwd');");

Risultato: Il contenuto del file viene visualizzato. L'attaccante ha ottenuto l'esecuzione di codice arbitrario (RCE - Remote Code Execution).

![[Pasted image 20251117150554.png]]

### Moodle Command line Injection (2018)
![[Pasted image 20251117151028.png]]
Details: https://blog.ripstech.com/2018/moodle-remote-code-execution/
guarda [[Moodle Command Line Injection Example|qui]]
Ci sono volute 4 patch per sistemare questa vulnerabilità. Non è assolutamente facile gestire user-inputs.

---

### Prevenzione

1. **EVITARE** funzioni pericolose come `eval()` che eseguono codice dinamico.
    
2. **EVITARE**, se possibile, funzioni che eseguono comandi di sistema. Usare librerie native del linguaggio equivalenti (es. usare una libreria per il ping invece di chiamare il binario del sistema operativo).
    
3. **Se indispensabile**, usare funzioni specifiche per l'escaping degli argomenti (es. `escapeshellarg()` in PHP), anche se questa è una soluzione spesso fragile.
    
4. **Difesa in profondità:** Usare sandbox, container e privilegi minimi per limitare l'impatto se l'injection dovesse riuscire.