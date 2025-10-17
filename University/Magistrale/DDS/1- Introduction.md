
---

# Dependable Distributed Systems

**Master of Science in Engineering in Computer Science**  
AA 2024/2025

## Introduction

---

## General Information

- **9 CFU** – first semester
    
- **Period:** September 25th – December 20th
    

### Instructor

- **Silvia Bonomi**
    

### Schedule

- **Tuesday** 09:00 – 12:00 → _Remote on Zoom_
    
    - Meeting ID: `870 8318 1029`, passcode: `868800`
        
- **Wednesday** 10:00 – 14:00 → _Room A1_, Dip. di Scienze Odontostomatologiche e Maxillo Facciali, Via Caserta 6
    
- **Thursday** 12:00 – 14:00 → _Room 29 San Pietro in Vincoli_, Via Eudossiana 18
    

### Course Material

- Available on **Google Classroom**
    
    - Code: `3eewzcl`
        

### Main References

- C. Cachin, R. Guerraoui, L. Rodrigues – _Introduction to Reliable and Secure Distributed Programming_, Springer (available at DIAG library)
    
- Scientific papers
    
- Supporting slides
    

### Students’ Hours

- By appointment (email)
    
- During lectures (start, end, or breaks)
    

**Office:**  
DIAG, Via Ariosto 25  
Room B114, 1st floor, B wing

### Exam

- **Written test**
    
- Questions cover all topics in the final syllabus
    

---

# Distributed Systems

---

## From Concurrent to Distributed Systems

|Concurrent Systems|Distributed Systems|
|---|---|
|Shared memory|Distributed memory|
|Processes share resources|Processes on separate machines|
|Easier coordination|Communication via messages|

---

## Definitions

> “A distributed system is a set of spatially separate entities, each with computational power, able to communicate and coordinate to reach a common goal.”

> “A distributed system consists of autonomous computers, connected through a network and middleware, enabling coordination and resource sharing so that users perceive a single integrated system.”  
> _(Wolfgang Emmerich)_

> “A distributed system ensures that independent computers appear as a single coherent system.”  
> _(Maarten van Steen)_

> “A distributed system is one in which the failure of a computer you didn’t even know existed can render your own computer unusable.”  
> _(Leslie Lamport)_

---

## Common Points

- Set of entities/computers/machines
    
- Communication and coordination
    
- Resource sharing
    
- Common goal
    
- Perceived as a single system
    

---

## Why Distributed Systems?

1. **Increase Performance**
    
    - Handle higher user demand (processing, storage)
        
    - Reduce latency for global users
        
2. **Build Dependable Services**
    
    - Cope with failures
        

---

## Examples

- **Internet**
    
- **Cloud infrastructure**
    
- **Blockchain systems**
    

---

## Characteristic 1: Autonomous Computing Elements

### Challenges

- Absence of a global clock
    
- Group membership (open vs closed groups)
    
- Overlay networks (structured vs unstructured)
    

---

## Characteristic 2: Single Coherent System

A distributed system is _coherent_ if:

- It behaves as expected by users
    
- Nodes collectively operate consistently
    

### Challenge

- **Failures**
    

---

# Middleware and Distributed Systems

The distributed system provides **inter-process communication**:

- Between components of a distributed application
    
- Between different applications
    

### Goals

- Hide hardware/OS differences
    
- Enable transparent communication
    

---

# Primary Goal: Overcome Centralization Limits

### Main Problems

- Connectivity and communication
    
- Synchronization
    
- Coordination
    

### Coordination Constraints

1. Temporal and spatial concurrency
    
2. No global clock
    
3. Failures
    
4. Unpredictable latencies
    

> These conditions limit what coordination problems can be solved.

---

# Trends in Distributed Systems

Modern distributed systems evolve due to:

- **Pervasive networking**
    
- **Ubiquitous computing** and user mobility
    
- **Demand for multimedia services**
    
- **Distributed computing as a utility**
    

---

## Pervasive Networking and the Modern Internet

### Characteristics

- Scale
    
- Heterogeneity in:
    
    - Devices (servers, IoT, mobile)
        
    - Protocols (wired/wireless)
        
    - Services
        
- No spatial or temporal limits to connections
    

---

## Mobile and Ubiquitous Computing

**Mobile computing:** computing while moving or in different locations.  
**Ubiquitous computing:** integration of many small devices into daily environments.

### Common Problems

- System scale
    
- Dynamic topology
    
- Heterogeneity
    
- Security issues
    

---

## Distributed Multimedia Systems

System must support **continuous media** (audio, video).

### Challenges

- Temporal synchronization
    
- Quality of Service (QoS)
    

---

## Distributed Computing as a Utility

**Cloud Computing Paradigms:**

- **IaaS** – Infrastructure as a Service
    
- **PaaS** – Platform as a Service
    
- **SaaS** – Software as a Service
    

---

# Dependability

---

## Definition

Dependability = _ability of a system to deliver a service that can justifiably be trusted._

A system interacts with:

- Hardware
    
- Software
    
- Humans
    
- Physical world (environment)
    

---

## Alternative Definition

A **service failure** occurs when delivered service deviates from the correct service.

- **Correct service:** meets functional specification in function and performance.
    
- **Dependability:** ability to avoid unacceptable service failures.
    

---

### Service Failure Lifecycle

```
Correct Service → FAILURE → Incorrect Service → RESTORATION
```

### Key Question

> How to design and deploy a dependable and secure system?

---

## Dependability Attributes

|Attribute|Meaning|
|---|---|
|**Availability**|Readiness for correct service|
|**Reliability**|Continuity of correct service|
|**Safety**|No catastrophic consequences|
|**Integrity**|No improper alterations|
|**Maintainability**|Ease of repair and modification|

### Secondary Attribute

- **Robustness:** dependability under external faults
    

---

## Failures, Errors, Faults

- **Failure:** deviation from correct service
    
- **Error:** incorrect internal state
    
- **Fault:** cause of an error (internal/external)
    

```
Fault → Error → Failure
```

---

## Means to Attain Dependability

|Technique|Purpose|
|---|---|
|**Fault Prevention**|Avoid introduction of faults|
|**Fault Tolerance**|Avoid service failure despite faults|
|**Fault Removal**|Detect and eliminate faults|
|**Fault Forecasting**|Estimate number and impact of faults|

---

## Threats During System Lifecycle

### Phases

- **Development**: analysis → design → testing → deployment → maintenance
    
- **Use**: service delivery, outages, shutdowns
    

Faults may be introduced by:

- Environment
    
- Human error
    
- Tools or facilities
    

---

# Dependable Distributed Systems: Characteristics and Challenges

1. **Heterogeneity**
    
2. **Openness**
    
3. **Security**
    
4. **Scalability**
    
5. **Fault Tolerance**
    
6. **Concurrency**
    
7. **Transparency**
    

---

## Heterogeneity

Affects:

- Networks
    
- Hardware
    
- OS
    
- Programming languages
    
- Implementations
    

**Solutions:**

- Middleware (RPC, SOA)
    
- Mobile code, virtual machines
    

---

## Openness

Ability to **extend and reimplement** systems.

- **Specification:** complete and neutral
    
- **Interface:** syntax, semantics, parameters, exceptions
    

Enables:

- Interoperability
    
- Portability
    
- Flexibility
    
- Add-on features
    
- Evolvability
    
- Self-management (Self-*)
    

---

## Security

|Attribute|Description|
|---|---|
|**Confidentiality**|No unauthorized disclosure|
|**Integrity**|No unauthorized alterations|
|**Availability**|Only authorized actions allowed|

### Secondary Security Attributes

- **Accountability** – identity integrity
    
- **Authenticity** – message origin correctness
    
- **Non-repudiation** – sender/receiver identity assurance
    

---

## Dependability & Security

|Dependability|Security|
|---|---|
|Availability|Confidentiality|
|Reliability|Integrity|
|Safety||
|Maintainability||

---

# Scalability

A system is **scalable** if it maintains adequate performance as users/resources increase.

### Challenges

- Centralization → bottlenecks
    
- Replication introduces:
    
    - Service coordination
        
    - Data consistency
        
    - Distributed computation
        

### Design Goals

- Dynamic server management
    
- Efficient algorithms
    
- Avoid bottlenecks
    
- Optimize scarce resources
    

---

# Concurrency

Multiple access to shared resources requires:

- **Coordination**
    
- **Synchronization**
    

---

# Transparency

A distributed system should hide distribution aspects from users.

|Type|Meaning|
|---|---|
|**Access**|Same operations for local/remote|
|**Location**|Hide physical location|
|**Concurrency**|Allow concurrent access|
|**Failures**|Mask failures|
|**Mobility**|Support moving users/resources|
|**Performance**|Enable reconfiguration for load|

---

# What You Will Learn

|Topic|Course|
|---|---|
|Heterogeneity|DDS|
|Openness|DDS|
|Security|DDS & Cybersecurity|
|Scalability|DDS|
|Fault Tolerance|DDS|
|Concurrency|DDS|
|Transparency|DDS|

---

## References

- A. Avizienis, J.-C. Laprie, B. Randell, C. Landwehr, _Basic Concepts and Taxonomy of Dependable and Secure Computing_, IEEE TDSC 1(1): 11–33 (2004)
    
    - [https://ieeexplore.ieee.org/document/1335465/](https://ieeexplore.ieee.org/document/1335465/)
        

---
