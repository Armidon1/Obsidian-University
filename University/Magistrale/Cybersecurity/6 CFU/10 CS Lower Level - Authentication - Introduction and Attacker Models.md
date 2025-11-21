# Authentication: An Introduction

**Tags:** #engineering #cybersecurity #authentication #security_design #biometrics

## 1. Definition and Scenario

**Authentication** is distinct from legal identification. In a digital context, we don't necessarily need the full legal identity (Name, Surname, ID number), but we need to establish a link with a previous registration.

- **Alice (User):** Needs to access a service or resource1.
    
- **Bob (Server):** Needs to be sure of Alice’s identity to grant access2.
    
- **Trudy (Attacker):** Tries to impersonate Alice3.
    

### [Technical Logic]

**The logical relationship provided is:**

$$\text{absolute identification} \implies \text{authentication}$$

> [!abstract] Math Analysis
> 
> Meaning: Identification implies authentication, but authentication does not necessarily provide absolute or fully legal identification. It simply verifies that the subject is the same one who registered previously 4.

---

## 2. The Authentication Cycle

The life cycle of authentication involves specific phases. It is crucial to understand that the security of the entire process depends on the **Registration** phase ("ground truth").

`![[SCREEN_SLIDE_AUTH_CYCLE]]`

> [!abstract] Visual Analysis
> 
> What to look at: The cycle showing Registration, Credential Storage, and the Authentication Loop (Attempt -> Verification) 5.
> 
> Meaning: The system validates credentials against trusted data stored during enrollment.

- **Registration / Enrollment:** The subject creates credentials. This is the moment the identity is established6.
    
- **Credential Storage:** The system securely stores data (hashed, encrypted, or in secure hardware)7.
    
- **Verification:** The system validates provided credentials against the stored reference8.
    

> [!failure] Common Pitfall: Storing Passwords
> 
> Never store a password in clear text. The professor emphasizes that even storing encrypted passwords is a weakness.
> 
> If the server is compromised, the decryption key is likely compromised too. The standard is to store Hashes (digests), not encrypted files 9.

---

## 3. Closed World Assumption

This is a fundamental logical approach in security policies (e.g., Firewalls).

### [Logical Definition]

**Here is the exact definition shown in the slides:**

> Presumption that what is not currently known to be true, is false.

- **Closed World Assumption:** Default is **False** (Blocked).
    
    - _Practical implication:_ **Whitelisting** (Allow only known good)10101010.
        
- **Open World Assumption:** Lack of knowledge does not imply falsity.
    
    - _Practical implication:_ **Blacklisting** (Allowed by default, block only known bad)11111111.
        

> [!tip] Exam Focus
> 
> Understanding the difference between Negation as failure (related to Closed World) and Open World assumptions is critical for configuring security policies like firewalls12.

---

## 4. Human vs. Computer Authentication

There is a distinct difference in capabilities:

- **Computers:** Can store high-quality secrets (long random numbers) and perform **cryptographic operations**13.
    
- **Humans:** Cannot perform crypto math in their heads. They rely on **Passwords** (short keys) or tokens14141414.
    

### Authentication Factors

To authenticate a human, we rely on three main categories:

1. **What you know:** Passwords, PINs15.
    
2. **What you have:** Smart cards, tokens, smartphones16.
    
3. **Who you are:** Biometrics (Fingerprint, Retina)17.
    
4. _(Weaker)_ **Where you are:** Network address (prone to spoofing)18.
    

---

## 5. Passwords ("What you know")

Passwords are essentially **short keys** used to derive or unlock longer cryptographic keys.

- **Vulnerabilities:** Easy to guess, susceptible to Phishing and Trojan Horses19.
    
- **Login Trojan:** A fake login window prompts the user to enter credentials, collecting them before passing control to the real OS20.
    

> [!example] Professor's Example: The Mainframe Trick
> 
> The professor recounts a personal anecdote: writing a simple program on a university mainframe that displayed a fake "Login:" prompt.
> 
> Users would type their credentials, the program would save them to a file, display a "Login failed" message, and then exit. The user, thinking they made a typo, would log in again successfully on the real prompt, never realizing their password was stolen 21.

> [!example] Professor's Example: Leslie Lamport
> 
> One-Time Passwords (OTP) were strongly introduced by Leslie Lamport.
> 
> Fun fact: LaTeX is named after him ("Lamport TeX") 22.

---

## 6. Biometrics ("Who you are")

Biometrics link authentication to physical characteristics.

- **Physiological:** Fingerprint, Retina, Face.
    
- **Behavioral:** Voice, Keystroke timing, Handwriting dynamics23.
    

### Accuracy & Issues

Biometrics are probabilistic. We deal with **False Positives** and **False Negatives**.

- **Fingerprint:** Can be faked (gummy fingers), changes with manual labor or age 24.
    
- **Voice:** Affected by colds, noise, or tape recordings25.
    

> [!example] Professor's Example: Bank Signatures
> 
> Banks use special tablets for signatures not just to check the "image" of the signature, but to measure dynamics: speed, pressure, and pen inclination. These behavioral metrics are harder to forge than the visual signature itself 26262626.

---

## 7. Attacker Models

To design a secure system, we must model the adversary. Security is not "one size fits all" 27.

### Attacker Dimensions

- **Motivation:** Financial gain, Espionage, Revenge, Fun 28.
    
- **Resources:** Time, Computational power (botnets), Budget 29.
    
- **Skills:**
    
    - _Script Kiddies:_ Use pre-made tools, low understanding.
        
    - _APT (Advanced Persistent Threats):_ High skill, targeted, long-term 30.
        

### Attack Vectors

- **Spray Phishing:** Sending millions of emails hoping for one click (Law of large numbers) 31.
    
- **Spear Phishing:** Highly targeted, researched attacks against a specific victim. Even experts fall for this 32.
    
- **Replay Attack:** Capturing a valid message and resending it.
    
    - _Note:_ Authentication messages must **always** be different (using nonces/timestamps) to prevent this33333333.
        
- **Insider Threat:** A legitimate user causing damage. They bypass the perimeter and have trust34343434.
    

`![[SCREEN_SLIDE_ATTACKER_MODEL]]`

> [!abstract] Visual Analysis
> 
> What to look at: The diagram contrasting different attacker types (Passive vs Active) .
> 
> Meaning: A Passive attacker monitors/collects metadata. An Active attacker modifies/injects messages 35.

---

## 8. Mapping Threats to Defenses

We design defenses based on specific threats.

|**Threat**|**Defense Strategy**|
|---|---|
|**MITM (Man-in-the-Middle)**|Mutual Authentication, TLS with certificate pinning 36.|
|**Replay Attack**|Nonces, Timestamps, One-Time Passwords (OTP) 37.|
|**Credential Theft**|Multi-Factor Authentication (MFA) 38.|
|**Brute Force**|Rate limiting, Account lockouts, **Salted Hashing** 39.|

### Security Design Principles

- **Networks are untrusted:** Assume traffic is monitored40.
    
- **Endpoints are compromised:** Assume malware exists41.
    
- **Users are fallible:** They will click phishing links42.
    
- **Design Rule:** "Define who, what, how" before designing defenses43.