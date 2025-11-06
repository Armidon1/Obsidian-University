# User-to-Root (U2R)

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
