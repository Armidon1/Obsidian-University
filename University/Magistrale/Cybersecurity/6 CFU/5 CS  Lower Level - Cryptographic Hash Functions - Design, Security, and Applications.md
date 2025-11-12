last lesson [[4 CS  Lower Level - Data Integrity - MAC, attacks and SHA-1]]

---

# Cryptographic Hashing Functions

## Making Hashing Functions Stronger

- Introducing two extra requirements:
    - Collision resistance
    - Irreversibility

### Mathematician terminology
> [!image and preimage]
> 
> we consider domain set and the image set. the value of the x in the domain X is considered ***counter-image/preimage***and the ***image*** is the f(x) value 

### Collision Resistance
>[!Weakly collision resistant]
A hash function _h: $D \Rightarrow R$_ is called _**weakly collision resistant**_ for $x \in D$ if it is **hard** to find $x’!= x$ such that $h(x’)=h(x)$

“Dato _questo_ messaggio $m_1$, non riesco a trovarne un altro messaggio $m_2$ con lo stesso hash.”

>[!Strongly collision resistant]
>A function _h: $D \Rightarrow R$ is called **strongly collision resistant** if it is **hard** to find $x$, $x’$ such that $x’!=x$ but $h(x)=h(x’)$

“Non riesco a trovare _nessuna_ coppia di messaggi diversi che produca lo stesso hash."

 - **Hard** → computationally ***infeasible***, which means that it would take too long (years or more)
- Birthday bound shows that short fingerprints (≤160 bits) are feasible today
	- [[SHA-1]]  (we saw it in [[4 CS  Lower Level - Data Integrity - MAC, attacks and SHA-1#SHA-1 basics]]) was a cryptographic function until 2014

**Note:** in SHA we consider not only the original message m, but also the padding. different padding creates different hashes. so we care, not only the message's bits but also how we pad. For instance, OpenSSL use a padding with a standard called PKCS#7 (the standard number 7), which says that the padding, for example, we want to add 6 padding bytes, each byte contains the number 6.   

### Weak vs. Strong Form
- **Strong form:** hard to find _any_ two messages that collide
- **Weak form:** given one message, hard to find another that collides
- “Strong” ⇒ “Weak” because strong implies weak

### Proof
If there exists a polynomial algorithm $A_h$ such that $A_{h}(x) = x'$ with h(x) = h(x') (which means that is a collision),  
then we can construct $B_{h}(x)$ that outputs (x, x') such that h(x) = h(x'). How do we create B?
- arbitrary choose x
- return $(x, A_h(x))$

## Requirements of Cryptographic Hashing Functions

- (Strong) collision resistance
- Non-reversibility (given `h = H(M)`, hard to find `M`)

> No function has been mathematically proven cryptographic, only conjectured. 

### Terminology Update

| Old Term                    | Modern Term                |
| --------------------------- | -------------------------- |
| Non-reversibility           | Preimage resistance        |
| Weak collision resistance   | Second preimage resistance |
| Strong collision resistance | Collision resistance       |

### Summary

- Deterministic    
- Efficient.
- Preimage resistance
- Second preimage resistance
- Collision resistance
- Avalanche effect
- Fixed output length

**Note**: when the input is small, or maybe standardised, then is also efficient
## Security of Cryptographic Hashing Functions

- Birthday bound holds even for cryptographic functions
	- Same number of collisions, just better distributed 
	- Birthday attack possible in theory
- Preimage resistance enables:
    - Privacy, Authentication, Blockchain (a data structure data provides immutability $\Rightarrow$ Integrity)
    - used for deriving keys from passwords. In the KDF i put inside the password itself and also salt (and maybe also pepper)
 

---
Now we need to know how to implement those things
# Cryptographic Hashing Functions: Design and Construction

## Recap

- Maps input of any length to a fixed-size digest
- Properties:
    - Preimage resistance
    - Second preimage resistance
    - Collision resistance
- Applications:
    - Integrity
    - Digital signatures
    - Password hashing
## Design Goals
- Output should be:
    - Unpredictable
    - Uniformly distributed
    - Sensitive to input changes (avalanche effect)
    - Efficient
    - **Secure against known attacks**

## Historical Designs
- **MD5** – Broken, deprecated
- **SHA-1** – Vulnerable to collisions
- **SHA-2 (it's a family of algorithms)** – Still widely used
- **SHA-3 (Keccak, a family)** – Sponge-based, more secure
the MD5, SHA1, SHA2 are more for engineers, while SHA-3 has a mathematician approach
![[Pasted image 20251015134708.png]]
In some cases we a forced to use SHA-1 (and other deprecated algorithm) for compatibility reasons. Today SHA-2 is secure, but will be deprecated with the upcoming quantum computing. The SHA-3 exists for that reason: be ready for the quantum computers

---
**Remember**: now we want to design a cryptographic hashing function. we are still considering the big family of *Unkeyed hashing function*
## Merkle–Damgård Construction

- Processes message in blocks
- Uses compression function (for each block) + padding
- Final hash = last output
- Strength: simple, modular
- Weakness: vulnerable to length extension attacks (will see later)

## Merkle–Damgård diagram
![[Pasted image 20251015135359.png]]
there are several tecnologies to build H. Now is possible to create it with the symmetric encryption. At the moment we are not considering that 
### Merkle–Damgård: *Compression* Function

- Should behave like a pseudorandom function
- Common structures: Davies-Meyer (block-cipher based)
- Requirements: non-linearity, diffusion, confusion
#### Example

- Davies-Meyer
	- denote by $O_{i}$ the output of block 𝑖
	- 𝐻 = $𝐸_{(𝑀_𝑖)}(𝑂_{(𝑖−1)})$ ⊕ $𝑂_{(𝑖−1)}$, (E is the encryption, which is also considering a different key, each time)
	- 𝐸 is a block cipher, and 𝑀𝑖 (message block) is used as key
- SHA-1/SHA-2
	- operations seen in SHA-1
### Remarks 
- Seed usually constant
- Padding includes message length. be aware: we can design our own padding algorithm but of course you have to be coherent with the encryption e decryption.
- If base function H is collision-resistant, so is the extension
- Typical block: 512 bits
- Output length >160 bits to avoid birthday attacks

In theory, if we consider an algorithm, given an input, it produces a deterministic output. If an adversary tries a key  $k'!=k$ to decrypt, it should recieve the wrong plaintext. OpenSSL gives the message "Key Wrong"... how it is possible? Remember the padding is very important: If the padding is all set with the same number, then the key is correct. 

---

## Sponge Construction (used in [[SHA-3]] / [[Keccak]])

Work like a real sponge:
- **Absorbs input, squeezes output**
- Uses internal state (rate + capacity) and permutation $f$
- Advantages:
	- Resistant to length extension attacks
	- Flexible (SHA3-256, SHAKE128, SHAKE256)
- XOFs (eXtendable Output Functions): variable output length. It uses an internal state (rate + capacity) and a permutation function (f). Data is absorbed into the rate (r) via XOR, followed by a transformation by 'f'. Output is then squeezed from r, with f applied between extractions. The capacity portion remains hidden for security
It isn't really clear, but the reality is highly complex

### SHA-3 Overview

- Based on Keccak
	- Not affected by length extension attacks
- 1600-bit internal state
- **Post-quantum suitability**
- Strong diffusion per round

### Keccak Functions

- SHA-3 family:
	- SHA3-224 (number of digest's bits)
	- SHA3-256
	- SHA3-384
	- SHA3-512
    
- SHAKE128, SHAKE256 (XOFs)
	- XOFs can be faster than SHA-3

### Most Used Today

- **SHA-256** (SHA-2 family). 
- **Based on Merkle-Damgård construction**
- Output: 256 bits
- Still secure, fast, standardized (FIPS 180-4)

---

# Cryptographic Hashing Functions: Applications

## Recap

- Maps input to fixed-size digest
- Properties:
    - Preimage resistance
    - Second preimage resistance
    - Collision resistance

## Applications

- Integrity
- Digital signatures *(we will see it later)* 
- Passwords *(we will see it later)*
- Key derivation functions (KDF)
- Blockchain
- Privacy
- Disk optimization
- PRNG *(we will see it later)*

### Key Derivation Functions (KDF)
- Generate secret keys from a password or shared secret
- Often **hash-based**
- Properties:
    - **Strengthen weak inputs**. if the user is dumb enough to choose an easy password, then we must prevent possible attacks from the adversary
    - **Key separation**: Generate multiple keys from a single master secret. This is strongly related with "Session Key", which is a symmetric key (needs to be shared so). In the network, while we setup the communication. To get integrity, we create a momentaneo key, which will be expired at the end of the communication
    - Use **salting** and **iteration**
	    - with the iteration we mean the times of, for instance, adding grains of salt. this adds entropy on our algorithm.  
	    - Has to be deterministic, even with the presence of the salt
    - Increase brute-force cost
    - one or more pseudo-random (in real life, we are always using a deterministic function to simulate the randomness) keys of desired length 

in the naive way, it was used to create the KDF simply by hashing the key. Of course now is way more complex

---

## Blockchain
It is a Distributed (many people has  the copy) database, always growing, organised in blocks. 
- Distributed ledger secured by cryptography
- Each block typically contains:
    - Transactions
    - Timestamp
    - The Cryptographic Hash of previous block
    - Nonce (for proof of work)

### Blockchain: Immutability

- **Each block depends on previous**: Each block’s hash depends on the content of the previous block, forming an unbroken chain: if any block is altered, all subsequent blocks become invalid unless recomputed
    
- Tampering invalidates chain
    
- Verified via **Proof of Work (PoW)**: Consists in solving a difficult computational puzzle

- **How it works** *(simplified):*
	- A transaction is broadcast to the network
	- Nodes group pending transactions into a block
	- The block is validated (by PoW)
	- The validated block is added to the blockchain
	- All nodes update their copy of the chain
### PoW

Find nonce (number used once) such that:

```
Hash(block data || nonce) < Target
```

- Brute-force only: this requires a powerful setup with powerful GPUs
- Miners compete to find valid nonce. 

---

# Hashing Functions in Privacy and Optimization
|                                   |                                                                                                                                                                                                                                |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Use case**                      | **How hashing supports privacy**                                                                                                                                                                                               |
| **Data anonymization**            | Hashes can obscure identifiers (e.g. names, emails) before data sharing. In some cases i don't want to share personal information.                                                                                             |
| **Password storage**              | Stores only a hashed version of the password, not the password itself. **NEVER STORE THE PASSWORD IN CLEAR**. If you want to do it, you must store them by encrypting them first                                               |
| **Zero-Knowledge Proofs (*ZKP*)** | Hashes are used to commit to a value without revealing it. Used by the adversary that created a Ransomware: How to prove to the victim that the adversary has the key, without sharing the key itself? It is possible somehow. |
| **Private blockchains**           | Transactions may include hashed identifiers to pseudonymize users                                                                                                                                                              |

## Disk Optimization

- Hashing detects and eliminates duplicates
- Compare hashes instead of full content
- Advantages:
    - Fast comparison
    - Memory-efficient
    - Scalable
    - Protects data via cryptographic hashes

|                              |                                                                                                 |
| ---------------------------- | ----------------------------------------------------------------------------------------------- |
| - **Domain**                 | - **Use Case**                                                                                  |
| - **File backups**           | - Avoid storing same file twice (e.g., rsync). Useful to compare files and merge backups        |
| - **Cloud storage**          | - Avoid storing identical files from different users. here is also present a file backup inside |
| - **Databases**              | - Filter repeated entries                                                                       |
| - **CDNs** **/ web caching** | - Identify same content by URL or payload hash                                                  |

---

# Keyed and Unkeyed Hashing Functions
Until now we considered the Unkeyed one

## Cryptographic Hashing Functions

- Normally unkeyed (anyone can compute)
- Based on Kerckhoffs’s principle
- Unkeyed hashing cannot ensure authenticity

### Need for Keyed Hashing

- Unkeyed hashing:
	-  Takes any input, produces a fixed-size hash
	- Properties: deterministic, one-way, collision-resistant, avalanche effect
	- Primary use: data Integrity (verifying if data has changed)
	- Limitation: cannot provide authenticity (who sent it?). If anyone can compute the hash, anyone can forge it
	Adds data **integrity + authenticity**.
    
- Goal of keyed hashing
	- To provide both data Integrity and data authenticity
	- Only someone with the shared secret key should be able to produce a valid hash for a given message
	**Only those with key can compute valid hash.**
- Why not just encrypt?
	- Encryption provides confidentiality (hides content) and can imply authenticity, but it's not the same
	- Hashing is often faster and doesn't require decryption to verify integrity/authenticity
	**Encryption ≠ Hashing (hashing faster, no decryption needed),**

**Note**: cryptographic hashing function by definition are not reversible. There are no reason to coming back with an hypothetical decryption. Encryption is needed for *Confidentiality*  
    

---

# Keyed Hashing Techniques 
it provides Authenticity, better then the Unkeyed One
### Keyed Functions
- A very simple way to obtain a **keyed function**, if a key is available, is **changing the domain of the function so that it considers a key**
    
	- example: if h is an unkeyed function, we can consider $h(k||x)$, where the $||$ symbol denotes concatenation (**prefix method**, which is not great)
    
	- domain is no longer the set of possible messages but still binary space
    
		- this function is insecure, as we'll see
### Keyed Hashing
- A keyed hashing function allows to fully obtain a $MAC_k$ (remember the CBC-MAC [[4 CS  Lower Level - Data Integrity - MAC, attacks and SHA-1#CBC Mode MACs]], which used the key to encrypt. in this case we are not encrypting, but **hashing**), used for data integrity and origin authentication (authenticity)
    
- This doesn't happen with unkeyed hashing
    
- For keyed hashing we continue talking of **digest**

	- fingerprint is less used
    
- A well-designed keyed hashing function is the best implementation of MAC

### Ways to add a key
- Multiple techniques allow to include a key as an argument of h and some are more secure than others
    
- It is crucial that only Alice and Bob can use k, whilst the adversary cannot (hence cannot compute a $MAC_k$)
    
- Several naïve approaches are possible

## Naïve Methods

- **Prefix:** `h(k || M)` → vulnerable to length extension attacks
	- ***Concept***: concatenate the secret key before the message, then hash the combined string
    
	- ***Example***: MAC = SHA-256("mysecretkey"‖"transfer $100 to Alice")
    
	- ***Intuition***: seems logical. If the key is secret, only those with the key can produce the correct hash
    
	- ***Insecure***, because subject to *length extension attacks*. Nobody is using this technique: intuitive solutions are the worst.
    
- **Suffix:** `h(M || k)` → vulnerable to collision attacks
	- ***Concept***: concatenate the secret key after the message, then hash the combined string
    
	- ***Example***: MAC = SHA256("transfer $100 to Alice"‖"mysecretkey")
    
	- ***Intuition***: also seems plausible. The key is still secret
    
- **Sandwich:** `h(k || M || k)` → still insecure in general
	- ***Concept***: concatenate the key, then the message, then the key again, then hash
    
	- ***Intuition***: "double protection" might seem stronger. We don't know if it is secure, but there are no attacks at the moment. Looks strong.
    

### Length Extension Attack

- Applies to Merkle–Damgård functions: - construction and in particular the **key prefix method**
    
- Attacker can forge valid tags for extended messages if `|k|` known (Remember, the forger wants to pass the validation test [[4 CS  Lower Level - Data Integrity - MAC, attacks and SHA-1#FORGERY]])
	- An attacker by simply knowing the authentication tag of M (remember, M is not only the message m but also the padding p) can append data to M and forge a valid tag–without knowledge of the key

	- Given a pair (M, t) known to the attacker, where t = h(k‖M), he can forge a valid tag for a longer message **by guessing |k|**, which determines the **padding p** applied to k‖M
	
	- The attacker forges a new message M‖p‖M′, where M′ is arbitrary
	
	- The attacker uses t (the internal state after hashing k‖M) to resume hashing and compute a valid tag for M‖p‖M′ (Selective attacks (?))
    

### Collision Attack (Suffix)
- If adversary manages to find M' colliding with M, then
	- h(M||k) = h(M'||k)

	- because of the Merkle-Damgård and the padding further details apply (h(M) = h(M') actually computed by considering padding)
	**If `h(M) = h(M')`, then `h(M||k) = h(M'||k)`.**

The prefix method is more insecure. In this method, is requiring more stuff. It is still insecure 

### Other Techniques

- Partial truncation of `h(k||M)` (partially okay)
	- h(k, M) = first bits (e.g., first half) of h(k‖M). Partially OK: blocks the length extension attack, lacks provable security guarantees
    
- Best solution: **HMAC** (MAC based Hashing function) (later): most used one and it's proven that is **secure**.  It is a standard at the moment

Note that a different view of keyed functions makes us considering them as unkeyed ones with a different binary input
- as key changes, for a fixed message, input changes, but still binary

### Birthday Bound and Keyed Hashing

Birthday paradox still applies but collisions untestable without the key.

I Keyed Hahing function is still a a Cryptographoc Hashing Function, so, even if we put inside a key, in the end the digest is still the result of an hashing function and can be found a collision. But for passing the test, is needed also the key. the adversay, when finds the collision, doesn't know for sure which key is used. So there are 2 types of collision. in other words, attacker cannot check correctness, so the collision is useless. check is possible by knowing the key

---

# HMAC (Hash-Based Message Authentication Code) [[HMAC]]
![[Pasted image 20251016155831.png]]
opad=outer pad, ipad=inner pad

## Why HMAC?

- Secure alternative to naïve keyed methods
	- - H(key || message): vulnerable to length extension attacks    
	- H(message || key): vulnerable to collision attacks (if H is weak)
	- Both lack robust security guarantees
- HMAC (hash-based message authentication code):
	- Designed to overcome these weaknesses
	- Provides a robust and secure MAC

- Industry standard for message authentication
	- Resists:
	    - Length extension attacks
        
	    - Collision-based forgeries
        
- Standardized (RFC 2104, FIPS 198)
    

### Construction
- HMAC uses a clever, nested two-pass hashing scheme
    
- purposely designed
```
HMAC(k, m) = H((k ⊕ opad) || H((k ⊕ ipad) || m))
```
**Key components:**
- 𝐻: underlying hash function (generally built with Merkle-Damgård)
- 𝐾: secret key (normalized)
- 𝑀: message to authenticate
- 𝐵: block size of 𝐻 (later)
- ipad: inner pad (block of 0x36 bytes)
- opad: outer pad (block of 0x5C bytes)

Key **preprocessing**
- If 𝐾 > 𝐵 bytes: 𝐾′ = 𝐻(𝐾)
- If 𝐾 < 𝐵 bytes: 𝐾′ =  pad 𝐾 with zeros to 𝐵 bytes

### Addressing weaknesses
- **Resistance to length extension attacks**
	- Nested hashing and XOR operation prevent reconstruction of a useful internal state
	- Inner_hash is "sealed" by outer_hash, spreading the key's influence
	- Impossible to extend without knowing the secret key
- **Improved collision resistance**
	- More robust even if underlying 𝐻 has vulnerabilities (e.g., MD5, SHA-1)
	- Requires finding a collision for both nested operations, significantly harder
	- Best practice: always use HMAC with robust hash functions (SHA-256, SHA-3)

### - **HMAC vs. naïve keyed hashing: a deeper dive**
- The core difference: HMAC's strength comes from its nested structure, unlike simple concatenation
- Role of **ipad** and **opad**
	- These pads (inner and outer) are **fixed, distinct constants**
	- **Two different derived keys**: **K_inner** **= K** **⊕** **ipad** and **K_outer** **= K** **⊕** **opad**
	- Inner and outer hash are distinct and don't expose key or internal state
- Preventing state reconstruction
	- Inner hash **H(****K_inner** **|| M)** produces an intermediate hash value
	- Then fed into the outer hash **H(****K_outer** **||** **inner_hash****)**
	- Attacker knowing only the final HMAC cannot easily reconstruct K_inner or K_outer, nor the internal state of the inner hash, because the outer hash "seals" it, making length extension attacks ineffective

### Inner and Outer Keys

- `K_inner = K ⊕ ipad`
    
- `K_outer = K ⊕ opad`
    
- Nested hashing prevents state exposure
    

### Advantages
- Key management and flexibility: handles various key lengths; can use any cryptographically secure hash function
    
- Proven security: extensively analyzed, widely adopted standard (RFC 2104, FIPS 198)
    
- Practical use cases
	- TLS/SSL: message authentication for secure web communications
    
	- IPsec: integrity and authentication for IP packets
    
	- JSON web tokens (JWTs): signing tokens for integrity and authenticity
    
	- API authentication: protecting web API requests
    
	- Software updates: verifying the integrity and authenticity of downloads
    
	- Challenge-response authentication (later)
        

---

## Recommendations

- **Underlying hash function strength**
    
	- While HMAC improves resistance, using a strong underlying hash function is still crucial for overall security
    
	- Recommendations: HMAC-SHA256, HMAC-SHA512, or HMAC-SHA3 are currently considered strong choices
    
- **Key management for HMAC**
    
	- Secure generation: use cryptographically secure random number generators for keys
    
	- Secure storage: store keys securely, separate from the data they protect
    
	- Key rotation: regularly change HMAC keys

- **HMAC is not encryption**
    
	- HMAC provides integrity and authenticity, not confidentiality
    
	- It does not hide the message content. It is one-way
    
- **Key reuse**
    
	- Avoid reusing the same key for different cryptographic purposes (e.g., using an HMAC key as an encryption key)
    
	- Each cryptographic primitive should ideally have its own unique key
    
- **Side-channel attacks**
	    
	- Even with a secure HMAC implementation, timing or power analysis attacks can sometimes leak key information
    
	- Proper implementation requires constant-time operations to mitigate this risk
    
- **Weak underlying hash function** **(again)**
    
	- While HMAC improves collision resistance, using a completely broken hash (like MD5) is still not recommended for new systems
    
	- The security of HMAC ultimately relies on the security properties of the underlying hash function

## Non repudiation

**Non-repudiation** is a key concept in information security that ensures that a party in a communication or transaction **cannot deny the authenticity of their signature or the sending of a message**.

In simpler terms, it means **proof of origin and delivery** — so that neither the sender nor the receiver can later claim they didn’t send or receive the information.

---

### 🔑 Key Points:

1. **Purpose:**  
    To provide evidence that can be used to prove that a specific action (like sending an email, signing a document, or making a payment) **actually occurred**.
    
2. **How It’s Achieved:**
    
    - **Digital Signatures:** Ensure the sender’s identity and message integrity.
        
    - **Public Key Infrastructure (PKI):** Manages certificates and keys used in digital signatures.
        
    - **Audit Logs:** Keep track of who did what and when.
        
    - **Timestamps:** Prove when an action took place.
        
3. **Example:**
    
    - You send an electronically signed contract via email.
        
    - The recipient receives it.
        
    - Because your digital signature is verified by a trusted certificate authority (CA), you **can’t later deny** having signed and sent it — that’s non-repudiation.
        

---

### ⚙️ In Cybersecurity:

Non-repudiation is one of the **five pillars of information security**:

1. **Confidentiality**
    
2. **Integrity**
    
3. **Availability**
    
4. **Authentication**
    
5. **Non-repudiation**
    

## HMAC and no-repudiation
HMAC is not providing no-repudiation. It is important to have a "judge" that verifies who sent the message

---

## Summary

- Purpose: a robust standard for message authentication, providing both data integrity and authenticity
- A nested hash construction that leverages the underlying hash function
- Security
	- Effectively prevents length extension attacks
	- Significantly improves collision resistance compared to naive keying methods
	- Theorem: HMAC can be forged if and only if the underlying hash function is broken (collisions found). [Bellare, Canetti, Krawczyk, 1996: https://cseweb.ucsd.edu/~mihir/papers/kmd5.pdf]
- Best practices
- Choose a strong underlying hash function (e.g., SHA-256, SHA-3)
- Implement secure key management (generation, storage, rotation)
- Always rely on standardized and well-vetted libraries for implementation
    

---

# HMAC and the Birthday Attack

## Adversary Model

- The adversary wants to find two messages 𝑚 ≠ 𝑚′ such that: HMAC(𝑘, 𝑚)=HMAC(𝑘, 𝑚′)
- The attacker knows
	- The HMAC algorithm and the hash function used
	- Several valid (message, tag) pairs using the same key
- But **does not know** the secret key 𝑘

## HMAC and the Birthday Paradox

- HMAC behaves like a pseudorandom function from the attacker’s perspective
    
- Even with many observed (message, HMAC) pairs
	- The attacker cannot test or verify a collision
	- He cannot generate new tags
	- Even if two messages yield the same tag, he can't confirm it's a true collision


## **Oracle attacks and HMAC**
- In **oracle attacks**, the adversary queries a system that produces valid tags using the (unknown) key, to learn something
    
- HMAC is **secure against chosen-message attacks**, even if the attacker can
    
	- submit many messages to an oracle and observe corresponding outputs
    
	- attempt adaptive queries based on previous responses
    
	- Because of its pseudorandom behaviour, HMAC reveals **no useful information** about k

## **HMAC and the birthday bound**
- The birthday bound is a universal hash property
    
- It applies to HMAC output in theory, but is **not exploitable** in practice
    
- Shows how HMAC resists attacks even at theoretical collision levels
    
- In HMAC, observed collisions are meaningless without the key

## **Theory and practice**
- Collisions **might exist** due to the birthday bound
    
- But the attacker cannot
    
	- Recognize or confirm them
    
	- Exploit them without the key
    
- HMAC output appears **random and independent** to the attacker

## Example
To exploit the birthday paradox, the attacker would need
- Submit 2^(𝑛/2) messages to oracle to obtain as many valid tags, where 𝑛 is the length of digest
- The ability to test tags
- Without k, no test can be done

protecting the key means protecting HMAC
## Sandwich-style keying
- Even a naïve keyed construction like H(k||m||k) may appear safe
    
- The attacker still cannot practically exploit the birthday paradox
    
	- The key is embedded in the input
    
	- Without knowing the key, collisions are untestable
    
	- Still oracle needed
    
- But under some (strong) hypotheses, two colliding messages under H can still collide in the sandwich structure

## Summary
- The birthday paradox has practical consequences on unkeyed hash functions, not to keyed
    
- HMAC hides the internal structure of the hash from the attacker
    
- Security of HMAC relies on the secrecy of k, not just hash function strength


# Other stuff
Remember the difference between **Hashing function** and **Cryptographic Hashing function**:
- **Scopo**
	- *Hash function (non-crypto)*: progettate per velocità e uniformità (es. hash table, checksums, dedup). Esempi: CRC32, MurmurHash, CityHash.
	- **Cryptographic hash function**: progettate per sicurezza (integrità, firme, KDF, blockchain). Esempi: SHA‑256, SHA‑3, BLAKE2.

- **Proprietà richieste**
    - *Non‑crypto*: deterministica, veloce, buona distribuzione; non garantisce resistenza a collisioni o inversione.
    - *Crypto*: preimage resistance (difficile invertire), second‑preimage resistance, collision resistance, avalanche; implementazioni constant‑time se necessario.
- 
- **Resistenza ad attacchi**
    - *Non‑crypto*: vulnerabile a collisioni deliberate e a ricostruzione del messaggio.
    - *Crypto*: progettata per rendere tali attacchi computazionalmente infeasible (ma non matematicamente provata).
    
- **Performance vs sicurezza**
    - *Non‑crypto*: molto più veloce, basso uso risorse.
    - *Crypto*: più costosa, ma necessaria quando la sicurezza è un requisito.
	    - For protecting us from brute-forcing attacks, we want slow hashing function. 
	    - For creating a key in KDF, it is needed 1 second (which is a lot). While doing brute-forcing we are searching on billions and billions keys, and that's a lot of time of course. 

- **Keyed variants / usi pratici**
    - Per autenticità usare HMAC o algoritmi keyed (es. BLAKE2 keyed), non la sola hash.
    - Per password usare KDFs/slow hashes (bcrypt, Argon2), non solo SHA‑256.

Regola pratica: se la finalità è sicurezza/integrità/autenticità usa una cryptographic hash (o MAC/KDF adeguato). Per prestazioni e strutture dati usa hash non‑cryptografici.

**Differences between Hashing and Encryption**: 
- *Hash (cryptographic hash)*: funzione unidirezionale che mappa input di qualsiasi lunghezza a un digest fisso. Proprietà importanti: preimage resistance (difficile trovare x dato h(x)), second‑preimage e collision resistance (ideali), avalanche. Non è reversibile e non fornisce confidenzialità.
    
- *Encryption*: operazione reversibile tramite chiave (decryption possibile). Fornisce confidenzialità; non è progettata per essere una funzione “one‑way” né per garantire collision resistance.
	
we can encrypt the disk for Confidentiality and can get a hash of the disk for optimisation

next lesson [[6 CS  Lower Level - Authenticated Encryption]]