# Random Number Generation: An Introduction

## 1. Introduction

> "The generation of random numbers is too important to be left to chance."
> 
> — Robert Coveyou, Oak Ridge National Laboratory

**Enrichment:** Robert Coveyou was a mathematician and pioneer in the field of pseudo-random number generators. The quote is ironic because the generation of "random" numbers by a computer is technically deterministic (based on algorithms), so leaving it to "chance" (bad design) leads to predictability, which is the enemy of security.

## 2. The Need for Randomness

In cryptography and security, random number generators (RNGs) are fundamental components. We need them for:

- **Session Keys:** Generating temporary keys for encrypting communications (e.g., TLS/SSL).
    
- **Preventing Key Guessing:** If an adversary knows a sequence of past session keys, the probability of them correctly predicting the _next_ key must be **negligible** (cryptographically speaking, close to $1/2^n$).
    
- **Nonces and Salts:** Random values used to prevent replay attacks and rainbow table attacks on passwords.
    

**Note:** A "good" random number generator suitable for cryptography is computationally expensive compared to those used for simple simulations.

## 3. Types of Generators

There are two principal methods for generating random numbers:

### A. True Random Number Generators (TRNG)

- **Mechanism:** Measure a physical phenomenon expected to be truly random.
    
- **Sources:** Thermal noise, radioactive decay, atmospheric noise, photoelectric effect.
    
- **Process:** The raw measurement usually has a bias, so it must be "whitened" or compensated to ensure uniform distribution.
    

### B. Pseudo-Random Number Generators (PRNG)

- **Mechanism:** Algorithms that produce long sequences of _apparently_ random values.
    
- **Determinism:** The sequence is fully determined by an initial value called the **Seed** or **Key**.
    
- **Implication:** If you know the seed and the algorithm, you know the entire sequence.
    

## 4. Clarifications on Randomness

- **Determinism vs. Randomness:** Deterministic computations (software) cannot generate _true_ random numbers because the output is inherently predictable based on the input.
    
- **Distinguishability:** Ideally, distinguishing a "true" random number from the output of a high-quality PRNG should be a computationally "hard" problem.
    
- **Usage:** Carefully chosen PRNGs can replace TRNGs in many applications (like stream ciphers), provided they undergo rigorous **statistical analysis** (e.g., NIST SP 800-22 test suite).
    

## 5. The Generation Process

A typical PRNG system involves:

1. **Entropy Collection:** Gathering system data or external information (high entropy).
    
2. **Seeding:** Using this data to initialize the PRNG.
    
3. **Expansion:** The PRNG program takes the short random seed and expands it into a long sequence of numbers.
    

**Security Goal:** If an adversary observes a long sequence of output, it must be computationally infeasible for them to guess the **next** output number (Next-Bit Unpredictability).

## 6. Sources of Entropy (The Initial Seed)

To seed a generator, we need unpredictable data sources.

**Machine/System Sources:**

- System Clock (often low entropy on its own).
    
- Free disk space or number of files.
    
- OS Information: I/O queue states, buffer states.
    
- Network: Inter-arrival time of packets (highly variable).
    

**User Sources:**

- Human Interface Device (HID) timing: Precise timing of keystrokes and mouse movements.
    

**Enrichment:** In Linux systems, these sources feed into the "entropy pool" managed by the kernel, accessible via `/dev/random` (blocking, potentially true random) and `/dev/urandom` (non-blocking, CSPRNG).

## 7. Entropy Quantity

- **Quality vs. Quantity:** Many sources provide very few bits of _real_ randomness (entropy).
    
- **Example (Clock):** Using the system time is dangerous.
    
    - The date/hour/minute is predictable.
        
    - Only the milliseconds (or microseconds) provide randomness.
        
    - Milliseconds $\approx$ 10 bits of randomness ($2^{10} = 1024$ possibilities), which is trivial to brute-force.
        
- **Solution:** Mix (hash) multiple sources of randomness together to accumulate enough entropy.
    

## 8. Common Mistakes in Implementation

1. **Small Initial Seed:** A 16-bit seed offers only 65,536 combinations. An attacker can test them all in milliseconds.
    
2. **Using Current Time:** If the clock granularity is 10ms, and the attacker knows the approximate time (e.g., the hour), the search space reduces to ~360,000 choices.
    
3. **Divulging the Seed:**
    
    - _Case Study:_ An implementation used the time of day as a seed for message encryption.
        
    - _The Flaw:_ The application included the exact time of day in the **unencrypted header** of the message, giving the attacker the seed immediately.
        

## 9. Case Study: Netscape 1.1 Vulnerability (1996)

Early web browsers had critical flaws in SSL implementation due to poor RNGs.

**The Vulnerable Code:**

```C
/* Netscape 1.1 seeding logic */
RNG_CreateContext() {
    (seconds, microseconds) = time_of_day;
    pid = process_ID;
    ppid = parent_process_ID;
    
    // mklcpr is a simple linear congruential generator
    a = mklcpr(microseconds);
    b = mklcpr(pid + seconds + (ppid << 12));
    
    seed = MD5(a, b); // MD5 is now broken, but that wasn't the main issue here
}
```

**The Analysis:**

- **Attack Surface:** If the attacker has a user account on the same UNIX machine (shared server), they can determine `pid` and `ppid`.
    
- **Entropy Calculation:**
    
    - `seconds`: Known.
        
    - `pid/ppid`: Often predictable or discoverable.
        
    - `microseconds`: The only real unknown, providing ~20 bits.
        
- **Result:** The "secret" key had at most **47 bits of entropy**, often much less.
    
- **Exploitation:**
    
    - `ppid` is often 1 (init) or close to `pid`.
        
    - Hackers could send an email to the server; the `Message-ID` returned by `sendmail` reveals the current `pid` state, allowing precise guessing of the browser's state.
        

## 10. Case Study: Debian OpenSSL Bug (2008)

A catastrophic failure in the Debian distribution (and Ubuntu) affected SSH and SSL keys for two years (2006-2008).

- **The Cause:** A developer removed the line `MD_Update(&m,buf,j)` from `md_rand.c`.
    
- **The Reason:** Tools like **Valgrind** and **Purify** complained about the use of "uninitialized data". In crypto, using uninitialized memory is often a _feature_ to add entropy, but it looks like a bug to debuggers.
    
- **The Consequence:** The code stopped mixing in random system data into the seed.
    
- **The Result:** The only "random" variable remaining was the **Process ID (PID)**.
    
    - Max PID on Linux is default 32,768.
        
    - The entire keyspace collapsed to just ~32k possible keys.
        
    - Any SSH key generated on these systems was trivially guessable.
        

## 11. Bruce Schneier's Commentary

> "Security flaws in random number generators are really easy to accidentally create and really hard to discover after the fact."

Historically, agencies like the NSA have weakened commercial cryptography not by breaking the encryption algorithms (like AES), but by **reducing the entropy** of the RNGs, making the keys predictable. (Example: The Dual_EC_DRBG scandal).

### Random Generator Folklore
![[Pasted image 20251119172229.png]]


## 12. PRNG vs. CS-PRNG

Not all pseudo-random generators are safe for crypto.

|**Feature**|**PRNG (Standard)**|**CS-PRNG (Cryptographically Secure)**|
|---|---|---|
|**Goal**|Speed, statistical randomness (simulations, games).|Unpredictability, security (keys, nonces).|
|**Checks**|Statistical tests (Uniformity, correlation).|Statistical tests + **Cryptanalysis resistance**.|
|**Predictability**|If state is known, future is known.|Even with partial info, future outputs are infeasible to guess.|
|**Seeding**|Simple, often static.|High-entropy sources, periodic re-seeding.|
|**Example**|Mersenne Twister, Linear Congruential.|AES-CTR, ChaCha20, Blum Blum Shub.|

## 13. A Challenge

Consider this generator:

```C
y = s (random seed)
for i = 1 to n:
    y = H(y)
    output(y)
```

**Is this a PRNG or CS-PRNG?**

- It depends on `H`. If `H` is a cryptographic one-way hash function (like SHA-256), this acts as a CS-PRNG because identifying the internal state `s` from `y` is hard (pre-image resistance). However, disclosing `y` allows calculating all _future_ `y` values (no forward secrecy in this raw form).
    

## 14. BSI Evaluation Criteria

The German Federal Office for Information Security (BSI) defines classes for RNGs:

- **K1:** Sequence has no obvious repeating patterns (low probability of long identical runs).
    
- **K2:** Statistically indistinguishable from true random (passes tests like Monobit, Poker, Runs, Autocorrelation).
    
- **K3 (Backward Secrecy):** Given the output, an attacker cannot calculate _past_ or _future_ outputs or the internal state.
    
- **K4 (Forward Secrecy):** Even if the **internal state** is compromised, an attacker cannot deduce _past_ outputs.
    

**Rule:** For cryptography, only **K4** is acceptable.

## 15. CS-PRNG Requirements

To be Cryptographically Secure, a generator must pass:

1. **Ordinary PRNG tests:** Statistical randomness (K1/K2).
    
2. **The Next-Bit Test:** Given the first $k$ bits, there is no polynomial-time algorithm that can predict bit $k+1$ with probability $> 50\% + \epsilon$.
    
3. **State Compromise Extension:**
    
    - **Backtracking Resistance:** If state is revealed at time $T$, outputs from time $< T$ remain secure.
        
    - **Prediction Resistance:** If new entropy is injected, knowledge of the state at time $T$ shouldn't allow predicting state at $T+1$ (assuming re-seeding).
        

## 16. Examples of Generators

### A. "Cipher of a Counter" (Cyclic Crypto)

- **Concept:** Use a block cipher (like AES) and a counter.
    
- **Formula:** $X_i = E_K(\text{Counter} + i)$
    
- **Security:** Relies on the strength of the block cipher $E$ and the secrecy of Key $K$. This is essentially **AES-CTR** mode.
    

### B. RSA-Based Generator

- **Setup:** Primes $p, q$; Modulus $n = p \cdot q$; Public exponent $e$.
    
- **Algorithm:**
    
    - $z_0 = \text{seed}$
        
    - $z_{i} = (z_{i-1})^e \pmod n$
        
    - Output: The Least Significant Bit (LSB) of $z_i$.
        
- **Security:** Based on the hardness of the RSA problem. Very slow but provably secure.
    

### C. ANSI X9.31 RNG (Deprecated)

- **Mechanism:** Uses AES or 3DES.
    
- **State:** Key $K$, Seed $V$, Time $DT$.
    
- **Process:** Updates $V$ and generates output $R$ by encrypting the XOR sum of Time and previous state.
    
- **Status:** Deprecated in 2016 due to potential vulnerabilities and better alternatives.
    

### D. Blum Blum Shub (BBS)

- **Setup:** $p, q$ large primes where $p \equiv q \equiv 3 \pmod 4$. $n = p \cdot q$. Seed $s$ coprime to $n$.
    
- **Algorithm:**
    
    - $x_0 = s^2 \pmod n$
        
    - $x_i = (x_{i-1})^2 \pmod n$
        
    - Output: Parity bit (or last few bits) of $x_i$.
        
- **Significance:** Security reduces directly to the difficulty of the **Quadratic Residuosity Problem** (related to factoring). Very strong, but slow.
    

### E. CTR_DRBG (AES) - Current Standard

- **Definition:** Counter mode Deterministic Random Bit Generator (NIST SP 800-90A).
    
- **Mechanism:** Uses AES-128 or AES-256.
    
- **Process:**
    
    - Increment a counter $V$.
        
    - Encrypt $V$ with Key $K$ to get output block.
        
    - Periodically "reseed" (update $K$ and $V$ using new entropy).
        
- **Properties:** Provides Forward and Backward secrecy. Widely used in modern OSs and SSL libraries.
    

## 17. Conclusion on Implementation

- **Don't Roll Your Own:** Programming language built-ins like `rand()` or `Math.random()` are usually Linear Congruential Generators (LCGs). They are **not** secure.
    
- **Best Practice:**
    
    - Use OS-provided CSPRNGs (`/dev/urandom`, `CryptGenRandom`).
        
    - Hash together as many entropy sources as possible (disk seek times, keystrokes, network stats).
        
    - Refer to **RFC 4086** (replaces RFC 1750) for randomness recommendations.