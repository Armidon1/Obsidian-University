# 🛡️ Virtualization-Based Security (VBS)

> **Context:** Modern Windows defense against credential dumping (mimikatz, pwdump, etc.) **Category:** Windows Security / Kernel Protection **Tags:** #windows #security #virtualization #credential-guard #hypervisor #defense

---

## 📌 Definition

**Virtualization-Based Security (VBS)** is a Windows security feature that uses the **hypervisor (Hyper-V)** to create isolated memory regions that **even the kernel itself cannot access**.

> [!important] Key insight VBS = **VBS does NOT mean Visual Basic Script** in this context. It stands for **Virtualization-Based Security**.

---

## 🧠 The Core Idea

### Traditional Assumption (Pre-VBS)

> "If I have kernel privileges (ring 0), I can read **any** memory on the system."

This is exactly what tools like `mimikatz` and `pwdump` exploit — they get SYSTEM, then read LSASS memory to extract credentials.

### What VBS Changes

VBS uses **hardware virtualization** to create a security boundary **below the kernel**. The hypervisor sits underneath the OS and uses CPU features to physically prevent the normal kernel from accessing protected memory regions.

---

## 🏛️ Architecture: Virtual Trust Levels (VTLs)

```
┌─────────────────────────────────────────────┐
│  Normal World (VTL 0)                       │
│  ┌───────────────────────────────────────┐  │
│  │  User Mode (ring 3)                   │  │
│  │  - Apps, services                     │  │
│  └───────────────────────────────────────┘  │
│  ┌───────────────────────────────────────┐  │
│  │  Kernel Mode (ring 0)                 │  │
│  │  - Windows kernel, drivers            │  │
│  │  - LSASS (placeholder)                │  │
│  └───────────────────────────────────────┘  │
└─────────────────────────────────────────────┘
              ↑ CANNOT ACCESS ↓
┌─────────────────────────────────────────────┐
│  Secure World (VTL 1) — protected enclave   │
│  ┌───────────────────────────────────────┐  │
│  │  Isolated User Mode (IUM)             │  │
│  │  - LSAIso.exe (real credentials)      │  │
│  │  - Code integrity checks              │  │
│  └───────────────────────────────────────┘  │
│  ┌───────────────────────────────────────┐  │
│  │  Secure Kernel                        │  │
│  └───────────────────────────────────────┘  │
└─────────────────────────────────────────────┘
              ↑
     Enforced by the hypervisor
```

|Layer|What runs here|Accessible from normal kernel?|
|---|---|:-:|
|**VTL 0**|Normal Windows (kernel + user mode)|—|
|**VTL 1**|Secure Kernel + Isolated User Mode (IUM)|❌ No|

---

## 🔐 What Lives in the Enclave (with Credential Guard)

When **Credential Guard** is enabled, Windows moves sensitive material into VTL 1:

|Secret|Where it lives with VBS|
|---|---|
|NTLM hashes|LSAIso (secure enclave)|
|Kerberos TGTs|LSAIso|
|Derived credentials|LSAIso|
|LSASS process itself|Still in normal kernel — but only as a **proxy** to LSAIso|

> [!tip] Important The normal LSASS still exists — it just becomes a **handle** that communicates with the real credential store in VTL 1.

---

## ⚙️ Hardware Requirements

VBS is not free — it needs:

|Requirement|Purpose|
|---|---|
|**CPU virtualization** (Intel VT-x / AMD-V)|Hypervisor execution|
|**IOMMU** (Intel VT-d / AMD-Vi)|Prevents DMA attacks|
|**TPM 2.0**|Key storage, attestation|
|**UEFI Secure Boot**|Verified boot chain|
|**HVCI** (Hypervisor-Protected Code Integrity)|Driver signature enforcement|

> [!info] Why Windows 11 requires TPM 2.0 Microsoft mandated TPM 2.0 on Windows 11 specifically to enable **VBS by default** on consumer hardware.

---

## 💥 Why This Killed Classic Credential Dumping

### Pre-VBS attack flow

```
Attacker gets SYSTEM privilege
        │
        ▼
Runs mimikatz / pwdump against LSASS
        │
        ▼
✅ Reads NTLM hashes, Kerberos tickets, plaintext passwords
        │
        ▼
Pass-the-Hash, Golden Ticket, lateral movement
```

### Post-VBS attack flow

```
Attacker gets SYSTEM privilege
        │
        ▼
Runs mimikatz against LSASS
        │
        ▼
Finds only LSAIso handles — actual hashes are in VTL 1
        │
        ▼
❌ No credentials extracted
        │
        ▼
Would need to break the hypervisor itself
(exponentially harder)
```

---

## ⚠️ Limitations & Caveats

VBS is **not** a silver bullet. It only closes specific attack vectors:

### What VBS Does NOT Protect Against

|Attack|Still works?|Why|
|---|:-:|---|
|**Kerberoasting**|✅ Yes|Attacks tickets, not local memory|
|**AS-REP Roasting**|✅ Yes|Attacks tickets, not local memory|
|**DCSync**|✅ Yes|DCs don't fully protect NTDS the same way|
|**Phishing / social engineering**|✅ Yes|VBS has nothing to say here|
|**Newly typed passwords**|⚠️ Partial|Briefly pass through normal LSASS during logon|
|**Keylogging**|✅ Yes|Captures input before it reaches LSASS|
|**Privilege escalation bugs**|✅ Yes|Until they pivot to credential dumping|

### Configuration Caveats

- VBS must be **explicitly enabled** — many Windows 10/11 deployments still don't have it on
- **Domain Controllers** have their own protection model (not standard Credential Guard)
- Some **legacy applications** break under HVCI / VBS
- **Driver compatibility** required — old drivers often fail HVCI checks

---

## 🛠️ Checking VBS Status

### PowerShell

```powershell
# Check VBS status
Get-CimInstance -ClassName Win32_DeviceGuard `
  -Namespace root\Microsoft\Windows\DeviceGuard

# Specifically check Credential Guard
(Get-CimInstance -ClassName Win32_DeviceGuard `
  -Namespace root\Microsoft\Windows\DeviceGuard).SecurityServicesRunning
# Output value 1 = Credential Guard is running
```

### MSINFO32

```
Start → msinfo32 → System Summary
Look for:
  - Virtualization-based security: Running
  - Virtualization-based security Services Running: Credential Guard
```

### Enabling VBS / Credential Guard

```
Group Policy:
Computer Configuration
  → Administrative Templates
    → System
      → Device Guard
        → Turn On Virtualization Based Security
```

---

## 🎯 Defender's Checklist

- [ ] Verify hardware supports VBS (VT-x/d, TPM 2.0, UEFI)
- [ ] Enable **Secure Boot** in UEFI
- [ ] Enable **VBS** via Group Policy
- [ ] Enable **Credential Guard**
- [ ] Enable **HVCI** (memory integrity)
- [ ] Audit drivers for HVCI compatibility
- [ ] Combine with **LSA Protection (RunAsPPL)** for defense in depth
- [ ] Monitor for VBS being disabled (registry, event log)

---

## 🔗 Related Notes

- [[Interactive Logon]]
- [[LSASS Credential Dumping]]
- [[Mimikatz]]
- [[Pass-the-Hash]]
- [[Credential Guard]]
- [[Windows Privilege Escalation]]
- [[Hypervisor Security]]
- [[TPM 2.0]]

---

## 📚 References

- _Hacking Exposed 7_ — Chapter 4 (context for what VBS defends against)
- Microsoft Docs — Virtualization-Based Security
- Microsoft Docs — Credential Guard
- "Battle of SKM and IUM" — Black Hat USA presentations

---

_Study note — modern Windows defense layer_

# VBS vs [[Mimikatz]]

Not quite — that's a common oversimplification. **VBS + Credential Guard breaks one specific mimikatz technique, but mimikatz is a Swiss Army knife with many other modules that still work.**

Let me break it down:

---

## What VBS/Credential Guard Actually Blocks

Only **one** category of mimikatz attacks:

|Module|Blocked by VBS?|
|---|:-:|
|`sekurlsa::logonpasswords` (dump LSASS hashes)|✅ Blocked|
|`sekurlsa::tickets` (extract Kerberos tickets from LSASS)|✅ Blocked|

That's basically it. The "headline" feature gets neutralized — but mimikatz has dozens of modules.

---

## What Still Works Even With VBS Enabled

### 🎫 Kerberos Attacks (most still work)

|Attack|Why VBS doesn't help|
|---|---|
|**Kerberoasting** (`kerberos::ask`)|Attacks service tickets from the KDC, not local memory|
|**AS-REP Roasting**|Same — targets accounts with pre-auth disabled|
|**Golden Ticket** (`kerberos::golden`)|Forges TGTs using the krbtgt hash (obtained elsewhere)|
|**Silver Ticket**|Forges service tickets with a service account hash|
|**Pass-the-Ticket** (`kerberos::ptt`)|Injects tickets — VBS doesn't stop ticket _injection_, only extraction|
|**Overpass-the-Hash**|Uses NTLM hash to request a TGT|

### 🔑 Local SAM / Registry Attacks

```
mimikatz # lsadump::sam
mimikatz # lsadump::secrets
mimikatz # lsadump::cache
```

These read the **local SAM database** and **LSA secrets** from the registry — completely outside Credential Guard's scope (which only protects domain credentials in LSASS memory).

### 🏰 Domain Controller Attacks

|Attack|Notes|
|---|---|
|**DCSync** (`lsadump::dcsync`)|Replicates secrets from DC via legitimate AD replication API|
|**DCShadow**|Registers a rogue DC and pushes changes|

DCSync is the **single most impactful attack** in modern AD pentests, and VBS does nothing to stop it.

### 🔓 Other Modules

- `crypto::*` — Certificate and key extraction
- `vault::*` — Windows Vault credentials
- `dpapi::*` — DPAPI-protected secrets (browser passwords, RDP creds)
- `misc::skeleton` — Skeleton key attack (patches LSASS for universal password)
- `token::elevate` — Token impersonation

---

## The Honest Summary

```
Pre-VBS mimikatz mindset:
"Get SYSTEM → dump LSASS → instant domain admin"
        │
        ▼  (VBS deployed)
        │
Post-VBS mimikatz mindset:
"Get SYSTEM → can't dump LSASS easily
  → pivot to Kerberoasting / DCSync / SAM dump
  → still get domain admin, just takes 2 extra steps"
```

---

## Cracks in VBS Itself

Even the LSASS protection isn't 100% airtight:

|Bypass|Status|
|---|---|
|**Vulnerable signed drivers** (BYOVD attacks)|Active in the wild|
|**Newly entered passwords** in transit|Brief window of exposure|
|**WDigest re-enablement** via registry|Pre-deployment misconfigs|
|**Mimikatz's own evolution**|Constantly adapting|

There's been a whole research line on bypassing Credential Guard — search for "BYOVD Credential Guard bypass" and you'll find ongoing work.

---

## Practical Takeaway

> **Mimikatz isn't useless with VBS** — it's just no longer a one-shot win. The credential-dumping headline attack is gone, but the tool remains essential for Kerberos manipulation, DCSync, SAM dumping, and ticket forging.

For defenders, this means VBS is **necessary but not sufficient**. You also need:

- Tier 0 isolation (protect DCs from compromised workstations)
- Restrict who can perform AD replication (blocks DCSync)
- Strong service account passwords (defeats Kerberoasting)
- LAPS (randomized local admin passwords — defeats SAM dump value)
- EDR monitoring for mimikatz behavior, not just signatures

So in your _Hacking Exposed 7_ notes: the **techniques** the book describes remain conceptually valid in 2026 — only the **specific attack surface** has shifted. The cat-and-mouse continues. 🐱🐭