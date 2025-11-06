# Compromises (Unauthorized Access)

**Goal:** Gain unauthorized access to a system, either from remote locations or by escalating privileges after initial entry.

#### Remote-to-Local (R2L)

Attacker gains local access from outside the network:

- Password guessing (brute-force)  
- Exploiting software bugs (e.g., buffer overflows in outdated software)  
- Phishing to steal credentials  

**Detection via Signatures:**

- ✅ **Brute-force signature patterns**: Repeated login attempts with different passwords → detectable by logging and rate-limiting rules.  
  - Example: A login attempt every 2 seconds from a single IP → detected as suspicious in SIEM (Security Information and Event Management).  
- ✅ **Vulnerability signatures**: Match known exploit payloads (e.g., `MS17-010` EternalBlue) to traffic or system logs.  

**Detection Methodology Insight:**  
Signature-based detection identifies known attack vectors. For example, a buffer overflow exploit in SMB can be detected using signature rules (like Snort’s `smb_exploit` rule). However, R2L attacks often rely on zero-day flaws — requiring **behavioral analytics** to spot unusual process creation or memory corruption.

#### User-to-Root (U2R)

Local attacker escalates from a standard user account to full administrative/root access:

- Exploiting system vulnerabilities in binaries (e.g., `SUID`, `setuid` programs, privilege escalation bugs)  
- Misconfigured permissions  
- Memory corruption flaws  

**Detection via Signatures:**

- ✅ **Process creation signatures**: Unusual processes spawning with elevated privileges.  
  - Example: A process called `calc.exe` launching with root rights → flagged as suspicious.  
- ✅ **System call signatures**: Abnormal use of privileged system calls (like `execve`, `ptrace`) in logs or audit trails.  

**Detection Methodology Insight:**  
While U2R exploits are often hidden, detection can be achieved through **behavioral rule sets** and **endpoint telemetry**. Signature-based tools may miss these if the exploit is novel — making **user behavior analytics (UEBA)** essential for detecting abnormal privilege escalation.