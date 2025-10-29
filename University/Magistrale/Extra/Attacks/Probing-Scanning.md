# Probing / Scanning

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
