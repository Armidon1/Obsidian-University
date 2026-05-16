# 🏛️ Windows Domains & Domain Logon

> **Context:** Foundational concept for Windows enterprise security **Source:** Hacking Exposed 7 — supporting concept **Category:** Windows Architecture / Identity **Tags:** #windows #active-directory #authentication #domain #kerberos #foundation

---

## 📌 Definition

A **Windows domain** is a **centralized identity and policy management system** for Windows networks.

> A group of computers that all trust a central authority (the **Domain Controller**) to handle authentication, authorization, and policy enforcement.

Think of it as **outsourcing user management to a central server**.

---

## 🎯 The Problem Domains Solve

Imagine a company with 500 employees and 2000 computers. Without a domain:

```
Without domain (painful):
- Alice has 2000 separate accounts on 2000 PCs
- Password change → must update on every machine
- New employee → create accounts on every machine
- No central audit log
- No central policy

With domain (sane):
- Alice has ONE account in Active Directory
- Password change → done in one place
- New employee → add once, available everywhere
- Centralized auditing and policy
```

This is the **exact same problem** Linux solves with LDAP / FreeIPA / Samba AD.

---

## 🐧 Linux Equivalents (Coming from Unix Background)

|Windows Concept|Linux Equivalent|
|---|---|
|**Active Directory Domain**|LDAP server + Kerberos KDC (e.g., FreeIPA)|
|**Domain Controller (DC)**|LDAP/Kerberos server|
|**Domain Logon**|LDAP / SSSD / PAM auth against central server|
|**Local Logon**|`/etc/passwd` + `/etc/shadow`|
|**Group Policy (GPO)**|Ansible / Puppet / Chef|
|**Domain user `CORP\alice`**|LDAP user `uid=alice,ou=people,dc=corp`|
|**Domain Admin**|`root` on the LDAP/Kerberos server|
|**SYSVOL share**|NFS-shared config / `/etc/skel`|

> [!tip] Mental shortcut If you've used **SSH with LDAP auth** or run `realmd join` — that's conceptually the same as a Windows machine joining a domain.

---

## 🆚 Local Logon vs Domain Logon

### Local Logon

```
Input:       username: alice
             password: hunter2

Process:     Windows checks LOCAL SAM database on THIS machine
             Found "alice" → password matches → ✅ login

Identity:    DESKTOP-ABC123\alice
                     ↑
              name of THIS specific machine
```

### Domain Logon

```
Input:       username: CORP\alice          ← DOMAIN prefix
             password: hunter2

Process:     "alice" isn't a local user
             → Send auth request to a DOMAIN CONTROLLER
             
DC checks:   Looks up "alice" in Active Directory
             Verifies password (via Kerberos AS-REQ)
             Issues a TGT
             → Tells the machine "this is alice, let her in"

Identity:    CORP\alice
                ↑
           name of the DOMAIN (whole company)
```

> [!important] Key insight In domain logon, the machine you type your password into doesn't even HAVE your account locally — it delegates the entire decision to the Domain Controller.

---

## 🏗️ Domain Architecture

### Roles in a Domain

|Role|Description|Count in typical company|
|---|---|---|
|**Domain Controller (DC)**|Stores AD database, authenticates users, issues tickets|1–5 servers|
|**Domain Member**|Trusts the DC for auth, has its own local SAM too|All other machines (PCs, servers)|
|**Standalone**|Not part of any domain, only local accounts|Home computers|

### Topology Diagram

```
                    ┌──────────────────────┐
                    │   DC01.contoso.com   │  ← Domain Controller
                    │   (Domain Controller)│     Stores all user accounts
                    │                      │     Issues Kerberos tickets
                    │   AD database:       │     Enforces policies
                    │   - alice            │
                    │   - bob              │
                    │   - charlie          │
                    │   - svc_sql          │
                    └──────────┬───────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
       ┌──────▼──────┐  ┌──────▼──────┐  ┌─────▼──────┐
       │ FILE01      │  │ ALICE-PC    │  │ BOB-LAPTOP │
       │ File server │  │ Alice's PC  │  │ Bob's      │
       │             │  │             │  │ laptop     │
       │ Domain      │  │ Domain      │  │ Domain     │
       │ member      │  │ member      │  │ member     │
       └─────────────┘  └─────────────┘  └────────────┘
```

---

## 🎬 Example Scenario: Alice Logs In

Walking through the full flow:

### Step 1: Alice sits at BOB-LAPTOP and types `CORP\alice` + password

```
1. BOB-LAPTOP forwards auth request to DC01
2. DC01 checks AD → password matches
3. DC01 issues Alice a TGT (Kerberos)
4. BOB-LAPTOP lets her in
5. She sees ALICE's profile (not Bob's)
```

### Step 2: Alice opens `\\FILE01\reports`

```
1. Her PC uses her TGT to request a service ticket
   for FILE01 from DC01
2. DC01 issues the service ticket
3. She presents the ticket to FILE01
4. FILE01 doesn't know Alice directly...
   but it trusts DC01's ticket → ✅ access granted
```

**This is the entire point of a domain.** One identity, used everywhere.

---

## 🏢 What You Actually Are in this Picture

> Your laptop in this model is **NOT** a domain server.

|You/Your machine is...|Means...|
|---|---|
|A **standalone** PC (home use)|No domain at all — only local accounts|
|A **domain member** (work PC)|Trusts a central DC, but you're not the DC|
|A **Domain Controller**|The actual central authority (rare — only servers)|

> [!warning] Common confusion "Windows as a domain server" only applies to Domain Controllers. Your work laptop is a **client** that trusts the company's DCs — it's not itself acting as a server.

---

## 🎯 Why This Matters for Hacking Exposed 7

Once you grasp domains, every Windows attack falls into one of two categories:

### Category 1: Local Attacks (one machine)

|Attack|Scope|
|---|---|
|**SAM dumping**|Gets LOCAL users on ONE machine|
|**Local Administrator hash**|Only useful on machines sharing that password|
|**Local privilege escalation**|One machine compromised|

### Category 2: Domain Attacks (whole company)

|Attack|Scope|
|---|---|
|**Pass-the-Ticket**|Steal TGT → impersonate user across entire domain|
|**Pass-the-Hash** (domain account)|Authenticate as domain user anywhere|
|**Kerberoasting**|Crack service ticket → service account password|
|**Golden Ticket**|Compromise `krbtgt` → forge tickets for ANY user|
|**DCSync**|Pretend to be a DC → extract ALL hashes|
|**Domain Admin compromise**|🎯 Game over — total company compromise|

> [!danger] Why domain attacks are catastrophic The domain is the **trust anchor for everything**. Compromise it → compromise every machine that trusts it.

---

## 🛡️ Defensive Implications

### Tier Model

Windows defense uses a **tiered model** to limit blast radius:

|Tier|Contains|Protection|
|---|---|---|
|**Tier 0**|Domain Controllers, AD admins|Maximum isolation, dedicated admin workstations|
|**Tier 1**|Server admins, server infrastructure|Separated from user workstations|
|**Tier 2**|Workstation admins, user PCs|Most exposed, least privileged|

The principle: **a Tier 2 compromise should never lead to a Tier 0 compromise.**

### Key Domain Defenses

- [ ] **Separate admin accounts** per tier (no admin account spans tiers)
- [ ] **Dedicated admin workstations (PAWs)** for Tier 0
- [ ] **LAPS** — randomize local admin passwords per machine
- [ ] **Credential Guard** — protect domain credentials in LSASS
- [ ] **Restrict NTLM** — force Kerberos where possible
- [ ] **Monitor DCSync replication** — should only come from other DCs
- [ ] **Rotate `krbtgt` password** — twice, to invalidate Golden Tickets

---

## 🧠 The Mental Model to Adopt

> **A Windows domain = a corporate Kerberos + LDAP server (the Domain Controller) that all the company's PCs delegate authentication to.**

When reading _Hacking Exposed 7_, always ask:

```
Is this attack about a LOCAL account or a DOMAIN account?

LOCAL attacks:
✓ SAM dumping
✓ Local password hash extraction
✓ Single-machine privilege escalation
→ Limited blast radius

DOMAIN attacks:
✓ Kerberos ticket theft
✓ AD enumeration
✓ Domain credential abuse
→ Massive blast radius
```

---

## 🔗 Related Notes

- [[Interactive Logon]]
- [[Pass-the-Ticket]]
- [[Pass-the-Hash]]
- [[Virtualization-Based Security]]
- [[Mimikatz]]
- [[Cain & Abel — Legacy Reference]]
- [[Kerberos Protocol]]
- [[Active Directory]]
- [[DCSync Attack]]
- [[Golden Ticket]]
- [[Tier Model for AD]]

---

## 📚 References

- _Hacking Exposed 7_ — foundational concept for Windows chapters
- Microsoft Docs — Active Directory Domain Services
- Microsoft Docs — Securing Privileged Access (Tier Model)

---

_Foundational concept note — links from all Windows enterprise security topics_