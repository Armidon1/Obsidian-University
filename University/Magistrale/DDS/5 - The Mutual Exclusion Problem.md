# The Mutual Exclusion Problem
Let us consider
◦ a set of processes 𝛱 = {p1, p2, … pn}
◦ a set of resources R= {r1, r2, … rm}
![[Pasted image 20251013122049.png]]
PROBLEM
◦ Processes need to access resources exclusively and we need to design a distributed
abstraction that allows them to coordinate to get access to resources

## Recap - System Model
Let us consider
◦ a set of processes 𝛱 = {p1, p2, … pn}
◦ a set of resources R= {r1, r2, … rm}
	◦ For the sake of simplicity let us assume |R| = 1
The system is asynchronous
Processes are not going to fail (they will be always correct)
Processes communicate by exchanging messages on top of perfect point-to-point
links
## Recap - The Mutual Exclusion abstraction
### EVENTS
◦ $request()$: it issues a request to enter into the critical section
◦ $ok()$: it notifies the process that it can now access the critical section
◦ $release()$: it is invoked to leave the critical section and to allow someone else to enter
### PROPERTIES
◦ **Mutual Exclusion**: at any time t, at most one process p is running the critical section
◦ **No-Deadlock**: there always exists a process p able to enter the critical section
◦ **No-Starvation**: every request() and release() operation eventually terminate
![[Pasted image 20251013122758.png]]
## Recap - Different Approaches to Distributed Mutual Exclusion
![[Pasted image 20251013122826.png]]

## Coordinator-based Distributed Mutual Exclusion

**BASIC IDEA**
◦ There exist a special process (i.e., a coordinator) that collects requests and grant permission to enter into the critical section. The next code is extremely important for the exam. 1/5 of the exam is writing a code like that.
**PROCESS CODE**
```Python 
#PROCESS CODE
Init
state = idle
coordinator = getCoordinatorId()

upon event request()
	state = waiting
	trigger pp2pSend(REQ, i) to coordinator
	
upon event pp2pDeliver(GRANT_CS)
	state = CS
	trigger ok()

upon event release()
	state = idle
	trigger pp2pSend(REL, i) to coordinator
```
**COORDINATOR  CODE**
```Python 
#COORDINATOR CODE
Init
pending = null 
current_in_CS=⊥

upon event pp2pDeliver(REQ, j) from pj
	pending = pending UNION {pj}

when pending != null and current_in_CS=⊥
	candidate=select_process (pending)
	pending = pending \ candidate
	current_in_CS = candidate
	trigger pp2pSend(GRANT_CS) to candidate
	
upon event pp2pDeliver(REL, j) from pj
	if current_in_CS = j
	current_in_CS = ⊥
```
### Example
![[Pasted image 20251013124347.png]]
![[Pasted image 20251013124400.png]]
![[Pasted image 20251013124407.png]]
![[Pasted image 20251013124415.png]]
![[Pasted image 20251013124421.png]]
![[Pasted image 20251013124427.png]]
![[Pasted image 20251013124432.png]]
![[Pasted image 20251013124437.png]]
![[Pasted image 20251013124442.png]]
![[Pasted image 20251013124500.png]]
does it implement **No deadlock**? YES: this is possible thanks to the handler
does it implement **No Starvation**? depends if we implement a FIFO queue. If we use a Random queue, well, it may happen then. 
## Discussion
**PERFORMANCE**
◦ entering the CS always requires 2 messages (i.e., REQ and GRANT) taking one RTT
◦ releasing the CS only requires 1 message
	◦ such message represent the delay between two different accesses to the CS
![[Pasted image 20251013124813.png]]

## Token-based Algorithm on Logical Ring
**BASIC IDEA**
◦ a process interested to the CS can access it only when it receives a token
◦ The token is unique and it is exchanged between processes
◦ to guarantee fairness, we can exploit a structured logical topology (i.e., a **ring**) for exchanging messages related to the mutual exclusion protocol.

Basically, when i finish my job in the CS (Critical Section), i pass the token to the next process.  

**INTUITION OF THE ALGORITHM**
1. **we construct** an overlay (i.e., a logical network) **as a ring** exploiting existing point-to-point communication channels
2. A token is created and inserted in the ring during the initialization phase (i.e., it is assigned to a process of the system)
3. When a process requests the CS
		a. it waits until it gets the token
		b. enter the CS and upon release it sends the token to its next on the ring
4. If a process receives the token and it is not interested in the CS, it simply passes it to the next in the ring

**INTUITION**
1. we construct an overlay (i.e., a logical network) as a ring exploiting existing point-to-point communication channels
◦ The ring is obtained by:
	◦ storing in a local variable the name of the next process in the ring and
	◦ allowing the communication only with the next
![[Pasted image 20251013130319.png]]
![[Pasted image 20251013130423.png]]

2. A token is created and propagated in the ring during the initialization phase (i.e., it is assigned to a process of the system)
**WARNING**: *The token must be unique to guarantee mutual exclusion*
Only one process (selected trough a deterministic function) can create the token
during the init
![[Pasted image 20251013130623.png]]
Of course, we have one token per resource given to one process
3. When a process requests the CS
	a. it waits until it gets the token
	b. enter the CS and upon release it sends the token to its next on the ring

4. If a process receives the token and it is not interested in the CS, it simply passes it to the next in the ring
![[Pasted image 20251013130930.png]]
```

```

If we put together all the algorhitm, we have this:
```python
Init
state = idle
next = p(i+1)mod N

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

Of course, we are considering the case that there aren't any failures. in those cases, we will see what we have to do in the next class.

**Discussion**
The algorithm continuously consume communication resources (even if no one is
interested to the CS).

The delay experienced by every process between the request and the grant
varies between 0 (it just receives the token) and N messages (it just forwarded
the token).

Can we do something in the between? A little bit more cheaper and centered Yes, with the n ext algorhitm

### Quorum-based Algorithm – Maekawa’s voting algorithm
**BASIC IDEA**
◦ to enter the CS every process waits to get the acknowledgement only by a subset of
processes large enough to guarantee conflicts

Each process pi has associated a **voting set** $V_{i}$. The process has to know if it is in the voting set.
◦ Voting sets must satisfy the following properties
	◦ $p_{i} ∈ V_{i}$
	◦ ∀ i, j, Vi ∩ Vj ≠ ∅ (i.e., there is at least one common member for each pair of voting sets)
	◦ |Vi| = K (voting sets have all the same size for fairness – same load principle)
	◦ each pj is contained in M voting sets (same responsibility principle)

is like when someone is inside and watching outside his windows and seing that someone took the resouces. after that, he broadcast the message to his neighbours that the resources has been taken.

**Algorhitm**
```python
Init
state = released
voted = false
Vi = get_voting_set(i)
replies = null
pending = null

upon event request()
	state = wanted
	for each pj (Vi \pi) do
		trigger pp2pSend(REQ, i) to pj

upon event pp2pDeliver(REQ, j)
	if state == held OR voted == true
		pending = pending  {i}
	else
		trigger pp2pSend(ACK, i) to pj
		voted = true

upon event pp2pDeliver(ACK, j)
	replies = replies  {j}

when |replies| == |Vi|-1
	state = held

upon event release()
	state = released
	replies = 
	for each pj (Vi \pi) do
		trigger pp2pSend(REL, i) to pj

upon event pp2pDeliver(REL, j)
	if |pending| > 0
		candidate=select_next(pending)
		pending = pending \candidate
		trigger pp2pSend(ACK, i) to candidate
		voted = true
	else
		voted = false
```


**CHALLENGE**: How to compute the values K and M to balance load and
responsibilities to be optimal? 
◦ Maekawa showed that the optimal solution which minimize k and allows to get ME is
having
	◦ K~ square root of N
	◦ M=K
◦ An approximation to define Vi is having sets such that |Vi| ~ 2 square root of 𝑁 defined as follows
	◦ Place processes in a matrix of size square root of 𝑁 x square root of 𝑁
	◦ for each pi, let Vi be the union of the rows and columns containing p i

**Example**
Let us consider a system composed by N = 4 processes
◦ (M = K ~ square root of 4 and |Vi|~ 2 square root of 4)
Let’s place processes in the matrix and compute Vi
![[Pasted image 20251013132540.png]]

Let us consider a system composed by N = 9 processes
	◦ (M = K ~ square root of 9 and |Vi|~ 2 square root of 9 = 6)
![[Pasted image 20251013132715.png]]
![[Pasted image 20251013132748.png]]
Theoretical speaking, the algorithm won't work, but in practical usage, with some timers and clocks, works even better compared to the others because there are less messages in the network.

**Reference**
George Coulouris, Jean Dollimore and Tim Kindberg, Gordon Blair "Distributed
Systems: Concepts and Design (5th Edition)". Addison - Wesley, 2012.
◦ Chapter 11 – section 11.2