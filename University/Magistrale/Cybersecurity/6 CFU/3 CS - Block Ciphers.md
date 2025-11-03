last lesson [[2 CS - Stream Ciphers]]

### 1. Introduction to Block Ciphers

#### What is a Block Cipher?

A **block cipher** is a fundamental tool in symmetric cryptography. It is an algorithm that operates on fixed-size groups of bits, called "blocks," using a secret key 1.

- **Input:** A plaintext block (P) of a fixed size, _h_ bits (e.g., 128 bits)2222.
    
- **Key:** A secret key (k) of a fixed size (e.g., 56, 128, or 256 bits)3.
    
- **Output:** A ciphertext block (C) of _h_ bits4.
    

A key feature is that a block cipher is a **deterministic transformation**5. This means that for a given plaintext (P) and a given key (k), the cipher will _always_ produce the exact same ciphertext (C)6. Think of the key as a custom mold and the plaintext as clay; the mold (key) always shapes the clay (plaintext) into the same final form 7.

#### Block Ciphers vs. Stream Ciphers

Cryptography offers two main types of ciphers:

- **Block Ciphers:** Encrypt data one fixed-size block at a time (e.g., 128 bits)8. This is like a large stamping machine that processes data in chunks.
    
- **Stream Ciphers:** Encrypt data one bit or one byte at a time9. This is like a faucet adding a "keystream" to the data as it flows by.
    

Block ciphers are ideal for structured data that is already chunked, such as files, database records, or disk sectors 10101010. Stream ciphers are often preferred for real-time communication11.

#### Desired Properties of a Block Cipher

To be secure, a block cipher must have several key properties12:

1. **Invertibility:** It must be reversible. We must be able to decrypt the ciphertext back to the original plaintext using the key13131313.
    
2. **Key Sensitivity:** A small change in the _key_ should produce a completely different ciphertext14.
    
3. **Avalanche Effect (Diffusion):** A small change in the _plaintext_ (even one bit) should cause a drastic and unpredictable change in the output ciphertext15.
    
4. **Non-linearity (Confusion):** The relationship between the key, plaintext, and ciphertext should be complex and non-linear, making it difficult to reverse-engineer the process using simple mathematics16.
    

---

### 2. A History of Block Ciphers

#### DES (Data Encryption Standard)

- **Developed:** By IBM and approved by the US government in 197617.
    
- **Specs:** 64-bit block size, 56-bit key18181818.
    
- **Downfall:** The 56-bit key was criticized as being too small, allegedly to allow the NSA to brute-force it19. By the 1990s, DES was proven to be practically breakable. In 1999, the "Deep Crack" machine and distributed.net broke a DES key in under 23 hours20.
    

#### 3DES (Triple DES)

- **Purpose:** A temporary fix for the weakness of DES by iterating the algorithm21.
    
- Mechanism: The most common form is EDE (Encrypt-Decrypt-Encrypt):
    
    `C = Ek1( Dk2( Ek1(P) ) )`22222222.
    
- **Security:** This gives the illusion of a 168-bit key (56 * 3)23. However, it is vulnerable to a **Meet-in-the-Middle (MITM) attack**, which reduces its effective security to 112 bits24.
    

#### Why Not 2DES (Double DES)?

Using DES twice (2DES) is **not secure**25. It is vulnerable to the **Meet-in-the-Middle (MITM) attack**, which is _not_ the same as a Man-in-the-Middle attack26.

- **The MITM Attack (on 2DES):**
    
    1. An attacker needs one known plaintext/ciphertext pair (P, C), where `C = Ek2(Ek1(P))`27.
        
    2. **Step 1:** The attacker encrypts P with all $2^{56}$ possible keys for _k1_. They store these intermediate results in a massive lookup table (requiring $2^{56}$ memory)28282828.
        
    3. **Step 2:** The attacker decrypts C with all $2^{56}$ possible keys for _k2_.
        
    4. **Step 3:** The attacker looks for a **match** (a "meet-in-the-middle") between the results from Step 1 and Step 229.
        
- **Result:** The attacker only needs $2^{56} + 2^{56}$ (or $2^{57}$) operations, not the $2^{112}$ required for a full brute-force, to break 2DES30. This is why 3DES (with 112-bit effective security) became the standard31.
    

#### Other Historical Ciphers

- **RC-2 (1987):** 64-bit block, variable key. Vulnerable 32.
    
- **IDEA (1991):** 64-bit block, 128-bit key. Strong, but now outdated 33.
    
- **Blowfish (1993):** 64-bit block, variable key. Still strong, but deprecated in favor of its successor, Twofish 34.
    
- **RC5 (1994):** Variable block, key, and round counts 35. The distributed.net project is still attempting to brute-force a 72-bit RC5 key; as of January 2025, it is only 12% complete after decades of work 36.
    

---

### 3. AES (Advanced Encryption Standard)

In 1997, the US government (NIST) held an open, international competition to find a successor to DES 37. The winning algorithm, chosen in 2001, was **Rijndael**, created by two Belgian cryptographers, Daemen and Rijmen38.

Rijndael won not because it was the most secure (Serpent was rated higher for security), but because it offered the best _overall balance_ of security, speed on both hardware and software, and simplicity 39.

#### AES Overview

- **Specs:** Symmetric block cipher, 128-bit block size40404040.
    
- **Key Lengths:** 128, 192, or 256 bits41.
    
- **Rationale:** Resistant to all known attacks, fast, and simple, making it suitable even for low-power devices like smart cards 42.
    

#### The Mathematics of AES: Galois Fields

AES is built on advanced mathematics, specifically arithmetic in the **Galois Field GF(2⁸)**43434343.

- A **Galois Field (GF)**, or finite field, is a set with a finite number of elements. A field $GF(p^k)$ has $p^k$ elements44.
    
- AES treats each byte of data as an element in $GF(2^8)$, which has 256 elements.
    
- This is implemented using polynomials. The two main operations are:
    
    1. **Addition:** This is simply a bitwise **XOR** operation (because 1+1=0)45.
        
    2. **Multiplication:** This is a more complex polynomial multiplication, followed by taking a remainder modulo an irreducible polynomial46.
        

#### AES Structure: State and Rounds

AES encryption is carried out in a series of **rounds** (e.g., 10 rounds for a 128-bit key)47.

1. **Input:** The 128-bit (16-byte) input block is loaded into a 4x4 matrix of bytes called the **State**48.
    
2. **KeyExpansion:** The original secret key (e.g., 128 bits) is "expanded" to create a unique 128-bit **Round Key** for each of the 10 rounds494949.
    
3. **Initial Step:** `AddRoundKey` (the first Round Key is XORed with the State)50.
    
4. **Rounds (9 rounds):** Each round consists of four transformations:
    
    - **SubBytes (Substitution):** A non-linear step. Each byte in the State is replaced with another byte according to a fixed lookup table called the **S-Box**. This S-Box is derived from the multiplicative inverse in $GF(2^8)$ and provides non-linearity (confusion)51.
        
    - **ShiftRows (Permutation):** A transposition step. The bytes in each row of the State are cyclically shifted by a different offset (row 2 shifts 1, row 3 shifts 2, etc.)525252. This provides diffusion, mixing data across columns.
        
    - **MixColumns (Mixing):** Each column of the State is treated as a polynomial and multiplied by a fixed polynomial in $GF(2^8)$535353. This provides significant diffusion.
        
    - **AddRoundKey:** The Round Key for the current round is XORed with the State54.
        
5. **Final Round (Round 10):** This round is the same but **omits the MixColumns** step.
    

**Decryption** is the reverse of this process, using the inverse of each step (Inv-SubBytes, Inv-ShiftRows, Inv-MixColumns).

---

### 4. Block Cipher Modes of Operation

A block cipher by itself can only encrypt a single, fixed-size block. A **mode of operation** is a technique that allows a block cipher to securely encrypt messages of arbitrary length5555.

#### ECB (Electronic Code Book) Mode

- **How it works:** This is the "naive" mode. Each plaintext block is encrypted separately and independently56.
    
- **Properties:** **DO NOT USE.** It is simple and can be done in parallel57.
    
- **Fatal Flaw:** It is **not secure** because it does not conceal plaintext patterns. If the same plaintext block appears twice in a message, it will produce the same ciphertext block5858. This allows an attacker to see patterns (as shown by the encrypted, but still visible, penguin image)59.
    

#### CBC (Cipher Block Chaining) Mode

- **How it works:** This is the classic, secure mode. Before encrypting a plaintext block, it is **XORed with the _previous_ ciphertext block**60.
    
- **Initialization Vector (IV):** To start the process, the first plaintext block is XORed with a random, public "dummy block" called the **Initialization Vector (IV)**61.
    
- **Properties:**
    
    - Conceals plaintext patterns6262.
        
    - Encryption _cannot_ be parallelized (each block depends on the last)6363.
        
    - Decryption _can_ be parallelized64646464.
        
    - A transmission error in one ciphertext block will corrupt its corresponding plaintext block and cause a predictable bit-flip in the _next_ block65.
        

#### OFB (Output FeedBack) Mode

- **How it works:** This mode turns a block cipher into a **synchronous stream cipher**6666.
    
- It generates a "keystream" by repeatedly encrypting the IV, and then re-encrypting _its own output_: `Keystream_Block_i = E(Keystream_Block_i-1)`.
    
- The final ciphertext is: `Ci = Pi ⊕ Keystream_Block_i`67.
    
- **Properties:**
    
    - Decryption is the exact same operation (XORing with the keystream)68.
        
    - Errors do _not_ propagate. A flipped bit in the ciphertext flips only one bit in the plaintext69696969.
        
    - Cannot be parallelized70.
        

#### CTR (Counter) Mode

- **How it works:** This is the modern, preferred mode. It also turns a block cipher into a stream cipher7171.
    
- It generates a keystream by encrypting successive values of a counter: `Keystream_Block_i = E(IV + i)`. The "counter" is usually just the IV (or nonce) incremented for each block727272.
    
- The ciphertext is: `Ci = Pi ⊕ Keystream_Block_i`.
    
- **Properties:**
    
    - **Fully Parallelizable:** Encryption and decryption can be done in parallel, making it very fast on multi-core processors73.
        
    - **Random Access:** You can decrypt any block (e.g., block 100) instantly, without needing to process the 99 blocks before it74.
        
    - Errors do not propagate.
        

#### The Importance of the IV (Initialization Vector)

- For all modes except ECB, an IV is required to introduce randomization757575.
    
- The IV does _not_ need to be secret, but it **MUST NEVER BE REUSED** with the same key767676.
    
- Reusing an IV in CBC leaks information about the first block77.
    
- Reusing an IV in OFB or CTR **completely destroys all security**, as it produces the exact same keystream78787878.

---

next lesson [[4 CS - Data Integrity - MAC, attacks and SHA-1]]