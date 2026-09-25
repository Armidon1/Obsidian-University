---
title: Dependable Distributed Systems — Introduction
course: Dependable Distributed Systems
academic_year: 2026/2027
tags:
  - distributed-systems
  - dependability
  - computer-science
---

# Dependable Distributed Systems — Introduction

> [!abstract] Purpose of this note
> This note follows the order of the introductory presentation and expands its key ideas. It introduces the course, explains why distributed systems are built and what makes them difficult, then develops the concepts of dependability and the main design challenges of dependable distributed systems.

## General Information

### Course structure

The course is **Dependable Distributed Systems**, part of the Master of Science in Engineering in Computer Science for academic year **2026/2027**. It is worth **9 CFU**, all taught in the first semester. The dates shown in the presentation are **23 September–22 December**.

The course is taught by **Silvia Bonomi** ([website](https://bonomi.diag.uniroma1.it)) and **Andrea Vitaletti** ([website](https://andreavitaletti.github.io)).

### Schedule and location

The schedule in the presentation is:

| Day | Time | Room |
|---|---:|---:|
| Monday | 12:00–14:00 | 29 |
| Wednesday | 10:00–13:00 | 11 |
| Thursday | 12:00–15:00 | 29 |

All lectures are listed as taking place at **San Pietro in Vincoli, Via Eudossiana 18**. These are course-specific logistics, so consult the current course announcements if you are reading this in another academic year.

### Course material

The slides say that course material will be shared through **Google Classroom**. The class code shown is `jeskyplw`. The expected material includes:

- the main textbook, *Introduction to Reliable and Secure Distributed Programming* by Christian Cachin, Rachid Guerraoui, and Luís Rodrigues (Springer, 2011);
- scientific papers, which supply research-level treatments and examples;
- supporting lecture slides.

The textbook is indicated as available for reference at the DIAG library. The materials complement one another: a textbook builds systematic foundations, papers expose specific results and designs, and slides organize the lecture topics.

### Students' hours and communication

For an appointment, contact the instructors by email and use a clear, specific subject line so the request is easy to identify. The slides also recommend Classroom messages: answers there may benefit other students who have the same question. Short questions can be asked before or after lectures and during breaks.

The instructors' offices are listed at **DIAG, Via Ariosto 25**:

- Silvia Bonomi: room B114, first floor, B wing.
- Andrea Vitaletti: room B206, second floor, B wing.

### Exam

The exam is a **written test**. Questions may cover any topic in the final syllabus. The presentation says the final syllabus will be published at the end of the course and will reflect the topics that the lectures manage to cover. The practical implication is to follow course announcements and not assume that this introductory presentation alone defines the complete exam scope.

## Distributed Systems

### From concurrent to distributed systems

A concurrent system allows multiple computations to make progress during overlapping periods. On a single machine, concurrent processes may share memory and use the same physical processor or multiple processors. The operating system and hardware provide mechanisms for scheduling, communication, and access to shared state.

A distributed system also contains concurrent computations, but its components are **separate computers** connected by a communication network. Instead of directly reading the same physical memory, components exchange messages. Each computer has its own processor, memory, and local view of the system.

This shift matters because the network introduces delay, message loss, reordering, and partial failure. A local shared-memory operation is not equivalent to sending a message to another machine: the sender cannot assume the receiver is active or that the message will arrive within a fixed time. Distributed design therefore has to make communication and coordination explicit.

### Definitions

The presentation brings together several complementary definitions:

- A distributed system is a set of spatially separate entities with computational power that communicate and coordinate to achieve a common goal.
- It can be viewed as autonomous computers connected by a network and middleware, sharing resources and coordinating their activities so users experience one integrated computing facility (Wolfgang Emmerich).
- It is software that makes a collection of independent computers appear to users as one coherent system (Maarten van Steen).
- A distributed system can expose users to failures in remote computers they may not even know exist (Leslie Lamport).

These definitions emphasize both the **implementation** and the **user experience**. Under the hood there are independent machines and network interactions; at the service boundary, the goal is to offer useful unified behavior. The last definition highlights that distribution creates failure dependencies: a remote component can affect a local user-visible service.

### Common points across definitions

The recurring elements are:

- **Multiple entities:** computers, processes, or other computational nodes.
- **Communication and coordination:** components exchange information and arrange their actions.
- **Resource sharing:** data, computation, storage, or services can be used across the system.
- **A common goal:** the parts cooperate to deliver an application or service.
- **A coherent view:** users are ideally given a consistent, understandable way to use the whole system.

The goal of a coherent view does not mean that the underlying system has become literally centralized. It means that the design provides abstractions and rules that make the distributed implementation usable.

### Why distributed systems?

The presentation gives two broad motivations: **increasing performance** and **building dependable services**.

#### To increase performance and capacity

Demand for processing power and data storage can exceed what one computer can economically or practically provide. A system can divide work among multiple machines, add storage nodes, or place services closer to their users. This is the basis for scaling out: capacity grows by adding resources to a coordinated system.

Adding computers does not automatically make an application faster. Work must be parallelizable, nodes need to communicate, and coordination itself consumes time and resources. Distributed computing is valuable when the resulting gains in capacity, throughput, or availability outweigh these costs.

#### To reduce latency

Users may be geographically far from the data or service they need. If every request must travel to one distant central location, network travel time can dominate the response time. Placing replicas or service instances nearer to users can reduce that delay.

Latency is the time between an action and its response. It depends on more than distance: network congestion, routing, processing, storage access, and queuing all contribute. Reducing latency often requires decisions about where data and computation should live and how copies are kept sufficiently current.

#### To cope with failures

Computers, network links, power supplies, and software can fail. A service that depends on one machine may become unavailable when that machine fails. Replication and redundancy can let another component continue the work, provided the system can detect failures and coordinate a safe transition.

Redundancy alone is not enough: copies can disagree, fail together, or be promoted incorrectly. Dependability therefore includes both architectural choices, such as replication, and protocols for managing those choices.

### Distributed systems in practice

The **Internet** is a familiar, large-scale distributed system: it connects many independently administered networks and devices that communicate using common protocols. Applications built on it may also be distributed systems in their own right.

Two systems can both be distributed while differing greatly in scale, ownership, topology, membership, and communication guarantees. For example, an industrial control network may have a known and relatively fixed set of devices, while a public Internet service may interact with changing populations of clients and data centers. Their requirements and failure assumptions are different, so the same design cannot be applied blindly to both.

### Questions to ask about a distributed system

Before choosing algorithms or guarantees, clarify the system's assumptions:

- Are the participating nodes known in advance, or can new nodes join dynamically?
- Are nodes expected to remain active, or can they disconnect and return?
- Can messages be lost? If they arrive, is there a known upper bound on delivery time?
- Can a message be corrupted, duplicated, or reordered?
- Can the receiver verify the sender's identity and the integrity of the message?
- Is there a meaningful order for events observed at different nodes?
- Can participants behave maliciously, or are failures assumed to be accidental?

These questions define the **system model**: the assumptions under which a distributed protocol is designed and analyzed. A guarantee is meaningful only relative to such assumptions. For example, a protocol may guarantee delivery if the network eventually recovers, while no protocol can guarantee timely delivery through a permanently broken connection.

### Characteristic: a collection of autonomous computing elements

Nodes in a distributed system operate independently. There is no single machine with direct, instantaneous knowledge of every component's state. Important challenges follow:

- **No global clock:** each node has its own clock, which may drift. Timestamps from separate machines do not automatically provide a perfect global ordering of events.
- **Group membership:** the system needs a way to know which nodes are considered members and how membership changes are handled.
- **Closed and open groups:** a closed group has a defined membership or controlled entry; an open group allows participants to join more freely. This changes the assumptions for coordination and trust.
- **Overlay networks:** applications may construct a logical network on top of the physical network. The overlay's organization affects how nodes find and communicate with one another.
- **Structured and unstructured overlays:** structured overlays impose rules on placement and lookup, while unstructured overlays rely on looser relationships among nodes. The trade-off is often between efficient, predictable operations and flexibility.

Autonomy is the source of both opportunity and difficulty: independent nodes can provide parallelism and resilience, but they must coordinate using incomplete and delayed information.

### Characteristic: a single coherent system

A distributed system is coherent when its behavior matches users' reasonable expectations. The collection should appear to operate in a consistent way regardless of where, when, or how the user interacts with it.

This is an **abstraction goal**, not a guarantee that all interactions are identical in every circumstance. Network partitions, replicas, delays, and failures may be observable. Designers choose which details to hide, which guarantees to provide, and how to communicate unavoidable limits. Failures are the central challenge because one part may stop while others continue.

### Middleware and distributed systems

**Middleware** is software that sits between applications and the lower-level operating system/network facilities. It can provide communication abstractions and common services, allowing:

- components of one distributed application to communicate;
- different applications to exchange information or use one another's services;
- applications to work across different hardware and operating systems with fewer platform-specific details.

Middleware does not eliminate the network's limits. It packages recurring mechanisms behind interfaces so application developers can work at a more useful level, while the system still has to address latency, failures, and interoperability.

### Primary goal: overcome the limitations of a centralized environment

The introductory slides group fundamental problems into three connected areas:

1. **Connectivity and communication:** how components discover each other and exchange data.
2. **Synchronization:** how operations are ordered or coordinated when different nodes act at different times.
3. **Coordination:** how multiple autonomous nodes reach decisions and collectively provide a service.

Coordination becomes difficult because distributed systems have conditions absent from the simplest centralized model:

- **Temporal concurrency:** operations overlap in time, such as pipeline stages processing requests concurrently.
- **Spatial concurrency:** operations execute in parallel on separate machines.
- **No global clock:** nodes cannot consult a universally exact clock to establish event order.
- **Failures:** nodes or communication paths can stop or behave unpredictably.
- **Unpredictable latency:** a slow response may indicate delay or failure, and those cases may be impossible to distinguish immediately.

These conditions limit which coordination problems can be solved and what guarantees can be offered. A design must state its assumptions and balance consistency, responsiveness, fault handling, and cost.

### Trends in distributed systems

The presentation connects the evolution of distributed systems to four trends:

- pervasive networking technology;
- ubiquitous computing and support for mobile users;
- increasing demand for multimedia services;
- treating computing as a utility.

Together, these trends expand the number and variety of devices, users, applications, and service expectations that a distributed design must support.

### Pervasive networking and the modern Internet

Modern networks connect systems at very large scale and with substantial **heterogeneity**:

- devices range from servers and workstations to small, resource-constrained devices;
- communication can use wired or wireless links and different protocols;
- available services differ across participants.

The network also allows connection requests without strict limits of time or place: a user or device may initiate communication from many locations and at changing times. This broad reach creates new requirements for discovery, compatibility, security, and reliable operation over links whose performance varies.

### Mobile and ubiquitous computing

**Mobile computing** means carrying out computing tasks while a user is moving or working outside their usual environment. Connectivity, available resources, and location may change as the user moves.

**Ubiquitous computing** uses many small, inexpensive computational devices embedded in everyday environments, such as homes, offices, and outdoor settings. Computing becomes less tied to one visible computer and more integrated into the physical world.

Common problems include:

- **Scale:** many devices and users may participate.
- **Dynamicity:** devices and network connections appear, disappear, or change state.
- **Heterogeneity:** devices differ in capability, operating system, and communication method.
- **Security:** devices handle data and actions in changing environments and may be exposed to unauthorized access.

### Distributed multimedia systems

Multimedia support means handling several media types in an integrated way. A system may need to process both discrete data, such as text or images, and **continuous media**, such as audio and video.

Continuous media have a temporal dimension: it is not enough to deliver every piece eventually; pieces must arrive and be played with appropriate timing. This makes **Quality of Service (QoS)** important. Depending on the application, QoS may concern latency, jitter, throughput, loss, or continuity. A video call, for example, may prefer a slightly degraded image over a long interruption.

### Distributed computing as a utility: cloud computing

Cloud computing presents computing resources as services that users can obtain on demand. The slides distinguish three common service levels:

- **IaaS (Infrastructure as a Service):** access to basic computing infrastructure such as virtual machines, storage, and networking.
- **PaaS (Platform as a Service):** a managed platform on which applications can be developed and run without managing all underlying infrastructure.
- **SaaS (Software as a Service):** a complete application delivered for users to access.

These levels differ in how much of the stack the provider manages and how much control the user retains. In every case, the service depends on a distributed backend that must allocate resources, coordinate machines, and handle failures.

### Data centers

Data centers house the servers, storage, networking equipment, power, and cooling used to provide large-scale digital services. Their architecture connects machines within and across facilities and influences performance, fault isolation, and operating cost.

The important conceptual link is that a service experienced as one application may be implemented by many machines distributed across racks, networks, or locations. Data-center design is therefore a practical setting for studying communication, replication, bottlenecks, and failure recovery.

### Blockchain

The presentation identifies blockchain as a prominent and challenging distributed system. A blockchain coordinates a shared ledger across multiple participants, often without relying on one central authority to decide the accepted history.

That goal raises core distributed-systems questions: how participants agree on updates, how they handle delays and failures, how they establish trust, and what security assumptions the protocol relies on. Blockchain is an example for discussing these issues; it is not a solution to every distributed-systems problem.

## Dependability

### Dependability definition

A **system** is an entity that interacts with other entities. Its environment may include hardware, software, people, and the physical world with its natural phenomena. A system boundary is therefore a modeling choice: what counts as “the system” depends on which components and interactions are being studied.

**Dependability** is the ability of a system to deliver a service that can justifiably be trusted. “Justifiably” matters: trust should rest on evidence, design, and an understanding of limitations rather than on an assumption that the system will never fail.

### An alternative dependability definition

Dependability can also be described as the ability to avoid service failures that are more frequent or more severe than acceptable. This version emphasizes that engineering is often about meeting a specified level of service, not achieving absolute perfection.

A **service failure** occurs when the delivered service deviates from correct service. A service is correct when it implements its functional specification, including its:

- **functionality:** the operations and results it is supposed to provide;
- **performance:** the timing, capacity, or other performance properties expected of it.

The specification defines what correctness means. If the specification is incomplete or unrealistic, a system can satisfy the written definition and still disappoint users.

### Service failure and restoration

Service can be viewed as moving between a **correct** state and an **incorrect** state. When the delivered service deviates from the specification, a failure has occurred. Recovery or repair may restore correct service, but a later failure can occur again.

This distinction helps separate the occurrence of a failure from the mechanisms that restore service. A system may recover quickly and still experience outages; a system may also be correct for long periods but have poor recovery when something goes wrong.

### Service outage

An **outage** is a period during which the service is unavailable or does not provide the required correct behavior. The presentation emphasizes that outages can recur over time and poses the central design question: how should a system be designed, developed, and deployed to be dependable and secure?

That question spans the system lifecycle. It involves preventing faults, containing their effects, detecting incorrect behavior, and restoring service while protecting users and data.

### Dependability attributes (or requirements)

The main attributes in the presentation are:

| Attribute | Meaning |
|---|---|
| **Availability** | Readiness to deliver correct service when needed. |
| **Reliability** | Continuity of correct service over time. |
| **Safety** | Absence of catastrophic consequences for users or the environment. |
| **Integrity** | Absence of improper system alterations. |
| **Maintainability** | Ability to modify or repair the system. |

These qualities are related but not interchangeable. A system may be highly available while occasionally producing incorrect results, or reliable in ordinary operation while difficult to repair. Requirements should therefore be stated separately and tied to the consequences that matter in the application.

### Secondary dependability attribute: robustness

**Robustness** describes dependability with respect to external faults, especially how a system reacts to a specified class of faults. A robust system does not merely assume that its environment behaves ideally; it has a defined response when certain disturbances occur.

The relevant fault classes must be specified. A system can be robust to one kind of input or environmental disturbance and vulnerable to another.

### Failures, errors, and faults

The terms form a causal chain:

**Fault → Error → Failure**

- A **fault** is the adjudged or hypothesized cause of an error. It may be internal to the system or external to it.
- An **error** is a deviation of the system's internal state from the correct state.
- A **failure** is the externally visible deviation of the delivered service from correct service.

A fault may be present without immediately causing an error. An error may exist internally without affecting the service. A failure occurs when the error propagates far enough to be visible at the service boundary. This distinction helps engineers locate where to intervene: prevent or remove the cause, detect and handle the incorrect state, or limit the user-visible consequences.

### The means to attain dependability

The presentation groups dependability methods into four areas:

| Means | Purpose | Main contribution |
|---|---|---|
| **Fault prevention** | Prevent faults from being introduced or occurring. | Supports delivery of a service that can be trusted. |
| **Fault tolerance** | Avoid service failures even when faults are present. | Keeps service correct or acceptably functional despite faults. |
| **Fault removal** | Reduce the number and severity of faults. | Improves the system through verification, debugging, repair, and maintenance. |
| **Fault forecasting** | Estimate current faults, future incidence, and likely consequences. | Provides evidence about whether requirements are likely to be met. |

Prevention and tolerance aim to provide dependable behavior; removal and forecasting help justify that the system is likely to satisfy its functional, dependability, and security requirements. These activities complement one another across development and operation.

The maintenance illustration in the slides can be used as an analogy: preventive maintenance aims to avoid a breakdown, corrective maintenance removes or repairs a known problem, and predictive maintenance estimates likely problems in advance. Dependability engineering applies the same broad logic to software and systems, while using techniques appropriate to their design and operating context.

### Threats to dependability during the system lifecycle

The system lifecycle has two broad phases:

1. **Development:** requirement elicitation, analysis, design, implementation, and testing.
2. **Use:** deployment, service delivery, maintenance, review, and eventual service shutdown.

Faults can be introduced during development by the environment in which the system is built: the physical world, human developers, development tools, and production or test facilities. A fault in the design or implementation may remain latent until a particular condition exposes it during use.

During operation, a service may move among delivery, outage, and shutdown states. Maintenance and review are part of the lifecycle because deployed systems encounter changing workloads, environments, and requirements. Dependability is not achieved only by writing correct code once; it must be supported throughout development and operation.

## Dependable Distributed Systems: Characteristics and Challenges

The presentation highlights seven areas: **heterogeneity, openness, security, scalability, fault tolerance, concurrency, and transparency**. They are interdependent. For instance, openness helps diverse components interoperate, while heterogeneity and scale create more failure and security cases to handle.

### Heterogeneity

Heterogeneity means that components differ. Differences can occur at several layers:

- networks and communication protocols;
- hardware;
- operating systems;
- programming languages;
- implementations produced by different developers.

The solution is not necessarily to make every component identical. **Middleware**, from remote procedure call (RPC) mechanisms to service-oriented architectures, can provide common interfaces across unlike platforms. **Mobile code** and **virtual machines** can also help software execute in different environments.

The core challenge is to define stable contracts and translate between differences without losing correctness, performance, or security. The slides note that many underlying technologies connect with topics studied in Software Engineering.

### Openness

**Openness** is the capability of a system to be extended and re-implemented. It depends on clear specifications and interfaces that allow independently built components to work together.

#### Specifications

A well-formed service or component specification should be:

- **Complete:** all relevant aspects of its behavior are described.
- **Neutral:** it describes expected behavior without prescribing a particular implementation.

Completeness makes it possible to reason about what clients can rely on. Neutrality allows alternative implementations while preserving the same externally visible contract.

#### Interfaces

An **interface** describes the syntax and semantics of a service or component: which operations are available, what parameters they accept, and what exceptions or errors may occur. An Interface Definition Language (IDL) is one way to express such contracts.

An interface makes a boundary explicit. A syntactically compatible call is not sufficient if the parties interpret its meaning differently, so both syntax and semantics matter. The presentation connects working with specifications and high-level interfaces to the course's relationship with Software Engineering.

### Openness: forms of cooperation and evolution

The presentation distinguishes several capabilities that arise from openness:

| Capability | Meaning |
|---|---|
| **Interoperability** | Two systems cooperate through services or components defined by a shared standard. |
| **Portability** | A component implemented for one system can work on another without modification. |
| **Flexibility** | A system can configure or orchestrate components developed by different programmers. |
| **Add-on features** | New services or components can be added and integrated into a running system. |
| **Evolvability** | A system can change over time, including keeping different versions of a service active during transition. |
| **Self-* capabilities** | A system reconfigures or manages itself with reduced human intervention. |

These capabilities are related but distinct. A standard may enable interoperability without guaranteeing portability; adding a component may be possible without making the system easy to evolve. Clear interfaces are the foundation, while runtime mechanisms and governance determine how safe and practical the changes are.

### Security

The primary security attributes introduced are:

| Attribute | Meaning in this context |
|---|---|
| **Confidentiality** | Information is not disclosed to unauthorized parties. |
| **Integrity** | The system is not altered without authorization. |
| **Availability** | Authorized users and actions can access the service when needed. |

The availability definition is about availability **for authorized actions**: a system that responds to unauthorized requests while denying legitimate users is not meeting the security goal. The presentation treats security from a distributed-system design perspective and points to a separate Cybersecurity course for more technical treatment.

### Secondary security attributes

The additional attributes are:

- **Accountability:** the identity of the person who performed an operation is available and protected from improper alteration.
- **Authenticity:** the integrity of a message's content and origin can be verified, and possibly other information such as its emission time.
- **Non-repudiability:** the identity of the sender or receiver of a message is available and protected so that a party cannot plausibly deny the relevant action.

These properties depend on mechanisms such as identity management, authentication, logging, and cryptography, but their meaning is broader than any single mechanism. Correct design must also account for how identities and evidence are managed across nodes and organizations.

### Dependability and security

Dependability and security overlap, but they answer different questions. Dependability includes maintainability, reliability, safety, integrity, and availability. Security includes confidentiality and also protects integrity and availability against unauthorized actions.

**Integrity** and **availability** appear in both because a system can become incorrect or unavailable through accidental faults or deliberate attacks. The cause and threat model differ, but the service-level property can be shared. A dependable design must therefore consider both accidental failures and hostile behavior where relevant.

### Scalability

A system is **scalable** if it continues to operate with adequate performance when the number of resources or users grows by large orders of magnitude. The key is not merely to accommodate more machines, but to prevent performance and coordination from collapsing as the system expands.

Centralization can work against scalability because one component can become a capacity limit or single point of failure. However, centralized solutions may still be imposed by security, business, or administrative requirements. The design must account for those requirements and the resulting trade-offs.

#### Replication as a way to scale

Replication places multiple copies of a service or resource at different nodes. Requests can then be distributed among copies, capacity can increase, and a surviving copy may continue serving users when another fails.

The copies introduce coordination costs. They need policies for handling updates, failures, and selection of an appropriate replica. Replication is therefore a way to address scalability, not a free or universal solution.

#### Replication issues

The slides group the issues into service, data, and computation:

- **Replicated service:** nodes must coordinate which operations they perform and how they present results.
- **Replicated data:** copies may diverge, creating consistency questions about which value a read should return and when updates become visible.
- **Distributed computation:** no single node necessarily holds the current state of the whole system. Each node makes decisions using the data it owns or can obtain, and the algorithm must still meet its goal if a node fails.

The more widely state is distributed, the more important it is to specify what each node knows, how it learns new information, and what correctness means when updates are concurrent or delayed.

#### Designing scalable systems

The presentation identifies four design concerns:

1. **System dynamicity:** servers or processes may need to be added or removed while the system is running.
2. **Performance metrics:** servers should not have to interact with every application user, and algorithms should avoid requiring the entire data set for every decision.
3. **Scarce resources:** system design should account for limited resources, such as battery power in embedded devices.
4. **Bottlenecks:** centralized components such as a single service or lookup point may limit performance; distributed alternatives may reduce that constraint.

Scalability should be measured against concrete workload and quality goals. A system can scale in user count but fail to scale in latency, storage, energy use, or operational complexity.

### Concurrency

Concurrency arises when multiple clients access shared resources at the same time. If clients invoke read and write operations on a shared variable concurrently, what value should each read return?

There is no universally correct answer without a rule for ordering and visibility. The system must specify how concurrent operations relate—for example, whether updates are serialized, whether clients may see stale values, or whether operations follow a defined consistency model. **Coordination** and **synchronization** provide ways to impose the required relationships among operations.

In distributed systems, concurrency is especially challenging because operations run at different nodes and no global clock gives a perfect ordering. The chosen behavior is part of the service's contract, not just an implementation detail.

### Transparency

Transparency describes ways to hide certain aspects of distribution from users or applications. The presentation lists six forms:

| Form | Intended effect |
|---|---|
| **Access transparency** | Use the same operations for local and remote resources. |
| **Location transparency** | Access a resource without knowing its physical location. |
| **Concurrency transparency** | Let users or processes share resources without interfering improperly. |
| **Failure transparency** | Mask failures where possible so users can complete remaining requested operations. |
| **Mobility transparency** | Move resources or users without changing the operations issued by users. |
| **Performance transparency** | Reconfigure the system to change load and improve performance. |

Transparency is a design objective with limits. Hiding a failure or location can simplify use, but hiding every consequence is often impossible or unsafe. The appropriate abstraction depends on what the system can guarantee and what the application needs to know.

### “Simple” models to deal with complexity

Distributed systems are too complex to reason about in every implementation detail at once. A model simplifies the problem by stating which properties matter and which assumptions are being made. For example, a design may model processes, message delivery, clocks, failures, or membership at an abstract level.

The purpose of a model is not to claim that the real system is simple. It is to make assumptions explicit so that behavior and guarantees can be analyzed. A useful model must still represent the conditions that can invalidate the intended guarantees.

The presentation returns to transparency in this part of the sequence. Transparency can be understood as one abstraction strategy: the system exposes a simpler interface while its distributed implementation handles location, concurrency, failures, and changing load as far as the design permits.

### What will you learn?

The concluding overview maps the listed challenges to areas of study:

| Challenge | Area indicated in the slides |
|---|---|
| Heterogeneity | Software Engineering (SE) |
| Openness | Software Engineering and Dependable Distributed Systems (SE, DDS) |
| Security | Cybersecurity and Dependable Distributed Systems (CS, DDS) |
| Scalability | Dependable Distributed Systems (DDS) |
| Fault tolerance | Dependable Distributed Systems (DDS) |
| Concurrency | Dependable Distributed Systems (DDS) |
| Transparency | Software Engineering and Dependable Distributed Systems (SE, DDS) |

This map explains the course's place in a broader curriculum: distributed systems draw on software engineering and cybersecurity, while the course focuses on the system-level mechanisms and reasoning needed to make distributed services dependable.

## References

- Algirdas Avizienis, Jean-Claude Laprie, Brian Randell, and Carl E. Landwehr. “Basic Concepts and Taxonomy of Dependable and Secure Computing.” *IEEE Transactions on Dependable and Secure Computing*, 1(1), 11–33, 2004. [IEEE Xplore](https://ieeexplore.ieee.org/document/1335465/)
- Christian Cachin, Rachid Guerraoui, and Luís Rodrigues. *Introduction to Reliable and Secure Distributed Programming*. Springer, 2011.
- Wolfgang Emmerich and Maarten van Steen definitions of distributed systems, as quoted in the presentation.
- Leslie Lamport's distributed-system failure observation, as quoted in the presentation.
- Further figures and examples in the slides cite Epoch AI on frontier-model training compute, Scalable Thread on latency, Arpit Bhayani on master-replica replication, WeeTech on distributed-system examples, Park Place Technologies on data-center network architecture, and a blockchain transaction-flow figure hosted on ResearchGate.

## Core ideas to retain

- A distributed system is made of autonomous nodes that communicate over a network and cooperate to provide a service.
- Users may see one coherent service, but the implementation remains distributed, with delays, partial failures, and incomplete information.
- Distribution enables capacity, geographic reach, and redundancy; it also creates coordination, consistency, and security challenges.
- Dependability concerns trustworthy service and is reasoned about through attributes such as availability, reliability, safety, integrity, and maintainability.
- A fault is a cause, an error is an incorrect internal state, and a failure is an externally visible deviation in service.
- Dependability is achieved through a combination of prevention, tolerance, removal, and forecasting.
- Heterogeneity, openness, security, scalability, fault tolerance, concurrency, and transparency are connected design challenges, not isolated features.
- Every guarantee depends on a clear specification and an explicit model of nodes, networks, failures, and threats.
