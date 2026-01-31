# UTF-8

## 💡 Definizione
**UTF-8** (Unicode Transformation Format - 8-bit) è una codifica di caratteri a **lunghezza variabile** usata per rappresentare testo nel computer. È lo standard dominante del World Wide Web (usato da oltre il 98% dei siti web).

Il suo scopo principale è mappare i "code points" dello standard [[Unicode]] (che include caratteri di tutte le lingue del mondo ed emoji) in sequenze di **byte** (da 1 a 4) comprensibili dalla macchina.

---

## ⚙️ Come funziona (Meccanica)
La caratteristica geniale di UTF-8 è la sua **lunghezza variabile**: non usa lo stesso spazio per ogni carattere, ottimizzando la memoria.

1.  **1 Byte (7 bit):** Usato per i caratteri standard US-ASCII (a-z, A-Z, 0-9).
    * *Vantaggio:* Un file di testo puro [[ASCII]] è identico sia in ASCII che in UTF-8.
2.  **2 Byte:** Caratteri latini estesi, Greco, Cirillico, Arabo, Ebraico.
3.  **3 Byte:** Cinese, Giapponese, Coreano (CJK).
4.  **4 Byte:** Simboli matematici complessi, caratteri storici ed **Emoji** 🍕.

### Esempio visivo

| Carattere | Code Point Unicode | Codifica UTF-8 (Binario) | Dimensione |
| :--- | :--- | :--- | :--- |
| **A** | `U+0041` | `01000001` | 1 Byte |
| **è** | `U+00E8` | `11000011 10101000` | 2 Byte |
| **€** | `U+20AC` | `11100010 10000010 10101100` | 3 Byte |
| **🌍** | `U+1F30D` | `11110000 10011111 10001100 10001101` | 4 Byte |

---

## ✅ Vantaggi principali
* **Retrocompatibilità con ASCII:** Qualsiasi file ASCII valido è automaticamente un file UTF-8 valido. Questo ha permesso una transizione indolore dai vecchi sistemi.
* **Efficienza:** Per i testi occidentali (prevalentemente latini), occupa molto meno spazio rispetto a codifiche fisse come UTF-32.
* **Indipendenza dall'Endianness:** A differenza di UTF-16, UTF-8 viene letto un byte alla volta, quindi non soffre dei problemi di *[[Big Endian]]* o *[[Little Endian]]* (BOM).

> [!WARNING] Il problema del BOM (Byte Order Mark)
> Anche se non necessario, alcuni editor (come il vecchio Blocco Note di Windows) aggiungono un carattere invisibile all'inizio del file chiamato **BOM**. Questo può "rompere" script (es. PHP o Bash).
> *Best Practice:* Salvare sempre i file come **"UTF-8 without BOM"**.

---

## 🆚 Confronto rapido
* **vs ASCII:** ASCII supporta solo 128 caratteri (niente accenti, niente cinese). UTF-8 supporta tutto.
* **vs UTF-16:** UTF-16 usa minimo 2 byte per tutto. È peggiore per i testi in inglese (sprecano spazio), ma a volte migliore per le lingue asiatiche che richiedono sempre 2 o più byte.

---

## 🔗 Collegamenti
* [[Encode]]
* [[ASCII]]
* [[Hexadecimal]]
* [[Binary]]