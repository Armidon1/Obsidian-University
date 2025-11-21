# ElGamal and Digital Signature Standard (DSS)

**Tags:** #engineering #cryptography #digital_signature #ElGamal #DSS #NIST

## 1. Introduction and Historical Context

**ElGamal** is a cryptosystem designed by **Taher Elgamal** (often called the "father of SSL"). It is significant because it defines **two distinct methods**:

- One for **Encryption** (Confidentiality).
    
- One for **Digital Signatures**.
    

Both methods are inspired by the **Diffie-Hellman** key exchange and rely on the difficulty of the **Discrete Logarithm** problem 1.

> [!abstract] Visual Analysis
> 
> ![[SCREEN_SLIDE_UNIFICATION_DIAGRAM]]
> 
> What to look at: The diagram showing ElGamal and DSS as related concepts rooted in Modular Arithmetic and Prime numbers.
> 
> **Meaning:** It visualizes how DSS is an evolution/standardization based on ElGamal, which in turn is based on Diffie-Hellman principles2.

---

## 2. ElGamal Encryption

Although the main focus is often on signatures, ElGamal encryption is historically important. It is composed of three components: Key Generator, Encryption Algorithm, and Decryption Algorithm.

### [Technical Logic / Math]

**The mathematical definition for Key Generation is:**

$$\begin{align*} & \text{Public Parameters:} \quad p \text{ (prime)}, g \in \mathbb{Z}_p^* \text{ (generator)} \\ & \text{Private Key:} \quad x \in \{0, 1, \dots, p-1\} \text{ (chosen at random)} \\ & \text{Public Key:} \quad y = g^x \pmod p \end{align*}$$

**The mathematical definition for Encryption (Bob sends to Alice) is:**

$$\begin{align*} & \text{Choose random } y_{rand} \in \{0, 1, \dots, p-1\} \\ & C_1 = g^{y_{rand}} \pmod p \\ & C_2 = m \cdot g^{x \cdot y_{rand}} \pmod p \\ & \text{Ciphertext:} \quad (C_1, C_2) \end{align*}$$

> [!abstract] Math Analysis
> 
> Randomness: Bob chooses a new random $y_{rand}$ for every message. This ensures that encrypting the same message twice yields different ciphertexts (probabilistic encryption).
> 
> **Decryption:** Alice computes $(C_1)^x = g^{x \cdot y_{rand}}$ and uses its inverse to recover $m$ 3.

---

## 3. ElGamal Signature Scheme

Unlike RSA, where the signature is often described as "decryption with the private key," ElGamal signatures use a dedicated algorithm that generates a pair of values $(r, s)$.

> [!example] Professor's Example
> 
> In RSA, to get different signatures for the same message, we need an external framework (like PKCS/PSS) to add randomness. In ElGamal, the randomness is built-in to the algorithm itself. This means no external pre-processing is needed to ensure signatures are unique 4.

### [Technical Logic / Math]

**The mathematical definition for Key Generation is:**

$$\begin{align*} & \text{Pick prime } p \text{ (1024 bits) s.t. Discrete Log is hard} \\ & \text{Let } g \text{ be a generator of } \mathbb{Z}_p^* \\ & \text{Pick } x \in [2, p-2] \text{ at random (Private Key)} \\ & \text{Compute } y = g^x \pmod p \text{ (Public Key: } p, g, y\text{)} \end{align*}$$

**The mathematical definition for Signing is:**

$$\begin{align*} & \text{Let } m = H(M) \\ & \text{Pick } k \in [1, p-2] \text{ s.t. } \gcd(k, p-1) = 1 \\ & r = g^k \pmod p \\ & s = (m - r \cdot x) \cdot k^{-1} \pmod{p-1} \end{align*}$$

**Procedural Step:**

- **If $s$ is zero, restart.**
    

> [!abstract] Math Analysis
> 
> - **The pair (r, s):** The signature consists of two numbers.
>     
> - **Pre-processing:** Notice that $r = g^k \pmod p$ does **not** depend on the message $m$. This allows $r$ to be computed **in advance** (offline), improving efficiency during the actual signing phase 5.
>     
> - **Modulo:** The calculation of $s$ is done modulo $p-1$, not $p$.
>     

### [Verification]

**The mathematical definition for Verification is:**

$$\text{Accept if } (0 < r < p) \land (0 < s < p-1) \land (y^r \cdot r^s \equiv g^m \pmod p)$$

> [!tip] Exam Focus
> 
> The verification works because:
> 
> $$ y^r r^s = g^{rx} g^{ks} = g^{rx + k(m-rx)k^{-1}} = g^{rx + m - rx} = g^m $$
> 
> This equality confirms authenticity without revealing the private key $x$ 6.

---

## 4. ElGamal vs RSA

A comparison of the two major public-key systems.

|**Feature**|**ElGamal**|**RSA**|
|---|---|---|
|**Computation**|Multiple exponentiations (slower verify)|One exponentiation (faster verify)|
|**Signature Size**|Larger (2 components: $r, s$)|Smaller (1 component)|
|**Security**|Discrete Logarithm|Integer Factorization|
|**Randomness**|**Required** for every signature|Not required for core algo (needs padding)|

> [!abstract] Visual Analysis
> 
> ![[SCREEN_SLIDE_ELGAMAL_VS_RSA]]
> 
> What to look at: The comparison table highlighting "Computation", "Signature Size", and "Security Level".
> 
> **Meaning:** RSA is generally preferred for environments prioritizing fast verification (like SSL certs in browsers), while ElGamal/DSS is useful if pre-processing can be leveraged 7.

---

## 5. Digital Signature Standard (DSS) & DSA

**DSS** (FIPS 186) is the NIST standard that uses the **DSA** (Digital Signature Algorithm). It is essentially an optimized version of ElGamal designed specifically for signatures.

### [Technical Logic / Math]

**The mathematical definition for Preparation is:**

$$\begin{align*} & p \text{: L-bit prime (1024 to 3072 bits)} \\ & q \text{: 160 to 256-bit prime that divides } p-1 \quad (p = j \cdot q + 1) \\ & \alpha \text{: A } q\text{-th root of 1 modulo } p \quad (\alpha^q \equiv 1 \pmod p) \end{align*}$$

**How to compute $\alpha$:**

$$\begin{align*} & \text{Take random } h \text{ s.t. } 1 < h < p-1 \\ & g = h^{(p-1)/q} \pmod p \\ & \text{If } g = 1 \text{ try different } h \\ & \text{Set } \alpha = g \end{align*}$$

> [!example] Professor's Example
> 
> "Sometimes when I am bored designing the exam, I insert an exercise: compute alpha for this case." It's a simple check of understanding the construction8.

### [DSA Execution]

**The mathematical definition for Signing is:**

$$\begin{align*} & \text{Choose random } k \quad (1 \le k \le q-1) \\ & P_1 = (\alpha^k \pmod p) \pmod q \\ & P_2 = (H(M) + s \cdot P_1) \cdot k^{-1} \pmod q \\ & \text{Signature: } (P_1, P_2) \end{align*}$$

> [!abstract] Math Analysis
> 
> - Modulo q: Unlike ElGamal (mod $p-1$), DSA calculates the second component modulo $q$ (a much smaller prime, e.g., 160 bits). This results in smaller signatures.
>     
>     * Pre-processing: $P_1$ is independent of the message $M$ 9.
>     

### [DSA Verification]

**The mathematical definition for Verification is:**

$$\begin{align*} & w = P_2^{-1} \pmod q \\ & e_1 = H(M) \cdot w \pmod q \\ & e_2 = P_1 \cdot w \pmod q \\ & \text{Accept if } ( (\alpha^{e_1} y^{e_2} \pmod p) \pmod q ) = P_1 \end{align*}$$

---

## 6. Security: The "k" Vulnerability

The security of DSA (and ElGamal) depends critically on the random number $k$.

> [!failure] Common Pitfall
> 
> Never reuse k! If an adversary finds two different messages signed with the same k, they can mathematically recover the private key $s$.
> 
> Additionally, if $k$ is known, $s$ is trivially revealed 10.

### [Technical Logic / Math]

**If the adversary knows $k$:**

$$s = (P_2 \cdot k - H(M)) \cdot P_1^{-1} \pmod q$$

If $k$ is reused for two messages ($M, M'$):

We have two equations with two unknowns ($s$ and $k$), which can be solved linearly to find $s$.

---
nella parte in cui fa accept if (..)  And (..) and (QUI) dice che è la parte più importante perché dipende dal messaggio (il digest)

nelle slide del signature (verification) mancano dei Mod p

il professore dice che ElGamal ha dentro di se il preprocessing ed il postprocessing, cosa che manca in RSA textbook. Il professore ha anche detto che esistono implementazioni di rsa più rapidi che sfruttano un algoritmo cinese, ma ora non lo stiamo considerando

oggi non si usa [[ElGamal]], ed è anche difficile trovare qualche libreria che lo supporti.

elgamal è forte perché si basa sul [[Discrete Logarithm (DL) Problem]].

DSA
nonostante elgamal ha anche qualche metodo per garantire [[Confidentiality]] dsa ha solo roba per non repudition. 

a volte il professore inserisce all'esame un esercizio che chiede di calcolare apha in un specifico caso

ha finito di spiegare dss/dsa ed ora apre la VM:
creiamo e verifiamo una signature con openssl, osando rsa
- crea il file:
```bash
>>shuf -n 20 /usr/share/dict/words > file.txt
>>cat file.txt    
scissors-shaped
hunger-starve
indescribableness
aberroscope
Lise
hesitate
foveate
potamogale
overpay
Vorticella
strolls
ondograms
photoist
demoralised
appassionate
icterogenous
Topsy
ceintures
pulvino
upshoulder

```
- iniziamo creando la private key. dopo averla creata la private key, andrebbe criptata
	- poiché esistono vari algoritmi e  per ogni algorimo deve esserci uan private key, dobbiamo specificare la private key
```bash
>>openssl genpkey -algorithm RSA -aes-256-cbc -pkeyopt rsa_keygen_bits:4096 -out privkey.pem                       
..+...+...+.....+.......+..+.+......+...+..+....+.........+.....+......+.+.....+.+..+............+.............+.....+...+....+.....+.........+......+.+.....+.......+......+............+..+.+...........+...+......+.+.....+......+....+..............+.+...+......+..+.......+........+++++++++++++++++++++++++++++++++++++++++++++*....+.+........+.......+.....+....+......+.....+...+...+....+.....+....+.....+....+..+...+...............+.+..+...+....+...+...+.........+..+.........+......+.+........+.......+.........+.....+++++++++++++++++++++++++++++++++++++++++++++*..............+.+........+..........+......+............+..+.+..+.......+.....+.......+...+.......................+.............+.....+.+.........+++++
....+.......+...+++++++++++++++++++++++++++++++++++++++++++++*..+......+..+.+...........+......+.......+..+.+...........................+..+......+++++++++++++++++++++++++++++++++++++++++++++*....+...+.......+......+.....+.........+.+............+...........+....+.....+.+.........+.....+...+....+......+.....+.......+.....+......+.+.....+....+.........+...............+...+...+.........+..+...+.....................+.........+.+...........+..........+.....+...+............+.........+....+..+.+...............+..+...+.........+...+.+..+..........+...+....................+...................+..+...............+....+...........+.+...+......+...+.....+................+..+...+......+...................+..+............+..........+........+.......+...+.....+..................+.........+...+....+......+..+......................+.....+......+...+.......+...........................+...........+.+.........+.....+.......+...+..............+............+.+........+.+......+...+..+...+.........+...+....+.........+..+...............+....+...+..+..........+.....................+........+......+.........+....+....................+...+......................+.....+.......+......+.....+....+......+..+.......+.....................+..+............+.............+...+..+.............+...+.....+.......+...+......+.....+.............+...+........+....+.....+.+.............................+......+......+...+.............+..+...+....+...+.....+...+....+...........+...+..........+......+...+..+......+...+.+......+..+................+......+...............+........+.........................+.....+.+...........+................+..+..........+......+++++
Enter PEM pass phrase: 
Verifying - Enter PEM pass phrase:

>>cat privkey.pem 
-----BEGIN ENCRYPTED PRIVATE KEY-----
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
-----END ENCRYPTED PRIVATE KEY-----
```
se vogliamo vedere i dettagli della chiave:
```bash
>>openssl pkey -in privkey.pem -text -noout 
Enter pass phrase for privkey.pem:
Private-Key: (4096 bit, 2 primes)
modulus:
    00:9d:cb:04:82:f0:42:bb:63:bf:5e:3d:76:98:76:
    45:48:7d:ec:c0:36:c3:d6:d9:b8:28:47:45:53:af:
    f1:46:1b:71:4f:2a:d4:42:d5:c8:22:df:31:89:34:
    6b:96:29:fe:73:12:f3:06:fd:ec:2b:7c:c1:a2:4d:
    29:e1:3d:68:f5:46:98:d1:9e:35:78:20:66:29:1c:
    05:a3:54:29:6a:6d:9a:c9:bb:6f:7d:36:4a:bc:e6:
    6b:aa:96:ed:2e:c7:e1:b5:bc:ac:e0:d9:36:85:5a:
    ab:94:85:50:b2:19:e1:1b:16:be:1e:ea:e9:14:b5:
    6f:06:00:17:7b:63:ed:79:4f:5c:4c:9d:e6:7d:35:
    7e:49:e6:18:b6:5b:49:c0:22:7c:59:03:4b:cd:59:
    a2:b1:39:6b:72:bf:d1:58:81:fc:22:87:1b:83:d7:
    64:21:ee:dc:8b:ff:c8:76:76:91:2a:2d:0b:1b:c9:
    64:89:da:e7:c0:11:75:48:e7:23:18:23:80:64:49:
    c4:fa:d2:09:6c:53:6d:a7:07:bd:fb:a3:19:5d:15:
    58:5d:92:48:bc:93:24:fc:74:76:a6:5d:ea:0c:53:
    c2:db:d4:e3:60:85:d9:b9:11:4c:be:20:1b:35:c8:
    33:ec:41:9b:4a:e1:54:64:a6:fe:e6:6b:84:32:15:
    81:2c:93:b6:a0:eb:3e:e0:90:c1:8b:31:bc:72:65:
    b6:1c:6d:e2:a2:c6:68:78:30:d9:01:74:6d:80:12:
    23:f9:75:ad:73:f2:83:94:0f:82:ab:3c:95:73:1f:
    3b:99:d4:55:03:51:30:4b:da:29:76:7e:8d:3d:1d:
    b2:f9:f3:d9:4f:67:9e:c3:09:47:1b:a0:98:d8:9c:
    a6:b9:09:44:fd:30:86:5a:de:ff:09:6d:64:46:7c:
    e6:03:5d:12:a4:a0:f7:b0:c5:24:98:17:d7:c2:a8:
    d9:bb:1e:68:56:ec:7d:ce:7c:fe:08:89:94:b5:0b:
    f9:73:24:28:05:33:04:59:07:89:09:4c:ba:74:e8:
    c0:b3:52:09:88:86:e3:a2:0e:bf:cd:e6:44:66:87:
    13:ab:70:60:b1:95:8a:7f:2f:e7:22:bb:89:d8:06:
    c4:ab:4b:6b:42:b9:88:ff:4b:b8:92:48:80:68:28:
    42:34:b1:98:d5:31:bb:ea:a6:e0:57:7b:4a:f8:7f:
    67:ec:fb:c3:fe:9b:4b:2f:03:5e:37:a7:68:81:9b:
    ec:7f:f6:2d:f2:c2:a4:46:27:69:c5:d5:ec:fb:c5:
    39:19:7f:45:a8:62:51:35:90:67:56:b3:7b:1e:14:
    f3:56:d1:2f:6b:05:ad:49:6c:14:ec:c9:83:cb:41:
    e3:a7:33
publicExponent: 65537 (0x10001)
privateExponent:
    45:9f:8f:a5:0a:c8:17:10:e3:1e:7c:f6:38:3d:6f:
    42:96:35:81:76:68:a1:03:3d:eb:9f:ce:ea:27:26:
    c9:6d:50:68:c3:18:17:49:66:de:64:26:e2:48:5b:
    f4:4d:21:35:bb:35:ba:6f:0d:e6:fe:4c:1e:05:f8:
    25:a7:48:09:79:95:f2:5f:e1:6d:d8:b5:db:0b:bf:
    3d:1a:e4:8f:4e:3f:4f:25:c2:02:b8:92:ef:98:a8:
    07:04:43:31:32:06:d8:7e:a0:b5:31:82:8a:02:c0:
    d4:6e:a2:75:83:4f:bc:f9:22:f8:57:64:72:bb:bf:
    7a:21:4e:3b:26:93:60:c4:70:90:69:d7:8a:85:b0:
    ec:80:77:84:f6:f0:aa:b3:4c:b4:a5:ec:ab:76:12:
    80:2a:3a:cb:cd:f1:5c:21:36:94:31:93:25:70:43:
    81:69:78:ac:d9:36:a5:76:99:84:c7:8d:30:3c:83:
    7d:04:36:df:9b:94:69:8f:7a:ff:aa:a2:7b:1d:c5:
    a9:7a:45:a8:23:83:ad:80:90:06:59:27:d6:d7:95:
    3e:ec:4d:e5:ce:f3:31:e5:5d:78:f8:d5:4d:8d:23:
    dc:85:a9:b2:2c:3d:2e:18:81:09:1e:f7:82:9a:8c:
    b6:81:18:39:49:05:48:c8:1a:8e:a7:00:14:6d:42:
    aa:2c:26:e3:02:dc:a3:16:49:52:bd:47:9c:6b:81:
    b2:7b:7a:cb:dd:a1:fc:c3:ed:88:80:39:37:f4:ff:
    43:b4:41:c4:5c:3a:b4:f6:b6:11:2e:55:35:e6:d0:
    08:1e:4a:c5:03:fa:48:c1:89:d7:91:ec:bf:84:03:
    e4:77:6c:7d:07:87:63:5f:f4:e1:79:26:b8:4d:43:
    f9:6f:17:2e:5b:4d:3f:4f:7e:12:58:5d:30:71:e8:
    dc:f2:63:1f:f2:54:0b:35:71:d9:dc:ab:5e:2f:34:
    c7:d0:f2:bd:8b:ea:95:96:cd:84:76:56:86:a8:11:
    95:af:08:0d:1f:9d:7a:35:17:48:e1:c4:07:02:9d:
    c4:8b:3c:24:d3:82:b0:dc:f6:57:38:ea:bb:6a:c9:
    e1:c7:8c:46:84:2a:16:6c:2a:bf:d0:54:37:c4:bb:
    fd:00:c2:62:dd:16:8b:45:26:3a:ff:5c:b6:03:02:
    18:6d:5b:7f:5c:df:b6:23:0a:f0:11:9f:4b:a7:2f:
    83:4f:7d:bb:13:01:b9:a6:c7:93:06:ee:d1:c8:a3:
    c9:d3:42:bc:8a:ed:c1:31:94:e2:05:a5:aa:be:3a:
    5d:e0:1f:d4:b2:65:24:87:57:4e:d1:eb:b9:a5:98:
    81:8f:86:73:a7:46:d9:a8:00:9a:0a:59:53:71:90:
    06:d1
prime1:
    00:d0:04:12:81:3b:fa:a2:47:ee:b7:44:9f:d6:53:
    29:fe:c5:e3:fa:f2:30:91:29:e1:72:a9:6a:1c:5a:
    1f:a5:0c:fa:a9:d2:b3:91:81:15:2c:46:e0:44:39:
    34:47:b2:c7:d5:bd:d4:b6:ce:b6:73:1a:ab:4d:9d:
    32:0a:99:99:71:07:bd:49:5a:e8:cd:21:1b:34:60:
    1a:92:14:14:44:62:26:db:8b:72:cd:16:e5:63:96:
    7c:d7:93:ab:12:d9:11:71:57:79:6b:d4:b6:50:73:
    3e:39:53:48:f7:34:fc:04:6a:24:93:e7:90:10:d6:
    cf:16:85:b6:87:a4:ae:c1:e8:44:6a:85:40:d4:36:
    b5:6e:cc:cc:b9:df:bc:0f:e8:72:87:d7:a9:ab:c7:
    73:ba:b3:cd:7f:74:cf:b8:c5:d0:20:5f:6c:6f:0e:
    7c:8d:b7:5e:9c:9a:89:63:65:b5:1e:b8:6c:a0:88:
    fb:a4:aa:d9:9b:42:0a:9d:12:45:ff:85:a6:00:0e:
    cb:8e:4d:15:c5:05:75:5c:be:cb:89:2a:31:51:dc:
    34:41:62:c5:8c:6e:30:39:ff:89:d2:7e:b7:8c:1e:
    f2:0c:71:52:43:91:e4:d6:d8:95:d8:dd:bd:da:3e:
    2e:e4:a3:11:fd:4e:64:2c:1d:2c:44:11:68:a3:c7:
    fd:69
prime2:
    00:c2:31:24:8f:da:11:a5:e0:9f:a6:b8:81:2e:d8:
    26:a5:a2:8d:de:a5:ca:36:c8:7c:1f:ac:72:66:82:
    c3:b6:a3:ac:4d:aa:69:9e:cc:12:3b:34:69:43:a6:
    c9:88:0a:40:61:4f:86:76:ce:43:1d:44:02:16:74:
    0f:6e:5c:a1:18:c4:72:9a:29:a4:93:b5:0f:60:6e:
    02:21:98:75:63:32:f4:a0:fc:64:e0:b3:da:84:0e:
    75:2f:6b:1b:1c:d1:ea:77:75:d6:0b:f9:be:be:8d:
    f6:7d:fe:6e:50:ff:e5:69:af:a6:a0:bd:d2:cb:46:
    36:cd:7f:36:83:43:be:9c:68:ab:18:38:66:bd:64:
    8f:67:33:a1:db:21:8d:6a:8b:4a:7b:ea:0c:43:43:
    89:66:90:ad:16:87:e6:90:4e:6d:b2:03:cb:4b:0c:
    27:d8:ca:09:1a:ed:57:89:2d:48:2e:53:47:ad:39:
    3b:76:9d:d2:6f:a5:80:94:53:74:4d:c0:04:54:aa:
    b0:2c:0f:08:7d:10:2f:8c:b5:4e:f8:46:4a:e9:59:
    68:6c:b7:8f:6d:d7:25:54:19:6f:f2:e5:6e:a7:f2:
    da:e4:99:d8:c2:bd:84:d4:30:4c:d1:11:04:40:e2:
    b8:77:26:45:a1:26:65:90:c1:dd:29:32:34:0f:a2:
    40:3b
exponent1:
    00:c0:a8:f4:e6:a3:41:b8:69:fd:2b:da:b0:5b:96:
    3d:10:0e:02:e0:5a:ce:26:b4:ee:6c:ff:82:1a:ee:
    51:de:d1:8d:9c:1a:5d:5c:47:7c:ef:bc:59:5c:76:
    ca:f8:19:1a:c2:d9:86:19:26:8d:8f:40:45:26:a6:
    90:41:87:0f:b9:c3:5c:4a:83:9b:98:d9:af:d3:ab:
    ab:10:5e:ee:82:83:91:cf:c7:71:35:88:9e:3e:c5:
    93:ad:2a:c4:c8:b9:29:51:9b:9e:07:04:45:33:6f:
    f9:52:a8:d3:ac:ba:73:2c:37:8e:d7:3a:22:91:a6:
    12:b9:9e:70:77:63:4c:c4:a5:b6:30:1e:68:f3:e4:
    13:d8:a2:70:7f:3b:3c:78:53:67:38:6f:c3:63:29:
    61:03:ac:22:89:89:0c:16:eb:87:9f:64:22:0f:1e:
    10:b8:44:fc:a8:f8:ec:84:96:1f:d1:6b:28:98:eb:
    26:7e:d6:0a:a3:a4:e0:25:a8:56:12:9a:9b:2b:f4:
    88:0d:ad:51:9b:60:39:da:03:90:89:e2:fd:38:ff:
    45:9a:c5:bb:88:1c:4a:28:7d:88:0d:e0:75:69:9f:
    03:ba:08:7f:13:bc:1d:81:eb:a9:a5:e9:82:3c:8f:
    59:69:43:ab:96:bb:b3:45:b4:63:5a:4b:f1:69:b8:
    01:f9
exponent2:
    00:8f:83:a6:13:b2:03:ec:e5:4e:d7:f5:ef:72:e1:
    47:de:8d:7d:ef:97:f3:13:fd:a2:cd:fd:b2:26:54:
    69:b3:a6:ce:86:2f:75:13:68:99:e8:ab:59:48:28:
    11:34:ba:ee:cd:7b:ea:52:0f:29:c6:8d:26:45:d5:
    cc:39:b1:b7:55:08:89:f1:a8:e8:fa:48:8b:6e:a6:
    9e:68:99:b5:d7:74:27:1a:7a:ad:4a:eb:60:88:cb:
    ee:8a:f6:ca:f8:c7:a2:52:5b:01:af:a4:08:f5:e7:
    10:ce:18:a5:0a:b3:b3:a6:21:ac:31:8b:58:27:e6:
    62:46:08:c8:0e:c6:98:2e:1b:a4:a6:a7:b8:36:2c:
    05:57:2d:ef:66:75:2b:80:1c:25:15:e2:e8:e1:25:
    1e:7c:70:5b:9b:15:20:ae:71:67:dc:71:b5:62:67:
    3f:63:96:1c:98:8b:e3:6f:7b:c9:a6:82:e1:ac:01:
    6a:12:c5:9c:69:ea:94:56:0a:3f:1f:de:d2:d4:87:
    b8:df:36:d4:fd:28:63:1b:c8:3a:ee:7d:74:8b:74:
    0a:1a:9e:a6:1f:75:2b:1f:36:15:68:1b:6b:66:2f:
    b2:d9:d3:61:40:ba:b3:59:e5:c0:3f:9a:25:dc:96:
    31:e1:cc:a5:14:ed:bd:8d:f7:d8:2c:c3:ef:79:c6:
    5d:55
coefficient:
    66:51:e3:8f:c9:c6:ab:9e:b1:2c:88:a5:d2:0e:19:
    e7:f2:bd:22:af:92:be:a1:0f:6a:b5:10:81:82:13:
    fd:53:7b:1c:5d:da:ed:6c:79:b6:9f:82:04:72:41:
    45:46:dc:b3:08:b0:16:ac:4e:5a:57:1d:7e:7b:f0:
    b1:be:1e:42:8e:42:a5:ca:40:b4:75:20:c6:89:23:
    75:9e:c0:d9:f5:17:70:87:eb:74:22:b4:87:70:e9:
    01:6a:13:1f:f0:b2:ba:1d:6b:d8:25:86:a4:5c:cb:
    cd:0b:22:b0:e0:c0:8b:79:eb:58:89:bd:5d:0e:d9:
    b7:8a:86:f1:5b:84:c6:cc:ef:1c:08:28:83:84:8c:
    03:8c:db:0f:e5:6a:b1:c4:e0:68:27:f3:82:ce:83:
    f1:c1:bd:f8:f1:e7:0c:16:6d:24:a2:3d:4f:9b:2c:
    a4:a6:9d:ee:64:f4:76:57:7b:cf:8b:24:a1:1b:dd:
    95:5e:ca:31:f6:8d:86:b2:9e:33:7b:f5:db:54:b1:
    10:7b:50:4e:f5:1f:a7:3e:3e:47:5f:ba:9a:2e:2b:
    8a:d5:3a:4d:9b:85:16:92:84:ef:f9:69:21:9a:b1:
    4f:49:68:3d:65:65:32:65:2b:ba:ac:ce:14:ee:2e:
    60:1c:89:87:1c:4f:10:fa:ee:78:b9:94:5a:a9:76:
    80

```
- ora che abbiamo la private key, creiamo la public key:
```bash
>>openssl pkey -in privkey.pem -pubout -out pubkey.pem
Enter pass phrase for privkey.pem:

>>cat pubkey.pem 
-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAncsEgvBCu2O/Xj12mHZF
SH3swDbD1tm4KEdFU6/xRhtxTyrUQtXIIt8xiTRrlin+cxLzBv3sK3zBok0p4T1o
9UaY0Z41eCBmKRwFo1Qpam2aybtvfTZKvOZrqpbtLsfhtbys4Nk2hVqrlIVQshnh
Gxa+HurpFLVvBgAXe2PteU9cTJ3mfTV+SeYYtltJwCJ8WQNLzVmisTlrcr/RWIH8
Iocbg9dkIe7ci//IdnaRKi0LG8lkidrnwBF1SOcjGCOAZEnE+tIJbFNtpwe9+6MZ
XRVYXZJIvJMk/HR2pl3qDFPC29TjYIXZuRFMviAbNcgz7EGbSuFUZKb+5muEMhWB
LJO2oOs+4JDBizG8cmW2HG3iosZoeDDZAXRtgBIj+XWtc/KDlA+CqzyVcx87mdRV
A1EwS9opdn6NPR2y+fPZT2eewwlHG6CY2JymuQlE/TCGWt7/CW1kRnzmA10SpKD3
sMUkmBfXwqjZux5oVux9znz+CImUtQv5cyQoBTMEWQeJCUy6dOjAs1IJiIbjog6/
zeZEZocTq3BgsZWKfy/nIruJ2AbEq0trQrmI/0u4kkiAaChCNLGY1TG76qbgV3tK
+H9n7PvD/ptLLwNeN6dogZvsf/Yt8sKkRidpxdXs+8U5GX9FqGJRNZBnVrN7HhTz
VtEvawWtSWwU7MmDy0HjpzMCAwEAAQ==
-----END PUBLIC KEY-----

```
- ora possiamo firmare il nostro file.txt creando il file.txt.sig:
```bash
>>openssl dgst -sha256 -sign privkey.pem -out file.txt.sig file.txt
Enter pass phrase for privkey.pem:
whitesteps@whitesteps-light|25-11-20 16:12|:~/Documenti/otherStuff/testing
>>cat -v file.txt.sig
at^G4M-Y`^\M-0M-_M-l1M-sM-^@BfM-}FsM-^F3M-:M-JM-;M-^ZM-HM-^?J^FM-2M-,M-^H^HM-^U^S^CM--M--M-^R\*;M-'$^\M-HOaeM-^]^P^OM-_M-4M-e^\fwM-I^WM-^GM-tM-^?nS.%M-{M-?M-^EM-^UM-^KJM-b^U|1qM-:M-^?FM-%M-_M-z4fLaM-"M-X`,M-^IM-h7M-TM-^HM-SM-(M-_M-)^K^^^?gM-^L^UM-ZM- ^^^_<hM-^Q^SM-a^E^W^WM-tM-CdM-3%	yM-t^[^@SOM-EXM-~qM-EM$M-~hM-<M-*FM-\;M-.|M-^ZHWM-=M-B}M-p^DM-+M-ZQ]3M-Op
^X*M-1R=M-c^UM-P9^^u'M-PM-H^VM-{M-,1K^O4?^DM-,=,aM-^GM-t<cM-VK^SM-xZM-YM-D{M^D^Ui!M-RM-LoM-CM-ZM-XmM-yM-^ZM-Y6M-;M-wiM-H'EM-^Wc+M-^J^XM-4M-^ZM-Lo_^VEM-)^LM-|M-8^CM-^?M-wM-5M-^JM-v^^xN-M-U^Tu^?M-^B:M-^ZXM-)M-"^KO\M-}C^BM-*M-[GY^^+M-^Y^OM-6WM->M-XM-&M-^[M-|^MM- ;^NM-^^LM-^Z^U^^M-@M-jyM-Q0-&&+M-3cSb^Ra^LM-~^HM-I+M-lM-A^HM-qM-ETp^]^DXM-}M-+M-^?M-.J>#$M-2M-,GM-NK^@8M-^HM-X^VM-{M-bM-^E^GM-CvU^E6M-^A3M-^M-9kM-KN>^PM-^\\i.M-_M-;^?1M-vM-^O&M-.^K^OM-YM-1M-q^C!pCM-+M-h"OM-N^^M-"M-a<5M-&M-q^PM-+^Of7^RmM-^YM-jnM-dM- NM-*0=M-^M-YfnM-vM-PM-^T9CM-LM-'^S^OM-dM-=f*M-VS^GM-;M-FM-WM-DM-!NgZ739o^\M-^E4@^VMM-(^\M-/YM-V^Z^]XM-/M-`M-'M-^GM-%M-(s(OM-59M-^B^\M-^FM-KM-:YZ&0M-^X^UF^V^LM-XM-+a^Y7M-^TPM-wM-zM-;M-VCM-^DM-+^NM-&%gR^RM-LM-^MM-6sqM-^T7M-^EM-SM-yM-D2M-L6M-<M-n%    
```
- ed ora verifichiamo tutto:
```bash
>>openssl dgst -sha256 -verify pubkey.pem -signature file.txt.sig file.txt
Verified OK
```

il professore ha detto che in futuro ci chiederà (in un altro contesto) di applicare questa roba ed inoltre ha sottolineato anche il fatto che openssl è un po' rompiscatole con la sintassi.