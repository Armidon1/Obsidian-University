Based on the notes you provided, here is the detailed explanation of how these two specific attacks work against naïve keyed hashing methods.

### 1. The Prefix Method: Length Extension Attack

**Method:** $h(k || M)$ 

To understand this attack, you must understand that **Merkle-Damgård** hash functions (like SHA-256 or MD5) work like a chain. They process data in blocks, and the output of processing one block becomes the input state (IV) for the next block.

The Mechanism:

The hash of a message isn't just a "final signature"; it is actually the internal state of the hash function after it has finished processing the data.

1. **The Setup:** Alice computes $Tag = h(k || M)$. This effectively processes the key, the message, and the mandatory padding ($P$). The internal state of the hash function after processing $(k || M || P)$ is the $Tag$.
    
2. **The Attack:** An attacker sees the message $M$ and the $Tag$. They do not know $k$.
    
3. **The Extension:** The attacker wants to forge a valid tag for a new message that includes extra data ($M'$) at the end. They construct a new message: $M_{new} = M || P || M'$.
    
4. **The "Resume" Trick:** The attacker initializes their own hash function. Instead of using the standard initialization vector (IV), they manually set the internal state to equal Alice's $Tag$.
    
5. **The Forge:** The attacker feeds $M'$ into this pre-loaded hash function. The function continues hashing exactly where Alice left off. It thinks it has already processed $k || M || P$ and simply continues to process $M'$.
    
6. **Result:** The output is a valid hash for $h(k || M || P || M')$. The attacker has successfully forged a MAC for a longer message without ever knowing $k$.
    

**Why it works:** The Prefix method exposes the internal state of the digest to the world, allowing anyone to "resume" the hashing process.

---

### 2. The Suffix Method: Collision Attack

**Method:** $h(M || k)$ 6

This attack relies on finding a collision in the _message_ part before the key is even involved. It is an **offline attack**, meaning the attacker can do the hard work on their own computer without interacting with the victim7.

**The Mechanism:**

1. **Offline Collision:** The attacker uses their own resources to find two different messages, $M$ and $M'$, that result in the same hash: $h(M) = h(M')$88.
    
    - _Note:_ The messages usually need to be the same length so that the padding remains identical9.
        
2. **Internal State Match:** Because $h(M) = h(M')$, the internal state of the hash function after processing $M$ is identical to the state after processing $M'$.
    
3. **The Swap:** The attacker tricks the victim (Alice) into signing $M$. Alice computes the tag $T = h(M || k)$.
    
4. **The Forge:** The attacker intercepts the message and swaps $M$ for $M'$.
    
5. **The Validation:** When the receiver checks the tag for $M'$, they compute $h(M' || k)$.
    
    - Since the internal state after $M$ and $M'$ was identical, and the suffix ($k$) is identical, the hash function proceeds through the key part exactly the same way for both messages.
        
    - Therefore, $h(M || k) = h(M' || k)$.
        

**Why it works:** The key is processed _after_ the collision occurs. The key acts as a deterministic suffix; if the inputs ($M$ and $M'$) produce the same intermediate state, appending the same secret key will inevitably produce the same final result.

### Summary Comparison

- **Prefix ($k||M$):** Broken because the output allows an attacker to **continue** the hash calculation (Length Extension).
    
- **Suffix ($M||k$):** Broken because an attacker can find a **collision** ($M$ vs $M'$) before the key is involved, making the key irrelevant to the distinction between the two messages.