# Problem Solving by Search

**Tags:** #uni #AI #engineering #search #algorithms
**Source:** Prof. Patrizi Slides (02-AI-Search) + Ch 3 "AI A Modern Approach"

---

## 1. Problem-Solving Agents

A **problem-solving agent** is a type of agent that decides what to do by undertaking a process of **search**: it looks ahead by simulating sequences of actions in its internal model to find a path that leads to a desired goal state .

The standard operating process follows 4 phases :
1. **Goal formulation:** The agent adopts a goal (e.g., reaching Bucharest). Goals organize behavior by limiting the objectives and hence the actions to be considered.
2. **Problem formulation:** The agent devises an abstract description of the states and actions (e.g., a road map). **Abstraction** is fundamental to removing irrelevant details (like weather or scenery) and making the problem computable.
3. **Search:** The agent simulates sequences of actions until it finds a **solution** (a sequence of actions leading from the initial state to the goal).
4. **Execution:** The agent executes the actions in the real world.

> **Note:** In fully observable, deterministic, known environments, the solution is a fixed sequence. The agent can operate in an **Open-loop** (ignoring percepts during execution because it knows the solution will work) .

---

## 2. Formal Definition of a Search Problem

A search problem is formally defined by the following 5 components :

1. **State Space ($S$):** The set of all possible states the environment can be in. It can be finite or infinite.
2. **Initial State ($s_0$):** The state in which the agent starts.
3. **Goal States ($G$):** A subset of states ($G \subseteq S$) or an `IS-GOAL(s)` function that checks if a state satisfies the objective.
4. **Actions ($A$):** A function `ACTIONS(s)` that returns the finite set of actions applicable in state $s$.
5. **Transition Model:** A function `RESULT(s, a)` that returns the state resulting from performing action $a$ in state $s$.
* This defines the state space graph: nodes = states, edges = actions.
6. **Action Cost Function ($c$):** `ACTION-COST(s, a, s')` gives the numeric cost of applying action $a$ in state $s$ to reach state $s'$. Costs are assumed to be additive and generally positive ($c \ge \epsilon > 0$).

### Classic Examples

#### Romania Map
- **States:** Cities (e.g., Arad, Sibiu).
- **Actions:** Drive from one city to another.
- **Cost:** Distance in miles.

![[Insert Image Figure 3.1 from PDF here]]
> *Figure 3.1: A simplified road map of part of Romania. The numbers on the edges indicate distance.*

#### The Vacuum World
- **States:** Agent location and dirt presence. With $n$ cells, there are $n \cdot 2^n$ states.
- **Actions:** Left, Right, Suck.

![[Insert Image Figure 3.2 from PDF here]]
> *Figure 3.2: State space graph for the two-cell vacuum world .*

#### The 8-Puzzle
- **States:** Configuration of tiles on a $3 \times 3$ grid.
- **Actions:** Move the blank space (Up, Down, Left, Right).
- **Goal:** Order the numbers.

![[Insert Image Figure 3.3 from PDF here]]
> *Figure 3.3: Start State and Goal State of the 8-puzzle.*

---

## 3. Solutions and Paths

- **Path:** A sequence of actions and states.
- **Solution:** A path from the initial state to a goal state.
- **Optimal Solution:** The solution that has the **lowest path cost** among all possible solutions.

---

## 4. Algorithms and Search Trees

A **Search Algorithm** takes a problem as input and returns a solution or failure. Most algorithms work by superimposing a **[[Search Tree]]** over the state space graph.

### Fundamental Distinction: State vs Node
- **State:** A physical configuration of the world (e.g., "Being in Arad").
- **Node:** A data structure within the search tree containing :
* `node.STATE`: The corresponding state.
* `node.PARENT`: The node that generated this node.
* `node.ACTION`: The action taken to get here.
* `node.PATH-COST`: The total cost from the root path to this node ($g(n)$).

### Expansion and Frontier
The algorithm proceeds via **Node Expansion**:
1. Select a node from the **Frontier** (the set of generated nodes not yet expanded, sometimes called *Open List*).
2. Apply possible actions to generate child nodes (Successors).
3. Add children to the frontier.

The **Frontier** separates the "explored" region (expanded nodes) from the "unexplored" region (states not yet reached).

![[Insert Image Figure 3.4 from PDF here]]
> *Figure 3.4: Three partial stages of the search tree. Green nodes represent the frontier .*

![[Insert Image Figure 3.5 from PDF here]]
> *Figure 3.5: How the search tree covers the state space graph.*

---

## 5. Graph Search vs Tree-like Search

A critical issue in search is **redundant paths** and **cycles** (loopy paths) .
* *Example:* Going from Arad to Sibiu and back to Arad is a cycle. Going to Arad via Zerind is a longer redundant path.

Algorithms are divided into two categories:
1. **Graph Search:** Keeps track of visited states (using a `reached` set or *Closed List*). If an explored state is encountered with a lower or equal cost, it is ignored. Necessary for spaces with many loops (e.g., grids).
2. **Tree-like Search:** Does not keep track of past states. Saves memory but can end up in infinite loops or explore the same states exponentially via different paths.

![[Insert Image Figure 3.6 from PDF here]]
> *Figure 3.6: The separation property. The frontier (green) separates the interior (visited) from the exterior (not reached) .*

---

## 6. Best-First Search (General Approach)

Most search algorithms are variants of **Best-First Search (which is not Breadth-First Search [[BFS]])**.
The idea is to select the node to expand based on an **evaluation function $f(n)$**.
* Always expand the node with the **minimum $f(n)$**.
* The Frontier is implemented as a **Priority Queue** ordered by $f$.

```python
function BEST-FIRST-SEARCH(problem, f) returns a solution node or failure
node <- NODE(STATE=problem.INITIAL)
frontier <- priority queue ordered by f, with node as element
reached <- lookup table {problem.INITIAL: node}

while not IS-EMPTY(frontier) do
node <- POP(frontier)
if problem.IS-GOAL(node.STATE) then return node
for each child in EXPAND(problem, node) do
s <- child.STATE
if s is not in reached or child.PATH-COST < reached[s].PATH-COST then
reached[s] <- child
add child to frontier
return failure

function EXPAND(problem, node) yields nodes 
s ← node.STATE 
for each action in problem.ACTIONS(s) do 
	s′ ← problem.RESULT(s, action) 
	cost ← node.PATH-COST + problem.ACTION-COST(s, action, s′) 
	yield NODE(STATE=s′, PARENT=node, ACTION=action, PATH-COST=cost)
````

> Figure 3.7: Best-First Search Algorithm (adapted pseudocode)1.

---

## 7. Algorithm Properties

We evaluate an algorithm using 4 criteria 2:

1. **Completeness:** Does it always find a solution if one exists?

2. **Optimality:** Does it find the solution with the lowest cost?

3. **Time Complexity:** How long does it take (number of generated nodes)?

4. **Space Complexity:** How much memory does it require (number of stored nodes)?


Typical parameters:

- $b$: branching factor or number of successors of a node that need to be considered.

- $d$: depth of the shallowest solution or number of actions inDepth an optimal solution.

- $m$: maximum length of any path in the state space or the maximum number of actions in any path.


---

## 8. Uninformed Search Strategies

These algorithms have no information about the "distance" to the goal. They only know how to generate successors and check if they have arrived4.

### 8.1 Breadth-First Search ([[BFS]])

Explores all nodes at depth $d$ before moving to $d+1$.

- **Strategy:** FIFO Queue. $f(n) = \text{depth}(n)$.

- **Completeness:** Yes (if $b$ is finite).

- **Optimality:** Yes, but **only if all action costs are equal** (or 1).

- **Complexity:** $O(b^d)$ for both time and space.

- _Problem:_ Memory is the critical bottleneck (exponential).


![[Pasted image 20251125194516.png]]

> Figure 3.8: Progress of BFS8.

### 8.2 Uniform-Cost Search ([[Dijkstra Algorithm]])

Expands the node with the lowest path cost $g(n)$9.

- **Strategy:** Priority Queue. $f(n) = g(n)$ (accumulated cost).

- **Optimality:** Yes, always (if costs $\ge \epsilon > 0$)10.

- **Completeness:** Yes.

- **Complexity:** $O(b^{1 + \lfloor C^*/\epsilon \rfloor})$. Can be worse than BFS if there are many small cost steps11.


![[Pasted image 20251125194555.png]]

> Figure 3.10: Uniform-Cost Search on the Romania map. Expands based on cost, not depth121314.1516

### 8.3 Depth-First Search ([[DFS]])1718

Explores every branch to the end before backtracking

- **Strategy:** LIFO Queue (Stack).

- **Completeness:** No (can get stuck in loops or infinite paths) 

- **Optimality:** No (returns the first solution found, 31even if long).

- **Space:** Very efficient: $O(bm)$ (linear with respect to depth)

- **Time:** $O(b^m)$.


![[Pasted image 20251125194621.png]]

> Figure 3.11: Progress of DFS. Note how the frontier (green) is very small compared to expanded nodes.

### 8.4 Depth-Limited & Iterative Deepening (IDS)

To solve DFS problems (non-completeness) while keeping its advantages (low memory):

1. **Depth-Limited:** DFS with a depth limit $l$. Incomplete if solution is at $d > l$.

2. **Iterative Deepening (IDS):** Runs Depth-Limited with $l=0$, then $l=1$, then $l=2$...

- **Completeness:** Yes.

- **Optimality:** Yes (if costs are equal).

- **Memory:** $O(bd)$ (like DFS).

- _Note:_ Regenerating nodes seems expensive, but the cost is dominated by the last level ($b^d$ nodes), so asymptotically it has the same time complexity as BFS ($O(b^d)$). It is the preferred algorithm for uninformed search with large state spaces37373737.


![[Pasted image 20251125194647.png]]

> Figure 3.13: Iterative Deepening Search38.

### Summary Table

![[Pasted image 20251125194709.png]]

> Figure 3.15: Comparison of uninformed search strategies39.

---

## 9. Informed (Heuristic) Search Strategies

These strategies use domain-specific hints about the location of goals to find solutions more efficiently than an uninformed strategy. The hints come in the form of a **heuristic function $h(n)$**, which returns the estimated cost of the cheapest path from the state at node $n$ to a goal state.
![[Pasted image 20251125124915.png]]

### 9.1 Greedy Best-First Search

This algorithm expands first the node with the lowest $h(n)$ value—the node that appears to be closest to the goal—on the grounds that this is likely to lead to a solution quickly3.

- **Strategy:** $f(n) = h(n)$.
    
- **Example:** Using the straight-line distance ($h_{SLD}$) to Bucharest as the heuristic for route-finding.
    
- **Properties:**
    
    - **Completeness:** It is complete in finite state spaces, but not in infinite ones.
        
    - **Optimality:** It is **not cost-optimal**7. On each iteration, it tries to get as close to the goal as it can ("greedy"), but this can lead to worse results than being careful, such as finding a path that is physically longer but appears shorter at each step.
        
- **Complexity:** The worst-case time and space complexity is $O(|V|)$ (where $|V|$ is the number of vertices), but with a good heuristic function, the complexity can be reduced substantially.
    

### 9.2 A* Search


The most common informed search algorithm, A* (pronounced "A-star"), combines the cost of the path already traveled ($g(n)$) with the estimated remaining cost ($h(n)$).

- **Function:** $f(n) = g(n) + h(n)$.
    
- $f(n)$ represents the estimated cost of the **best path** that continues from $n$ to a goal.
    
- **Completeness:** Yes, A* search is complete.
    
- **Optimality:** Yes, provided that $h(n)$ is **Admissible** (or Consistent).
    
- **Search Contours:** A* search can be visualized as drawing contours (like a topographic map). Because it expands the frontier node of the lowest $f$-cost, the search fans out from the start node in concentric bands of increasing $f$-cost 15. With a good heuristic, these bands stretch toward a goal state and become narrowly focused around an optimal path.
    

#### Admissible Heuristic

A heuristic $h(n)$ is admissible if it **never overestimates** the cost to reach a goal17. An admissible heuristic is therefore "optimistic".

- $h(n) \le h^*(n)$ (where $h^*$ is the true optimal cost to the goal).
    
- **Example:** Straight-line distance ($h_{SLD}$) is admissible because it is the shortest distance between two points, so it never exceeds the actual road distance.
    
- **Optimality Proof:** If $h(n)$ is admissible, A* returns only cost-optimal paths. If it were to return a suboptimal path, there would have to be some unexpanded node on the true optimal path with an $f$-value lower than the returned path's cost, which contradicts the algorithm's selection process.
    

#### Consistency (Stronger Condition)

A heuristic is consistent if, for every node $n$ and every successor $n'$ generated by action $a$, the estimated cost $h(n)$ is no greater than the step cost plus the estimated cost of the successor:

$$h(n) \le c(n, a, n') + h(n')$$

This is a form of the **triangle inequality**.

- Every consistent heuristic is admissible.
    
- With a consistent heuristic, the first time a state is reached, it is on an optimal path, meaning the algorithm never has to re-add a state to the frontier.