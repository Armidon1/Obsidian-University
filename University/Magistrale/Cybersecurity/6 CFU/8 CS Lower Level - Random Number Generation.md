Here are the integrated notes for Obsidian, translated into English as requested.

***

# Random Number Generation

## 1. Introduction and the Importance of Randomness

> "The generation of random numbers is too important to be left to chance."
> — Robert Coveyou, Oak Ridge National Laboratory

This quote is ironic but fundamental: we cannot leave number generation to "chance" (meaning poor design), because random numbers are the foundation of many cryptographic algorithms.

When we speak generally of "random numbers," we are imprecise. In the context of security, we must always aim for the concept of a **Cryptographically Secure Pseudo-Random Number Generator (CSPRNG)**.

### Why do we need them?
We primarily use random numbers for:
- **Session Keys:** Temporary keys to encrypt communications.
- **Nonces and Salts:** Unique values to prevent replay attacks or to strengthen passwords.

> [!tip] Fundamental Concept: The Adversary
> The security of a generator is measured against the power of the adversary.
> If an attacker knows all **past session keys**, the probability of them guessing the **next** one must be **negligible** (at least for an adversary with polynomial computational power).

---

## 2. Generation Methods: TRNG vs. PRNG

There are two main approaches to obtaining "randomness".

### A. True Random Number Generators (TRNG)
These rely on **physical phenomena** that we expect to be intrinsically random.
- **Examples:** Temperature, atmospheric noise, radioactive decay, pressure.
- **Problems:**
1. **Bias:** Physical values can be unbalanced. It is often necessary to compensate for these biases ("whitening").
2. **Measurement Precision:** If we measure time or temperature, precision is limited. We cannot have infinite decimal places. This reduces the number of real entropy bits we can extract.

### B. Pseudo-Random Number Generators (PRNG)
This is the most common computational approach. It uses a **deterministic algorithm**.
- **Mechanism:** Given an initial input (**Seed**), the algorithm produces a sequence of numbers that *look* random.
- **The Paradox:** Since the algorithm is deterministic, if I provide the same input (Seed), I will *always* get the same output sequence.

> [!img-desc] Analysis of the Generator Schema
> `![[Insert PRNG block diagram with Seed and Salt]]`
>
> **What to look at:** The diagram shows a "box" (the algorithm) that takes a Seed as input (often combined with a Salt).
> **Meaning:** The real input is the sum of Seed + Salt. For the adversary, guessing the output must be as hard as guessing the secret input. According to **Kerckhoffs's Principle**, the adversary knows the algorithm, so security relies entirely on the secrecy and unpredictability of the initial Seed.

---

## 3. The Source of Entropy (The Seed)

If the PRNG is deterministic, true randomness must come from the **Seed**. Where do we get it?

### System and User Sources
We need to collect data that is difficult for a remote attacker to replicate:
- **System Clock:** Widely used, but dangerous if used alone (see below).
- **Disk State:** Free space, head position.
- **Network:** Packet inter-arrival times.
- **User:** Mouse movements, typing speed on the keyboard.

> [!example] The Mouse Example
> Many libraries ask the user to "move the mouse randomly" to generate a key.
> **Prof's Note:** It's not that mouse movement is magical. The point is that, even if the adversary knows you are moving the mouse, the probability of them replicating *exactly* the same trajectory and timing (down to the millisecond) is extremely low.

### The Quantity of Entropy Problem
We often have the illusion of having a lot of randomness, but we have very little. We need to be quantitative.
- **Time Stamp Example:** Using date and time as a seed. The adversary knows the day and probably the hour. Only the milliseconds remain uncertain.
* If the granularity is 10ms, we are talking about roughly **10 bits of randomness** ($2^{10} \approx 1000$ combinations).
* An attacker can try 1000 combinations in an instant. It is too little.

**Solution:** Do not use a single source. Take everything (time, mouse, network), mix it together (via **Hashing**) to obtain a robust seed.

---

## 4. Case Studies: Historical Failures

The professor highlights how errors in generator implementation have caused critical vulnerabilities.

### Case 1: Netscape 1.1 (1996)
Netscape used a generator to create SSL keys. The source code (reverse-engineered) revealed the seed was created like this:

`![[Insert Netscape RNG_CreateContext C code]]`

> [!img-desc] Code Analysis
> **What to look at:** The variables used for the seed are `time_of_day` (seconds and microseconds), `pid` (Process ID), and `ppid` (Parent Process ID).
> **Meaning:** These look like variable data, but for an attacker with an account on the same machine (or who can query the server), they are predictable.

- **The Vulnerability:**
* `seconds` are known (just look at the clock).
* `pid` and `ppid` on Unix machines of that era were often predictable or sequential.
* **The `sendmail` Attack:** The prof explains that by sending an email to the server, the server responded with a header containing the **Message-ID**. At that time, the Message-ID was generated using the current Process ID.
* **Result:** The attacker obtained the PID, knew the time, and the only unknown remained the microseconds. Entropy collapsed to about **47 bits** (or less), making brute-forcing the SSL key possible in minutes/hours.

### Case 2: Debian OpenSSL (2008)
A catastrophic bug introduced "for code cleanliness".

- **The Event:** A developer used debug tools (like *Valgrind* or *Purify*) on the OpenSSL code. These tools flagged a warning: "Use of uninitialized variable".
- **The "Fix":** The developer removed the line of code that added uninitialized entropy to the pool.
- **The Consequence:** The only variable left to generate keys was the **Process ID**.
* On Linux, the maximum PID was 32,768.
* **Disaster:** There were only ~32,000 possible SSH/SSL keys worldwide for that Debian version. An attacker could try them all in a few seconds.

> [!tip] Exam Note
> These examples demonstrate that even if the cryptographic algorithm (e.g., RSA, AES) is secure, if the random number generator is weak (low entropy or software bugs), the entire system collapses.

---

## 5. PRNG vs. CS-PRNG (Cryptographically Secure)

Not all pseudo-random generators are suitable for security.

### Standard Pseudo-Random Number Generator (PRNG)
- **Use:** Simulations, video games, debugging.
- **Properties:** Good statistics (uniform distribution), speed.
- **Flaw:** If I know the internal state, I can predict all future numbers.

### Cryptographically Secure PRNG (CS-PRNG)
- **Use:** Cryptography (keys, nonces).
- **Fundamental Property:** **Unpredictability**.
* Even if the adversary sees a long sequence of numbers, they must not be able to guess the next one (Next-Bit Test).
* They must not be able to deduce the internal state or past numbers (**Backward Secrecy**).
* If the state is compromised, they should not be able to deduce future keys if new entropy is added (**Forward Secrecy**).

> [!img-desc] PRNG vs CS-PRNG Comparison Table
> `![[Insert PRNG vs CS-PRNG comparison table from slide]]`
>
> **Meaning:** Note how the CS-PRNG requires resistance to cryptanalysis, not just statistical tests.

---

## 6. BSI Evaluation Criteria

The German agency BSI defines 4 classes of generators:
- **K1:** Sequence without obvious repeating patterns (basic statistics).
- **K2:** Statistically indistinguishable from true random (advanced statistical tests like Monobit, Runs).
- **K3:** Impossible to calculate past or future outputs or the internal state starting from the output.
- **K4 (Cryptographic Standard):** Impossible to calculate past outputs **even knowing the internal state** (Forward Secrecy mechanism).

> [!tip] Important
> For real security applications, **K4** compliance is required.

---

## 7. Algorithms and Practical Solutions

The prof presents several solutions for building a CS-PRNG.

### A. Cyclic Approach (Cipher Counter)
Uses a block cipher (e.g., AES) and a counter.
$$Random\_Value = E_K(Counter + i)$$
By incrementing the counter and encrypting it with a secret key, I get unpredictable numbers (as long as the key remains secret). This is similar to **AES-CTR** mode.

### B. RSA-Based Generator
Exploits the mathematical difficulty of RSA.
$$z_{i} = (z_{i-1})^e \pmod n$$
The LSB (Least Significant Bit) of the result is taken as the random bit. It is **provably secure** (if you can predict the bit, you can invert RSA), but it is **very slow**.

### C. Blum Blum Shub (BBS)
Very famous in theory. Based on the quadratic residuosity problem.
* Choose two large prime numbers $p, q$ congruent to 3 mod 4.
* $$x_{i} = (x_{i-1})^2 \pmod n$$
* Extract the parity bit.
- **Security:** Very strong (linked to factoring), but slow.

### D. AES-CTR DRBG (Modern Standard)
This is what is used today (e.g., NIST SP 800-90A).
* Uses AES in counter mode.
* Includes **Reseeding** mechanisms: periodically the algorithm stops, collects new entropy from the system, updates the key, and restarts.
* Guarantees both *Forward* and *Backward Secrecy*.

---

## 8. Conclusions and Best Practices

1. **Never invent your own generator:** "Don't roll your own crypto".
2. **Avoid `rand()` in C:** Standard library functions (like `rand()` in C or Java) are great for tests but are **not** cryptographically secure.
3. **Use OS libraries:** `/dev/urandom` on Linux or Windows cryptographic APIs (`CryptGenRandom`). These handle entropy collection from various sources (network, disk, keyboard) and secure hashing for us.
4. **Bruce Schneier advises:** Vulnerabilities in RNGs are easy to create by accident and very hard to detect. Rely on standard and reviewed algorithms.