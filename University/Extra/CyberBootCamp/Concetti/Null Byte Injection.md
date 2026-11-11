---
title: Null Byte Injection
tags:
  - cyberbootcamp
  - concetto
  - web-security
  - php
---

# Null Byte Injection

> [!summary] In breve
> Un `%00` nell'input tronca la stringa per le funzioni che la trattano come stringa C, eliminando per esempio un suffisso imposto dal programmatore.

```php
include($_GET["page"] . ".php");
// page=../../../etc/passwd%00
// PHP: "../../../etc/passwd\0.php"  →  include apre "../../../etc/passwd"
```

- Le stringhe PHP possono contenere `\0`, ma alcune funzioni implementate in C si fermano lì.
- Corretto in PHP 5.3.4: oggi vale per software vecchio, ma l'idea (due parser diversi) resta valida.

## Collegamenti

- **Concetti correlati**: [[Parser Differential]] · [[Path Traversal]]
- **Mappa**: [[MOC - CyberBootCamp]]

> [!info] Approfondimento
> - [[01 - CB - Web Insecurity 1#Path traversal: tips & tricks|Lezione 1 — Path traversal: tips & tricks]]
