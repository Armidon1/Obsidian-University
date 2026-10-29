---
title: Broadcast Communications
aliases:
  - DDS — Broadcast Communications
  - DDS Lecture 8
tags:
  - dependable-distributed-systems
  - broadcast
  - reliable-broadcast
  - gossip
source: DDS-Lecture8-2026-2027.pdf
academic_year: "2026/2027"
---

# Broadcast Communications

> [!abstract] Purpose of this lecture
> So far communication was **point-to-point** ([[2 - DDS - Modelling Distributed Systems and Abstracting Communications#Lecture 4 — Abstracting Communications|links]]), between two processes, like in a client/server setting. Now a process wants to send a message to **the whole group**. Without failures this is trivial; with **crashes** the sender can die halfway through, and the group may **disagree** on whether the message was delivered. This lecture builds a hierarchy of broadcast abstractions of increasing strength:
> **BEB** (best effort) → **RB** (reliable: correct processes agree) → **URB** (uniform: agreement includes what faulty processes delivered) → and, for very large groups, **probabilistic broadcast** (gossip).
> It uses the [[6 - DDS - Failure Detection and Leader Election|perfect failure detector]] for the synchronous versions. The *order* in which messages are delivered is the topic of [[10 - DDS - Ordered Communications|ordered communications]] and [[11 - DDS - Total Order Broadcast|total order broadcast]].
>
> Course map: [[MOC - Dependable Distributed Systems]]. Book: Cachin, Guerraoui, Rodrigues, Chapter 3, §3.1–3.4 (pp. 73–84) and §3.8 (pp. 92–97).

## Recap: what we know up to now

- How to define a **system model** and specify a problem or abstraction in terms of **safety** and **liveness**.
- **Point-to-point** communication abstractions: fair-loss, stubborn and perfect links.
- How to **timestamp events**: [[3 - DDS - Time in Distributed Systems|physical clocks]] and [[4 - DDS - Logical Clocks|logical clocks]].
- How to **handle failures**: [[6 - DDS - Failure Detection and Leader Election|failure detectors and leader election]].

Up to now the focus has been on the interaction between **two** processes.

## Communication in a group: broadcast

![[DDS-L07-p03.png]]

*Left, no failures: the sender sends the message to every member and everybody delivers it. Right, crash failures: the sender crashes while sending; some processes got the message, others did not. What should they do?*

Like for links, we distinguish **send/deliver**: `broadcast(m)` is the request of the sender; `deliver(m)` is the indication given to each process when the abstraction hands the message to the application. A message can be *received* by the algorithm (from a lower layer) without being *delivered* yet.

## Best Effort Broadcast (BEB)

Vedi [[Best Effort Broadcast (BEB)]].

### Specification

```text
Module: BestEffortBroadcast, instance beb
Events:
  Request:    ⟨beb, Broadcast | m⟩     — broadcast m to all processes
  Indication: ⟨beb, Deliver | p, m⟩    — deliver m broadcast by p
Properties:
  BEB1 Validity: if a correct process broadcasts m, then every correct
       process eventually delivers m.
  BEB2 No duplication: no message is delivered more than once.
  BEB3 No creation: if a process delivers m with sender s, then m was
       previously broadcast by s.
```

Validity is the **liveness** property; no duplication and no creation are **safety** properties. They mirror the properties of perfect links.

### Implementation: Basic Broadcast

**System model:** asynchronous system, perfect links, crash failures.

```text
Algorithm 3.1: Basic Broadcast
Implements: BestEffortBroadcast, instance beb
Uses:       PerfectPointToPointLinks, instance pl

upon event ⟨beb, Broadcast | m⟩ do
  forall q ∈ Π do
    trigger ⟨pl, Send | q, m⟩

upon event ⟨pl, Deliver | p, m⟩ do
  trigger ⟨beb, Deliver | p, m⟩
```

The sender simply sends the message to everybody (itself included) over perfect links. It is a *fail-silent* algorithm: no failure detector.

### Correctness

- **Validity** — from the *reliable delivery* property of perfect links + the fact that the sender sends the message to every process.
- **No duplication** — from the no duplication property of perfect links + the assumption that messages are **unique** (different messages have different identifiers).
- **No creation** — directly from the corresponding property of perfect links.

**Performance:** 1 communication step, $O(N)$ messages.

### Observations on BEB

![[DDS-L07-p07.png]]

*$p_1$ broadcasts $m_1$: every process delivers it. Then $p_1$ broadcasts $m_2$ and crashes while sending: only one process receives $m_2$, the others never will.*

- BEB ensures delivery **as long as the sender does not fail**.
- If the sender fails, processes may **disagree** on whether or not to deliver the message. This is allowed: validity only talks about **correct** senders.

## (Regular) Reliable Broadcast (RB)

Vedi [[Reliable Broadcast (RB)]].

### Specification

```text
Module: ReliableBroadcast, instance rb
Events:
  Request:    ⟨rb, Broadcast | m⟩
  Indication: ⟨rb, Deliver | p, m⟩
Properties:
  RB1 Validity: if a correct process p broadcasts m, then p eventually
      delivers m.
  RB2 No duplication       (same as BEB)
  RB3 No creation          (same as BEB)
  RB4 Agreement: if a message m is delivered by some correct process,
      then m is eventually delivered by every correct process.
```

RB = BEB + the liveness property **agreement**. Even if the sender crashes, the correct processes deliver **the same set** of messages: all or nothing.

> [!note] Validity is weaker than in BEB, but agreement compensates
> RB1 only asks the (correct) sender to deliver its own message; together with RB4 this implies that every correct process delivers it — i.e. BEB1.

### BEB vs RB

![[DDS-L07-p09.png]]

*Arrows on the time lines are broadcast events (double arrows) and deliver events (block arrows); each color is a message. Top: the green message, broadcast by $p_1$ that then crashes, is delivered by $p_2$ (circled) but never by $p_3$. Since $p_2$ and $p_3$ are both correct, **agreement is violated**: it satisfies BEB (the sender is faulty) but not RB. Bottom: the green message is delivered only by $p_1$ itself, which crashes: no correct process delivered it, so RB is satisfied.*

### Implementation in synchronous systems: Lazy Reliable Broadcast

**Idea:** use BEB; if the sender is detected as crashed (by a [[Perfect Failure Detector|perfect failure detector]]), every process **relays** the messages it has delivered from that sender. The algorithm is **lazy**: it retransmits **only when necessary**.

```text
Algorithm 3.2: Lazy Reliable Broadcast
Implements: ReliableBroadcast, instance rb
Uses:       BestEffortBroadcast, instance beb
            PerfectFailureDetector, instance P

upon event ⟨rb, Init⟩ do
  correct := Π
  from[p] := [∅]^N                 // from[s] = messages of s already delivered

upon event ⟨rb, Broadcast | m⟩ do
  trigger ⟨beb, Broadcast | [DATA, self, m]⟩

upon event ⟨beb, Deliver | p, [DATA, s, m]⟩ do
  if m ∉ from[s] then
    trigger ⟨rb, Deliver | s, m⟩
    from[s] := from[s] ∪ {m}
    if s ∉ correct then            // sender already known as crashed:
      trigger ⟨beb, Broadcast | [DATA, s, m]⟩    // relay now

upon event ⟨P, Crash | p⟩ do
  correct := correct \ {p}
  forall m ∈ from[p] do            // relay everything I got from p
    trigger ⟨beb, Broadcast | [DATA, p, m]⟩
```

- The message carries the **original sender** $s$ (`[DATA, s, m]`), because a relayed copy arrives from $p \neq s$.
- Two events cause a retransmission: (1) detecting the crash of $s$ — relay what was already delivered from $s$; (2) delivering a message from $s$ **after** having detected its crash — relay it immediately.

### Examples

**Example 1:**

![[DDS-L07-p11.png]]

*$p_1$ rb-broadcasts $m_1$, delivered by everybody. Then it broadcasts $m_2$ and crashes: only $p_2$ beb-delivers (and rb-delivers) $m_2$. $p_3$ detects `crash(p1)` and relays $m_1$ (`from[p1] = {m1}`). $p_2$ detects the crash and relays $m_1$ and $m_2$. $p_3$ discards the duplicate $m_1$ and rb-delivers $m_2$: agreement holds.*

**Example 2:**

![[DDS-L07-p12.png]]

*Same start, but $p_2$ crashes right after relaying $m_1, m_2$, and its relay of $m_2$ does not reach $p_3$. Only $p_1$ and $p_2$ — both **faulty** — delivered $m_2$, so RB is still satisfied: agreement only constrains correct processes. (URB, below, would forbid this.)*

**Example 3:**

![[DDS-L07-p13.png]]

*$p_1$ crashes right after broadcasting $m_2$, and $m_2$ is slow. $p_2$ and $p_3$ detect the crash first and relay $m_1$. Later $p_2$ beb-delivers $m_2$: since $p_1 \notin$ `correct`, it rb-delivers and **relays it immediately** (second retransmission case). $p_3$ gets it from $p_2$.*

**Example 4:**

![[DDS-L07-p14.png]]

*As in Example 3, but $p_2$ crashes after relaying $m_2$, and the relay is lost: $p_3$ never delivers $m_2$. Again correct for RB, because $p_2$ is faulty.*

**Example with removal of retransmission:**

![[DDS-L07-p15.png]]

*Same as Example 3, but without the `if s ∉ correct` relay in the deliver handler: $p_2$ rb-delivers $m_2$ after detecting $p_1$'s crash and does **not** relay it. $p_2$ is correct and delivered $m_2$, $p_3$ is correct and never will: **agreement is violated**. This is why the check is needed.*

### Performance of the lazy algorithm

- **Best case:** 1 BEB message per RB message (the sender does not crash).
- **Worst case:** $n-1$ BEB messages per RB message (when $n-1$ processes crash, each one triggers a relay).

> [!quote] Dal libro — performance (p. 79)
> "If the initial sender does not crash then the algorithm requires a single communication step and O(N) messages to rb-deliver a message to all processes. Otherwise, it may take O(N) steps and O(N²) messages in the worst case (if the processes crash in sequence)."

**What if the failure detector is not perfect?**

| FD property violated | Effect on lazy RB |
|---|---|
| **Accuracy** (false crash detections) | Unnecessary relays: wasted messages, but **still correct** |
| **Completeness** (a crash is never detected) | Nobody relays the messages of the crashed sender: **agreement can be violated** |

So the lazy algorithm really needs completeness. To get rid of the failure detector altogether we relay **always**.

### Implementation in asynchronous systems: Eager Reliable Broadcast

```text
Algorithm 3.3: Eager Reliable Broadcast
Implements: ReliableBroadcast, instance rb
Uses:       BestEffortBroadcast, instance beb

upon event ⟨rb, Init⟩ do
  delivered := ∅

upon event ⟨rb, Broadcast | m⟩ do
  trigger ⟨beb, Broadcast | [DATA, self, m]⟩

upon event ⟨beb, Deliver | p, [DATA, s, m]⟩ do
  if m ∉ delivered then
    delivered := delivered ∪ {m}
    trigger ⟨rb, Deliver | s, m⟩
    trigger ⟨beb, Broadcast | [DATA, s, m]⟩    // relay every message
```

The algorithm is **eager**: every process relays every message the first time it delivers it, assuming the worst case (the sender may have crashed). No failure detector is needed — it works in asynchronous systems.

**Performance:** best case = worst case = **$n$ BEB messages per RB message**, i.e. $O(N^2)$ point-to-point messages.

> [!tip] Lazy vs eager
> | | Lazy RB | Eager RB |
> |---|---|---|
> | Model | synchronous (fail-stop, uses $\mathcal{P}$) | asynchronous (fail-silent) |
> | Relay | only after the sender's crash is detected | always |
> | BEB messages per RB | 1 (best) … $n-1$ (worst) | $n$ always |

## Uniform Reliable Broadcast (URB)

Vedi [[Uniform Reliable Broadcast (URB)]].

### Why RB is not enough

![[DDS-L07-p19.png]]

*Top: violation of agreement, as before. Bottom: the green message is delivered by $p_1$ (circled) and then $p_1$ crashes; nobody else ever delivers it. This **satisfies RB**, because $p_1$ is faulty. But $p_1$ may have acted on the message before crashing — e.g. replied to a client, written to disk — and now its view differs from the rest of the group.*

### Specification

```text
Module: UniformReliableBroadcast, instance urb
Events:
  Request:    ⟨urb, Broadcast | m⟩
  Indication: ⟨urb, Deliver | p, m⟩
Properties:
  URB1–URB3: same as RB1–RB3
  URB4 Uniform agreement: if a message m is delivered by some process
       (whether correct or faulty), then m is eventually delivered by
       every correct process.
```

Agreement on a message delivered by **any** process, crashed or not. Equivalently: **the set of messages delivered by a correct process is a superset of the ones delivered by a faulty one**.

### BEB vs RB vs URB

![[DDS-L07-p21.png]]

*Each color is a message; arrows are deliveries. **R1**: every message delivered by $p_1$ (which crashes) is also delivered by $p_2$ and $p_3$ → **URB**. **R2**: the yellow message is delivered by $p_1$ and $p_3$ but not by the correct $p_2$: agreement is violated. It is **BEB** if yellow was sent by $p_1$ (faulty sender: BEB promises nothing), **not correct** for any abstraction otherwise.*

![[DDS-L07-p22.png]]

*__R3__: yellow is delivered by both correct processes but not by $p_1$ → **URB** (a faulty process may deliver *less*). **R4**: yellow is delivered **only** by $p_1$, which then crashes → **RB** (not URB) if yellow was sent by $p_1$; **not correct** otherwise (if a correct process sent it, validity requires correct processes to deliver it).*

| Run | Abstraction satisfied |
|---|---|
| R1 | URB (hence also RB and BEB) |
| R2 | BEB only, if yellow sent by $p_1$ |
| R3 | URB |
| R4 | RB (not URB), if yellow sent by $p_1$ |

### Implementation in synchronous systems: All-Ack URB

**Idea:** in lazy and eager RB, a process delivers *and then* may crash before its relay reaches anybody. In URB a process delivers a message only when it **knows that every correct process has seen it** (and therefore will relay it): the relays act as **acknowledgements**.

```text
Algorithm 3.4: All-Ack Uniform Reliable Broadcast
Implements: UniformReliableBroadcast, instance urb
Uses:       BestEffortBroadcast, instance beb
            PerfectFailureDetector, instance P

upon event ⟨urb, Init⟩ do
  delivered := ∅
  pending := ∅                     // seen and relayed, not yet delivered
  correct := Π
  forall m do ack[m] := ∅          // who I know has seen m

upon event ⟨urb, Broadcast | m⟩ do
  pending := pending ∪ {(self, m)}
  trigger ⟨beb, Broadcast | [DATA, self, m]⟩

upon event ⟨beb, Deliver | p, [DATA, s, m]⟩ do
  ack[m] := ack[m] ∪ {p}
  if (s, m) ∉ pending then
    pending := pending ∪ {(s, m)}
    trigger ⟨beb, Broadcast | [DATA, s, m]⟩    // relay once

upon event ⟨P, Crash | p⟩ do
  correct := correct \ {p}

function candeliver(m) returns Boolean is
  return (correct ⊆ ack[m])

upon exists (s, m) ∈ pending such that candeliver(m) ∧ m ∉ delivered do
  delivered := delivered ∪ {m}
  trigger ⟨urb, Deliver | s, m⟩
```

- Every process relays each message **once**; receiving a copy from $p$ means "$p$ has seen $m$" (`ack[m] ∪= {p}`).
- `candeliver(m)`: all processes still considered correct have acknowledged $m$. When a process crashes, it leaves `correct`, so we stop waiting for it (strong completeness of $\mathcal{P}$); a correct process is never removed (strong accuracy), so we never deliver too early.

#### Examples

**No failures:**

![[DDS-L07-p24.png]]

*$p_3$ urb-broadcasts $m_1$ (`pending3 = {⟨p3, m1⟩}`). Each process, on the first copy, adds it to `pending` and relays it. Acks accumulate: `ack[m1] = {p3}` → `{p3, p2}` → `{p3, p2, p1}`. When `ack[m1] = correct = {p1, p2, p3}`, each process urb-delivers $m_1$ (purple arrows).*

**$p_1$ crashes:**

![[DDS-L07-p25.png]]

*$p_1$ collects all three acks and delivers $m_1$, then crashes. $p_2$ and $p_3$ have `ack[m1] = {p3, p2}` and are stuck until $\mathcal{P}$ reports `Crash(p1)`: then `correct = {p2, p3} ⊆ ack[m1]` and they deliver. Uniform agreement holds: the faulty $p_1$ delivered $m_1$, and so do all correct processes.*

**The sender $p_3$ crashes:**

![[DDS-L07-p26.png]]

*$p_3$ crashes right after broadcasting; its own copy never reaches the others in time. $p_1$ and $p_2$ relay $m_1$, so `ack[m1] = {p1, p2}` at both. After `Crash(p3)`, `correct = {p1, p2} ⊆ ack[m1]` and they deliver.*

> [!quote] Dal libro — cost of uniformity (p. 84)
> "In the best case, the algorithm requires two communication steps to urb-deliver a message to all processes. In such scenario, in the first step it sends N messages and in the second step N(N−1) messages, for a total of N² messages. […] Therefore, uniform reliable broadcast requires one step more to deliver a message than its regular counterpart."

### Implementation in asynchronous systems: Majority-Ack URB

Without a failure detector we cannot know who is correct, so we cannot wait for "all correct". Instead we wait for a **majority**:

```text
Algorithm 3.5: Majority-Ack Uniform Reliable Broadcast
Implements: UniformReliableBroadcast, instance urb
Extends:    All-Ack Uniform Reliable Broadcast (Algorithm 3.4)
Uses:       BestEffortBroadcast, instance beb

function candeliver(m) returns Boolean is
  return #(ack[m]) > N/2

// Except for the function above, and the non-use of the perfect failure
// detector, same as Algorithm 3.4.
```

> [!important] We need to assume a majority of correct processes
> $N > 2f$, where $f$ is the maximum number of crashes. If a process delivers $m$, more than $N/2$ processes have seen and relayed it; at least one of them is **correct**, and its relay (by BEB validity) reaches every correct process, which will in turn relay it — so every correct process eventually collects a majority of acks. Without a correct majority, a process could wait forever (validity violated) — the waiting condition could never be satisfied.

### An open question

- There is an algorithm for **synchronous** systems using a **perfect failure detector**.
- There is an algorithm for **asynchronous** systems assuming a **majority of correct processes**.
- **Can we devise a URB algorithm for a partially synchronous system (using $\Diamond\mathcal{P}$) without a majority of correct processes?**

> [!quote] Dal libro — Exercise 3.7 (p. 124), Solution 3.7 (p. 128)
> **No, a majority of correct processes is necessary.** Partitioning argument with four processes $\{p, q, r, s\}$, two of which may fail:
> 1. Execution A: $p$ urb-broadcasts $m$; $r$ and $s$ crash without receiving anything from $p$ or $q$. By **validity**, at some time $t$ the process $p$ must urb-deliver $m$.
> 2. Execution B: identical up to $t$, but $r$ and $s$ are **correct** and only *falsely suspected* by $\Diamond\mathcal{P}$ (allowed: it is only *eventually* accurate). For $p$ the two executions are indistinguishable, so it delivers $m$ at $t$. Right after, $p$ and $q$ crash.
> 3. Now $p$ delivered $m$, but $r$ and $s$ — correct — have no way of knowing about $m$ and never deliver it: **uniform agreement is violated**.
>
> With $\mathcal{P}$ the false suspicion in step 2 is impossible; with a correct majority $p$ would have to wait for an ack from $r$ or $s$ before delivering.

## Probabilistic broadcast

Vedi [[Probabilistic Broadcast (Gossip)]].

**Motivation:**

- delivery of the message **99% of the times** — not fully reliable;
- for **large and dynamic groups** (thousands or millions of processes);
- **acks make reliable broadcast not scalable**.

### Ack implosion and ack tree

![[DDS-L07-p30.png]]

*Figure 3.5 of the book. (a) Direct communication: the sender sends to all and receives all acks — with thousands of processes it spends **all its time doing the ack task** (**ack implosion**). (b) Hierarchical communication (a tree): each node handles only its children, but the **tree structure must be maintained** (reconfigured on failures and joins), and latency grows with the depth.*

### Specification

```text
Module: ProbabilisticBroadcast, instance pb
Events:
  Request:    ⟨pb, Broadcast | m⟩
  Indication: ⟨pb, Deliver | p, m⟩
Properties:
  PB1 Probabilistic validity: there is a positive value ε such that when
      a correct process broadcasts m, the probability that every correct
      process eventually delivers m is at least 1 − ε.
  PB2 No duplication       (same as BEB)
  PB3 No creation          (same as BEB)
```

Only validity changes: it holds with probability $\geq 1 - \varepsilon$.

### Gossip dissemination

![[DDS-L07-p32.png]]

*Figure 3.6 of the book: epidemic dissemination with fanout 3, rounds 1, 2, 3. Infected (black) processes grow quickly at each round.*

- A process sends the message to a set of **$k$ randomly chosen** processes ($k$ = **fanout**).
- A process receiving the message **for the first time** forwards it to $k$ randomly chosen processes; this step is called a **round**.
- The algorithm performs a **maximum number $r$ of rounds**.

It works like the spread of an epidemic or a rumor: no acks, the load per process is $k$ messages, and the redundancy of random paths gives high reliability.

### Eager Probabilistic Broadcast

```text
Algorithm 3.9: Eager Probabilistic Broadcast
Implements: ProbabilisticBroadcast, instance pb
Uses:       FairLossPointToPointLinks, instance fll

upon event ⟨pb, Init⟩ do
  delivered := ∅

procedure gossip(msg) is
  forall t ∈ picktargets(k) do trigger ⟨fll, Send | t, msg⟩

upon event ⟨pb, Broadcast | m⟩ do
  delivered := delivered ∪ {m}
  trigger ⟨pb, Deliver | self, m⟩
  gossip([GOSSIP, self, m, R])

upon event ⟨fll, Deliver | p, [GOSSIP, s, m, r]⟩ do
  if m ∉ delivered then
    delivered := delivered ∪ {m}
    trigger ⟨pb, Deliver | s, m⟩
  if r > 1 then gossip([GOSSIP, s, m, r − 1])

function picktargets(k) returns set of processes is
  targets := ∅
  while #(targets) < k do
    candidate := random(Π \ {self})
    if candidate ∉ targets then
      targets := targets ∪ {candidate}
  return targets
```

- `r` counts the remaining rounds: the message stops after $R$ hops.
- It runs over **fair-loss** links: losses are tolerated by redundancy, not by retransmission.

> [!quote] Dal libro — choosing the fanout (pp. 95–96)
> "A higher fanout not only increases the probability of having the entire population infected but also decreases the number of rounds required to achieve this. […] However, increasing the fanout is costly. The higher the fanout, the higher the load imposed on each process and the amount of redundant information exchanged over the network." Delivery can fail, e.g. if all the first receivers pick the same $k$ targets, "but by choosing large enough values of k and R in relation to N, this probability can be made arbitrarily small."
>
> A first estimate (only the sender infects others, a fraction $\gamma = k/N$ per round): the probability that a given process is infected after $R$ rounds is at least about $1 - (1-\gamma)^R$.

## References

C. Cachin, R. Guerraoui, L. Rodrigues, *Introduction to Reliable and Secure Distributed Programming*, Springer, 2011:
- Chapter 3 — "from Section 3.9 (except 3.9.6)";
- Chapter 6 — Section 6.1.

> [!note] About the references on the slide
> The topics of this lecture are in §3.1–3.4 (BEB, RB, URB, pp. 73–86) and §3.8 (probabilistic broadcast, pp. 92–97). §3.9 (FIFO and causal broadcast) and §6.1 (total order broadcast) are the topics of [[10 - DDS - Ordered Communications|Lecture 12]] and [[11 - DDS - Total Order Broadcast|Lecture 13]]: the slide probably means "up to Section 3.9".

## Core ideas to retain

| Abstraction | Agreement | Model / algorithm | Cost |
|---|---|---|---|
| **BEB** | none (only if the sender is correct) | Basic Broadcast, perfect links | 1 step, $N$ msgs |
| **RB** | correct processes deliver the same set | Lazy ($\mathcal{P}$) / Eager (async) | Lazy: 1…$n-1$ BEB; Eager: $n$ BEB |
| **URB** | anything delivered by anyone is delivered by all correct | All-Ack ($\mathcal{P}$) / Majority-Ack ($N > 2f$) | 2 steps, $N^2$ msgs |
| **Probabilistic** | with probability $\geq 1-\varepsilon$ | gossip with fanout $k$, $R$ rounds | $k$ msgs per process per round |
