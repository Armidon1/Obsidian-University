# La risposta onesta

Hacking Exposed 7 è un libro del **2012** — quei dettagli organizzativi di ICANN erano già abbastanza accademici allora, figuriamoci oggi. Nessun penetration tester nel 2026 si chiede mai "qual è la differenza tra ASO e GNSO" durante un engagement.

---

### Cosa devi sapere davvero

Solo la catena funzionale — quella sì che serve: 

```
ICANN
└── coordina tutto il sistema DNS a livello globale
    └── delega la gestione dei TLD ai Registry
        └── .com → Verisign
            .it  → Registro.it
            .org → PIR
            └── i Registry delegano la vendita ai Registrar
                └── GoDaddy, Aruba, OVH, Namecheap...
                    └── tu acquisti il dominio → sei il Registrant
```

Questo è tutto quello che ti serve per capire WHOIS, footprinting e DNS. giarda anche i [[Registry]]

---

### Gli acronimi in due righe ciascuno

Se proprio vuoi saperli per completezza:

```
IANA   → Internet Assigned Numbers Authority
         gestisce IP, numeri di porta, protocol numbers
         ora parte di ICANN

ICANN  → Internet Corporation for Assigned Names and Numbers
         il "governo" di internet — coordina DNS e IP globalmente

ASO    → Address Supporting Organization
         consiglia ICANN sulla gestione degli indirizzi IP
         lavora con i Regional Internet Registry (ARIN, RIPE, ecc.)

GNSO   → Generic Names Supporting Organization
         si occupa dei gTLD (.com, .org, .net...)
         è chi ha approvato i nuovi TLD dal 2013

ccNSO  → Country Code Names Supporting Organization
         si occupa dei ccTLD (.it, .de, .fr...)
         coordina i registry nazionali
```

---

### Il punto pratico

```
Per fare WHOIS su un dominio:
→ non ti serve sapere nulla di ICANN

Per capire perché un .it ha regole diverse da un .com:
→ ti basta sapere che i ccTLD hanno registry nazionali

Per un pentest reale:
→ whois example.com
→ leggi i risultati
→ fine
```

> [!tip] Hacking Exposed 7 è un classico ma ha 13 anni. Per la parte organizzativa di ICANN/IANA salta pure e concentrati sui concetti tecnici — quelli non sono cambiati. Per il WHOIS quello che conta è saper leggere l'output e capire cosa rivela sul target.