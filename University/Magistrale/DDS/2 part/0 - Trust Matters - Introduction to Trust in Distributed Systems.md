# 0. Trust Matters - Introduction to Trust in Distributed Systems
**Tags:** #computer_engineering #distributed_systems #blockchain #trust_models #client_server

## 1. The Dominant Paradigm: Client/Server
The vast majority of online services we rely on today are built upon the **Client/Server Paradigm** ($C/S$). Even in modern distributed architectures, this fundamental relationship remains the standard.

### The "Black Box" Abstraction
From an engineering perspective, the most critical concept to grasp is the visibility of operations.
- **The Client:** Sends a request (Input).
- **The Server:** Processes the request and returns a response (Output).

**Crucially, the Server acts as a Black Box.**

![[Pasted image 20251129160850.png]]
> [!abstract] Visual Analysis
> **What to look at:** The diagram shows the Client interacting with a dark cube (the Server). Inside the cube, a sequence of actions ($A_1, A_2, \dots, A_n$) occurs hidden from the Client's view.
> **Meaning:** We only see the interface (Request/Response). We have **zero visibility** on the internal execution flow.

### Formal Definition of Server Actions
We can model the server's internal behavior as a sequence of discrete operations. The user *assumes* the server performs the set of expected actions:

$$A_{expected} = \{A_1, A_2, A_3, \dots, A_n\}$$

However, because the execution is remote and encapsulated, we simply **trust** that the actual execution matches the expected execution.

---
### So we have many consequence
- Do we have any formal proof that our money deposited in a bank are not used for diﬀerent proposes to the ones stated in the contract?
- Do we have any formal proof that our data are deleted from a server when requested?
- Do we have any formal proof our data are not delivered to third parties?
- Do we have any formal proof …

The answer is obviously NO.

---

## 2. The Consequence of Centralization
The "Black Box" nature of the server leads to significant consequences regarding data sovereignty and trust.

### The Unverified Questions
In a centralized $C/S$ architecture, we lack **formal proofs** for critical operations. As an engineer, you must ask:

- **Financial Integrity:** Do we have formal proof that money deposited in a bank is not used for purposes other than those stated in the contract?
- **Data Deletion:** Do we have formal proof that our data is physically deleted from a server when we request it?
- **Privacy:** Do we have formal proof that our data is not delivered to third parties?

> [!failure] Engineering Gap
> In current standard systems, the answer to all above questions is **NO**. We cannot mathematically verify these states from the client side.

### Market Centralization
The issue is amplified by the fact that the cloud infrastructure market is an oligopoly. A massive portion of global traffic relies on a few providers:
- **AWS:** ~30% market share.
- **Azure:** ~21% market share.
- **Google Cloud:** ~12% market share.

This means we are concentrating trust in very few, massive "Black Boxes".

---

## 3. The Current Trust Model: Reputation vs. Math
If we cannot verify the code running on the server, why do we use these services?

### Status Quo
The current system functions based on **Social and Legal Trust**, not Engineering Trust.
1. **Trust in Authority:** We rely on Certification Authorities (CAs) to audit processes.
2. **Reputation as Collateral:** We assume the provider respects the contract because losing their reputation would be too costly.... but in general, those guys are really good to mask their filthy work. 
3. **Incentives:** The primary incentive for honest behavior is the fear of losing future revenue, not the inability to cheat.

### The Mathematical Reality
In a centralized system, there is usually **no formal proof** (e.g., mathematical *with high probability* - w.h.p.) that the server is honest.

$$P(\text{Honesty}) \propto \text{Reputation}$$

> [!tip] Exam Focus
> Remember this distinction: In $C/S$, trust is **extrinsic** (based on reputation/contracts). In decentralized systems, we aim for trust to be **intrinsic** (based on math/cryptography).

---

## 4. Overcoming the Need for Trust
The core question of this course is: **"Can we overcome the need for trust in third parties intrinsic in centralized services?"**

### The Pivot Point
This is where **Blockchain** technology enters the discussion as a potential solution to the "Black Box" problem.
![[Thatsexactlythepoint.gif]]

> [!example] Concept
> Referencing the "That's exactly the point!" slide: The goal is not just to build a database, but to build a system where the "Server" cannot cheat because the validation is distributed.

### Comparative Analysis: Client/Server vs. Blockchain
As an engineer, you must avoid "hype". You must choose the right tool for the job.

**1. Client/Server ($C/S$):**
- **Pros:** Extremely efficient, scalable, standard.
- **Cons:** Requires trust in the central authority.
- **Use Case:** The vast majority of applications where trusted intermediaries are acceptable.

**2. Blockchain:**
- **Pros:** Removes the need for a trusted third party; provides formal verification of the process.
- **Cons:** Less efficient (generally slower and more expensive).
- **Use Case:** Specific scenarios where "Trustlessness" (not needing to trust a human/company) is superior to efficiency.

> [!abstract] Summary
> * **Awareness:** We must be aware of the consequences of employing $C/S$ (blind trust).
> * **Evaluation:** Blockchain is a viable alternative only when the cost of trust exceeds the cost of inefficiency.

---
