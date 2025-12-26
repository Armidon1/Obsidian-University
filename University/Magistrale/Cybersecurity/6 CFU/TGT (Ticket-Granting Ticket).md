# Ticket-Granting Ticket (TGT)

## 🧐 Che cos'è?
Il **Ticket-Granting Ticket (TGT)** è un piccolo file di dati crittografato rilasciato dal *Key Distribution Center* (KDC) nel protocollo [[Kerberos]].

È la prova che un utente si è autenticato con successo. Il suo scopo è permettere all'utente di richiedere l'accesso a specifici servizi di rete senza dover reinserire la password ogni volta.

> [!EXAMPLE] L'analogia del Parco Divertimenti
> Immagina il TGT come il **braccialetto** che ricevi all'ingresso di un parco o di un festival dopo aver mostrato il biglietto e il documento.
> * Non devi mostrare il documento a ogni singola giostra.
> * Ti basta mostrare il braccialetto (TGT) allo stand specifico per ottenere l'accesso a quella giostra (che in Kerberos corrisponde al [[Service Ticket]]).

---

## ⚙️ Come funziona nel flusso Kerberos

Il TGT è il protagonista della **Fase 1** e **Fase 2** dell'autenticazione Kerberos:

1.  **Richiesta (AS_REQ):** L'utente invia una richiesta di autenticazione all'Authentication Service (AS) del KDC.
2.  **Rilascio (AS_REP):** Se le credenziali sono valide, il KDC crea il TGT.
    * ⚠️ **Nota Importante:** Il TGT è crittografato con la **chiave segreta del KDC** (in particolare dell'account `krbtgt`). L'utente *non può* decifrarlo né modificarlo, può solo custodirlo.
3.  **Utilizzo (TGS_REQ):** Quando l'utente vuole accedere a una risorsa (es. un File Server), invia il TGT al *Ticket Granting Service* (TGS).
4.  **Verifica:** Il TGS decifra il TGT (poiché possiede la chiave segreta), verifica che sia valido e non scaduto, e rilascia un [[Service Ticket]] per quella specifica risorsa.

---

## 🛡️ Caratteristiche di Sicurezza

* **Scadenza (Time-to-Live):** Il TGT ha una durata limitata (solitamente 8-10 ore in ambiente Windows/Active Directory). Dopo la scadenza, l'utente deve autenticarsi di nuovo.
* **Rinnovo:** Può essere rinnovato entro certi limiti senza reinserire la password.
* **Opacità:** Come detto, è opaco per il client. Solo il KDC sa cosa c'è scritto dentro.

---

## ⚠️ Rischi e Attacchi

Essendo la chiave di volta dell'identità dell'utente, il TGT è bersaglio di attacchi specifici:

* **Pass-the-Ticket (PtT):** Un attaccante ruba un TGT valido dalla memoria di un computer compromesso e lo usa per accedere alle risorse come se fosse quell'utente,