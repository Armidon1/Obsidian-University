# SSL (Secure Sockets Layer)
#cybersecurity #networking #encryption #protocols

## 1. Definition
**SSL (Secure Sockets Layer)** is the standard security technology for establishing an encrypted link between a server and a client (typically a web server and a browser). It ensures that all data passed between them remains private and integral.

> [!INFO] SSL vs. TLS
> **Strictly speaking, SSL is dead.** The protocols SSL 1.0, 2.0, and 3.0 have all been deprecated due to security vulnerabilities.
> 
> What we use today is **[[TLS]] (Transport Layer Security)**. However, the term "SSL" is still widely used in the industry as a generic name for the technology (e.g., "SSL Certificates").

---

## 2. Core Security Pillars (The CIA Triad)
SSL/TLS implements the following to guarantee the CIA triad:

### 🔒 Confidentiality (Privacy)
* **Goal:** Prevent eavesdroppers from reading the data.
* **Mechanism:** Uses **Symmetric Encryption** (like AES or ChaCha20) for the actual data transfer.
* **Why:** Symmetric encryption is fast and efficient for large streams of data.

### 🛡️ Integrity (Trust)
* **Goal:** Ensure data has not been altered or tampered with in transit.
* **Mechanism:** Uses **Hashing** and **MACs (Message Authentication Codes)**.
* **Process:** Each packet has a cryptographic tag. If a hacker flips even one bit, the hash check fails, and the connection drops.

### 🆔 Authenticity (Identity)
* **Goal:** Prove that the server is who it claims to be (e.g., `google.com` and not a hacker).
* **Mechanism:** Uses **Digital Certificates (X.509)** and **Asymmetric Encryption** (RSA or ECC).
* **Process:** The client validates the server's certificate against a list of trusted **Certificate Authorities (CAs)**.

---

## 3. How It Works (The Handshake)
Before any data is sent, the client and server perform a "Handshake" to negotiate security:

1.  **Client Hello:** "I support TLS 1.3 and these cipher suites."
2.  **Server Hello:** "Let's use TLS 1.3. Here is my **Certificate** (Public Key)."
3.  **Verification:** Client checks if the certificate is valid and trusted.
4.  **Key Exchange:** They use Asymmetric encryption (Diffie-Hellman) to securely agree on a **Session Key**.
5.  **Secure Session:** They switch to Symmetric encryption using the Session Key.

---

## 4. Protocol History
| Version | Status | Notes |
| :--- | :--- | :--- |
| **SSL 1.0 - 3.0** | ❌ Deprecated | Vulnerable to POODLE, DROWN. |
| **TLS 1.0 - 1.1** | ❌ Deprecated | Old algorithms, vulnerable to BEAST. |
| **TLS 1.2** | ✅ Active | The current industry workhorse. |
| **TLS 1.3** | 🚀 **Best** | Faster handshake, Perfect Forward Secrecy forced. |