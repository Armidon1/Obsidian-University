Previous lesson: [[1- Email Security]]

See the italian and enriched version: [[NETWORK SECURITY]]
# Network Security

Cyber Intelligence and Information Security (CIS Sapienza)

Lecturer: Leonardo Querzoni

📧 querzoni@diag.uniroma1.it

---

## Introduction

- No preventative shielding (like firewalls, VPNs, or access control lists) is 100% intrusion-proof. Prevention systems will always have gaps.
    
- **New attack techniques** emerge continuously, creating **zero-day exploits** that existing defenses cannot recognize.
    
- **Unexploited or _silent_ vulnerabilities** (bugs) may exist in software for years before being discovered.
    
- **Misconfigurations** (e.g., default passwords, open ports, improper permissions) and **malicious insiders** (trusted users with bad intent) are persistent risks that bypass traditional perimeter defenses.
    
- Because prevention _will_ eventually fail, **continuous monitoring** and **attack detection** are essential components of a robust security posture (Defense in Depth).
    

---

## Intrusion Detection

> “The process of monitoring the events occurring in a computer system or network and analyzing them for signs of intrusions — attempts to compromise confidentiality, integrity, availability, or to bypass security mechanisms.”
> 
> — NIST Definition

---

## Attacks

### Terminology

- **Attack:** An _attempt_ to intrude. It may be blocked by a firewall or other preventative measure and have no impact.
    
- **Intrusion:** A _successful_ attack. This means the attacker has bypassed defenses and caused a malicious, externally induced operational fault.
    

### Classification Criteria

Attacks can be categorized based on:

- **Type:** The goal of the attack (e.g., DoS, compromise).
    
- **Involved network connections:** Single vs. multiple connections.
    
- **Source:** A single IP vs. multiple distributed sources.
    
- **Environment:** The target (e.g., host, network, wireless).
    
- **Automation level:** Manual (human-driven) vs. automated (script/worm).
    

---

## Attack Types

### Denial of Service (DoS)

[[DoS]]

**Goal:** To disrupt or shut down a network, computer, or process, denying the use of resources to authorized users. This is an attack on **Availability**.

**Strategies:**

- **Consumption of scarce resources:**
    
    - **Bandwidth Consumption:** Saturating the network connection with junk traffic (e.g., UDP floods, ICMP floods).
        
    - **Network Connectivity Flooding:** Exhausting the system's ability to manage connections (e.g., a **SYN Flood** fills the connection state table).
        
    - **Other Resources:** Consuming all available CPU, memory, or disk I/O.
        
- **Destruction or alteration of configuration:** Changing routing tables or DNS records.
    
- **Physical destruction or alteration:** Physically damaging components.
    

---

### Probing / Scanning

[[Probing-Scanning]]

**Goal:** The _reconnaissance_ phase. An attacker attempts to identify valid IP addresses in a domain and collect information about them (e.g., open ports, running services, OS versions) to find potential vulnerabilities.

**Tools:** `IPsweep`, `Portsweep`, `nmap`

- **Noisy Scans:** Fast, aggressive scans are easy to detect (e.g., "this IP scanned 1000 ports in 3 seconds").
    
- **Stealthy Scans:** These are more challenging to detect as they are designed to fly under the radar (e.g., very slow scans, or scans using non-standard flags like a FIN scan).
    

---

### Compromises

[[Compromises]]

**Goal:** Breaking into a system to gain unauthorized or privileged access (e.g., a user shell or root/admin access). This is an attack on **Confidentiality** and **Integrity**.

#### Remote-to-Local (R2L)

[[R2L]]

An attacker with no account on a machine gains local access _from the network_.

- **Examples:** Password guessing (brute-force SSH), or exploiting a known vulnerability in a network-facing service (e.g., a buffer overflow in Sendmail, an RCE flaw in a web application).
    

#### User-to-Root (U2R)

[[U2R]]

An attacker who already has a low-privilege local account _escalates_ their privileges.

- **Examples:** Exploiting a bug in the operating system kernel or a program that runs with `setuid` root privileges.
    

---

### Malware-Based Attacks

[[Malware-Based Attacks]]

#### Viruses

[[Virus]]

- Malicious code that attaches itself to other legitimate programs.
    
- Requires **human interaction** (e.g., running the infected program) to spread.
    

#### Worms

[[Worms]]

- **Self-replicating** programs that aggressively spread through a network by exploiting vulnerabilities.
    
- **No human interaction** is needed to propagate.
    
- Spreads via:
    
    - Direct network connections (e.g., the Slammer worm).
        
    - Email or file sharing.
        
    - Hybrid mechanisms.
        

#### Trojan Horses

[[Trojan]]

- Malicious, security-breaking software that is **disguised as something benign** (e.g., a game, a utility).
    
- Relies on social engineering; users are tricked into installing and running them voluntarily.
    
- A common payload is a **RAT (Remote Access Trojan)**.
    

#### Rootkits

[[Rootkits]]

- Software designed to take full (administrator-level) control of a machine while **actively hiding its own presence**.
    
- They hook into the operating system (or kernel) to hide their files, processes, and network connections from security tools.
    
- They often open up a **backdoor** to allow a hacker to take full control of the system.
    

---

## Attack Characteristics (Classification Recap)

### By Network Connections

- **Multiple connections:** Typical for [[DoS]] attacks or large-scale scans.
    
- **Single connection:** Often used for a specific exploit or [[Compromises]].
    

### By Source

- **Single source:** A typical port scan from one attacker's IP.
    
- **Multiple sources:** A **Distributed Denial of Service ([[DDoS]])** attack, which uses a _botnet_ of many compromised machines to attack a single target.
    

### By Environment

- **Host intrusion:** Targeting a single server or workstation.
    
- **Network intrusion:** Targeting infrastructure like routers or switches.
    
- **P2P environments:** Targeting peer-to-peer protocols.
    
- **Wireless networks:** Targeting Wi-Fi, Bluetooth, etc.
    

### By Automation Level

- **Automated:** Use automated tools (like worms or scanners) that probe the internet with no human intervention.
    
- **Semi-automated:** An attacker uses automated scripts for scanning but then manually analyzes the results and launches the final exploit.
    
- **Manual:** Involve manual scanning and exploitation. These are not frequent but are usually more dangerous and harder to detect, as a human attacker can adapt to defenses in real-time.
    

---

## Monitoring for Attacks

A simple attack may impact several subsystems, leaving a trail of evidence across routers, firewalls, proxies, and workstations.

![[Pasted image 20251029134610.png]]

Monitoring data is generated by virtually all IT systems across the entire network infrastructure.

![[Pasted image 20251029134622.png]]

### Data Sources for Monitoring

There are three primary sources of data for intrusion detection:

1. **Network flows**
    
2. **System and event logs**
    
3. **Full packet capture (FPC)**
    

### 1. Network Flows

Network flows are **metadata** records of network communication sessions. Think of them as a "phone bill" for your network: they show _who_ talked to _whom_, for _how long_, and _how much_ data was sent, but **NOT the actual content (payload)** of the conversation.

**5-Tuple Identification (The Key Fields):**

1. Source IP Address
    
2. Destination IP Address
    
3. Source Port
    
4. Destination Port
    
5. Protocol (e.g., TCP, UDP, ICMP)
    

**Additional Data Also Captured:**

- Start and End Time (duration)
    
- Number of Bytes / Packets transferred
    
- TCP Flags (providing session state like SYN, ACK, FIN, RST)
    
- Autonomous System (AS) Number (for tracing external connections)
    

---

### 2. Event / System Logs

These are text-based records of activities generated by all IT assets, providing the "ground truth" of what happened on a specific device.

- **Generated by:**
    
    - Network appliances (firewalls, routers, switches)
        
    - Servers (e.g., Windows Event Logs, Linux `/var/log/syslog`)
        
    - Hosts (desktops, laptops)
        
    - Applications (e.g., web server access logs, database error logs)
        
- They contain crucial information, such as failed authentication attempts, system errors, or application-level commands.
    

---

### 3. Full Packet Capture (FPC)

FPC means capturing and storing the **entire packet**, including the actual data **payload**.

**Advantages:**

- This is the ultimate tool for **digital forensics**.
    
- It allows analysts to literally **reconstruct the attack** step-by-step, analyze malware payloads, or extract encryption keys.
    

**Limitations (Why it's not used everywhere):**

- **Massive Storage Requirements:** Storing all payloads for an enterprise is extremely expensive.
    
- **Performance Overhead:** Requires high-speed, specialized hardware to capture traffic at line rate without dropping packets.
    
- FPC is typically deployed **selectively** (e.g., only capturing packets that trigger an alert) or on very high-value, low-volume network segments.
    

---

## Intrusion Detection Systems (IDS)

An IDS is a system that automates the monitoring and analysis process.

### General Framework

![[Pasted image 20251029135049.png]]

**Core Components & Flow:**

1. **Monitored System:** The network or host being protected.
    
2. **Sensor:** Collects data (flows, logs, packets) from the monitored system and generates **Events** (a record of an observation with a timestamp).
    
3. **Analysis Engine:** The "brain" of the IDS. It processes events, compares them against the **Knowledge Base**, and generates **Alarms** if a threat is found.
    
4. **Knowledge Base:** A database of rules, signatures, or behavioral models that define what is "normal" or "malicious."
    
5. **Dashboard:** A user interface where a human security operator monitors alarms.
    
6. **Response Component:** An optional module that can take **Actions** (e.g., send an email, block an IP) based on a pre-defined **Configuration** when an alarm is triggered.
    

Security operators rely on the IDS output, but IDSs are not perfect. Operators must investigate alarms (which could be **False Positives**) by looking at the raw logs. However, the most dangerous failure is a **False Negative** (a real attack that the IDS missed), which is why IDS reliability is paramount.

---

### Desired IDS Characteristics

A good IDS must balance three main characteristics:

#### 1. Detection KPIs (Key Performance Indicators)

IDS accuracy is a statistical trade-off:

- **True Positive (TP):** A real attack occurs, and the IDS correctly fires an alarm. (Good)
    
- **False Positive (FP):** No attack occurs, but the IDS incorrectly fires an alarm. (Bad - causes alert fatigue).
    
- **True Negative (TN):** No attack occurs, and the IDS correctly stays silent. (Good)
    
- **False Negative (FN):** A real attack occurs, and the IDS _misses it_. (Very Bad - a complete failure of detection).
    

**Key Metrics:**

- **Detection Rate (True Positive Rate, TPR):** `TP / (TP + FN)`
    
    - _Question:_ Of all the real attacks, what percentage did we catch?
        
- **False Alarm Rate (False Positive Rate, FPR):** `FP / (FP + TN)`
    
    - _Question:_ Of all normal events, what percentage did we incorrectly flag as an attack? (We want this to be 0).
        
- **Accuracy:** `(TP + TN) / Total Events`
    
    - _Question:_ Overall, what percentage of the IDS's decisions were correct?
        
- **Precision:** `TP / (TP + FP)`
    
    - _Question:_ Of all the alarms that fired, what percentage were real attacks? (High precision means less time wasted on false positives).
        

_Real-World Note:_ These metrics are hard to measure. In a real network, you never know the true number of "Total Attacks" (especially the ones you missed, FN). Therefore, an IDS must be fine-tuned for its specific environment (e.g., a hospital's needs are different from a bank's).

ROC Curve:

The Receiver Operating Characteristics (ROC) curve visualizes the trade-off between the Detection Rate (TPR) and the False Alarm Rate (FPR).

![[Pasted image 20251029140336.png]]

- A **Perfect IDS** is a single point in the top-left corner (100% detection, 0% false alarms).
    
- **Random Prediction** (guessing) is the 45-degree diagonal line.
    
- A good IDS has a curve that bends as close to the top-left corner as possible. In general, to increase the detection rate (move up), you must often accept a higher false alarm rate (move right).
    

#### 2. [[Timeliness]]

- This is the total delay from the start of an intrusion to the alert being generated.
    
- It includes all processing time, network propagation time, and the analysis/response time. We want this to be as low as possible.
    

#### 3. [[Fault Tolerance]]

- The IDS itself is a target. An adversary knows it exists and will try to make it inefficient or crash it.
    
- The IDS must be robust against attacks and able to recover quickly.
    
- **Example Attack:** A DoS attack on the IDS, where an attacker floods it with obvious, low-level alerts to hide a real, stealthy attack in the "noise."
    

---

## IDS Classification

IDSs can be categorized based on several key properties:

1. **Monitored system** (Where it looks: Host vs. Network)
    
2. **Detection methodology** (How it thinks: Misuse vs. Anomaly)
    
3. **Time aspects** (When it works: Online vs. Offline)
    
4. **Architecture** (Where it runs: Centralized vs. Distributed)
    
5. **Reaction type** (What it does: Passive IDS vs. Active IPS)
    

---

### 1. Monitored System

#### Host-Based IDS (HIDS)

A HIDS is a software agent installed directly on a single host (a server, workstation) that monitors _internal_ events.

- **Monitors:**
    
    - System logs (e.g., auth.log)
        
    - Running processes
        
    - File access and filesystem integrity (e.g., FIM - File Integrity Monitoring)
        
    - Configuration changes
        
    - System calls
        
- **Techniques:** Code analysis, sandbox-based execution, log analysis.
    
- **Pros:**
    
    - **Can see inside encrypted traffic** (it runs on the host _after_ decryption).
        
    - Highly granular insight into what happened on that specific host.
        
- **Cons:**
    
    - Can have a negative performance impact (overhead) on the host.
        
    - Lacks a wider network context (it only sees what's happening on its own host).
        

**Modern Evolution (EDR):** The active evolution of HIDS is **EDR (Endpoint Detection and Response)**. EDR systems don't just detect threats; they also provide tools to _respond_ (e.g., remotely isolate the host from the network, kill a malicious process, or delete a file).

#### Network-Based IDS (NIDS)

A NIDS is a device (physical or virtual) that monitors network traffic on a specific network segment.

- **Monitors:** Network packets at various layers:
    
    - Application (HTTP, SMTP, DNS)
        
    - Transport/Network (TCP, UDP, IP)
        
    - Lower layers (MAC, ARP)
        
- **Deployment:**
    
    - **Passive:** The NIDS monitors a _copy_ of the traffic (from a network TAP or switch's SPAN port). It is "read-only" and can only **Detect**.
        
    - **Inline:** The NIDS sits directly in the path of traffic. It can actively block malicious packets, making it an **Intrusion Prevention System (IPS)**.
        
- **Fundamental Limitation:** A NIDS **cannot inspect encrypted traffic** (e.g., SSL/TLS, SSH). The payload is unreadable. The only workaround is a **TLS Proxy** (or TLS Interception), which performs a "man-in-the-middle" decryption, inspection, and re-encryption.
    

#### Log-Based IDS

- A specialized IDS that only monitors the logs of specific applications (e.g., a Database Management System (DBMS), Content Management System (CMS), or accounting software).
    
- It has high granularity for that application but requires complex tuning.
    

#### Wireless IDS (WIDS)

- Monitors the wireless medium (802.11) for attacks.
    
- **Challenges:**
    
    - The broadcast medium is inherently less secure.
        
    - It's hard to physically locate attackers.
        
    - Continuously scanning multiple channels requires expensive, multi-radio hardware.
        

#### Multi-Level IDS (Correlated IDS)

- A hierarchical system that aggregates alerts from many other IDS layers (HIDS, NIDS).
    
- An analysis engine (like a SIEM) correlates these low-level alerts to find complex, large-scale attack patterns.
    

---

### 2. Detection Methodology

#### Misuse Detection (Signature-Based)

This methodology is based on knowledge about **previously known attacks**.

- A model of _abnormal_ behavior (a "signature") is defined.
    
- The IDS compares events to this model. If there is a match, an alarm is raised.
    
- All other behavior (anything not matching a "bad" signature) is considered normal and ignored.
    

**Techniques:**

- **Signature-based IDS:**
    
    - Works like an antivirus, using a database of "fingerprints" of known attacks (e.g., a specific string, a binary pattern).
        
    - **Tools:** _Snort_ or _Suricata_ (see also [[Signatures (Cybersecurity)]]).
        
    - **Cons:** Unable to detect new (zero-day) attacks or significant variations of old attacks. The signature DB must be constantly updated.
        
- **Rule-based systems:**
    
    - Use explicit "if...then" conditions to capture attacks (e.g., "IF packet is from X AND port is Y THEN block").
        
    - Can leverage high-performance rule engines.
        
- **State transition analysis:**
    
    - Models an attack as a finite state machine.
        
    - States correspond to different states of a system or protocol.
        
    - Transitions are triggered by events.
        
    - If the machine reaches a state that is flagged as a security threat, an alarm is raised.
        
- **Machine-Learning based (Supervised):**
    
    - A model is trained on a massive, _labeled_ dataset (containing examples of "normal" and "intrusive" events).
        
    - Can be very accurate at detecting known attacks and their variations.
        
    - **Algorithms:** Decision trees, neural networks, Support Vector Machines (SVMs).
        
    - **Problems:**
        
        - **Marketing vs. Reality:** Many products are sold as "AI-powered" but may be simple heuristics.
            
        - **Explainability:** It's often hard to know _why_ a complex model (like a neural net) flagged an event, making it difficult to triage false positives.
            
        - **Ambiguity:** The term "AI" is broad and can mean anything from simple classifiers to complex deep learning.
            

#### Anomaly Detection

This methodology is based on knowledge about the **normal system behavior**.

- A baseline model of "normal" is built.
    
- Everything that _departs_ (deviates) from this model is flagged as a potential attack.
    
- **Pros:** Can detect novel (zero-day) attacks.
    
- **Cons:** Prone to high false-positive rates (legitimate but unusual activity can trigger an alarm).
    

**Challenges:** Anomaly detection is very hard to develop. It requires modeling an extremely detailed system. Furthermore, "normal" behavior changes over time (**model drift**). By the time a model is trained, the system may have already evolved, making the model obsolete.

**Approaches:**

- **Programmed:** The system is configured with _fixed_ behavioral models.
    
    - **Default Deny:** A very accurate model of "expected" behavior. Only modeled states are allowed.
        
    - **Descriptive Statistics:** Uses simple statistics, rules, and thresholds (e.g., "CPU usage should not exceed 90% for 5 minutes").
        
- **Self-learning:** The IDS automatically builds a model representing "normal" behavior by observing the system.
    
    - **Non-time series:** Stochastic modeling that does not consider time (e.g., rule-based or statistical models).
        
    - **Time series:** The model _does_ consider the correlation between events over time (e.g., Hidden Markov Models (HMM), Neural Networks).
        
- **Rule-based (for anomaly):**
    
    - Defines the _normal_ behavior with a set of rules (e.g., "This user should only log in from 9-5").
        
    - When a rule is broken, an attack is suspected.
        
- **Statistical:**
    
    - Monitors behavior by measuring variables over time (e.g., in moving time windows).
        
    - Detects when thresholds are exceeded (e.g., 3 standard deviations from the average).
        
    - **Outlier Detection:** A key technique. Data points are modeled using a distribution, and points that fall far outside this distribution are flagged as outliers.
        
- **Distance-based:**
    
    - An alternative to statistical modeling.
        
    - Detects outliers by computing distances between data points in a multidimensional space.
        
    - Can be based on **clustering** (points far from any cluster) or **density** (points in a low-density neighborhood).
        
- **Profiling:**
    
    - A profile characterizing the _normal execution_ of protocols and services is generated.
        
    - Any deviation from this profile (e.g., an HTTP request that doesn't look like a normal web request) is considered suspicious.
        
- **Immune System-Inspired:**
    
    - A specific profiling method. Small patterns of normal behavior (e.g., sequences of system calls) are collected.
        
    - If a new interaction presents a pattern that has never been seen before, an alarm is fired.
        

#### Compound Detection

A hybrid approach that bases its functioning on models for _both_ normal and abnormal behavior.

- Events are compared to both models.
    
- The relative distance of an event from the two models is used to classify it as an attack or normal.
    

### Detection Methodology Recap

![[Pasted image 20251029153606.png]]

---

### 3. Time Aspects

- **On-line (Real-time) tools:**
    
    - Can check streams of incoming data as they arrive.
        
    - Useful to timely detect attacks and react promptly (required for an IPS).
        
    - Requires strong processing capabilities (e.g., stream processors, high-performance rule engines).
        
    - Cannot easily work on events that are out of sync (like batched statistical reports).
        
- **Off-line tools:**
    
    - Perform post-analysis of audit data (logs, FPC files).
        
    - Best for reporting or deep digital forensics.
        
    - Performance is rarely an issue, so more complex and comprehensive analysis can be performed.
        

|**Type**|**Description**|
|---|---|
|**Online IDS**|Real-time detection using stream processing.|
|**Offline IDS**|Post-analysis of logs for complex insights.|

---

### 4. Architecture

- **Centralized:**
    
    - The analysis of data is performed in a fixed number of locations (e.g., one central server), independent of how many hosts are monitored.
        
    - **Pros:** Simplifies configuration and management.
        
    - **Cons:** Less fault tolerant (it's a single point of failure) and less scalable.
        
- **Distributed:**
    
    - The analysis is performed in many locations, often proportional to the number of hosts (e.g., agent-based IDSs).
        
    - **Pros:** Graceful degradation in case of failures; easier to customize for ad-hoc duties.
        
    - **Cons:** Complex configuration and management.
        

|**Type**|**Description**|
|---|---|
|**Centralized**|Easier to manage, less scalable, single point of failure.|
|**Distributed**|Uses multiple analysis nodes, fault-tolerant, customizable.|

---

### 5. Reaction Type

This defines the difference between a passive **IDS (Detection)** and an active **IPS (Prevention)**.

- **Passive Reaction (IDS):** Typically, IDSs only report alarms to human administrators or a SIEM. The most common "reaction" is to increase the sensor sensitivity to gather more data.
    
- **Active Reaction (IPS):** The system can take automatic, non-destructive actions.
    

![[Pasted image 20251029154241.png]]

![[Pasted image 20251029154301.png]]

|**Action**|**Description**|**Use Case**|
|---|---|---|
|**Dropping Malicious Packets**|Blocks specific malicious packets from reaching their destination.|Blocking malware, SQL injection, DDoS.|
|**Blocking/Terminating Connections**|Terminates suspicious connections (e.g., by sending reset packets).|Stopping brute-force attacks, port scanning.|
|**Blocking IP Addresses (Blacklisting)**|Blocks all future traffic from a specific IP address.|Preventing repeated attacks from known malicious IPs/botnets.|
|**Rate Limiting (Throttling)**|Limits the rate of certain types of traffic (e.g., new connections).|Mitigating DDoS attacks, brute-force login attempts.|
|**Traffic Rerouting (Honeypots)**|Redirects malicious traffic to a **honeypot** (a decoy system).|Gathering attack intelligence while protecting critical systems.|
|**Modifying Attack Payloads**|Alters or neutralizes parts of malicious payloads (e.g., stripping a command).|Preventing buffer overflow attacks.|

---

## Network Segmentation and Zero Trust

### The Traditional Model: "Castle and Moat"

- The typical network design is based on the concept of **"internal trust"**.
    
- The world is divided into two zones: "external" (untrusted) and "internal" (trusted).
    
- The transfer of data is only possible through controlled checkpoints (the **firewall**, or "moat").
    
- **Weakness:** This model has a hard shell but a soft, chewy center. If an attacker breaches the barrier (e.g., via a phishing email), **nothing stops them from moving freely inside the network** (this is called **lateral movement**).
    

---

## Zero Trust Architecture

**Principle:** A modern security model that operates on the principle of **"Never trust, always verify."**

It assumes no user or device should be trusted by default, even if it is "inside" the network perimeter.

### Core Principles

- **Verify Explicitly:** Continuously validate access for every request using all available data points (identity, location, device health, service).
    
- **Use Least Privilege Access:** Restrict user permissions to the _minimum_ necessary for their job, reducing the potential blast radius if credentials are compromised.
    
- **Assume Breach:** Design the network to _contain_ potential breaches and minimize their impact. Don't just try to keep attackers out; assume they are already in.
    

### Key Components of a Zero Trust Architecture

- **Identity and Access Management (IAM):** Manages user identities and enforces strong authentication and authorization.
    
- **Device Security:** Monitors device health (e.g., "is this device patched and running antivirus?").
    
- **Network Segmentation:** (See below) Breaks the network into small zones to limit lateral movement.
    
- **Data Protection:** Secures data itself (e.g., via encryption) and enforces data privacy.
    
- **Continuous Monitoring and Analytics:** Tracks user and device behavior for anomalies.
    

### Benefits

- **Enhanced Security:** Limits access and minimizes the impact of a breach.
    
- **Reduced Attack Surface:** There is no single "trusted" internal network to attack.
    
- **Supports Remote Work and Cloud:** Designed for modern, distributed environments.
    
- **Compliance and Data Privacy:** Helps meet regulatory requirements with granular controls.
    

---

## Network Segmentation Strategies (Implementing Zero Trust)

### What Is Network Segmentation?

A security strategy that divides a network into smaller, isolated protection domains (segments). It requires implementing controls (like firewalls) on the borders that link these segments.

**Advantages:**

- **Hampers lateral movement** for an attacker.
    
- **Reduces the attack surface** and limits potential damage.
    
- **Allows more granular monitoring** and management of traffic.
    
- **Helps meet regulatory requirements** by isolating sensitive data (e.g., a PCI segment for credit cards).
    

---

### Physical Segmentation

- Works at the hardware level, cutting the network into physically separate chunks (e.g., different switches, different rooms).
    
- The ultimate example is an **"air-gapped" network** with no physical connection to other networks.
    
- **Pros:** Maximum security and isolation.
    
- **Cons:** Extremely inflexible, expensive, and difficult to manage.
    

### Logical Segmentation

- Works at the software level, creating software-defined boundaries on shared hardware.
    
- **Pros:** Much more flexible than physical segmentation; allows for dynamic, centralized control (e.g., Software-Defined Networking - SDN).
    
- **Cons:** Can be vulnerable to software bugs that break security guarantees.
    

### Microsegmentation

- A very fine-grained approach that applies segmentation at the **individual application or workload level**.
    
- **Example:** Instead of a "Web Server" segment, _each web server_ is its own segment and is only allowed to talk to its _specific database_ on its _specific port_, and nothing else.
    
- **Pros:** The best option for implementing Zero Trust; maximum flexibility; supports hybrid and cloud environments.
    
- **Cons:** Can lead to complex policy management; potential for overhead.
    

#### Microsegmentation Approaches

- **Network-Based:** Uses IP addresses or subnets.
    
- **Application-Based:** Policies are based on application-level identifiers.
    
- **User-Based:** Controls access at the user level (e.g., "Alice" can access the finance app).
    
- **Process-Based:** Policies are based on _specific processes_ within a workload (e.g., `apache.exe` can talk on port 80, but `powershell.exe` cannot).
    

---

## VLANs (Virtual LANs)

VLANs are the most common technology for implementing **logical segmentation**.

- They work at **OSI Layer 2** (Data Link).
    
- They are implemented by nearly all commercial network switches.
    
- They allow a single physical network infrastructure to be split into multiple _logical_ broadcast domains.
    

As shown in the diagram, devices on VLAN 10 (HR) and VLAN 20 (Finance) can be plugged into the same physical switch but cannot communicate directly.

![Immagine di VLAN trunks connecting multiple switches](https://encrypted-tbn3.gstatic.com/licensed-image?q=tbn:ANd9GcQvb_suXg-D_8ZxZ4ZdAtcztu4hx8Kym_mv73as_Ma3f0fUZw-xSRmP99OX9rvoHAb6ok4FKxummS_QrWGkKqmXZqxW1jIHw92d4drJepyzQULji64)

Shutterstock

To communicate _between_ VLANs (e.g., for the HR Clerk to access the HR DB Server), traffic must pass through a **Layer 3 device (a router)**. This router acts as the checkpoint where Access Control Lists (ACLs) are applied to enforce security rules.

---

## SIEM – Security Information and Event Management

### The Problem: Data Overload

A modern network has hundreds of devices (firewalls, IDS, servers, switches), all generating thousands of logs and alerts.

![[Pasted image 20251029134622.png]]

A single attack creates a confusing trail of data across all these systems.

![[Pasted image 20251029134610.png]]

### The Solution: SIEM

A **Security Information and Event Management (SIEM)** system solves this problem.

- It is a layer of management and analysis positioned _above_ all existing security controls.
    
- It **connects and unifies** information from all these pre-existing systems, allowing it to be analyzed and **correlated** from a single interface.
    

### Purpose and Functions

The ultimate goal of a SIEM is to "distill" low-level information (logs, flows) into high-level, **actionable intelligence**.

- **Functions:**
    
    - **Aggregate:** Collect and combine logs and events from all sources.
        
    - **Correlate:** Find hidden relationships between events (e.g., "a failed login on the server, _followed by_ a port scan from the same IP, _followed by_ a successful login on another machine" = a multi-stage attack).
        
    - **Support:** Enable incident detection, rapid response, and compliance reporting.
        

### Key Goals

- **Unified Security Visibility:** A single pane of glass for security across the entire organization.
    
- **Incident Detection and Response:** Helps detect, prioritize, and respond to threats in real time.
    
- **Compliance and Reporting:** Automates log collection and reporting needed for regulations (e.g., PCI, HIPAA, GDPR).
    

---

## References

- NIST SP 800-94 — _Guide to Intrusion Detection and Prevention Systems (IDPS)_, 2007
    
- Lazarevic et al., _Intrusion Detection: A Survey_, in _Managing Cyber Threats_, Springer, 2005
    
- Moore et al., _The Spread of the Sapphire/Slammer Worm_, 2003
    
- Powell & Stroud, _MAFTIA Project Deliverable D2_, IBM Zurich, 2001