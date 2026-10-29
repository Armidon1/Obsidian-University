---
title: Distributed Mutual Exclusion
aliases:
  - DDS — Distributed Mutual Exclusion
  - DDS Lecture 6
tags:
  - dependable-distributed-systems
  - mutual-exclusion
  - token-ring
  - quorum
source: DDS-Lecture6-2026-2027.pdf
academic_year: "2026/2027"
---

# Distributed Mutual Exclusion

> [!abstract] Purpose of this lecture
> [[4 - DDS - Logical Clocks#Distributed mutual exclusion|The previous lecture]] defined the **mutual exclusion abstraction** and solved it with logical clocks (Lamport, Ricart-Agrawala), which require *every* process to agree on every access. This lecture presents the three other families of algorithms: **coordinator-based** (one process decides), **token-based on a logical ring** (only the holder of a unique token enters), and **quorum-based** (Maekawa's voting: ask only a subset of processes). For each one we look at the code, an execution and its costs. All of them assume processes that **never fail**: what happens when the coordinator or the token holder crashes is the motivation for [[6 - DDS - Failure Detection and Leader Election|failure detectors and leader election]].
>
> Course map: [[MOC - Dependable Distributed Systems]].

## Recap

### The mutual exclusion problem

A set of processes $\Pi = \{p_1, \dots, p_n\}$ wants **exclusive** access to a set of resources $R = \{r_1, \dots, r_m\}$; we need a distributed abstraction that lets them coordinate (see [[Mutual Exclusion Abstraction]]).

### System model

- $|R| = 1$ for simplicity;
- **asynchronous** system;
- processes **do not fail**;
- communication over **perfect point-to-point links** (`pp2pSend` / `pp2pDeliver`, see [[2 - DDS - Modelling Distributed Systems and Abstracting Communications|Lecture 4]]).

### The abstraction

- **Events:** `request()`, `ok()`, `release()`.
- **Properties:** **Mutual Exclusion** (at most one process in the CS at any time), **No-Deadlock** (some process can always enter), **No-Starvation** (every `request()` and `release()` eventually terminates).

### Approaches

| Approach | Lecture |
|---|---|
| Coordinator-based | today |
| Token-based (logical ring) | today |
| Quorum-based | today |
| Logical clock-based | [[4 - DDS - Logical Clocks#Lamport's distributed mutual exclusion\|previous lecture]] |

## Coordinator-based mutual exclusion

Vedi [[Coordinator-based Mutual Exclusion]].

**Basic idea:** there is a special process, the **coordinator**, that collects the requests and **grants the permission** to enter the CS. It is the distributed version of a lock server: the coordinator holds the lock and serializes the accesses.

The pseudocode uses the event-based notation of the course (`upon event … do`): every process runs the *process code*, and the coordinator additionally runs the *coordinator code*.

```text
PROCESS CODE                                  COORDINATOR CODE

Init                                          Init
  state = idle                                  pending = ∅
  coordinator = getCoordinatorId()              current_in_CS = ⊥

upon event request()                          upon event pp2pDeliver(REQ, j) from pj
  state = waiting                               pending = pending ∪ {pj}
  trigger pp2pSend(REQ, i) to coordinator
                                              when pending ≠ ∅ and current_in_CS = ⊥
upon event pp2pDeliver(GRANT_CS)                candidate = select_process(pending)
  state = CS                                    pending = pending \ {candidate}
  trigger ok()                                  current_in_CS = candidate
                                                trigger pp2pSend(GRANT_CS) to candidate
upon event release()
  state = idle                                upon event pp2pDeliver(REL, j) from pj
  trigger pp2pSend(REL, i) to coordinator       if current_in_CS = j
                                                  current_in_CS = ⊥
```

- `current_in_CS = ⊥` means that nobody is in the CS: this is the guard that guarantees **mutual exclusion** (at most one GRANT outstanding).
- `select_process(pending)` decides the order. To guarantee **No-Starvation** it must be fair, e.g. **FIFO** in order of arrival; a choice that can skip a process forever would starve it.
- The `when` clause is a guard on the local state: it fires whenever the condition becomes true (after a REQ arrives or after a REL frees the CS).

> [!important] Simone's note (from last year's notes)
> "The next code is extremely important for the exam. 1/5 of the exam is writing a code like that."
> A worked exercise on a leader-based variant (with a coordinator that can change) is in [[DDS - Exercises 2]].

### Example

$p_2$ is the coordinator; $p_1$ and $p_3$ request the CS.

![[DDS-L05-p10.png]]

*$p_1$ calls `request()` and sends `(REQ, 1)`, but its message is slow. $p_3$ requests later and its `(REQ, 3)` reaches the coordinator first: `pending = {p3}`; since `current_in_CS = ⊥`, the coordinator removes $p_3$ from `pending`, sets `current_in_CS = p3` and sends `GRANT_CS` to $p_3$.*

![[DDS-L05-p16.png]]

*Complete execution. When `(REQ, 1)` arrives, `current_in_CS = p3` so $p_1$ stays in `pending = {p1}`. $p_3$ receives the grant, gets `ok()`, executes the CS, calls `release()` and sends `(REL, 3)`. The coordinator sets `current_in_CS = ⊥`, the `when` guard fires again and `GRANT_CS` goes to $p_1$, which enters the CS.*

The example shows that the order of access is the order in which requests **arrive at the coordinator**, not the order in which they were issued: $p_1$ asked first but entered second. This is still correct (the requests are concurrent).

### Discussion

**Performance:**

- entering the CS always takes **2 messages** (REQ and GRANT), i.e. **one RTT**;
- releasing takes **1 message** (REL); this message is the **synchronization delay** between two consecutive accesses (REL + GRANT, between one exit and the next entry).

![[DDS-L05-p17.png]]

| Pro | Cons |
|---|---|
| **Lightweight protocol** (3 messages per CS, independent of $N$) | **Potential scalability issues**: all requests go through one process (bottleneck) |
| | **The coordinator is a single point of failure (SPoF)**: if it crashes, nobody can enter anymore — and in an asynchronous system the others cannot even tell a crash from slowness |

The SPoF is the reason why, once we allow crashes, we need to **elect a new coordinator** — see [[6 - DDS - Failure Detection and Leader Election#Leader election (LE)|leader election]].

## Token-based algorithm on a logical ring

Vedi [[Token Ring Mutual Exclusion]].

**Basic idea:**

- a process interested in the CS can access it **only when it holds the token**;
- the token is **unique** and is passed between processes;
- to guarantee **fairness**, the messages of the protocol travel on a structured logical topology, a **ring**: the token visits every process in turn, so nobody can be skipped.

### Intuition of the algorithm

1. Build an **overlay** (a logical network) shaped as a ring on top of the existing point-to-point channels.
2. Create a token and insert it in the ring during **initialization** (assign it to one process).
3. When a process requests the CS:
   1. it waits until it gets the token;
   2. it enters the CS, and upon release it sends the token to its **next** on the ring.
4. If a process receives the token and is **not interested** in the CS, it simply passes it to the next.

### 1. Building the ring

The ring is obtained by:

- storing in a local variable the name of the **next** process in the ring;
- allowing communication **only with the next**.

![[DDS-L05-p20.png]]

*Left: the complete communication graph given by perfect links. Right: the overlay ring, where each process only knows $next_i = p_{(i+1) \bmod N}$ ($next_1 = p_2$, …, $next_5 = p_1$).*

```text
Init
  state = idle
  next = p(i+1) mod N
```

### 2. Creating the token

> [!warning] The token must be unique
> Two tokens would let two processes into the CS at the same time. So **only one process**, selected with a **deterministic function** that everybody computes in the same way (here: "I am $p_0$"), creates the token during init.

![[DDS-L05-p22.png]]

```text
Init
  state = idle
  next = p(i+1) mod N
  if self = p0
     trigger pp2pSend(TOKEN) to next
```

### 3–4. Requesting, using and passing the token

![[DDS-L05-p23.png]]

*$p_2$ calls `request()` (state = waiting). When the token arrives it enters the CS; at `release()` it forwards the token to $p_3$. A process that is idle just forwards the token.*

The complete algorithm:

```text
Init
  state = idle
  next = p(i+1) mod N
  if self = p0
     trigger pp2pSend(TOKEN) to next

upon event request()
  state = waiting

upon event pp2pDeliver(TOKEN)
  if state == waiting
     state = CS
     trigger ok()
  else
     trigger pp2pSend(TOKEN) to next

upon event release()
  state = idle
  trigger pp2pSend(TOKEN) to next
```

Why it is correct:

- **Mutual exclusion** — there is exactly one token, and only the holder can be in state CS.
- **No-Starvation** — the token travels around the ring; a waiting process gets it after at most $N-1$ other CS executions (each process holds it for at most one CS).

### Discussion

- The algorithm **continuously consumes communication resources**, even when nobody is interested in the CS: the token keeps circulating.
- The delay between `request()` and `ok()` varies between **0** messages (the token arrives right after the request) and **$N$** messages (the process just forwarded the token and must wait for a full round).
- Not discussed on the slides, but important for the rest of the course: if a process **crashes while holding the token**, the token is lost and must be **regenerated** — which again requires detecting the crash and agreeing on who creates the new token (failure detection + leader election).

## Quorum-based algorithm — Maekawa's voting algorithm

Vedi [[Maekawa's Voting Algorithm]].

**Basic idea:** to enter the CS a process does not need the permission of *all* the others (as in Ricart-Agrawala): it waits for the acknowledgement of a **subset** of processes, large enough to guarantee that two concurrent requests always **conflict** on at least one process.

Each process $p_i$ has a **voting set** $V_i$, with these properties:

- $p_i \in V_i$;
- $\forall i, j:\ V_i \cap V_j \neq \emptyset$ — every pair of voting sets has at least one common member;
- $|V_i| = K$ — all voting sets have the same size (fairness: **same load** principle);
- each $p_j$ is contained in $M$ voting sets (**same responsibility** principle).

> [!tip] Why the intersection gives mutual exclusion
> Each process **votes for one requester at a time** (`voted = true`). If $p_i$ and $p_j$ were both in the CS, each would have the votes of all its voting set; the common member $p_k \in V_i \cap V_j$ would have voted for both at the same time — impossible. This "two quorums always intersect" argument reappears for [[13 - DDS - Registers|registers]] and [[9 - DDS - Paxos|Paxos]] (majority quorums).

### Code

```text
Init
  state = released
  voted = false
  Vi = get_voting_set(i)
  replies = ∅
  pending = ∅

upon event request()
  state = wanted
  for each pj ∈ (Vi \ pi) do
     trigger pp2pSend(REQ, i) to pj

upon event pp2pDeliver(REQ, j)
  if state == held OR voted == true
     pending = pending ∪ {j}               // cannot vote now: queue it
  else
     trigger pp2pSend(ACK, i) to pj        // vote for pj
     voted = true

upon event pp2pDeliver(ACK, j)
  replies = replies ∪ {j}

when |replies| == |Vi| - 1
  state = held
  trigger ok()

upon event release()
  state = released
  replies = ∅
  for each pj ∈ (Vi \ pi) do
     trigger pp2pSend(REL, i) to pj

upon event pp2pDeliver(REL, j)
  if |pending| > 0
     candidate = select_next(pending)
     pending = pending \ candidate
     trigger pp2pSend(ACK, i) to candidate  // move my vote to the next one
     voted = true
  else
     voted = false
```

- `state` ∈ {released, wanted, held}: *held* means "in the CS".
- A process waits for $|V_i| - 1$ acks because it does not send a request to itself.
- On release, the process frees the votes of its voting set; every member then gives its vote to the next pending requester (or becomes free).

> [!note] About the requester's own vote
> In the version in Coulouris et al. (§11.2, the reference of the lecture), the requester multicasts the request to **all** of $V_i$, itself included, so it also has to obtain **its own vote** (it cannot use it if it already voted for someone else). In the slide code the request goes to $V_i \setminus \{p_i\}$ and the requester's own `voted` flag is not checked.

### How big must the voting sets be?

**Challenge:** how to choose $K$ and $M$ to balance load and responsibility?

- Maekawa showed that the optimal solution that minimizes $K$ while guaranteeing ME has
$$K \sim \sqrt{N}, \qquad M = K.$$
- A simple **approximation** gives $|V_i| \sim 2\sqrt{N}$:
  - place the processes in a $\sqrt{N} \times \sqrt{N}$ matrix;
  - $V_i$ = **union of the row and the column** containing $p_i$.

Any two "crosses" in a grid intersect: the row of $p_i$ crosses the column of $p_j$. So the intersection property holds by construction. The exact size is $2\sqrt{N} - 1$ (row + column, minus $p_i$ counted twice).

### Examples

**N = 4** ($M = K \sim \sqrt{4} = 2$, $|V_i| \sim 2\sqrt{4}$):

![[DDS-L05-p29.png]]

| Process | Matrix position | $V_i$ |
|---|---|---|
| $p_1$ | row 1, col 1 | $p_1, p_2, p_3$ |
| $p_2$ | row 1, col 2 | $p_1, p_2, p_4$ |
| $p_3$ | row 2, col 1 | $p_1, p_3, p_4$ |
| $p_4$ | row 2, col 2 | $p_2, p_3, p_4$ |

*The Venn diagram on the right shows that every pair of sets overlaps.*

**N = 9** ($M = K \sim \sqrt{9} = 3$, $|V_i| \sim 2\sqrt{9} = 6$): processes in a $3 \times 3$ matrix

| | | |
|---|---|---|
| $p_1$ | $p_2$ | $p_3$ |
| $p_4$ | $p_5$ | $p_6$ |
| $p_7$ | $p_8$ | $p_9$ |

| Process | $V_i$ |
|---|---|
| 1 | $p_1, p_2, p_3, p_4, p_7$ |
| 2 | $p_1, p_2, p_3, p_5, p_8$ |
| 3 | $p_1, p_2, p_3, p_6, p_9$ |
| 4 | $p_4, p_5, p_6, p_1, p_7$ |
| 5 | $p_4, p_5, p_6, p_2, p_8$ |
| 6 | $p_4, p_5, p_6, p_3, p_9$ |
| 7 | $p_7, p_8, p_9, p_1, p_4$ |
| 8 | $p_7, p_8, p_9, p_2, p_5$ |
| 9 | $p_7, p_8, p_9, p_3, p_6$ |

> [!note] $2\sqrt{N}$ vs the real size
> The slide writes $|V_i| \sim 2\sqrt{9} = 6$, while the table has 5 elements per set: the exact size is $2\sqrt{N} - 1 = 5$ ($p_i$ is in both its row and its column). $2\sqrt{N}$ is the asymptotic approximation.

### Maekawa's algorithm is not deadlock-free

![[DDS-L05-p31.png]]

*With $N = 4$: $V_1 = \{p_1,p_2,p_3\}$ and $V_4 = \{p_2,p_3,p_4\}$. $p_1$ and $p_4$ request concurrently. $p_2$ receives $p_1$'s request first and votes for $p_1$ (then $p_4$'s request goes in `pending = {p4}`); $p_3$ receives $p_4$'s request first and votes for $p_4$ (then `pending = {p1}`). $p_1$ waits for $p_3$'s vote, $p_4$ waits for $p_2$'s vote: nobody releases, nobody enters.*

This is a classic **circular wait** (compare the Coffman conditions in [[Condizioni di Coffman|SDC2]]). It violates **No-Deadlock**. The algorithm can be made deadlock-free (Sanders, 1987) by ordering the requests with **logical timestamps** — as in [[4 - DDS - Logical Clocks|Lamport/Ricart-Agrawala]] — and letting a process **withdraw** its vote from a request with a larger timestamp when one with a smaller timestamp arrives.

## Comparison

| Algorithm | Messages per CS | Delay request→entry (best case) | Main problem |
|---|---|---|---|
| Coordinator | 3 (REQ, GRANT, REL) | 2 messages (1 RTT) | bottleneck, SPoF |
| Token ring | 1 to $\infty$ (token always moving) | 0 to $N$ messages | wastes bandwidth, token loss |
| Lamport | $3(N-1)$ | 2 messages | needs every process |
| Ricart-Agrawala | $2(N-1)$ | 2 messages | needs every process |
| Maekawa | $3K \approx 3\sqrt{N}$ (REQ, ACK, REL to $V_i$) | 2 messages | **deadlock** |

All of them assume **no failures**: a crash of the coordinator, of the token holder, or of any process whose reply/vote is needed blocks the others forever.

## Reference

George Coulouris, Jean Dollimore, Tim Kindberg, Gordon Blair, *Distributed Systems: Concepts and Design* (5th ed.), Addison-Wesley, 2012 — Chapter 11, section 11.2.

## Core ideas to retain

- **Coordinator**: REQ → GRANT → REL; 3 messages; SPoF.
- **Token ring**: unique token created deterministically; enter only with the token; delay 0…N; wastes messages when idle.
- **Maekawa**: voting sets that pairwise intersect, $|V_i| \sim \sqrt{N}$ (grid: $2\sqrt{N}-1$); each process votes for one requester at a time → ME; **not deadlock-free**.
