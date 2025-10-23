# Broadcast Communications

---

## Recap: What We Know Up to Now

- Define a system model and specify a problem or an abstraction in terms of **safety** and **liveness**
    
- **Point-to-point communication abstractions**
    
    - Fair-loss, stubborn, or perfect links
        
- **Timestamping events**
    
    - Physical clocks
        
    - Logical clocks
        
- **Handling failures**
    
    - Failure detector
        
    - Leader election
        

> Up to now, the focus has been on interactions between two processes (like in a client/server environment).

---

## Communication in a Group: Broadcast

|Scenario|Type|
|---|---|
|No Failures|—|
|Crash Failures|—|

---

## Best Effort Broadcast (BEB)

### Specification

```
BEB
Broadcast(msg)
Deliver(msg)
```

### Implementation

**System Model:**

- Asynchronous system
    
- Perfect links
    
- Crash failures
    

**Algorithm:**

```
BEB_Broadcast(m)
  → pp2pSend(m)

BEB_Deliver(m)
  ← pp2pDeliver(m)
```

### Correctness Properties

- **Validity:** Guaranteed by reliable delivery of perfect links and sender broadcasting to all.
    
- **No Duplication:** Ensured by perfect links and message uniqueness.
    
- **No Creation:** Ensured by perfect link properties.
    

---

### Observations on BEB

- Ensures delivery as long as the sender does not fail.
    
- If sender fails, processes may disagree on delivery.
    

---

## (Regular) Reliable Broadcast (RB)

### Specification

Same as BEB, plus **liveness (agreement)** property.

```
RB
RB_Broadcast(msg)
RB_Deliver(msg)
```

---

### BEB vs RB

|Scenario|Result|
|---|---|
|Satisfies BEB but not RB|**Agreement property violated**|
|Satisfies RB|**All processes agree on message delivery**|

---

## (Regular) Reliable Broadcast (RB)

### Implementation in Synchronous Systems

```
RB_Broadcast(m)
RB_Deliver(m)
```

Uses:

- BEB
    
- Perfect Failure Detector (P)
    
- Crash(pi)
    

> Algorithm is _lazy_: retransmits only when necessary.

---

### Performance of Lazy RB Algorithm

|Case|Messages per RB|
|---|---|
|Best|1 BEB message|
|Worst|n−1 BEB messages (with n−1 failures)|

---

### Implementation in Asynchronous Systems

> Algorithm is _eager_: retransmits every message.

**Performance:**  
Best = Worst = n BEB messages per RB.

---

## Uniform Reliable Broadcast (URB)

### Specification

> The set of messages delivered by a correct process is a **superset** of those delivered by a faulty one.

```
URB
URB_Broadcast(msg)
URB_Deliver(msg)
```

**Property:** Agreement on a message delivered by _any_ process (crashed or not).

---

### BEB vs RB vs URB

|Comparison|Notes|
|---|---|
|BEB|Works if sender is correct|
|RB|Ensures agreement among correct processes|
|URB|Ensures uniform agreement (even with crashes)|

---

## URB Implementation in Synchronous Systems

Uses:

- BEB
    
- Perfect Failure Detector (P)
    
- Crash(pi)
    

Algorithm tracks:

- **Delivered**
    
- **Pending**
    
- **Acknowledgments**
    
- **Correct process set**
    

---

## URB Implementation in Asynchronous Systems

> Requires a **majority of correct processes**.

Uses BEB for underlying communication.

---

## Summary of URB

- Exists for **synchronous systems** (with perfect failure detector)
    
- Exists for **asynchronous systems** (with majority of correct processes)
    
- Open question:
    
    > Can we implement URB for _partially synchronous systems_ with _eventually perfect failure detectors_ and **no majority assumption**?
    

---

## Probabilistic Broadcast

### Characteristics

- Message delivered **99%** of the times
    
- **Not fully reliable**
    
- **Large & dynamic groups**
    
- Acknowledgments make reliable broadcast **not scalable**
    

---

### Ack Implosion & Ack Tree

**Problems:**

- High overhead for acknowledgment tasks
    
- Maintaining tree structure is complex
    
- Still limited scalability
    

**Solutions:**

- Hierarchical (tree-based) communication
    
- Randomized (epidemic/gossip) dissemination
    

---

## Probabilistic Broadcast (PbB)

```
PbB
Pb_Broadcast(msg)
Pb_Deliver(msg)
```

---

## Gossip Dissemination

- A process sends a message to **k randomly chosen processes**
    
- Each receiver forwards the message to **k random processes**
    
- Repeats for **r rounds**
    

---

## Eager Probabilistic Broadcast

> Broadcast using randomized epidemic dissemination.  
> Fast, fault-tolerant, and scalable at the cost of probabilistic delivery.

---

## References

C. Cachin, R. Guerraoui, and L. Rodrigues,  
**_Introduction to Reliable and Secure Distributed Programming_**, Springer, 2011.

- Chapter 3 (up to 3.9, except 3.9.6)
    
- Chapter 6, Section 6.1
    

---

Would you like me to include **code-style pseudocode blocks** for the broadcast algorithms (e.g., BEB, RB, URB, PbB) in the markdown as well? It can make the document more technical and ready for study notes or documentation.