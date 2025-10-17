![[Pasted image 20251016140539.png]]
1) lets's consider each processes. considering each latency. i have to find
for each $p_i$ : $|S(t)-C_{i}(t)|<D$, where S(t) is .... and $C(t)=S(t)+- RTT/2$, so:

$$D_1 = | S(t) - (S(t)+- RTT/2)| = RTT_{1}/2 = (1+1)/2 = 1$$
$$D_2 = ... = RTT_{2}/2 = (2+2)/2 = 2$$
2) External clock for each $p_i$ and Internal clock for each $p_i,p_j$,, :
	1) ◦ Clocks are internally synchronized in a time interval I:
		◦ | Ci(t) - Cj(t)| < D for i,j = 1, 2, … N and for all time t in I
			C1=t-1 and C2=t+2 then |t-1-t-2| = 3
	2) external clock...
3) 

---
![[Pasted image 20251016140641.png]]

---
![[Pasted image 20251016140654.png]]
we learn that the scalar clock $L_i$ is an integer that in the and is equal to zero, for each $p_i$. here is the evolution of $L_i$:
![[SmartSelect_20251016_150219_Samsung Notes.jpg]]
in the vector clock:
![[SmartSelect_20251016_150229_Samsung Notes.jpg]]

---
![[Pasted image 20251016140708.png]]

---
![[Pasted image 20251016140720.png]]
Hint: implementing the rounting beetween source and destination. Look if the destination is on your neighbours, then you have to propagate (or in the left or in the right). to understand where to go, on the left or the right, all you have to do is simply compare the index of the process.