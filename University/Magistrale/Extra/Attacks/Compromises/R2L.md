# Remote-to-Local (R2L)

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