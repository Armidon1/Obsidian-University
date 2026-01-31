
# Base64

## 💡 Definizione
**Base64** è un metodo di codifica che converte dati binari (come immagini, PDF, o file audio) in una stringa di testo [[ASCII]].

Il nome deriva dal fatto che utilizza un "alfabeto" di **64 caratteri** sicuri e stampabili per rappresentare i dati.
L'alfabeto standard è composto da:
* `A-Z` (26 caratteri)
* `a-z` (26 caratteri)
* `0-9` (10 caratteri)
* `+` e `/` (2 caratteri simbolici)

---

## ❓ Perché serve?
Molti protocolli storici di internet (come l'Email/SMTP) o formati dati (come JSON o XML) sono stati progettati per trasmettere **solo testo**. Se provassi a inviare un'immagine "cruda" (bit binari) via email, il sistema potrebbe interpretare male alcuni bit come comandi di controllo (interrompendo l'invio).

Base64 risolve il problema trasformando qualsiasi dato binario in testo sicuro che può viaggiare ovunque senza corrompersi.

---

## ⚙️ Come funziona (Il meccanismo 3-a-4)
Base64 prende gruppi di **3 byte** (24 bit) dall'input originale e li divide in **4 gruppi** da 6 bit ciascuno.

Poiché $2^6 = 64$, ogni gruppo da 6 bit corrisponde perfettamente a uno dei 64 caratteri della tabella Base64.

### L'Overhead (Il costo)
Poiché trasformiamo 3 byte in 4 caratteri, la dimensione del file **aumenta di circa il 33%**.
* *File originale:* 30 MB
* *File in Base64:* ~40 MB

> [!NOTE] Il Padding (=)
> Se la lunghezza dei dati originali non è divisibile per 3, Base64 aggiunge dei caratteri speciali ` = ` alla fine della stringa per riempire lo spazio.
> Se vedi una stringa che finisce con `==`, è quasi sicuramente Base64.

---

## 🚀 Casi d'uso comuni
1.  **Email (MIME):** Tutti gli allegati che invii via mail vengono convertiti in Base64 dietro le quinte.
2.  **Data URIs (HTML/CSS):** Puoi incorporare piccole immagini direttamente nel codice senza caricarle come file esterni.
    ```html
    <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAU...">
    ```
3.  **Autenticazione:** Gli header "Basic Auth" delle API usano spesso `username:password` codificati in Base64.
4.  **JWT (JSON Web Tokens):** La struttura dei token di sicurezza moderni è basata su stringhe Base64 (nella variante URL-safe).

---

## ⚠️ Base64 NON è Cifratura (Encryption)
Questo è un errore comune. Base64 **non protegge i dati**.
Chiunque può decodificare una stringa Base64 istantaneamente.
* **Encoding (Base64):** Serve a *trasportare* i dati in modo sicuro attraverso i sistemi.
* **Encryption:** Serve a *nascondere* i dati agli occhi indiscreti.

---

## 🔗 Collegamenti
* [[Encoded]]
* [[ASCII]]
* [[Binary]]
* [[Web Development]]