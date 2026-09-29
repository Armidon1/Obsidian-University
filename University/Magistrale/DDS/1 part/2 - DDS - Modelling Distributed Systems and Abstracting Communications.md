---
title: "Dependable Distributed Systems — Modelling Distributed Systems and Abstracting Communications"
aliases:
  - "DDS Lectures 3 and 4"
tags:
  - distributed-systems
  - dependability
  - system-models
  - communication-abstractions
source: "DDS-Lecture3&4-2026-2027.pdf"
academic_year: "2026/2027"
---

# Dependable Distributed Systems: Modelling Distributed Systems and Abstracting Communications

> [!abstract] The through-line
> A distributed algorithm is meaningful only relative to a **system model**: which processes exist, how they communicate, what can fail, and what timing can be assumed. We then specify a useful **abstraction** by the properties its clients may rely on, implement it using weaker abstractions, and compose the layers. The second part applies this method to point-to-point communication: **fair-loss → stubborn → perfect links**.

## Lecture 3 — Modelling Distributed Systems

### Recap: what is a distributed system?

![[Pasted image 20260928121328.png]]

A distributed system is a collection of entities, computers, or processes that **communicate, coordinate, and share resources toward a common goal**, while presenting itself to users as one computing system. This appearance does not mean that there is one machine or one shared memory. Each participant has its own local state and sees only its own events and received messages. A distributed algorithm is the software that coordinates those participants and addresses the resulting communication and failure problems.

**Why this matters:** if machines cannot directly inspect one another's state, any agreement, delivery guarantee, or fault tolerance must arise from local steps plus communication. The user-facing service hides this complexity.

we need to write software in a away that allows that the users to coommunicate to our distributed system in a a way to let them think that it is a single server, also taking in account the fact that the software should be modular. The idea is that the server is distributed but the software is modular and shared, also considering replicas.

### System deployment

![[Pasted image 20260928121549.png]]

To realize a distributed system, software components must be instantiated and placed on actual machines. The choices range from a **centralized** arrangement to a **fully distributed** one; a deployed arrangement is a *system architecture*. Placement changes where communication occurs, where failures matter, and which resources can become bottlenecks. The same abstract service may admit several deployments.

The course focuses on properties of distributed abstractions and their algorithms; the specific language, machine placement, and middleware are separate implementation decisions. Thus, do not infer an algorithm's correctness solely from a particular deployment drawing.

if we consider the centralized one, everything is way more simple but obviously has its own limitations, and the exact same thing can be applied to the fully distributed one. so the idea is to learn the instruments to understande if we have to be in the middle of those two architectures.

### Architectural style

An architectural style describes:

1. **Components:** modular, replaceable units with specified required and provided interfaces.
2. **Connections:** how components are wired together.
3. **Exchanged data:** what crosses those connections.
4. **Configuration:** how the above form a complete system.

compoents can be abstarcted by their specification and their interfces.
A component can be reasoned about through its **specification** and **interface**, without exposing every implementation detail. Later, a perfect-link component will provide a strong interface while internally using a stubborn-link component. So we will deal just with a generical langiage, but the implementation can be with whatever language you want. In Software Engineering we will (maybe) see how to design the methodology and in the Lab of advacned programming of to implement it. 

### Why abstractions are important

Abstractions (1) capture properties shared by many systems. notice that we may want to use multiple langiages: one interface with python and another one in rust. this can be done due to the abstraction of mudles/interfaces. 

(2) separate essential constraints from incidental engineering choices,

(3) let designers reuse solutions instead of solving small variants from scratch. For example, “a message from a correct sender to a correct receiver eventually arrives exactly once” is a reusable contract; whether the network uses particular sockets, routes, or devices is a different question.So we move the effort from the effort on the design instead on the implementtion: the implementation is way easier once we have a nice and clear design.

Notice that when for istance we apply the ACID methodology, but in general also, we will find many bugs in the code. tipicaally is normal stuff when we deal with notrmal scripts or centralized applications, but in a distributed one is a real mess, so how to debutg in that scenario is another real thing. 



### The road to a distributed abstraction

1. **Define the system model:** identify relevant entities, their intrinsic properties, and their interactions. In this lecture these include processes, messages, failures, and timing. This means that you have to understand which enviroment are we considerign: if our peace of dofware is running in a datacenter, is way faster the communicaton, osmething that it is not if it is distributed arround the wordl. HERE WE DO NOT CARE ABOUT ALGORITHMS, BUT ONLY WHAT IT IS SUPPOSED TO DO THE SOWTFARE
2. **Design and specify a distributed abstraction:** identify recurring i(ricorrente) nteraction patterns, define its interface and guarantees, then develop a protocol that provides them under the model. IN HEERE WE CARE ABOUT ALGORITHMS. This can be done after we know the specification in step 1 and here we are implementing a pseudocode.
3. **Implement and deploy the algorithm:** choose concrete language, architecture, and perhaps middleware. This step depends on the target system. Here we implement the actual code. Notice that this is the coolest part, but the previous ones are too much importantf for optimization reasosn. MORE IN LAB AND SOFTWARE Engineering

The model is a set of **assumptions**, not a claim that every real system always behaves that way. The specification is a **promise** to clients, conditional on those assumptions. Confusing the two makes it easy to claim a guarantee that the implementation cannot provide.

### Composition model

we are not design a peace of code in general, but we will desing something upon events occurs. We have to think in terms of wvents. This is the most difficult part of the course. It is fundamental to know how to design an handler.

The lecture writes protocols in event-driven pseudocode. Components within one process exchange events; each component has event handlers that change local state and may `trigger` further events. A handler can be activated by an external event, by an event from another component, or by an internal condition. Instances such as `jh`, `fl`, and `pl` distinguish which component owns an event.

![[Pasted image 20260928123407.png]]
So for pur point of view, we are simply considering a set of components (a kind of black box) which interracts by each other due to an incoming event. So, each component should have its own handelr, and upon an event, does something (this is an example of API that the component who recieved the event is offering). Notice taht here we do not care the catual implementation. when a componetn generates an event for another component, we are trusting that component to do its job. when a component finises a specific task, it generates an event. 


![[Pasted image 20260928123620.png]]
Notice that obvously as a component i have to check if an event arrived while i was finiching something. 


```text
upon event ⟨component, Event | attributes⟩ do
    update local state
    trigger ⟨other_component, AnotherEvent | attributes⟩

upon internal condition do
    update local state
```

A guarded handler (`upon event ... such that condition`) acts only if its condition holds. An internal action (`upon condition`) is enabled by local state rather than a newly received message. When a proof needs eventual progress from such an action, it also needs a suitable **fairness/scheduling assumption**: an action that stays enabled must eventually run. The pseudocode is an abstract transition system, not a prescribed thread or callback implementation.

#### Programming interface: three kinds of events
![[Pasted image 20260928124210.png]]
![[Pasted image 20260928124224.png]]



| Event            | Direction and purpose                                                                                                                                                                                                                                                                                 | Example                                                     |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| **Request**      | A client asks a component to perform a service. it is used by another component to generate an event on another compponent. Notice tha TCP and UDP doesn't guarantee the ordering.                                                                                                                    | `Submit(job)` or `Send(q, m)`                               |
| **Confirmation** | A component acknowledges completion of a request, according to that interface's exact meaning. Tipically it is paiered with a Request event.                                                                                                                                                          | A completion acknowledgment                                 |
| **Indication**   | A component reports information to a client, possibly as a result of an earlier request or an external occurrence. It is something that the box notify to the user. No Events triggers the indication: it is the componetnts itself that send the status of the task that it is working on currently. | `Deliver(p, m)` or `Confirm(job)` in the job-handler module |

The words *confirmation* and *indication* describe interface roles; the exact event name is not sufficient to determine its semantics. In the example below, `Confirm(job)` is written as an **indication**, and its contract deliberately allows “processed **or will be** processed.” Never assume a `Confirm` event implies that physical processing has already finished unless the specification says so.

### Example: job handler

![[Pasted image 20260928124703.png]]

The `JobHandler` module (instance `jh`) accepts a request `⟨jh, Submit | job⟩` and emits an indication `⟨jh, Confirm | job⟩`. Its property **JH1 — Guaranteed response** says: every submitted job is eventually confirmed. The interface says that the job *has been or will be processed*; JH1 alone does not establish completion before confirmation, exactly-once processing, or a bound on response time.

notice that the JH1 is the contract to the user that that property will be respected.

#### Synchronous implementation
This means that the user is waiting your reaspons. it s trivial.

![[Pasted image 20260928124946.png]]

```text
upon event ⟨jh, Submit | job⟩ do
    process(job)
    trigger ⟨jh, Confirm | job⟩
```

Here processing occurs within the submit handler before the confirmation is triggered. This makes the confirmation follow processing, but the request handler remains occupied while `process` runs. Event “synchronous” here describes this implementation's sequencing; it should not be confused with the **synchronous system model** discussed later.

It is trivail also beacausse of every event that i know, there should be a module an handelr for an incoming arrow and something for an outgoing arrow. Notice that i have to queuing the incoming events while i have to complete the current job. This may occur an huge latency

#### Asynchronous implementation

Here i want to reduce latency, moving the queue inside. 

![[Pasted image 20260928125325.png]]

```text
upon event ⟨jh, Init⟩ do
    buffer := ∅

upon event ⟨jh, Submit | job⟩ do
    buffer := buffer ∪ {job}
    trigger ⟨jh, Confirm | job⟩

upon buffer ≠ ∅ do
    job := selectjob(buffer)
    process(job)
    buffer := buffer \ {job}
```

This confirms on acceptance into the buffer; an enabled internal action subsequently processes a job. It illustrates why the specification permits “will be processed.” Guaranteed eventual **processing** requires that buffered work is eventually selected and that `process` completes; these progress conditions are additional to simply inserting into a set. A literal set also collapses identical jobs, so distinct submissions should carry distinct identities if both must count separately.

it not that hard: we have an initialization, when comes an event, i'll just put it in my buffer and confirm the job, and until the buffeer is not empty, i'll pop one of them and create an event. 

### Example: layering a transformation handler over the job 

![[Pasted image 20260928125615.png]]

`TransformationHandler` (instance `th`) **implements** an upper interface while **using** `JobHandler` (instance `jh`) below it. The upper request is `⟨th, Submit | job⟩`; its indications are `⟨th, Confirm | job⟩` and `⟨th, Error | job⟩`.

- **TH1 — Guaranteed response:** every submitted job is eventually confirmed or its transformation fails.
- **TH2 — Soundness:** a job whose transformation fails is not processed.

The layering diagram has two boundaries: the client talks to `th`, while `th` sends `Submit` to `jh` and receives `jh`'s `Confirm`. An indication from the lower component must be interpreted under the *upper* interface's contract before exposing it to the client.

![[Pasted image 20260928125910.png]]
notice that i have 2 incoming events, so for sure i have to deal with them. The same i have to check i have 3 outgoing so i have to check if i actually oroduce them: obvously is not something that confirms that my implementation is correct. 


The lecture's **“Job-Transformation by Buffering”** pseudocode initializes a circular buffer of size `M`, counters `top` and `bottom`, and a `handling` flag. On `th.Submit(job)`, a full buffer (`bottom + M = top`) produces `th.Error(job)`; otherwise the job is enqueued, `top` advances, and `th.Confirm(job)` is emitted. An internal action, when `bottom < top` and no lower job is being handled, dequeues the next job, sets `handling := TRUE`, and calls `jh.Submit(job)`. On `jh.Confirm(job)`, it resets `handling := FALSE`. Buffer indexing wraps with `counter mod M + 1` in the displayed algorithm.

**Interpretation:** this example teaches composition, buffering, and backpressure. An immediate upper confirmation means acceptance into the upper buffer, while the lower confirmation permits the next dispatch. The displayed pseudocode does not show a separate transformation operation or a transformation-failure branch beyond rejecting a full buffer, so do not infer a concrete transformation procedure from it. Liveness depends on fair scheduling of the internal dispatch and the lower handler's promised response; a finite buffer may reject submissions even if the lower handler is otherwise correct. As with the simpler handler, real code would need unambiguous job identities and careful treatment of counter wraparound and resource bounds.

### Modelling distributed computations

![[Pasted image 20260928130517.png]]

The lecture now fixes four ingredients before designing further algorithms:

1. Processes and their interactions. For instance we have a shared memory for IPC but in a distributed enviroment we have a virtual shared memroy (we will see in the end of the couse an example of virtual shared memory) 
2. Specifications as **safety** and **liveness** properties. I have to chek if a comonent is still alive for instance.
3. Failure models. If a System dies, well i will have to deal with **chrash failures** and know how to manage them and also we ave **arbitrary failures**. 
4. Timing assumptions. Deelays are unpredictable, so we have to design the algorithm in a way to take in account that you have no idea the actual delay.

Each ingredient narrows what can be proved. When reading a later link property, identify its quantifiers (“correct sender/receiver,” “infinitely often,” “eventually”) and the model assumptions that support it.

### Processes
for a moment, every process is running i a different machine and a failure may occur, now we are not dealing with the [[Dependability]] property. They may fail, we may have replicas but we are not dealing with the refreshing those dead reaplicas. This simplyfies a lot the learning process.

![[Pasted image 20260928130840.png]]

Let $\Pi$ denote the set of processes and $N = |\Pi|$. Unless stated otherwise, membership is **static** and every process knows the identities of all members. A function $\operatorname{rank}:\Pi\to\{1,\ldots,N\}$ may assign a unique index to each process. `self` in an algorithm is the identity of the process executing that local code. Notice that we are just denoting each process with a number, but we can denote in whatever way we want. $p1$ is the process 1.  if in the description algotithm we have a "self" we are denoting the name of the process that it is executing that algorithm.

These assumptions simplify addressing and membership reasoning. A real system that dynamically joins or removes machines would need an additional membership abstraction or a different model. `self` is local: the same pseudocode can run at every process while referring to different identities.

### Process interactions and messages
Now our IPC is just message passing. So we are considering the fact that there exists a message communication link between 2 processes.  In concurred threads we were used to share variables, but here each process has it's own local varibales and communicate to each other over a link. We may assume that that communication link could not be [[Reliability]], so we have to made it reliable with our algorithm. Notice that if i ask, i have to wait for a response: in that period of time it can happen may things. 
![[Pasted image 20260928131358.png]]

Processes exchange messages over communication links. Messages are **uniquely identified** throughout an algorithm's execution, for example by combining a sender identifier with a monotonically increasing sequence number or logical counter. Distinct sends must be distinguishable even when their payloads are equal.

This identity convention is central to duplicate suppression: a receiver must tell a retransmitted copy of *one* message from a separate legitimate message with the same content. The link abstraction hides network details but does not make message loss, duplication, or delay disappear unless its specification promises that.

### Distributed algorithms

the professor said that our algorithm cna be represented as an finite state of automaton: obvoiusly it means that every process has its own state and we could possibly have millions of possible automata states.

![[Pasted image 20260928131707.png]]

A distributed algorithm is a collection of automata, **one per process**. Each automaton describes local state and the steps a process takes, including reactions to messages. The lecture assumes every process uses the same automaton; different identities, inputs, and local histories still yield different states. An execution is an interleaving or sequence of process steps. There is no assumption here that all processes execute a step together or see a single global state.

A property of an algorithm refers to **executions** allowed by the system model. To establish correctness, one must show that all relevant allowed executions satisfy the specification, including adverse schedules and failures within the chosen bounds.

### Safety and liveness

- **[[Safety]]:** “nothing bad happens.” A violation has a **finite bad prefix**: once the violating finite history has occurred, extending that history cannot undo it. **Notice that a process that does nothing satisfies the [[Safety]] property**: that's why [[Liveness]] is important. Example: delivering a forged message, or delivering the *same uniquely identified* message twice under a no-duplication contract. For every possibile sceinario the safety property HAS TO BE SATISFIED. We have to prove them. If we find one execution that prooves that in tha tcase we dont have safety, we dont have safety in general. It is extremmely hard, but must be provided.
- **[[Liveness]]:** “something good eventually happens.” No finite prefix by itself rules out future success: after any finite delay there is still a possible continuation in which the obligation is met. Example: a message from a correct sender to a correct receiver is eventually delivered.

In this course won't enhance the formal proof sometimes: we will see something that shows how to prove those properties on a specific algotithm, but not that much.

For a perfect link, **no creation** and **no duplication** are safety properties; **reliable delivery** is liveness. A run may be safe yet make no progress. Conversely, eventual delivery cannot excuse an earlier duplicate. “Eventually” imposes no numeric deadline unless timing assumptions provide one. A liveness claim usually depends on conditions such as correct processes, fair message delivery, and scheduling of enabled local actions.

### Failure models (we will continue later here)
The lecture distinguishes the following behaviors:

| Failure behavior | What can go wrong |
| --- | --- |
| **Crash (crash-stop)** | A process stops executing permanently. |
| **Omission** | An expected message is not sent or received. |
| **Crash and recovery** | A process stops and later restarts, possibly repeatedly. |
| **Eavesdropping** | Information learned in the algorithm leaks to an outside entity. |
| **Arbitrary / Byzantine** | A process may behave in ways not prescribed by its algorithm, including inconsistent or malicious behavior. |

These are different contracts about faulty behavior, not interchangeable synonyms. An algorithm proved for crashes does not automatically tolerate arbitrary messages from a Byzantine process. The communication abstractions in the next lecture are stated under a **crash-failure** setting.

### Crash fault: the crash-stop abstraction

A process crashes at some time $t$ and **never recovers** within the crash-stop model. A process is **faulty** if it crashes during the execution. It is **correct** if it never crashes and executes infinitely many steps. Thus “correct” includes continuing to make progress, rather than merely having stayed alive up to the current instant.

A property qualified by “correct process” does not necessarily promise delivery to a receiver that crashes or after a sender stops forever. This restriction is essential: no algorithm can force a permanently stopped receiver to execute a delivery event.

### Dependability and crash faults: resilience

Fault tolerance is one way to obtain dependability: the algorithm should satisfy its stated properties despite allowed faults. Let $f$ be the assumed **upper bound** on faulty processes out of $N$. The relation between $f$ and $N$ is called the algorithm's **resilience** (often stated as a threshold or condition involving both). “At most $f$” includes all cases from zero through $f$ faults, with any permitted choice of failing processes. The actual threshold required depends on the problem and model; this lecture does not assert one universal value.

### Crash-stop versus crash-recovery

Physical machines can restart. Under the **crash-stop abstraction**, a restarted machine is not treated as the return of the original process for that algorithm. This does **not** ban restart in the deployment. It means that correctness and progress do not **rely on** a crashed process recovering. A higher layer might use the machine again under a new process identity or separate recovery protocol.

In a **crash-recovery** model, a process is faulty if it never recovers after crashing, or if it crashes and recovers infinitely often. A process that crashes and recovers only finitely many times is considered **correct** under the lecture's definition (given the intended continued execution afterward). “Correct” therefore has model-dependent meaning; read it with the current failure model.

#### Recovery, amnesia, and stable storage

A recovered process may suffer **amnesia**: volatile local state disappears. Without recovery logic it might issue a new message contradicting what it sent before a crash, or repeat a message it previously emitted. To preserve relevant state, algorithms may assume stable storage or a **log** accessed by `store()` and `retrieve()`. The lecture also assumes that a recovering process can tell that it has recovered.

Durability is not automatic merely because a variable was assigned. A recovery-aware algorithm must decide what to persist and in what order relative to sending or confirming operations. This is why the failure model changes algorithm design rather than just the deployment procedure.

### Timing assumptions

Timing determines what can be inferred from a delay. A slow response could indicate failure, a slow process, or a delayed message; without bounds, those cases cannot generally be distinguished by waiting a fixed amount of time.

#### Synchronous systems

A synchronous model has **known upper bounds** on:

1. The time for a process to perform a basic computation step.
2. The communication delay for a message to reach its destination.
3. The drift of each local physical clock relative to real time.

Together these support timed failure detection, measuring transit delays, time-based coordination, worst-case performance bounds (including under modeled failures), and synchronized clocks. A timeout is meaningful only when its bound covers the relevant processing, communication, and clock uncertainty.

The hard engineering problem is **coverage**: do the assumed bounds actually hold for the components and operating conditions of the real system, with the needed confidence? A proof under synchronous bounds cannot rescue an execution in which a bound is violated.

#### Asynchronous systems

An asynchronous model makes **no timing assumptions** about processes or communication links. It does not mean that processes never run or that no message ever arrives; it means the model supplies **no known finite upper bound** on how long a step or delivery can take. Therefore, a timeout alone cannot conclusively distinguish a crash from extreme delay.

One may still order events using communication: a local event precedes a later event at the same process, and sending a message precedes its receipt. **Logical time** records such causal relationships without claiming to measure seconds or a global physical time. This is the motivation for logical clocks.

#### Partial (eventual) synchrony

Partial synchrony models systems that sometimes behave within timing bounds and sometimes do not. One formal form, **eventual synchrony**, posits an **unknown** time after which the relevant synchrony bounds hold. The lecture warns against reading the simplified description as a literal prediction that all hardware, software, and network components become permanently synchronous at a known point, or that the execution neatly begins in a single asynchronous phase followed by a single synchronous phase.

Operationally, the desired progress argument is that there is a **sufficiently long period of synchrony for the algorithm to terminate**. Before such a period, retries or timeouts may be misleading; safety should still hold, while liveness may wait for favorable timing. Distinguish the exact eventual-synchrony assumption used in a formal theorem from this intuition of a long enough good interval.

#### Summary of timing models

| Model | Computation / communication / clocks | Consequence for reasoning |
| --- | --- | --- |
| **Synchrony** | Known upper bounds on computation time, message delay, and clock drift. | Timeouts and worst-case deadlines can be justified if bounds hold. |
| **Partial synchrony** | Bounds become usable after an unknown point, or there is a sufficiently long stable interval in the lecture's intuition. | Eventual progress can be argued once timing is favorable; earlier delays remain ambiguous. |
| **Asynchrony** | No known bounds of these kinds. | Reason from event order and messages, not fixed physical-time deadlines. |

#### Reference for this part

C. Cachin, R. Guerraoui, and L. Rodrigues, *Introduction to Reliable and Secure Distributed Programming*, Springer, 2011, Chapter 2, Sections 1, 2, and 5 (as cited in the lecture).

## Lecture 4 — Abstracting Communications

### Link abstraction

A **link** is the interface by which one process sends a message to another. At the abstract level, each pair of processes has a bidirectional link. This does **not** require one direct physical cable per pair: a routing algorithm may realize the apparent link over a more complex topology. The lecture illustrates both richly connected and sparser topologies to separate the client-facing communication abstraction from its physical realization.

A bidirectional connection can be considered as two directed send paths for specifying behavior: guarantees about sending from $p$ to $q$ should be read for that direction. The abstraction lets higher layers reason about `Send` and `Deliver` instead of raw network buffers, packet routes, and retransmission details.

### Link abstractions under crash failures

The lecture builds three progressively stronger services:

1. **Fair-loss link:** a message may be lost, but repeated sends between correct processes have a fairness guarantee; delivered copies can be duplicated finitely.
2. **Stubborn link:** a one-time upper-level send is repeatedly attempted, so correct endpoints eventually see infinitely many deliveries of that message.
3. **Perfect link:** a one-time send eventually produces one upper-level delivery, without duplicates or invented messages.

The strengthening is achieved by **composition**: retransmit over fair-loss to get stubborn delivery, then suppress duplicates over stubborn delivery to get a perfect link. “Stronger” means a stronger contract at the upper interface, not a change to the underlying network's physical behavior.

### System model for the links

The immediate picture has **two processes**, a sender and a receiver, communicating through a link. Messages can be lost and have an unpredictable delivery time. Processes may crash. A process's operation takes bounded time, although the bound may be **unknown**. This last distinction matters: a finite but unknown bound is not automatically a known timeout for detecting a crash. The specification below explicitly conditions progress on correct endpoints.

### Generic link interface: send versus deliver

A point-to-point link accepts `Send(q, m)` at the sender and emits `Deliver(p, m)` at the receiver, identifying the destination $q$ and source $p$. The upper-layer **delivery** is not the same event as a network-card **receipt**. A raw packet may arrive at a port and enter a buffer; link code may then validate, deduplicate, or otherwise process it before emitting `Deliver` to its client.

This boundary is why one can receive the same packet many times internally yet deliver the identified message exactly once at the perfect-link interface. The lower and upper events in the pseudocode (`fl`, `sl`, `pl`) refer to different layers.

### Fair-loss point-to-point link: specification

The module is `FairLossPointToPointLinks`, instance `fl`:

- **Request:** `⟨fl, Send | q, m⟩` — send message $m$ to process $q$.
- **Indication:** `⟨fl, Deliver | p, m⟩` — deliver message $m$ attributed to sender $p$.

Its three properties are:

| Property | Precise promise | Why it matters |
| --- | --- | --- |
| **FLL1 — Fair-loss** | If a **correct** $p$ sends the **same identified message** $m$ infinitely often to a **correct** $q$, then $q$ delivers $m$ infinitely often. | Repeated attempts cannot all disappear forever. It says nothing comparable about just one send. |
| **FLL2 — Finite duplication** | If correct $p$ sends $m$ a finite number of times to $q$, then $q$ cannot deliver $m$ infinitely many times. | The link cannot turn finitely many attempts into endless duplicates. It does not promise zero duplicates. |
| **FLL3 — No creation** | If $q$ delivers $m$ with sender $p$, then $p$ previously sent $m$ to $q$. | The link cannot invent an attributed message. |

The informal phrase “nonzero chance” motivates the name, but **FLL1 is the actual execution-level guarantee used in proofs**; a positive probability on each send alone does not, without further assumptions, establish every required infinite-run property. A fair-loss link allows an individual message to be lost, and one physical or abstract send may yield more than one delivery.

### Fair-loss point-to-point link: issues

To obtain eventual delivery from a fair-loss link, a sender must retransmit. The fair-loss specification provides no acknowledgment or other rule proving when retransmissions may safely stop: a finite number of attempts may all be lost. Hence the straightforward implementation **retransmits forever**. Repeated transmissions can produce repeated deliveries, so an upper layer must filter duplicates if it promises exactly-once delivery.

These two issues motivate the next two abstractions: **stubborn links** solve the repeated-attempt side; **perfect links** solve the duplicate-delivery side. “Quiescent” would mean eventually ceasing communication for an operation; the presented retransmit-forever algorithm is deliberately not quiescent.

### Stubborn point-to-point link: specification

The module is `StubbornPointToPointLinks`, instance `sl`, with request `⟨sl, Send | q, m⟩` and indication `⟨sl, Deliver | p, m⟩`.

- **SL1 — Stubborn delivery:** if a **correct** $p$ sends $m$ **once** to a **correct** $q$, then $q$ delivers $m$ **infinitely many times** at the stubborn-link interface.
- **SL2 — No creation:** if $q$ delivers $m$ attributed to $p$, then $p$ previously sent $m$ to $q$.

“Infinite deliveries” is intentional, not an error: the service converts a single upper request into persistent attempts and passes the successful lower deliveries upward. This is useful as an intermediate abstraction, even though a client wanting one notification would not consume it directly.

### Stubborn point-to-point link: implementation by retransmitting forever

This algorithm implements `sl` using `fl`. At each process it keeps a set `sent` of destination-message pairs and periodically retries every stored pair:

```text
upon event ⟨sl, Init⟩ do
    sent := ∅
    starttimer(Δ)

upon event ⟨Timeout⟩ do
    for each (q, m) ∈ sent do
        trigger ⟨fl, Send | q, m⟩
    starttimer(Δ)

upon event ⟨sl, Send | q, m⟩ do
    trigger ⟨fl, Send | q, m⟩
    sent := sent ∪ {(q, m)}

upon event ⟨fl, Deliver | p, m⟩ do
    trigger ⟨sl, Deliver | p, m⟩
```

The first send is immediate; later timer expirations resend. `sent` is never cleared in this simple algorithm. If correct processes continue to take steps, the timer fires repeatedly and each stored message is sent infinitely often, **FLL1** yields infinitely many lower deliveries to a correct receiver, and forwarding gives **SL1**. **FLL3** plus the fact that only previously requested pairs are passed down gives **SL2**. These arguments need timer/scheduling progress; $\Delta$ determines retry cadence, not a reliable failure-detection deadline. Memory and traffic grow with the number of distinct stored messages, a limitation of this teaching implementation.

### Perfect point-to-point link: specification

The module is `PerfectPointToPointLinks`, instance `pl`, with request `⟨pl, Send | q, m⟩` and indication `⟨pl, Deliver | p, m⟩`.

| Property | Precise promise | Class |
| --- | --- | --- |
| **PL1 — Reliable delivery** | If correct $p$ sends $m$ to correct $q$, then $q$ **eventually** delivers $m$. | Liveness |
| **PL2 — No duplication** | No process delivers the **same message** more than once. | Safety |
| **PL3 — No creation** | If $q$ delivers $m$ with sender $p$, then $p$ previously sent $m$ to $q$. | Safety |

“Exactly once” is a compact intuition for the specified correct-endpoint case: **at least once eventually** (PL1) plus **at most once** (PL2), with authenticity of origin in PL3. It does not impose a deadline, guarantee delivery to a process that has stopped forever, or claim that application processing and its side effects are exactly once.

### Perfect point-to-point link: implementation by eliminating duplicates

The perfect layer calls the stubborn layer and keeps a receiver-side set of messages already delivered to its client:

```text
upon event ⟨pl, Init⟩ do
    delivered := ∅

upon event ⟨pl, Send | q, m⟩ do
    trigger ⟨sl, Send | q, m⟩

upon event ⟨sl, Deliver | p, m⟩ do
    if m ∉ delivered then
        delivered := delivered ∪ {m}
        trigger ⟨pl, Deliver | p, m⟩
```

**Why it works:** for correct endpoints, **SL1** produces infinitely many lower deliveries after one send, so at least the first produces an upper delivery (**PL1**). After the first, $m$ is in `delivered`, so later lower copies are ignored (**PL2**). **SL2** ensures every forwarded message traces back to a send (**PL3**). Atomic local handling of the membership check and insertion is assumed in this abstract automaton.

The notation `m ∈ delivered` relies on the lecture's global **unique-message identity** assumption. If an implementation uses only payload equality, two legitimate messages with identical payloads could be incorrectly merged. A practical key often includes a sender ID and sequence number. The simple `delivered` set also grows over time; garbage collection or bounded identifiers requires extra protocol reasoning, especially with retries and recovery. This algorithm is presented in the crash-stop setting; after a receiver restart, preserving deduplication may require stable state and a revised recovery proof.

### How the three layers fit together

| Upper service | Uses | Added mechanism | Guarantee a client gains |
| --- | --- | --- | --- |
| Fair-loss `fl` | Underlying communication | Assumed base abstraction | Fairness under infinite sends; finite duplication; no creation |
| Stubborn `sl` | Fair-loss `fl` | Store every send and retransmit indefinitely | One upper send leads to infinitely many upper deliveries for correct endpoints |
| Perfect `pl` | Stubborn `sl` | Record delivered message IDs and suppress repeats | One upper send leads to exactly one eventual upper delivery for correct endpoints |

A useful proof pattern is **assume the lower contract, prove the upper contract**. Trace each upper event to the lower event(s) that caused it, show safety by excluding forbidden traces, and show liveness by following progress through every layer. The client sees only the upper interface: repeated raw deliveries may continue indefinitely without repeated perfect-link deliveries.

#### Reference for this part

C. Cachin, R. Guerraoui, and L. Rodrigues, *Introduction to Reliable and Secure Distributed Programming*, Springer, 2011, Chapter 2, Section 4 through 2.4.4 (as cited in the lecture).

## Conceptual checklist

When you encounter a new distributed algorithm, ask:

1. **Model:** Who are the processes, what are the message identities, which processes count as correct, and which failure and timing assumptions are in force?
2. **Interface:** Which events are requests and which are indications or confirmations? At which layer is an event emitted?
3. **Specification:** Which obligations are safety (“never”) and which are liveness (“eventually”)? What do the quantifiers and preconditions actually say?
4. **Implementation:** What local state and event handlers turn a weaker service into the promised stronger one?
5. **Proof and limits:** Which lower-layer guarantee justifies each upper-layer property? What fairness, storage, or scheduling assumptions are needed? What would change under crash-recovery or a finite resource budget?

> [!tip] One-sentence synthesis
> Model the environment, specify the promise, implement it with local event handlers and weaker components, then prove that every permitted execution respects the promise.
