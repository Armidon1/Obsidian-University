# **AES (Advanced Encryption Standard)**

> È un **algoritmo di cifratura simmetrica a blocchi** usato per garantire la **[[Confidentiality]] dei dati**, standardizzato dal NIST nel 2001 come successore del [[DES]].

**Caratteristiche principali:**

- Usa la **stessa chiave** per cifrare e decifrare (cifratura simmetrica).
    
- Opera su **blocchi di 128 bit**.
    
- Supporta chiavi di **128, 192 o 256 bit**, determinando il livello di sicurezza.
    
- Basato su una struttura matematica detta **rete di sostituzione–permutazione** (Substitution–Permutation Network).
    

**Modalità d’uso comuni (block modes):**

- **[[ECB]] (Electronic Codebook):** insicura, non protegge contro pattern ripetuti.
    
- **[[CBC]] (Cipher Block Chaining):** aggiunge casualità ma non [[Authenticity]].
    
- **[[GCM]] (Galois/Counter Mode):** fornisce **[[Confidentiality]] + [[Integrity]]** ([[Authenticity]] integrata).
    

**Garantisce:**

- ✅ **[[Confidentiality]]** — i dati sono cifrati e illeggibili senza la chiave corretta.
    

**Non garantisce da solo:**

- ❌ **[[Integrity]]**
    
- ❌ **[[Authenticity]]**
    

**Esempi d’uso:**

- Cifratura di file e dischi (BitLocker, VeraCrypt)
    
- Comunicazioni sicure ([[TLS]], IPsec, Wi-Fi WPA2/WPA3)
    
- Applicazioni e protocolli crittografici moderni
    

**In breve:**

> **AES** è il principale standard di cifratura simmetrica moderno: **veloce, sicuro e ampiamente adottato** per proteggere la **riservatezza dei dati**.

# Nel dettaglio
preso dalla nota [[3 CS  Lower Level - Block Ciphers#AES (Advanced Encryption Standard)]]]
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
    
    - These coefficients $x,y$ can be found using the **[[Extended Euclidean Algorithm (EEA)]]**, which is vital for finding multiplicative inverses in finite fields (used in the AES S-Box).
        

### Finite Fields ([[Galois Field]]s)

AES does not use standard integer arithmetic; it uses arithmetic within a finite field to ensure results always stay within a fixed number of bits (a byte).

- **Definition**: A finite field $GF(p^k)$ is a field with a finite number of elements, specifically $p^k$ where $p$ is a prime and $k$ is a positive integer.
    
- **Uniqueness**: For every prime power $p^k$, there is a unique finite field of that size.
    
- **AES Usage**: AES uses **$GF(2^8)$**. This means elements are 8-bit polynomials (bytes).
    
    - **Addition**: Performed as bitwise **XOR** (since $1+1=0 \pmod 2$). This is extremely fast.
        
    - **Multiplication**: Polynomial multiplication followed by reduction modulo an irreducible polynomial $m(x)$.
        
        - AES standard irreducible polynomial: $m(x) = x^8 + x^4 + x^3 + x + 1$.
            
        - For efficiency, multiplication in $GF(2^8)$ is often implemented using lookup tables (like `alogs` tables).
        ![[Pasted image 20251111103456.png]]

## 3. AES Design Rationale

Why was Rijndael chosen as AES?

1. **Security**: Resistant to all known attacks (linear and differential cryptanalysis) at the time of selection.
    
2. **Efficiency**: Excellent speed in both software (PCs) and hardware (dedicated chips).
    
3. **Compactness**: Code can be very small, making it suitable for smart cards and restricted devices.
    
4. **Simplicity**: The design is clean and relies on well-understood algebraic structures.
    

## 4. AES Internal Specification

AES operates on a $4 \times 4$ matrix of bytes called the **State**.

- **Input**: 128 bits are arranged into this $4 \times 4$ grid ($16$ bytes: $A_{0,0}$ to $A_{3,3}$).![[Pasted image 20251111103626.png]]
    
- **Key**: The initial key is also arranged in a similar matrix (size depends on key length).![[Pasted image 20251111103633.png]]
    

### High-Level Algorithm
![[Pasted image 20251111103712.png]]

AES is an iterated cipher consisting of **Rounds**.

- **128-bit key**: 10 Rounds
    
- **192-bit key**: 12 Rounds
    
- **256-bit key**: 14 Rounds
    

**Pseudocode Structure:**

Plaintext

```C
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
   ![[Pasted image 20251111103804.png]]
    
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

## Video animation
![](https://youtu.be/gP4PqVGudtg?si=Xu7JpzlxAnexGEZ5)
