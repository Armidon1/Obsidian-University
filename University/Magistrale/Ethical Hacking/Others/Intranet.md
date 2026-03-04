# Intranet

### The Intranet: Technical Overview

At its core, an intranet is a private, isolated enterprise network built using standard internet protocols (TCP/IP, HTTP/HTTPS, FTP) to securely share corporate resources, host internal applications, and facilitate collaboration among authorized personnel.

While it mirrors the underlying technology of the public internet, its defining characteristic is strict access control and network isolation from external routing.

### Network Architecture

From a networking perspective, an intranet relies heavily on private IP address spaces (defined by RFC 1918, such as `10.0.0.0/8`, `172.16.0.0/12`, or `192.168.0.0/16`). These IP addresses are not routable on the public internet.

- **Infrastructure:** It consists of Local Area Networks (LANs) and Wide Area Networks (WANs) connected via internal routers, switches, and load balancers.
    
- **Internal Services:** It hosts bare-metal or virtualized servers, including web servers (IIS, Apache, Nginx) for internal portals, database servers (SQL, NoSQL), and file shares.
    
- **Perimeter Defense:** The boundary between the intranet and the public internet is strictly managed by edge routers, Next-Generation Firewalls (NGFW), and often a Demilitarized Zone (DMZ) where public-facing services (like web or email servers) sit isolated from the sensitive internal network.
    
- **Remote Access:** External authorized access is handled through VPN gateways or Reverse Proxies, utilizing protocols like IPsec or SSL/TLS to create encrypted tunnels straight into the internal network.
    

### The Cybersecurity Perspective

Historically, intranets relied on a "castle-and-moat" security model. Once a user or device bypassed the perimeter firewall (the moat), they were implicitly trusted inside the intranet (the castle). As a cybersecurity student, this is where your focus should lie, because this traditional model is highly vulnerable.

- **Lateral Movement:** If an attacker compromises a single internal endpoint (for example, through an email phishing payload), traditional intranets allow them to easily pivot. They can map the internal network, exploit internal vulnerabilities, and escalate privileges using protocols like SMB or RDP without crossing the perimeter firewall again.
    
- **Identity and Access Management (IAM):** Intranets rely on centralized identity providers, most commonly Microsoft Active Directory (AD) or LDAP. Internal authentication relies on protocols like Kerberos and NTLM. Compromising these protocols (via attacks like Pass-the-Hash or Golden Ticket) gives an attacker the "keys to the kingdom."
    
- **Insider Threats:** Because of implicit trust, malicious, compromised, or negligent employees have a much easier time accessing sensitive internal databases or introducing malware (like ransomware, which spreads rapidly across unsegmented intranets).
    
- **Zero Trust Architecture (ZTA):** Modern security engineering is actively dismantling the traditional intranet concept. ZTA assumes the intranet is already compromised. It requires strict, continuous authentication, least-privilege access, and network micro-segmentation for every application and data flow, regardless of whether the user is sitting in the corporate office or working remotely.
    
