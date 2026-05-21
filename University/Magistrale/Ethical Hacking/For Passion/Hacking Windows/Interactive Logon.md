# 🔐 Interactive Logon (Windows)

> **Source:** Hacking Exposed 7 — Chapter 4 (Privilege Escalation) **Category:** Windows Security / Authentication **Tags:** #hacking #windows #authentication #privilege-escalation #logon

---

## 📌 Definition

An **interactive logon** is an authentication session in which a user (human) is **directly operating the machine in real time**, with a full working environment loaded around them.

When Windows establishes an interactive session, it sets up:

- A **desktop** (graphical or terminal)
- A **user profile** loaded in memory
- An **access token** with the user's privileges
- **Credentials cached in LSASS** (Local Security Authority Subsystem Service)

> [!important] Why this matters The credentials cached in LSASS are exactly what tools like **mimikatz** target. An interactive session = high-value target.

---

## 🧭 Mental Model

> An interactive session means **someone is "present"** at the machine, with a full working environment loaded around them.

A **network logon** is like showing your ID at a door to grab a specific file — you never actually enter the building. An **interactive logon** means you walked in, sat down, and everything is loaded up around you.

From the attacker's perspective: **the building is where all the valuables are kept.**

---

## 🆚 Interactive vs Non-Interactive

|Scenario|Interactive?|Why|
|---|---|---|
|Sitting at a PC and logging in|✅ Yes|Full desktop, token, credentials in memory|
|RDP into a server|✅ Yes|Same as above, just remote|
|Accessing a shared folder over SMB|❌ No|Only password validation, no desktop/token loaded|
|A Windows service starting automatically|❌ No|Runs in background, no human present|
|Scheduled task execution|❌ No|Batch logon, no full session|

---

## 🔢 Windows Logon Types

Windows assigns a numeric **Logon Type** to every authentication event (visible in Event Viewer, `Event ID 4624`):

|Type|Name|Example|Interactive?|
|---|---|---|:-:|
|**2**|Interactive|Local console login|✅|
|**3**|Network|SMB share access|❌|
|**4**|Batch|Scheduled tasks|❌|
|**5**|Service|Windows services|❌|
|**7**|Unlock|Unlocking a workstation|✅|
|**8**|NetworkCleartext|Cleartext network logon|❌|
|**9**|NewCredentials|`runas /netonly`|⚠️ Partial|
|**10**|RemoteInteractive|RDP session|✅|
|**11**|CachedInteractive|Domain login with cached creds|✅|

> [!tip] Attacker focus Types **2** and **10** are the most valuable — they cache credentials in memory and create full sessions.

---

## 🎯 Why It Matters in Privilege Escalation

### Attack Chain

```
Low-priv shell obtained
        │
        ▼
Enumerate interactive sessions (types 2 / 10)
        │
        ▼
Dump LSASS memory (mimikatz, procdump)
        │
        ▼
Extract NTLM hashes / Kerberos tickets / plaintext passwords
        │
        ▼
Pass-the-Hash / Token Impersonation
        │
        ▼
SYSTEM or Domain Admin
```

### Key Concepts

- **Credentials cached in LSASS** → extractable by attackers with SeDebugPrivilege
- **Access tokens generated** → can be stolen or impersonated (_token impersonation_)
- **More forensic traces** → but also more exploitable material left behind

---

## 🛡️ Countermeasure: "Deny Log On Locally"

A Windows Group Policy setting:

> `Security Settings → Local Policies → User Rights Assignment → Deny log on locally`

> [!warning] Common misconception This does **NOT** mean "nobody can use the computer." It is **account-scoped** — it blocks **specific accounts** from ever starting an interactive session.

### Accounts to Deny Interactive Logon To

|Account Type|Why deny?|
|---|---|
|`NETWORK SERVICE`|Service-only, should never have a shell|
|`LOCAL SERVICE`|Same — service-only|
|SQL Server / IIS service accounts|No reason for an interactive session|
|Domain service accounts|Limits blast radius if compromised|
|Guest account|Should never have an interactive session|
|Privileged admin accounts|Force use of `runas` instead|

### What This Blocks

```
Attacker exploits web app running as "svc_webapp"
        │
        ▼
Tries to spawn interactive shell as svc_webapp
        │
        ▼
❌ BLOCKED by "Deny log on locally" policy
        │
        ▼
No LSASS credential caching, no pivot point
```

### Related Policies

- **Deny log on through Remote Desktop Services** → blocks Logon Type 10
- **Deny log on as a service** → controls who can run services
- **Deny log on as a batch job** → controls scheduled tasks

---

## 🔑 Underlying Principle

> **Least privilege applied to logon rights**: every account should only be able to authenticate in the ways it actually needs.

A service account needs to run a service — it does **not** need:

- An interactive desktop
- Credentials cached in LSASS
- An access token sitting in a user session

---

## 🔗 Related Notes

- [[Wireless Driver Exploits]]
- [[LSASS Credential Dumping]]
- [[Mimikatz]]
- [[Token Impersonation]]
- [[Pass-the-Hash]]
- [[Windows Privilege Escalation]]
- [[Group Policy Hardening]]

---

## 📚 References

- _Hacking Exposed 7_ — Chapter 4 (Privilege Escalation)
- Microsoft Docs — [Logon Types](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4624)
- Microsoft Docs — User Rights Assignment

---

_Note created during Cybersecurity study session_