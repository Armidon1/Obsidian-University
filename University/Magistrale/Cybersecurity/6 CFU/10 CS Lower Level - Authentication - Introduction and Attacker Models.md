# Authentication: Introduction and Attacker Models

## The Concept of Authentication

Authentication is the fundamental process of establishing and verifying identity in a digital system.

In a typical scenario, we have two parties: **Alice** (who needs to prove her identity) and **Bob** (who needs to verify it). Alice typically wants to access a service, information, or a resource. The core problem is ensuring that Alice is truly who she claims to be, preventing **Trudy** (an intruder) from impersonating her.

### Definition vs. Legal Identification

It is crucial to distinguish between **Authentication** and **Legal Identification**.

- **Authentication** is the process of establishing that the subject attempting access is the _same subject_ who originally registered with the system.
    
- **Legal Identification** involves verifying the physical and legal identity of a person (e.g., name, surname, ID number).
    

> [!tip] Important Distinction
> 
> Authentication does not necessarily provide absolute or fully legal identification. You can register with an anonymous email; authentication only proves you are the owner of that anonymous account, not who you are in the real world.
> 
> Systems like SPID (in Italy) bridge this gap by providing both identification and authentication, but standard computer authentication is strictly about matching a user to a registered account.

`![[Insert screen slide showing Authentication definition]]`

> [!img-desc] Visual Analysis
> 
> What to look at: The slide likely defines authentication as validating factors against trusted reference data.
> 
> Significance: The professor emphasizes that absolute identification != authentication. Authentication increases assurance but is not absolute proof of identity.

### One-Way vs. Mutual Authentication

Authentication is directional:

1. **One-Way:** Alice proves her identity to Bob (e.g., logging into a website).
    
2. **Mutual Authentication:** Alice proves her identity to Bob, **AND** Bob proves his identity to Alice.
    

> [!example] Professor's Example: Man-in-the-Middle
> 
> Mutual authentication is critical to prevent Man-in-the-Middle (MITM) attacks. In a MITM scenario, an attacker sits between Alice and Bob. Alice thinks she is talking to Bob, but she is talking to the attacker. If the protocol requires Bob to authenticate himself to Alice (Mutual Auth), the attacker will fail to prove they are Bob, and the attack stops.

---

## The Authentication Lifecycle

The life of an identity in a system follows a structured cycle.

### 1. Registration / Enrollment

This is the initial phase where the subject creates credentials.

- The user provides information (e.g., email, username).
    
- The system verifies this information (e.g., checking control of the email address).
    
- **Note:** The information provided is arbitrary based on the service's needs (it could be a phone number, a nickname, etc.).
    

### 2. Credential Storage

The system must securely store the authentication data.

- **Rule of Thumb:** **Never store a password in plain text.**
    
- Data should be **hashed** or encrypted.
    
- Modern hardware often uses **Secure Modules** to store private keys or sensitive data, preventing even the OS from accessing them directly.
    

> [!tip] Critical Security Rule
> 
> If you find a system where administrators can see your password, that system is fundamentally broken and vulnerable. Passwords should ideally be stored as hashes, not even as encrypted text, because if the server is compromised, the decryption key is likely compromised too.

### 3. The Authentication Loop

This occurs every time access is requested:

- **Authentication Attempt:** Subject presents credentials.
    
- **Verification:** System validates credentials against the stored reference.
    
- **Access Management:** Granting/Denying access.
    

`![[Insert screen slide showing the Authentication Cycle]]`

> [!img-desc] Analysis of the Cycle
> 
> What to look at: The flow from Registration -> Storage -> The recurring Loop of Attempt/Verification.
> 
> Significance: This highlights that authentication relies entirely on the integrity of the data captured during the Registration phase.

---

## The Closed World Assumption

In security and logic, we often operate under specific assumptions regarding knowledge.

- **Closed World Assumption:** The presumption that what is not currently known to be true, is **false**.
    
    - _Context:_ False by default. "If I don't know you, you are not allowed."
        
- **Open World Assumption:** The lack of knowledge does not imply falsity.
    
    - _Context:_ True by default.
        

### Application in Firewalls and Access Control

The professor relates this directly to network security policies:

- **Whitelisting (Closed World):** Block everything by default. Only allow specific IP addresses/Users listed. (More secure).
    
- **Blacklisting (Open World):** Allow everything by default. Only block specific known bad IP addresses.
    

---

## Authenticating Humans vs. Computers

There is a fundamental difference in how we authenticate a person versus a machine.

|**Feature**|**Human Authentication**|**Computer Authentication**|
|---|---|---|
|**Secret Type**|**Passwords** (Short keys, easy to remember)|**Cryptographic Keys** (Long, high entropy, random)|
|**Capability**|Cannot perform crypto operations mentally|Can perform complex crypto operations|
|**Storage**|Memory (brain)|Secure Storage / TEE / Encrypted files|
|**Vulnerability**|Easy to guess, phishing, social engineering|Malware, Key extraction|

> [!example] Public Workstations (Historical Context)
> 
> In the past, "public workstations" posed a unique authentication problem. A user would sit at a terminal without logging in. Today, we almost always login (Authentication), identifying the user to the machine. Even tablets authenticate via PIN or biometrics.

---

## Authentication Factors

To authenticate a human, we rely on three (plus one) main categories of factors:

### 1. What You Know (Knowledge)

- **Examples:** Passwords, PINs, Answers to secret questions.
    
- **Characteristics:** Short secrets (metaphorically "short keys").
    
- **Weakness:** Vulnerable to guessing, sniffing, and phishing.
    

### 2. What You Have (Possession)

- **Examples:** Smart card, Hardware Token, Smartphone (for OTP apps).
    
- **Characteristics:** Requires physical possession of an object.
    

### 3. Who You Are (Inherence / Biometrics)

- **Examples:** Fingerprint, Retina scan, Voice recognition, FaceID.
    
- **Characteristics:** Based on physical or behavioral traits.
    

### 4. Where You Are (Location)

- **Examples:** Network IP address, GPS location.
    
- **Weakness:** Easy to spoof (VPNs, GPS spoofing), so it is considered a "weak" factor usually used to reinforce others.
    

`![[Insert screen slide showing Authentication Factors]]`

> [!img-desc] Visual Analysis
> 
> What to look at: The classification of factors: Know, Have, Are.
> 
> Significance: Multi-Factor Authentication (MFA) is defined as using more than one of these different categories (e.g., Password + Token). Using two passwords is NOT multi-factor.

---

## Biometric Analysis

Biometrics are increasingly popular but have specific challenges regarding **False Positives** (authenticating the wrong person) and **False Negatives** (rejecting the right person).

### Fingerprinting

- **Issues:**
    
    - **Stability:** Not stable over time. Children's fingers grow; manual labor can damage fingerprints.
        
    - **Spoofing:** Fake fingerprints (gelatin/silicone) or, grimly, fingerprints from dead people.
        

### Voice Recognition

- **Issues:**
    
    - Affected by health (cold/flu).
        
    - Background noise.
        
    - **Replay Attacks:** An attacker can record your voice (e.g., from a phone call) and replay it to the system.
        

### Handwritten Signature (Behavioral Biometric)

- **Static Signature:** Just the image (Low security).
    
- **Dynamic Signature (Tablets):** Used heavily in **Banks**.
    
    - It measures **Timing, Pressure, Speed, and Pen Inclination**.
        
    - This is much harder to forge than a static image because the attacker needs to replicate the _motion_, not just the look.
        

> [!example] Bank Enrollment
> 
> When you register a signature at a bank, they ask you to sign multiple times. This is to calculate an "average" profile of your speed and pressure to set a threshold for future verification.

---

## Attacker Models

Understanding **who** is attacking is essential to design the right defense (Scope). Security is not "one size fits all."

### Why Model Attackers?

1. **Resource Focus:** Don't waste money defending against the NSA if your threat is a script kiddie (or vice versa).
    
2. **Protocol Design:** Ensure the protocol mitigates the _specific_ risks relevant to the environment.
    

### Dimensions of an Attacker

1. **Motivation:**
    
    - Financial gain (Cybercrime).
        
    - Espionage (Corporate/Political).
        
    - Disruption/Sabotage.
        
2. **Resources:**
    
    - Computational power (CPU/GPU for cracking).
        
    - Time (Patience for long-term monitoring).
        
    - Budget.
        
3. **Skills:**
    
    - **Script Kiddies:** Low skill, use pre-made tools/scripts found online (e.g., from YouTubers).
        
    - **APTs (Advanced Persistent Threats):** High skill, professional, state-sponsored.
        

### Attack Strategies: Distributed vs. Targeted

- **Distributed Attacks (e.g., Generic Phishing):**
    
    - "Spray and pray." Sending 1 million emails hoping for a 0.1% success rate.
        
    - Easy to spot for humans (generic greetings, "your cloud is blocked").
        
    - Relies on large numbers.
        
- **Targeted Attacks (e.g., Spear Phishing):**
    
    - Focuses on **one specific victim**.
        
    - Attacker studies the victim for months (Passive monitoring).
        
    - **Spear Phishing:** Emails are customized with real references to the victim's job, colleagues, or recent activities.
        
    - **Danger:** Even security experts often fall for well-crafted spear phishing.
        

`![[Insert screen slide showing Attacker Dimensions/Model]]`

> [!img-desc] Attacker Profile
> 
> What to look at: The dimensions: Motivation, Resources, Skills, Access, Persistence.
> 
> Significance: A "Passive, Insider, High Resource" attacker is the most dangerous combination.

---

## Attack Vectors and Defenses

### 1. Replay Attack

- **Mechanism:** The attacker captures a valid authentication message (e.g., a hashed password sent over the network) and "replays" (resends) it later to the server.
    
- **Note:** The attacker doesn't need to decrypt the password; they just need to send the identical encrypted blob.
    
- **Defense:**
    
    - **Nonces:** Random numbers used only once.
        
    - **Timestamps:** Message is only valid for a few seconds.
        
    - **OTPs (One-Time Passwords):** The password itself changes every time.
        

### 2. Man-in-the-Middle (MITM)

- **Mechanism:** Intercepting and modifying traffic. Often done via Malware acting as a proxy.
    
- **Defense:** **Mutual Authentication** (Server authenticates to Client, Client to Server) and TLS (Certificates).
    

### 3. Credential Theft (Keyloggers/Phishing)

- **Mechanism:** Malware recording keystrokes or fake login pages.
    
- **Defense:** **Multi-Factor Authentication (MFA)**. Even if they have the password, they don't have the token/phone.
    

### 4. Brute Force

- **Mechanism:** Guessing passwords repeatedly.
    
- **Defense:**
    
    - **Rate Limiting:** Block IP after N failed attempts.
        
    - **Salted Hashing:** Prevents the use of **Rainbow Tables** (pre-computed hash tables) by adding random data ("salt") to the password before hashing.
        

### 5. Insider Threat

- **Mechanism:** A legitimate user abusing privileges or being tricked (Social Engineering).
    
- **Danger:** High access level, trusted by the network.
    

> [!tip] Security Design Summary
> 
> "Who, What, How": Before designing a system, define Who you are defending against, What assets are at risk, and How the attacker might operate. Security is a combination of Protocol Soundness, Endpoint Security, and Human Factor Resilience.

---

the [[Authentication]] is the process to verify if you are really the one that you claim to be. ovviamente questa cosa si può fare solo dopo la fase di registrazione 
absolute [[Authentication]] is the spid

nella slide closed worklds assumpptions ha fatto un paraagone con la blakclist e whitelist dei firewall 

il professore nella slide - **A particular case: the closed environment** ha aggiunto di un caso della realtà con internet

never store a password, not even the encrypted version: why im weak? when a server is compromised, so the key for doing the encryption and decryption is also comprimised. So a 2 ways function, like encryption and decryption, are not used. What about the digest? we will see it later. what happens if we manage many password (and ignoring the danger)? at least for each password is needed a different key, so if one key is compromised, we have just one password compromised.

il prof ha fatto vedere anche un trojan password simpatico

