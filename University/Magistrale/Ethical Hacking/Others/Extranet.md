# Extranet
### The Extranet: Technical Overview

An extranet is an extension of an enterprise's intranet that is securely opened up to trusted third parties—such as vendors, suppliers, partners, or major clients. While an [[Intranet]] is strictly for internal employees, an extranet facilitates B2B (Business-to-Business) collaboration, joint ventures, and supply chain integration.

You can think of it as a controlled bridge between two or more separate organizations, allowing them to share specific data and applications without exposing their entire internal networks to one another.

### Network Architecture

Architecturally, an extranet connects disparate corporate networks over a wide area, usually traversing the public internet using secure, encrypted protocols.

- **Secure Tunnels:** The backbone of an extranet is typically a Site-to-Site VPN (using [[IPsec]]) or dedicated leased lines. This creates an encrypted conduit over the public internet, securely linking the host organization's edge router to the partner's edge router.
    
- **The [[DMZ]] (Demilitarized Zone):** Instead of granting raw network access to the core intranet, external partners are usually restricted to specific web applications or file-sharing services hosted within the DMZ. The inner firewall tightly controls what data these DMZ applications can query from the core internal databases.
    
- **Federated Identity:** Rather than the host company creating and managing new local accounts for every external partner, modern extranets use Identity Federation (via protocols like SAML 2.0 or OAuth/OIDC). This allows partners to authenticate using their _own_ company's credentials. The partner's Identity Provider (IdP) vouches for the user, and the host's system grants access based on that trusted token.
    

### The Cybersecurity Perspective

From a cybersecurity standpoint, building an extranet fundamentally expands an organization's attack surface. You are explicitly extending a level of trust to an entity that is entirely outside your administrative control.

- **Third-Party / Supply Chain Risk:** This is the most critical threat vector. If a partner has a weak security posture and gets compromised, attackers can hijack that trusted extranet connection to infiltrate your network. The infamous 2013 Target data breach occurred exactly this way: attackers stole credentials from a third-party HVAC vendor that had extranet access to Target's billing systems.
    
- **Strict Segmentation:** An extranet connection must never have flat, unhindered access to the core intranet. Firewalls must enforce strict Access Control Lists (ACLs) that implement the principle of least privilege—limiting partner traffic _only_ to the specific servers, protocols, and ports required for their business function.
    
- **Data Loss Prevention (DLP):** Because an extranet exists specifically to flow data outside the organization, DLP solutions are heavily utilized on these boundaries. They monitor traffic to ensure that highly sensitive internal data (like PII or proprietary source code) isn't accidentally or maliciously exfiltrated through the partner channel.
    
- **API Security:** Extranets increasingly rely on APIs for automated system-to-system communication (e.g., a supplier's inventory system talking to a retailer's ordering system). Securing these APIs against injection attacks, Broken Object Level Authorization (BOLA), and rate-limiting abuse is a major focus for security engineers.
    

