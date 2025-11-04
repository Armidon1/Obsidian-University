See the italian and enriched version: [[EMAIL SECURITY]]
# Email Security

**Cyber Intelligence and Information Security (CIS Sapienza)**  
**Lecturer:** Leonardo Querzoni  
📧 [querzoni@diag.uniroma1.it](mailto:querzoni@diag.uniroma1.it)

---

## Overview

### The Internet E-Mail System

- **Architecture and basic functioning**
    
- **Protocols:** SMTP, POP, IMAP
    
- **Extensions:** MIME
    
- **Email threats**
    
- **Infrastructure security:** SPF, DKIM, ARC, DMARC
    
- **End-to-end security:** PGP, S/MIME
    

---

## The Email System
[[EMAIL SECURITY]]
E-mail is a method of exchanging digital messages from an author to one or more recipients, operating across the Internet or intranet.

- One of the **oldest Internet services** (since 1971)
    
- **First message:** Sent by _Ray Tomlinson_ using `user@domain` addressing
    
- Based on a **store-and-forward model** — servers accept, forward, store, and deliver messages
    
- Users don’t need to be online simultaneously
    
- See **RFC 5598** for details
    
All the internet is not based on standards, but in practical yes, and the RFC contains all kind of protocols that internet uses. In RFC 5598 we can find all the information about all basic email system. This RFC doesn’t contain other useful information. Those designs are simple but very clever and works greatly.

---

## Internet E-Mail Architecture
![[Pasted image 20251028131532.png]]
Defined by **RFC 5598 (2009)**.

**Key Components:**

- **[[MUA]] (Message User Agent)** — User’s email client
    
- **[[MSA]] (Mail Submission Agent)** — Accepts mail from MUA, checks format
    
- **[[MTA]] (Mail Transfer Agent)** — Transfers mail between servers
    
- **[[MDA]] (Mail Delivery Agent)** — Delivers mail to local mailbox
    
- **[[MS]] (Message Store)** — Stores messages
    
- **Protocols:** [[SMTP]], POP, IMAP
    
The MUA is the client part of the protocol takes in charge the message, checks if syntax is correct and if everything is okay, it takes simply in charge the messages and sends to his email server. The MUA is outside the message handling system (MHS). This one can be a single piece of software. The MTA is the core of the MHS: does basically everything. This is a distributed system. The MTA needs only to understand which server needs to contact to send the message. This is possible thanks the Ip-routing system. As we can see, we have a SMTP protocol: Simple mail transfer protocol.  We can see also “Local”, which means there are no predefined protocols, and then POP/IMAP (manly IMAP) used to access to the local messages stored.

---

## Components Explained

### [[MUA]] (Message User Agent)

Used by end-users to send, receive, and manage emails.

### [[MSA]] (Mail Submission Agent)

- Receives messages from MUA.
    
- Works with MTA for delivery.
    
- Ensures message format compliance.
    

### [[MTA]] (Mail Transfer Agent)

- Transfers messages using **SMTP**.
    
- Acts as both client and server.
    

### [[MDA]] (Mail Delivery Agent)

- Handles final delivery to recipient’s mailbox.
    
- Stores message locally.
    

---

## Email Exchange

**Protocol:** [[SMTP]] (RFC 821 → RFC 5321)

- **Envelope:** Contains delivery parameters, separate from header/body.
    
- **Address format:** `user@domain`
    
    - `user`: local part
        
    - `domain`: fully qualified domain name (FQDN)
        
The domain has exactly the struct needed to find the destination. The MTA if checks that I AM the domain, if is true, then the destination is LOCAL, else i have to send out of here. Tipycally we have only 2 steps when i send an email. But happens that we have more steps when an industry has an heiracly structure and happens that is neened a central destination that does as a gateway between the sender and the reciever. The domain is foundamental in this case. In the end we will talk about the DNS.

---

## Message Format

Defined by **RFC 5322** and extended by **[[MIME]] (RFC 2045–2049)**.

### Structure:

- **Header:** Structured fields (From, To, CC, Subject, Date, etc.). The Header are all the meta-data and the body is basically a long piece of text.
    
- **Body:** Main content, plain text or rich format.
    
- Header and body are separated by a **blank line**.
    

---

## Email Headers

### Structure

Each field = _Name_ + _Value_, separated by a colon (`:`).

- Fields can be multi-line (must start continuation lines with space or tab).
    
- Restricted to **7-bit ASCII** (non-ASCII encoded via MIME).
    

### Identifiers

- **Message-ID:** Globally unique identifier (`<1234@example.com>`). The message-id is insert in the MTA of the sender. Chiedere a chat qualche problematica dovuta alla risposta
    
- **ENVID:** Envelope identifier for message tracking (RFC 3885, RFC 3464)
    

### Mandatory Fields

- `From:` Sender’s address
    
- `To:` Recipient(s)
    
- `Date:` Sent timestamp (RFC 5322 format)
    
- `Message-ID:` Unique identifier
    
- `Subject:` Summary of message content
    

### Optional Fields

- `Cc:` Carbon copy
    
- `Bcc:` Blind carbon copy (hidden recipients)
    
- `Reply-To:` Alternate reply address
    
- `In-Reply-To:` Message ID of referenced email
    
- `References:` For threading conversation chains
    
- `Sender:` When different from `From`
    
- `Return-Path:` For bounce messages
    
- `Received:` Added by each server along the route

See the [[EMAIL - Difference between receivedFrom and ReturnPath||difference between Received and Return to Path]]

## Example of header

From: Michela Cellamare <michela.cellamare@uniroma1.it> Date: ...

As we can see, an header contains more lines which means value: content.

There are also optional headers needed for other providers. If the provider is google and sees an outlook header, then google will ignore them.

All the values in the header are restricted only with 7-bit.

The headers can contain a chain of Received if the email jumps between servers. Each time does a jump, another line Received is created. This history is extremely important to understand where this email has been. Every time arrives in a server, may happen that this server changes the content of this email.

---

## Email Transmission

- **MUA → MSA:** Uses SMTP for sending
    
- **MUA → Server:** Uses POP (offline) or IMAP (online) for receiving
    
- **Examples:** Microsoft Exchange, Lotus Notes use proprietary protocols

IMAP is used fot online mail reading. Nowadays is used only IMAP.

---

## Operation Overview
![[Pasted image 20251028131610.png]]

1. User composes email (MUA). Alice composes a message using her MUA; she enters the e-mail address of her correspondent, and hits the "send" butto
    
2. MUA sends via Submission Protocol (SMTP variant).  The MUA formats the message in email format and uses the Submission Protocol (variant of SMTP, see RFC 6409) to send the message to the local MSA
    
3. MSA resolves domain → finds destination MTA via DNS MX record. The MSA looks at the destination address provided in the SMTP protocol and resolves a domain name to determine the fully qualified domain name of the mail exchange server
    
4. MTA sends to remote MTA (may relay through several servers). he DNS server for the b.org domain responds with any MX records listing the mail exchange servers for that domain, in this case mx.b.org, a MTA server run by Bob's ISP
    
5. MDA stores message in recipient’s mailbox. smtp.a.org sends the message to mx.b.org using SMTP
	1. this server may need to forward the message to other MTAs before the message reaches the final message delivery agent (MDA), which delivers it to the mailbox of Bob
    
6. Recipient retrieves mail using POP3 or IMAP4. Bob presses the "get mail" button in his MUA, which picks up the message using either the Post Office Protocol (POP3) or the Internet Message Access Protocol (IMAP4)
    

---

## SMTP and ESMTP

- **SMTP:** Simple Mail Transfer Protocol (RFC 821 → 5321)
    
- **ESMTP:** Extended version (RFC 5321)
    
    - Introduced new commands (e.g., `EHLO`, `STARTTLS`, `AUTH`)
        

### Common ESMTP Extensions

|Command|Purpose|RFC|
|---|---|---|
|8BITMIME|8-bit data transmission|6152|
|AUTH|Authenticated SMTP|4954|
|STARTTLS|TLS encryption|3207|
|SIZE|Message size declaration|1870|
|DSN|Delivery status notifications|3461|
|PIPELINING|Command pipelining|2920|
## Sample SMTP Interaction 
![[Pasted image 20251028145421.png]]![[Pasted image 20251028145437.png]]
## Other ESMTP Commands
▪ 8BITMIME — 8 bit data transmission, RFC 6152
▪ ATRN — Authenticated TURN for On-Demand Mail Relay, RFC 2645
▪ AUTH — Authenticated SMTP, RFC 4954
▪ CHUNKING — Chunking, RFC 3030
▪ DSN — Delivery status notification, RFC 3461 (See Variable envelope return path)
▪ ETRN — Extended version of remote message queue starting command TURN, RFC 1985
▪ HELP — Supply helpful information, RFC 821
▪ PIPELINING — Command pipelining, RFC 2920
▪ SIZE — Message size declaration, RFC 1870
▪ STARTTLS — Transport layer security, RFC 3207 (2002)
▪ SMTPUTF8 — Allow UTF-8 encoding in mailbox names and header fields, RFC 6531
▪ UTF8SMTP — Allow UTF-8 encoding in mailbox names and header fields, RFC 5336
(deprecated)
---

## MIME – Multipurpose Internet Mail Extensions

Extends email to support:

- Non-ASCII text
    
- Attachments (images, audio, video, etc.)
    
- Multi-part messages
    
- Complex content types
    

### Key RFCs

RFC 822, 2045, 2046, 2047, 2048, 2049

### MIME Features

- Character set support (UTF-8, ISO-8859-1, etc.)
    
- Content type labeling
    
- Binary data encoding (Base64)
    
- Compound documents
    

### Common MIME Types
![[Pasted image 20251028150803.png]]

| File  | MIME Type       | Description     |
| ----- | --------------- | --------------- |
| .txt  | text/plain      | Plain text      |
| .html | text/html       | HTML document   |
| .jpg  | image/jpeg      | JPEG image      |
| .mp3  | audio/mpeg      | MP3 audio       |
| .zip  | application/zip | Compressed file |
|       |                 |                 |
## Content-transfering Encoding
![[Pasted image 20251028150826.png]]
## MIME Scheme
![[Pasted image 20251028150005.png]]
## MIME headers
![[Pasted image 20251028150024.png]]
---

## Encodings

### Base64
![[Pasted image 20251028150317.png]]![[Pasted image 20251028150408.png]]

- Converts binary → ASCII text for transport.
    
- Groups 3 bytes into 4 Base64 characters.
    
- Uses padding (`=`) when needed.
    

### Quoted-Printable
![[Pasted image 20251028150434.png]]
- Encodes 8-bit characters using `=` followed by two hex digits.
    
- Keeps text mostly readable.
    

---

## Multipart Messages

- **Mixed:** Different attachments
    
- **Digest:** Multiple text parts
    
- **Alternative:** Text + HTML versions
    
- **Message:** Encapsulated email
    

## MIME types/subtypes
![[Pasted image 20251028150955.png]]![[Pasted image 20251028151013.png]]

---

## Plain Text vs HTML

- HTML emails can include links, images, and styles.
    
- Usually sent with a plain text fallback.
    
- Header: `Content-Type: text/html`
    

---

## Subaddressing

### Local (“+”) Subaddressing

`querzoni+mastercourses@diag.uniroma1.it`  
→ Alias for `querzoni@diag.uniroma1.it` (RFC 5233)

### Domain Subaddressing

`mastercourses@querzoni.diag.uniroma1.it`  
→ Alias for `querzoni@diag.uniroma1.it`

---
# Email Security
## Email Example
![[Pasted image 20251028151405.png]]
## Email Security Challenges

- Spam
    
- Phishing
    
- Malware / Ransomware
    
- Spoofing
    
- Lack of traceability
    
- Data leakage
    
- MITM attacks
    
- Business Email Compromise (BEC)
    
- Email bombing
    

## Simple Spoofing Examples
### Example 1
![[Pasted image 20251028151425.png]]![[Pasted image 20251028151436.png]]![[Pasted image 20251028151500.png]]
### Example 2
![[Pasted image 20251028151526.png]]![[Pasted image 20251028151536.png]]![[Pasted image 20251028151544.png]]![[Pasted image 20251028151559.png]]
### Example 3
![[Pasted image 20251028151619.png]]


---

## Sender Authentication

|Protocol|Function|RFC|
|---|---|---|
|SPF|Validates sending mail servers|4408|
|DKIM|Cryptographically signs emails|4871|
|DMARC|Combines SPF + DKIM, defines policies|7489|
|ARC|Preserves authentication through intermediaries|—|

---

## SPF – Sender Policy Framework

- Defines authorized mail servers via **DNS TXT records**
    
- Validates sender’s IP address
    
- Example record:
    

```
example.net TXT "v=spf1 mx a:pluto.example.net include:aspmx.googlemail.com -all"
```
![[Pasted image 20251028162915.png]]
here `pluto.example.net` will be authorised to send email on behalf of `example.net`

- When an email is sent from the domain, the receiving mail server queries the DNS for the domain's SPF record to verify if the IP address of the sending server is listed in the SPF record.
	- **Pass**: If the sending server’s IP matches one of the authorized IPs in the Specify record, the email passes the SPF check.
	- **Fail**: If the sending IP is not listed, the email fails the SPF check. The receiving server can then choose to reject, ag, or accept the message based on local policy.

```
<XXXX.YYYY@gmail.com>: host gmail-smtp-in.l.google.com[173.194.78.26]
said: 550-5.7.1 [aa.bb.cc.dd] The IP you're using to send mail is not
authorized to 550-5.7.1 send email directly to our servers. Please use the SMTP relay at your 550-5.7.1 service provider instead. Learn more at 550 5.7.1 http://support.google.com/mail/bin/answer.py?answer=10336 fl4si3665795wib.12 - gsmtp (in reply to end of DATA command)
```

## Example to check
![[Pasted image 20251028163320.png]]![[Pasted image 20251028163346.png]]

See more on [[SPF]]

### Limitations

- Breaks on forwarding or mailing lists
    
- No content integrity
    
- Misconfiguration risks
    
- No body protection
    
SPF ignores the body, he just checks if the server which sends an email is authorised to send email to me. In this case we can easily block those people who creates his own server.

See also [[SPF#Perché le mailing list rompono SPF (concetto chiave)|Why the mailing list broke SPF]]


---

# DKIM 2

DomainKeys Identified Mail (DKIM), as specified in RFC 4871, is a protocol that allows a signing domain to claim responsibility for an email message by affixing a cryptographic signature3. This signature is attached to the email as a header.

Recipients of the message (or their mail servers) can verify this signature4. They do this by querying the DNS (Domain Name System) of the signing domain to get the public key required for verification5.

DKIM is a core component of modern email authentication, working alongside SPF and DMARC to combat email spoofing and phishing.

## **What DKIM Guarantees:** 

- **Email content integrity:** 7 It ensures that parts of the email (like the body and specific headers) have not been tampered with after being signed.
    
- **Domain authentication:** 8 It verifies that the domain listed in the signature is the one that actually signed the message.
    
- **Non-repudiation:** 9 The signer cannot easily deny having sent the message, as the signature can only be created with their private key.
    

## Possible DKIM Deployment 
![[Pasted image 20251028184726.png]]
Here is a transcription and enrichment of the provided PDF content on email security.


The provided diagram illustrates the flow of a DKIM-signed email:

1. **Mail Origination Network:** 11
    
    - A user (MUA - Mail User Agent) 12sends a message via SMTP1313.
        
    - It goes to the Mail Submission Agent (MSA) 14, which passes it to the **Signer**15.
        
    - The Signer uses a private key to generate the signature and attaches it to the email.
        
    - The message is then sent to the outbound Mail Transfer Agent (MTA)1616.
        
2. **Mail Delivery Network:** 17
    
    - The email travels via SMTP 18181818to the recipient's MTA, which passes it to the Mail Delivery Agent (MDA)19.
        
    - The **Verifier** 20 component of the MDA sees the `DKIM-Signature` header.
        
    - It performs a **DNS Public key query/response** 21to the sender's DNS 22 to fetch the public key.
        
    - It uses this key to validate the signature.
        
    - If valid, the message is delivered to the recipient's MUA 23(e.g., via POP or IMAP 24).
        

How Does DKIM Work 25

1. Generating the Signature (Signing Process) 26262626

When an email is sent, the sender's mail server (or a signing service) generates a cryptographic signature27. This signature is based on specific parts of the message, such as the body and selected headers (e.g., `From`, `Subject`, `Date`)28.

- This signature is created using a **private key** that is controlled only by the sending domain29.
    
- The signature is then added to the email as a new header, the **`DKIM-Signature` header**30.
    

This header contains several key-value pairs (tags), including: 31

- **`a=`:** The hashing algorithm used (e.g., `rsa-sha256`)32323232.
    
- **`d=`:** The domain that is taking responsibility for the email33333333.
    
- **`s=`:** The "selector," a name used to find the specific public key in DNS34.
    
- **`h=`:** The list of email headers that were included in the signature calculation35353535.
    
- **`bh=`:** The hash of the message body36.
    
- **`b=`:** The actual signature itself (a base64-encoded value)37373737.
    

2. Public Key Published in DNS 38

The sending domain publishes the public key that corresponds to the private key used for signing39.

- This is published in the Domain Name System (DNS) as a **TXT record**40.
    
- The public key is used by recipients to **verify the signature's authenticity**41.
    
- The DNS record's location is specific, combining the selector (`s=`) and the domain (`d=`). For example: `google._domainkey.uniroma1.it`42.
    
- The selector allows a domain to have multiple public keys, which is useful for key rotation or for allowing third-party services to send on the domain's behalf43.
    

Here is an example query for a DKIM public key: 44

> dig +noall +answer google._domainkey.uniroma1.it txt

google._domainkey.uniroma1.it. 21600 IN TXT "v=DKIM1; k=rsa; p=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzMa8wGDtu7DVjVP1JwVzMym/KktdVSBhvtMbgpolQTWqKxRHejICsUvvFv6WGP7kKQnVA5" "2JtFU9LVGvTfkNF5J/x/9wU1BSQMCwGc4IXNdgA5fcn/49fV+YY1RFY44PhoTSWTQnKp7axDRF03Uo05uFXS100nNo0Gd/" "tnDRG538tnM8VzZIF+jjS76GkV/iZT2tcDSBMsWjZTR" "tk7eG/GDVS8pbD14CX/bf7RTf1t3sTiwcp3YUn5T66ioCmc7PIu5CCKfTcW7i7E246Ef4hz+6CySyNRxipnrK6BrXGoraod5U66K6boXVWojDKHRflvdoeQ49hW8N5PHFqJKebwIDAQAB" 

3. Verification Process 46

When a receiving mail server gets an email, it performs the following steps:

- It looks at the `DKIM-Signature` header to find the signing domain (`d=`) and the selector (`s=`)47.
    
- It queries the DNS for that domain and selector to retrieve the public key48.
    
- The server then re-calculates the hash of the received message's content (using the headers listed in `h=` and the body)49.
    
- It uses the public key to decrypt the signature (`b=`) and compares the result with the hash it just calculated50.
    

If the signature matches, it confirms two things: 51

1. **Message Integrity:** The signed parts of the email have not been altered in transit52.
    
2. **Authenticity:** The email was indeed authorized by the domain listed in the `d=` tag53.
    

3. Passing or Failing the DKIM Check 54

- **Pass:** If the signature is valid, the message is authenticated55. The receiving server knows the message came from an authorized source and wasn't tampered with56.
    
- **Fail:** The message fails the DKIM check if the signature doesn't match57. This can happen for two main reasons:
    
    1. The content or signed headers were altered during transit.
        
    2. The public key in the DNS doesn't correspond to the private key that created the signature (it's a forgery).
        
- **Action:** A DKIM fail alone doesn't usually cause an email to be rejected. The final action (like rejection or sending to spam) typically depends on other factors, most notably the domain's **DMARC policy**58.
    

Selectors 59

Selectors are used to subdivide the key namespace, allowing for multiple concurrent public keys per signing domain60.

- For example, selectors could indicate office locations, signing dates, or even individual users61.
    
- In modern practice, selectors are most often used to delegate signing capability to third-party providers.
    

**Common Use Cases for Selectors:** 62

- **Delegation:** A domain can allow a partner (like an advertising provider or marketing platform) to send emails on its behalf for a specific duration63. The partner gets its own selector and key, which the domain owner can easily revoke without affecting other mail streams.
    
- **Remote Users:** Allowing frequent travelers to send messages locally without needing to connect to a specific, centralized Mail Submission Agent (MSA)64.
    
- **Forwarding Domains:** Used by "affinity" domains (e.g., college alumni associations) that forward incoming mail but don't operate an MSA for outgoing mail65.
    

DKIM and SPF 66

**How does DKIM compare to SPF?** 67

- **SPF (Sender Policy Framework):** Authenticates the _sending server_. It checks if the server's IP address is listed in the domain's SPF record as an authorized sender68. It validates _where_ the email came from.
    
- **DKIM:** Authenticates the _email content_. It verifies a digital signature against a public key in DNS69. It validates _what_ was sent and _who_ signed it.
    

**Limitations of DKIM:** 70

- **Doesn't authenticate the visible "From" address:** 71 This is a critical limitation. DKIM only verifies the authenticity of the domain in the `d=` tag of its signature. An attacker can put `ceo@yourcompany.com` in the _visible_ `From:` header but sign the message with their own malicious domain (`d=evil-domain.com`). The DKIM check will _pass_ (for `evil-domain.com`), but the email is still a spoof. This is solved by DMARC's "alignment" check.
    
- **Email forwarding can break DKIM:** 72If a forwarding server alters the content, even by adding a small disclaimer or footer, the DKIM signature will break and the check will fail73.
    
- **No encryption:** DKIM provides authenticity and integrity, but it does **not** provide encryption or privacy74. The message content is still sent in plaintext.
    

Canonicalization 75

Email servers and relays often make minor modifications to an email in transit, which can inadvertently invalidate a DKIM signature76.

To account for this, DKIM uses **canonicalization algorithms** to create a "normalized" version of the headers and body before signing and verifying.

- Headers are subjected to a canonicalization algorithm77.
    
- Bodies are also subjected to a canonicalization algorithm78.
    
- The choices for header and body are independent (e.g., `c=relaxed/simple`)79.
    

The two types are:

- **`simple` (strict):** 80 Tolerates almost no changes. Even a change in whitespace can break the signature.
    
- **`relaxed` (tolerating):** 81 More robust. It allows for common modifications, like changes in whitespace or header case. Using `relaxed/relaxed` is the common practice to help signatures survive forwarding.
    

DKIM Example Header Tags 82

Here is a breakdown of the tags found in a `DKIM-Signature` header:

- `v=` DKIM version 83
    
- `a=` Hashing/signing algorithm (e.g., `rsa-sha256`) 84
    
- `d=` The signing domain 85
    
- `s=` The selector used to find the key 86
    
- `c=` The canonicalization algorithm(s) for header/body (e.g., `relaxed/relaxed`) 87
    
- `h=` A list of headers included in the signature 88
    
- `bh=` The hash of the canonicalized body 89
    
- `b=` The signature itself 90
    
- `t=` Signing timestamp (seconds since 1/1/1970) 91
    
- `x=` Expiration time for the signature 92
    
- `i=` The signing identity (less common) 93
    

---

## 🛡️ DMARC 

DMARC (Domain-based Message Authentication, Reporting, and Conformance) is a technical standard (RFC 7489) that acts as the policy layer for email authentication95. It helps protect domains from being used in spam, spoofing, and phishing attacks96.

DMARC essentially **"puts together SPF and DKIM"**. It allows a domain owner to:

- Publish its email authentication practices (i.e., "we use SPF and DKIM")98.
    
- State what actions receiving mail servers should take if a message fails these authentication checks.
    
- Enable reporting, allowing receivers to send data back to the domain owner about messages claiming to be from their domain.
    

How Does DMARC Work? 101

1. Publish a Policy 102

A domain administrator publishes a DMARC policy in their domain's DNS records103.

- This is a specially-formatted **DNS TXT record**104.
    
- It is placed at a specific hostname: `_dmarc.yourdomain.com`105.
    

DMARC Record Example: 

> dig +noall +answer _dmarc.uniroma1.it txt

_dmarc.uniroma1.it. 21600 IN TXT "v=DMARC1; p=reject; pct=10; rua=mailto:lxoyu6mk@ag.eu.dmarcadvisor.com, mailto:dmarc-ar@uniroma1.it; ruf=mailto:lxoyu6mk@fr.eu.dmarcadvisor.com, mailto:dmarc-f@uniroma1.it;" 1
**Key Tags:**

- `v=DMARC1`: Specifies the DMARC version108.
    
- `p=reject`: Specifies the **policy** to apply to failing messages109.
    
- `pct=10`: The **percentage** of mail to which the policy should be applied110. This `pct=10` is a safety measure, allowing domains to gradually roll out a strict policy (applying `reject` to only 10% of failures) while monitoring reports.
    
- `rua=mailto:...`: The mailbox to which **aggregate reports** should be sent111.
    
- `ruf=mailto:...`: The mailbox to which **forensic reports** should be sent112.
    

## **DMARC Policies:** 

- `p=none`: The "monitoring" policy. The receiver takes no action but still sends reports114.
    
- `p=quarantine`: The receiver should accept the mail but place it somewhere other than the inbox (e.g., the spam folder)115.
    
- `p=reject`: The receiver should reject the message outright116.
    

2. Check Authentication and Alignment 117117117

When an inbound mail server receives an email, it looks up the DMARC policy for the domain found in the message's **"From" (RFC 5322) header**118.

The server then checks three key factors: 119

1. Does the message's **DKIM signature validate**? 120
    
2. Did the message come from an IP address allowed by the sending domain's **SPF records**? 121
    
3. Do the headers show proper **"domain alignment"**? 122
    

Domain Alignment: 123

This is the most important concept in DMARC. It solves the limitation of

DKIM/SPF by matching the domain in the visible From header with the domains used in the SPF and DKIM checks124.

- **SPF Alignment:** The `From` domain must match the `Return-Path` domain (used for the SPF check)125.
    
- **DKIM Alignment:** The `From` domain must match the `d=` domain in the DKIM signature126.
    

A message passes DMARC if it passes _either_ aligned SPF _or_ aligned DKIM.

3. Apply Policy 127

With the alignment and authentication results, the receiving server is ready to apply the sending domain's DMARC policy (`none`, `quarantine`, or `reject`) to decide the message's fate128.

4. Send Reports 129

After determining the message's disposition, the receiving mail server will report the outcome to the sending domain owner using the addresses specified in the `rua` and `ruf` tags130.

**DMARC Reports:** 131

- **Aggregate reports (`rua`):** 132These are XML documents containing statistical data about messages claiming to be from a domain133. They include IP addresses, authentication results (SPF, DKIM, DMARC), and message dispositions134. They are machine-readable and essential for monitoring135.
    
- **Forensic reports (`ruf`):** 136These are individual copies of messages that failed authentication, enclosed in a special format137. They are useful for troubleshooting and identifying malicious attacks138. Due to privacy concerns (as they contain message content), many receivers do not send forensic reports.
    

DMARC Check Outcomes 139

The results of these checks are often added to the email's headers in the `Authentication-Results` header.

Example Header:

Authentication-Results: mx.google.com;

`dkim=pass header.i=@diag.uniromal.it header.s=google header.b=gx0VIcD5;` 140`spf=pass (google.com: domain of querzoni@diag.uniromal.it designates 209.85.220.41 as permitted sender) smtp.mailfrom=querzoni@diag.uniroma1.it;` 141`dmarc=pass (p=NONE sp=NONE dis=NONE) header.from=diag.uniroma1.it;` 142

This shows that the message passed DKIM (for `diag.uniromal.it`), passed SPF (for `diag.uniromal.it`), and therefore passed DMARC (with alignment to the `header.from=diag.uniroma1.it`).

DMARC Limitations 143143143143

The biggest problem with DMARC is that strict policies (`p=reject`) can block **legitimate messages** that go through indirect mailflows, such as mailing lists or forwarding services144144144144.

This happens because intermediaries often break both SPF and DKIM:

- **Forwarding breaks SPF:** 145The intermediary sends the message from a **new IP address** that is not in the original sender's SPF record, causing SPF to fail146.
    
- **Forwarders break DKIM:** 147Intermediaries often **alter the message contents**, which invalidates the DKIM signature148. Common changes include:
    
    - Adding disclaimers and footers 149
        
    - Adding tags to the subject line (e.g., `Subject: [List] ...`) 150150150150
        
    - Showing virus scan results 151
        
    - Removing attachments 152
        

This problem led to the development of ARC.

---

## 🔗 AUTHENTICATED RECEIVED CHAIN (ARC) 

ARC helps preserve the email authentication status when a message passes through multiple intermediaries or forwarding services154.

- **Preserves Authentication:** If an email passes SPF, DKIM, and DMARC at the _original_ source, ARC ensures this "pass" status can be carried forward to the final recipient155.
    
- **Accountability:** Each intermediary in the email flow adds its own ARC authentication results, creating a verifiable chain of who handled the message and whether they altered it156.
    
- **Improved Deliverability:** ARC helps legitimate emails sent through mailing lists or forwarders pass DMARC checks that they would otherwise fail157.
    
- **Complements DMARC:** ARC does not replace DMARC; it works alongside it to preserve the authentication chain158.
    

**What ARC Does Not Do:** 159

- It does not say anything about the **"trustworthiness"** of the sender or intermediaries160.
    
- It says nothing about the **message contents**161.
    
- Intermediaries might still inject bad content 162or remove ARC headers163.
    

## ARC Headers 164

ARC introduces three new header fields:

1. **`ARC-Authentication-Results` (AAR):** An archived copy of the `Authentication-Results:` header. It records the authentication check results (SPF, DKIM) as seen by the intermediary165.
    
2. **`ARC-Message-Signature` (AMS):** A DKIM-style signature of the _entire message_ (except the `ARC-Seal` headers)166. This preserves the integrity of the message as it passed through that specific intermediary167.
    
3. **`ARC-Seal` (AS):** A DKIM-style cryptographic signature that verifies the authenticity of the _ARC headers_ up to that point, confirming no one has tampered with the previous ARC headers in the chain168.
    

The `ARC-Seal:` header contains several fields: 169

- `i=` A sequence number for the ARC header set (e.g., `i=1` for the first hop, `i=2` for the second)170.
    
- `a=/d=/s=` Fields that match corresponding DKIM tags for the intermediary's signature171. (Intermediaries can use their existing DKIM keys for ARC 172).
    
- `cv=` Indicates whether the ARC chain validated (`pass` or `fail`) as received by this intermediary173.
    
- `b=` The signature of all ARC headers174.
    

### ARC Signing and Verification

**Signing (by an intermediary):** 175An intermediary (like a mailing list) only needs to add a new set of ARC headers if it makes changes that might break DMARC checks176.

1. It copies the current `Authentication-Results:` content into a new `ARC-Authentication-Results:` (AAR) header and prefixes it to the message177.
    
2. It calculates the `ARC-Message-Signature:` (AMS) for the message (including the new AAR) and prefixes it178.
    
3. It calculates the `ARC-Seal:` (AS) for the ARC headers and prefixes it179.
    

The `i=` sequence tag is crucial as it groups the header sets (AAR, AMS, AS) and orders them correctly, regardless of the order they were inserted180.

**Verification (by the final recipient):** 181

1. **Verify the `ARC-Seal`:** Check the cryptographic signature in the seal182.
    
2. **Verify the `ARC-Message-Signature`:** Check the signature of the message content183.
    
3. **Check Authentication Results:** Review the `ARC-Authentication-Results` to see the original email's authentication status (SPF, DKIM)184.
    
4. **Evaluate the Chain:** Continue verifying the chain of ARC headers (`i=2`, `i=1`, etc.) to maintain the chain's integrity185.
    

If the final DMARC check fails, but a _valid_ ARC chain exists that shows an _original_ DMARC pass, the receiving server can (at its discretion) trust the ARC result and deliver the message.

---

## 🔒 END-TO-END SECURITY 

The protocols discussed so far ([[SPF]], [[DKIM]], [[DMARC]], [[ARC]]) focus on _authentication_—proving a sender is who they say they are. They do not provide _[[Confidentiality]]_.

For a fully-trustable email system, we would like the following guarantees: 187

- **Confidentiality of message content** 188 (encryption)
    
- **Authentication of message sender** 189
    
- **Message integrity** 190
    
- **Sender non-repudiation** 191
    

This level of security is achieved using end-to-end encryption standards like PGP and S/MIME.

Securing E-mail by PGP 192

**Pretty Good Privacy (PGP)** is a standard created by Phil Zimmermann in 1991193.

- It was created to empower individuals to "take their privacy into their own hands"194.
    
- It has been widely used since the 90s 195and integrates the best available crypto algorithms into a single program196.
    
- While the original PGP is now owned by Symantec 197, the **OpenPGP** standard (RFC 4880) 198is open, with popular implementations like **Gnu Privacy Guard (GnuPG)**199.
    

PGP provides two main services, which can be used separately or together:

1. Authentication (Digital Signature)
    
2. Confidentiality (Encryption)
    

PGP Authentication (Authentication Only) 200

This process provides message integrity and sender authentication.

1. **Sender:** Creates a message (M)201201201201.
    
2. **Hash:** Calculates a hash of the message (e.g., SHA-1) H(M)202202202202.
    
3. **Sign:** Encrypts (signs) the hash using the sender's **private key ($PR_a$)**.
    
4. **Append:** Attaches the signed hash to the original (plaintext) message204204204204.
    
5. **Receiver:** Receives the message and the signed hash.
    
6. **Decrypt Hash:** Uses the sender's **public key ($PU_a$)** to decrypt the signed hash and recover the original H(M)205205205205.
    
7. **Verify:** The receiver independently calculates the hash of the message they received206206206206.
    
8. **Compare:** If the two hashes match, the receiver knows the message came from the sender (authentication) and was not altered (integrity)207207207207.
    

PGP Confidentiality (Confidentiality Only) 208

This process ensures only the intended recipient can read the message. It uses a hybrid encryption model.

1. **Sender:** Creates a message (M)209.
    
2. **Session Key:** Generates a random, one-time **session key ($K_s$)** (e.g., 128-bit)210210210210.
    
3. **Encrypt Message:** Encrypts the entire message (M) using the _symmetric_ session key ($K_s$)211211211211.
    
4. **Encrypt Session Key:** Encrypts the session key ($K_s$) using the _receiver's_ **public key ($PU_b$)**212212212212.
    
5. **Append:** Attaches the encrypted session key to the encrypted message and sends it.
    
6. **Receiver:** Receives the encrypted payload.
    
7. **Decrypt Session Key:** Uses their _own_ **private key ($PR_b$)** to decrypt the encrypted session key and recover $K_s$ 213213213213.
    
8. **Decrypt Message:** Uses the recovered session key ($K_s$) to (symmetrically) decrypt the message (M)214214214214.
    

Confidentiality & Authentication 215

PGP can provide both services on the same message216. The order of operations is crucial: **sign first, then encrypt**.

1. The sender creates a signature (signed hash using $PR_a$) and attaches it to the message217.
    
2. The sender then encrypts _both_ the original message and its signature using a one-time session key ($K_s$)218.
    
3. The sender encrypts the session key ($K_s$) using the receiver's public key ($PU_b$) and attaches it219.
    

The receiver first decrypts the session key, then decrypts the message+signature, and finally verifies the signature.

### PGP Operations

Compression 220

- By default, PGP **compresses** the message _after_ signing but _before_ encrypting221.
    
- It uses the ZIP compression algorithm222.
    
- This is done so the uncompressed message and signature can be stored for later verification223.
    
- Compression before encryption is also a good security practice, as it reduces patterns in the plaintext, strengthening the encryption.
    

PGP Public & Private Keys 224

- A user may have many public/private keys. To identify which key was used, PGP uses a **Key ID**225225225225.
    
- This ID is the **least significant 64-bits of the public key** 226and is very likely to be unique227.
    
- This ID is used in signatures 228 and in the encrypted session key component so the receiver knows which private key from their keyring to use for decryption.
    

PGP Key Rings 229

PGP does not rely on a central server for key lookups. Instead, each user maintains a pair of keyrings: 230

- **Public-key ring:** A local database containing all the public keys of _other_ PGP users that this user knows, indexed by their Key ID231.
    
- **Private-key ring:** Contains the user's _own_ public/private key pair(s)232. The private keys in this ring are themselves encrypted, secured by a key derived from a hashed **passphrase**233.
    

The security of the user's private keys is entirely dependent on the strength of their passphrase234.

(The diagrams for PGP Message Generation 235and Reception 236 visually summarize the flow of using these keyrings to select the sender's private key ($PR_a$), the receiver's public key ($PU_b$), and the receiver's private key ($PR_b$) to perform signing and decryption operations.)

PGP Key Management (Web of Trust) 237

PGP's key management model is its most defining feature and contrasts sharply with the centralized model used by S/MIME.

- PGP does not rely on Certificate Authorities (CAs)238.
    
- Instead, **every user is their own CA**239.
    
- Users **sign the public keys** of other users they know directly to vouch for their identity240.
    
- This creates a decentralized **"web of trust"**241.
    

You can trust a new public key if:

1. You signed it yourself (you trust it completely).
    
2. It has been signed by someone else _whose key you already trust_242.
    

The PGP keyring includes trust indicators to manage this243. This "fault-tolerant web of confidence" 244 allows PGP to function without any central, trusted third party. Users can also issue "revocation" certificates to invalidate their keys if they are compromised245.

S/MIME 246

S/MIME (Secure/Multipurpose Internet Mail Extensions) is the other major standard for end-to-end email security.

- It is a MIME extension for email security247.
    
- It provides the same guarantees as PGP: confidentiality, authentication, integrity, and non-repudiation248.
    

The Key Difference:

S/MIME uses a completely different key management model: a centralized Public Key Infrastructure (PKI)249.

- Instead of a "web of trust," S/MIME relies on **X.509 certificates**250.
    
- These certificates are issued by trusted third-party Certificate Authorities (CAs). The CA (e.g., DigiCert, Sectigo) verifies your identity and issues a certificate that binds your public key to your name/email.
    
- This model gives the user **less control** but provides **better interoperability**, as it is built into most major corporate email clients (like Outlook and Apple Mail) which already trust the world's major CAs.
    

---

prossima lezione [[2 - Network Security]]