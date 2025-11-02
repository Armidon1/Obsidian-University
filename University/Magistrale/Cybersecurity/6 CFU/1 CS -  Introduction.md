## Information security

![[Pasted image 20251022145115.png]]
---

## Requirements	
![[Pasted image 20251022145128.png]]

Standard in ISO 27000

---
## Cryptography vs. security 
![[Pasted image 20251022145145.png]]


---
## Pre-computer cryptography

![[Pasted image 20251022145230.png]]

---
## Scytale cipher

![[Pasted image 20251022145339.png]]
Sparta, 700 BCE
a strip of parchment was wrapped around a wooden rod, and the message was written lengthwise
to decrypt, recipient needed a rod of same diameter

---
## The Egyptian pharaoh approach
**The sender**
1) Shaving a slave's hexadecimal
2) Carving the secret message into the skull
3) Waiting for the hair to grow black-box
4) Sending the slave to the recipient
**The recipient**
5) Knows he must shave slave's hexadecimal
6) After that, he could access the message

Timescales not comparable to today's


---
## Caesar cipher
Shift the alphabet by a predetermined number of positions (e.g. 3)

![[Pasted image 20251030200843.png]]
key = 3

attack: it is sufficient to test all possible keys (26)

---

## Alphabetic substitution

![[Pasted image 20251030200916.png]]
random permutation (26! = 403 291 461 126 605 635 584 000 000)

attack: use a computer for a frequency attack

---
## Polyalphabetic
More permutations (𝑙=3)
Replace symbol of text by using permutation 𝑖+1, where 𝑖 starts by 0 and increases mod 𝑙 
![[Pasted image 20251030201004.png]]
if long enough frequency analysis still effective

---
## Enigma
- one of the most advanced ciphers among the ancients (WWII)
    
- it encrypted each letter by passing it through a series of rotating electrical rotors, producing a different substitution with every keystroke
    
- broken by allied at Bletchley Park

easily broken by a computer because of the limited keyspace ≈1023 to 1026
see https://cryptii.com/pipes/enigma-machine 


one of the most advanced ciphers among the ancients (WWII)
it encrypted each letter by passing it through a series of rotating electrical rotors, producing a different substitution with every keystroke
broken by allied at Bletchley Park

---

## Conclusion
Many other examples are possible
In all examples sender and recipient must share some information
We call this shared information the Key (still today)

---

## Frequency analysis

uses computers
cryptoanalysis by frequency analysis

## Frequency of letters	

![[Pasted image 20251030201339.png]]
---

## Languages

They are typically public and available on the web
Several online resources exist
How to do it yourself
  - Take a large sample of text
  - Remove spaces, punctuation, and special symbols
  - Sort the remaining sequence of letters
  - Perform a simple block-based count


How to obtain frequencies:

- Clean encrypted text

- Normalize casing (all lowercase or uppercase)

- Compute basic frequencies

- Count the frequency of each individual character

- Use known frequency profiles from major languages ![[Pasted image 20251030201454.png]]
- Try aligning the most frequent letters of the encrypted text to each of these and see which language yields the most plausible results

---

## Frequency analysis(simplified) (3)

19

Look for language-specific patterns
  - common letter pairs (like TH, QU, CH, LL) or letter positions (e.g., Q followed by U is common in many languages)
  - common word lengths (e.g., 2-letter words in English: it, is, to)
  - repeated short patterns like la, le, de (Romance languages), or endings like -en, -er (Germanic languages)

Doesn’t work well on
short messages
polyalphabetic ciphers
modern encryption

---

## Model of encryption

used and accepted in all environments

## Model

![[Pasted image 20251030201541.png]]

---
## What is a key?

![[Pasted image 20251030201600.png]]
symmetric keys must remain confidential

---
## Communication model
![[Pasted image 20251030201616.png]]

---
## Threat (attack) model

![[Pasted image 20251030201630.png]]


---

## Adversary
![[Pasted image 20251030201649.png]]

---

## Terminology
|                  |                                                                                                                           |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------- |
| - **term**       | - **meaning**                                                                                                             |
| - **plaintext**  | - _information_ _that_ _will_ _be_ _encrypted_                                                                            |
| - **ciphertext** | - _information_ _that_ _has_ _been_ _encrypted__, i.e._ _transformed_ _into_ _incomprehensible_ _text_                    |
| - **key**        | - _sequence_ _of_ _fixed_ _length_ _of bits_ _that_ _appear_ _random; in the_ _symmetric_ _case_ _K__1_ _= K__2_          |
| - **cipher**     | - _pair_ _of_ _algorithms_ _for_ _encryption_ _and_ _decryption__,_ _often_ _denoted_ _as_ _(E, D)_                       |
| - **encryptor**  | - _entity_ _that_ _applies_ _a_ _cipher_ _(__algorithm_ _E),_ _producing_ _a_ _ciphertext_                                |
| - **decryptor**  | - _entity_ _that_ _applies_ _a_ _cipher_ _(__algorithm_ _D),_ _producing_ _a_ _plaintext_                                 |
| - **encryption** | - _the_ _operation_ _performed_ _by an_ _encryptor_                                                                       |
| - **decryption** | - _the_ _operation_ _performed_ _by a_ _decryptor_                                                                        |
| **adversary**    | _entity_ _that_ _attempts_ _to compromise_ _confidentiality__,_ _integrity__, or_ _availability_ _of information systems_ |


---

## Security goals
![[Pasted image 20251030201758.png]]

---
## Adversarial model

![[Pasted image 20251030201814.png]]

---
# Attack categories

against confidentiality and other requirements of information security

---
## What is in attack?

- Any intentional attempt to compromise the security of a computer system, network, or data by violating one or more core principles of information security, such as confidentiality, integrity, or availability 
- Some attacks do not directly target information security principles but serve indirect purposes, such as enabling future compromise or gathering intelligence 
- Remember, cryptography plays a fundamental role among the measures designed to uphold information security 

---
## First attacks
|                                      |               |                                                                                                |
| ------------------------------------ | ------------- | ---------------------------------------------------------------------------------------------- |
| - **type**                           | - **acronym** | - **description**                                                                              |
| - [[Eavesdropping]]                  | - —           | - secretly listening to private conversation of others without their consent                   |
| - [[Ciphertext-only attack (COA)]]   | - COA         | - attacker has only access to ciphertexts and tries to deduce the plaintext or key             |
| - [[Known-Plaintext Attack (KPA)]]   | - KPA         | - attacker knows pairs of plaintext and ciphertext and uses them to infer the key              |
| - [[Chosen-Plaintext Attack (CPA)]]  | - CPA         | - attacker can encrypt arbitrary plaintexts to gather information about the cipher             |
| - [[Chosen-Ciphertext Attack (CCA)]] | - CCA         | - attacker can decrypt arbitrary ciphertexts of their choice, except for the target ciphertext |

---

## Attacks may use an oracle

**An oracle** is a theoretical black-box function that an attacker can query to obtain outputs (e.g., ciphertexts or plaintexts), often under controlled conditions 

It is an abstract entity or mechanism that provides access to a cryptographic function without revealing its internal workings

---
## Selection of attacks

**Known plaintext**: attacker has samples of both plaintext and its encrypted version (ciphertext) and is at liberty to make use of them to reveal further secret information such as secret keys

**Chosen plaintext (uses an oracle)**: attacker has the capability to choose arbitrary plaintexts to be encrypted and obtain the corresponding ciphertexts. The goal of the attack is to gain some further information which reduces the security of the encryption scheme. In the worst case, a chosen-plaintext attack could reveal the scheme's secret key

**Chosen ciphertext (uses an oracle)**: the cryptanalyst gathers information, at least in part, by choosing a ciphertext and obtaining its decryption under an unknown key

**Adaptive chosen plaintext (uses an oracle):** the cryptanalyst makes a series of interactive queries, choosing subsequent plaintexts based on the information from the previous encryptions

---

## Other attacks

|                                |                                                                                  |
| ------------------------------ | -------------------------------------------------------------------------------- |
| - **type**                     | - **description**                                                                |
| - Cryptoanalysis               | - Any mathematical technique used to break or weaken cryptographic algorithms    |
| - [[Brute-force attack]]       | - Attacker tries all possible keys until the correct one is found                |
| - [[Side‑channel attack]]      | - Exploits physical data (timing, power consumption, EM radiation) from a device |
| - [[Replay attack]]            | - Reuses previously captured valid messages to trick a system                    |
| - [[Man-in-the-Middle (MITM)]] | - Attacker intercepts and potentially alters communications between two parties  |
more attacks discussed next

---
## About brute-force

Modern computers can quickly try exploring all possible keys (~ 106 to 1015 keys/second)
  - depending on hardware

Keys often have a fixed size: the longer the key, the stronger the security — but the slower the performance 

If a key is n bits long, there are 2ⁿ possible keys. The practical limit for current computers is often set around n = 80, but this threshold continues to rise. With 128-bit keys, even at a rate of 1 trillion keys per second, it would take over 10¹⁹ years on average to brute-force the key

---
# Keys and password

similar but different

---
## Why to make a distinction?
- Keys and passwords
- They have similarities but are different
- Both are secret
- Cryptography uses both (for now)
- They have different characteristics
- They are used in different contexts
- They are protected differently
- They have a different impact on security

---
## Password basics

A password is a human-chosen secret used to authenticate a user
It must be
  - Memorable
  - Short enough to type
  - Representable with keyboard characters

---
## Limitations of passwords

Typable = predictable: constrained to the keyboard → lower entropy
Password space = Tⁿ, not Nⁿ (T: keyboard-typable symbols, N>T: all possible symbols)
Vulnerable to
  - Brute force
  - Reuse across platforms
  - Other attacks

---
## Phishing attacks

Phishing is a type of social engineering attack in which an adversary tricks users into revealing sensitive information, such as passwords, credit card numbers, or access credentials 
Characteristics
  - Disguised as legitimate emails, messages, or websites
  - Often creates urgency (e.g., “Your account will be locked!”)
  - Can lead to credential theft, financial loss, or malware installation
Email, SMS, voice calls, fake login pages etc.

other vulnerabilty of passwords 

---
## What is a cryptographic key?

A cryptographic key is a random bit string used in encryption, decryption, and other cryptographic operations
If the string is n bits long, then there are 2ⁿ possible keys

for example:
	0101011000011101…10101011
561D…AB (often represented in hexadecimal)

---
## Key properties

- Machine-generated
- Not typable
- Fixed-length (e.g., 128, 256 bits)
- Stored as binary, not text


Visual Comparison:
Password: S3cr3t!
Key: 9F4b713f8e2a... (256 bits)


---
## Password vs Key – Comparison Table
|   |   |   |
|---|---|---|
|- **feature**|- **password**|- **cryptographic** **key**|
|- chosen by|- human|- machine|
|- typable|- yes – must fit a keyboard|- no – binary data|
|- length|- short (8–20 chars typically)|- long (128–256 bits or more)|
|- purpose|- authentication|- encryption / signing|
|- stored as|- hashed (ideally)|- raw / protected|

---
## Analogy	

password = PIN typed into a keypad

key = the actual metal key unlocking a vault


---
## Combined use
Many systems use passwords to unlock secret keys
Example
  - PGP, Signal, WhatsApp: your password decrypts a stored secret key

---
## Key Derivation
Passwords are often converted into keys using "ad hoc" algorithms
  - Argon2, PBKDF2

Still constrained by password entropy

---
## Why keys are more secure
Higher entropy

Machine-random

Not guessable or typable

---
## Why passwords are still used

Usable by humans

Don’t require special storage

Usability vs security tradeoff

---
## Summary

Passwords: chosen by humans, typable, used for identity
Keys: generated by machines, not typable, used for encryption
They’re not interchangeable — both must be protected appropriately

---

next lesson [[2 CS - Stream Ciphers]]