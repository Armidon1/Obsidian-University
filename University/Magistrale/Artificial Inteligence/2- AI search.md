# Searching

we are not going to analyse it completely, but this will be a nice introduction and will be necessary to complete by our own with the book. ^781675

We are NOW considering an environment which is:
- **deterministic**: given an input we know exactly which output will be.
- **fully observable**: there are no hidden properties
- **non dynamic**: the agent is the only one who can change the world around him. 
- **single agent**.
in this course we are always assuming that the environment is **fully observable, non dynamic** and single agent.

## Search Problems
Those are the simplest class of problems. We need to formalise this problem. 
Fundamental class of problems in AI. 

A _Search Problem_ is defined by:

- _State space_ : all possible world states (can be infinite)
- _Initial state_ : in what state the world starts
- _Goal state(s)_ : in what state(s) the agent would like to be
- _Actions_ : what the agent can do in each state. the actions that the agent can perform
- _Transition model_ : how the state changes when an action is performed. Is a formalization on how the actions change the state.
- _Action-cost function_ : represents cost of performing action in given state and
    ending up in successor state


## Search Problems

_$P=<S, A, s_0, G⊆S, 𝛼:S→𝒫 (A),𝛿:SxA→S,c:SxAxS→ℝ>$

- S: State space
- $s_0$ : Initial state
- G: Goal states
- A: Action space
- 𝛼 : Action-precondition function: if i'm in a specific state, i can have a set of actions to reach my goal
- 𝛿 : Transition function: given a state and an action, it tells us the next state. This is possible because is deterministic. if it is not, in this case we have a set of possible states.
- c: Action-cost function: given an initial state $s$, and perform an action $a$ to reach another state $s'$, it returns a value $v$ (an integer or something else). 

now we are dealing those concepts in a mathematical way, when we are in programming languages, it is another thing


## Example
![[Pasted image 20251021180828.png]]
Agent can move along edges

Edge weights model distances

Environment is (this is the simplest case):

- fully observable
- single agent
- deterministic
- static
- discrete

we want to reach Bucharest from Arad in the shortest possible way.
There are many possible paths to reach the destination. 

So, let's use the past formailization:
- State space: all possible agent's positions
    - E.g.: _Sibiu_
- Initial state: (agent in) _Arad_
- Goal state: _Bucharest_
- Actions: _applicable_ moves along edges
    - E.g.: $𝛼(Arad)=\{{ToZerind, ToSibiu, ToTimisoara }\}$
- _Transition model_ : all allowed moves
    - $𝛿(Arad, ToZerind)=Zerind$
- _Action-cost function_ : road distance
    - E.g.: $c(Arad,ToSibiu,Sibiu)$=$140$
    - For deterministic environment: $c(Arad,ToSibiu)=140$ (successor state is known)


## Example: vacuum world
![[Pasted image 20251021181640.png]]
a robot moving in two rooms. See the book 

## Example: 8-puzzle
![[Pasted image 20251021181722.png]]
similar to rubiks cube

## Formalization
Useful notions:

- _Path_ : sequence of actions
    - E.g.: _ToTimisoara, ToLugoj, ToMehadia_
- _Solution_ : path leading from initial to (some) goal state (only for deterministic)
    - E.g.: _ToArad, ToSibiu, ToFagaras, **ToBucharest**_ (cost: 450)
- _Optimal_ solution: solution of minimal cost (sum of costs)
    - E.g.: _ToSibiu, ToRimnicuVilcea, ToPitesti, ToBucharest_ (cost: 418)


## Search Algorithm

_Search Algorithm_ : algorithm that solves a Search Problem

Typically (but not always) uses _Search Tree_


## Search Tree (ST)

Fundamental notion in AI

Tree defined by transition model, with:

- _Nodes_ corresponding to states of the problem
- _Root_ corresponding to initial problem's state
- _Edges_ corresponding to actions


## Search Tree

```
WARNING: node ≠ state
```
```
Transition Model Search Tree
```

## Paths in Search Tree

- ST Paths are action sequences applicable from initial state
- Tree Paths from initial state to some goal state are solutions
- We can solve problem by searching a path in the Search Tree

```
Observe: Search Tree can be infinite!
```

## Node Expansion

Node expansion:

- Visit all applicable actions
- Basic search step on ST

Frontier:

- Set of unexpanded nodes


## Node Expansion

Basic search algorithms are based on repeated node expansions

Until goal state reached

Key point: which node to expand next?


## Loops, tree-like and graph-like search

In the presence of loops, we need to mark states already visited

We also need to record cost of getting to state, as searching for optimal solutions

Two search approaches:

```
● Graph-like search : avoid getting stuck in loops, by marking
● Tree-like search: no marking, can get stuck
```

## Best-first Search

General approach to searching

```
● Assume evaluation function f(n) modeling how bad a state is wrt goal
● Expand node n with minimum value f(n) first (Best node first)
● Different evaluation functions yield different search approaches
```

## Best-first Search


## Properties of (Search) Algorithms

```
● Soundness:
○ When the algorithm returns non-failure, is that a solution?
● Completeness:
○ Does the algorithm find a solution when there is one?
● Optimality:
○ Is the returned solution minimal-cost?
● Complexity:
○ Time: How many states/actions are considered, depending on input size?
○ Space: How much memory is required?
```

## Uninformed Search

_Uninformed Search:_ no information about distance to goal is used (or available)

```
● Different evaluation functions f(n) yield different search approaches
● Can still use current (root-to-node) cost to expand
```

## Breadth-first Search

```
● Assume all actions have same cost (e.g.: 1)
● Choose f(n)=depth-of-node-n (shallower nodes are better)
● Best-first then reduces to Breadth First
```
Optimizations: use queue instead of _f(n)_ ; use set of _reached_ states instead of table; _early goal test_

Sound, Complete, Optimal

Complexity: _O(bd)_ for both time and space; b: branching factor; _d_ : depth of shallower goal state


## Breadth-first Search


## Uniform-cost Search (a.k.a. Dijkstra's Algorithm)

Applicable if cost are strictly positive

f(n)=cost of root-to-n path (a.k.a. _path cost_ )

Sound, Complete, Optimal

Time and Space complexity: _O(b1+(C*/_ 𝜖 _))_

```
● C*: cost of optimal solution
● 𝜖 : min cost of
```

## Depth-first Search

f(n)= -(depth-of-n)


## Depth-first Search

```
● Not Optimal :(
● Sound
● Incomplete, in general
○ For infinite state-spaces can get stuck visiting some infinite path
● Complete over finite state spaces
○ may visit same node multiple times
```

## Depth-first Search

However:

```
● Very convenient when tree-search like is feasible
○ Feasibility depends on structure of transition model, e.g., tree-shaped
● Memory efficient!
○ Stores in memory only root-to-node path
○ Space complexity: O(db) , with d depth of tree
```

## Depth-first Search Variants

How to avoid getting stuck down infinite paths?

```
● Depth-limited Limit search up to some depth limit l
○ Time: O(bl)
○ Space: O(bl)
● Iterative-deepening: Increase l iteratively
○ Time: O(bd)
○ Space: O(bd)
```
May not find solution if one exists, even for finite state space


## Uninformed Search: Summary


## Heuristic Search

Assume you know straight-line distance between Bucharest and other cities

How can we use such information to improve search?


## Greedy Best-first Search

Straight-line distance can be taken as an _estimate of road distance_

Idea: expand nodes with shortest straight-line distance from Bucharest first


## Greedy Best-first Search – Example


## Greedy Best-first Search – Example


## Greedy Best-first Search

In general:

```
● h(n): estimated cost of cheapest path form node n to goal node
● h(n) is called heuristic function
● Greedy Best-first search corresponds to Best-first search with f(n)=h(n)
```
Sound, Complete, not Optimal (as example above shows)

Time and Space complexity: _O(bm)_

```
● heuristic function may greatly impact efficiency
```

## A*-Search

Call:

```
● g(n) : cost of path from initial state to node n
● h(n) : estimated cost of best path from n to some goal node
```
A*-Search:

```
● Best-first search with evaluation function f(n)=g(n)+h(n)
● (Intuitively, combines Uniform-cost Search with Greedy Best-first Search)
```

## A*-Search – Example


## A*-Search – Example


## A*-Search – Example


## A*-Search

Use of heuristic function allows for _pruning_ high number of branches in ST

Properties of A*-Search:

```
● Sound
● Complete
● Time and Space complexity : O(bd)
● Optimal? Depends on heuristic function h(n)
```

## Admissible Heuristic Function

_h(n)_ is _admissible_ if it never overestimates cost of reaching goal from _n_

```
Theorem. If h(n) is admissible then A*-Search is Optimal
```
Observe:

```
● there exist pairs of problems and inadmissible h(n) for which A* is optimal
```

## A*-Search Remarks

A* not better than Breadth-first wrt worst-case complexity

However:

```
● Impact of heuristic can be impressive
● Allows for pruning huge number of branches
● (This becomes apparent in many cases, e.g., planning)
```
Memory requirements can still be prohibitive for large state spaces

In practical cases optimized Depth-first approaches used, giving up optimality


