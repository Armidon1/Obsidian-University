last lesson [[2 CS - Stream Ciphers]]

---
# Block Ciphers

## 1. Introduction and Definition

A **block cipher** is a fundamental cryptographic protocol that operates on fixed-length groups of bits, called blocks.

- **Core Mechanism**: It uses a deterministic algorithm and a secret key of a fixed number of bits to transform a plaintext block ($P$) into a ciphertext block ($C$).
    
- **Mathematical Notation**: Often denoted as $C = E_k(P)$, where $E$ is the encryption function and $k$ is the key.
    
- **Key Features**:
    
    - **Fixed-size blocks**: Commonly 64 bits (older ciphers like DES) or 128 bits (modern ciphers like AES).
        
    - **Determinism**: The same input block and same key _always_ produce the exact same ciphertext.
        
    - **Reversibility**: The function must be invertible. Decryption is the reverse transformation using the same key: $P = D_k(C)$.
        

> **Visual Analogy**: Imagine plaintext as a piece of clay and the key as a custom mold. The cipher presses the mold onto the clay to shape it into ciphertext. The same mold always produces the same shape.

## 2. Block Ciphers vs. Stream Ciphers

While block ciphers work on large chunks of data at once, **stream ciphers** encrypt data one bit or one byte at a time.

|**Feature**|**Block Cipher**|**Stream Cipher**|
|---|---|---|
|**Unit of Operation**|Fixed blocks (e.g., 128 bits)|Individual bits/bytes|
|**Analogy**|Stamping machine|Faucet (continuous flow)|
|**Best Use Case**|Structured data (files, DBs)|Real-time communication|

- **Why Block Ciphers for Structured Data?**
    
    - Files (PDF, DOCX) and database records have known formats and regular sizes ideal for chunking.
        
    - Operating systems read/write disk sectors in blocks (e.g., 512 or 4096 bytes), which aligns naturally with block cipher operation.
        

## 3. Desired Cryptographic Properties

To be secure against cryptanalytic attacks, a block cipher needs more than just reversibility.

- **Avalanche Effect**: A small change in the input (e.g., flipping just one bit) should cause a drastic change in the output (ideally flipping ~50% of output bits).
    
- **Non-linearity**: The relationship between plaintext and ciphertext should not be expressible by simple linear equations, preventing easy mathematical reversal. This is often achieved using **S-boxes** (Substitution boxes).
    
- **Key Sensitivity**: A tiny difference in keys should result in vastly different ciphertexts.
    

### Applications

Block ciphers are ubiquitous in modern security:

- **Data at Rest**: Full disk encryption (e.g., BitLocker), file encryption, encrypted databases.
    
- **Data in Transit**: Encrypted communication packets (e.g., TLS often uses block ciphers in specific modes like GCM).
    

## 4. History and Evolution of Algorithms

### Late 20th Century Designs

- **[[DES]] (Data Encryption Standard) (1976)**:
    
    - 64-bit block, **56-bit key**.
        
    - Developed by IBM, approved by US NIST. The small 56-bit key was controversial and is now considered easily breakable by brute force (broken in <23 hours in 1999).
        
    - Vulnerable to linear cryptanalysis (Matsui's attack requires $2^{43}$ known plaintext pairs).
        
- **IDEA (1991)**: 64-bit block, 128-bit key. Still considered generally strong, but older.
    
- **Blowfish (1993)**: 64-bit block, variable key (32-448 bits). Strong but deprecated in favor of modern alternatives; known for a slow key schedule which makes it good for password hashing (e.g., bcrypt).
    
- **RC5 (1994)**: Highly variable parameters (block size 32/64/128, key 0-2040 bits, rounds 0-255).
    

### The AES Competition (late 1990s)

Due to DES's growing weakness, NIST called for a new standard in 1997. It was an open international competition with 15 proposals and 6 finalists.

- **Winner (2001)**: **Rijndael**, developed by Belgian cryptographers Daemen and Rijmen, became **AES (Advanced Encryption Standard)**.
    
- **AES Specs**: 128-bit block size; key sizes of 128, 192, or 256 bits.
    
- **Why Rijndael won**: It offered the best balance of security, software/hardware speed, and simplicity compared to other strong finalists like Serpent (more secure but slower) and Twofish.
    

### AES Internal Structure

AES is a Substitution-Permutation Network (SPN), unlike DES which is a Feistel network. It operates in rounds (10-14 depending on key size).

- **SubBytes**: Non-linear substitution for confusion.
    
- **ShiftRows & MixColumns**: Permutation/mixing layers for diffusion.
    
- **AddRoundKey**: XORing the data with a subkey derived from the main key.
    

## 5. Iterating Block Ciphers & Attacks

### Triple DES ([[3DES]])

To extend the life of DES, it was applied three times.

- **Construction**: $C = E_{k3}(D_{k2}(E_{k1}(P)))$ (EDE mode is most common for backward compatibility).
    
- **Key Length Illusion**: Using 3 distinct 56-bit keys seems to offer $56 \times 3 = 168$ bits of security.
    
- **Effective Security**: Due to the **Meet-in-the-Middle (MITM)** attack, the real security is roughly **112 bits**.
    

### Meet-in-the-Middle (MITM) Attack

Not to be confused with _Man_-in-the-Middle, this is a cryptanalytic attack against iterated ciphers.

- **Concept**: When attacking 2DES ($E_{k2}(E_{k1}(P))$), instead of brute-forcing $k1$ and $k2$ together ($2^{112}$), the attacker:
    
    1. Encrypts plaintext $P$ with all possible $k1$ values and stores them in a huge lookup table (requires $2^n$ memory).
        
    2. Decrypts ciphertext $C$ with all possible $k2$ values.
        
    3. Checks for matches between the two resulting sets. A match reveals a potential $(k1, k2)$ pair.
        
- **Impact**: Reduces the time complexity of breaking 2 iterations to roughly that of 1 iteration, but requires massive memory. This is why "2DES" is rarely used and we jumped straight to 3DES.

---

# AES (Advanced Encryption Standard)

## 1. Introduction to AES

**[[AES]] (Advanced Encryption Standard)** is the current globally accepted standard for symmetric encryption, replacing the aging DES.

- **Origin**: Originally named **Rijndael** (standardized in 2001 by NIST).
    
- **Block Size**: Strictly **128 bits** (16 bytes).
    
    - _Note: The original Rijndael algorithm allowed for 192 and 256-bit block sizes, but the AES standard fixed it at 128 bits for simplicity and efficiency._
        
- **Key Lengths**: Supports 128, 192, or 256 bits.
    
- **Mathematics**: heavily relies on **Finite Field arithmetic** (specifically $GF(2^8)$), making it efficient in both hardware and software.
    

## 2. Mathematical Foundations

Understanding AES requires some background in number theory and abstract algebra.

### Noteworthy Math Concepts

- **[[Euler's totient function]]  $\varphi(n)$**: Counts the number of positive integers less than $n$ that are relatively prime ([[Coprime]]) to $n$.
    
- **[[Euler's Theorem]]**: If $a$ and $n$ are [[Coprime]], then $a^{\varphi(n)} \equiv 1 \pmod n$. This is a generalization of [[Fermat's Little Theorem]] and is crucial for public-key cryptography (like [[RSA]]), though less directly used in [[AES]] encryption itself.
    
- **[[Bézout's identity]]**: For any non-zero integers $a$ and $b$, let $d = GCD(a,b)$. There exist integers $x$ and $y$ such that $ax + by = d$.
    
    - These coefficients $x,y$ can be found using the **[[Extended Euclidean Algorithm]]**, which is vital for finding multiplicative inverses in finite fields (used in the AES S-Box).
        

### Finite Fields (Galois Fields)

AES does not use standard integer arithmetic; it uses arithmetic within a finite field to ensure results always stay within a fixed number of bits (a byte).

- **Definition**: A finite field $GF(p^k)$ is a field with a finite number of elements, specifically $p^k$ where $p$ is a prime and $k$ is a positive integer.
    
- **Uniqueness**: For every prime power $p^k$, there is a unique finite field of that size.
    
- **AES Usage**: AES uses **$GF(2^8)$**. This means elements are 8-bit polynomials (bytes).
    
    - **Addition**: Performed as bitwise **XOR** (since $1+1=0 \pmod 2$). This is extremely fast.
        
    - **Multiplication**: Polynomial multiplication followed by reduction modulo an irreducible polynomial $m(x)$.
        
        - AES standard irreducible polynomial: $m(x) = x^8 + x^4 + x^3 + x + 1$.
            
        - For efficiency, multiplication in $GF(2^8)$ is often implemented using lookup tables (like `alogs` tables).
            

## 3. AES Design Rationale

Why was Rijndael chosen as AES?

1. **Security**: Resistant to all known attacks (linear and differential cryptanalysis) at the time of selection.
    
2. **Efficiency**: Excellent speed in both software (PCs) and hardware (dedicated chips).
    
3. **Compactness**: Code can be very small, making it suitable for smart cards and restricted devices.
    
4. **Simplicity**: The design is clean and relies on well-understood algebraic structures.
    

## 4. AES Internal Specification

AES operates on a $4 \times 4$ matrix of bytes called the **State**.

- **Input**: 128 bits are arranged into this $4 \times 4$ grid ($16$ bytes: $A_{0,0}$ to $A_{3,3}$).
    
- **Key**: The initial key is also arranged in a similar matrix (size depends on key length).
    

### High-Level Algorithm

AES is an iterated cipher consisting of **Rounds**.

- **128-bit key**: 10 Rounds
    
- **192-bit key**: 12 Rounds
    
- **256-bit key**: 14 Rounds
    

**Pseudocode Structure:**

Plaintext

```
AES(State, Key) {
    KeyExpansion(Key, ExpandedKey)
    AddRoundKey(State, ExpandedKey[0]) // Initial whitening step
    for i = 1 to Nr-1 do {             // Standard Rounds
        Round(State, ExpandedKey[i])
    }
    FinalRound(State, ExpandedKey[Nr]) // Final round omits MixColumns
}
```

_Note: The omission of MixColumns in the final round makes encryption and decryption symmetric in structure, allowing for code reuse._

### The AES Round

Each regular round consists of four distinct transformations (layers):

1. **SubBytes (Substitution)**:
    
    - **Non-linear layer**: Every byte in the state is replaced independently using an **S-Box** (Substitution Box).
        
    - **Math**: The S-Box is derived by taking the multiplicative inverse of the byte in $GF(2^8)$ followed by an affine transformation.
        
    - **Purpose**: Provides _confusion_ and non-linearity. Without this, AES would just be a large system of linear equations, easily solvable.
        
2. **ShiftRows (Permutation)**:
    
    - **Diffusion layer (Rows)**: Rows of the state matrix are shifted cyclically to the left.
        
        - Row 0: No shift.
            
        - Row 1: Shift left by 1.
            
        - Row 2: Shift left by 2.
            
        - Row 3: Shift left by 3.
            
    - **Purpose**: Spreads data across columns, ensuring that bytes from one column interact with other columns in subsequent rounds.
        
3. **MixColumns (Mixing)**:
    
    - **Diffusion layer (Columns)**: Each column of the state is treated as a 4-term polynomial over $GF(2^8)$ and multiplied by a fixed polynomial $c(x) = 03x^3 + 01x^2 + 01x + 02 \pmod{x^4+1}$.
        
    - **Matrix View**: This can be viewed as matrix multiplication of the column by a fixed Maximum Distance Separable (MDS) matrix.
        
    - **Purpose**: Provides high diffusion within columns. Combined with ShiftRows, this ensures that a change in a single input bit affects every output bit after just a few rounds (Avalanche Effect).
        
4. **AddRoundKey (Key Mixing)**:
    
    - The current state is **XORed** with the subkey for that round.
        
    - This is the only layer that uses the secret key.
        

## 5. Key Expansion (Key Schedule)

AES needs a separate 128-bit subkey for each round (plus one for the initial step).

- The original key is expanded into a much larger Linear Array of words (4-byte columns).
    
- Uses operations like `RotWord` (rotate bytes), `SubWord` (apply S-Box to all bytes in a word), and `Rcon` (Round Constants) to ensure each round key is derived non-linearly from the previous ones.
    
- **Goal**: To prevent attackers from calculating round keys even if they know part of the original key, and to defend against related-key attacks.

---
# Block Cipher Modes of Operation

## 1. Introduction to Modes of Operation

While block ciphers (like AES or DES) are powerful, they have a fundamental limitation: they only operate on fixed-length blocks of data (e.g., 64 or 128 bits).

- **The Problem**: Real-world messages are of arbitrary length (emails, files, video streams).
    
- **The Solution**: **Modes of Operation** are algorithms that specify how to repeatedly apply a block cipher to securely encrypt amounts of data larger than a single block.
    
- **Core Goal**: To provide confidentiality (and sometimes authenticity, though standard modes only do confidentiality) for messages of any length.
    

## 2. Electronic Code Book ([[ECB]])

The simplest and most naive mode.
![[Pasted image 20251030105024.png]]

- **Mechanism**: Divide the plaintext into blocks ($P_1, P_2, P_3...$) and encrypt each one independently with the same key: $C_i = E_k(P_i)$.
    
- **Properties**:
    
    - Simple and very fast.
        
    - **Parallelizable**: Both encryption and decryption can be done in parallel for all blocks.
        
- **Critical Weakness**: identical plaintext blocks produce identical ciphertext blocks. It **does not conceal plaintext patterns**.
    
    - _Active Attacks_: An attacker can easily reorder, delete, or repeat blocks without breaking the encryption process itself.
        
- **Usage**: strictly for teaching purposes or encrypting very small, singular independent data (like a single encryption key).
    

> **The Penguin Demo**: Encrypting an image of Tux (the Linux penguin) with ECB results in a scrambled image where the penguin is still clearly visible because large areas of uniform color (like the white belly) always encrypt to the same pattern.
> ![[Pasted image 20251030105201.png]]

## 3. Cipher Block Chaining ([[CBC]])

For a long time, this was the industry standard (e.g., in older TLS/SSL and IPSec).

- **Mechanism**:
- ![[Pasted image 20251030104756.png]]
    
    - **Encryption**: Each plaintext block is XORed with the _previous_ ciphertext block _before_ being encrypted: $C_i = E_k(P_i \oplus C_{i-1})$.
        
    - **Initialization**: The first block $P_1$ has no previous ciphertext, so it is XORed with an **Initialization Vector (IV)**: $C_1 = E_k(P_1 \oplus IV)$.
        
    - **Decryption**: $P_i = D_k(C_i) \oplus C_{i-1}$.
        
- **IV Requirements**:
    
    - Must be **unpredictable** (random) at encryption time to prevent chosen-plaintext attacks (like the BEAST attack on TLS).
        
    - Does not need to be secret, but must never be reused with the same key for the same first block of message.
        
- **Properties**:
    
    - **Chaining dependency**: Encryption is _sequential_ (cannot be parallelized) because you need $C_{i-1}$ to compute $C_i$.
        
    - **Parallel Decryption**: Yes, you can decrypt $C_i$ once you have $C_i$ and $C_{i-1}$.
        
    - **Error Propagation**:
        
        - A 1-bit error in a ciphertext block $C_i$ completely garbles its own plaintext block $P_i$ upon decryption.
            
        - Crucially, it _also_ flips the exact corresponding bit in the _next_ plaintext block $P_{i+1}$ (due to the XOR in decryption).
            
        - Self-recovering: The error doesn't propagate beyond the next block.
            
- **Padding**: Since CBC requires complete blocks, messages must be padded (usually PKCS#7 padding). Alternatively, **Ciphertext Stealing (CTS)** can be used to avoid data expansion.
    

## 4. Output Feedback ([[OFB]])

Turns a block cipher into a **synchronous stream cipher**.
![[Pasted image 20251110235237.png]]

- **Mechanism**: The block cipher effectively becomes a pseudorandom number generator.
    
    - Keystream generation: $O_i = E_k(O_{i-1})$, starting with $O_0 = IV$.
        
    - Encryption: The output $O_i$ is the keystream, which is XORed with plaintext: $C_i = P_i \oplus O_i$.
        
- **Properties**:
    
    - **Preprocessing**: The keystream can be generated in advance, before the message is even known.
        
    - **No Chaining Dependency on Data**: Encryption/decryption is just XOR, so it's fast once the keystream is ready.
        
    - **Error Propagation**: A bit flipped in ciphertext ONLY flips the corresponding bit in plaintext. Highly suitable for noisy channels (like satellite links) where you don't want one error to destroy whole blocks of data.
        
    - **Security Critical**: Reusing an IV with the same key generates the same keystream. If this happens, $C_1 \oplus C_2 = P_1 \oplus P_2$, completely breaking confidentiality (known as a "two-time pad" attack).
        

## 5. Counter Mode ([[CTR]])

The modern standard for many applications (uses in [[TLS]] 1.3, [[AES-GCM]] standard base). It also turns the block cipher into a stream cipher, but better than [[OFB]].
![[Pasted image 20251030133804.png]]

- **Mechanism**: Instead of encrypting the previous output, it encrypts successive values of a **counter**.
    
    - Keystream: $O_i = E_k(Nonce || Counter_i)$.
        
    - Encryption: $C_i = P_i \oplus O_i$.
        
- **Properties**:
    
    - **Full Parallelization**: Since you know the counter values $(IV, IV+1, IV+2...)$ in advance, you can generate all keystream blocks in parallel.
        
    - **Random Access**: You can decrypt just the 50th block of a file without decrypting the 49 blocks before it.
        
    - **Security Critical**: Like OFB, IV/Counter uniqueness is mandatory. NEVER reuse a counter value with the same key.
        

## 6. Summary Comparison Table

|**Feature**|**ECB**|**CBC**|**OFB**|**CTR**|
|---|---|---|---|---|
|**Parallel Encryption**|**Yes**|No|No (sequential keystream)|**Yes**|
|**Parallel Decryption**|**Yes**|**Yes**|No|**Yes**|
|**Random Access**|**Yes**|Yes (decryption only)|No|**Yes**|
|**Stream Cipher?**|No|Asynchronous|Synchronous|Synchronous|
|**Error Propagation** (1 bit flip in C)|1 Block ruined|1 Block ruined, 1 bit flipped in next|1 bit flipped (precise)|1 bit flipped (precise)|
|**Security**|**Insecure** (leaks patterns)|Secure (if IV random)|Secure (if IV unique)|Secure (if IV unique)|

---
next lesson [[4 CS - Data Integrity - MAC, attacks and SHA-1]]