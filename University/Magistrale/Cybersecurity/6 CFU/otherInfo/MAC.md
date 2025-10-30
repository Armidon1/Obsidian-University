# **MAC (Message Authentication Code)**

> È un **meccanismo di autenticazione** che garantisce **l’[[Integrity]] e l’[[Authenticity]]** di un messaggio tramite un **valore crittografico** calcolato con una **chiave segreta condivisa** tra mittente e destinatario.

**In pratica:**

- Il mittente calcola il MAC del messaggio usando una chiave segreta.
    
- Il destinatario ricalcola il MAC sul messaggio ricevuto con la stessa chiave.
    
- Se i due valori coincidono → il messaggio **non è stato modificato** e **proviene da una fonte autentica**.
    

**Esempio:**  
[[HMAC]](Hash-based MAC) → usa una funzione di hash (come [[SHA]]-256) combinata con una chiave segreta.

👉 **Garantisce:** _[[Integrity]]_ e _[[Authenticity]]_  
❌ **Non garantisce:** _[[Confidentiality]]_ (non cifra i dati)


come visto in [[4 - Data Integrity - MAC, attacks and SHA-1#CBC Mode MACs]] :
## An integrity mechanism: MAC
this is not the MAC of the wifi card. 
### Recall final goal
Ensure **integrity** of messages, even in presence of
an **active** adversary who sends own messages
![[Pasted image 20251009215922.png]]
Remark: **Authenticity** is orthogonal to **secrecy**, yet systems often required to provide both

"forging" is the type of attack that violates the integrity. 
### Definitions
- Authentication algorithm - $A$
- Verification algorithm - $V$ (“accept”/”reject”)
- Authentication key – $k$
- Message space (usually binary strings)
- Every message between Alice and Bob is a pair $(m, A_{k}(m))$
- $A_{k}(m)$ is called the authentication tag of m ^04821e

Requirement – $V_{k}(m,A_{k}(m))$ = “accept”
- The authentication algorithm is called [[MAC]] (Message Authentication Code)
- $A_{k}(m)$ is frequently denoted $MAC_{k}(m)$
- Verification is by executing authentication on m and comparing with $MAC_{k}(m)$

we want an algorithm that is sure that if the integrity is violated, it displays always to the user that something went wrong. May happen that when the algorithm says "accept", sometimes it isn't. 

A (alice) sends a pair $(M,t)$, where $M$ is the message and $t$ the authentication tag, after a while, $B$ (bob) receives $(M',t')$. in the best case $M=M'$ and $t=t'$. Bob but for  security reasons, always use the verification algorithm.

### About 1:1
- More than a mere design choice, a MAC cannot assign a unique tag to each message (i.e., be one-to-one) because this would require the set of possible messages and the set of MAC values (tags) to have the same cardinality, regardless of the tag length
    
- message space is vastly larger—potentially infinite—whereas tag space is finite by design. *Pigeonhole principle: you cannot assign unique tags from a finite set to an unbounded set of messages*
    
- there are additional reasons to prefer short, fixed-length tags, including efficiency, ease of implementation and constant-time verification

### Adversary's goal
To produce a message–tag pair $(m, MAC_{k}(m))$ such that the verification function returns “accept”, i.e., $V_{k} (m, MAC_{k}(m))$ = "accept"
- An adversary capable of controlling the communication channel (e.g., a man-in-the-middle) can easily compromise data integrity—i.e., alter the message during transmission—but cannot ensure origin integrity (authenticity) without knowledge of the secret key

- In the standard threat model, the adversary is assumed to know everything except the secret key k

See also [[CBC-MAC]]