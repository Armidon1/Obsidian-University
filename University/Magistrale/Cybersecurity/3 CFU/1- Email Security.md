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

- **MUA (Message User Agent)** — User’s email client
    
- **MSA (Mail Submission Agent)** — Accepts mail from MUA, checks format
    
- **MTA (Mail Transfer Agent)** — Transfers mail between servers
    
- **MDA (Mail Delivery Agent)** — Delivers mail to local mailbox
    
- **MS (Message Store)** — Stores messages
    
- **Protocols:** SMTP, POP, IMAP
    
The MUA is the client part of the protocol takes in charge the message, checks if syntax is correct and if everything is okay, it takes simply in charge the messages and sends to his email server. The MUA is outside the message handling system (MHS). This one can be a single piece of software. The MTA is the core of the MHS: does basically everything. This is a distributed system. The MTA needs only to understand which server needs to contact to send the message. This is possible thanks the Ip-routing system. As we can see, we have a SMTP protocol: Simple mail transfer protocol.  We can see also “Local”, which means there are no predefined protocols, and then POP/IMAP (manly IMAP) used to access to the local messages stored.

---

## Components Explained

### MUA (Message User Agent)

Used by end-users to send, receive, and manage emails.

### MSA (Mail Submission Agent)

- Receives messages from MUA.
    
- Works with MTA for delivery.
    
- Ensures message format compliance.
    

### MTA (Mail Transfer Agent)

- Transfers messages using **SMTP**.
    
- Acts as both client and server.
    

### MDA (Mail Delivery Agent)

- Handles final delivery to recipient’s mailbox.
    
- Stores message locally.
    

---

## Email Exchange

**Protocol:** SMTP (RFC 821 → RFC 5321)

- **Envelope:** Contains delivery parameters, separate from header/body.
    
- **Address format:** `user@domain`
    
    - `user`: local part
        
    - `domain`: fully qualified domain name (FQDN)
        
The domain has exactly the struct needed to find the destination. The MTA if checks that I AM the domain, if is true, then the destination is LOCAL, else i have to send out of here. Tipycally we have only 2 steps when i send an email. But happens that we have more steps when an industry has an heiracly structure and happens that is neened a central destination that does as a gateway between the sender and the reciever. The domain is foundamental in this case. In the end we will talk about the DNS.

---

## Message Format

Defined by **RFC 5322** and extended by **MIME (RFC 2045–2049)**.

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

See more on [[EMAIL - SPF]]

### Limitations

- Breaks on forwarding or mailing lists
    
- No content integrity
    
- Misconfiguration risks
    
- No body protection
    
SPF ignores the body, he just checks if the server which sends an email is authorised to send email to me. In this case we can easily block those people who creates his own server.

See also [[EMAIL - SPF#Perché le mailing list rompono SPF (concetto chiave)|Why the mailing list broke SPF]]

---
# continuare la registrazione a partire dal minuto 33  
## DKIM – DomainKeys Identified Mail

One of the limitation of SPF is protect the body. The sending server makes a cryptography string with a private key. 

### Guarantees

- **Integrity** (message unaltered)
    
- **Authentication** (valid signer)
    
- **Non-repudiation**

### Possible DKIM Deployiment 
![[Pasted image 20251028184726.png]]

### Process

1. **Signing:** Sender adds DKIM-Signature using [[7 CS - Asymmetric encryption||private key]] 
    
2. **DNS:** Publishes public key via TXT record
    
3. **Verification:** Receiver checks signature with [[7 CS - Asymmetric encryption||public key]] 
    

## How does DKIM Work 
### 1) generating the Signature (Signing Process)
```text
DKIM-Signature: 
	v=1;
	a=rsa-sha256;
	c=relaxed/relaxed;
	d=diag.uniroma1.it;
	s=google;
	t=1728828422;
	x=1729433222;
	dara=google.com;
	h=to:subject:message-id:date:from:mime-version:from:to:cc:subject:date:message-
	id:reply-to;
	bh=t6DYHnvgeJvZ02sgmWVU/4X9LTVieRyKbl+FRWPu3Co=;
b=gx0VlcD55ZtEOTnE2FJJSSgt8Padr87pkhbkWw7FbuIyWY2O0QvKy52DD6DsuiT2oj
q5/jSGM4y1b0XKHM7CU1Fhk+ScKi16hj8HdezlpnFOZbbiKS43uysV8lLfbv5SOaDEFv
REmsa4Az8duRs1fYEsQ9ixRu5RPOLRgCBcxb0=
```

### 2 - Public Key Published in DNS:

- The domain that sends the email publishes the corresponding public key in the Domain Name System (DNS) as a TXT record. The public key is used to verify the authenticity of the signature.
- The DNS record also speci es the selector (a pre x to di erentiate between multiple keys) and the policy the sender wants to use for DKIM. 

```Bash
> dig +noall +answer google._domainkey.uniroma1.it txt

google._domainkey.uniroma1.it. 21600 IN
TXT "v=DKIM1; k=rsa;
p=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzMa8wGDtu7DVjVP1JwVzMym/
KktdVSBhvtMbgpolQTWqKxRHejICsUvvFv6WGP7kKQnVA5" "2JtFU9LVGvTfkNF5J/x/
9wUlBSQMCwGc4IXNdgA5fcn/49fV+YY1RFY44PhoTSWTQnKp7axDRFO3Uo05uFXSl0OnNo0Gd/
tnDRG538tnM8VzZIF+jjS76GkV/iZT2tcDSBMsWjZTR" "tk7eG/GDVS8pbD14CX/
bf7RTflt3sTiwcp3YUn5T66ioCmc7PIu5CCKfTcW7i7E246Ef4hz+6CySyNRxipnrK6BrXGoraod5U66K6boXVW
ojDKHRflvdoeQ49hW8N5PHFqJKebwIDAQAB"
```

#### SELECTORS
To support multiple concurrent public keys per signing domain, key
namespace is subdivided using selectors
- for example selectors might indicate the names of o ce locations, the signing
date, or even the individual user
Selectors are useful to implement some important use cases
- domains that want to delegate signing capability for a speci c address for a given duration to a partner, such as an advertising provider or other outsourced function
- domains that want to allow frequent travelers to send messages locally without the need to connect with a particular MSA.
- "affinity" domains (e.g., college alumni associations) that provide forwarding of incoming mail, but that do not operate a MSA for outgoing mail

### 3 - Verification Process:

- When an email is received, the recipient’s mail server looks at the DKIM signature header to see which domain signed the message and which selector to use. It retrieves the corresponding public key from the domain’s DNS.
- The server then veri es the digital signature by comparing it with the hash of the received message's content. If the signature matches, it con rms that the email:
	- Hasn’t been altered in transit (message integrity).
	- Is indeed authorized by the sender’s domain (authenticity).

---

## DMARC – Domain-based Message Authentication, Reporting & Conformance

### Purpose

- Protects domains from spoofing and phishing
    
- Builds on SPF and DKIM
    
- Allows domain owners to specify actions and receive reports
    

### Example Record

```text
_dmarc.example.com TXT
"v=DMARC1; p=reject; rua=mailto:reports@example.com; pct=100"
```

### Policies

- `none` → No action
    
- `quarantine` → Mark as spam
    
- `reject` → Block message
    

### Reports

- **Aggregate reports:** XML-based statistics
    
- **Forensic reports:** Copies of failed messages
    

### Limitations

- Mailing lists and forwarding can break validation
    
- Strict policies may reject legitimate mail
    

---

## ARC – Authenticated Received Chain

- Preserves authentication results across intermediaries
    
- Adds:
    
    - `ARC-Authentication-Results`
        
    - `ARC-Message-Signature`
        
    - `ARC-Seal`
        
- Each relay signs the message and seals prior headers
    

### Benefits

- Maintains trust through relays
    
- Prevents DMARC breaks due to forwarding
    
- Improves delivery for mailing lists
    

### Does Not Guarantee

- Sender trustworthiness
    
- Content safety
    

---

## Summary

|Mechanism|Ensures|Limitation|
|---|---|---|
|**SPF**|Sender server authorization|Fails on forwarding|
|**DKIM**|Message integrity/authenticity|Doesn’t verify From:|
|**DMARC**|Domain alignment + policy enforcement|Needs aligned SPF/DKIM|
|**ARC**|Chain of trust preservation|No content validation|

---

**End of Notes**  
(c) 2016 F. Amore — _E-Mail: A Rich Introduction_

---

Would you like me to include **syntax-highlighted examples** (like `dig` queries, headers, and email samples) in Markdown code blocks for your study version?