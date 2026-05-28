---
tags:
  - security
  - web-hacking
  - hacking-exposed
source: "Hacking Exposed 7 — Web Application Hacking"
type: nota
up: "[[Web Application Hacking]]"
---

# Authorization

> [!abstract] In una riga
> Una volta autenticato: **cosa ti è permesso fare?** Attacchi al controllo degli accessi.

## Cos'è

[[Authentication Attacks|Autenticazione]] = *"chi sei"*; **autorizzazione** = *"cosa puoi fare"*. È il controllo degli accessi: l'app deve verificare, **a ogni richiesta**, che l'utente abbia il diritto di vedere o fare quella cosa specifica. Quando questo controllo manca o è debole, si accede a risorse altrui o a funzioni privilegiate.

## Attacchi tipici

- **IDOR** (*Insecure Direct Object Reference*): cambi un identificatore nell'URL/parametro e accedi ai dati di un altro utente, es. `…/fattura?id=1001` → `id=1002`.
- **Privilege escalation:** *orizzontale* (dati di un altro utente al tuo stesso livello) o *verticale* (funzioni da amministratore).
- **Forced browsing / missing function-level access control:** raggiungere direttamente per URL pagine admin che non dovrebbero essere accessibili.
- **Parameter tampering:** manomettere valori come `role=admin`.

## Difese

- **Controllo di autorizzazione lato server su OGNI richiesta**, non solo nascondere link/bottoni.
- Principio **deny-by-default**: tutto negato salvo esplicito permesso.
- Non affidarsi a URL "segreti" o offuscati (security by obscurity).
- Riferimenti **indiretti** agli oggetti e verifica della proprietà per-utente.

## Collegamenti

- ⬆️ [[Web Application Hacking]]
- ↔️ [[Authentication Attacks]] (viene prima) · [[Session Management]]
