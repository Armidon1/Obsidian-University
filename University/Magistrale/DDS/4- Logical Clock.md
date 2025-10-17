## Logical Clock

---

## Recap

- Physical clock synchronization algorithms aim to coordinate processes toward a common notion of time.
    
- Synchronization accuracy depends on estimating transmission delays.
    
    - 🧩 Issue: hard to estimate accurately.
        

### Observation

In many applications, the **order of events** is more important than their actual time.

> We need a reliable way to order events **without relying on physical clocks**.

---

# Happened-Before Relation

---

### Observations

- Events in the same process occur in the order observed by that process.
    
- If `pi` sends a message to `pj`, the **send** event happens before the **receive** event.
    

Lamport introduced the **happened-before relation (→)** to capture **causal dependencies** between events.

---

## Definition

Two events `e` and `e'` are related by the happened-before relation (`e → e'`) if:

1. ∃ process `pi`: `e →i e'` (same process order)
    
2. ∃ message `m`: `e = send(m)` and `e' = receive(m)`
    
3. ∃ event `e''`: `(e → e'') ∧ (e'' → e')` (transitive closure)
    

---

## Properties

- The happened-before relation defines a **partial order** over events.
    
- There may exist events `ei` and `ej` such that neither `ei → ej` nor `ej → ei`.
    
    - In that case, `ei` and `ej` are **concurrent** (`ei || ej`).
        
- For any two events `ei` and `ej`, one of the following holds:
    
    1. `ei → ej`
        
    2. `ej → ei`
        
    3. `ei || ej`
        

---

# Logical Clocks

---

Introduced by **Lamport**, a **logical clock** is a software counter that **monotonically increases** to order events.

Each process `pi` maintains a logical clock `Li`.

- Each event `e` is timestamped with `tse = Li(e)`.
    
- Property: if `e → e'`, then `tse < tse'`.
    

> Logical timestamps provide a **partial ordering** consistent with causality.

---

## Scalar Logical Clock: Implementation

Each process `pi`:

1. Initializes `Li = 0`.
    
2. Increments `Li` by 1 for each event (send or receive).
    
    ```
    Li = Li + 1
    ```
    
3. When sending a message `m`:
    
    - Increment `Li`
        
    - Attach timestamp `ts = Li`
        
4. When receiving a message `m` with timestamp `ts`:
    
    ```
    Li = max(Li, ts)
    Li = Li + 1
    ```
    

---

## Scalar Logical Clock: Example

Example:

- Events in the same process are ordered.
    
- Concurrent events may have identical timestamps.
    
- Non-causally related events may still have different timestamps.
    

### Key Observations

- If `e1 → e2`, timestamps reflect this (`L1 < L2`).
    
- If events are concurrent (`e1 || e2`), timestamps may not reflect that accurately.
    

---

## Limits of Scalar Logical Clocks

They satisfy:

- If `e → e'`, then `L(e) < L(e')`
    

But **not** the converse:

- If `L(e) < L(e')`, it does _not_ imply `e → e'`.
    

> Scalar clocks cannot determine if two events are concurrent.

To fix this, **Mattern (1989)** and **Fidge (1991)** introduced **vector clocks**.

---

# Vector Clocks

---

## Definition

A **Vector Clock** for `N` processes is an array of `N` integers.

Each process `pi` maintains a vector `Vi[1..N]`.

- `Vi[i]` counts the number of events executed by `pi`.
    
- `Vi[j]` (for `j ≠ i`) counts how many events of `pj` are known to `pi`.
    

### Rules

1. Initialize `Vi[j] = 0` for all `j`.
    
2. On each local event:
    
    ```
    Vi[i] = Vi[i] + 1
    ```
    
3. On `send(m)`:
    
    - Increment `Vi[i]`
        
    - Attach timestamp `ts = Vi`
        
4. On `receive(m)`:
    
    ```
    For all j: Vi[j] = max(Vi[j], ts[j])
    Vi[i] = Vi[i] + 1
    ```
    

---

## Comparison Rules

Given two vector timestamps `V` and `V'`:

- `V = V'` if and only if `V[j] = V'[j]` ∀ j
    
- `V ≤ V'` if and only if `V[j] ≤ V'[j]` ∀ j
    
- `V < V'` (and hence `e → e'`) if:
    
    ```
    V ≤ V' ∧ V ≠ V'
    ```
    

Thus:

- If `V(e) < V(e')` → `e → e'`
    
- If `V(e)` and `V(e')` are incomparable → `e || e'` (concurrent)
    

---

## Properties

|Component|Meaning|
|---|---|
|`Vi[i]`|# of events produced by `pi`|
|`Vi[j]`|# of events from `pj` known by `pi`|

---

## Advantages Over Scalar Clocks

- Vector clocks **distinguish concurrency**.
    
- They fully capture the **causal structure** of events.
    

---

# Logical Clocks in Distributed Algorithms

Two mechanisms to represent logical time:

|Mechanism|Typical Use|
|---|---|
|Scalar Clock|Lamport’s Mutual Exclusion|
|Vector Clock|Causal Broadcast|

---

# Distributed Mutual Exclusion

---

## The Problem

Given:

- A set of processes: `Π = {p1, p2, …, pn}`
    
- A set of resources: `R = {r1, r2, …, rm}`
    

Processes must access shared resources **exclusively**.

### Objective

Design a **distributed abstraction** ensuring:

- Only one process accesses a resource at a time.
    

---

## System Model

Assume:

- |R| = 1 (one critical resource).
    
- Asynchronous system.
    
- Processes never fail.
    
- Communication via **perfect point-to-point links**.
    

---

## The Mutual Exclusion Abstraction

### Events

- `request()` – request access to the critical section (CS).
    
- `ok()` – permission granted.
    
- `release()` – leave CS.
    

### Properties

1. **Mutual Exclusion** – at most one process in CS.
    
2. **No Deadlock** – some process can always enter CS.
    
3. **No Starvation** – every request eventually completes.
    

---

## Approaches

1. Coordinator-based
    
2. Token-based (logical ring)
    
3. Quorum-based
    
4. **Timestamp-based (Logical Clock)** – Lamport’s algorithm
    

---

# Lamport’s Distributed Mutual Exclusion Algorithm

---

### Core Idea

Use timestamps to order requests consistently across processes.

### Data Structures per Process `pi`

- `ck`: local counter (logical clock)
    
- `Q`: request queue (ordered by timestamp)
    

---

### Rules

#### Requesting CS

1. Increment `ck`
    
2. Send `REQUEST(ck)` to all processes
    
3. Add request to local `Q`
    

#### Receiving Request

1. Add request from `pj` to local `Q`
    
2. Send `ACK` to `pj`
    

#### Entering CS

A process enters the CS if:

1. Its request is at the top of the queue
    
2. It has received ACKs from all other processes
    
3. Its timestamp is the smallest in the queue
    

#### Releasing CS

1. Send `RELEASE` to all
    
2. Remove own request from `Q`
    

---

### Properties

- **Fairness:** Requests are served in order of timestamps.
    
- **Mutual Exclusion:** Guaranteed by total order.
    
- **Message Complexity:** 3(N − 1) per CS execution.
    
- **Delay:** 2 message delays (best case).
    

---

# Ricart–Agrawala Algorithm

---

Improves Lamport’s algorithm — **fewer messages** (2(N−1) total).

### Local Variables

- `#replies` – count of received replies
    
- `State ∈ {Requesting, CS, NCS}`
    
- `Q` – pending requests queue
    
- `Last_Req`, `Num` – timestamp variables
    

---

### Algorithm

#### Requesting CS

```
State = Requesting
Num = Num + 1
Last_Req = Num
Send REQUEST(Num) to all
Wait until #replies = N-1
Enter CS
```

#### Upon Receiving REQUEST(t) from pj

```
If (State == CS) or (State == Requesting and {Last_Req, i} < {t, j})
   Add {t, j} to Q
Else
   Send REPLY to pj
Num = max(t, Num)
```

#### Upon Receiving REPLY

```
#replies = #replies + 1
```

#### Upon Exiting CS

```
For all r in Q: send REPLY to r
Clear Q; reset #replies; set State = NCS
```

---

### Properties

| Property          | Description                       |
| ----------------- | --------------------------------- |
| Mutual Exclusion  | Guaranteed by timestamp ordering  |
| Fairness          | Requests served in causal order   |
| Messages per CS   | 2(N − 1)                          |
| Delay             | 1 round-trip (request + replies)  |
| Failure Tolerance | Requires all processes to respond |

---

# Summary

| Concept                       | Purpose                                 |
| ----------------------------- | --------------------------------------- |
| **Scalar Clock**              | Partial ordering (causality)            |
| **Vector Clock**              | Detect concurrency                      |
| **Lamport’s Algorithm**       | Ensures mutual exclusion via timestamps |
| **Ricart–Agrawala Algorithm** | Optimized version with fewer messages   |

---

## References

- L. Lamport, _Time, Clocks, and the Ordering of Events in a Distributed System_, CACM 1978
    
- M. Ricart, A. Agrawala, _An Optimal Algorithm for Mutual Exclusion in Computer Networks_, CACM 1981
    
- C. Cachin, R. Guerraoui, L. Rodrigues – _Introduction to Reliable and Secure Distributed Programming_, Springer 2011
    

---
