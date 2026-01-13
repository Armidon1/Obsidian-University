last lesson [[7 CS  Lower Level - Asymmetric encryption]]
# Random Number Generation: An Introduction

**Tags:** #engineering #cryptography #cybersecurity #RNG #PRNG #CSPRNG

## 1. Introduction and The Importance of Randomness

> "The generation of random numbers is too important to be left to chance."
> 
> — Robert Coveyou, Oak Ridge National Laboratory

In the context of security, we cannot rely on poor design or simple "chance." Random numbers are the **foundation** of many cryptographic algorithms. If the generator is weak, the entire security system collapses.

**Why do we need them?**

- **Session Keys:** Temporary keys to encrypt communications (avoid key guessing).
    
- **Nonces and Salts:** Unique values to prevent replay attacks or strengthen passwords.
    
- **Key Generation:** Creating public/private key pairs 1.
    

> [!tip] Exam Focus
> 
> The security of a generator is measured against the computational power of the adversary.
> 
> Given a sequence of past session keys, the probability of correctly predicting the next one must be negligible2.

---

## 2. Generators of Randomness: TRNG vs PRNG

There are two principal methods to generate random numbers.

### A. True Random Number Generators (TRNG)

These rely on **physical phenomena** expected to be intrinsically random.

- **Examples:** Temperature, atmospheric noise, radioactive decay, thermal noise.
    
- **Issues:** They may have biases (require "whitening") and measurement precision limits the extraction of entropy bits3.
    

### B. Pseudo-Random Number Generators (PRNG)

This is the most common computational approach. It uses a **deterministic algorithm**.

- **Mechanism:** Given an initial input (**Seed**), the algorithm produces a long sequence of numbers that _look_ random.
    
- **The Paradox:** Since the algorithm is deterministic, providing the same Seed results in the **exact same output sequence**4.
    

`![[SCREEN_SLIDE_PRNG_DIAGRAM]]`

> [!abstract] Visual Analysis
> 
> What to look at: The diagram typically shows an input (Seed) entering a "box" (Algorithm) to produce a stream of numbers.
> 
> Meaning: Security relies entirely on the secrecy and unpredictability of the Seed. According to Kerckhoffs's Principle, the adversary knows the algorithm; they must not know the Seed.

---

## 3. The Source of Entropy (The Seed)

Since the PRNG is deterministic, true randomness must come from the **Seed**. We must collect data that is difficult for a remote attacker to replicate.

**Common Sources:**

- **System/Network:** Clock, free disk space, number of files, I/O queues, packet inter-arrival times.
    
- **User Input:** Keyboard typing speed, mouse movements 5.
    

> [!example] Professor's Example: Mouse Movement
> 
> Many systems ask you to "move the mouse randomly" to generate a key. It is not magic. Even if an adversary sees you moving the mouse, they cannot replicate the exact trajectory and timing down to the millisecond. This timing difference provides the necessary entropy bits.

### The "Quantity of Entropy" Problem

We often have the illusion of randomness.

- **Clock Granularity:** Using only milliseconds might yield only ~10 bits of randomness ($2^{10} \approx 1000$ combinations).
    
- **Day/Hour:** These are easily guessable by an attacker.
    
- **Solution:** Mix several sources using crypto functions (Hashing) 6.
    

---

## 4. Case Studies: Historical Failures

Errors in RNG implementation have caused massive vulnerabilities in the past.

### Case 1: Netscape 1.1 (1996)

Netscape used a weak generator for SSL keys. The source code revealed the seed was derived from predictable values.

### [Implementation / Code]

**Here is the exact implementation shown in the slides:**

```C
/* Netscape 1.1  seeding & key generation (1996) */

global variable seed;

RNG_CreateContext()
    (seconds, microseconds) = time of day;
    /* Time elapsed since 1970 */
    pid = process ID; ppid = parent process ID;
    a = mklcpr(microseconds);
    b = mklcpr(pid + seconds + (ppid << 12));
    seed = MD5(a, b);
    MD5 broken since 1996
    /* not cryptographically significant */
mklcpr(x)
    return ((0xDEECE66D * x + 0x2BBB62DC) >> 1);

RNG_GenerateRandomBytes()
    x = MD5(seed);
    seed = seed + 1;
    return x;
```

> [!abstract] Code Analysis
> 
> Vulnerability:
> 
> - `seconds` are known.
>     
> - `pid` and `ppid` were often predictable or sequential on UNIX systems.
>     
> - **Attack Vector:** An attacker could send an email to the `sendmail` daemon. The reply's **Message-ID** contained the PID.
>     
> - **Result:** Entropy collapsed to ~47 bits. The key could be broken in minutes 7.
>     

### Case 2: Debian OpenSSL (2008)

A catastrophic bug introduced by "cleaning up" code to satisfy a debugger.

- **The Cause:** A developer used **Valgrind** (debug tool) which warned about "Use of uninitialized variable".
    
- **The "Fix":** The developer removed the line `MD_Update(&m,buf,j);` which added uninitialized entropy to the pool.
    
- **The Result:** The only variable left was the **Process ID** (max 32,768 on Linux).
    
- **Impact:** Any SSH/SSL key generated on Debian/Ubuntu during that period was trivially guessable (only ~32,000 possibilities) 8.
    

> [!failure] Common Pitfall
> 
> **Divulging the Seed:** Never include the seed source (like the time of day) in unencrypted parts of the message (e.g., headers), as happened in some implementations 9.

---

## 5. PRNG vs. CS-PRNG

Not all generators are suitable for security. We must distinguish between standard PRNG and **Cryptographically Secure** PRNG.

`![[SCREEN_SLIDE_PRNG_VS_CSPRNG]]`

> [!abstract] Visual Analysis
> 
> What to look at: The comparison table highlighting "Predictability" and "Security Properties".
> 
> Meaning: PRNGs focus on statistical distribution (for games/simulations). CS-PRNGs focus on unpredictability (for crypto) 10.

### [Technical Logic / Math]

**Challenge: Is this a PRNG or CS-PRNG?**

```C
hash function H
random initial seed s
y = s
for i = 1 to n do
    y = H(y)
    output(y)
```

**Requirements for CS-PRNG:**

1. **Next-Bit Test:** Given $k$ bits, no algorithm can predict the $(k+1)^{th}$ bit with probability $> 50\%$.
    
2. **Forward Secrecy:** If the state is compromised, _future_ keys remain secure.
    
3. **Backward Secrecy:** If the state is compromised, _past_ keys cannot be reconstructed 11.
    

---

## 6. BSI Evaluation Criteria

The German Federal Office for Information Security (BSI) defines 4 criteria for RNG quality:

- **K1:** Sequence without obvious repeating patterns.
    
- **K2:** Indistinguishable from "true random" via statistical tests (Monobit, Poker, Runs).
    
- **K3:** Impossible to calculate past/future outputs or internal state from the **output**.
    
- **K4 (Crypto Standard):** Impossible to calculate past outputs **even if the internal state is known** (requires Forward Secrecy mechanisms) 12.
    

---

## 7. Algorithms and Practical Solutions

### A. Generator "Cipher of a Counter"

Uses a block cipher (like AES) in a cyclic manner.

**Here is the exact implementation shown in the slides:**

```C
cyclic cryptography: use counter + cipher
Meyer and Matyas, 1982
crypto algorithm E
C + 1 mod N
C
master key Km
Xi = E[Km, C + 1]
```

### B. RSA Based Generator

Exploits the mathematical difficulty of inverting RSA. Provably secure but slow.

**Here is the exact implementation shown in the slides:**

```C
prime numbers p, q
n = p∙q
integer e s.t. GCD(e, (p-1)∙(q-1)) = 1
z = seed
loop
    zi = (zi-1)^e mod n
    i = i +1
    output:  least significant bit of zi
```

### C. Blum Blum Shub (BBS)

Based on the quadratic residuosity problem.

**Here is the exact implementation shown in the slides:**

```C
choose p, q big prime s.t. p ≡ q ≡ 3 (mod 4)
n = p∙q
randomly choose s s.t. GCD(s, n) = 1
output the sequence of bits Bi

X0 = s2 mod n
for i = 1 to ∞
    Xi = (Xi-1)^2 mod n
    Bi = Xi mod 2
    return Bi
```

### D. CTR_DRBG (AES)

Current best practice (NIST SP 800-90A). Uses AES in Counter Mode with reseeding capabilities.

**Here is the exact implementation shown in the slides:**

```C
Maybe the current best (Counter mode Deterministic Random Bit Generator, 2012)
State: Key K, counter V
Block cipher: AES-128 / AES-256 in CTR mode
Generate:
    V ⟵ V + 1 (mod  2block size)
    out_block = EK(V)
    Repeat until enough bits produced
Update:  regenerate K and V by encrypting V+1, V+2, … with current K and using the output blocks to form the new state
Security: Forward & backward secure (if reseeded periodically)
```

---

## 8. Best Practices

1. **"Don't roll your own crypto":** Never invent your own generator.
    
2. **Avoid `rand()`:** Standard library functions are for simulations, not security.
    
3. **Use OS APIs:** `/dev/urandom` (Linux) or `CryptGenRandom` (Windows). These libraries handle entropy collection and hashing securely.
    
4. **Reference:** RFC 1750 13.

---
domande esame [[domande esame PRNG|qui]]
next lesson [[9 CS Lower Level - ElGamal and Digital Signature Standard (DSS)]]