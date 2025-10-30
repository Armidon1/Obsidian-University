# **ECB (Electronic Codebook Mode)**

> È la **modalità più semplice** di funzionamento di un **algoritmo di cifratura a blocchi** (come [[AES]]), in cui **ogni blocco di testo in chiaro viene cifrato indipendentemente** usando **la stessa chiave**.

**Come funziona:**
![[Pasted image 20251030105024.png]]

- Il messaggio viene diviso in blocchi (es. 128 bit per [[AES]]).
    
- Ogni blocco ( $P_i$ ) viene cifrato separatamente:  $$ C_i = E_k(P_i)$$
    dove ( $E_k$) è la cifratura con chiave ( $k$ ).
    
- Durante la decifratura:  ![[Pasted image 20251030105038.png]]$$P_i = D_k(C_i)  $$
**Garantisce:**

- ✅ **[[Confidentiality]]** _solo a livello di singolo blocco_ (i dati non sono leggibili senza chiave).
    

**Non garantisce:**

- ❌ **Diffusione**: blocchi identici in chiaro producono blocchi cifrati identici.
    
- ❌ **Protezione contro analisi statistica**.
    
- ❌ **[[Integrity]]** o **[[Authenticity]]**.
    

**Problema principale:**

> ECB **rivela i pattern** del testo in chiaro: immagini o dati strutturati cifrati con ECB mantengono una forma riconoscibile.

**Esempio:**
![[Pasted image 20251030105201.png]]
- Cifrare un’immagine con AES-ECB mostra ancora i contorni visibili della figura originale.
    

**Conclusione:**

> **ECB è insicuro** per la maggior parte degli usi pratici.  
> Viene sostituito da modalità più sicure come **CBC**, **CTR** o **GCM**, che introducono **casualità o autenticazione** per proteggere meglio i dati.