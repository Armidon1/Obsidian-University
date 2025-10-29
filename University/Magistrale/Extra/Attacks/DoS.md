# Denial of Service (DoS)

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

Let me know if you’d like a real Snort rule example, a visual flowchart, or integration with SIEM/EDR tools! 🛡️📊