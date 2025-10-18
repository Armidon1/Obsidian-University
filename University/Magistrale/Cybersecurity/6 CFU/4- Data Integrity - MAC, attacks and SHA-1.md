	# DATA INTEGRITY
### What is data integrity?
- Integrity = trust in the unaltered state of information
- Goal: prevent undetected or unauthorised changes
- Part of the CIA triad
  - Confidentiality
  - Integrity
  - Availability

Data integrity guarantees that the source of the information is authentic. *we do data integrity without confidentiality for now*, this because confidentiality is not always needed because the information itself is not sensitive.

### Simple Analogy
**Sealed envelope**
- You receive a letter with an intact seal
- You assume the content hasn’t been altered
- If the seal is broken $\Rightarrow$ loss of integrity

### Why integrity matters
<span style="color:orange">Medical example</span>
- Patient record
10 mg $\Rightarrow$ altered to $\Rightarrow$ 100 mg
- Consequences: severe or fatal errors

<span style="color:orange">Finance & Contracts</span>
- Transaction amount altered
- Bank account changed
- Digital contract edited after signing

<span style="color:orange">Software & information</span>
- Software update injected with malware
- Download from web sites
- News article subtly modified to spread disinformation

### What threatens integrity?
- **Human error**: typos, wrong input
- **Hardware failure**: bit rot, power loss
- **Malicious tampering**: insider edits
- **Transmission errors**: corrupted network packets

Transmission errors are no longer a big problem. That's because, thanks to the last technological improvement, this happens very rarely.

### Two facets of integrity
1) **Data Integrity**
Ensures the content stays unchanged. Data Integrity can also be threatened in the case where the source is duplicated.

2) **Origin Integrity (authenticity)**
Ensures the sender is legitimate

fun fact: servers will always be violated somehow. servers are managed by a group of people, when attackers are thousands. 

### What do we want?
- A way to detect unauthorized changes
- Confidence that the information is authentic
- Methods exist to verify integrity
	- seen later
- Integrity cannot be guaranteed proactively; it can only be verified upon inspection
	- on verification failure, typical response is to reject the data, as recovery is generally not feasible

we can design using an approach called security by design. in this case, we are making things harder to the adversary. in general we cannot be sure about integrity. how can we satisfy integrity? On verification failure, we cannot obtain in any case the original information. all we can do is ask to re-transmit again. 
### Summary
- Integrity = unaltered, trustworthy data and source
- Critical in: healthcare, finance, law, journalism etc.
- Foundation for trust in digital systems
- Before any algorithm, the need for integrity is universal
- Integrity is perhaps the unique information security requirement that is always desired

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
- $A_{k}(m)$ is called the authentication tag of m

Requirement – $V_{k}(m,A_{k}(m))$ = “accept”
- The authentication algorithm is called MAC (Message Authentication Code)
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
### CBC Mode MACs
- Start with the all zero seed

- Given a message consisting of n blocks M1,M2,…,Mn, apply CBC (using the secret key k)
![[Pasted image 20251009154828.png]]


###  **CBC-MAC is insecure for variable-length messages**
- CBC-MAC is secure only for fixed-length messages; it is insecure when message lengths can vary.

- An attacker who knows valid message–tag pairs $(m, t)$ and $(m', t')$ can construct a new (longer) message $m''$ such that $CBC-MAC_k(m'') = t'$. This is not a mere replay: $m''$ is a new message that the verifier will accept as if it came from the legitimate sender.

- Construction: XOR the first block of $m'$ with $t$ and concatenate:
  - $m'' = m || (m1' XOR t) || m2' || … || mℓ'$
  - After processing $m$ the CBC state equals $t$; processing $(m1' XOR t)$ produces the same block-cipher input as $m1'$, so the remainder of the MAC computation reproduces the tag $t'$.

- Why this is dangerous: even if $m''$ is built from previously seen blocks, the concatenated sequence can have a different application-level meaning (e.g., multiple bank transfers, chained IoT commands, or a combined firmware image) and therefore cause real damage.

- Short mitigations:
  - Do not use CBC‑MAC on variable-length messages.
  - Prefer CMAC or HMAC for variable-length data.
  - Alternatively, include an unambiguous length prefix or use domain separation / context binding when authenticating messages.

###  **final remarks on CBC-MAC**
- secure only for messages of fixed, known length
    
- if confidentiality is also needed you can use CBC, but with a different shared key
    
- still present in some legacy or constrained-use standards
    
- understanding its vulnerability on variable-length messages is crucial for secure design

you mustn't use CBC-MAC. You can use it only if is necessary backward compatibility: in many cases it is not possbile to keep everything up to date. unfortunally, in those situation you have to keep old mechanism like CBC-MAC

##  **Attacks to integrity**
### **Recap – Adversary’s goal**
- An adversary tries to forge a message–tag pair (m, τ) such that the verifier accepts it as valid:
	 Vk(m, τ) = "accept"
    
	where τ = MACk(m)
    
- Such an adversary is called a **forger**, and the accepted pair (m, τ) is called a **forgery**

### FORGERY
There are three types of forgery, with different power
- Existential (E)
- Selective (S)
- Universal (U)

###  **Existential forgery (E)**
- Adversary creates any message/signature pair (m,σ), where σ was not produced by the legitimate sender/author
- Adversary need not have any control over m; m need not have any meaning
- Existential forgery is essentially the weakest adversarial goal; therefore the strongest schemes are those which are "existentially unforgeable"
###  **Selective forgery (S)**
- Adversary creates a pair (m,σ) where m has been chosen by the adversary prior to the attack
- m may be chosen to have interesting mathematical properties with respect to the MAC algorithm; however, in selective forgery, m must be fixed before the start of the attack
- The ability to successfully conduct a selective forgery attack implies the ability to successfully conduct an existential forgery attack
- $S \Rightarrow E$
###  **Universal forgery (U)**
- Adversary creates a valid tag σ for any given message m
- It is the strongest ability in forging, and it implies the other types of forgery
- $U \Rightarrow S \Rightarrow E$
### use the contrapositive 
According to the basic rules of propositional logic
$(U \Rightarrow S \Rightarrow E) \iff (\neg E \Rightarrow \neg S \Rightarrow \neg U)$

***This means that if we can prevent E, then we are also able to prevent S and U***

### About the existential forgery
An existential forgery is considered a success even if the forged message is meaningless
- Upon successful verification, the receiver might
	- wonder: “Is it encrypted?”, “Why don’t I recognize the cipher?”
	- or simply treat the message as a valid sequence of numbers
(since any bitstring can be interpreted as a sequence of integers)

Success is defined by acceptance, not by semantic value

## HASHING FOR INTEGRITY
###  **Hash functions**
- Map large domains to smaller ranges
- Example h: ${0,1,…,p^{2}} \Rightarrow {0,1,…,p-1}$ defined by h(x) = ax+b mod p
- Used extensively for searching (hash tables) in computer science. 
- Collisions are resolved by several possible means – chaining, double hashing, etc. 
- The idea is to implement MAC by hashing
- We need to proceed step-by-step
- We'll consider two types of hashing functions
  - Unkeyed
  - Keyed
![[Pasted image 20251009164235.png]]
![[Pasted image 20251009164316.png]]

### Properties of hash functions
- Avalanche effect
  - if $H(M_{1})$ is the hash value of M1, then, even if M2 is different from M1 in only one bit, $H(M_{2})$ is strongly different from $H(M_{1})$ – small changes cause big differences
- Fast to compute (except special cases that are not related to integrity)
- All hash values have the same (short) length
	- For standards, efficient operations with values and verification
- A hash value should be a random sequence of bits

### About collisions
- Fact 1: collisions are (always) many
- Fact 2: the more uniformly distributed the better
- Fact 3: in traditional hashing function, although collisions are not welcome, these are handled with special algorithms
- Fact 4: in cryptography collisions are much more harmful
- In cryptography hash values have two names (synonymous)
	- **digest** (more common)
	- **fingerprint** (less common)

### Sending
Alice wants to send message $M$ to Bob, with data integrity
1) Alice computes $t=H(M)$, where $𝐻$ is an agreed hashing function
2) Alice sends $(M,t)$ to Bob

### Verification
Bob receives a pair $(M,t)$
1) Bob computes $h$, the fingerprint of $𝑀$
2) Bob compares $𝑡$ and $h$
	1) if $t=h$ accept
	2) if $t\neq h$ reject

even if we consider this approach in a positive way, because a collision is hard, an attacker can still find a collision. We cannot provide absolute guarantees of integrity.

### Practical case
- Alice is a web site
	- It contains a file $𝐹$, the name of $𝐻$ and the fingerprint $𝑓$
- Bob wants to download $𝐹$
	- He reads the name of $𝐻$, downloads $𝐹$ and $𝑓$
	- He gets $(F',f')$
	- Bob computes $𝐻(𝐹′)$ and verifies that this is equal to $𝑓′$
	- If equal, he accepts $𝐹′$ as $𝐹$, else no.

**But Fran may have compromised the web site and replaced $𝐹$ by $𝐹′′$ and $𝑓$ by $𝐻(𝐹′′)$ (so, verification still works)**

### Other possible attacks
- The attacker may intercept 𝑀1 and substitute it with a colliding message 𝑀2

- The attacker may intercept (𝑀1, 𝐻(𝑀1)) and substitute it with (𝑀2, 𝐻(𝑀2))
	- Partial mitigation: Alice sends 𝑀1 and 𝐻(𝑀1) using two different channels of communication
	- Still insecure because Fran can intercept both. Just more difficult

### Variant
- Bob may know already the fingerprint, so Alice doesn't need to send a pair: sending only message M is sufficient
- Still attacker can intercept transmission and replace M by a colliding M'
- *Collisions are a vehicle of attack!*

We must protect ourselves from collisions.
We must avoid small inputs because they are easy to collide.

![[SmartSelect_20251009_171303_Samsung Notes.jpg]]

### Summary
- Hashing functions are interesting candidate for implementing MAC functions
- Promising properties
- Still imperfect
- No origin authentication

- Some improvements are needed

### Birthday paradox and attack
**Idea first**
- The birthday paradox is the surprising probability result that in a group of just 23 people, there is a greater than 50% chance that at least two people share the same birthday
- This seems counter-intuitive because 23 is much less than 365, but the key lies in how many pairs of people can be formed
- In fact, with 23 people, there are 253 possible pairs (23 choose 2), and each pair has a 1/365 chance of sharing a birthday
- This means that even with a relatively small group, the probability of a collision (two people sharing a birthday) becomes significant

**Statement**
In a set of randomly chosen people, the probability that at least two of them share the same birthday exceeds 50% when the group has 23 or more individuals, assuming
- 365 equally likely birthdays
- no leap years
- birthdays are independent

**Proof**
- Build a group of people having different birthdays
- Can choose the first person in 3565 ways, the second in 364 ways, third in 363 etc.
- So, probability that first has a unique birthday is 1, for second is 364/365, this 363/365 etc.
- Probability n people have different birthdays is $P(n)=\prod_{(k=0)}^{(n−1)}(\frac{365−k}{365})$
- The probability at least two have same birthday is $1−𝑃(𝑛)$
	- $1−𝑃(23)$ is $0.5073$, in case n=23. so it exceeds the 50%! 

**The Birthday Paradox in numbers**
![[Pasted image 20251009172232.png]]
- Hashing can be seen as mapping people to birthdays, where the range size is 365
- After inserting the 23rd person into the group the probability of collision exceeds 50%

**The Birthday Paradox for length 𝑚 of range**
- Assume the range is defined by an 𝑚-bit output space ($2^𝑚$ digests)
- Then the probability that at least two messages collide exceeds 50% when
		$K≈1.177·2^{(𝑚/2)}$
- is the number of randomly chosen hashed messages being mapped into the range 
- ==*The bound only depends on range size*==, ****but**
- **domain should have at least 𝒌 elements**

### Birthday attack
- Let a cryptographic hash function output 𝑚-bit values
- A birthday attack finds two distinct colliding inputs 𝑥 ≠ 𝑦 with high probability after hashing roughly $k≈1.177·2^{(m/2)}$ inputs
- Note that the brute-force bound is $2^{𝑚}$
- In practice, 50% probability is exceeded after roughly $\sqrt(2^{𝑚})$ attempts
- Example: for 𝑚 = 128, a collision is expected after about $2^{64}$ hash operations

### Birthday attack: procedure
```python
#Assume H known
map = ∅
while True:
    m = generate_random_message()
    h = H(m)
    if h in hash_map:
 		return (map[h], m)
    hash_map[h] = m
```
### Remarks
- Expected number of iterations is $≈2^{(𝑚/2)}$
- Attacker can't control colliding messages
	- Existential forgery, the most dangerous
- The procedure can't be used for finding an element colliding with a given message
- The procedure reduces iterations from $2^𝑚$ (brute-force) to $2^{(𝑚/2)}$
- Digest lengths of around 160 (SHA-1) bits are deprecated, as they yield an expected effort of $2^{80}$ iterations — a threshold now considered feasible and progressively rising.

### Check numbers

note that

$2^{80}$ = 1,208,925,819,614,629,174,706,176

$2^{160}$ = 1,461,501,637,330,902,918,203,684,832,716,283,019,655,932,542,976

### Summary
- The birthday attack is a powerful technique for finding collisions in hash functions.
- It exploits the mathematics behind the birthday paradox to significantly reduce the number of required hash computations.
- Implementing a birthday attack requires careful consideration of the hash function's properties and the input space.

### Precisazione
**Concetto base**
- È un attacco per trovare collisioni in funzioni hash: due input distinti x ≠ y tali che $H(x) = H(y)$.
- Sfrutta il paradosso del compleanno: in uno spazio di N possibili output le collisioni compaiono dopo $≈√N$ tentativi.

**Complessità e formula**
- Se l'output è $m$ bit, il numero di possibili digest è $2^m$.  
- Probabilità di collisione ≈50% quando il numero di hash provati k soddisfa$$k ≈ \sqrt(2·2^m·ln 2) ≈ 1.177 · 2^{m/2}$$(si usa l'approssimazione $ln(1−x) ≈ −x$ per $k ≪ 2^m$).
- Quindi costo tipico per trovare una collisione: tempo ≈ $2^{m/2}$ (e nella versione naive anche memoria ≈ $2^{m/2}$).

**Procedura pratica (naive)**
- Supponendo che l'hacker sappia l'algoritmo $H(m)$ di hashing,
- Genera molti messaggi casuali, calcola $H(m)$, memorizza hash→messaggio; alla prima ripetizione ottieni una collisione.
- Variante: tecniche time–memory trade off (rainbow tables, distinguished points, van Oorschot–Wiener) riducono memoria o distribuiscono il lavoro.

Nota che però secondo la metodologia **Kerckhoffs**: le funzioni hash usate in sicurezza sono considerate pubbliche; la sicurezza non deve basarsi sul segreto dell'algoritmo. Nascondere H (security by obscurity) non è una difesa affidabile.

**Tipologie di attacco correlate**
- Collision attack (birthday): trova due messaggi qualsiasi che collidono (existential forgery).
- Chosen-prefix/collision: costruire due messaggi con prefissi scelti che collidono (più potente e complesso; usato contro SHA‑1).
- Preimage / second-preimage: trovare un messaggio che collida con un dato target; costo tipico ≈ 2^m (molto più difficile).

Impatto pratico
- Permette forgery di certificati, firme digitali, documenti PDF o file immagine in cui il verificatore si fida solo del digest.
- Attacchi reali: collisioni pratiche su MD5 (e attacchi pratici contro SHA‑1 con risorse industriali) hanno reso insicuri quegli algoritmi per scopi di sicurezza.

Mitigazioni e buone pratiche
- Usare digest più lunghi: SHA‑256/SHA‑3 (m ≥ 256) spostano il costo a livelli impraticabili.
- Per autenticazione, usare MAC basati su chiave (HMAC, CMAC) o firme digitali: knowledge of the key (o private key) è necessaria per produrre tag validi.
- Evitare hash deprecati (MD5, SHA‑1) per integrità/autenticazione.
- Applicare domain separation, salt/nonce, includere metadata non controllabili dall'attaccante.
- Per protocolli critici: policy di rotazione, verifica multipla, e controllo delle collisioni note (CT per certificati).

Quando preoccuparsene
- Se il digest ha m bits relativamente piccoli (es. ≤ 160), o se si usa hash non chiave come unico meccanismo di autenticazione.
- Se un attaccante può generare grandi quantità di input e sfruttare risorse parallele (GPU/ASIC/cluster).

## A hash example: SHA-1 (today Obsoleted)
### SHA-1 basics
- Developed by: NIST & NSA, published in 1995 (FIPS, a federal istitution tha publishes random stuff 180-1)
- like MD4 (Message Digest 4) & MD5. those are completely broken
- $|message|$ < $2^{64}$ bits , we also want that the message is a multiple of 512, and if the original message isn't so, we will pad it. the last 64 bits are used to communicate the original length in bits, to read the message properly. 
- $|digest|$ = $160$ bits, which is the output of the hash function SHA-1
![[Pasted image 20251009210659.png]]

we use SHA-256. this because it easy to find collision in SHA-1, because we can find those in a polynomial time. 
### SHA-1 overview
- The 160-bit message digest consists of five 32-bit words: $A$, $B$, $C$, $D$, and $E$.
- Before first stage: $A = 67452301_{16}$, $B = efcdab89_{16}$, $C = 98badcfe_{16}$, $D = 10325476_{16}$, $E = c3d2e1f0_{16}$.
- After last stage $A|B|C|D|E$ is message digest

### High-level scheme
We start from a constant, we use the first 512bits to get a partian digest, then i continue with the other 512 bits of the padded message.
![[Pasted image 20251009211141.png]]
the way we process each block, is always the same, see below...
## SHA-1: processing one block
A,B,C,D,E, are magic numbers.
Block  (512 bit, 5 32-bits words) 
- 80 rounds: each round modifies the  buffer (A,B,C,D,E)

**Round** (we are changing values, for example from $A$ to $E$):
$$
(A,B,C,D,E) \Leftarrow 
(E + f(t, B, C, D) + (A<<5) + W_t + K_t), A, (B<<30), C, D)
$$
$t$ number of round and $<<$  denotes left shift
$f(t,B,C,D)$ is a complicate nonlinear function (in reality is an easy function)
$W_t$ is a 32-bit word obtained by expanding original words into  80 words (using shift and ex-or) 
$K_t$ constants
![[Pasted image 20251009211516.png]]

## function f
$f(t, B, C, D) =$

$(B∧C)∨(~B∧D)$
$(0 ≤ t ≤ 19)$

$B⊕C⊕D$
$(20 ≤ t ≤ 39)$

$(B∧C)∨(B∧D)∨(C∧D)$
$(40 ≤ t ≤ 59)$

$B⊕C⊕D$
$(60 ≤ t ≤ 79)$

## Words wt
$w_0...w_{15}$ are the original 512 bits

for $16 ≤ t ≤ 79$
$w_t = (w_{t-3} + w_{t-8} + w_{t-14} + w_{t-16}) <<= 1$
"$<<=$" denotes left bit rotation

## SHA-1: round t
![[Pasted image 20251009212053.png]]
![[Pasted image 20251009212116.png]]
in reality, is not the input but the initials values. in the first stage, we have the user input, in the second stage, the initial value is the first stage output

## Summary on SHA-1
1) Pad initial message: final length must be ≡ 448 mod 512 bits
2) Last 64 bit are used to denote the message length
3) Initialize buffer of 5 words (160-bit) (A,B,C,D,E) (67452301, efcdab89, 98badcfe, 10325476, c3d2e1f0)
4) Process first block of 16 words (512 bits):
	1) expand the input block to obtain 80 words block $W_0,W_1,W_2,…,W_{79}$ (ex-or and shift on the given 512 bits)
	2) initialise buffer (A,B,C,D,E)
	3) update the buffer (A,B,C,D,E): execute 80 rounds
		1) each round transforms the buffer 
	4) the final value of buffer (H1 H2 H3 H4 H5) is the result
5) Repeat for following blocks using initial buffer (A+H1, B+H2,…)

### How to use SHA-1
We can simply use it in all operative systems, because is a primitive function. That's the command line:
```bash
shasum -a1 <file>
```
let's try to execute
```bash
>> echo "hello" | shasum -a1
output: f572d396fae9206628714fb2ce00f72e94f2258f  -
```
that's the SHA-1 of "hello". if doing echo $-n$, i'm not considering the newline
```bash
>>echo -n "hello" | shasum -a1
aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d 
```
as we can see, is present an avalanche effect and the hashes are completely different.
If i want to use SHA-256, a can simply use the command:
```bash
>>echo -n "hello" | shasum -a256
2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824 
```
it those cases, i simply used an "hello" text, but in the first command i can simply do the SHA of a file easilly. 
with the command:
```bash
man shasum
```
you can see everything of $shasum$

![[Pasted image 20251009212443.png]]
as the article says, SHA-1 was used until 2017 for HTTPS certificates. another this said by the prof is "don't use MD5".

## Types of SHA
- SHA-1 is Borderline
- SHA-2 contains SHA-256, SHA-512 and others
- SHA-3 are the new one


### Mathematical definition of hashing function 
**(in general, in the exam, the prof wants the exact same mathematical definition)**
Cryptographic hashing function has two properties:
1) one way
2) collision resistance: hard to find colliding pair but depends of the length of hash. if the digest is 64 bits, it is easy to find.


**HOMEWORK** (Due Sunday, October 19, 2025, at 11:59):
1) Use the OpenSSL API to implement and test multiple encryption and decryption operations with a fixed 128-bit symmetric key, randomly generated at initialization, using CBC mode.
2) Focus on the following algorithms: AES, Camellia (used in China as a standard), and SM4
	1) Compare **encryption** and **decryption** performance using three fixed input files: a 16-byte (the size of a block, you can notice the padding) text file, a 20KB text file, and a large (>2MB) binary file
3) Measure the execution times and present the result graphically (not tables, but drawings). Also, analyse and compare file sizes
4) include any source code in the report.
we can use whatever programming language, is suggested C/C++. 
Considering that report considers 3 files and for each file we have to do an encryption and decryption, for each 3 algorithm. 

