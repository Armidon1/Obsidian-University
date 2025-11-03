last lesson [[6 CS - Authenticated Encryption]]
# Asymmetric encryption: the Diffie-Hellman intuition
now we talked always about symmetric keys. Now we think in a different way: a asymmetric encryption: the tipical usage is different because it is harder to guarantee Confidentiality.


## Reminder about the model
![[Pasted image 20251022151244.png]]
if keys𝐾1 = 𝐾2 symmetric encryption
else asymmetric

remember: encryption doesn't provide only Confidentiality but also other properties.

## Another definition

- **Key exchange** is the process of establishing a shared symmetric key between two parties over an insecure communication channel
	- classic challenge in enabling private communication between remote parties
	- the part of key exchange is extremely important and there are many protocols used in those situations.
- **Asymmetric** cryptography provides a solution to this problem by enabling secure key exchange mechanisms

## Public-key encryption

A relevant example of asymmetric encryption
- when K 1 ≠K 2
is the **public-key encryption**. Note that:
- public key encryption $\Rightarrow$ Asymmetric encryption
- Asymmetric encryption $\nRightarrow$ public key encryption

purposes
- integrity and non-repudiation
- key exchange
    - main example that requires confidentiality


## Diffie and Hellman [1976]  “New Directions in Cryptography”

Split the Bob’s secret key K into two parts

- $K_E$ to be used for encrypting messages to Bob
- $K_D$ to be used for decrypting messages by Bob
- $K_E$ can (must) be made public
    - essence of public key cryptography a type of
       asymmetric cryptography

I can also encrypt also with the other key and viceversa with the other one. 

Other people will use your public key, and you can decrypt easily.
If i encrypt with my private key, who can encrypt? EVERYONE. that's why there is not confidentiality.
but because you are the only one who can encrypt a message, so i'm the owner, everyone that can decrypt can be sure that the message is made by me (**NO REPUDIATION**, even stronger than **Autenticity**).

I can use the asymmetric key to share the symmetric key: i use the public key to encrypt the symmetric key and then i can create a secret communication channel.

## Number of keys
Imagine each node is a Spy. if we consider a complete graph, how many arches do we have? consider n spies, each spy has n-1 arcs, then we have n(n-1)/2, where the /2 is because when i consider another spy, i compute an exact same arch of another spy
- if arc(spy1,spy2) == arch(spy2, spy1)
![[Pasted image 20251022152451.png]]
Today we say that a pair of keys (private, public) is associated with each actor
- linear number of asymmetric keys
- quadratic number of symmetric keys


## “New Directions in Cryptography” • The Diffie-Hellman paper [IEEE Transactions on Information

```
Theory, vol. IT-22, Nov. 1976] generated lot of interest in
crypto research, both in academia and private industry
http://www-ee.stanford.edu/%7Ehellman/publications/24.pdf
```
- Diffie & Hellman produced the revolutionary idea of public key cryptography, but did not have a proposed implementation (this came up two years later with Merkle-Hellman and Rivest-Shamir-Adelman)
- **In their '76 paper, Diffie & Hellman did invent a method for key exchange over insecure communication lines, a method that is still in use today**

## Excerpt from RSA paper

- Historical paper: "A Method for Obtaining Digital
    Signatures and Public-Key Cryptosystems
    R.L. Rivest, A. Shamir, and L. Adleman", Communications of the ACM 21,
    1978 https://people.csail.mit.edu/rivest/Rsapaper.pdf
- ***The era of electronic mail may soon be upon us*** _; we must ensure that_
    _two important properties of the current paper mail system are preserved: (a)_
    _messages areprivate, and (b) messages can besigned. We demonstrate in_
    _this paper how to build these capabilities into an electronic mail system._
- _At the heart of our proposal is a new encryption method. This method_
    _provides an implementation of a public-key cryptosystem, an elegant_
    _concept invented by Diffie and Hellman [1]. Their article motivated our_
    _research, since they presented the concept but not any practical_
    _implementation of such a system. Readers familiar with [1] may wish to skip_
    _directly to Section V for a description of our method._


## Meaning of encryption

Alice **encrypts**

- by Bob's public key
    - although public it must be known
    - all can use Bob's public key
    - **confidentiality**
- by Alice's private key
    - only Alice can use it
    - everybody can decrypt
    - no confidentiality, but **path to non-repudiation**


## Encryption behaviour

- What is encrypted by a public key can be decrypted by the associated private key

- What is encrypted by a private key can be decrypted by the associated public key
	- This happens for RSA (later)
- This perfect symmetry causes the frequent use of the term encryption for both (classic) encryption and decryption


# Introduction to one-way functions

## One-way function

>[!One-Way Function]
>A function 𝑓: 0,1 ∗→ 0,1 ∗is called a one-way function (OWF) if it is
>- **Efficiently computable**
>	- There exists a deterministic polynomial-time algorithm that, given any input𝑥∈ 0,1 ∗, computes𝑓(𝑥)
>- **Hard to invert on average**
  > 	 - For every probabilistic polynomial-time algorithm𝐴, for every positive polynomial 𝑝(·)and for sufficiently large 𝑛
    >      $$\Pr_{x \leftarrow \{0,1\}^n}[A(f(x)) \in f^{-1}(f(x))] < \frac{1}{p(n)}$$
>	where the probability is over the uniform random choice of𝑥∈ 0,1 𝑛and the internal randomness of𝐴

**cryptographic hashing functions are OWF**
## Integer multiplication & factoring as an OWF
![[Pasted image 20251023113341.png]]
**Q.: Can a public key system be based? on this observation**

## 1. Foundational Concepts: One-Way Functions (OWFs)

Modern cryptography is built on the concept of "hard problems." These are formalized as **One-Way Functions (OWFs)**.

- **Definition:** A function that is **easy to compute** in one direction (e.g., $f(x) = y$) but **computationally infeasible** to invert (e.g., given $y$, find $x$).
    
- **Do OWFs Exist?** This is an **open problem** in computer science.
    
    - They are widely **conjectured to exist**.
        
    - **Theorem:** If a one-way function exists, then **P ≠ NP**.
        
    - Since it is strongly believed that P ≠ NP, it is also believed that OWFs exist.
        
- **Utility:** OWFs are the foundation for many cryptographic guarantees, including:
    
    - Cryptographic hashing
        
    - Secure key exchanges
        
    - Public-key cryptography
        
    - Random number generation
        

### Candidate 1: Integer Factorization

This problem is the basis for the RSA algorithm.

- **Easy Problem:** Given two large prime numbers, $x$ and $y$ (e.g., _n_ bits each), computing their product $z = xy$ is easy (polynomial time). The result $z$ will have about _2n_ bits.
    
- **Hard Problem:** Given a large composite number $z$, finding its prime factors $x$ and $y$ is computationally infeasible (no known polynomial-time algorithm for classical computers).
    
    - _Note:_ Shor's algorithm can factor in polynomial time, but only on a (currently hypothetical, large-scale) quantum computer.
        

### Candidate 2: The Discrete Logarithm (DL) Problem

This problem is the basis for Diffie-Hellman and ElGamal.

- **Definition:** Let $G$ be a finite cyclic group with _n_ elements and $g$ be a generator of $G$.
    
- **Easy Problem:** Given $g$ and an integer $x$, it is easy to compute $y = g^x$.
    
- **Hard Problem:** Given $y$ and $g$, it is computationally infeasible to find the minimal non-negative integer $x$ that satisfies the equation $y = g^x$.
    
- **Terminology:** This $x$ is called the **discrete logarithm of $y$ to the base $g$**.
    
- **Example:** A common group used is the multiplicative group of integers modulo $p$, $\mathbb{Z}^*_p$. The problem is: find $x$ given $y$, $g$, and $p$ in $y = g^x \pmod p$.
    
- **DL in $\mathbb{Z}^*_p$ as an OWF:**
    
    - The function $x \rightarrow g^x \pmod p$ is **easy** to compute.
        
    - The inverse function $y \rightarrow x$ is **believed to be hard**.
        
    - This is a **computation-based** notion of security.
        

---

## 2. Essential Mathematical Tools

To implement these cryptographic systems, we need efficient algorithms for modular arithmetic.

### Modular Exponentiation

This is the "easy" operation in the Discrete Logarithm problem.

- **Property:** `c mod p = (a ⋅ b) mod p = ((a mod p) ⋅ (b mod p)) mod p`
    
    - This means we can apply the `mod p` operation at each partial step to keep the numbers small.
        
    - See: [https://en.wikipedia.org/wiki/Modular_arithmetic#Properties](https://en.wikipedia.org/wiki/Modular_arithmetic#Properties)
        
- **Optimization (Euler's Theorem):** If $p$ is prime and $b$ and $p$ are co-prime:
    
    - $b^e \pmod p = (b \pmod p)^{e \pmod{\varphi(p)}} \pmod p$
        
    - (where $\varphi(p) = p-1$ since $p$ is prime)
        
    - See: [https://en.wikipedia.org/wiki/Euler%27s_theorem](https://en.wikipedia.org/wiki/Euler%27s_theorem)
        

#### Fast Modular Exponentiation (Algorithm)

Instead of calculating $g^x$ and _then_ taking the modulus (which would result in a gigantic intermediate number), we use the "exponentiation by squaring" method, applying the modulus at every step.

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

- **Efficiency:** This algorithm computes the result in $O(\log(x))$ multiplications, with each multiplication taking $O(\log^2(p))$ steps. Since $x < p$, the overall complexity is $O(\log^3(p))$.
    

### The Extended Euclidean Algorithm (EEA)

This tool is essential for RSA key generation, specifically for finding the private exponent $d$ from the public exponent $e$.

- **Purpose:** To find the **multiplicative inverse** of a number in a modulus.
    
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
            
    - This means $a$ is the multiplicative inverse of $x$ modulo $y$ (i.e., $a \equiv x^{-1} \pmod y$).
        
    - Similarly, $b \equiv y^{-1} \pmod x$.
        

_Note_: For the exam, the professor wants the interpretation of [[Bézout's identity]] given a specific number, not just the algorithm itself. You must understand _what_ it is and _why_ it's used.

#### The EEA Algorithm

This algorithm finds the coefficients $a$ and $b$ (here called `x0` and `y0`) from Bézout's identity.

C

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

DH is a protocol that uses the **Discrete Logarithm problem** to achieve a secure key exchange.

- **Goal:** Two parties (Alice and Bob) who share no secret information can perform a protocol over a public (insecure) channel and derive the **same shared secret key**.
    
- **Security:** An eavesdropper (Eve) who is listening cannot obtain this shared key (in polynomial time).
    

### DH Procedure

1. **Public Parameters:** Alice and Bob first agree (publicly) on two numbers:
    
    - A large prime $p$.
        
    - An element $g$ (which is a generator of the multiplicative group $\mathbb{Z}^*_p$).
        
    - _Note:_ For best security, $p$ should be a "safe prime," where $p = 2q + 1$ and $q$ is also prime (making $q$ a Sophie Germain prime).
        
2. **Alice's Steps:**
    
    - Chooses a **private key** $a$ (a random secret number, $1 \le a \le p-1$).
        
    - Computes her **public key** $A = g^a \pmod p$.
        
    - Sends $A$ to Bob.
        
3. **Bob's Steps:**
    
    - Chooses a **private key** $b$ (a random secret number, $1 \le b \le p-1$).
        
    - Computes his **public key** $B = g^b \pmod p$.
        
    - Sends $B$ to Alice.
        
4. **Shared Secret Calculation:**
    
    - Alice receives $B$ and computes: $K = B^a \pmod p = (g^b)^a \pmod p = g^{ab} \pmod p$.
        
    - Bob receives $A$ and computes: $K = A^b \pmod p = (g^a)^b \pmod p = g^{ab} \pmod p$.
        

Both parties now possess the same **shared secret key $K = g^{ab} \pmod p$**. Eve, who only sees $g, p, A, B$, cannot compute $K$ because she would need to solve the Discrete Log problem to find $a$ or $b$.

### DH Properties and Variants

#### Perfect Forward Secrecy (PFS)

- **Definition:** A cryptosystem has PFS if it generates **random, temporary public keys for each session**.
    
- **Implication:** The compromise of a single key (e.g., a long-term private key) **does not compromise any past or future session keys**. If an attacker records all traffic and _later_ steals the server's main key, they _still_ cannot decrypt the old sessions.
    

#### Types of DH

|**Feature**|**Static Diffie-Hellman**|**Ephemeral Diffie-Hellman (DHE/ECDHE)**|
|---|---|---|
|**Key Lifespan**|Uses a long-term key pair that remains the same across sessions (typically on the server side).|Generates a **new, temporary** key pair for **each** communication session.|
|**Mathematical Basis**|Modular exponentiation or elliptic curves.|Modular exponentiation or elliptic curves.|
|**Primary Security Property**|**Lacks Forward Secrecy.**|**Provides Forward Secrecy.**|
|**Primary Use Case**|Specific scenarios where long-term key management is required.|The **standard** for modern secure communication (e.g., TLS).|

### DH Vulnerabilities

The "textbook" DH protocol is effective _only against a passive adversary (eavesdropper)_.

|**Vulnerability**|**Description**|**Impact**|**Mitigation**|
|---|---|---|---|
|**Man-in-the-Middle (MitM)**|**No authentication** in basic DH. Alice doesn't know she's talking to Bob.|Attacker (Trent) intercepts and alters the key exchange.|Use **Authenticated DH** (e.g., signing keys with X.509 certs).|
|**Logjam Attack**|Exploits the use of small (e.g., 512-bit) or common/shared prime numbers ($p$).|Attacker breaks DH with massive precomputation against a common prime.|Use $\ge$ 2048-bit unique, safe primes.|
|**Static DH Keys**|Reuse of long-term DH private keys.|**No Forward Secrecy.**|Use **Ephemeral DH (DHE)**.|

#### The Man-in-the-Middle (MitM) Attack (Detailed)

An active attacker (Trent) sits between Alice and Bob:

1. A $\rightarrow$ T(B): Alice sends $A = g^a \pmod p$ (intending to send to Bob).
    
2. T(B) $\rightarrow$ A: Trent intercepts $A$, generates his _own_ secret $t$, computes $T = g^t \pmod p$, and sends $T$ to Alice (pretending it's from Bob).
    
3. T(A) $\rightarrow$ B: Trent sends $T = g^t \pmod p$ to Bob (pretending it's from Alice).
    
4. B $\rightarrow$ T(A): Bob receives $T$, generates his secret $b$, computes $B = g^b \pmod p$, and sends $B$ to Trent (thinking he's sending to Alice).
    

**Effects:**

- Alice computes a shared key with Trent: $K_A = T^a \pmod p = g^{ta} \pmod p$.
    
- Bob computes a shared key with Trent: $K_B = T^b \pmod p = g^{tb} \pmod p$.
    
- Alice and Bob believe they have a secure channel, but Trent can intercept, decrypt, read, modify, and re-encrypt all messages between them. This violates [[Availability]] and all other security properties.
    

### Other DH Systems

- The DH idea can be used with any group, _except_ those where the discrete log is easy (e.g., the additive group of $\mathbb{Z}_p$).
    
- **ECDH (Elliptic-Curve Diffie–Hellman):** A modern variant that uses elliptic curve groups. It provides the same level of security with much smaller keys, making it more efficient. [https://en.wikipedia.org/wiki/Elliptic-curve_Diffie%E2%80%93Hellman](https://en.wikipedia.org/wiki/Elliptic-curve_Diffie%E2%80%93Hellman)
    

---

## 4. Protocol 2: The RSA Cryptosystem

RSA is an algorithm built on the **Integer Factorization problem**. It can be used for both encryption and digital signatures.

### Part 1: The RSA Algorithm

#### Mathematical Basis: The Group $\mathbb{Z}^*_{pq}$

1. Let $p$ and $q$ be two large primes. Let $N = pq$.
    
2. The multiplicative group $\mathbb{Z}^*_N$ contains all integers in $[1, N-1]$ that are relatively prime to $N$.
    
3. The size of this group is given by Euler's Totient Function:
    
    $\varphi(N) = \varphi(pq) = (p-1)(q-1)$.
    
4. By Euler's Theorem, for any element $x \in \mathbb{Z}^*_N$, we have:
    
    $x^{\varphi(N)} \equiv 1 \pmod N$
    
    $x^{(p-1)(q-1)} \equiv 1 \pmod N$
    

#### Exponentiation in $\mathbb{Z}^*_{pq}$

- **Question:** When is the operation $x \rightarrow x^e$ a **one-to-one** operation (a _permutation_) in this group?
    
- **Claim:** If $e$ is relatively prime to $\varphi(N)$ (i.e., $\gcd(e, (p-1)(q-1)) = 1$), then $x \rightarrow x^e$ is a one-to-one operation.
    
- **Constructive Proof (Why decryption works):**
    
    1. Since $\gcd(e, \varphi(N)) = 1$, $e$ has a multiplicative inverse $d$ modulo $\varphi(N)$. (We find $d$ using the **Extended Euclidean Algorithm**).
        
    2. This means $ed \equiv 1 \pmod{\varphi(N)}$, or $ed = 1 + k\varphi(N)$ for some integer $k$.
        
    3. Let $y = x^e \pmod N$ (Encryption).
        
    4. Now compute $y^d \pmod N$ (Decryption):
        
        $y^d = (x^e)^d = x^{ed} = x^{1 + k\varphi(N)}$
        
        $y^d = x^1 \cdot (x^{\varphi(N)})^k$
        
    5. From Euler's Theorem, we know $x^{\varphi(N)} \equiv 1 \pmod N$.
        
    6. Therefore: $y^d \equiv x \cdot (1)^k \pmod N \equiv x \pmod N$.
        
    7. This proves that $y \rightarrow y^d$ is the inverse of $x \rightarrow x^e$. **QED**.
        

#### RSA Key Generation and Operation

1. **Key Generation:**
    
    - Choose two large, distinct primes $p$ and $q$.
        
    - Compute the modulus: $N = pq$.
        
    - Compute the totient: $\varphi(N) = (p-1)(q-1)$.
        
    - Choose a public exponent $e$ (where $1 < e < \varphi(N)$ and $\gcd(e, \varphi(N)) = 1$). A common choice is $e = 65537$.
        
    - Compute the private exponent $d$ such that $de \equiv 1 \pmod{\varphi(N)}$ (using the EEA).
        
    - **Public Key:** $(e, N)$
        
    - **Private Key:** $(d, N)$ (or sometimes $(d, p, q)$)
        
2. **Encryption (Alice sends to Bob):**
    
    - Alice gets Bob's public key $(e_B, N_B)$.
        
    - She converts her message $M$ into a number (or numbers) $M < N_B$.
        
    - She computes the ciphertext: $C = M^{e_B} \pmod{N_B}$.
        
    - She sends $C$ to Bob.
        
3. **Decryption (Bob receives from Alice):**
    
    - Bob uses his private key $(d_B, N_B)$.
        
    - He computes the plaintext: $M = C^{d_B} \pmod{N_B}$.
        

#### Why Decryption Works (Formal Proof for all $M \in \mathbb{Z}_N$)

The proof above only worked for $x \in \mathbb{Z}^*_N$. What if $M$ is not coprime to $N$ (i.e., $M$ is a multiple of $p$ or $q$)?

- We need to prove $M^{ed} \equiv M \pmod N$.
    
- By the [[Chinese Remainder Theorem]], this is true if and only if:
    
    1. $M^{ed} \equiv M \pmod p$
        
    2. $M^{ed} \equiv M \pmod q$
        
- **Case 1 (for mod p):**
    
    - If $\gcd(M, p) = 1$ (i.e., $M$ is not a multiple of $p$), then by Fermat's Little Theorem, $M^{p-1} \equiv 1 \pmod p$.
        
    - Since $ed = 1 + k(p-1)(q-1)$, we can write $M^{ed} = M \cdot (M^{p-1})^{k(q-1)}$.
        
    - $M^{ed} \equiv M \cdot (1)^{k(q-1)} \equiv M \pmod p$. (Holds)
        
- **Case 2 (for mod p):**
    
    - If $\gcd(M, p) = p$ (i.e., $M$ is a multiple of $p$), then $M \equiv 0 \pmod p$.
        
    - $M^{ed} \equiv 0^{ed} \equiv 0 \pmod p$.
        
    - Therefore, $M^{ed} \equiv 0 \equiv M \pmod p$. (Holds)
        
- The same logic applies for $\pmod q$. Since the congruence holds for both $p$ and $q$, it holds for their product $N$. **This proves RSA decryption works for all messages $M < N$.**
    

#### Practical RSA Details

- **Key Length:** Variable, but 2048 to 4096 bits are common today for security.
    
- **Block Size:** Plaintext must be $< N$. Ciphertext is always $= N$ (in bit-length).
    
- **Speed:** RSA is much **slower** than symmetric ciphers (like AES).
    
- **Use Case:** It is **not used** to encrypt long messages. It is used for **key exchange** (encrypting a _symmetric key_, which is then used to encrypt the message) or for **digital signatures**. This is called [[Hybrid Encryption]].
    

---

### Part 2: A Small RSA Example

- Let $p = 47$, $q = 59$.
    
- Modulus: $N = pq = 2773$.
    
- Totient: $\varphi(N) = (p-1)(q-1) = 46 \times 58 = 2668$.
    
- Choose a public exponent $e = 157$.
    
    - (We check $\gcd(2668, 157) = 1$).
        
- Find the private exponent $d$:
    
    - We need $d \equiv 157^{-1} \pmod{2668}$.
        
    - Using the EEA, we find $157 \times 17 - 2668 \times 1 = 1$.
        
    - Therefore, $d = 17$.
        
- **Public Key:** $(e=157, N=2773)$
    
- **Private Key:** $(d=17, N=2773)$
    

_Historical Note:_ The original RSA paper presented an example swapping $d$ and $e$. This is irrelevant; the keys are mathematically symmetric. You can choose either to be private, and the other becomes public.

**Encoding the Message:**

- Let's use 2 digits per letter (A=01, B=02, ..., blank=00).
    
- Message: `ITS ALL GREEK TO ME`
    
- Encoded blocks (since $2626 < 2773$, we can use 2 letters per block):
    
    IT | S | AL | L | GR | EE | K | TO | M | E
    
    0920 1900 0112 1200 0718 0505 1100 2015 0013 0500
    ![[Pasted image 20251030153054.png]]
    

**Encryption (Example with _wrong_ key from slide):**

- The slide example incorrectly encrypts $M$ with $d=17$ (the private key). Let's follow the slide:
    
- First block $M = 0920$.
    
- $C = M^d \pmod N = 0920^{17} \pmod{2773}$
    
- Using fast modular exponentiation: $C = 948$.
    
- Encrypted Message: `0948 2342 1084 1444 2663 2390 0778 0774 0219 1655`
    

**Decryption (with $e=157$):**

- First block $C = 948$.
    
- $M = C^e \pmod N = 0948^{157} \pmod{2773}$
    
- $M = 920$. (It works!)
    

---

### Part 3: Purposes of RSA (Dual-Use)

RSA has two main functions, depending on _which key you use to encrypt_.

- **Case 1: Encryption for [[Confidentiality]]**
    
    - **Action:** Alice encrypts a message $M$ using **Bob's PUBLIC key** $(e_B)$.
        
    - **Effect:** Everybody can encrypt, but **only Bob** (who has the corresponding private key $d_B$) can decrypt.
        
    - **Goal Achieved:** [[Confidentiality]].
        
    - _Note:_ This is vulnerable to a MitM attack if Alice gets a _fake_ public key for Bob from an attacker.
        
- **Case 2: Encryption for Signatures ([[Authenticity]] & [[Non-Repudiation]])**
    
    - **Action:** Alice "encrypts" a message $M$ using **Alice's OWN PRIVATE key** $(d_A)$.
        
    - **Effect:** **Only Alice** can encrypt, but **everybody** (who has her public key $e_A$) can decrypt to "verify" it.
        
    - **Goal Achieved:** [[Integrity]], [[Authenticity]], and a path to [[Non-Repudiation]].
        
    - This provides **no [[Confidentiality]]**.
        
- **Non-Repudiation:**
    
    - The sender of a message cannot deny having sent it.
        
    - This is _not_ provided by **HMAC**, because in an HMAC, two parties share the _same_ key. A judge can't tell which of the two parties created the message.
        
    - With private-key encryption, only the owner of the private key could have created the message.
        

---

### Part 4: "Textbook" RSA Weaknesses and Attacks

The "textbook" RSA algorithm (just $M^e \pmod N$) is **NOT secure** and must never be used in practice. It is vulnerable to many attacks.

#### Weakness 1: Existential Forgery

Using private-key encryption directly for signatures is insecure.

- **Naive Signature:** Alice sends $(M, S)$ where $S = E_{V}(M)$ (Message $M$ encrypted with her private key $V$).
    
- **Naive Verification:** Bob checks if $E_{U}(S) = M$ (decrypts $S$ with her public key $U$).
    
- **The Forgery Attack:**
    
    1. Attacker Fran (pretending to be Alice) wants to forge a signature.
        
    2. Fran creates a random binary file $R$ (this will be the "signature").
        
    3. Fran computes $D = E_{U}(R)$ (i.e., "decrypts" the random file $R$ with Alice's _public_ key).
        
    4. Fran sends the pair $(D, R)$ to Bob.
        
    5. Bob verifies: He checks if $E_{U}(R) = D$. This is true by definition!
        
    6. Bob accepts the pair $(D, R)$ as a valid message $D$ signed by Alice, even though $D$ is probably meaningless. This is a successful **existential forgery**.
        
- **The REAL RSA Signature (Solution):**
    
    - We sign a **hash** of the message, not the message itself.
        
    - **Signature:** Alice sends $(M, E_V(H(M)))$, where $H$ is a cryptographic hash function ([[OWF]]).
        
    - **Verification:** Bob receives $(M, S)$.
        
        1. Bob computes $h_1 = H(M)$.
            
        2. Bob computes $h_2 = E_U(S)$ (decrypts the signature).
            
        3. If $h_1 = h_2$, he accepts.
            
    - This works because the hash $H$ provides **[[Integrity]]** and is an **[[OWF]]**, preventing the forgery attack. The encryption by $V$ provides **[[Authenticity]]**.
        

#### Weakness 2: Factoring $N$

- If an attacker can factor $N$ into $p$ and $q$, they can compute $\varphi(N)$ and then compute the private key $d$ from the public key $e$.
    
- Factoring is **believed hard**, but requires careful key generation:
    
    - $p$ and $q$ must be **large enough** (~2048 bits for $N$).
        
    - $p$ and $q$ must **not be too close** together.
        
    - $(p-1)$ and $(q-1)$ must have large prime factors (to foil Pollard's rho algorithm).
        
- **Open Problem:** We know (Factoring $N$) $\implies$ (Break RSA). Is the reverse true? (Break RSA) $\implies$ (Factoring $N$)? This is not known.
    

#### Weakness 3: Deterministic Encryption

- Textbook RSA is deterministic: $RSA(M)$ always produces the same $C$.
    
- This leaks information. An attacker can build a dictionary of encrypted messages.
    
- **Attack:** If an adversary knows the message is either $m_1$ or $m_2$, they can encrypt both with the public key and see which one matches the ciphertext.
    
- **Solution:** **Add random padding** to the message before encrypting.
    

#### Weakness 4: Malleability (Multiplicative Property)

- RSA has a multiplicative homomorphism:
    
    $RSA(m_1) \cdot RSA(m_2) = (m_1^e)(m_2^e) \pmod N = (m_1 \cdot m_2)^e \pmod N = RSA(m_1 \cdot m_2)$
    
- **Attack:** An attacker can modify a ciphertext $C$ in a predictable way without knowing the plaintext $M$.
    
- **Chosen Ciphertext Attack (Example):**
    
    1. Attacker wants to decrypt $C = M^e \pmod n$.
        
    2. Attacker chooses a random $X$ and computes $C' = C \cdot X^e \pmod n$.
        
    3. Attacker asks a "decryption oracle" (a server that decrypts messages) to decrypt $C'$.
        
    4. The oracle returns $(C')^d = (C \cdot X^e)^d = C^d \cdot (X^e)^d = M \cdot X \pmod n$.
        
    5. The attacker divides this result by $X$ to get the original message $M$.
        
- **Solution:** **Padding**. The oracle will decrypt $C'$, find that the padding is invalid, and return an error instead of the plaintext.
    

#### Weakness 5: Attacks on Small Values

- **Easy Messages:** If $M=0, 1,$ or $N-1$, then $RSA(M) = M$.
    
- **Small $M$ and Small $e$:** If $e=3$ and the message $M$ is small (e.g., $M=100$), then $M^e = 100^3 = 1,000,000$. If $N$ is large, $M^e < N$, so $C = M^e$. The attacker just computes the $e$-th root of $C$ (integer root, not modular) to find $M$.
    
- **Small $e$ and Related Messages:** If an attacker intercepts $c_1 = m^3 \pmod n$ and $c_2 = (m+1)^3 \pmod n$, they can use this relation to solve for $m$ algebraically.
    
- **Small $e$ and Same Message (CRT Attack):** If $e=3$ and the _same message $M$_ is sent to 3 different users (with moduli $n_1, n_2, n_3$), an attacker intercepts:
    
    - $c_1 = M^3 \pmod{n_1}$
        
    - $c_2 = M^3 \pmod{n_2}$
        
    - $c_3 = M^3 \pmod{n_3}$
        
    - Using the [[Chinese Remainder Theorem]], the attacker can compute $M^3 \pmod{n_1 n_2 n_3}$.
        
    - Since $M^3 < n_1 n_2 n_3$, this is just $M^3$. The attacker computes the cube root to find $M$.
        
- **Solution to all:** **Add random padding** (e.g., "salt") to every message.
    

#### Weakness 6: Implementation Attacks

- **Timing Attacks:** Based on the time required to compute $C^d \pmod N$.
    
- **Energy Attacks:** Based on the power consumed by a smart card to compute $C^d \pmod N$.
    
- **Solution:** Add random delays or "blinding" steps in the implementation.
    

---

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

|**Standard**|**Title**|**Function / Description**|**Status / Adoption**|
|---|---|---|---|
|**PKCS #1**|RSA Cryptography Standard|RSA encryption, signatures, and padding (like OAEP, PSS).|Widely used; parts adopted in **RFC 8017**.|
|**PKCS #3**|Diffie-Hellman Key Agreement|Diffie–Hellman key exchange format.|Obsolete; replaced by IETF standards.|
|**PKCS #5**|Password-Based Cryptography|Defines PBKDF1, PBKDF2 (key derivation).|Widely used; part of **RFC 8018**.|
|**PKCS #6**|Extended Certificate Syntax|Defines certificate extensions.|Obsolete; superseded by **X.509v3**.|
|**PKCS #7**|Cryptographic Message Syntax|Format for signed/enveloped data (S/MIME).|Superseded by CMS (**RFC 5652**).|
|**PKCS #8**|Private Key Information Syntax|Standard for storing private keys (encrypted or not).|Widely used (OpenSSL, Java).|
|**PKCS #9**|Selected Attribute Types|Defines attributes for use in other PKCS standards.|Still relevant.|
|**PKCS #10**|Certificate Request Syntax|Format for Certificate Signing Requests (CSRs).|Ubiquitous in TLS/PKI.|
|**PKCS #11**|Cryptographic Token Interface (Cryptoki)|API for interacting with cryptographic hardware (HSMs, smartcards).|Actively maintained by OASIS.|
|**PKCS #12**|Personal Information Exchange Syntax|Container for certs & private keys (.p12, .pfx files).|Still widely used (Windows, browsers).|
|**PKCS #15**|Cryptographic Token Information Format|Format for storing crypto objects on tokens.|Used in smartcard infrastructure.|

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
        
    - **PBKDF1** (legacy) and **PBKDF2** (the modern standard) are the most famous.
        
    - PBKDF2 "stretches" a password by mixing it with a **Salt** (a unique random value) and running it through a pseudorandom function (like HMAC-SHA256) thousands of times (the **iteration count**).
        
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

- **Purpose:** Provides **extensibility** for other PKCS standards. It is not a protocol itself, but a _library of definitions_ for "attributes" that can be attached to objects like certificates or private keys.
    
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
        
    - Used by browsers, operating systems, and VPN/Email clients to import user credentials.
        

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