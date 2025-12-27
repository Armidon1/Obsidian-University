
# Master Key (Kerberos / krbtgt)

## 🔑 Che cos'è?
Nel contesto del protocollo [[Kerberos]], la **Master Key** (spesso chiamata **KDC Key** o chiave dell'account `krbtgt` in Active Directory) è la chiave crittografica segreta a lungo termine utilizzata dal [[KDC (Key Distribution Center)]].

È il "segreto supremo" dell'intero dominio di autenticazione. In Active Directory, questa chiave è derivata direttamente dall'hash della password dell'account di sistema chiamato **krbtgt**.

> [!DANGER] Importanza Critica
> Chi possiede questa chiave controlla l'intera identità del dominio. È l'unica chiave in grado di generare e validare i [[TGT (Ticket-Granting Ticket)]].

---

## ⚙️ A cosa serve?

La Master Key ha una funzione principale e insostituibile: **Cifrare e Firmare i TGT.**

Quando l'[[AS (Authentication Service)]] rilascia un TGT a un utente, cifra la parte più importante del ticket (quella che contiene l'identità dell'utente, la scadenza e la chiave di sessione) utilizzando proprio la **Master Key**.

Perché?
1. **Integrità:** Solo il KDC (che possiede la Master Key) può aver creato quel ticket.
2. **Riservatezza:** L'utente che riceve il TGT non può modificarlo né leggerne il contenuto interno, perché non possiede la Master Key.
3. **Stateless:** Grazie a questa cifratura, il KDC non deve memorizzare in un database quali ticket ha rilasciato. Gli basta provare a decifrare il TGT che gli viene presentato: se ci riesce con la propria Master Key, il ticket è valido.

---

## ⚠️ Il Rischio Supremo: Golden Ticket

Se un attaccante riesce a compromettere il Domain Controller e a estrarre l'hash NTLM dell'account `krbtgt` (ovvero la Master Key), può eseguire un attacco chiamato **Golden Ticket**.

Con la Master Key, l'attaccante può:
* Creare TGT falsi a piacimento ("forgiare" i biglietti).
* Impersonare **qualsiasi utente** (anche l'Amministratore del Dominio o CEO).
* Impostare una scadenza arbitraria (es. un ticket valido per 10 anni).
* Accedere a qualsiasi servizio nel dominio.

Tutto questo avviene **offline**, senza dover interagire con il KDC, rendendo l'attacco molto difficile da rilevare.

---

## 🛡️ Best Practices: Rotazione della Chiave

Dato che la Master Key è così critica, deve essere protetta con misure estreme.

1. **Rotazione Periodica:** In Active Directory, è buona norma cambiare la password dell'account `krbtgt` regolarmente (es. ogni 180 giorni o dopo ogni incidente di sicurezza o cambio di staff amministrativo critico).
2. **Doppia Rotazione:** Poiché il KDC mantiene la cronologia delle ultime 2 password per permettere ai ticket vecchi di funzionare ancora per qualche ora, per invalidare *immediatamente* tutti i Golden Ticket esistenti è necessario cambiare la password di `krbtgt` **due volte** consecutivamente.

---

