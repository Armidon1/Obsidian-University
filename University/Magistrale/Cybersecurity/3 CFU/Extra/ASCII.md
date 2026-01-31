# ASCII

## 💡 Definizione
**ASCII** (acronimo di *American Standard Code for Information Interchange*) è il primo standard universale di codifica dei caratteri, sviluppato negli anni '60.

Rappresenta il testo utilizzando numeri interi mappati su **7 bit**, permettendo un totale di **128 caratteri possibili** (da 0 a 127). È il sottoinsieme fondamentale su cui si basano quasi tutte le codifiche moderne, inclusa [[UTF-8]].

---

## 🏗️ Struttura della tabella ASCII
I 128 caratteri sono divisi in gruppi funzionali specifici:

1.  **Codici di Controllo (0-31):** Caratteri non stampabili usati originariamente per controllare le telescriventi (es. `CR` Carriage Return, `LF` Line Feed, `BEL` Bell).
2.  **Caratteri Stampabili (32-126):** Lettere (A-Z, a-z), numeri (0-9), punteggiatura e lo Spazio (che è il 32).
3.  **Delete (127):** Il comando di cancellazione.

### Esempio di mappatura
Un trucco classico è che tra le maiuscole e le minuscole c'è una differenza esatta di **32** (un singolo bit di differenza), rendendo facile la conversione via codice.

| Carattere | Decimale | Binario (7 bit) | Note |
| :--- | :--- | :--- | :--- |
| **NULL** | 0 | `0000000` | Usato per terminare le stringhe in C |
| **(spazio)** | 32 | `0100000` | Il primo carattere stampabile |
| **0** | 48 | `0110000` | I numeri partono da qui |
| **A** | 65 | `1000001` | Maiuscola |
| **a** | 97 | `1100001` | Minuscola (65 + 32) |

---

## ⚠️ I Limiti di ASCII
Poiché ASCII usa solo 7 bit (e l'inglese non ha accenti), presenta grossi limiti per l'internazionalizzazione:

* **Nessun accento:** Niente `è`, `ù`, `ñ`, `ç`.
* **Nessun alfabeto non latino:** Impossibile scrivere in greco, russo, arabo o cinese.
* **Nessuna emoji:** Lo spazio era troppo prezioso per le faccine.

> [!DANGER] La confusione di "Extended ASCII"
> Poiché i computer lavorano a 8 bit (1 byte), rimaneva 1 bit libero. Negli anni '80/90, diversi produttori usarono quel bit extra per creare i caratteri 128-255 (chiamati **Extended ASCII** o codifiche ISO-8859).
>
> Il problema? Ognuno usava quei numeri diversamente.
> * Su un PC italiano, il codice `133` era **à**.
> * Su un PC russo, lo stesso codice `133` era una lettera cirillica.
>
> Questo caos ("Mojibake") è il motivo principale per cui è nato [[UTF-8]].

---

## 🔗 Relazione con UTF-8
ASCII è un **sottoinsieme valido** di UTF-8.
Questo significa che i primi 128 caratteri di UTF-8 sono **identici** alla tabella ASCII. Un file che contiene solo testo inglese semplice è, byte per byte, identico sia se salvato come ASCII sia se salvato come UTF-8.

---

## 🔗 Collegamenti
* [[Encoded]]
* [[UTF-8]]
* [[Binary]]
* [[History of Computing]]