# Consensus in Distributed Systems
**Tags:** #distributed_systems #consensus #blockchain #algorithms #fault_tolerance

## 1. Definition and Core Concept
The **Consensus Problem** is a fundamental challenge in distributed computing where a group of processes must agree on a specific value that has been proposed by one of them.

It serves as an abstraction for problems where processes start with differing opinions (initial values) and must converge on a single decision.
- **The Goal:** Every process has to decide the same value $\in \{0,1\}$ based on initial proposals.
- **Real-world Example:** Committing or aborting a transaction in a database , or deciding between "attack" or "retreat" in the Byzantine Generals Problem.


> [!abstract] The Shift: Trust vs. Algorithm
> In centralized systems, "Consensus" is trivial because the central database defines the truth. In distributed systems, we move from a **Black Box** (Trust in an authority) to a **White Box** (Trust in a distributed algorithm).

---

## 2. Formal Specifications (The Properties)
For a consensus algorithm to be considered correct, it must satisfy specific properties. These are divided into safety (nothing bad happens) and liveness (something good eventually happens).

### Regular Consensus Properties (Module 5.1)
1. **C1: Termination:** Every *correct* process eventually decides some value.
2. **C2: Validity:** If a process decides $v$, then $v$ was actually proposed by some process.
3. **C3: Integrity:** No process decides twice.
4. **C4: Agreement:** No two *correct* processes decide differently.

### Uniform Consensus Properties (Module 5.2)
In many systems (like Blockchain or banking), it is not enough for only "correct" (non-crashed) nodes to agree. If a node decides "Commit" and then crashes, the others must not decide "Abort".
- **UC4: Uniform Agreement:** No two processes (correct *or* faulty) decide differently.
* Properties UC1, UC2, and UC3 remain the same as C1-C3.

---

## 3. The FLP Impossibility Result
Before designing algorithms, we must understand the theoretical limits.
- **The Result:** No algorithm can guarantee consensus in an **asynchronous system** (where message delays are unbounded), even with just **one** process crash failure.
- **Implication:** We must assume a synchronous model (time bounds exist) or use failure detectors to solve consensus practically.

---

## 4. Consensus Algorithms (Synchronous Model)
We study algorithms working on weak models using a modular software stack: **Consensus** sits on top of **BestEffortBroadcast (BEB)** and a **Perfect Failure Detector (P)**.


### A. Flooding Consensus (Regular)
This algorithm aims for Regular Consensus (C1-C4).
- **Mechanism:** Processes exchange (flood) their known proposals every round.
- **Stopping Rule:** A process decides when the set of proposals it received in the current round is identical to the previous round (information has stabilized).
- **Performance:**
* **Best Case (No failures):** 1 round ($2N^2$ messages).
* **Worst Case ($N-1$ failures):** $N$ rounds ($N^3$ messages).

### B. Flooding Uniform Consensus (Uniform)
This algorithm satisfies Uniform Agreement (UC4).
- **The Constraint:** A process cannot decide early. Even if information stabilizes, it must wait to ensure *all* other processes have seen the decision before committing.
- **Mechanism:** It forces execution for **$N$ rounds** (where $N$ is the number of processes).
- **Decision:** The decision is made *only* at the end of round $N$.
- **Performance:** Always $N$ rounds and $O(N^3)$ messages.

> [!failure] Trade-off
> To achieve **Uniformity** (higher safety), we sacrifice **Performance** (we cannot stop early, even if the network is stable).

---

## 5. Consensus in Blockchain
In the specific context of Blockchain, Consensus solves the **ordering** problem to prevent **double spending**.

### Validation vs. Consensus
It is critical to distinguish these two steps:
1. **Validation (Local Check):**
* A validator checks if a transaction is consistent with protocol rules (e.g., valid signature, sufficient balance).
* This is a local action.
2. **Consensus (Global Agreement):**
* The network determines the **ordering** of events.
* If Alice sends coins to Bob and Charlie simultaneously, both are "Valid," but Consensus decides which one happened first to maintain a consistent history.

### Finality
- **Deterministic Finality:** Algorithms like PBFT or the **Uniform Flooding Consensus** provide instant/guaranteed finality once the decision step is reached.
- **Probabilistic Finality:** In Proof-of-Work (Bitcoin), finality is probabilistic; the deeper a block is, the less likely it is to be reversed.

#### See more in [[8 - Consensus Problem]] 
