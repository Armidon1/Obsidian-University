## Exercice 1
![[Pasted image 20251023141515.png]]
## Exercise 2
![[Pasted image 20251023141756.png]]
Solution
```C
INIT
left=get_left(my_id)
right=get_lright(my_id)
leader=null

when leader == null or left ==null
	if left == null
		leader=my_id
		trigger Leader(leader)
		trigger pp2pSend(NEW_LEADER, leader) to right
		upon event pp2pDeliver(NEW_LEADER, l)

if l > leader
	leader = l
	trigger Leader(leader)
	pp2pSend(NEW_LEADER, leader) to right
	upon event new_right(pj)
	right=pj
	trigger pp2pSend(NEW_LEADER, leader) to right

upon event new_left(pj)
	left=pj
```
## Exercise 3
![[Pasted image 20251023141828.png]]
## Exercise 4
![[Pasted image 20251023141848.png]]
**SOLUTION for Leader based Algorithm**
```C
PROCESS CODE

Init
state = idle
coordinator = getCoordinatorId()
correct = {p1, p2, … pn}
transition = false

upon event request()
	state = waiting
	trigger pp2pSend(REQ, i) to coordinatorupon event pp2pDeliver(GRANT_CS)
	state = CS
	trigger ok()

upon event release()
	state = idle
	trigger pp2pSend(REL, i) to coordinator

upon event crash(pj)
	correct = correct \{pj}
	if coordinator == pj
		coordinator = getCoordinatorId(correct)
		if coordinator == self
			% manage transition
			transition = true
			pending = NULL
			current_in_CS=⊥
			ACK=NACK=NULL
			for every pk in correct
				trigger pp2pSend(CHECK_CS) to pk
		else
			if state == waiting
				trigger pp2pSend(REQ, i) to coordinator

upon event pp2pDeliver(CHECK_CS) from coordinator
	if state== CS
		trigger pp2pSend(ACK, self) to coordinator
	else
		trigger pp2pSend(NACK, self) to coordinator


COORDINATOR CODE
Init
pending = NULL
current_in_CS=⊥
correct = {p1, p2, … pn}
transition = false

upon event pp2pDeliver(REQ, j) from pj
	pending = pending  {pj}

when pending != NULL and current_in_CS=⊥ and not transition
	candidate=select_process (pending)
	pending = pending \ candidate
	current_in_CS = candidate
	trigger pp2pSend(GRANT_CS) to candidateupon event pp2pDeliver(REL, j) from pj

upon event pp2pDeliver(REL, j) from pj
	if current_in_CS == j
		current_in_CS = ⊥

upon event crash(pj)
	correct = correct \{pj}
	if pj in pending
		pending = pending \{pj}
	if current_in_CS= pj
		current_in_CS=⊥

upon event pp2pDeliver (ACK, j)
	current_in_CS = j
	transition= false

upon event pp2pDeliver (NACK, j)
	NACK= NACK union {j}

when correct  NACK
	transition = false
```