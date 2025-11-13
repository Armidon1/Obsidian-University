last lesson [[6 CS  Lower Level - Authenticated Encryption]]
# Asymmetric encryption: the Diffie-Hellman intuition

So far, we have discussed symmetric encryption, where the same key is used for both encryption and decryption. Now, we shift to **asymmetric encryption**, where we use a pair of different keys.

The typical usage is different from symmetric encryption. While [[Symmetric Encryption]] is the workhorse for ensuring **[[Confidentiality]]** of large amounts of data (it's fast), [[Asymmetric Encryption]] is computationally "heavier" (slower). Its primary strengths lie in solving other critical problems, such as **key exchange** and **[[Authentication]]**.

## Reminder about the model

![[Pasted image 20251022151244.png]]

- If the encryption key $K_1$ is the same as the decryption key $K_2$ ($K_1 = K_2$), we have **symmetric encryption**.
    
- If $K_1 \neq K_2$, we have **asymmetric encryption**.
    

Remember: Encryption as a mechanism doesn't _only_ provide confidentiality. As we will see, it can also provide other critical security properties.

## Another Definition: Key Exchange

- **Key exchange** (or key establishment) is the process of establishing a shared symmetric key between two parties over an **insecure communication channel**.
    
    - This is the classic challenge in enabling private communication. If Alice and Bob want to talk securely using a fast symmetric cipher, they must first agree on a secret key. But how can they agree on that key if their only channel (e.g., the internet) is being watched by an adversary (Eve)?
        
- **Asymmetric cryptography** provides an elegant solution to this problem by enabling secure key exchange mechanisms.
    

## Public-Key Encryption

A primary application of asymmetric encryption ($K_1 \neq K_2$) is **[[Public-Key Encryption]]**. It's crucial to understand the relationship:

- [[Public-Key Encryption]] $\Rightarrow$ [[Asymmetric Encryption]]
    
- [[Asymmetric Encryption]] $\nRightarrow$ [[Public-Key Encryption]] (Asymmetric just means the keys are different; public-key is a specific system where one key is published).
    

**Main Purposes:**

1. **[[Integrity]] and [[Non-Repudiation]]:** Achieved through _digital signature_.
    
2. **Key Exchange:** Securely establishing a shared symmetric key. This is the main use case that enables **[[Confidentiality]]** for bulk data.
    

## Diffie and Hellman [1976] – “New Directions in Cryptography”

The revolutionary idea was to split the secret key `K` into two parts:

- A **Public Key ($K_{pub}$)**: Used for encryption. This key can (and must) be made public and shared with everyone.
    
- A **Private Key ($K_{priv}$):** Used for decryption. This key is kept completely secret by the owner (Bob).
    

This is the essence of public-key cryptography.

### Two Key Scenarios

**Scenario 1: Sending a Confidential Message (Enabling [[Confidentiality]])**

1. Alice wants to send a secret message to Bob.
    
2. Alice gets **Bob's public key ($K_{pub-Bob}$)** (which is available to everyone).
    
3. She encrypts the message using $K_{pub-Bob}$.
    
4. She sends the ciphertext to Bob.
    
5. Only Bob, who possesses the corresponding **Bob's private key ($K_{priv-Bob}$)**, can decrypt and read the message.
    

**Scenario 2: Signing a Message (Enabling [[Non-Repudiation]])**

1. Alice wants to send a message to everyone and _prove_ it came from her.
    
2. Alice "encrypts" (or more accurately, _signs_) the message using **her own private key ($K_{priv-Alice}$)**.
    
3. She sends the "signed" message out.
    
4. _Anyone_ can decrypt this message using **Alice's public key ($K_{pub-Alice}$)**.
    
5. **This provides no [[Confidentiality]]** (everyone can read it).
    
6. However, it proves that the message _must_ have come from Alice, because only she has the private key that could create a message decryptable with her public key. This provides **[[Authentication]]** and, even stronger, **[[Non-Repudiation]]** (Alice cannot later deny having sent it).
    

Combining the two:

We can use Scenario 1 to securely share a new symmetric key. Alice encrypts a new symmetric key $K_s$ using Bob's public key. Only Bob can decrypt it. Now, Alice and Bob share $K_s$ and can use it for fast, confidential symmetric encryption.

## Number of Keys: Symmetric vs. Asymmetric

Imagine a network of `n` spies who all need to communicate securely with each other.

![[Pasted image 20251022152451.png]]

- **Symmetric Encryption:**
    
    - Each _pair_ of spies needs one shared secret key.
        
    - Spy 1 needs `n-1` keys (one for Spy 2, Spy 3, ... Spy n).
        
    - Spy 2 needs `n-2` _new_ keys (he already has one for Spy 1).
        
    - ...
        
    - The total number of keys is $(n-1) + (n-2) + ... + 1 = \frac{n(n-1)}{2}$.
        
    - This is a **quadratic** number of keys (grows with $O(n^2)$). Managing 1000 spies would require ~500,000 keys.
        
- **Asymmetric Encryption:**
    
    - Each spy generates _one_ pair of keys (public/private).
        
    - They publish their public key in a directory.
        
    - The total number of key pairs is `n`.
        
    - This is a **linear** number of keys (grows with $O(n)$). Managing 1000 spies requires 1000 key pairs.
        

## “New Directions in Cryptography”

- The Diffie-Hellman paper [IEEE Transactions on Information Theory, vol. IT-22, Nov. 1976] generated enormous interest in crypto research.
    
    ```
    http://www-ee.stanford.edu/%7Ehellman/publications/24.pdf
    ```
    
- Diffie & Hellman produced the revolutionary _idea_ of public-key cryptography, but they did not have a practical implementation for it. (This came later with Merkle-Hellman and, most famously, **[[RSA]] - Rivest-Shamir-Adelman**).
    
- **However, in their '76 paper, Diffie & Hellman _did_ invent a practical method for KEY EXCHANGE over an insecure channel, a method that is still in use today.**
    

## Excerpt from the RSA Paper (1978)

This historical paper shows the immediate impact of Diffie & Hellman's idea.

> "A Method for Obtaining Digital Signatures and Public-Key Cryptosystems"
> 
> R.L. Rivest, A. Shamir, and L. Adleman, Communications of the ACM 21, 1978
> 
> https://people.csail.mit.edu/rivest/Rsapaper.pdf

> **_The era of electronic mail may soon be upon us_**; _we must ensure that two important properties of the current paper mail system are preserved: (a) messages are private, and (b) messages can be signed. We demonstrate in this paper how to build these capabilities into an electronic mail system._
> 
> _At the heart of our proposal is a new encryption method. This method provides an implementation of a public-key cryptosystem, an elegant concept invented by Diffie and Hellman [1]. Their article motivated our research, since they presented the concept but not any practical implementation of such a system..._

## Meaning of "Encryption" in Asymmetric Crypto

The term "encrypt" can be confusing as it has two distinct uses:

1. **Encryption for Confidentiality:**
    
    - Alice encrypts a message using **Bob's public key**.
        
    - _Who can encrypt?_ Anyone (the key is public).
        
    - _Who can decrypt?_ Only Bob (with his private key).
        
    - **Property:** **Confidentiality**.
        
2. **Encryption for Signing (Authentication):**
    
    - Alice encrypts (signs) a message using **Alice's private key**.
        
    - _Who can encrypt?_ Only Alice (the key is private).
        
    - _Who can decrypt?_ Everyone (with Alice's public key).
        
    - **Property:** No confidentiality, but provides **Authentication** and **Non-Repudiation**.
        

## Encryption Behaviour

- **Rule 1:** What is encrypted by a public key can be decrypted by the associated private key. (This is true for all public-key systems).
    
- **Rule 2:** What is encrypted by a private key can be decrypted by the associated public key.
    
    - This "perfect symmetry" is **true for RSA**, which is why it's so flexible.
        
    - This is _not_ true for all asymmetric systems.
        
- Because of this symmetry in RSA, the term "encryption" is often used loosely to mean both classic encryption (for confidentiality) and signing (for authentication).


---

vedi anche [[Prerequisiti RSA]], per capire meglio il motivo di tutto sto casino.

---
# Introduction to one-way functions

## 1. Foundational Concepts: One-Way Functions (OWFs)

Modern cryptography is built on the concept of "hard problems." These are formalized as **One-Way Functions (OWFs)**.

- **Simple Definition:** A function that is **easy to compute** in one direction (e.g., $f(x) = y$) but **computationally infeasible** (or "hard") to invert (e.g., given $y$, find an $x$ such that $f(x)=y$).
    
- **Cryptographic hash functions** (like [[SHA-2]]56) are a prime example of functions that behave like OWFs.
    

> [!One-Way Function]
> 
> A function $f: \{0,1\}^* \rightarrow \{0,1\}^*$ is called a one-way function ([[OWF]]) if it satisfies two properties:
> 
> 1. **Efficiently computable:**
>     
>     - There exists a deterministic polynomial-time algorithm (it's "easy" or "fast") that, given any input $x$, computes $f(x)$.
>         
> 2. **Hard to invert on average:**
>     
>     - For every probabilistic polynomial-time algorithm $A$ (an "attacker"), for every positive polynomial $p(\cdot)$, and for sufficiently large $n$:
>         
>         $$\Pr_{x \leftarrow \{0,1\}^n}[A(f(x)) \in f^{-1}(f(x))] < \frac{1}{p(n)}$$
>         
>     - In plain English: Any efficient (polynomial-time) attacker $A$, given an output $y = f(x)$ (where $x$ was chosen randomly), has only a negligible probability of finding _any_ valid input $x'$ that produces $y$.
>         

- **Do OWFs Exist?** This is a major **open problem** in computer science.
    
    - They are widely **conjectured to exist**.
        
    - **Theorem:** If a one-way function exists, then **P ≠ NP**.
        
    - Since it is strongly believed that P ≠ NP, it is also believed that OWFs exist.
        
- **Utility:** OWFs are the foundation for many cryptographic guarantees, including:
    
    - Cryptographic hashing
        
    - Secure key exchanges
        
    - Public-key cryptography
        
    - Random number generation
        

## 2. Candidate One-Way Functions

### Candidate 1: Integer Multiplication & Factoring

This problem is the basis for the **[[RSA]] algorithm**.

- **Easy Problem:** Given two large prime numbers, $p$ and $q$ (e.g., _n_ bits each), computing their product $N = pq$ is very easy (polynomial time). The result $N$ will have about _2n_ bits.
    
- **Hard Problem:** Given a large composite number $N$ (that is the product of two large primes), finding its prime factors ([[Factorize a Number]]) $p$ and $q$ is computationally infeasible. There is no known polynomial-time algorithm to do this on a classical computer.
    
    - _Note:_ Shor's algorithm _can_ factor in polynomial time, but it requires a large-scale, fault-tolerant **quantum computer** (which does not yet exist).
        
- **Question:** Can a public key system be based on this observation?
    
- **Answer:** Yes, absolutely. This is the core idea behind RSA.
    

![[Pasted image 20251023113341.png]]

### Candidate 2: The Discrete Logarithm (DL) Problem
[[Discrete Logarithm (DL) Problem]]

This problem is the basis for the **[[Diffie-Hellman Key Exchange]]** and the **[[ElGamal]]** encryption system.

- **Definition:** Let $G$ be a finite cyclic group with _n_ elements and $g$ be a generator of $G$.
    
- **Easy Problem:** Given $g$ and an integer $x$, it is easy (efficient) to compute $y = g^x$. This is **[[Modular Exponentiation]]**.
    
- **Hard Problem:** Given $y$ and $g$, it is computationally infeasible to find the integer $x$ that satisfies the equation $y = g^x$.
    
- **Terminology:** This $x$ is called the **discrete logarithm of $y$ to the base $g$**. Ma perché diciamo logaritmo discreto? Questa è un'ottima domanda di approfondimento che va al cuore della differenza tra la matematica "classica" e quella usata in crittografia.
	- La parola **"discreto"** viene usata per sottolineare che stiamo lavorando all'interno di un **insieme finito e specifico di numeri interi**, (come gli interi modulo p), e non sull'insieme **continuo** dei numeri reali. vedi qui un [[Logaritmo Discreto vs Logaritmo Standard#🧩 Logaritmo Discreto|Esempio di Logaritmo Discreto]]
    
- **Example (a common group):** The multiplicative group of integers modulo a prime $p$, $\mathbb{Z}^*_p$. The problem is:
    
    - Find $x$ given $y$, $g$, and $p$ in the equation: $y \equiv g^x \pmod p$
        
- **DL in $\mathbb{Z}^*_p$ as an [[OWF]]:**
    
    - The function $x \rightarrow g^x \pmod p$ is **easy** to compute.
        
    - The inverse function $y \rightarrow x$ is **believed to be hard**.
        
    - This provides a **computation-based** notion of security.
        

---

## 3. Essential Mathematical Tools

To implement these cryptographic systems, we need efficient algorithms for modular arithmetic.

### Modular Exponentiation (The "Easy" Problem)
[[Modular Exponentiation]]

This is the "easy" operation in [[Discrete Logarithm (DL) Problem]] (computing $y = g^x \pmod p$).

- Key Property: We can avoid gigantic intermediate numbers by applying the modulus at every step.
    
    (a ⋅ b) mod p = ((a mod p) ⋅ (b mod p)) mod p
    
    (See: https://en.wikipedia.org/wiki/Modular_arithmetic#Properties)
    
- Optimization ([[Euler's Theorem]]): If $p$ is prime and $b$ and $p$ are [[Coprime]]:
    
    $b^e \pmod p = (b \pmod p)^{e \pmod{\varphi(p)}} \pmod p$
    
    (where $\varphi(p) = p-1$ since $p$ is prime. This is also known as Fermat's Little Theorem)
    
    (See: https://en.wikipedia.org/wiki/Euler%27s_theorem)
    

#### Fast Modular Exponentiation (Algorithm)

We don't compute $g^x$ and _then_ take the modulus. We use **exponentiation by squaring** (or the binary method), applying the modulus at every partial step.

```C
/*
 * Computes (base^exp) % mod efficiently.
 */
long fastModExp(unsigned int base, unsigned int exp, long mod) {
    long result = 1;
    long b = base % mod; // Apply mod to base first

    while (exp > 0) {
        // If the last bit of exp is 1 (i.e., exp is odd)
        if (exp & 1)
            result = (result * b) % mod;
        
        // Square the base (and apply mod)
        b = (b * b) % mod;
        
        // Right-shift the exponent (divide by 2)
        exp >>= 1;
    }
    return result;
}
```

- **Efficiency:** This algorithm runs in $O(\log(x))$ multiplications. Since $x < p$, the overall complexity is $O(\log^3(p))$.
    

---

### The Extended Euclidean Algorithm (EEA)
[[Extended Euclidean Algorithm (EEA)]]

This tool is essential for **RSA key generation**. Specifically, it's used to find the private exponent $d$ from the public exponent $e$ and the [[Euler's totient function]] $\varphi(N)$.

- **Purpose:** To find the **[[Multiplicative Inverse]]** of a number in a modulus (e.g., find $x^{-1} \pmod y$).
    
- **Basis:** [[Bézout's identity]].
    
    - Given two non-zero integers $x$ and $y$, there exist signed integers $a$ and $b$ such that:
        
        $$ax + by = \gcd(x, y)$$
        
- **Finding the Inverse:**
    
    - If $x$ and $y$ are [[Coprime]] (their $\gcd(x,y) = 1$), the identity becomes:
        
        $$ax + by = 1$$
        
    - If we apply `mod y` to this equation:
        
        - $ax \equiv 1 - by \pmod y$
            
    - Since $by \equiv 0 \pmod y$, this simplifies to:
        
        - $ax \equiv 1 \pmod y$
            
    - This means $a$ is the **[[Multiplicative Inverse]] of $x$ modulo $y$** (i.e., $a \equiv x^{-1} \pmod y$).
        
    - Similarly, $b \equiv y^{-1} \pmod x$.
        

_Note_: For the exam, the professor wants the interpretation of [[Bézout's identity]] given a specific number, not just the algorithm itself. You must understand _what_ it is and _why_ it's used.

#### The EEA Algorithm (Pseudocode)

This algorithm finds the coefficients $a$ and $b$ (here called `x0` and `y0`) from Bézout's identity.

```C
/*
 * Returns (x0, y0) such that a*x0 + b*y0 = 1
 * We are typically looking for x0, which is the inverse of a mod b.
 */
function extendedEuclid(a, b) // In the identity, a=x and b=y
    // Assumes gcd(a, b) = 1 (so they are Coprime)
    x0 ← 1, y0 ← 0
    x1 ← 0, y1 ← 1

    while b ≠ 0
        q ← a div b
        (a, b) ← (b, a mod b)
        (x0, x1) ← (x1, x0 - q * x1)
        (y0, y1) ← (y1, y0 - q * y1)

    return (x0, y0) 
}
```
---
## 3. Protocol 1: Diffie-Hellman (DH) Key Exchange
[[Diffie-Hellman Key Exchange]]

The Diffie-Hellman (DH) protocol is a practical application of the **[[Discrete Logarithm (DL) Problem]]** designed to achieve a secure key exchange.

- **Goal:** To allow two parties (Alice and Bob), who initially share no secret information, to perform a protocol over a public (insecure) channel and jointly derive the **same shared secret key**.
    
- **Security:** An eavesdropper (Eve) who listens to the entire exchange cannot obtain this shared key in polynomial time.
    

---

### DH Procedure

1. **Public Parameters:** Alice and Bob first publicly agree on two large numbers:
    
    - A large prime $p$.
        
    - An element $g$, which is a generator of the multiplicative group $\mathbb{Z}^*_p$ (meaning $g^x \pmod p$ can generate all elements in the group).
        
    - _Note:_ For best security, $p$ should be a "safe prime," where $p = 2q + 1$ and $q$ is also prime. This $q$ is known as a Sophie Germain prime.
        
2. **Alice's Steps:**
    
    - Chooses a **private key** $a$ (a random secret number, $1 \le a \le p-1$).
        
    - Computes her **public key** $A = g^a \pmod p$.
        
    - Sends her public key $A$ to Bob over the insecure channel.
        
3. **Bob's Steps:**
    
    - Chooses his **private key** $b$ (a random secret number, $1 \le b \le p-1$).
        
    - Computes his **public key** $B = g^b \pmod p$.
        
    - Sends his public key $B$ to Alice over the insecure channel.
        
4. **Shared Secret Calculation:**
    
    - Alice receives $B$ and computes the secret:
        
        $K = B^a \pmod p = (g^b)^a \pmod p = g^{ab} \pmod p$.
        
    - Bob receives $A$ and computes the secret:
        
        $K = A^b \pmod p = (g^a)^b \pmod p = g^{ab} \pmod p$.
        

Both parties now possess the same **shared secret key $K = g^{ab} \pmod p$**.

An eavesdropper, Eve, only sees the public values: $g, p, A, B$.

- To find $K$, Eve would need to compute $g^{ab}$ from $g^a$ and $g^b$. This is the **Computational Diffie-Hellman (CDH) problem**, which is believed to be computationally hard.
    
- An even harder-sounding (but related) way would be to first solve the **Discrete Log problem** to find $a$ (from $A$) or $b$ (from $B$), which is also infeasible.
    

---

### DH Properties and Variants

#### Perfect Forward Secrecy (PFS)

- **Definition:** A cryptosystem has Perfect Forward Secrecy (PFS) if it generates **random, temporary public keys for each new session**.
    
- **Implication:** The compromise of a single key (e.g., a server's long-term private key) **does not compromise any _past_ or _future_ session keys**. If an attacker records all of today's encrypted traffic and _tomorrow_ steals the server's main key, they _still_ cannot decrypt today's traffic.
    

#### Types of DH

|**Feature**|**Static Diffie-Hellman**|**Ephemeral Diffie-Hellman (DHE/ECDHE)**|
|---|---|---|
|**Key Lifespan**|Uses a long-term, fixed key pair that remains the same across sessions (typically on the server side).|Generates a **new, temporary** key pair for **each** communication session.|
|**Mathematical Basis**|Modular exponentiation or elliptic curves.|Modular exponentiation or elliptic curves.|
|**Primary Security Property**|**LACKS Forward Secrecy.**|**PROVIDES Perfect Forward Secrecy.**|
|**Primary Use Case**|Specific scenarios where long-term key management is required.|The **standard** for modern secure communication (e.g., TLS 1.3).|

---

### DH Vulnerabilities

The "textbook" DH protocol described above is effective **only against a passive adversary (eavesdropper)**. It is critically vulnerable to an _active_ adversary.

|**Vulnerability**|**Description**|**Impact**|**Mitigation**|
|---|---|---|---|
|**Man-in-the-Middle (MitM)**|**No authentication** in basic DH. Alice has no proof she is talking to Bob, and vice-versa.|Attacker (Trent) intercepts and alters the key exchange, establishing separate secret keys with both Alice and Bob.|Use **Authenticated DH** (e.g., signing the public keys $A$ and $B$ with long-term X.509 certificates).|
|**Logjam Attack**|Exploits the use of small (e.g., 512-bit) or common/shared prime numbers ($p$).|Attacker breaks DH with massive precomputation against a single common prime.|Use $\ge$ 2048-bit unique, safe primes.|
|**Static DH Keys**|Reuse of long-term DH private keys.|**No Perfect Forward Secrecy.** A compromise of the static key reveals all past sessions.|Use **Ephemeral DH (DHE/ECDHE)**.|

#### The [[Man-in-the-Middle (MITM)]] Attack (Detailed)

An active attacker (Trent) sits in the middle of the communication channel:

1. **Alice $\rightarrow$ Trent:** Alice (thinking she's talking to Bob) sends her public key $A = g^a \pmod p$. Trent intercepts this.
    
2. **Trent $\rightarrow$ Bob:** Trent (pretending to be Alice) generates his _own_ secret key $t$ and sends his public key $T = g^t \pmod p$ to Bob.
    
3. **Bob $\rightarrow$ Trent:** Bob (thinking he's talking to Alice) sends his public key $B = g^b \pmod p$. Trent intercepts this.
    
4. **Trent $\rightarrow$ Alice:** Trent (pretending to be Bob) sends his public key $T = g^t \pmod p$ back to Alice.
    

**Attack Effects:**

- Alice computes a shared key with Trent:
    
    $K_{AT} = T^a \pmod p = (g^t)^a \pmod p = g^{ta} \pmod p$
    
- Bob computes a shared key with Trent:
    
    $K_{BT} = T^b \pmod p = (g^t)^b \pmod p = g^{tb} \pmod p$
    
- **Trent computes _both_ keys**:
    
    - To talk to Alice: $K_{TA} = A^t \pmod p = (g^a)^t \pmod p = g^{at} \pmod p$
        
    - To talk to Bob: $K_{TB} = B^t \pmod p = (g^b)^t \pmod p = g^{bt} \pmod p$
        

Alice and Bob believe they have a secure, private channel, but Trent is in the middle, intercepting every message, decrypting it with one key, reading/modifying it, and re-encrypting it with the other key. This violates confidentiality, integrity, [[Availability]], and all other security properties.

---

### Other DH Systems

The Diffie-Hellman concept can be used with any mathematical group, _except_ for those where the discrete logarithm problem is easy.

- For example, it **cannot** be used with the additive group of $\mathbb{Z}_p$ ($y \equiv g+x \pmod p$), because the "logarithm" (finding $x$) is just simple subtraction.
    

**[[ECDH]]:**

- A modern, highly efficient variant of Diffie-Hellman that uses the group of points on an **elliptic curve**.
    
- The math is different, but the protocol flow is identical.
    
- It provides the same level of security as traditional DH but with **much smaller keys** (e.g., a 256-bit ECDH key is roughly equivalent in strength to a 3072-bit DH key), making it much faster and more suitable for mobile devices.
    
- [https://en.wikipedia.org/wiki/Elliptic-curve_Diffie%E2%80%93Hellman](https://en.wikipedia.org/wiki/Elliptic-curve_Diffie%E2%80%93Hellman)

---

# RSA: Purposes of Encryption

RSA is a public-key cryptosystem that provides several key security services, which are achieved by using its two different keys (public and private) in different ways.

The core security services are:

- **[[Confidentiality]]:** Keeping data secret.
    
- **[[Authentication]]:** Proving who you are.
    
- **[[Integrity]]:** Ensuring data hasn't been altered.
	    
- **Key Exchange:** Securely sharing a secret key.
    
- **[[Non-Repudiation]]:** Creating undeniable proof that someone sent a message.
    

---

## RSA: Two Ways of Encrypting
[[RSA]]
Recall that in an asymmetric system, there are two keys: one **public** (which everyone knows) and one **private** (which only the owner knows).

RSA encryption behaves differently depending on _which key_ Alice uses to encrypt a block of data, M:

1. **Encrypting with Bob's Public Key:** Anyone can do this, as the key is public.
    
2. **Encrypting with Alice's Private Key:** Only Alice can do this, as she is the only one who has her private key.
    

---

## Effects of RSA Encryption

These two methods achieve completely different goals:

### 1. Encryption with a Public Key (Confidentiality)

- **Who can encrypt?** _Everybody_ can encrypt a message using Bob's public key.
    
- **Who can decrypt?** _Only Bob_, the owner of the corresponding private key, can decrypt the message.
    
- **Result:** This achieves **confidentiality**. It's used to send secret messages _to_ Bob.
    

### 2. Encryption with a Private Key (Authentication)

- **Who can encrypt?** _Only the owner_ (Alice) can encrypt a message with her own private key.
    
- **Who can decrypt?** _Everybody_ can decrypt the message using Alice's public key.
    
- **Result:** This provides **no confidentiality** at all. However, it proves that the message could _only_ have come from Alice. This is the foundation for **non-repudiation**.
    

---

## Non-Repudiation

- **Definition:** Non-repudiation is a strong guarantee that the sender of a message **cannot later deny having sent it**.
    
- It provides undeniable **proof of origin** and **proof of integrity**.
    
- This is typically achieved using a **digital signature**.
    

### Non-Repudiation vs. HMAC

It's important to understand why an [[HMAC]] (a symmetric-key MAC) does _not_ provide non-repudiation.

- An HMAC is created using a **shared secret key** known by both Alice and Bob.
    
- If Bob receives a message with a valid HMAC, he knows it came from _either_ Alice _or himself_.
    
- A judge cannot determine which of the two parties created the message, as both had the key. Therefore, Alice can "repudiate" (deny) sending it.
    
- With a private-key signature, only one person (the owner) has the key, making the signature undeniable.
    

---

## Summary of RSA Purposes

### Encryption with Public Key:

- **Goal:** **Confidentiality**.
    
- **Primary Use:** **Key Exchange**.
    
- **Why?**
    
    - RSA is **too slow** (inefficient) to encrypt long files or messages.
        
    - Symmetric ciphers (like AES) are thousands of times faster.
        
    - RSA has size limitations (the message must be a number smaller than $N$).
        
    - "Textbook" RSA is deterministic (encrypting "Attack" always yields the same ciphertext), which is insecure unless padding is used.
        
- **Practical Use ([[Hybrid Encryption]]):**
    
    1. Alice generates a new, random **symmetric key** (e.g., for AES).
        
    2. Alice encrypts her long message using AES (which is fast).
        
    3. Alice encrypts the _AES key_ using Bob's **RSA public key** (which is fast, as the key is small).
        
    4. Alice sends the encrypted message + the RSA-encrypted key to Bob.
        

### Encryption with Private Key:

- **Goal:** **Integrity**, **Authenticity**, and **Non-Repudiation**.
    
- This is not just encryption; it's a **verification** process, similar to checking a MAC. The public can decrypt the message to verify it was originated by the owner of the private key.
    

---

## The Problem: Non-Repudiation and Forgery

Using private-key encryption directly is **not secure** and does not yet provide true non-repudiation. It is vulnerable to an **existential forgery** attack.

### The Naive (Insecure) Signature

- Let $U$ be Alice's public key and $V$ be Alice's private key.
    
- **Naive Signature Process:** Alice sends the pair $(M, S)$, where $S = E_V(M)$ (the message $M$ encrypted with her private key).
    
- **Naive Verification Process:** Bob receives $(M, S)$ and checks if $E_U(S) = M$ (decrypting the signature $S$ with her public key should reveal the original $M$).
    

### The Existential Forgery Attack
[[Existential Forgery (E)]]
An attacker, Fran, can forge a "valid" signed message _from scratch_ without Alice's private key.

1. Fran (the attacker) creates a random binary file, $R$. This $R$ will be his _signature_.
    
2. Fran computes $D = E_U(R)$ (i.e., he "decrypts" $R$ using Alice's **public key**).
    
3. Fran (pretending to be Alice) sends the pair $(D, R)$ to Bob.
    
4. Bob receives the message $D$ and the signature $R$. He performs the verification:
    
    - Bob checks: Does $E_U(R)$ equal $D$?
        
    - Yes, by definition! Fran _created_ $D$ to be $E_U(R)$.
        
5. Bob accepts the pair $(D, R)$ as a valid message and signature from Alice, even though $D$ is probably meaningless. The existential forgery is successful.
    

---

## The Solution: RSA Digital Signature (Hash-then-Sign)

The vulnerability is fixed by **signing a hash of the message**, not the message itself.

- **Signature Process:** Alice sends the pair $(M, S)$, where $H$ is a cryptographic hash function (like SHA-256) and $S = E_V(H(M))$.
    
    - She hashes the message $M$ to get a small, fixed-size digest $h$.
        
    - She encrypts (signs) the hash $h$ with her private key $V$.
        
- **Verification Process:**
    
    1. Bob receives the pair $(M, S)$.
        
    2. Bob computes $h_1 = H(M)$ (he hashes the plaintext message himself).
        
    3. Bob computes $h_2 = E_U(S)$ (he decrypts the signature $S$ with Alice's public key).
        
    4. If $h_1 = h_2$, the signature is **valid**. If not, it is rejected.
        
- **Why this works:**
    
    - The hash function $H$ is a **One-Way Function ([[OWF]])**, which makes the [[Forgery]] attack impossible. Fran cannot find a message $D$ that hashes to $R$.
        
    - Encrypting a hash is fast and efficient.
        
    - $H$ guarantees **data [[Integrity]]** (if $M$ is changed, $h_1$ changes).
        
    - $E_V$ guarantees **[[Authenticity]]** (only Alice could have created $h_2$).
        

---

## "Textbook" RSA: Common Weaknesses & Attacks

The basic, "textbook" RSA algorithm ($C = M^e \pmod N$) is dangerously insecure. Practical RSA implementations _must_ include mitigations, primarily **padding**.

### 1. Factoring $N$

- **Attack:** If an attacker can factor $N$ into $p$ and $q$, they can compute $\varphi(N)$ and then use $e$ to find the private key $d$. Factoring $N$ breaks RSA.
    
- **Open Problem:** We know (Factoring $N$) $\implies$ (Break RSA). Is the reverse true? (Break RSA) $\implies$ (Factoring $N$)? This is not known.
    
- **Solution:** Use proper key generation:
    
    - $p$ and $q$ must be **large enough** (e.g., $N$ should be 2048 or 4096 bits).
        
    - $p$ and $q$ must **not be too close** together.
        
    - $(p-1)$ and $(q-1)$ must have large prime factors (to foil Pollard's p-1 algorithm).
        
- **Historical Context:** Factoring challenges have shown the difficulty. RSA-640 (bits) was factored in 2005. In 2008, the Gpcode ransomware used a 1024-bit key, and Kaspersky Labs estimated it would take 15 million modern computers 1 year to break. The key was never broken, proving the practical strength of 1024-bit keys at the time.
    

### 2. Attacks on Easy or Small Messages

- **Problem 1:** If $m = 0$, $1$, or $N-1$, then $RSA(m) = m$. The ciphertext is the same as the plaintext.
    
    - **Solution:** Use a "salt" or padding.
        
- **Problem 2:** If both $m$ and $e$ are small (e.g., $e = 3$) and $m$ is small, we might have $m^e < N$.
    
    - In this case, $C = m^e \pmod N = m^e$.
        
    - The attacker doesn't need to do modular arithmetic; they just compute the simple $e$-th root of $C$ to find $m$.
        
    - **Solution:** Add non-zero padding to _all_ messages to ensure $m$ is never small.
        

### 3. Low-Exponent Attacks ($e=3$)

- **Problem 1 (Related Messages):** If an attacker intercepts two messages related by a known transformation, e.g., $c_1 = m^3 \pmod n$ and $c_2 = (m+1)^3 \pmod n$, they can use this algebraic relationship (the Coppersmith attack) to solve for $m$.
    
    - **Solution:** Choose a large $e$ (like 65537) or use padding.
        
- **Problem 2 (Chinese Remainder Theorem Attack):** If the _same message_ $m$ is sent to 3 different users (with $e=3$ and different moduli $n_1, n_2, n_3$), an attacker intercepts:
    
    1. $c_1 = m^3 \pmod{n_1}$
        
    2. $c_2 = m^3 \pmod{n_2}$
        
    3. $c_3 = m^3 \pmod{n_3}$
        
    
    - Using the Chinese Remainder Theorem (CRT), the attacker can combine these to find the value of $m^3 \pmod{n_1n_2n_3}$.
        
    - Since $m < n_i$ for all $i$, $m^3$ will be smaller than the product $n_1n_2n_3$. The result is simply $m^3$.
        
    - The attacker computes the simple cube root and finds $m$.
        
    - **Solution:** Add random padding to every message. This ensures the _same_ message is never sent twice.
        

### 4. Deterministic Encryption Attack

- **Problem:** "Textbook" RSA is deterministic. If an attacker knows the message is either $m_1$ ("YES") or $m_2$ ("NO"), they can encrypt both $m_1$ and $m_2$ with the public key. They compare the results to the intercepted ciphertext to learn the message.
    
- **Solution:** Add a random string (padding) to the message.
    

### 5. Common Modulus Attack

- **Problem:** If two users are set up with the _same modulus $n$_ (but different $e$ and $d$), this is catastrophic.
    
- User 1 (with $e_1, d_1, n$) could use their keys to figure out $p$ and $q$ (this is tricky but possible).
    
- Once they have $p$ and $q$, they can compute $\varphi(N)$ and use it to find User 2's private key $d_2$ from their public key $e_2$.
    
- **Solution:** Each person must generate their own unique $N$.
    

---

## Other Attacks on RSA

Besides the basic factorization attack, there are many other ways to attack an RSA implementation, especially if it follows the "textbook" definition without proper padding.

- **Factoring Attacks:** The most direct mathematical attack. If an attacker can factor the modulus $N$ into its prime components $p$ and $q$, they can compute the private key $d$.
    
- **Low Exponent Attacks:** Using a small public exponent (like $e=3$) can make RSA vulnerable if the same message is sent to multiple recipients (e.g., Håstad's broadcast attack) or if the message is small.
    
- **Common Modulus Attack:** If the same modulus $N$ is used by different users (with different $(e,d)$ pairs), one user can potentially use their knowledge to factor $N$ or decrypt messages sent to others.
    
- **Small Prime Attack:** If one of the primes ($p$ or $q$) is too small, it can be easily found by trial division or other factorization methods.
    
- **Side-Channel Attacks:** These attacks don't break the math but exploit the physical implementation.
    
    - **Timing Attacks:** By measuring precisely how long decryption takes, an attacker might be able to deduce bits of the private key $d$.
        
    - **Energy/Power Analysis Attacks:** Measuring the power consumption of a device (like a smart card) during decryption can leak information about the private key.
        
- **Fault-Injection Attacks:** Deliberately causing errors during the cryptographic computation (e.g., by fluctuating voltage or temperature) can sometimes cause the device to output corrupted data that reveals secret information.
    

---

### Multiplicative Property and Malleability

In cryptography, a function $f$ is said to have a multiplicative homomorphism (or simply be multiplicative) if:

$$f(m_1 \cdot m_2) \equiv f(m_1) \cdot f(m_2) \pmod n$$

This is true for "textbook" RSA encryption:

$$RSA(m_1 \cdot m_2) = (m_1 \cdot m_2)^e \pmod N = (m_1^e \cdot m_2^e) \pmod N = RSA(m_1) \cdot RSA(m_2) \pmod N$$

- This property makes RSA **malleable**. Malleability means an attacker can modify a ciphertext into another valid ciphertext for a related plaintext, without knowing either plaintext.
    
- For example, if an attacker has ciphertext $C = M^e \pmod N$, they can easily create a ciphertext for $2M$ by computing $C' = C \cdot 2^e \pmod N$. The receiver will decrypt $C'$ as $2M$, potentially tricking them into accepting a modified message.
    

---

### Attacks on RSA: Exploiting Malleability

The multiplicative property can be generalized:

If $M = M_1 \cdot M_2 \cdot \dots \cdot M_k$, then:

$$RSA(M) = RSA(M_1) \cdot RSA(M_2) \cdot \dots \cdot RSA(M_k) \pmod N$$

This allows an adversary to construct ciphertexts for composite messages if they know the ciphertexts for their components.

**Solution:** Always use a secure **padding scheme** (like OAEP) before encrypting. Padding destroys this multiplicative structure, making the encryption non-malleable.

---

### Chosen Ciphertext Attack (CCA) Example

An adversary wants to decrypt a target ciphertext $C = M^e \pmod N$.

1. The adversary computes a new ciphertext $X$ by multiplying $C$ with the encryption of a chosen number (e.g., $2$):
    
    $$X = (C \cdot 2^e) \pmod N$$
    
2. The adversary sends $X$ to the victim (or a decryption oracle) and asks them to decrypt it. The victim might be tricked into doing this if $X$ looks like a different, valid message.
    
3. The victim decrypts $X$ and returns the result $Y$:
    
    $$Y = X^d \pmod N = (C \cdot 2^e)^d \pmod N = (C^d \cdot (2^e)^d) \pmod N$$
    
    Since $C^d = M$ and $(2^e)^d = 2^{ed} \equiv 2^1 \pmod N$, we get:
    
    $$Y = M \cdot 2 \pmod N$$
    
4. The adversary now has $Y = 2M$. They can easily recover the original message $M$ by computing:
    
    $$M = Y \cdot 2^{-1} \pmod N$$
    
    (where $2^{-1}$ is the modular multiplicative inverse of 2 modulo $N$).
    

---

### Chosen Ciphertext Attack (General)

This is a more general version of the attack above.

Assume an attacker $T$ knows a target ciphertext $c = M^e \pmod N$.

1. $T$ randomly chooses a value $X$.
    
2. $T$ computes a new ciphertext $c' = c \cdot X^e \pmod N$.
    
3. $T$ asks the decryption oracle to decrypt $c'$.
    
4. The oracle returns the plaintext $M' = (c')^d \pmod N$.
    
5. $T$ can now compute the original message $M$:
    
    $$M' = (c')^d = (c \cdot X^e)^d = c^d \cdot (X^e)^d = M \cdot X \pmod N$$
    
    So, $M = M' \cdot X^{-1} \pmod N$.
    

**Solution:** The decryption process must rigorously **verify the structure** of the decrypted message before returning it. If a secure padding scheme (like OAEP) is used, the decrypted message $M'$ will likely have invalid padding, and the oracle will return an error instead of the raw plaintext, thwarting the attack.

---

### Implementation Attacks (Side-Channel)

These attacks don't break the mathematics of RSA but exploit weaknesses in how it is implemented on real hardware.

- **Timing Attacks:** The time it takes to perform the modular exponentiation $C^d \pmod N$ can depend on the specific bits of the private key $d$ (e.g., a '1' bit might take longer to process than a '0' bit due to an extra multiplication step). By measuring these minute differences over many decryptions, an attacker can recover $d$.
    
- **Energy/Power Analysis:** Similar to timing, the amount of power consumed by a processor (like in a smart card) can vary depending on the operation being performed. Differential Power Analysis (DPA) can be used to extract the key.
    
- **Solution:** Use **constant-time implementations** where every decryption takes the same amount of time regardless of the key or input. Another technique is **blinding**, where random values are introduced into the computation to mask the actual inputs, and then removed at the end.
    

---

## RSA - Attacks: Conclusion

- **"Textbook" RSA implementation is NOT safe.** It does not satisfy modern security criteria (like indistinguishability under chosen ciphertext attack, IND-CCA).
    
- It is vulnerable to many mathematical and implementation attacks due to its deterministic nature and malleability.
    
- **Standard Version:** In practice, RSA is always used with a padding scheme. The message $M$ is preprocessed into a padded message $M'$ before encryption.
    
    - $C = (M')^e \pmod N$
        
    - Since $M'$ contains random data (from the padding scheme), the encryption becomes probabilistic and non-malleable.
        

---

### PKCS: The Standard for Padding

**PKCS** stands for **Public-Key Cryptography Standards**. These are a set of standards developed by RSA Laboratories to ensure the secure implementation and interoperability of public-key crypto.

| **Standard** | **Title**                     | **Function / Description**                                                                                                                                                       |
| ------------ | ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **PKCS #1**  | **RSA Cryptography Standard** | Defines the correct formats for **RSA encryption** and **signatures**, including the crucial **padding schemes** (like OAEP and PSS) needed to stop the attacks described above. |
| **PKCS #3**  | Diffie-Hellman Key Agreement  | Defines the DH key exchange format. (Now largely obsolete and replaced by IETF standards).                                                                                       |
| **PKCS #5**  | Password-Based Cryptography   | Defines key derivation functions (PBKDF1, PBKDF2) to turn passwords into cryptographic keys.                                                                                     |
| **PKCS #6**  | Extended Certificate Syntax   | Defines certificate extensions. (Obsolete, superseded by X.509v3).                                                                                                               |
### Part 5: The Solution - PKCS (Public-Key Cryptography Standards)

**Conclusion: Textbook RSA is NOT safe.**

To be secure, RSA must be used with a **padding scheme**. The standards for this are defined by **PKCS**.

#### PKCS #1 (Old Version)

This standard defined a padding scheme for encryption:

m = 0x00 || 0x02 || [at least 8 non-zero random bytes] || 0x00 || M

- `0x00` (first byte): Ensures the resulting number is $< N$.
    
- `0x02`: Denotes encryption (0x01 was used for signatures).
    
- `Random bytes`: This is the padding that solves most of RSA's weaknesses. It makes the encryption non-deterministic and prevents attacks on small or related messages.
    

#### Overview of PKCS Standards

These standards, developed by RSA Laboratories, define formats for secure public-key cryptography.

| **Standard** | **Title**                                | **Function / Description**                                          | **Status / Adoption**                       |
| ------------ | ---------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------- |
| **PKCS #1**  | RSA Cryptography Standard                | RSA encryption, signatures, and padding (like OAEP, PSS).           | Widely used; parts adopted in **RFC 8017**. |
| **PKCS #3**  | Diffie-Hellman Key Agreement             | Diffie–Hellman key exchange format.                                 | Obsolete; replaced by IETF standards.       |
| **PKCS #5**  | Password-Based Cryptography              | Defines [[PBKDF1]], [[PBKDF2]] (key derivation).                    | Widely used; part of **RFC 8018**.          |
| **PKCS #6**  | Extended Certificate Syntax              | Defines certificate extensions.                                     | Obsolete; superseded by **X.509v3**.        |
| **PKCS #7**  | Cryptographic Message Syntax             | Format for signed/enveloped data ([[S-MIME\|S\MIME]]).              | Superseded by CMS (**RFC 5652**).           |
| **PKCS #8**  | Private Key Information Syntax           | Standard for storing private keys (encrypted or not).               | Widely used (OpenSSL, Java).                |
| **PKCS #9**  | Selected Attribute Types                 | Defines attributes for use in other PKCS standards.                 | Still relevant.                             |
| **PKCS #10** | Certificate Request Syntax               | Format for Certificate Signing Requests (CSRs).                     | Ubiquitous in TLS/PKI.                      |
| **PKCS #11** | Cryptographic Token Interface (Cryptoki) | API for interacting with cryptographic hardware (HSMs, smartcards). | Actively maintained by OASIS.               |
| **PKCS #12** | Personal Information Exchange Syntax     | Container for certs & private keys (.p12, .pfx files).              | Still widely used (Windows, browsers).      |
| **PKCS #15** | Cryptographic Token Information Format   | Format for storing crypto objects on tokens.                        | Used in smartcard infrastructure.           |
there is also PKCS#13 which talks about Elliptic Curve Cryptography, which allows to gain the exact same security of a one 1 million bits of key with simply one thousand bits and this helps a lot with [[Performance]]. 


---
## An Overview of PKCS (Part 2)

The **Public-Key Cryptography Standards (PKCS)** were a series of standards developed by RSA Laboratories to ensure **interoperability** across vendors for cryptographic operations. While many have since been superseded or integrated into IETF RFCs (Request for Comments), they formed the foundational basis for many security protocols in use today.

Here is an overview of several key standards from the collection.

---

## PKCS #3 — Diffie-Hellman Key Agreement

- **Purpose:** To standardize the **Diffie-Hellman (DH) key exchange**.
    
- **Mechanism:** It defined the parameters and encoding for the DH protocol, where two parties each generate a public/private key pair and use them to compute a shared secret ($g^{ab} \pmod p$). This shared secret is then used to derive symmetric session keys.
    
- **Status & Context:**
    
    - **Obsolete.** This standard is historically important as the first to standardize DH, but it has been superseded by more robust IETF standards like **RFC 2631** (which references ANSI X9.42).
        
    - Modern DH parameter definitions (e.g., specific prime groups) are defined in standards like **RFC 3526**.
        
- **Applications:** It was a foundational component for protocols like legacy TLS (now deprecated) and IPsec (which still uses DH "groups" for key agreement).
    

---

## PKCS #5 — Password-Based Encryption (PBE)

- **Purpose (Motivation):** Solves a core human problem: users remember **passwords** (which have low entropy and are often weak), not long cryptographic keys (which have high entropy). PKCS #5 provides a secure method to **derive a strong key from a weak password**.
    
- **Mechanism (Key Derivation):**
    
    - It specifies **Password-Based Key Derivation Functions (PBKDFs)**.
        
    - **[[PBKDF1]]** (legacy) and **[[PBKDF2]]** (the modern standard) are the most famous.
        
    - [[PBKDF2]] "stretches" a password by mixing it with a **Salt** (a unique random value) and running it through a pseudorandom function (like HMAC-SHA256) thousands of times (the **iteration count**).
        
    - **Function:** `Derived Key = PBKDF2(password, salt, iterations, output_key_length)`
        
    - This process is _deliberately slow_ to make brute-force attacks against the password computationally infeasible. Modern KDFs like `bcrypt`, `scrypt`, and `Argon2` build on this same concept.
        
- **Applications:**
    
    - **Wi-Fi Security:** WPA/WPA2 use PBKDF2 to derive the network encryption key from the Wi-Fi password.
        
    - **Password Managers:** Used to encrypt your password vault (e.g., KeePass, 1Password).
        
    - **Disk Encryption:** Used to derive the key that unlocks an encrypted hard drive.
        
    - **PKCS #12:** Used to password-protect private key files.
        

---

## PKCS #8 — Private Key Information Syntax

- **Purpose:** A standard syntax (using ASN.1) for **storing private key information**. It provides a common format that different systems and software (like OpenSSL, Java, .NET) can all understand.
    
- **Structure:** It defines two main structures:
    
    1. **`PrivateKeyInfo`:** An unencrypted container that holds the key type (RSA, EC, etc.) and the key data itself (the `OCTET STRING`).
        
    2. **`EncryptedPrivateKeyInfo`:** A container for an _encrypted_ private key. It specifies the encryption algorithm (typically a PBE from **PKCS #5**) and the encrypted key data.
        
- **Applications:**
    
    - This is the format you see in **PEM files** used for TLS/HTTPS:
        
        - `-----BEGIN PRIVATE KEY-----` (Unencrypted PKCS #8)
            
        - `-----BEGIN ENCRYPTED PRIVATE KEY-----` (Encrypted PKCS #8, protected with a password)
            
    - Essential for secure key storage and interoperability in all modern PKI systems.
        

---

## PKCS #9 — Selected Attribute Types

- **Purpose:** Provides **extensibility** for other PKCS standards. It is not a protocol itself, but a _library of definitions_ for "attributes" that can be attached to objects like certificates or private keys. The attributes are like additional informations. 
    
- **Examples of Attributes:**
    
    - `emailAddress`
        
    - `unstructuredName`
        
    - `challengePassword` (a password used in a PKCS #10 Certificate Signing Request (CSR) to authenticate a renewal or revocation request).
        
    - It also allows for custom attributes via **Object Identifiers (OIDs)**.
        
- **Applications:** Used to provide richer identity information inside X.509 certificates and PKCS #10 CSRs.
    

---

## PKCS #11 — Cryptographic Token Interface (Cryptoki)

- **Purpose:** This is a standard **C-language API** (Application Programming Interface), not a file format. It provides a vendor-independent way for software to _talk to_ hardware cryptography devices.
    
- **Key Concepts (Architecture):**
    
    - **HSM (Hardware Security Module):** The physical or cloud device that protects keys.
        
    - **Cryptoki (Crypto Key API):** The "driver" or interface software.
        
    - **Slot:** An interface or reader (e.g., a smart card reader, a USB port).
        
    - **Token:** The cryptographic device itself (e.g., a smart card, a USB token).
        
    - **Session:** An active connection between the application and the token.
        
    - **Objects:** The keys, certificates, or data stored on the token. Keys are often marked as "non-exportable," meaning they can be _used_ but never _extracted_.
        
- **Applications:**
    
    - Enterprise PKI (using HSMs to protect root CAs).
        
    - Smart card logins for operating systems.
        
    - Securely performing digital signatures or TLS termination (the web server talks to the HSM via PKCS #11 to sign data).
        
    - Cloud HSMs (e.g., in AWS, Azure) present a PKCS #11 interface.
        

---

## PKCS #12 — Personal Information Exchange Syntax

- **Purpose:** Defines a **container format** (a single file) to bundle related cryptographic information together. It is commonly known by its file extensions: **.pfx** or **.p12**.
    
- **Structure:** A PKCS #12 file is a "digital suitcase" that typically contains:
    
    1. A **Private Key** (which is itself usually encrypted using PKCS #5 PBE).
        
    2. The corresponding **Public Key Certificate** (X.509).
        
    3. The "chain of trust": any intermediate and root certificates.
        
- **Usage:**
    
    - **Backup and Transport:** This is the most common way to **export** a certificate and its private key from one server and **import** it onto another (e.g., when moving a website to a new server).
        
    - Used by browsers, operating systems, and VPN/Email clients to import user credentials and Windows.
        

---

## PKCS #15 — Cryptographic Token Information Format

- **Purpose:** This standard defines the **file system format** _on_ a cryptographic token. It ensures that a token (like a national eID card) from one vendor can be understood and used by software from another vendor.
    
- **PKCS #11 vs. PKCS #15 (The Key Distinction):**
    
    - **PKCS #15 (Storage):** This is _how data is structured_ on the token (e.g., the directory structure, file names, and access control rules).
        
    - **PKCS #11 (Access):** This is the _API used by an application_ to read, write, and use the objects stored in the PKCS #15 format.
        
- **Applications:**
    
    - National eID cards.
        
    - Digital passports.
        
    - Healthcare cards.
        
    - Enterprise access cards.


---
DA SCHEMATIZZARE ANCORA NEL CANVAS
# RSA Implementation

This section covers the practical steps required to implement the RSA algorithm, from key generation to the secure encryption and decryption process.

The core "textbook" algorithm involves two main formulas:

- **Encryption (Public Key):** $c = m^e \pmod n$
    
- **Decryption (Private Key):** $m = c^d \pmod n$
    

However, a secure _implementation_ requires several more steps to be safe against attacks.

## Key Properties (Recap)

- **Uniqueness:** The requirement that $\gcd(e, \phi(n)) = 1$ is crucial. It ensures that $e$ has a unique modular multiplicative inverse $d$, which is necessary for decryption to work.
    
- **The RSA Assumption:** Finding the private key $d$ is computationally _easy_ if you know the prime factors $p$ and $q$. However, finding $d$ given only the public key $(n, e)$ is assumed to be computationally _hard_. This is the core assumption RSA's security relies on.
    
- **Public Exponent (e):** The public exponent $e$ is _chosen_, not calculated. It can be small to make encryption fast.
    
    - A common value is **$e=3$**, but this is **problematic** as it is vulnerable to specific attacks (like small-message attacks or broadcast attacks) if not implemented with proper padding.
        
    - The most common and recommended value is **$e = 65537$** (which is $2^{16}+1$).
        
- **Performance:** Encryption and decryption both involve modular exponentiation.
    
    - **Encryption** is generally _fast_ because $e$ is chosen to be small.
        
    - **Decryption** is significantly _slower_ because the private exponent $d$ is calculated, is typically very large (on the same order of magnitude as $n$), and cannot be optimized in the same way.
        

## Constructing an RSA Key Pair (Alice's Job)

Here is the step-by-step process for generating the public and private keys:

1. **Generate Primes:** Alice randomly chooses two distinct, very large prime numbers, $p$ and $q$. These must be cryptographically random so an attacker cannot guess them.
    
2. **Compute Modulus:** Alice computes the modulus $n$ by multiplying the primes: $n = p \cdot q$.
    
3. **Compute Totient:** Alice computes Euler's totient function $\phi(n)$: $\phi(n) = (p-1)(q-1)$.
    
4. **Choose Public Exponent:** Alice _chooses_ a public exponent $e$ (e.g., 65537) that is coprime to $\phi(n)$. This means $\gcd(e, \phi(n)) = 1$.
    
5. **Compute Private Exponent:** Alice _calculates_ the private exponent $d$ by finding the modular multiplicative inverse of $e$ modulo $\phi(n)$. This is the value that satisfies the equation: $d \cdot e \equiv 1 \pmod{\phi(N)}$.
    
6. **Publish/Keep Keys:**
    
    - **Public Key:** Alice publishes $(n, e)$. This is shared with the world.
        
    - **Private Key:** Alice keeps $(n, d)$ secret.
        
    - **Crucial Secret:** Alice must also keep $p$, $q$, and $\phi(N)$ secret. If any of these are leaked, $d$ can be easily recalculated. The primes $p$ and $q$ are often kept secret alongside $d$ to enable a much faster decryption process using the **Chinese Remainder Theorem (CRT)**.
        

## Three-Step Implementation Details

### Step 1. Finding Large Primes

This is a critical step for key generation.

- **Algorithm:**
    
    1. Randomly choose a large odd integer of the desired bit-length (e.g., 1024 bits).
        
    2. Test if this integer is prime. This is **not** done with a deterministic test (which is too slow), but with a fast **probabilistic primality test** like the **Miller-Rabin** algorithm.
        
    3. If the test fails, repeat with a new random integer.
        
- **Why this works:** The **Prime Number Theorem** states that prime numbers are relatively frequent. The average gap between primes near a large number $N$ is roughly $\ln(N)$. This means on average, we only need to test about $\ln(N)$ random odd numbers to find a prime.
    

### Step 2. Modular Exponentiation (Encryption/Decryption)

Calculating $m^e \pmod n$ is not done by computing $m^e$ and then taking the remainder, as the intermediate number would be astronomically large.

- **Algorithm:** The operation is performed using **Exponentiation by Repeated Squaring** (also called the binary method).
    
- **Cost:** This algorithm is very efficient, requiring only $O(\log N)$ modular multiplications.
    
- **Fast Encryption ($e$):**
    
    - If **$e=3$**: $m^3 \pmod n$ is just $(m^2 \pmod n) \cdot m \pmod n$. (2 multiplications).
        
    - If **$e=65537 = 2^{16}+1$**: The calculation is $m^{2^{16}+1} \pmod n$. This requires 16 squarings (to get $m^{2^{16}}$) and 1 final multiplication (to get $m^{2^{16}} \cdot m$), for a total of **17** operations.
        

### Step 3. Computing $d$ (The Extended Euclidean Algorithm)

To find the private key $d$, we must solve $d \cdot e \equiv 1 \pmod{\phi(N)}$. This is done using the **Extended Euclidean Algorithm (EEA)**, which finds the modular multiplicative inverse of $e$ modulo $\phi(N)$.

- **Pseudocode:**
    
    ```C
    /*
     * Finds the modular multiplicative inverse of e modulo phi.
     * Returns d such that (d * e) % phi == 1
     */
    function mod_inverse(int e, int phi) {
        int x0 = 1, x1 = 0;
        int a = e, b = phi;
    
        while (b != 0) {
            int q = a / b;
    
            // Standard Euclidean step
            int t = b;
            b = a % b;
            a = t;
    
            // Update Bézout coefficients
            t = x1;
            x1 = x0 - q * x1;
            x0 = t;
        }
    
        // At the end, x0 is the modular inverse.
        // If x0 is negative, add phi to bring it into the correct range.
        if (x0 < 0) {
            x0 = x0 + phi;
        }
        return x0;
    }
    ```
    

## Encoding: Bridging Text and Numbers

RSA primitives (like [[RSAEP]]/[[RSADP]]) only operate on numbers, but messages are streams of bytes (text, files, etc.). We need a standard way to convert between them.

- **OS2IP (Octet-Stream to Integer Primitive):**
    
    - Converts a $k$-byte string into a single large integer.
        
    - It does this by interpreting the byte string as a **big-endian** number in base 256.
        
    - _Example:_ `b'\x01\x02\x03\x04'` becomes:
        
        - $1 \times 256^3 = 16,777,216$
            
        - $2 \times 256^2 = 131,072$
            
        - $3 \times 256^1 = 768$
            
        - $4 \times 256^0 = 4$
            
        - **Total Integer:** 16,909,060
            
- **I2OSP (Integer to Octet-Stream Primitive):**
    
    - Converts an integer back into a $k$-byte string.
        
    - $k$ is the fixed length of the modulus $N$ in bytes (e.g., $k=256$ for a 2048-bit key).
        
    - _Example:_ Convert integer 84,281,096 to an 8-byte string.
        
        - Integer in hex: `0x05060708`
            
        - Padded to 8 bytes: `00 00 00 00 05 06 07 08`
            
        - **Result (Octet String):** `b'\x00\x00\x00\x00\x05\x06\x07\x08'`
            

## The Secure Scheme: RSA with Padding (PKCS#1)

"Textbook" RSA (just $m^e \pmod n$) is **dangerously insecure**. It is deterministic (same $m$ always gives same $c$) and malleable (an attacker can alter the ciphertext). To be secure, RSA _must_ use a **padding scheme**.

### RSAES-PKCS1-v1.5

This is the original, widely-used padding standard.

- Padding Format: A padded message $M'$ is constructed before encryption:
    
    M' = 0x00 || 0x02 || PS || 0x00 || M
    
- **Components:**
    
    - `0x00`: A single byte, ensures the final number is less than $N$.
        
    - `0x02`: A single byte, the block type, indicating encryption.
        
    - `PS`: A padding string of random, **non-zero** bytes. Must be at least 8 bytes long.
        
    - `0x00`: A single byte separator.
        
    - `M`: The original message.
        
- **Example (2048-bit key, 100-byte message):**
    
    - Key/Modulus size ($k$) = 256 bytes.
        
    - Message size = 100 bytes.
        
    - Padding size = $256 - 1 \text{ (00)} - 1 \text{ (02)} - 1 \text{ (sep)} - 100 \text{ (msg)} = 153$ bytes.
        
    - `M' = 0x00 || 0x02 || [153 random non-zero bytes] || 0x00 || [100-byte message]`
        
This helps for being protected by some [[Forgery]] attacks. 
### Full Encryption Process ([[RSAES]])

1. **Pad:** Create the padded message $M'$ according to the v1.5 scheme.
    
2. **Convert:** Create the integer $m = \text{OS2IP}(M')$.
    
3. **Encrypt (Primitive):** Compute the ciphertext integer $c = m^e \pmod N$. (This is the **[[RSAEP]]**).
    
4. **Convert:** Convert the integer $c$ back to bytes: $C = \text{I2OSP}(c)$.
    

Decryption (**[[RSADP]]**) is the reverse: $C \rightarrow c \rightarrow m \rightarrow M'$. The receiver then parses $M'$ to find the separator `0x00` and extract the original message $M$.

### Security Warning: PKCS#1 v1.5

**PKCS#1 v1.5 is now considered insecure and deprecated for encryption.** While its random padding prevents simple deterministic attacks, it is critically vulnerable to **Chosen-Ciphertext Attacks (CCA)**, specifically **Bleichenbacher's "padding oracle" attack**. An attacker can decrypt messages by sending slightly modified ciphertexts and observing whether the server responds with a "padding error".

## The Modern Standard: RSA-OAEP

To address the severe security flaws in v1.5, a new padding scheme was created: **OAEP (Optimal Asymmetric Encryption Padding)**.

- OAEP is a more complex padding scheme that incorporates a hash function and a Mask Generation Function (MGF).
    
- It is not vulnerable to padding oracle attacks.
    
- It is the current recommended standard for all new applications using RSA for encryption.

---
# RSA: OAEP (Optimal Asymmetric Encryption Padding)

## Introduction to OAEP

**OAEP** stands for **Optimal Asymmetric Encryption Padding**. This is the PKCS#1 v2.2. 

- What is it?
    
    OAEP is a secure padding scheme designed to be used with RSA encryption. It is not an encryption algorithm itself, Remember what is a "Perfect Cipher" 
    
- Purpose:
    
    Its goal is to format the plaintext message $M$ in a specific, structured way before the raw RSA encryption ($m^e \pmod n$) is applied. It adds randomness and structure to achieve semantic security (IND-CPA) and, crucially, security against chosen-ciphertext attacks (IND-CCA).
    
- **Key Features:**
    
    - **Prevents [[Chosen-Ciphertext Attack (CCA)]]:** This is its primary advantage over the older PKCS#1 v1.5 padding.
        
    - **Probabilistic Encryption:** It uses a random **seed** and a **Mask Generation Function (MGF1)**.
        
    - **Semantic Security:** Because of the random seed, encrypting the _same message_ multiple times will produce a _different ciphertext_ every time.
        
    - **Standardization:** It is the modern standard, defined in **PKCS#1 v2.2** (RFC 8017).
        
- Use Case:
    
    The full, secure encryption process is: 
  ```C
    Ciphertext = RSA_Encrypt(OAEP(message, seed)). 
   ```
    It is the recommended standard for all new RSA-based confidentiality applications. this kind of usage of RSA is recognised as [[RSA-OAEP]]. 
    

---

## OAEP: Background and Security Goals

OAEP was introduced by Bellare and Rogaway in 1994 to fix the known vulnerabilities of "textbook" RSA. See the original resource: "Optimal Asymmetric Encryption - How to Encrypt with RSA" 1994, 1995 ([https://cseweb.ucsd.edu/~mihir/papers/oaep.pdf](https://cseweb.ucsd.edu/~mihir/papers/oaep.pdf "https://cseweb.ucsd.edu/~mihir/papers/oaep.pdf")).

- **Random Oracles:** The original proof of security for OAEP models the internal hash functions, **G** and **H**, as "random oracles" (perfect, idealized hash functions). In practice, these are replaced by specific cryptographic hash functions (like SHA-256) and a Mask Generation Function (MGF).
    
- **Probabilistic Scheme:** The random seed ensures the encryption is **probabilistic**, not deterministic, which is the first line of defense against attacks.
    
- **CCA Security:** OAEP is designed to prevent sophisticated attacks, like **Chosen-Ciphertext Attacks (CCA)**, which exposed the vulnerabilities of the older PKCS#1 v1.5 standard (e.g., Bleichenbacher's attack).
    

### Understanding Security Levels ("IND-" Attacks)

OAEP is designed to achieve the highest practical level of security, IND-CCA2.

|**Notation**|**Full Name**|**Attacker's Capabilities**|
|---|---|---|
|**IND-CPA**|Indistinguishability under Chosen Plaintext Attack|Attacker can ask for encryptions of any message they choose. (This is the "semantic security" OAEP provides).|
|**IND-CCA1**|Indistinguishability under Chosen Ciphertext Attack (non-adaptive)|Attacker can decrypt ciphertexts _before_ they receive the challenge ciphertext.|
|**IND-CCA2**|Indistinguishability under Adaptive Chosen Ciphertext Attack|Attacker can decrypt _any_ ciphertext (before _and after_ the challenge), _except_ for the challenge ciphertext itself. This is the strongest level.|

OAEP (when implemented correctly) provides **IND-CCA2** security, which is the gold standard for public-key encryption.

## PPT (Probabilistic Polynomial Time)

Se un algoritmo probabilistico, che produce un output a partire da un imput e da un random string, se non gli inserisco un random string allora diventa un algoritmo deterministico. Allora la classe di algoritmi probabilistici sono più forti di quelli deterministici..

### Analisi:

> gli algoritmi probabilistici possono includere tutti gli algoritmi deterministici.

Questo è vero! Un algoritmo deterministico è solo un caso speciale di algoritmo probabilistico che "ignora" la sua stringa casuale (o usa sempre la stessa).

La tua seconda osservazione:

> anche se non usiamo il random string, noi lo consideriamo comunque un output random.

Qui c'è un piccolo malinteso.

- Se un algoritmo è _probabilistico_ (come OAEP), **deve** usare la "random string" (il _seed_ casuale) per essere sicuro. Se non la usi, l'algoritmo diventa deterministico e perde tutte le sue garanzie di sicurezza.
    
- L'output **non** è random se non usi un input random.
    

Quando diciamo che l'**Avversario** è PPT (Probabilistic Polynomial Time), intendiamo due cose:

1. **Polynomial Time:** Non può impiegare un miliardo di anni per trovare la risposta. Ha un tempo di calcolo "ragionevole".
    
2. **Probabilistic:** Anche l'Avversario può "lanciare monete", cioè usare la casualità per aiutarsi nel suo attacco.
    

Spero che questo chiarisca il ruolo del Challenger e lo scenario del gioco!

Vuoi che esaminiamo perché l'algoritmo "textbook" RSA fallirebbe questo gioco?


### Spiegazione Dettagliata (Passo-Passo)

Ecco una descrizione più strutturata della fase di sfida che hai descritto:

1. **Preparazione dell'Attacco:** L'**Adversary** (l'attaccante) sonda il sistema. Ha accesso a un **oracolo di decifratura** (e talvolta di cifratura), gestito dal Challenger, e lo usa per capire come funziona il sistema.
    
2. **Produzione della Sfida:** Quando si sente pronto, l'Adversary sceglie due messaggi distinti della stessa lunghezza, $m_0$ e $m_1$, che vuole provare a distinguere. Invia entrambi questi messaggi al **Challenger**.
    
3. **Il Lancio della Moneta:** Il **Challenger** riceve $m_0$ e $m_1$. Esegue il "toss a coin": sceglie un bit $b$ in modo perfettamente casuale (o 0 o 1).
    
4. **Creazione del Testo Cifrato di Sfida:** Il Challenger seleziona il messaggio $m_b$ (quindi $m_0$ se $b=0$, oppure $m_1$ se $b=1$). Cifra _solo quel messaggio_ usando la chiave pubblica, ottenendo il "ciphertext di sfida" $c_b$.
    
5. **Invio della Sfida:** Il Challenger invia $c_b$ all'Adversary.
    


### 1. Chi è il "Challenger" (Lo Sfidante)?

Pensa al **Challenger** come all'**arbitro del gioco**.

- È un'entità teorica (un computer nel nostro esperimento) che **imposta la sfida**.
    
- **Possiede le chiavi:** È lui che genera la coppia di chiavi (pubblica e privata) all'inizio.
    
- **Rappresenta l'utente "onesto":** Si comporta come un normale utente che cifra e decifra messaggi.
    
- **Fornisce gli "oracoli":** Quando l'attaccante chiede di cifrare o decifrare qualcosa (l'oracolo), è il Challenger che esegue l'operazione usando le chiavi che possiede.
    

### 2. Chi è l'"Adversary" (L'Avversario)?

È l'**attaccante** (il "cattivo"). Il suo obiettivo è **vincere il gioco**, ovvero "rompere" la sicurezza del sistema.

### 3. Cosa sta succedendo? (Il Gioco IND-CCA2)

Il gioco che hai descritto serve a dimostrare l'**Indistinguibilità** (IND). L'obiettivo dell'Avversario è capire se riesce a **distinguere** tra la cifratura di due messaggi diversi.

Ecco i passaggi esatti:

1. **Fase di Preparazione (Fase 1 del CCA):**
    
    - L'**Avversario** può "imparare" il sistema.
        
    - Chiede all'**Oracolo** (gestito dal Challenger) di decifrare tutti i messaggi che vuole. Questa è la parte "Chosen-Ciphertext Attack" (CCA).
        
    - Il Challenger risponde onestamente a tutte le richieste.
        
2. **La Sfida (Il cuore del gioco):**
    
    - L'**Avversario** ora sceglie due messaggi qualsiasi della stessa lunghezza, $m_0$ e $m_1$. Pensa a $m_0$ = "Attacca all'alba" e $m_1$ = "Ritirata generale".
        
    - L'Avversario invia entrambi i messaggi al **Challenger**.
        
3. **Il Lancio della Moneta:**
    
    - Il **Challenger** riceve $m_0$ e $m_1$.
        
    - Fa esattamente quello che hai scritto: "toss a coin". Sceglie un bit casuale $b$ (che può essere 0 o 1).
        
    - Cifra **uno solo** dei due messaggi: $c_b = \text{Encrypt}(m_b)$.
        
    - Invia questo singolo testo cifrato, $c_b$ (chiamato il "challenge ciphertext"), all'Avversario.
        
4. **La Prova (Fase 2 del CCA):**
    
    - L'**Avversario** riceve $c_b$. Non sa se contiene $m_0$ o $m_1$.
        
    - Per scoprirlo, può continuare a fare domande all'Oracolo di decifratura (questa è la parte "adattiva" o "CCA2").
        
    - **Regola importante:** L'Avversario può chiedere di decifrare _qualsiasi cosa_, **tranne** l'esatto $c_b$ che ha appena ricevuto (sarebbe troppo facile!).
        
5. **L'Indovinello Finale:**
    
    - Alla fine, l'Avversario deve fare una scelta. Deve dire: "Il $c_b$ che mi hai mandato conteneva $m_0$ o $m_1$?"
        

### Come si vince (e cosa significa)?

- **Sistema Insicuro (es. RSA "textbook"):** L'Avversario riesce a trovare un modo per indovinare correttamente con una probabilità molto più alta del 50%. Ha trovato una falla. Il sistema **perde**.
    
- **Sistema Sicuro (come OAEP):** Non importa quanto l'Avversario studi il sistema o quante domande faccia all'oracolo, non ottiene **nessuna informazione** utile. L'unica cosa che può fare è tirare a indovinare a caso. La sua probabilità di azzeccare è esattamente del 50% (come lanciare una moneta). Il sistema **vince**.
    

In sintesi: **il Challenger è l'arbitro che testa l'Avversario** per vedere se quest'ultimo sa distinguere tra due messaggi cifrati. Se l'Avversario non sa farlo (non fa meglio che tirare a indovinare), l'algoritmo è sicuro.


---

## The OAEP Scheme (Feistel Structure)
![[Pasted image 20251113160151.png]]

OAEP works by taking the message $m$ and a random seed $r$, and formatting them using a structure similar to a **Feistel network**.

- **Parameters:**
    
    - $n$ = number of bits in the RSA modulus (e.g., 2048)
        
    - $k0$ = length of the random seed $r$ (e.g., 256 bits for SHA-256)
        
    - $k1$ = length of the padding block (e.g., a block of zeros)
        
    - $m$ = plaintext message
        
    - $G, H$ = cryptographic hash functions (or [[MGF]]s)
        
- **Encryption (Padding) Process:**
    
    1. **Pad Message:** The message $m$ is padded with $k1$ zeros to a fixed length.
        
    2. **Generate Seed:** A random $k0$-bit string $r$ is generated.
        
    3. **Mask Message:** The seed $r$ is put through the hash function $G$ to create a mask. This mask is XORed with the padded message to create block $X$:
        
        - $X = (m \ || \ 00...0) \oplus G(r)$
            
    4. **Mask Seed:** The new block $X$ is put through the hash function $H$ to create a second mask. This mask is XORed with the seed $r$ to create block $Y$:
        
        - $Y = r \oplus H(X)$
            
    5. **Output:** The final padded message to be encrypted by RSA is the concatenation $X || Y$.
        
- **Decryption (Unpadding) Process:**
    
    1. **Split Blocks:** The decrypted block is split back into $X$ and $Y$.
        
    2. **Recover Seed:** The seed $r$ is recovered by re-calculating the mask from $X$ and XORing it with $Y$:
        
        - $r = Y \oplus H(X)$
            
    3. **Recover Message:** The message $m$ is recovered by re-calculating the mask from the recovered $r$ and XORing it with $X$:
        
        - $m \ || \ 00...0 = X \oplus G(r)$
            
    4. **Verify:** The receiver checks if the $k1$ padding bits are all zeros. If they are not, the message is rejected as invalid. This check is critical for security.
        
Notice that, thanks to how in the scheme the randomness ins well integrated, the result is way more powerful compared to the PKCS#1 v1.5.

### "All-or-Nothing" Security

This Feistel structure creates an "all-or-nothing" property.

- To recover the message $m$, you must have the _entire_ block $X$ and the _entire_ block $Y$.
    
- You need $X$ to recover $r$ from $Y$.
    
- You need $r$ to recover $m$ from $X$.
    
- If an attacker modifies _even a single bit_ of the ciphertext, the properties of the cryptographic hash functions will cause the decrypted $X$ and $Y$ to be completely scrambled. This will result in the recovered padding ($k1$ bits) _not_ being all zeros, and the entire decryption will fail. This prevents the very "padding oracle" attacks that plague the v1.5 standard.
    

---

## RSAES-OAEP: The Full Process
[[RSAES-OAEP]]

**[[RSAES]] (RSA Encryption Scheme)** combines the OAEP padding with the RSA primitives.

- **Encryption:**
    
    1. **Encode:** Given message $M$, produce the encoded message $M'$ using the OAEP scheme.
        
    2. **OS2IP:** Convert the octet-stream $M'$ into an integer $m$ ($m = \text{OS2IP}(M')$).
        
    3. **RSAEP:** Apply the RSA Encryption Primitive: $c = \text{RSAEP}((N, e), m)$, which is $c = m^e \pmod N$.
        
    4. **I2OSP:** Convert the integer $c$ into the final ciphertext octet-stream $C$ ($C = \text{I2OSP}(c, |N|)$).
        
- Decryption:
    
    This is the symmetric reverse, using the RSA Decryption Primitive (RSADP) and the OAEP unpadding operation ($OAEP^{-1}$).
    

This full process is the modern standard, **PKCS#1 v2.2**.

---

## Comparison of RSA Padding Schemes

|**Feature**|**PKCS#1 v2.2 (RSA-OAEP)**|**PKCS#1 v1.5**|
|---|---|---|
|**Randomization**|Uses MGF for robust, structured randomization.|Weaker randomization; less structured.|
|**CCA Resistance**|**Secure** against adaptive CCA (e.g., Bleichenbacher's attack).|**Vulnerable** to adaptive CCA attacks.|
|**Hash-Based**|**Yes**, integrates a hash function (e.g., SHA-256) into the padding.|**No**, does not use hash functions in the padding.|
|**Recommendation**|**Recommended for all new implementations.**|**Deprecated.** Use only for backward compatibility (e.g., TLS < 1.3).|

### Importance of Hash-Based Security in OAEP

The use of a hash function (like SHA-256) in OAEP is critical.

- It adds an extra layer of cryptographic robustness.
    
- It cryptographically links the message and the random seed, preventing attackers from manipulating the padding and the message independently.
    
Fun fact: in this algorithm is considered still usefull [[SHA-1]] because somehow provides enough security.

---

## Summary

- **RSA-OAEP (PKCS#1 v2.2)** offers significant and necessary security advantages over the old **PKCS#1 v1.5** standard. 
    
- Its **randomized padding** (using a seed and MGF) provides semantic security, preventing attackers from recognizing patterns.
    
- Its **all-or-nothing structure** provides provable resistance to **chosen-ciphertext attacks (CCA)**, ensuring data robustness.
    
- It is the preferred and modern standard for any application requiring high-security data confidentiality with RSA.

Again: RSA is not used for [[Confidentiality]] but just for Key Exchange, which gives the opportunity to have [[Confidentiality]] with a [[Symmetric Encryption]]. 

---
# RSA for Non-Repudiation
THIS IS THE MOST IMPORTANT PART OF THIS COURSE. What happens if the adversary let you believe that his public key is the Bob's public key? The Adversary wins. So how can we be sure about the ownership of the public key? 
## What is Non-Repudiation?

**Non-repudiation** is the assurance that someone cannot deny having performed a particular action or having sent a particular message. In digital communications, this means providing proof of the origin, authenticity, and integrity of data.

**Digital signatures** are the primary cryptographic tool used to achieve non-repudiation.

A digital signature provides three key security services:

1. **[[Authentication]]:** Proof of who the sender is.
    
2. **[[Integrity]]:** Proof that the message was not altered in transit.
    
3. **[[Non-Repudiation]]:** The sender cannot later deny having signed the message.
    

The RSA algorithm achieves this by reversing its encryption process:

- **To Encrypt ([[Confidentiality]]):** You use the recipient's **Public Key**.
    
- **To Sign ([[Non-Repudiation]]):** You use your _own_ **Private Key**.
    

Because only the sender possesses the private key, a signature created with it serves as undeniable proof of origin. Anyone can then use the sender's public key to verify that the signature is valid.

However, simply signing a raw message ($S = M^d \pmod n$) is insecure. A robust, standardized process is needed, which is defined by standards like PKCS#1.

---

## 1. Legacy Standard: RSASSA-PKCS1-v1_5

This is the original and still widely used signature standard, though it is now considered a legacy system.

- **Paradigm:** It follows the **"hash-then-sign"** model.
    
    - **Why?** Signing a large message with RSA is extremely slow. Hashing the message first (e.g., with SHA-256) produces a small, fixed-size string (the "digest").
        
    - Signing this small digest is very fast and provides the same security, as any change to the message will change the hash.
        
- **Key Feature:** It uses a **deterministic padding** format. This means signing the same message twice always produces the exact same signature, which is a known vulnerability.
    
- **Standard:** The encoding method is called **EMSA** (Encoding Method for Signature with Appendix). 
	- Preprocessing before signature

### v1.5 Signature Generation

1. **Hash:** First, the message $M$ is hashed to produce a digest $H$.
    
    - $H = \text{Hash}(M)$
        
2. **Encode Digest:** The hash $H$ is combined with its algorithm identifier to create a standard structure called `DigestInfo`, which is denoted as $T$. This structure is encoded using a format called **DER** (Distinguished Encoding Rules).
    
3. **Build Encoded Message (EM):** A padding block is constructed. This block is deterministic.
    
    - `EM = 0x00 || 0x01 || PS || 0x00 || T`
        
    - `0x00 || 0x01`: A standard header to indicate a signature block (distinguishing it from the `0x02` encryption block).
        
    - `PS`: A padding string of all `0xFF` bytes. This fills the block until it is the same length as the modulus $n$.
        
    - `0x00`: A single-byte separator.
        
    - `T`: The DER-encoded `DigestInfo` (hash + algorithm ID) from Step 2.
        
4. **Sign:** The RSA Signature Primitive (RSASP) is applied to the final encoded message using the **private key**.
    
    - $S = \text{EM}^d \pmod n$
        
Full method named RSASSA (RSA+MSA)
### v1.5 Signature Verification

1. **Hash:** The receiver hashes the original message $M$ to get $h$.
    
2. **Encode:** The receiver _re-creates_ the expected encoded message, `
   ```
   EM_expected = EMSA-PKCS1-v1_5-ENCODE(h, |N|_8)
   ```
    by following the same padding steps (using $h$ and its OID).
    
3. **Verify (Decrypt):** The receiver applies the RSA Verification Primitive (RSAVP) using the sender's **public key**.
    
    - $\text{EM}' = S^e \pmod N$
        
4. **Compare:** The signature is valid **if and only if** the recovered $\text{EM}'$ is identical to the `EM_expected`.
    

Fun fact: Tampered means changed by the adversary, Forgery means successfully tampered

### Security Flaws of v1.5

- **Deterministic:** The biggest flaw is that the padding is deterministic. This opens it up to practical attacks.
    
- **Vulnerability:** It is vulnerable to **padding oracle attacks**. An attacker can trick a server into verifying modified signatures and, based on whether the server reports a "valid" or "invalid" signature, progressively forge a signature without ever knowing the private key.
    
- **Status:** Due to these flaws, it is deprecated for new applications but is still widely used in legacy systems like TLS 1.2, [[S-MIME|S/MIME]], and older [[Code-Signing]] standards.
    

---

## 2. Modern Standard: RSASSA-PSS (Probabilistic Signature Scheme)

**PSS (Probabilistic Signature Scheme)** is the modern, recommended standard for RSA signatures, introduced in PKCS#1 v2.1.

- **Key Feature:** It is **probabilistic**, not deterministic.
    
- **How it Works:** It achieves this by adding a random **salt** (a random string of bytes) to the signature process.
    
- **Result:** Every time you sign the _same message_, you will get a **different signature** due to the new random salt.
    
- **Security:** PSS is **provably secure** in the random oracle model (meaning its security can be mathematically reduced to the hardness of the RSA problem).
    

### PSS Signature Generation

While the process is complex, the core idea is:

1. **Hash:** $H = \text{Hash}(M)$ (Hash the message).
    
2. **Salt:** Generate a random string, `salt`.
    
3. **Combine:** Create a new hash $H'$ by hashing the original hash $H$ _and_ the random `salt` together.
    
    - $H' = \text{Hash}(0x00...*8\ times || H || \text{salt})$
        
4. **Mask:** Create a "Data Block" (`DB`) containing the salt and padding. $$DB = PS || 0x01 || salt$$
   - PS = zero bytes (padding)
   - $|PS| = |N|_8 - hLen - saltLen - 2$
   
1. Then, use a **Mask Generation Function (MGF)** (which is a hash-based function) to "stretch" $H'$ into a mask. This mask is XORed with the `DB`.
    
    - $maskedDB = DB \oplus \text{MGF1}(H')$`
        
2. **Encode:** The final encoded message `EM` is built from the `maskedDB` and the hash $H'$.
    
    - `EM = \text{maskedDB} || H' || 0xbc` (The `0xbc` is a fixed trailer byte).
        
3. **Sign:** Sign the final `EM` block with the **private key**.
    
    - $S = \text{EM}^d \pmod n$
        

### PSS Signature Verification

The verifier essentially reverses the process to check if all the components match.

1. **Hash:** $H = \text{Hash}(M)$ (Hash the original message).
    
2. **Recover EM:** Use the **public key** to recover the encoded message.
    
    - $\text{EM} = S^e \pmod n$
        
3. **Check & Split:** Check that the trailer byte is `0xbc`, then split `EM` into its `maskedDB` and $H'$ components.
    
4. **Unmask:** Use the recovered $H'$ to unmask the `maskedDB` and recover the `DB`.
    
    - `DB = \text{maskedDB} \oplus \text{MGF1}(H')`
        
5. **Parse & Recover Salt:** Parse the `DB` to extract the `salt`.
    
6. **Recompute H':** The verifier now re-computes what $H'$ _should_ be, using the _original_ message hash $H$ (from Step 1) and the _extracted_ `salt` (from Step 5).
    
    - `H'_check = \text{Hash}(0x00... || H || \text{salt})`
        
7. **Verify:** The signature is valid **if and only if** the recovered $H'$ from the signature matches the re-computed `H'_check`.
    

---
## Why prefer PSS 

- Probabilistic → immune to many attacks targeting PKCS#1 v1.5
    
- Flexibility in choosing hash and salt lengths
    
- Recommended by modern standards (e.g., FIPS 186-5, TLS 1.3, OpenPGP)

---

## Final Comparison: PKCS#1 v1.5 vs. PSS

PSS is the superior standard in every practical way.

|**Feature**|**PKCS#1 v1.5 (Legacy)**|**RSA-PSS (Modern)**|
|---|---|---|
|**Padding**|**Deterministic** (Same message = same signature)|**Probabilistic** (Same message = different signature)|
|**Security Proof**|**None.** Has known vulnerabilities.|**Yes.** Provably secure in the random oracle model.|
|**Salt**|No|**Yes** (a random value is added to each signature)|
|**Standard Use**|Legacy systems (TLS 1.2, S/MIME)|Modern standards (TLS 1.3, FIPS 186-5)|
