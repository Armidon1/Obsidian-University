# Clickjacking (UI Redressing)

**Tag:** #security #web-security #vulnerability #clickjacking #CSP #fetch-metadata

**Fonte:** [[5 - CS Application Level - Web Security Part II]]

---

## 📝 Definizione

_(Nota: Definizione generale non presente esplicitamente nelle slide, inserita per contesto)_

Il **Clickjacking** (o UI Redressing) è una tecnica in cui un attaccante utilizza frame trasparenti o sovrapposti per ingannare l'utente, portandolo a cliccare su un elemento diverso da quello che percepisce visivamente (es. un pulsante "Bonifico" nascosto sotto un pulsante "Play").

---

## 🛡️ Prevenzione e Mitigazione

Le slide evidenziano due meccanismi moderni per mitigare questo tipo di attacco:

### 1. Fetch Metadata

L'uso dei **Fetch Metadata Request Headers** fornisce al server informazioni sul contesto in cui una richiesta viene generata, permettendo di bloccare richieste sospette.

- **Mitigazione:** I Fetch Metadata possono essere utilizzati per mitigare il Clickjacking (oltre a CSRF e XSSI) verificando come la risorsa viene richiesta.
    
- **Navigation Isolation Policy:** È possibile definire una policy che isola la navigazione. Ad esempio, verificando se `Sec-Fetch-Site` è `cross-site` e il `Sec-Fetch-Mode` è `Maps` (o `nested-navigate`), il server può decidere se permettere o meno il caricamento della pagina in un frame.
    

### 2. Content Security Policy (CSP)

La **Content Security Policy** è uno standard versatile utilizzato per controllare quali risorse possono essere caricate, ma offre anche controlli sul "framing".

- **Restrizione Framing:** La CSP viene utilizzata per limitare le "framing capabilities", ovvero definire chi è autorizzato a incorporare la pagina corrente (es. tramite `<frame>`, `<iframe>`, `<object>`).