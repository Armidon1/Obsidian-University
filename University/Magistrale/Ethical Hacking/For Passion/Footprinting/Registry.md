# I Registry — Chi Sono

### Definizione

Un **Registry** è l'organizzazione che gestisce il database autoritativo di tutti i domini registrati sotto un determinato TLD. È il livello intermedio tra [[ICANN]] (che stabilisce le regole) e i Registrar (che vendono i domini agli utenti).

```
Registry ≠ Registrar

Registry  → gestisce il DATABASE del TLD
            "chi possiede example.com?"
            risponde a questa domanda

Registrar → vende i domini agli utenti
            GoDaddy, Aruba, Namecheap...
            interfaccia con il Registry per aggiornare il database
            
Registrant → Il cliente che si registra
```

---

### I Registry Principali

**gTLD Registry**

```
Verisign          → .com e .net
                    il più grande al mondo
                    gestisce ~170 milioni di domini

Public Interest   → .org
Registry (PIR)      organizzazione no-profit

Afilias           → .info, .org (in passato)

NeuStar           → .us, .biz e molti new gTLD

Google Registry   → .dev, .app, .page, .foo
                    domini molto usati da sviluppatori

Amazon Registry   → .aws, .amazon e altri
```

**ccTLD Registry — Europa**

```
Registro.it       → .it (Italia)
                    gestito da IIT-CNR, Pisa
                    ~3.5 milioni di domini

DENIC             → .de (Germania)
                    ~17 milioni di domini
                    il ccTLD più grande d'Europa

AFNIC             → .fr (Francia)

Nominet           → .uk (Regno Unito)

EURid             → .eu (Unione Europea)

DNS Belgium       → .be (Belgio)

SWITCH            → .ch (Svizzera)
```

**ccTLD Registry — Resto del Mondo**

```
CNNIC             → .cn (Cina)
JPRS              → .jp (Giappone)
NIC Brazil        → .br (Brasile)
RU-CENTER         → .ru (Russia)
auDA              → .au (Australia)
```

---

### Cosa Fa Concretamente un Registry

```
1. Mantiene il database Whois
   → "example.com è registrato da Mario Rossi
      dal 2020-01-15, scade 2026-01-15"

2. Gestisce i nameserver autoritativi del TLD
   → a.gtld-servers.net per .com (Verisign)
   → nameserver.nic.it per .it (Registro.it)

3. Propaga le modifiche DNS
   → quando cambi nameserver su GoDaddy
     GoDaddy avvisa Verisign
     Verisign aggiorna il database .com

4. Stabilisce le regole di registrazione
   → .it richiede dati verificabili
   → .com accetta praticamente chiunque
   → .bank richiede verifica che tu sia una banca

5. Gestisce i prezzi wholesale
   → i Registrar comprano da loro
     e rivendono con markup
```

---

### Come lo Vedi nel WHOIS

```bash
whois example.com
```

```
Registry Domain ID: 2336799_DOMAIN_COM-VRSN
                    ↑
                    VRSN = Verisign
                    questo ID è nel database Verisign

Registrar WHOIS Server: whois.godaddy.com
Registrar: GoDaddy.com, LLC
                    ↑
                    chi ha venduto il dominio

Registry Expiry Date: 2025-08-13T04:00:00Z
                    ↑
                    data nel database Verisign
```

---

### Perché Conta nel Footprinting

```
Registry rivela:
→ Quando è stato registrato il dominio
  (dominio vecchio = organizzazione consolidata)
  (dominio recente = potenziale phishing/typosquatting)

→ Quando scade
  (dominio in scadenza = possibile domain hijacking
   se l'azienda dimentica di rinnovarlo)

→ Quale Registrar usano
  (alcuni Registrar hanno vulnerabilità note
   o politiche di sicurezza deboli)
```

```bash
# Controllare la scadenza di un dominio
whois example.com | grep -i "expir"

# Monitorare domini in scadenza è una tecnica
# usata sia dai difensori che dagli attaccanti
```

> [!tip] Il **domain hijacking** avviene spesso quando un'azienda dimentica di rinnovare un dominio. Il Registry lo mette in periodo di grazia, poi in redemption, poi lo rilascia. Un attaccante lo registra immediatamente — e improvvisamente possiede un dominio con storico, reputazione email e magari record DNS che puntano ancora a servizi interni dell'azienda originale.