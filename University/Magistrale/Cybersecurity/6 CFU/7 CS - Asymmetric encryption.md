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

## Integer multiplication

- given x, y, two large prime numbers of roughly equal bit-length (say, n bits each)
- computing z =xy, 2n bits, is easy
    - many poly algs
- no poly alg is know for factoring z
    - Shor is poly on quantum computers


## Discrete Log (DL)

- Let G be a finite cyclic group with n elements and g a generator of G
- Let y be any element in G; then it can be written as $y= g^x$, for some integer x
- Let $y = g^x$ and $x$ the minimal non-negative integer satisfying the equation
- The minimal x s.t. $y = g^x$ is called the **discrete log of** **y to base g**
- Example: $y = g^x$ mod p in the multiplicative group of ℤp


## Modular exponentiation

- `c mod p = (a ⋅ b) mod p = ((a mod p) ⋅ (b mod p)) mod p`

- https://en.wikipedia.org/wiki/Modular_arithmetic#Properties
- be mod p =(b mod p)$^{e mod𝜑(p)}$ mod p
	- p prime and (b,p) co-prime
	- https://en.wikipedia.org/wiki/Euler%27s_theorem
- can use mod on partial results


## Fast mod exponentiation
```c
long fastModExp(unsigned int base, unsigned int exp, long mod) {
	long result = 1;
	long b = base % mod;
	while (exp > 0) {
		if (exp & 1)
		result = (result * b) % mod;
		b = (b * b) % mod;
		exp >>= 1;
	}
	return result;
}
```

##  Discrete Log in ℤ𝒑 : a candidate as OWF
- Let $y=g^x$ mod 𝑝 in $ℤ^∗_p$
    - e.g.,$ℤ^*_{10}$ = {1,3,7,9}  ($p$ is not necessarily prime)
- $g^x$ mod 𝑝 can be computed in $O(log(x))$ multiplications, each multiplication taking $O(log^2(p))$ steps (remind $g<p$)
	- also, it turns out $x$ must be < $p$ ⟹ overall # of steps is $O(log^3(p))$
- Standard discrete log is believed to be computationally hard
- 𝑥 $\rightarrow g^x$ mod 𝑝  is believed to be an OWF
    - 𝑥 $\rightarrow g^x$ mod 𝑝 is easy (efficiently computable)
    - $g^x$ mod 𝑝 $\rightarrow x$ believed hard (computationally infeasible)
- This is a **computation-based** notion

## Do OWFs exist?
- open problem
    - they are conjectured to exist
- **Theorem**. If a one-way function exists, then P ≠ NP (theoretical proof)
    - one-way functions are conjectured to exist, as P is conjectured to be strictly included in NP

## Utility of OWFs

- Cryptographic hashing (and its uses), secure key exchanges, public key cryptography, random numbers...
- More generally, assuming OWFs exist, we obtain strong mathematical properties that are computationally **hard to break**, forming the foundation of many cryptographic guarantees


# Diffie-Hellman key exchange

## Public exchange of keys

- Goal: two parties (Alice and Bob) who do not share
    any secret information, perform a protocol and derive
    the same shared key
- Eve, who is listening, cannot obtain the new shared
    key if she has limited computational resources (i.e. in
    polynomial time)
       - unless P = NP


#### DH procedure

- Public parameters: a prime𝑝, and an element 𝑔(possibly a
    generator of the multiplicative groupℤ∗𝑝)
       - better a safe prime, i.e., a prime 𝑝 = 2𝑞 + 1 where 𝑞is
          also prime (a Sophie Germain prime)
- Alice chooses 𝑎at random from the interval
    [1..𝑝−1] and sends𝑔𝑎mod 𝑝 to Bob
- Bob chooses𝑏 at random from the interval
    [1..𝑝−1] and sends𝑔𝑏mod 𝑝 to Alice
- Alice and Bob compute the shared key 𝑔𝑎𝑏mod 𝑝
    - Bob holds 𝑏, computes 𝑔𝑎 𝑏𝑚𝑜𝑑 𝑝 = 𝑔𝑎𝑏 mod 𝑝
    - Alice holds 𝑎, computes 𝑔𝑏 𝑎𝑚𝑜𝑑 𝑝 = 𝑔𝑎𝑏 mod 𝑝


#### DH procedure – visual


#### Terminology

- **Public parameters** (𝑔 and 𝑝)
- **Private keys** (𝑎 and 𝑏): they are secret
- **Public keys** (𝐴 = 𝑔𝑎mod 𝑝 and 𝐴 = 𝑔𝑎mod 𝑝):

```
public
```
- **Shared secret sey** (𝐾 = 𝑔𝑎𝑏mod 𝑝)


#### DH and MITM

1. A->T(B):𝑔𝑎mod 𝑝
2. T(B)->A:𝑔𝑡mod 𝑝 _(t chosen by T)_
3. T(A)->B:𝑔𝑡mod 𝑝
4. B->T(A):𝑔𝑏mod 𝑝

Effects

- B shares a key 𝑔𝑏𝑡mod 𝑝 with T (believing to share it with
    A)
- A shares a key 𝑔𝑎𝑡mod 𝑝 with T (believing to share it with
    B)

[[Availability]]
#### Perfect forward secrecy

The cryptosystem

- generates random public keys per session for the
    purposes of key agreement, and
- does not use any sort of deterministic algorithm in doing so

**The compromise of a shared key does not compromise
former, or subsequent, shared keys**


28

#### Types of DH

```
Feature Static Diffie-Hellman Ephemeral Diffie-Hellman(DHE/ECDHE)
```
```
Key Lifespan
```
```
Uses a long-term key pair
that remains the same across
sessions (typically on the
server side)
```
```
Generates a new, temporary
key pair for each
communication session
```
```
Mathematical
Basis
```
```
Either modular
exponentiation or elliptic
curves (more advanced)
```
```
Either modular
exponentiation or elliptic
curves (more advanced)
Primary Security
Property Lacks Forward Secrecy Provides Forward Secrec
```
```
Primary Use Case
```
```
Used in specific scenarios
where long-term key
management is required
```
```
The standard for modern
secure communication
```

#### Vulnerabilities

```
Vulnerability Description Impact Mitigation
```
**Man-in-the-
Middle**

```
No authentication in
basic DH
```
```
Attacker can
intercept and alter
key
```
```
Use authenticated
DH
```
**Logjam
Attack**

```
Exploits small (e.g.,
512-bit) shared
primes
```
```
Breaks DH with
precomputation
```
```
Use ≥2048-bit
primes, avoid shared
parameters
```
**Shared
Parameters**

```
Use of common
primes/groups
across many
servers
```
```
Enables large-
scale
precomputation
```
```
Use unique, safe
primes
```
**Static DH
Keys**

```
Reuse of long-term
DH private keys
```
```
Weak forward
secrecy Use ephemeral DH
```

#### MITM and static DH

- MITM can be prevented by inserting key material
    within X509 certificates
- Used in authentication
- To be developed later


#### Properties of key exchange

```
Necessary security requirement: the shared secret key is
a one-way function of the public and transmitted
information
```
```
Necessary “constructive” requirement: an appropriate
combination of public and private pieces of information
forms the shared secret key efficiently
```
```
DH Key exchange by itself is effective only against a
passive adversary. Man-in-the-middle attack is lethal
```

#### Security requirements

- Is the one-way relationship between public
    information and shared private key sufficient?
- A one-way function may leak some bits of its
    arguments: this is prevented by carefully
    choosing g and p
- The full requirement is: given all the
    communication recorded throughout the
    protocol, computing any bit of the shared key
    is hard
- Note that the “any bit” requirement is
    especially important


#### Other DH Systems

- The DH idea can be used with any group
    structure
- Limitation: groups in which the discrete log can be
    easily computed are not useful (for example:
    additive group of Zp)
- Currently useful DH systems: ECDH, the
    multiplicative group of Zp and elliptic curve
    systems https://en.wikipedia.org/wiki/Elliptic-
    curve_Diffie%E2%80%93Hellman
- Keys are exchanged in most network protocols,
    refreshed, automatically distributed, etc.


## RSA – the algorithm

#### The multiplicative group ℤ

```
∗
𝒑𝒒
```
- Let 𝑝 and 𝑞 be two large primes. Denote their
    product 𝑁 = 𝑝𝑞
- The multiplicative group ℤ∗𝑵 contains all integers
    in the range [1,𝑝𝑞−1] that are relatively prime to
    both 𝑝 and 𝑞
- Since in [1,𝑝𝑞−1] there are (𝑝−1) multiples of 𝑞 and
    (𝑞−1) multiples of 𝑝, the size of the group is
    φ(𝑝𝑞) = 𝑝𝑞−1−(𝑝−1)−(𝑞−1) = 𝑝𝑞−(𝑝 + 𝑞) + 1 = (𝑝−
    1)(𝑞−1)
- By Euler’s theorem, for 𝑥∈ℤ∗𝑁, 𝑥 𝑝−1 𝑞−1 = 1


36

#### The multiplicative group ℤ

```
∗
𝒑𝒒
```
- Let 𝑝 and 𝑞 be two large primes. Denote their
    product 𝑁 = 𝑝𝑞
- The multiplicative group ℤ∗𝑵 contains all integers
    in the range [1,𝑝𝑞−1] that are relatively prime to
    both 𝑝 and 𝑞
- Since in [1,𝑝𝑞−1] there are (𝑝−1) multiples of 𝑞 and
    (𝑞−1) multiples of 𝑝, the size of the group is
    φ(𝑝𝑞) = 𝑝𝑞−1−(𝑝−1)−(𝑞−1) = 𝑝𝑞−(𝑝 + 𝑞) + 1 = (𝑝−
    1)(𝑞−1)
- By Euler’s theorem, for 𝑥∈ℤ∗𝑁, 𝑥 𝑝−1 𝑞−1 = 1


#### Exponentiation in ℤ

```
∗
𝒑𝒒
```
- We want to exponentiatefor encryption.
- Not all integers in {1,2,...𝑝𝑞−1} belong to ℤ∗𝑝𝑞.
    - These elements do not necessarily have a
       unique inverse in ℤ∗𝑝𝑞
- Let 𝑒 be an integer, 1 < 𝑒 < (𝑝−1)(𝑞−1)
- **Question: when is exponentiation to the** 𝒆 **-th**

```
power, 𝒙 → 𝒙𝒆 , a one-to-one oper. in ℤ∗𝑝𝑞?
```

#### Exponentiation in ℤ

∗

#### 𝒑𝒒 -

- **detailsClaim** : If 𝑒 is relatively prime to 𝑝−1 𝑞−1  then 𝑥 ⟶
    𝑥𝑒 is a one-to-one op. in ℤ∗𝒑𝒒
- **Constructive proof** : Since gcd (𝑒, (𝑝−1)(𝑞−1)) = 1, 𝑒
    has a multiplicative inverse mod (𝑝−1)(𝑞−1)
- Denote it by 𝑑, then 𝑒𝑑 = 1 + 𝐶(𝑝−1)(𝑞−1), 𝐶 constant
- Let 𝑦 = 𝑥𝑒, then 𝑦𝑑 = 𝑥𝑒 𝑑 = 𝑥1+𝐶 𝑝−1 𝑞−1 =

```
𝑥^1 𝑥𝐶 𝑝−1 𝑞−1 = 𝑥 𝑥 𝑝−1 𝑞−1
```
```
𝐶
= 𝑥·1 = 𝑥
```
- Meaning 𝑦 ⟶ 𝑦𝑑 is the inverse of 𝑥 ⟶ 𝑥𝑒
    QED


39

#### RSA public key

- **cryptosystem** Let 𝑁 = 𝑝𝑞 be the product of two primes
- Choose 1 < 𝑒 < 𝜑(𝑁) such that gcd 𝑒, 𝜑 𝑁 = 1
- Let 𝑑 be such that 𝑑𝑒 ≡ 1 𝑚𝑜𝑑 φ(𝑁)
- The public key is (𝑒,𝑁)
- The private key is (𝑑, 𝑁)
- Encryption of 𝑀∈ℤ𝑁 by 𝐶 = 𝐸(𝑀) = 𝑀𝑒 mod 𝑁
- Decryption of 𝐶∈ℤ𝑁 by 𝑀 = 𝐷(𝐶) = 𝐶𝑑 mod 𝑁
The above-mentioned method should not be confused with
the exponentiation technique presented by Diffie and
Hellman to solve the key distribution problem


40

#### Why decryption works

- Since𝑒𝑑 ≡ 1 (mod φ), there is integer𝑘s.t.
    𝑒𝑑 = 1 + 𝑘𝜑,𝜑 = (𝑝−1)(𝑞−1)
- Ifgcd (𝑚, 𝑝) = 1then (by Fermat)𝑚𝑝−1≡ 1 (mod 𝑝)
- raise both sides to the power𝑘(𝑞−1)and then multiply both sides
    by𝑚, and get
       𝑚1+𝑘(𝑝−1)(𝑞−1)= 𝑚𝑒𝑑≡ 𝑚 (mod 𝑝)
- Ifgcd (𝑚, 𝑝) = 𝑝(no other possibilities!) then the last congruence
    still holds because both sides congruent to 0  mod 𝑝, because𝑚 =
    𝑗𝑝, for some 𝑗 ≥ 1(𝑚is multiple of𝑝)
- Hence, in both cases,𝑚𝑒𝑑 ≡ 𝑚 (mod 𝑝)
- Similarly,𝑚𝑒𝑑 ≡ 𝑚 (mod 𝑞)
- Sincegcd (𝑝, 𝑞) = 1, it follows (by Chinese Remainder Theorem)
    𝑚𝑒𝑑 ≡ 𝑚 (mod 𝑁)


41

#### RSA

- key length is variable
    - the longer, the higher security
    - 2048-4096 bits are common
- block size also variable
    - but |plaintext| ≤ |N|(in practice, for avoiding weak cases,
       |plaintext| < |N|)
    - |ciphertext| = |N|
- note that plaintext and ciphertext are numbers < N
- slower than symmetric ciphers
    - not used in practice for encrypting long messages
    - mostly used to encrypt a symmetric key, then used for
       encrypting the message
          - key exchange


## RSA – an example

#### Historical note

- The original paper presented an example by
    exchanging 𝑑 and 𝑒
- This is not relevant because the two keys have the
    same behaviour
- You can use any of the two keys for encrypting and
    the other key for decrypting
- You can choose any key to be the private one, then
    the other will be the public one
       - Or vice versa
- In the example that follows we restore the use of 𝑒 and
    𝑑 to match what we have presented


#### Multiplicative inverses

- The Extended Euclidean algorithm is used
- Based on **[[Bézout's identity]]** : given two non-zero integers 𝑥
    and 𝑦 there exist signed integers 𝑎and 𝑏 such that $$𝑎𝑥 + 𝑏𝑦 =
    gcd (𝑥,𝑦)$$ where $gcd$ is the Greatest common Divisor
- If 𝑥 and 𝑦 are **[[Coprime]]** then 𝒂𝒙 + 𝒃𝒚 = 𝟏
    - Key for computing multiplicative inverses
    - 𝑎𝑥 = 1−𝑏𝑦
    - Apply to both sides mod 𝑦 (remember the [[mod operator]])
    - 𝑎𝑥 ≡ 1 (mod 𝑦) (since 𝑏𝑦 ≡ 0 (mod 𝑦))
    - 𝑎 ≡ 𝑥−1 (mod 𝑦) and (similarly) 𝑏 ≡ 𝑦−1 (mod 𝑥)
- Remember: multiplicative inverses are equivalence classes

*Note*: in the exam the professor wants also the interpretation of the meaning of the [[Bézout's identity]] given a specific number. he doesn't want us to write the algorithm but he want us to understand what the [[Bézout's identity]] is.

#### Overview on the Extended Euclidean Algorithm EEA

- Classical Euclid's algorithm can be extended to
    maintain the equality $𝑢_𝑖𝑥 + 𝑣_𝑖𝑦 = 𝑟_𝑖$
- At the end, $𝑟_𝑘 = 1$ (for some 𝑘)
    - equality converges to Bézout's identity
- Construction is based on correct initialization
- Maintenance of equality can be obtained by suitable
    update of non-constant values and proved by
    induction

#### The EEA algorithm

```
function extendedEuclid(a, b) //in the last slide a=x and b=y
// Assumes gcd(a, b) = 1     //so they are Coprime
x0 ← 1, y0 ← 0    //those are the starting values
x1 ← 0, y1 ← 1
```
```
while b ≠ 0
q ← a div b
(a, b) ← (b, a mod b)
(x0, x1) ← (x1, x0 - q * x1)
(y0, y1) ← (y1, y0 - q * y1)
```
```
return (x0, y0) // such that a*x0 + b*y0 = 1
```


#### A small example

- Let p = 47, q = 59, N = pq = 2773
    - φ(N)= 46×58 = 2668 (that's the [[Euler's totient function]])
- Pick e = 157 (gcd(2668, 157) = gcd(157, 156) = gcd(156, 1) =
    gcd(1, 0) = 1), then 157×17 – 2668 = 1, so d = 17 is the inverse of
    157 mod 2668
- For N = 2773 we can encode two letters per block, using a two-digit
    number per letter:
- blank = 00, A = 01, B = 02, ..., Z = 26
- Message: ITS ALL GREEK TO ME is encoded
![[Pasted image 20251030153054.png]]
#### A small example

- N = 2773, d = 17
- ITS ALL GREEK TO ME is encoded as
    0920 1900 0112 1200 0718 0505 1100 2015 0013 0500
- First block M = 0920 encrypts to$$M^d= M^{17} = (((M^2 )^2 )^2 )^2 ×M = 948 (\bmod 2773)$$
- The whole message (10 blocks) is encrypted as
    `0948 2342 1084 1444 2663 2390 0778 0774 0219 1655`
- Indeed $0948^d = 0948^{157} = 9481+4+8+16+128 = 920 (\bmod 2773)$, etc.

#### Choice of exponents

- Each of the two exponents can be chosen at random
    - as long as coprime to (𝑝−1)(𝑞−1) = 𝜑
- The other exponent is its multiplicative inverse mod 𝜑
- First exponent is often chosen small (e.g., 65537)
    - good for the public exponent

## RSA – purposes of  encryption

#### RSA: two ways for

- Recall the existence of two keys **encrypting**
    - public
    - private
- Depending on which key is used, RSA encryption
    behaves differently
- Alice encrypts a block M using
    - Bob's public key (any public key can be
       used)
    - Alice's private key (only the owner can use
       their private key)


#### RSA: effects

- Encryption by a public key
    - everybody can encrypt by using a pub key
    - only the owner of the corresponding private
       key can decrypt
    - confidentiality
- Encryption by a private key
    - only the owner can encrypt
    - everybody can decrypt
    - no [[Confidentiality]]
    - [[Non-Repudiation]]?

*note*: imagine if the attacker sends to alice another public key which is different from the bob's public key. Alice encrypt with the fake bob's public key, and only the adversary can decrypt. bob cannot even understand the ciphertext.
#### Non-repudiation

- The sender of a message cannot deny
    having sent it
- It provides proof of origin and integrity
- Typically reached through a digital
    signature
- HMAC doesn't provide non-repudiation
    - A judge can't attribute the message to
       one of the parties sharing the HMAC
       key


#### Purposes

- Encryption with pub key
    - [[Confidentiality]]
    - mainly used for key-exchange
    - not used for messages longer than
       one block (or ≥ N)
- Encryption with pvt key
    - [[Integrity]], [[Authenticity]]
    - [[Non-Repudiation]]


#### Discussion (confidentiality)

- RSA is not used to encrypt long files because it
    is inefficient and insecure for that purpose.
    Instead, RSA is typically used for key exchange
    (or digital signatures)
       - Perfomarce issues. Symmetric ciphers
          much faster
       - Size limitation. Number should be < N
       - Security. RSA is deterministic unless
          padded
       - Battery draining
- [[Hybrid Encryption]]. Key exchange + AES
    - Only few bits are encrypted


#### Discussion ([[Non-Repudiation]])

- Disregarding the performance issues, RSA encryption with private key is a path to [[Non-Repudiation]]
- Because public can repeatedly decrypt a message and see that it was originated by who encrypted
	- the process is a verification, like [[MAC]] verification


#### Not yet non-repudiation

**Existential forgery example:**
- Let 𝑈 and 𝑉 respectively be public and private key of Alice
- Imagine that we expect non-repudiation if Alice sends pair (𝑀,𝑆) where $𝑆 = 𝐸_𝑉(𝑀)$
- Everybody can verify that $𝐸_𝑈(𝑆)$ = 𝑀 and understand that Alice sent the pair
    - **recall that in RSA encryption & decryption are same op**

 **Forgery:**
- Fran (attacker) creates a random binary file 𝑅
    - many implementation details missing
- Fran computes $𝐷 = 𝐸_𝑈(𝑅)$
- Fran (pretending to be Alice) sends to Bob pair (𝐷,𝑅)
- Bob verifies and checks that $𝐷 = 𝐸_𝑈(𝑅)$
- Even if 𝐷 is meaningless the existential forgery is successful
       - Bob got direction to accept
       - Whatever file can be interpreted as a sequence of integers


#### RSA signature

- Alice sends pair $(𝑀,𝐸_𝑉(𝐻(𝑀))$, where 𝐻 is cryptographic hashing function
- Previous attack doesn't work because 𝐻 is [[OWF]] (One Way Function)
    - Fran cannot get a message to send
- Encrypting a hashing is not demanding because of its small size
- Still **theoretical** (just mathematical), some further details to be discussed later

the digital encryption is not just an encryption of the message with the key but is the encryption of the digest of the message
#### Bob's verification

- Bob receives a pair (𝑀,𝑆) from somebody pretending to be Alice
- Bob computes $𝐻(𝑀) = ℎ_1$
- Bob computes $ℎ_2 = 𝐸_𝑈(𝑆)$
- If $ℎ_1 = ℎ_2$ **accept** , else **reject**
- **[[Non-Repudiation]] only when verification accepts**
    - 𝑯 **guarantees data [[Integrity]]**
    - **Encrypted by** 𝑽 **guarantees [[Authenticity]]**

notice that the fact we are working with digests, it is possible to suffer the birthday bound. of course we can defend our self by using a big enough digest (SHA-256 for example, is great).

## "textbook" RSA weaknesses
#### "textbook" RSA is not always robust
- There are several vulnerabilities in the original definition of RSA
- Let's examine the main
#### Attacks on RSA

1. **Factor $N = pq$**. This is believed hard unless p, q have
    some “bad” properties. To avoid such primes, it is
    recommended to
       - Take **p, q large enough** (at least ~1024 bits each)
       - Make sure **p, q are not too close together**
       - Make sure both **(p-1), (q-1) have large prime factors**
          (to foil Pollard’s rho algorithm)
             - special-purpose integer factorization algorithm
                (John Pollard, 1975); particularly effective at
                splitting composite numbers with small factors.
2. **Some messages might be easy to decrypt**
#### RSA and factoring

- Fact 1: given **N, e, p** and **q** it is easy to compute **d**
- Fact 2: given **N, e
    - if you factor **N**  ([[Factorize a Number]]) then you can compute φ(N) and d
- Conclusion
    - If you can factor N, then you break RSA
    - If you invert RSA, then you can factor N?
       **OPEN PROBLEM**: there is no a solution yet to this problem


#### Factoring RSA challenges

- RSA (the company) challenges: factor N = pq
- RSA Security has published factoring challenges
    - RSA 426 bits, 129 digits: factorized in 1994 (8
       months, 1600 computers on the Internet (10000
       Mips))
    - RSA 576 bits, 173 digits: factorized in dec. 2003,
       $10000
    - RSA 640 bits, Nov. 2005, 30 2.2GHz-Opteron-CPU
- Challenge is not active anymore (2007)


#### A case study

- June 2008: Kaspersky Labs analyzed a variant of the Gpcode
    [[Ransomware]] that used RSA encryption with a 1024-bit key to
    lock victims’ files
- Kaspersky proposed a global distributed computing effort to
    break the key. Estimate (from their website):
       - ~15 million modern computers
       - Running for ~1 year
       - To factor a single 1024-bit RSA modulus
- This estimate was theoretical only—no such project was
    launched
- Result: The RSA key was not broken. Victims could only
    recover files via backups or by paying ransom
- The case illustrated the practical strength of RSA-1024 (as of
    2008) against classical brute-force factoring


#### RSA - Attacks

- There are messages m easy to decrypt:
    if $m = 0, 1, N-1$ then RSA(m) = m
       - notice e must be odd ≥ 3, hence $(N-1)^e \bmod N ≡ N-1$, because $(N-1)^2 \bmod N ≡ 1$
       - SOLUTION: rare, use salt
- If both m and e are small (e.g., e = 3) then we
    might have $m^e < N$; hence $m^e \bmod N = m^e$
       - compute e-th root in arithmetic is easy:
          adversary compute it and finds m
       - **SOLUTION: Add nonzero bytes to avoid small messages**


#### RSA - Attacks

Small e (e.g., e = 3)
- Suppose adversary has two encryptions of similar messages such as
	- $c_1 = m^3 \bmod n$, and $c_2 = (m+1)^3 \bmod n$
	Therefore
	- $m = (c_2 + 2 c_1 - 1) / (c_2 - c_1 +2)$
- The case m and (am + b) is similar

**SOLUTION: Choose large e**

![[Pasted image 20251030172117.png]]


#### Some attacks use CRT

**Chinese Remainder Theorem (CRT)**

- Suppose $n_1 , n_2 , ..., n_k$ are positive integers which are pairwise [[Coprime]]. Then, for any given integers $a_1 , a_2 , ..., a_k$, there exists an integer x solving the system of simultaneous congruencies.
- Furthermore, all solutions x to this system are congruent modulo the product $N = n_1n_2...n_k$


#### RSA - Attacks

- Assume e = 3 and then send the same message three times to three different users, with public keys
       $(3, n_1 ) (3, n_2 ) (3, n_3 )$
- **Attack** : adversary knows public keys and
	    $m^3 \bmod n_1$ , $m^3 \bmod n_2$ , $m^3 \bmod n_3$
- He can compute (using CRT)
    $m^3 \bmod (n_1 ∙n_2 ∙n_3 )$
- Moreover $m < n_1 , n_2 , n_3$ ; hence $m^3 < n_1 ∙n_2 ∙n_3$ and
    $m^3 \bmod n_1 ∙n_2 ∙n_3 = m^3$
- Adversary computes cubic root and gets result
- **SOLUTION: Add random bytes to avoid equal messages**

#### RSA - Attacks

- If message space is small, then adversary can test all possible messages
- example: adv. knows encoding of m and knows that m is either $m_1 =10101010$ or $m_2 =01010101$
	- adversary encrypts $m_1$ and $m_2$ using public key and verifies
- **SOLUTION: Add random string in the message**

#### RSA - Attacks

- If two user have same n (but different e and d) then
    bad
       - One user could compute p and q starting from
          his e, d, n (somewhat tricky, based on Euler’s
          theorem – see for instance “The Handbook of
          Applied Cryptography”, Sect. 8.2.2)
       - Then, the user could easily discover the secret
          key of the other user, given his public key
- SOLUT. Each person chooses his own n (the
    probability two people choose same n is very very low)


#### Discussion

- Many mitigations follow similar patterns
- Additional attacks will be discussed later
- These considerations highlight the necessity of
    preprocessing messages before RSA encryption
       - In cryptographic contexts, this preprocessing is
          referred to as padding


##### Other attacks

##### to RSA


#### Multiplicative property and

#### malleability

- In cryptography a function 𝑓 is said to have a
    multiplicative homomorphism (or simply be
    multiplicative) if 𝑓 𝑚 1 ∙𝑚 2 ≡ 𝑓 𝑚 1 ∙𝑓 𝑚 2  mod 𝑛
- This is true for RSA encryption: RSA 𝑚 1 ∙𝑚 2 =
    RSA 𝑚 1 ∙RSA 𝑚 2
- This property is what makes RSA **malleable** : an
    attacker can modify a ciphertext in a predictable
    way without knowing the plaintext, by exploiting
    this multiplicative behavior


#### Attacks on RSA

❑ Multiplicative property of RSA:
❑ If M =M1*M2 then (M1*M2)e mod N=
((M1e mod N) * (M2e mod N) )mod N
Hence an adversary can proceed using small
messages (chosen ciphertext, see next slide)

```
❑ Can be generalized if M= M1*M2* ...*Mk
❑ Solut.: padding on short messages
```

#### Attacks on RSA

Adversarywants to decrypt C = Me mod n

1. adv. computes X = (C∙2e) mod n
2. adv. uses X as chosen ciphertextand asks the oracle for Y
    = Xd mod n
but....
X = (C mod n)∙(2e mod n) = (Me mod n)∙(2emod n) = = (2M)e
    mod n
thus adv. got Y = (2M)


#### Attacks on RSA

Chosen ciphertext attack (more general):

❑ Adv. T knows c = Me mod n
❑ T randomly chooses X and computes
c’ = c Xemod n and ASKS ORACLE TO
DECRYPT c’
❑ T computes (c’)d = c d (X e) d = M X mod n!!
❑ SOLUT: require that messages verify a given structure
(oracle does not answers if M does not verify requirements)


#### Attacks on RSA

Implementation attacks

❑ Timing: based on time required to compute Cd

❑ Energy: based on energy required to compute
(smart card) Cd

❑ Solut.: add random steps in implementation


#### RSA - Attacks : conclusion

Textbook implementation of RSA is NOT safe

❑ It does not verify security criteria

❑ Many attacks

There exists a standard version

❑ Preprocess (pad) M to obtain M’ and apply RSA
to M’ (clearly the meaning of M e M’ is the same)


#### PKCS

**PKCS # Title Function / Description Status / Adoption**

**PKCS #1** RSA CryptographyStandard RSA encryption, signatures,and padding Widely used; partsadopted in **RFC 8017**

**PKCS #3** Diffie-Hellman KeyAgreement Diffie–Hellman keyexchange format

```
Obsolete; replaced by
IETF standards (e.g.,
RFC 2631)
```
**PKCS #5** Password-BasedCryptography

```
Defines PBKDF1, PBKDF2,
encryption schemes based
on passwords
```
```
Widely used; part of
RFC 8018
```
**PKCS #6** ExtendedCertificate Syntax Defines certificateextensions Obsolete; supersededby **X.509v3**

```
PKCS stands for Public-Key Cryptography Standards. These are standards
developed by RSA Laboratories in early 90s to facilitate the secure
implementation and interoperability of public-key cryptography
```

#### PKCS (2)

**PKCS # Title Function / Description Status / Adoption**

**PKCS #7** CryptographicMessage Syntax

```
Format for
signed/enveloped data
(original S/MIME basis)
```
```
Superseded by CMS
(RFC 5652)
```
**PKCS #8** Private KeyInformation Syntax

```
Standard for storing private
keys with optional
encryption
```
```
Widely used; in
OpenSSL , Java , etc.
```
**PKCS #9** Selected AttributeTypes Defines standard attributesfor use in PKCS#7, #8, #10 Still relevant

**PKCS #10** Certificate RequestSyntax (CSR) Format for CertificateSigning Requests (CSRs) Ubiquitous in TLS/PKI(e.g., OpenSSL req)


84

#### PKCS (3)

```
PKCS # Title Function / Description Status / Adoption
```
```
PKCS #11
```
```
Cryptographic
Token Interface
(Cryptoki)
```
```
API for interacting with
cryptographic hardware
(e.g., HSMs, smartcards)
```
```
Actively maintained
by OASIS , latest: v3.1
```
```
PKCS #12
```
```
Personal
Information
Exchange Syntax
```
```
Container for certs, private
keys, etc. (e.g., .p12, .pfx)
```
```
Still widely used in
Windows, browsers
```
```
PKCS #13 Elliptic CurveCryptography ECC primitives and formats
```
```
Rarely used directly;
ECC now in other
standards (e.g., RFC
7748)
PKCS #15
```
```
Cryptographic
Token Information
Format
```
```
Standard format for storing
cryptographic objects on
tokens/smartcards
```
```
Used in smartcard
infrastructure
```

#### PKCS #1 (old version)

Standard to send message M using RSA. The result of

padding is m

**m = 0 ║ 2 ║ at least 8 non-zero bytes ║ 0 ║ M**

- first byte 0 implies message is less than N
- second byte (= 2) denotes encrypting of a message (1
    denotes non-repudiation use)
- random bytes imply
    - same message sent to many people is always
       different
    - space of messages is large


##### Overview on a

##### selection of

##### PKCS


#### PKCS — 1

**st**

#### overview

- Public-Key Cryptography Standards (PKCS) developed by

```
RSA Laboratories
```
- Initially focused on RSA algorithms, later expanded to broader

```
cryptography
```
- Define widely used formats and protocols
- Some drafts addressed advanced or experimental topics:
    - Not always standardized or implemented
    - Several are now considered obsolete or legacy


#### PKCS — 2

**nd**

#### overview

- Range from PKCS#1 (RSA) to PKCS#15 (tokens)
- Some merged into RFCs (e.g., PKCS#7 → CMS,

```
PKCS#10 → CSR)
```
- Focus here on some...
- Key idea: interoperability across vendors


# PKCS #3 —

# Diffie–Hellman

# key agreement


#### What is PKCS #3?

- Defines Diffie–Hellman (DH) key exchange
- Each party generates public/private pair
- Compute shared secret: gab mod p
- Used for session keys


#### PKCS #3 in context

- Originally specified how Diffie-Hellman parameters were

```
encoded
```
- Obsolete — superseded by ANSI X9.42 and RFC 2631

```
(Diffie-Hellman Key Agreement Method)
```
- Further refined in RFC 3526
- Historically important: first standardized DH parameter

```
encoding
```
- Applications: TLS (legacy, now deprecated), IPsec (DH

```
groups)
```

# PKCS #5 —

# Password-based

# encryption (PBE)


#### PKCS #5 – Motivation

- Users can remember passwords, but not long
    cryptographic keys
- A secure method is needed to derive keys from
    passwords
- Passwords have low entropy and require strengthening
    (e.g., with PBKDFs such as PBKDF2, bcrypt, scrypt,
    Argon2)


#### PKCS #5 – Applications

- Wi-Fi (WPA/WPA2) uses PBKDF2 to derive the
    Pairwise Master Key
- Password managers (e.g., KeePass, 1Password) rely
    on PBKDF2
- PKCS #12 protects private keys using password-based
    encryption
- Modern KDFs (e.g., Argon2) build on concepts
    introduced in PKCS #5


#### PKCS #5 – Mechanism

- Key derivation via PBKDF1 (legacy) and PBKDF2
    (standard)
- Inputs: password, salt, iteration count, pseudorandom
    function (e.g., HMAC-SHA256)
- Output: derived cryptographic key (suitable for
    encryption or authentication)
       - Example: PBKDF2(password, salt, iterations,
          dkLen)


## PKCS #8 — Private

## key information

## syntax


#### PKCS #8 – Purpose

- Defines the ASN.1 syntax for representing private keys
- Supports multiple key types: RSA, EC, DH, etc.
- Private keys can be encrypted using password-based
    encryption (PBE, PKCS #5)


#### PKCS #8 – Structure

- Structure of PKCS #8 private keys
- PrivateKeyInfo
    - AlgorithmIdentifier
    - PrivateKey (OCTET STRING)
    - Attributes (optional, PKCS #9)
- EncryptedPrivateKeyInfo
    - EncryptionAlgorithm
    - EncryptedData


#### PKCS #8 – Usage

- PEM file encodings
    -----BEGIN PRIVATE KEY----- (unencrypted PKCS #8)
    -----BEGIN ENCRYPTED PRIVATE KEY----- (PKCS #8 with PBE)
- Used in OpenSSL, PKI exports, secure key storage,
    TLS/HTTPS


# PKCS #9 —

# Selected

# attribute types


#### PKCS #9 – an overview

- Defines attributes to be used with PKCS objects
- Provides extensibility in PKI
- Examples of attributes
    - challengePassword (used in PKCS #10 CSR for
       renewal/revocation)
    - emailAddress, unstructuredName
    - Custom attributes via Object Identifiers (OIDs)
- Importance
    - Enable richer identity representation in certificates
    - Still used in CSRs and directories (X.500/X.509)


# PKCS #11 —

# Cryptoki API


#### Cryptoki (PKCS #11)

- Stands for “Crypto Key API”
- Standard C API for interacting with
    - HSMs (Hardware Security Modules)
    - Smart cards, USB tokens
- Architecture
    - Slot = interface/reader
    - Token = cryptographic device
    - Session = active connection
    - Objects = keys, certs, data
- Supports: key management, authentication, encryption,
    signing, RNG
- Vendor-independent


#### Cryptoki (PKCS #11)

#### applications

- Enterprise PKI: integration with HSMs
- Digital signatures, TLS termination with HSMs
- Smart card logins (Windows, Linux)
- Still evolving: adoption in cloud HSMs and modern key
    management


## PKCS #12 —

## Personal

## information

## exchange


#### PKCS #12 — Purpose &

#### structure

- Defines a container format to bundle certificates, private
    keys, and related data
- Per-object protection: private keys can be encrypted using
    PKCS #5 PBE
- Container-level protection: the entire PFX file can also be
    password-encrypted
- PFX (Personal Information Exchange) container
- Contains “safe bags” (logical containers)
    - certBag (certificates)
    - keyBag (private keys)
    - CRLBag (revocation lists)


#### PKCS #12 — Usage

- File extensions: .pfx, .p12
- Used for certificate import/export (browsers, OS stores,
    VPN/Email clients)
- Transport and backup of user credentials (certificates +
    private keys)
- Widely supported by Microsoft (Windows), OpenSSL,
    and other tools


## PKCS #15 —

## Cryptographic

## token information

## format


#### PKCS #15 — Overview

- Goal: standardize file structure on cryptographic tokens,
    ensure interoperability across vendors
- Token: hardware or software container holding cryptographic
    material (e.g., smart card, USB token, HSM, virtual token)
- Objects on token: keys (private/public), certificates,
    PINs/authentication data, access control structures
- Applications: eID cards, passports, healthcare cards,
    enterprise access cards
- In practice
    - PKCS #15 = storage format (how data is structured on
       token)
    - PKCS #11 = access interface (how applications use the
       token)



---
