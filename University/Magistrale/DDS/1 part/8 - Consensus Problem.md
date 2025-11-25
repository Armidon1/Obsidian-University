# Consensus Problem

#### Overview  
A group of processes must agree on a value that has been proposed by one of them (e.g., commit/abort of a transaction).  

This is an abstraction of a class of problems where processes start with their own opinion and then converge on one of them.  
It is a fundamental problem in distributed systems.

---

#### Consensus Example: The Generals’ Problem

![[Pasted image 20251023121728.png]]

*The generals must reach consensus on whether to attack or retreat.*

---

#### Consensus Definition

- A set of initial values ∈ {0, 1}.  
- Every process must decide the same value ∈ {0, 1} based on the initial proposals.

---

#### Consensus Protocol
![[Pasted image 20251023121747.png]]

---

#### Consensus Specification
![[Pasted image 20251023121814.png]]

- **Propose(v)** → Each process proposes a value `v`  
- **Decide(v')** → All correct processes must decide on the same value `v'`

---

#### FLP Impossibility Result  

> No algorithm can guarantee to reach consensus in an asynchronous system, even with one process crash failure.  

So the consensus blocks the flow in any situation. If we want mutal exclusion, consensus is one way. 

**Reference:**  
Fisher, Lynch, and Patterson (FLP result) — *Journal of the ACM*, Vol. 32, No. 2, April 1985. notice that some people spent all their life to study the consensus

---

### A Consensus Implementation in Synchronous Systems: Flooding Consensus
#### Basic Idea  
- Processes exchange their proposed values.  
- When all proposals from correct processes are received, a single value is selected.  

**Problem:**  
Due to failures, some values may be lost during communication. 

**Solution:**  
A value can only be selected if no failures occur during the entire communication phase. if someone failed and doesn't respond anymore, we simply exclude him

---

#### Flooding Consensus Algorithm (Step-by-step)
![[Pasted image 20251023122649.png]]
**Scenario Setup**  
- Processes: `p₁`, `p₂`, `p₃`  
- Correct processes: `{p₁, p₂, p₃}`  
- Crash event: `Crash(p₂)` → Correct set becomes `{p₁, p₃}`  

---

#### Execution Trace (Round-by-Round)

**Initial State (Round = 1)**  
- Decision = ⏊ (no decision yet)  
- `receivedFrom[0]` = {p₁, p₂, p₃}  
- `Proposals[0]` = {}  

**Propose values:**  
- `p₁ → Propose(5)`  
- `p₂ → Propose(3)`  
- `p₃ → Propose(7)`

**Round 1 Propagation:**

| Process | Action |
|--------|--------|
| From p₂ | Proposal[1] = {5, 3} (receivedFrom[1] = {p₂}) |
| From p₁ | Proposal[1] = {5, 3} (receivedFrom[1] = {p₂, p₁}) |
| From p₃ | Proposal[1] = {5, 3, 7} (receivedFrom[1] = {p₂, p₁, p₃}) |

**Decision at Round 1:**  
- `Decision₁ = 3` → **Decide(3)**
![[Pasted image 20251023124537.png]]

**Round 2 (after crash of p₂):**
![[Pasted image 20251023124622.png]]
![[Pasted image 20251023124706.png]]

| Process | Action |
|--------|--------|
| From p₁ | Proposal[2] = {5} (receivedFrom[2] = {p₁}) |
| From p₃ | Proposal[2] = {5, 7} (receivedFrom[2] = {p₁, p₃}) |

**Decision at Round 2:**  
- `Decision₂ = 3` → **Decide(3)**  

> *Note: The value 3 is still chosen due to convergence on common proposals.*

---

### Uniform Consensus Specification
![[Pasted image 20251023134520.png]]
As we can see, we removed the *agreement* property and implemented the *UC4: uniform agreement (we are not considering anymore only correct processes but we consider in general*. For doing so, we implement a way to take time.
#### Definition  
In uniform consensus:

- All processes decide the same value.  
- Decisions are made at the end of a round, not earlier.  
- No premature decisions.

**Formal Definition:**  
- **Propose(v)** → Each process proposes value `v`  
- **Decide(v')** → All correct processes agree on the same value `v'`, and this happens only after all rounds.

---

#### Does Flooding Consensus Satisfy Uniform Consensus?

❌ **No**, not as originally described.  

The original flooding consensus algorithm allows early decisions based on partial information, violating the *uniform agreement* property.  
It decides values in intermediate rounds (e.g., at round 1), while uniform consensus requires that all processes wait until the end of a complete communication phase to decide.

> 🔍 **Key Issue:** Early decision-making violates the requirement for synchronization and uniformity across correct processes.

---

### Uniform Consensus Implementation in Synchronous Systems
![[Pasted image 20251023134952.png]]
#### Algorithm Overview  
- Uses **Best-Effort Broadcast (BEB)** with Perfect Failure Detection.  
- No decisions are made until the end of a full communication round.  
- A "cleaned" set of proposals is maintained at each round, removing crashed processes.

**Key Features:**  
- Decisions happen only in final rounds.  
- Round-based propagation ensures completeness and consistency.  

What happens if the Perfect FDP doesn't work properly (so is not perfect but Eventually Perfect)? We use the uniform broadcast agreement, we need to switch the philosophy, work with majority (we will see it later)

---

#### Execution Example (With Crash)
![[Pasted image 20251023135010.png]]
**Initial State (Round = 1)**  
- Decision = ⏊  
- `receivedFrom` = {}  
- `Proposals` = {}

**Propose values:**  
- p₁ → Propose(5)  
- p₂ → Propose(3)  
- p₃ → Propose(7)

**Round 1 Propagation (after p₂ crashes):**

| Process | Action |
|--------|--------|
| From p₁ | Proposal[1] = {5} (receivedFrom[1] = {p₁}) |
| From p₃ | Proposal[1] = {5, 7} (receivedFrom[1] = {p₁, p₃}) |
![[Pasted image 20251023135041.png]]
**Round 2 Propagation:**

| Process | Action |
|--------|--------|
| From p₁ | Proposal[2] = {5, 7} (receivedFrom[2] = {p₁, p₃}) |

**Decision at Round 3:**  
- All correct processes (p₁ and p₃) have the same proposal set → **Decide(5)**

> ✅ Decision = 5 is consistent across all surviving correct nodes.  
> ✅ No early decisions → satisfies uniform consensus.

---

### Correctness and Performance Analysis

#### Correctness Properties:

| Property | Explanation |
|--------|-------------|
| **Validity** | The decided value must be one of the proposed values. |
| **Integrity** | The system preserves initial proposals via broadcast. |
| **Termination** | All correct processes eventually decide (due to perfect failure detection). |
| **Agreement** | All correct processes reach same decision using same function on proposals. |
| **Strong Completeness** | Crashed processes are removed from the correct set; no infinite waiting. |
| **Uniform Agreement** | All correct processes decide at round N with identical proposal sets. |

#### Performance:

| Scenario | Communication Steps | Messages Exchanged |
|--------|----------------------|--------------------|
| Best Case (No failures) | 1 round | O(N²) messages |
| Worst Case (n−1 crashes) | Up to N rounds | O(N³) total messages (for all correct processes) |

> ⚠️ Performance degrades with failure frequency due to multiple rounds and message replication.

---

### References

- C. Cachin, R. Guerraoui, L. Rodrigues. *Introduction to Reliable and Secure Distributed Programming*. Springer, 2011  
  - Chapter 5: Sections 5.1.1, 5.1.2, 5.2.1, 5.2.2  

---

> 💡 **Summary:**  
The FLP impossibility result shows that no deterministic consensus algorithm can guarantee termination in asynchronous systems with crash failures. In synchronous settings, flooding-based consensus can achieve agreement under perfect failure detection, but only if uniformity is enforced (i.e., decisions deferred to the end of each round). The proposed uniform consensus implementation ensures safety and liveness while avoiding premature decisions — making it suitable for practical distributed systems where failure patterns are predictable.

--- 

