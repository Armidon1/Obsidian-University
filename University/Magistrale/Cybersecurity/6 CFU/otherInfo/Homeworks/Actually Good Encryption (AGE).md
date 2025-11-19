![[Pasted image 20251118192424.png]]

*SIMONE NOLÈ 1940213 18/10/2025*

# REPORT 2° HOMEWORK
---
## What is AGE?
AGE (Actually Good Encryption) is a tool which allows to Encrypt and Decrypt files easily. What makes special AGE is the impossibility of making errors, because it doesn't give the possibility to the user change some configurations (reducing the user's surface of action).

AGE not only gives the opportunity to do **Symmetric Encryption** but also a **Public-Key Encryption**. More in details, for Public-Key Encryption, in reality it is used an **Hybrid Encryption** approach (it will be discussed later) to guarantee Confidentiality, Integrity, Authenticity and also Confidentiality for the Symmetric Key thanks to the usage of an **Elliptic Curve Diffie-Hellman Key Exchange**.

## Examples of AGE's usage

### Symmetric Encryption
fare vedere come viene implementata la sua simmetric encryption tramite concatenazione di KDF e ChaCha20-Poly1305
```bash
age 
```

### Public-Key Encryption
il cuore di AGE.

---