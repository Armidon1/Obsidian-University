Perfetto, ti spiego in dettaglio 👇

Nella formula dell’[[HMAC]]:
$$\text{HMAC} = \text{Hash} \big( \text{chiave} \oplus \text{opad} , | , \text{Hash}(\text{chiave} \oplus \text{ipad} , | , \text{messaggio}) \big)  
$$
**`ipad` e `opad`** sono valori costanti definiti dallo standard HMAC:

---

### **1. ipad (inner padding)**

- Valore costante di **0x36 ripetuto** fino alla lunghezza del blocco della funzione di hash (es. 64 byte per SHA-256).
    
- Serve per **distinguere la parte interna** della funzione HMAC.
    
- Viene combinato con la chiave tramite **XOR**:  
    [  
    \text{chiave} \oplus \text{ipad}  
    ]
    

---

### **2. opad (outer padding)**

- Valore costante di **0x5C ripetuto** fino alla lunghezza del blocco della funzione di hash.
    
- Serve per **la parte esterna** della funzione HMAC.
    
- Anch’esso combinato con la chiave tramite XOR:  
    [  
    \text{chiave} \oplus \text{opad}  
    ]
    

---

### **Perché servono ipad e opad**

- Creano una **differenziazione tra l’hash interno e quello esterno**, impedendo attacchi di tipo **extension attack** sulle funzioni hash.
    
- Permettono di usare HMAC con qualsiasi funzione hash senza comprometterne la sicurezza.
    

---

**In breve:**

- `ipad` = inner pad (0x36) → combinato con la chiave per l’hash interno
    
- `opad` = outer pad (0x5C) → combinato con la chiave per l’hash esterno
    
- Entrambi garantiscono che l’HMAC sia **resistente alle collisioni e agli attacchi sulle funzioni hash**.
    
