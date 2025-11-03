# **HMAC (Hash-based Message Authentication Code)**

> È una forma specifica di **[[MAC]] (Message Authentication Code)** che usa una **funzione di hash crittografica** (come [[SHA]]-256 o [[SHA]]-3) combinata con una **chiave segreta** per garantire **[[Integrity]]** e **[[Authenticity]]** dei messaggi.

**Come funziona:**

1. Mittente e destinatario condividono una chiave segreta.
    
2. Il mittente calcola un valore $HMAC = Hash(chiave \oplus opad ‖ Hash(chiave \oplus ipad ‖ messaggio))$. vedi che sono [[opad e ipad]] 
    
3. Il destinatario ricalcola l’[[HMAC]] e lo confronta con quello ricevuto.
    
4. Se coincidono → il messaggio **non è stato alterato** e **proviene da una fonte autentica**.
    
 
**Garantisce:**

- ✅ **Integrità** (il messaggio non è stato modificato)
    
- ✅ **Autenticità** (solo chi conosce la chiave può generare un HMAC valido)
    

**Non garantisce:**

- ❌ **[[Confidentiality]]** (il contenuto del messaggio non è cifrato)
    

**Esempi d’uso:** [[TLS]], IPsec, JWT (JSON Web Token), autenticazione API.

vedi anche la [[differenza tra GHASH e HMAC]]