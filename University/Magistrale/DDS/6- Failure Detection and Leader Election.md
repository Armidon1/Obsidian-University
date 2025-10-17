## Lecture 7A: Failure Detection

---

## Recap on Timing Assumptions

### Synchronous Systems

- Explicit timing assumptions
- Upper bounds on:
    - Process execution time
    - Communication time
- Existence of a global clock

**Asynchronous Systems**
- No timing assumptions

### Partial Asynchronous SystemsSynchrony

- Abstract timing assumptions:
    
    - After some unknown time _t_, the system becomes synchronous
        

> ⚠️ Manipulating time inside protocols is complex and correctness proofs may become error-prone.

---

## Time Management Approaches

### Explicit

- Include timing assumptions directly in the **system model** (links and processes)
    

### Implicit

- Create **separate abstractions** encapsulating timing assumptions
    

---

## Failure Detector Abstraction

A **Failure Detector (FD)** is an oracle providing information about process failures.  
It is a software module used alongside process and link abstractions.

- Encapsulates timing assumptions (partial or full synchrony)
    
- Stronger timing assumptions → more accurate detection
    

### Properties

1. **Accuracy** – ability to avoid mistakes
    
2. **Completeness** – ability to detect all failures
    

---

## Failure Detector Classification

| Accuracy | Completeness | Type                     | Description                                                      |
| -------- | ------------ | ------------------------ | ---------------------------------------------------------------- |
| Strong   | Strong       | **P** (Perfect FD)       | Detects all failures correctly, never suspects correct processes |
| Strong   | Weak         | **S** (Strong FD)        | Some correct process never suspected                             |
| Weak     | Strong       | **Q** (Quasi-perfect FD) | Detects all crashes but may make temporary mistakes              |
| Weak     | Weak         | **W** (Weak FD)          | Detects some crashes, some correct never suspected               |

---

### Observations

- **W**: at least one correct process is never suspected (difficult in practice).
    
- Introduce _eventual_ versions for realistic behavior:
    

#### Eventual Strong Accuracy

- After some time, correct processes are no longer suspected.
    

#### Eventual Weak Accuracy

- After some time, at least one correct process is never suspected.
    

---

## Eventual Failure Detector Classification

|Accuracy|Completeness|Type|
|---|---|---|
|Strong|Strong|♢P – Eventually Perfect|
|Weak|Strong|♢Q – Eventually Quasi-perfect|
|Strong|Weak|♢S – Eventually Strong|
|Weak|Weak|♢W – Eventually Weak|

---

## Perfect Failure Detector (P)

### System Model

- **Synchronous** system
    
- **Crash failures** only
    

Using local clocks and synchrony bounds, a process can infer if another process crashed.

### Specification

- Detects crashed processes (`Crash(pi)`)
    

### Implementation

- Relies on **Perfect Point-to-Point Links**
    

```
pp2pSend(msg)
pp2pDeliver(msg)
```

### Correctness

Must satisfy:

- **Strong Completeness**: all crashed processes are detected
    
- **Strong Accuracy**: no correct process suspected
    

#### Questions:

- What if links are fair-loss?
    
- What if timeout too long or too short?
    

---

## Eventually Perfect Failure Detector (♢P)

### System Model

- Partial synchrony
    
- Crash failures
    
- Perfect point-to-point links
    

Crashes are detected **only after** an unknown time _t_.  
Before _t_, mistakes are possible.

### Specification

```
Suspect(pi)
Restore(pi)
```

### Basic Construction Rules

- Use **timeouts** to suspect processes missing expected messages
    
- If a process later sends a message → restore trust and update timeout
    
- Once a process truly crashes → suspicion remains permanent
    

### Correctness

- **Strong Completeness:** all crashed processes eventually suspected
    
- **Eventual Strong Accuracy:** after time _T_, correct processes no longer suspected
    

---

## References

- C. Cachin, R. Guerraoui, L. Rodrigues, _Introduction to Reliable and Secure Distributed Programming_, Springer 2011
    
    - Chapter 2, Sections 2.6.1–2.6.5
        
- T. Chandra, S. Toueg, _Unreliable Failure Detectors for Reliable Distributed Systems_,  
    [ACM DL Link](https://dl.acm.org/doi/pdf/10.1145/226643.226647)
    

---

# Leader Election

---

## Recap on Timing Assumptions

### Synchronous Systems

- Explicit bounds on:
    - Process execution and communication
    - Global clock
    - Or both

### Asynchronous Systems

- No timing assumptions

### Partial Synchrony

- System becomes synchronous after unknown time _t_

Two approaches:

1. Include assumptions in the system model
    
2. Use separate abstractions encapsulating timing behavior
    

> ⚠️ Time manipulation in algorithms → complex correctness proofs.

---

## Alternative: Leader Election

Instead of detecting failures, sometimes we just need **one alive process** (e.g., a coordinator).

A **Leader Election module** provides that.

### Specification

```
Leader(pi)
```
![[Pasted image 20251016121927.png]]
### Implementation

Uses a **Perfect Failure Detector (P)**:

```
Crash(pi)
```
![[Pasted image 20251016121940.png]]
as we can see, we implemented de Perfect Failure Detector. It's important that every process uses the exact method on how to recognise the leader

---

## Example Scenarios

When a leader crashes, processes may temporarily disagree on who the new leader is due to failure detector latency.

Different scenarios illustrate:
- Leader reassignments
- Temporary inconsistencies
- Convergence to the same leader after stability

**Example 1**
Consider $p_3$ our leader and somehow it crashes. Since we have the Perfect Failure Detector, it will provide to all the other processes the information that the leader crashed: but may happen that is not perfectly sync and instantaneously with other processes (may happen that a process will be notified before another process.

Notice that when $p_3$ fails, there's a period of time in which there isn't any leader. When another process doesn't know that, simply it fails when tries to communicate with the current crashed leader. 

![[Pasted image 20251016122528.png]]
**Example 2**
if $p_2$ crashes (which is not the leader), nothing happens, because it isnt the leader but it will be added to the suspected list. when also the leader $p_3$ crashes, then, after beaing added to the suspected list, will be necessary choose the new leader, which will be $p_1$. consider that $p_2$ and $p_3$ are gone and then won't update their current state
![[Pasted image 20251016122539.png]]
**Example 3**
	
![[Pasted image 20251016122545.png]]
**Example 4**
if $p_3$ crashes, may happen that a process $p_2$ will be chosen as a leader by $p_1$, but this one doesn't get notified instantaneously so he can become a leader and he doesn't know yet.
![[Pasted image 20251016122555.png]]

---

## Correctness Question

- What happens if the failure detector is **not perfect**? 
Since we know that the detector can detect a false positive, may happen that two processes are leader at the same time. If this happens, we have consistancy issue. We have to work on accuracy of the detector. How we can survive? We have to move from Asynchronous to Synchronous.

---

## Eventual Leader Election (Ω)

### Specification
The event is called:
```
Trust(pi)
```
"i don't know if the other processes are trust worthy, but i'm sure that $p_i$ is trusted to be leader"
![[Pasted image 20251016124315.png]]

### Properties
- Eventually, all correct processes trust the **same correct process** as leader.
- Before stabilization:
    - Leaders may change arbitrarily
    - Multiple leaders may coexist

Once stabilized → a single, persistent leader.

---

### Implementation (Using ♢P)
♢P is the Eventually Perfect Failure Detector.

- Use deterministic rule:    
    - Trust the **highest identifier** among processes not suspected by ♢P
- Assumption: at least one correct process exists
![[Pasted image 20251016124945.png]]

### Example Behavior
Processes update trust dynamically as they suspect or restore others.
**Example 1**
![[Pasted image 20251016125556.png]]
**Example 2**
![[Pasted image 20251016125611.png]]

---

## System Model for Ω

- **Crash-Recovery**: if a process crashes, it can be restored and returning to work. In crash-recovery, a process is correct if never fails or fails only a finite number of times.
    
- **Partial synchrony**
    

A **correct process** is one that:
1. Never crashes, or
2. Eventually recovers and never crashes again

---

## Ω with Crash-Recovery and Fair Lossy Links and timeouts

### Components

```
flSend(msg)
flDeliver(msg)
```

- **Epoch** keeps track of how many times the process crashes and recovered.
- **Recovery** 
- Determines leader using deterministic rule:
    
    - Lowest epoch number
        
    - Among equals, lowest process ID

 
![[Pasted image 20251016130102.png]]
![[Pasted image 20251016130425.png]]
**Notice**: the ***select*** function is a deterministic fucntion that returns a process among all candidates, which can be chosen for whatever reason (for example, because has the best RTT), but must consider also the lowest epoch number.

---

## Example Behavior

- Processes exchange trust messages with epochs
    
- Determine the leader based on current candidate set
    
- Eventually converge on a stable leader
    
**Example 1**
![[Pasted image 20251016131005.png]]
**Example 2**
![[Pasted image 20251016131030.png]]

---
### Suggestion
Try to implement by yourself those algorithm and play by yourself

## References

- C. Cachin, R. Guerraoui, L. Rodrigues, _Introduction to Reliable and Secure Distributed Programming_, Springer 2011
    
    - Chapter 2, Sections 2.6.1–2.6.5
        

---
