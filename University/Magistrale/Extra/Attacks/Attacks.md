### Probing / Scanning
[[Probing-Scanning]]
**Goal:** Discover active IP addresses, open ports, services, and network vulnerabilities to identify potential entry points for future attacks.

**Strategies:**

- **IP address sweeps**: Send ICMP echo requests (ping), TCP SYN packets, or UDP probes to detect live hosts.  
- **Port scanning**: Identify open ports using tools like `nmap`, `Portsweep`, or `IPSweep`.  
- **Service version detection**: Detect running software versions (e.g., Apache 2.4.37) to reveal known vulnerabilities.  
- **OS fingerprinting**: Determine the operating system type (Linux, Windows) to tailor attack payloads.

**Detection via Signatures:**

- ✅ **Network traffic signatures** for SYN scans, ICMP pings, or UDP probes detect common scanning patterns.
  - Example: A high volume of TCP SYN packets to a single IP → signature rule in IDS like Snort.  
- ✅ **Pattern-based detection**: Tools identify repetitive scan sequences (e.g., 100+ rapid port scans).  
- ⚠️ *Stealthy or fragmented scans* (like ACK sweeps or fragmented UDP) are harder to detect due to low volume and lack of clear patterns.

**Detection Methodology Insight:**  
Signature-based systems can flag fast, noisy scanning behavior. However, stealthy probes may evade detection — requiring **anomaly detection**, **behavioral analysis**, or **rate-limiting rules** in combination with signatures.

---

### Compromises (Unauthorized Access)
[[Compromises]]
**Goal:** Gain unauthorized access to a system, either from remote locations or by escalating privileges after initial entry.

#### Remote-to-Local (R2L)
[[R2L]]
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

---

#### User-to-Root (U2R)
[[U2R]]
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

---

### Malware-Based Attacks
[[Malware-Based Attacks]]
**Goal:** Infect systems with malicious code to disrupt operations, steal data, or maintain persistent access.

#### Viruses
[[Virus]]

- Attach themselves to legitimate programs  
- Spread only when a user runs the host program  
- Require human interaction  

**Detection via Signatures:**

- ✅ **File signature patterns**: Match known virus file structures (e.g., embedded code, boot sector codes).  
  - Example: A `.exe` file with an unusual section of hex data → detected by antivirus using file content signatures.  
- ✅ **Behavioral signatures**: Look for execution of infected programs in a non-standard location or context.

**Detection Methodology Insight:**  
Traditional antivirus relies heavily on **file signature databases** (e.g., Microsoft Defender, Kaspersky). Newer variants (like polymorphic viruses) evade detection — requiring **heuristics and machine learning models** to identify behavioral anomalies.

---

#### Worms
[[Worms]]
- Self-replicate across networks without user interaction  
- Spread via:  
  - Network shares  
  - Email attachments  
  - File-sharing systems (e.g., peer-to-peer)  

**Detection via Signatures:**

- ✅ **Network traffic signatures**: Identify rapid propagation patterns (e.g., high-volume file transfers, abnormal DNS queries).  
- ✅ **Payload signature detection**: Match known worm code (e.g., `Morris Worm`, `Conficker`) in packet data or file content.  

**Detection Methodology Insight:**  
Worms are often detected by **signature-based IDS/IPS** and email gateways. However, self-replicating worms can change their payload to avoid detection — so **anomaly-based detection** (e.g., sudden spike in network traffic) is crucial for early warning.

---

#### Trojan Horses
[[Trojan]]
- Appear as legitimate software but perform malicious actions  
- Users install them voluntarily (e.g., fake antivirus, free utilities)

**Detection via Signatures:**

- ✅ **File hash signatures**: Detect known Trojan hashes (SHA-256, MD5) in downloads or executables.  
- ✅ **Behavioral triggers**: Monitor for unexpected network connections, data exfiltration, or registry changes.  

**Detection Methodology Insight:**  
Trojans are often caught by **signature databases** and **sandboxing tools**. However, stealthy variants may remain undetected until they perform damage — so **behavioral monitoring** (e.g., monitoring for unusual outbound traffic) is key to catching them in action.

---

#### Rootkits
[[Rootkits]]
- Gain full system control after gaining access  
- Hide from detection by modifying kernel or OS processes  
- Often include backdoors for remote control  

**Detection via Signatures:**

- ❌ **No direct file signature**: Rootkits operate at a deeper level (kernel space), so traditional file-based signatures fail.  
- ✅ **Behavioral and system call signatures**: Detect unusual behavior like:  
  - Unexplained process listing  
  - Hidden processes in task manager  
  - Altered boot logs or registry entries  

**Detection Methodology Insight:**  
Rootkits are **hard to detect with signature-based methods alone**. Detection relies on:  
- **Integrity checking tools** (e.g., system hash comparisons)  
- **Hardware root-of-trust solutions**  
- **Behavioral analytics and endpoint detection (EDR)**  

> 🔍 Key Takeaway: Rootkits are a major challenge for traditional signature-based systems — requiring **layered defense with behavior monitoring, memory scanning, and real-time telemetry**.

---

### Summary Table: Attack Types & Detection via Signatures

| Attack Type           | Goal                          | Key Detection Methods (Signatures) |
|-----------------------|------------------------------|-------------------------------------|
| Probing / Scanning    | Find active services         | SYN flood, ping sweep patterns; high-volume scan detection |
| Remote-to-Local (R2L) | Gain access remotely        | Brute-force attempts; known exploit payloads (e.g., EternalBlue) |
| User-to-Root (U2R)    | Escalate to admin rights     | Privilege escalation in process logs; unusual system calls |
| Viruses               | Spread via host programs    | File content signatures; attachment-based detection |
| Worms                 | Self-replicate across net   | Network traffic patterns; payload matching |
| Trojan Horses         | Masquerade as legitimate    | File hash signatures; suspicious behavior (exfiltration) |
| Rootkits              | Full control + stealth      | Behavioral anomalies; missing processes; registry tampering |

---

### Final Thoughts

While **signature-based detection** is effective for known threats like malware, buffer overflows, and scanning patterns — it has significant limitations against:

- Zero-day attacks  
- Polymorphic or obfuscated code (e.g., rootkits, worms)  
- Stealthy or stealthy behavior  

✅ **Best Practice**: Combine signature-based detection with:  
- Behavioral analytics (UEBA)  
- Endpoint Detection & Response (EDR)  
- Network traffic analysis (NDR)  
- Machine learning for anomaly detection  

This hybrid approach ensures robust protection against both known and emerging threats.

Absolutely! Here's your requested content — **restructured and expanded in the exact same clear, structured style** as before, now fully dedicated to **Denial of Service (DoS)** attacks.

---

### Denial of Service (DoS)

**Goal:** Disrupt service availability by overwhelming a system, network, or application with traffic or resource demands, rendering it inaccessible to legitimate users.

**Strategies:**

- **Resource consumption**:  
  - Overload critical system resources like CPU, memory, disk space, or bandwidth.  
  - Example: A script that loops infinitely consumes 100% CPU → crashes the server.  

- **Network connectivity flooding**:  
  - Flood network connections with requests to exhaust bandwidth or connection limits.  
  - Examples:  
    - TCP SYN flood (half-open connection attacks)  
    - UDP floods (e.g., ICMP ping of death, DNS floods)  
    - HTTP flood (excessive GET/POST requests to a web server)

- **Configuration destruction or alteration**:  
  - Maliciously modify system settings (e.g., disable services, corrupt configuration files).  
  - Example: A hacker changes firewall rules to block legitimate traffic.

---

### Detection via Signatures

**Key Signature Patterns Used in Cybersecurity Systems**

| Signature Type | How It Works | Real-World Examples |
|---------------|-------------|----------------------|
| 🔍 **Network traffic signatures** | Detect abnormal patterns of request volume, packet size, or protocol usage. | - A sudden spike in TCP SYN packets → Snort rule: `alert tcp any any -> any any (msg:"SYN flood detected"; flags:S; sid:1000001;)`<br> - High-frequency HTTP GET requests from one IP → flagged as possible HTTP flood |
| 📂 **File or process signatures** | Identify malicious scripts that consume CPU/memory (e.g., infinite loops). | - Signature for a known resource-hogging script like `evil-loop.exe` in antivirus databases |
| 💡 **Behavioral anomaly rules** | Flag deviations from baseline usage (e.g., sudden 10x increase in bandwidth) | - SIEM systems detect abnormal CPU or disk I/O spikes using threshold-based rules |
| 📉 **Rate-of-attack signatures** | Measure request rate per second and trigger alerts when thresholds are exceeded. | - Rule: "If >5,000 requests/second from one IP → alert" |

---

### Detection Methodology Insight

#### ✅ Effective in Signature-Based Systems:
- **IDS/IPS (e.g., Snort, Suricata)** detect known DoS attack patterns using pre-defined rules.
  - Example: A SYN flood is detected by matching the TCP handshake pattern with a specific signature rule.
- **Firewall & WAFs** block suspicious traffic based on known attack signatures (e.g., blocking high-volume IP addresses).
- **Antivirus/EDR tools** identify malicious processes that consume excessive CPU or memory.

#### ⚠️ Limitations:
- ❌ Cannot detect **new, unknown DoS attacks** (especially those using novel resource-hogging techniques).  
- ❌ May miss **distributed denial-of-service (DDoS)** attacks if traffic is spread across many sources.  
- ❌ Resource exhaustion via **application-level bugs** or logic flaws may not show up in network signatures.

> 🚨 Example: A worm spreads through a network and consumes memory — this can be detected by behavioral monitoring, but a traditional signature system might only catch it after the CPU usage spikes above normal.

---

### Best Practices for Detection & Mitigation

| Layer | Recommended Approach |
|------|------------------------|
| **Network Level** | Use IDS/IPS with DoS-specific signatures (e.g., SYN flood detection). Deploy rate-limiting on firewalls. |
| **Application Level** | Implement input validation, timeouts, and request throttling to prevent resource abuse. |
| **Endpoint Level** | Monitor CPU, memory, disk, and network usage in EDR tools for abnormal spikes. |
| **Hybrid Detection** | Combine signature-based rules with **anomaly detection (AI/ML)** to catch novel attacks. |

---

### Summary Table: DoS Attack Types & Signature-Based Detection

| DoS Strategy               | Goal                            | Key Detection Signatures / Methods |
|---------------------------|----------------------------------|-------------------------------------|
| Resource consumption      | Overload CPU, memory, disk     | High CPU/memory/disk usage; process behavior logs |
| TCP SYN flood             | Exhaust connection pool        | TCP handshake patterns (SYN → SYN-ACK) with high volume |
| UDP/ICMP flooding        | Flood bandwidth or network     | Large volume of UDP/ICMP packets from one source |
| HTTP flood               | Overload web server            | High frequency of GET/POST requests; abnormal request rates |
| Configuration attacks    | Disable services or break config | Unexpected system state changes (e.g., service down, firewall disabled) |

---

### Final Thoughts
[[DoS]]
While **signature-based detection is powerful** for identifying known DoS attack patterns — such as SYN floods or HTTP request storms — it has critical gaps against:

- Newly emerging or polymorphic attacks  
- Distributed DDoS campaigns using botnets  
- Application-level logic exploits that consume resources silently  

✅ **Best Defense Strategy**:  
Use a **layered, hybrid approach** combining:  
- Signature-based detection (for known threats)  
- Behavioral analytics and AI-driven anomaly detection (to catch novel or stealthy attacks)  
- Rate limiting and traffic shaping at network and application layers  

This ensures comprehensive protection against both traditional and evolving Denial of Service threats.

