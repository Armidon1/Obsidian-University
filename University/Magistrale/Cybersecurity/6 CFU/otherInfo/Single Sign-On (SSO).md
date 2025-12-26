# Single Sign-On (SSO)

## 📝 Definizione
Il **Single Sign-On (SSO)** è un metodo di autenticazione che permette a un utente di accedere a molteplici applicazioni o siti web indipendenti utilizzando un unico set di credenziali (username e password).

> [!INFO] Concetto Chiave
> L'SSO disaccoppia l'autenticazione (chi sei) dall'applicazione che stai utilizzando. L'applicazione si fida di una terza parte per verificare la tua identità.

---

## ⚙️ Come Funziona (Flusso Generale)

Il processo coinvolge tre attori principali:
1. **Utente (Principal):** La persona che vuole accedere.
2. **Service Provider (SP):** L'applicazione o risorsa (es. Slack, Jira, Gmail).
3. **Identity Provider (IdP):** Il sistema che detiene la directory degli utenti e verifica le credenziali (es. [[Okta]], [[Auth0]], [[Azure AD]]).

### Il Workflow Step-by-Step
1. L'utente tenta di accedere al **Service Provider (SP)**.
2. L'SP vede che l'utente non è loggato e genera una richiesta di autenticazione, reindirizzando l'utente verso l'**Identity Provider (IdP)**.
3. L'utente inserisce le credenziali *solo* sul portale dell'IdP (se non ha già una sessione attiva).
4. L'IdP verifica le credenziali.
5. L'IdP genera un **Token** (una "prova" crittografata) e reindirizza l'utente indietro all'SP.
6. L'SP valida il token e garantisce l'accesso.

---

## 📡 Protocolli Comuni

Per far comunicare SP e IdP in modo sicuro, si usano protocolli standard:

* **[[SAML]] (Security Assertion Markup Language):** Basato su XML. È lo standard storico per le aziende Enterprise.
* **[[OIDC]] (OpenID Connect):** Costruito sopra [[OAuth 2.0]]. Basato su JSON/REST. Più moderno, usato spesso per app mobile e web (es. "Accedi con Google").
* **Kerberos:** Usato principalmente in reti locali (LAN) e ambienti Windows.

---

## ✅ Vantaggi e ❌ Svantaggi

| Vantaggi (Pros) | Svantaggi (Cons) |
| :--- | :--- |
| **User Experience:** Meno password da ricordare (riduce la *password fatigue*). | **Single Point of Failure (SPOF):** Se l'IdP è offline, nessuno può accedere a nulla. |
| **Sicurezza:** Riduce la superficie di attacco (le password non sono salvate su ogni app). | **Rischio a catena:** Se le credenziali SSO vengono rubate, l'attaccante ha accesso a *tutti* i sistemi collegati. |
| **Gestione IT:** Facilita l'onboarding/offboarding e il reset delle password. | **Complessità:** Implementare correttamente l'SSO richiede competenze tecniche specifiche. |

---

## 🔗 Collegamenti Correlati
- [[Autenticazione vs Autorizzazione]]
- [[Multi-Factor Authentication (MFA)]]
- [[Gestione delle Password]]