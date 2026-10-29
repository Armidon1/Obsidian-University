---
title: Logical Clocks and Timestamp-based Mutual Exclusion
aliases:
  - DDS — Logical Clocks
  - DDS Lecture 5B
tags:
  - dependable-distributed-systems
  - logical-clocks
  - happened-before
  - vector-clocks
  - mutual-exclusion
source: DDS-Lecture5B-2026-2027.pptx
academic_year: "2026/2027"
---

# Logical Clocks and Timestamp-based Mutual Exclusion

> [!abstract] Purpose of this lecture
> [[3 - DDS - Time in Distributed Systems|Physical clock synchronization]] is only approximate, and its accuracy depends on delays we cannot estimate well. But many applications only need to know **in which order** events happened, not *when*. This lecture introduces Lamport's **happened-before** relation, the **scalar logical clock** that is consistent with it, and the **vector clock** that characterizes it exactly. It then uses logical timestamps to solve the first coordination problem of the course, **distributed mutual exclusion**, with **Lamport's** and **Ricart-Agrawala's** algorithms. The other approaches to mutual exclusion are in [[5 - DDS - Distributed Mutual Exclusion|the next lecture]]; vector clocks will come back in [[10 - DDS - Ordered Communications|causal broadcast]].
>
> Course map: [[MOC - Dependable Distributed Systems]].

## Recap: why we need something else

- Physical clock synchronization algorithms try to make processes agree on a **common notion of time**.
- Their accuracy depends **strongly on the estimation of the transmission delay** (e.g. $\pm(RTT/2 - min)$ for [[Cristian's Algorithm]]), and a good estimation can be hard to find.

> [!important] Observation
> In several applications it is not important **when** things happened but **in which order** they happened. We need a reliable way to **order events without using clock synchronization**.

## The happened-before relation

Vedi [[Happened-Before Relation]].

Two observations are enough to order *some* events with certainty:

1. Two events that occur at the same process $p_i$ happened in the order in which $p_i$ observes them.
2. When $p_i$ sends a message to $p_j$, the **send** event happens before the **deliver** event (a message cannot be received before it is sent).

Lamport (1978, *"Time, Clocks, and the Ordering of Events in a Distributed System"*) built on this the **happened-before** relation, which captures the **causal dependencies** between events (it is also called the **causal order** relation):

- $\to_i$ is the ordering relation between events of a single process $p_i$;
- $\to$ is happened-before between any pair of events.

### Definition

Two events $e$ and $e'$ are related by happened-before ($e \to e'$) if:

1. **local order**: $\exists\, p_i \mid e \to_i e'$;
2. **message**: $\exists\, m \mid e = send(m) \land e' = deliver(m)$;
3. **transitivity**: $\exists\, e'' \mid (e \to e'') \land (e'' \to e')$.

![[DDS-L04-p04.png]]

*$e_0 \to e_1 \to e_2 \to e_3$ on $p_i$ by local order; $e_3 = send(m)$ and $e_4 = deliver(m)$, so $e_3 \to e_4$; by transitivity also $e_0 \to e_5$, for example.*

### Partial order and concurrency

![[DDS-L04-p05.png]]

*$e_2$ on $p_j$ happens before the delivery $e_4$ (same process), but there is no chain of arrows between $e_2$ and the events $e_0, e_1, e_3$ of $p_i$: they are concurrent.*

- Happened-before imposes a **partial order** on the events of the execution history: there can be pairs $\langle e_i, e_j\rangle$ that are not related.
- If $e_i$ and $e_j$ are not related by happened-before they are **concurrent**: $e_i \parallel e_j$.
- For any pair of events **exactly one** of the following holds: $e_i \to e_j$, $e_j \to e_i$, or $e_i \parallel e_j$.

> [!tip] Intuition
> $e \to e'$ means "information could have flowed from $e$ to $e'$", i.e. $e$ **may have caused** $e'$. Concurrent events cannot influence each other, so for correctness it does not matter in which order we place them. Note that "concurrent" does not mean "simultaneous in real time": two events far apart in real time are concurrent if no message chain links them.

## Logical clock

The **logical clock**, introduced by Lamport, is a **software counter** that increases **monotonically**. A logical clock $L_i$ is used to timestamp events: $ts_e = L_i(e)$ is the *logical* timestamp that $p_i$ assigns to event $e$.

> [!important] Clock condition
> $$e \to e' \;\Rightarrow\; ts_e < ts_{e'}$$

The order obtained from logical timestamps is still only **partial** (two events can get the same timestamp).

## Scalar logical clock

Vedi [[Scalar Logical Clock]].

**Implementation (Lamport clock):**

- each $p_i$ initializes $L_i = 0$;
- $p_i$ increments $L_i$ by 1 whenever it generates an event (also *send* and *receive*): $L_i = L_i + 1$;
- when $p_i$ **sends** $m$: it creates the event $send(m)$, increments $L_i$, and timestamps $m$ with $ts = L_i$;
- when $p_i$ **receives** $m$ with timestamp $ts$: it updates $L_i = \max(ts, L_i)$, produces the event $receive(m)$ and increments $L_i$.

```text
upon event <internal or send event> do
    L := L + 1
    (if send) attach ts := L to m

upon event <receive m with ts> do
    L := max(L, ts)
    L := L + 1          // the receive event
```

The `max` is what enforces the clock condition across processes: after a receive, the local clock is greater than the timestamp of the send.

### Example

![[DDS-L04-p08.png]]

Following the arrows:

- $p_1$ sends at $e_1^1$ ($L_1 = 1$); $p_3$ sends at $e_3^1$ ($L_3 = 1$);
- $p_2$ receives $p_1$'s message: $\max(1, 0) + 1 = 2$; $p_1$ receives $p_3$'s message: $\max(1, 1) + 1 = 2$;
- $p_2$ sends at $L_2 = 3$; $p_3$ receives it: $\max(3, 1)+1 = 4$; $p_3$ sends at $5$; $p_1$ receives: $\max(5, 2) + 1 = 6$; and so on up to $L_2 = 9$.

The slide notes:

- $e_1^1 \to e_1^2$ and the timestamps reflect it ($1 < 2$);
- $e_1^1 \parallel e_3^1$ and they have the **same** timestamp (1);
- $e_2^1 \parallel e_3^1$ but they have **different** timestamps (2 and 1).

### Limits of the scalar logical clock

The scalar clock guarantees $e \to e' \Rightarrow ts_e < ts_{e'}$, but **not the converse**:

$$ts_e < ts_{e'} \;\not\Rightarrow\; e \to e'$$

(in the example $ts(e_3^1) = 1 < 2 = ts(e_2^1)$ but the two events are concurrent). Consequently, looking at scalar timestamps **we cannot tell whether two events are concurrent or related by happened-before**.

> [!tip] Total order from scalar clocks
> Scalar clocks are still very useful when we want **some total order consistent with causality**: order events by $(ts, \text{process id})$ — ties are broken by the identifier. This is exactly what Lamport's mutual exclusion does below (`t = 3, id = 3`).

Mattern (1989) and Fidge (1991) proposed an improved logical clock, the **vector clock**.

> [!note] Name
> The slide writes "Fridge"; the author is **Colin Fidge**.

## Vector clock

Vedi [[Vector Clock]].

### Definition

- For $N$ processes a vector clock is an **array of $N$ integer counters**.
- Each $p_i$ keeps its vector clock $V_i$ and timestamps its events with it.
- As with scalar clocks, the timestamp is attached to messages — now it is a vector of integers.
- Vector clocks let us decide happened-before **just by looking at the timestamps**:
  - scalar clocks: $e \to e' \Rightarrow L(e) < L(e')$;
  - vector clocks: $e \to e' \iff V(e) < V(e')$.

### Implementation

- $p_i$ initializes $V_i[j] = 0$ for all $j = 1..N$;
- for every event, $p_i$ increments **its own** entry: $V_i[i] = V_i[i] + 1$;
- **send** $m$: create the event $send(m)$, increment $V_i$, timestamp $m$ with $ts = V_i$;
- **receive** $m$ with $ts$: update $V_i[j] = \max(ts[j], V_i[j])$ for all $j$ (component-wise max), generate $receive(m)$, increment $V_i[i]$.

### Example

![[DDS-L04-p12.png]]

*Same execution as the scalar example. Each column is $[V[1], V[2], V[3]]$. E.g. when $p_1$ receives the message sent by $p_3$ at $[1,2,3]$, its clock goes from $[2,0,1]$ to $\max = [2,2,3]$ and then to $[3,2,3]$.*

All the vectors in the figure can be checked step by step with the rules above (they are correct).

### Properties

- $V_i[i]$ = number of events produced by $p_i$;
- $V_i[j]$, $j \ne i$ = number of events of $p_j$ that $p_i$ **knows about** (that causally precede the current event of $p_i$).

Comparison:

- $V = V' \iff V[j] = V'[j]\ \forall j$
- $V \le V' \iff V[j] \le V'[j]\ \forall j$
- $V < V' \iff V \le V' \land V \ne V'$, i.e. $\forall i: V'[i] \ge V[i]$ and $\exists i: V'[i] > V[i]$. In that case **the event of $V$ happened before the event of $V'$**.
- If neither $V \le V'$ nor $V' \le V$, the events are **concurrent**.

![[DDS-L04-p14.png]]

*Top: $[1,0,0] < [1,1,0]$, so $e \to e'$. Bottom: $[1,0,0]$ and $[0,0,1]$ are not comparable (each has a component greater than the other), so $e \parallel e'$.*

> [!important] The gain
> Unlike scalar clocks, vector clocks **determine** whether two events are concurrent or related by happened-before. The price is a timestamp of size $N$ on every message.

### Logical clocks in distributed algorithms

| Mechanism | What it gives | Used for |
|---|---|---|
| Scalar clock | total order consistent with causality (with ids) | **Lamport's mutual exclusion** (below) |
| Vector clock | exact causality / concurrency | **Causal broadcast** ([[10 - DDS - Ordered Communications\|Lecture 12]]) |

Which one to use depends on the specification of the problem.

## Distributed mutual exclusion

Vedi [[Mutual Exclusion Abstraction]].

### The problem

Consider a set of processes $\Pi = \{p_1, \dots, p_n\}$ and a set of resources $R = \{r_1, \dots, r_m\}$. Processes need to access the resources **exclusively**, and we must design a **distributed abstraction** that lets them coordinate to get access.

![[DDS-L04-p17.png]]

*Processes $p_1 \dots p_n$ compete for the resources $r_1 \dots r_m$; the padlocks show that a resource can be used by one process at a time.*

This is the same problem as the critical section among threads (see [[Algoritmo del Panettiere|SDC2 — Bakery algorithm]] and [[Algoritmo di Dijkstra per la Mutua Esclusione|SDC2 — Dijkstra]]), but **without shared memory**: processes can only exchange messages.

### System model

- processes $\Pi = \{p_1, \dots, p_n\}$, resources $R$; for simplicity $|R| = 1$;
- the system is **asynchronous**;
- processes **do not fail** (they are always correct);
- processes communicate over **perfect point-to-point links** ([[2 - DDS - Modelling Distributed Systems and Abstracting Communications#Perfect point-to-point link specification|Lecture 4]]).

### The mutual exclusion abstraction

**Events:**

- `request()` — asks to enter the critical section (CS);
- `ok()` — notifies the process that it can now access the CS;
- `release()` — leaves the CS and lets someone else enter.

![[DDS-L04-p19.png]]

**Properties:**

- **Mutual Exclusion** (*safety*): at any time $t$, at most one process is running the CS.
- **No-Deadlock** (*liveness*): there always exists a process able to enter the CS.
- **No-Starvation** (*liveness*): every `request()` and `release()` eventually terminates — i.e. every process that asks will eventually enter.

> [!note] No-Deadlock vs No-Starvation
> No-Deadlock is a *global* progress guarantee (the system as a whole does not get stuck); No-Starvation is *per process* (nobody waits forever). No-Starvation implies No-Deadlock, not vice versa. Compare with [[Deadlock|SDC2 — Deadlock]].

### Approaches

![[DDS-L04-p20.png]]

| Approach | Idea | Where |
|---|---|---|
| Coordinator-based | a special process grants the permission | [[5 - DDS - Distributed Mutual Exclusion\|next lecture]] |
| Token-based (logical ring) | only the holder of a unique token may enter | next lecture |
| Quorum-based | ask permission to a subset (quorum) of processes | next lecture |
| **Logical clock-based** | ask everyone, order the requests by timestamp | **today** |

## Lamport's distributed mutual exclusion

Vedi [[Lamport's Mutual Exclusion Algorithm]].

**Difference with a concurrent (shared-memory) system:** when a process wants to enter the CS it **sends a request message to all the others**.

- A history of the operations is kept with a counter (**timestamp**), i.e. a scalar logical clock.
- Every send and receive event is relevant: the counter is incremented for **every** send and receive, **including messages not related to mutual exclusion** (the "program messages" in the example).

### Implementation

Local data of $p_i$:

- `ck` — the logical clock of $p_i$;
- `Q` — a queue of CS access requests, ordered by $(timestamp, id)$.

Rules for $p_i$:

- **Request the CS:** send `REQUEST(ck)` to all other processes; add the request to its own `Q`.
- **Receive a request from $p_j$:** put $p_j$'s request (with its timestamp) in `Q`; send back an `ACK` to $p_j$.
- **Enter the CS iff:**
  1. `Q` contains its request with timestamp $t$;
  2. $t$ is the **smallest** timestamp in `Q` (ties broken by process id);
  3. it has received from **every** other process an ack with timestamp $t' > t$.
- **Release the CS:** send `RELEASE` to all other processes; delete its own request from `Q`.
- **Receive a release from $p_j$:** delete $p_j$'s request from `Q`.

```text
Init: ck := 0; Q := ∅

upon event request() do
    ck := ck + 1
    Q := Q ∪ {(ck, i)}
    for all pj ≠ pi: trigger pp2pSend(REQUEST, ck, i) to pj

upon event pp2pDeliver(REQUEST, t, j) do
    ck := max(ck, t) + 1
    Q := Q ∪ {(t, j)}
    ck := ck + 1
    trigger pp2pSend(ACK, ck, i) to pj

upon (my request (t, i) is the minimum of Q) and
     (received ACK with ts > t from all pj ≠ pi) do
    trigger ok()

upon event release() do
    Q := Q \ {(t, i)}
    for all pj ≠ pi: trigger pp2pSend(RELEASE, i) to pj

upon event pp2pDeliver(RELEASE, j) do
    Q := Q \ {request of pj}
```

> [!note] Assumption of the original algorithm
> In Lamport's 1978 paper, channels are assumed **FIFO**: a request of $p_j$ cannot be overtaken by a later ack of $p_j$. Condition 3 relies on this: once $p_i$ got a message from $p_j$ with timestamp larger than $t$, any earlier request of $p_j$ is already in $p_i$'s queue.

### Example

The diagram uses three message types: **program messages** (blue, not related to ME but they still advance the clocks), **CS access requests** (red), **acks** (green), and **releases** (yellow).

![[DDS-L04-p24.png]]

*$p_1$ sends a program message (clock 1) that $p_3$ receives (clock 2). Then $p_3$ requests the CS with timestamp 3: the request $(t=3, id=3)$ is put in its own queue and sent to $p_1$ and $p_2$.*

![[DDS-L04-p25.png]]

*$p_1$ and $p_2$ receive $p_3$'s request (clocks 4), queue it, and send back an ack (clock 5).*

![[DDS-L04-p27.png]]

*Meanwhile $p_1$ also requests the CS with timestamp 6: its queue contains $(3,3)$ and $(6,1)$. When $p_1$ has received both acks it still has to wait: its request is not the one with the smallest timestamp.*

![[DDS-L04-p28.png]]

*$p_3$ has received both acks (with timestamps greater than 3) and its request is the smallest in its queue → $p_3$ enters the CS.*

![[DDS-L04-p29.png]]

*$p_3$ leaves the CS and sends RELEASE (yellow). $p_1$ and $p_2$ remove $(3,3)$. Now $p_1$'s request $(6,1)$ is the smallest and $p_1$ has all the acks → $p_1$ enters the CS.*

### Safety proof

Suppose by contradiction that both $p_i$ and $p_j$ are in the CS. Then both received an ack from every other process and both had the smallest timestamp in their queue:

- $t_i < t_j < ack_i.ts$
- $t_j < t_i < ack_j.ts$

These cannot both hold since timestamps $(t, id)$ are **totally ordered**. More concretely, look at when $p_i$ receives $p_j$'s ack relative to $p_j$'s request:

![[DDS-L04-p30.png]]

- **Green:** $p_j$'s ack arrives *before* $p_j$'s request is sent → $p_j$'s request will have a larger timestamp, and $p_i$ enters without any problem.
- **Blue:** $p_j$'s ack arrives after $p_j$'s request but before $p_i$'s ack → $p_i$ enters, and sends its ack after executing the CS.
- **Red:** both processes receive the acks when **both requests are already in the queues**: ME is guaranteed by the **total order on the timestamps** — both queues agree on which request is first.

### Properties

**Fairness:** requests are satisfied in the order in which they are generated, where the order comes from happened-before:

- if two requests are related by happened-before, they are satisfied in that order;
- if they are concurrent, the access can happen in any order (the tie-break by $(t, id)$ chooses one, consistently at all processes).

### Performance

$3(N-1)$ messages per CS execution:

- $N-1$ requests;
- $N-1$ acks;
- $N-1$ releases.

In the best case (nobody is in the CS and only one process asks) the **synchronization delay** from request to access is **2 messages** (request → ack).

## Ricart-Agrawala's algorithm

Vedi [[Ricart-Agrawala Algorithm]].

Ricart and Agrawala (1981) optimize Lamport's algorithm by **merging the ack and the release**: a process replies to a request only when it does not need the CS itself (or its own request has lower priority); otherwise it **defers** the reply until it leaves the CS. So the reply acts as both "ok from me" and "I am done".

### Implementation

![[DDS-L04-p33.png]]

The slide gives the local variables and the three handlers (request the CS, receive a REQUEST, receive a REPLY), transcribed below.

Local variables:

- `#replies` (initially 0)
- `State` ∈ {Requesting, CS, NCS} (initially NCS)
- `Q` — queue of pending (deferred) requests (initially empty)
- `Last_Req` — timestamp of my last request
- `Num` — the logical clock

```text
begin  (request the CS)
1. State = Requesting
2. Num = Num + 1; Last_Req = Num
3. for i = 1..N send REQUEST(Num) to pi
4. wait until #replies = N - 1
5. State = CS
6. <critical section>
7. for each r ∈ Q send REPLY to r
8. Q = ∅; State = NCS; #replies = 0

upon receipt REQUEST(t) from pj
1. if State = CS or (State = Requesting and {Last_Req, i} < {t, j})
2.   then insert {t, j} in Q            // defer the reply
3.   else send REPLY to pj
4. Num = max(t, Num)

upon receipt REPLY from pj
1. #replies = #replies + 1
```

$\{Last\_Req, i\} < \{t, j\}$ compares pairs **lexicographically**: first by timestamp, then by process id. The process with the "smaller" pair has priority.

> [!note] Line 3
> The slide writes "∀ i = 1…N send REQUEST"; the request goes to the other $N-1$ processes (the algorithm waits for $N-1$ replies).

### Example

Three processes, $P_1$ (top), $P_2$ (middle), $P_3$ (bottom), all initially NCS.

![[DDS-L04-p34.png]]

*$P_2$ requests the CS: $Num = 1$, $Last\_Req = 1$, and sends REQUEST(1) to $P_1$ and $P_3$. $P_3$ (NCS) will reply immediately and set $Num = \max(1, 0) = 1$.*

![[DDS-L04-p38.png]]

*$P_1$ also requests the CS, concurrently, with $Num = 1$. When $P_1$ receives $P_2$'s request it compares $\{1, 1\} < \{1, 2\}$: **yes**, $P_1$ has priority (same timestamp, smaller id), so it defers $P_2$'s request into its queue $Q = \{(1,2)\}$.*

![[DDS-L04-p41.png]]

*$P_3$ replies to $P_1$ as well. When $P_2$ receives $P_1$'s request it compares $\{1, 2\} < \{1, 1\}$: **no**, so $P_2$ replies to $P_1$.*

![[DDS-L04-p45.png]]

*$P_2$ has one reply (from $P_3$). $P_1$ receives replies from $P_2$ and $P_3$: $\#replies = 2 = N-1$ → $P_1$ enters the CS.*

![[DDS-L04-p46.png]]

*When $P_1$ exits it sends the deferred REPLY to $P_2$ and empties $Q$. $P_2$ now has its second reply and enters the CS.*

> [!tip] Lamport vs Ricart-Agrawala
> | | Lamport | Ricart-Agrawala |
> |---|---|---|
> | Messages per CS | $3(N-1)$ | $2(N-1)$ |
> | Release | explicit RELEASE to all | deferred REPLY only to waiting processes |
> | Queue | all requests, replicated at every process | only deferred requests |
> | FIFO channels needed | yes | no |
> | Delay (best case) | 2 messages | 2 messages |

## Core ideas to retain

- **Happened-before**: local order + send→deliver + transitivity; a partial order. Not related ⇒ **concurrent**.
- **Scalar clock**: $e \to e' \Rightarrow L(e) < L(e')$, not vice versa. With ids it gives a total order.
- **Vector clock**: $e \to e' \iff V(e) < V(e')$; detects concurrency.
- **Mutual exclusion**: ME (safety), No-Deadlock and No-Starvation (liveness).
- **Lamport ME**: request to all, ack, release; enter when own request is the smallest and all acks are newer; $3(N-1)$ messages.
- **Ricart-Agrawala**: defer replies instead of acking and releasing; $2(N-1)$ messages.
