# 01 - Introduction to Knowledge-Based Agents and The Wumpus World

## Knowledge-Based Agents
Before diving into the syntax of logic, it is important to understand how logic is used within an Artificial Intelligence system. Intelligent agents need knowledge about the world in order to reach good decisions. A **knowledge-based agent** uses a process of reasoning over an internal representation of knowledge to decide what actions to take.

*   **Knowledge Base (KB):** The central component of this agent is its knowledge base, which is a set of "sentences" expressed in a knowledge representation language.
*   **Axioms:** When a sentence is taken as given without being derived from other sentences, it is called an axiom.
*   **TELL and ASK Operations:** The agent interacts with the KB through two main operations. It uses `TELL` to add new sentences (or percepts) to the KB, and `ASK` to query what is known in order to choose an action. Both operations may involve **inference**, which is the process of deriving new sentences from old ones.
*   **Declarative vs. Procedural Approach:** Building an agent by `TELL`ing it what it needs to know step-by-step is known as the *declarative* approach, which contrasts with the *procedural* approach where behaviors are hard-coded into the program.

## Motivating Example: The Wumpus World

![[Pasted image 20260305144402.png]]

To illustrate how a knowledge-based agent operates, we use a classic environment called the **Wumpus World**. The wumpus world is a cave consisting of rooms connected by passageways, hiding a wumpus that eats anyone who enters its room, and bottomless pits that trap the agent.

![[Pasted image 20260305144501.png]]![[Pasted image 20260305144510.png]]

The task environment is defined by its **PEAS** (Performance, Environment, Actuators, Sensors) description:
*   **Performance Measure:** +1000 points for climbing out of the cave with the gold, -1000 for falling into a pit or being eaten by the wumpus, -1 for each action taken, and -10 for using up the arrow. The game ends when the agent dies or climbs out.
*   **Environment:** A $4 \times 4$ grid of rooms surrounded by walls. The agent always starts in square facing east. The gold and the wumpus are placed randomly (uniform distribution) in squares other than the start, and every other square has a 0.2 probability of containing a pit.
*   **Actuators:** The agent can move *Forward*, *TurnLeft* (90°), or *TurnRight* (90°). It can use *Grab* to pick up the gold, *Shoot* to fire its single arrow in a straight line to kill the wumpus, and *Climb* to exit the cave from. Moving forward into a wall results in no movement.
*   **Sensors:** The agent receives a percept vector with five bits of information:
    1.  **Stench:** Perceived in squares directly adjacent (not diagonally) to the wumpus.
    2.  **Breeze:** Perceived in squares directly adjacent to a pit.
    3.  **Glitter:** Perceived in the square containing the gold.
    4.  **Bump:** Perceived when the agent walks into a wall.
    5.  **Scream:** Perceived anywhere in the cave when the wumpus is killed.

## The Need for Logical Inference
In the Wumpus World, the agent cannot directly see the pits or the wumpus. It can only perceive breezes and stenches locally. However, a cautious agent will move only into a square that it definitively knows to be safe ("OK").

By combining the percepts it gathers over time with its initial knowledge of the rules of the environment, the agent is able to indirectly infer the position of hidden dangers. For instance, if an agent is in and feels a stench, but felt no stench previously in or, it can systematize this information to logically deduce the exact location of the wumpus.

This guarantees that conclusions are correct if the available information is correct, which is a fundamental property of logical reasoning. To systematize this inference procedure, we use **Propositional Logic**.

# 02 - Syntax and Semantics of Propositional Logic

## Building Blocks of Logical Systems
Any formal logical system must provide three fundamental components:
1.  **Syntax:** Defines which strings of characters constitute a well-formed formula in the logic. It is the structural representation.
2.  **Semantics:** Defines the *meaning* of each formula. Specifically, it defines the truth of each sentence with respect to each possible world (or model).
3.  **Inference System:** Specifies the rules and processes to infer new knowledge from existing knowledge.

The connection between logical reasoning processes and the real environment is called *grounding*, meaning that while inference operates on "syntax" (internal representations), it corresponds to real-world relationships.

---

## Syntax of Propositional Logic
Propositional logic is a formalism for representing the state of the world and reasoning about it. The syntax defines the allowable sentences.

### Propositional Alphabet
*   **Atomic Sentences (Propositions):** A countable set $P$ of atomic propositions (or atoms or variables). Each symbol stands for a proposition that can be either *true* or *false* (e.g., $S_{1,2}$ for "there is a stench in cell"). The symbols `True` (always true) and `False` (always false) are also fixed atomic sentences.
*   **Logical Connectives:**
    *   $\neg$ **(NOT / Negation):** A sentence such as $\neg W_{1,3}$ is the negation of $W_{1,3}$.
    *   $\land$ **(AND / Conjunction):** A sentence whose main connective is $\land$ is a conjunction; its parts are the *conjuncts*.
    *   $\lor$ **(OR / Disjunction):** A sentence whose main connective is $\lor$ is a disjunction; its parts are the *disjuncts*.
    *   $\Rightarrow$ or $\supset$ **(Implies / Implication):** Also known as rules or if-then statements. The left side is the *premise* (or antecedent) and the right side is the *conclusion* (or consequent).
    *   $\Leftrightarrow$ or $\leftrightarrow$ **(If and only if / Biconditional):** Represents material equivalence.

> **Note on Terminology:** A **literal** is either an atomic sentence (a *positive literal*, e.g., $P$) or a negated atomic sentence (a *negative literal*, e.g., $\neg P$).

### Formulas of Propositional Logic
Not all sequences of symbols are valid formulas. The set of well-formed formulas is defined inductively:
1. Every atomic proposition $p \in P$ is a formula.
2. If $\phi$ and $\psi$ are formulas, then $\neg\psi$, $\phi \land \psi$, $\phi \lor \psi$, $\phi \supset \psi$, $\phi \leftrightarrow \psi$, and $(\phi)$ are also formulas.
3. Nothing else is a formula.

*(The book formalizes this using a strict Backus-Naur Form (BNF) grammar).*

### Operator Precedence
To resolve ambiguities in reading formulas without explicit parentheses (e.g., $\phi \land \psi \supset \gamma$), propositional logic relies on operator precedence. From highest to lowest precedence:
1. $\neg$
2. $\land$
3. $\lor$
4. $\supset$ (or $\Rightarrow$)
5. $\leftrightarrow$ (or $\Leftrightarrow$)

Thus, $\phi \land \psi \supset \gamma$ is correctly read as $(\phi \land \psi) \supset \gamma$.

---

## Semantics of Propositional Logic
Semantics defines the rules for determining the truth of a sentence with respect to a particular mathematical abstraction called a **model** (or interpretation).

### Propositional Interpretations (Models)
A propositional interpretation $I$ is a function assigning a truth value, $T$ (true) or $F$ (false), to every propositional symbol: $I: P \rightarrow \{T,F\}$.
Alternatively, an interpretation can be represented as a set $I \subseteq P$, under the convention that $I(p) = T$ if and only if $p \in I$.

If a sentence $\phi$ is true in a model $m$, we say that **$m$ satisfies $\phi$**, or $m$ is a model of $\phi$ (written as $m \models \phi$). The set of all models of $\phi$ is denoted as $M(\phi)$.

### Truth Evaluation and Truth Tables

![[Pasted image 20260305144722.png]]

In order to assign a truth value to a complex formula, we compute it recursively based on the truth values of its atomic symbols.
*   $I \models p$ iff $p \in I$
*   $I \models \neg\psi$ iff $I \not\models \psi$
*   $I \models \psi \land \gamma$ iff $I \models \psi$ and $I \models \gamma$
*   $I \models \psi \lor \gamma$ iff $I \models \psi$ or $I \models \gamma$
*   $I \models \psi \supset \gamma$ iff $I \not\models \psi$ or $I \models \gamma$
*   $I \models \psi \leftrightarrow \gamma$ iff $I \models \psi \supset \gamma$ and $I \models \gamma \supset \psi$

This inductive evaluation can be represented using **Truth Tables**.

> **Important note on Implication ($\Rightarrow$):** The truth table for implication can be counter-intuitive. Propositional logic does not require any relation of causation between the premise and the conclusion. Any implication is true whenever its antecedent is false. For example, "5 is even $\Rightarrow$ Sam is smart" is a true sentence in propositional logic simply because the premise is false.

### Algorithm for Checking $I \models \phi$
This recursive evaluation translates perfectly into a simple checking algorithm:

``` javascript
Boolean check(I, φ) { // Returns true iff I ⊨ φ
    if φ is an atom then return true if φ ∈ I, false otherwise
    if φ = ¬ψ then return (!check(I, ψ))
    if φ = ψ ∧ γ then return (check(I, ψ) && check(I, γ))
    if φ = ψ ∨ γ then return (check(I, ψ) || check(I, γ))
    if φ = ψ ⊃ γ then return ((!check(I, ψ)) || check(I, γ))
    if φ = ψ ↔ γ then return (check(I, ψ ⊃ γ) && check(I, γ ⊃ ψ))
    if φ = (ψ) then return check(I, ψ)
}
```

# 03 - Knowledge Bases, Entailment, and Satisfiability

## Knowledge Bases (KBs)
A set $\Gamma$ of propositional formulas is called a **Knowledge Base** (KB). It provides an agent with knowledge about some world, and it can be used to reason about that world.

### Example: The Wumpus World KB
To formalize the Wumpus World, we can build a KB starting with atomic propositions:
*   $p_{x,y}$: pit in $[x,y]$
*   $w_{x,y}$: Wumpus in $[x,y]$
*   $b_{x,y}$: breeze in $[x,y]$
*   $s_{x,y}$: stench in $[x,y]$
*   $l_{x,y}$: agent is in $[x,y]$

We then add formulas describing the constraints of the map:
1.  **Wumpus is in exactly one square:** $\bigvee w_{x,y}$ (at least one) and $\neg(w_{x,y} \land w_{x',y'})$ for all $(x,y) \neq (x',y')$ (at most one).![[Pasted image 20260305152701.png]]
2.  **Stench Rules:** A square has a stench if and only if there is a Wumpus in an adjacent square. E.g., $s_{x,y} \leftrightarrow w_{x+1,y} \lor w_{x,y+1} \lor w_{x-1,y} \lor w_{x,y-1}$.![[Pasted image 20260305152719.png]]
3.  **Breeze Rules:** A square has a breeze iff there is a pit in an adjacent square. E.g., $b_{x,y} \leftrightarrow p_{x+1,y} \lor p_{x,y+1} \lor p_{x-1,y} \lor p_{x,y-1}$.![[Pasted image 20260305152735.png]]
4.  **Initial Safe Square:** No pit in $[1, 1]$: $\neg p_{1,1}$.

Only the interpretations (models) that satisfy **all** the formulas in the KB are relevant and represent physically possible map configurations.

# Logical Inference in the Wumpus World

**Tags:** #ArtificialIntelligence #PropositionalLogic #WumpusWorld #LogicalInference #ModelChecking

## Interpretations and Map Configurations
In Propositional Logic applied to the Wumpus World, every interpretation corresponds to a specific map configuration, and vice versa. An interpretation is essentially an assignment of truth values to all propositional symbols (e.g., $\{l_{1,1}, b_{2,1}, p_{3,1}, \dots\}$).

However, interpretations can model maps that are inconsistent with the agent's Knowledge Base (KB). For the agent's reasoning process, **only the interpretations that satisfy *all* formulas in the KB are relevant**. If an interpretation fails to satisfy even a single formula—such as $b_{2,2} \leftrightarrow p_{3,2} \vee p_{2,3} \vee p_{1,2} \vee p_{2,1}$—it is not a valid model of the KB.

## Ruling Out Inconsistent Models via Entailment
As the agent navigates the environment and perceives features (like breeze or stench), some or possibly all previously considered maps are ruled out. The KB becomes false in any models that contradict what the agent knows through its percepts.

This reasoning relies on the core logical concept of **entailment** ($\alpha \models \beta$). Entailment means that a sentence logically follows from another: if $\alpha$ entails $\beta$, then in every model where $\alpha$ is true, $\beta$ must also be true. Mathematically, this is expressed as $M(\alpha) \subseteq M(\beta)$, where $M$ denotes the set of models.
*   **Example:** If the KB entails $\alpha_1$ ("There is no pit in"), it means that in all models where the KB is true, $\alpha_1$ is also true, making it safe for the agent to move.
*   If the KB does not entail $\alpha_2$ ("There is no pit in"), the agent cannot conclude that the square is safe, as there are models where the KB is true but $\alpha_2$ is false.

## The Model Checking Algorithm
Before making a move, the agent must systematically check if a danger (like a pit) can exist in an adjacent square. To find out if a pit could be in, the agent considers the observations collected so far ($Obs$) and checks whether there is a model that satisfies all formulas in the set $\Gamma \cup Obs \cup \{p_{1,2}\}$ (where $\Gamma$ is the Wumpus World KB). If such a model exists, it means there is a valid map where the breeze and pit align, making the move to unsafe.

This systematic evaluation is known as **model checking**. It works by enumerating all possible models to check if a query $\alpha$ is true in all models where the KB is true.

### Inference Properties
While entailment is like knowing the needle is in the haystack, **inference** is the actual algorithm used to find it. If an inference algorithm $i$ can derive $\alpha$ from the KB, it is denoted as $KB \vdash_i \alpha$. For an inference algorithm to be reliable, it must possess two key properties:
1.  **Soundness (Truth-preserving):** The algorithm only derives sentences that are actually entailed by the KB. An unsound procedure would make things up, discovering "nonexistent needles". Model checking is a sound procedure.
2.  **Completeness:** The algorithm can derive *any* sentence that is entailed by the KB.

![[Pasted image 20260305152828.png]]![[Pasted image 20260305152809.png]]![[Pasted image 20260305152841.png]]![[Pasted image 20260305152848.png]]![[Pasted image 20260305152857.png]]

# Propositional Satisfiability, Validity, and Implication

**Tags:** #ArtificialIntelligence #PropositionalLogic #SAT #TheoremProving #LogicalImplication

## Propositional Satisfiability (SAT)
The problem of checking whether there exists an interpretation $I$ (or model) that satisfies a propositional formula $\varphi$ is called the **Propositional Satisfiability Problem (SAT)**.
*   **Satisfiable:** A formula $\varphi$ is satisfiable if there exists *at least one* interpretation $I$ such that $I \models \varphi$. For example, $\neg(a \lor b) \to c$ is satisfiable because it is true in the interpretation $I=\{c\}$.
*   **Unsatisfiable:** If a formula has absolutely no models, it is unsatisfiable (e.g., $a \land (a \to b) \land (b \to \neg a)$).

The SAT problem is one of the most studied problems in Computer Science and was the very first problem proven to be **NP-complete**. A naive way to check satisfiability is by constructing a **Truth Table**. However, this requires listing all $2^{|P|}$ possible interpretations (where $P$ is the set of propositional variables), which leads to exponential time complexity and is highly inefficient for large systems.

## Valid Formulas (Tautologies)
A propositional formula $\varphi$ is **valid** if $I \models \varphi$ for *all* possible interpretations $I$. Valid sentences are also known as **tautologies**—they are necessarily true regardless of the state of the world (e.g., $P \lor \neg P$).

Because the sentence `True` is true in all models, every valid sentence is logically equivalent to `True`.

## The Connection: Satisfiability, Unsatisfiability, and Validity
Validity and satisfiability are deeply connected through negation. Understanding these relationships is fundamental for logical theorem proving:
*   If $\varphi$ is valid, then it is inherently satisfiable.
*   $\varphi$ is **satisfiable** if and only if $\neg\varphi$ is **not valid**.
*   $\varphi$ is **valid** if and only if $\neg\varphi$ is **unsatisfiable**.
*   $\varphi$ is **unsatisfiable** if and only if $\neg\varphi$ is **valid**.

These definitions apply equally to finite Knowledge Bases (KBs), where $I \models \Gamma$ is equivalent to checking if $I \models \varphi_1 \land \varphi_2 \land \dots \land \varphi_n$.

## Using Satisfiability in the Wumpus World
Whenever we want to check if a specific property is *possible* in our environment (e.g., "Can there be a pit in?"), we must check for satisfiability.
To check if a pit can be in, the agent assumes the observations collected so far ($Obs$) and checks if there exists a model for all formulas in $\Gamma \cup Obs \cup \{p_{1,2}\}$.
*   If such a model exists, the configuration is possible.
*   If a logical contradiction occurs (e.g., the rules dictate that a breeze must be present, but the percepts show no breeze), no interpretation can satisfy all formulas. Thus, the scenario is **unsatisfiable**, proving that no pit can exist in.

## Logical Implication and Equivalence
*   **Logical Implication ($\varphi \models \psi$):** A formula $\varphi$ logically implies $\psi$ if, for every interpretation $I$ where $I \models \varphi$, it is also the case that $I \models \psi$. This means the set of models of $\psi$ completely includes the models of $\varphi$.
*   **Logical Equivalence ($\varphi \equiv \psi$):** Two formulas have the exact same meaning if they are true in the same set of models. This is equivalent to saying $\varphi \models \psi$ AND $\psi \models \varphi$.

### Core Properties for Theorem Proving
Instead of enumerating models with truth tables, we can use inference rules to construct a proof. Two crucial principles bridge the gap between entailment and satisfiability/validity:
1.  **The Deduction Theorem:** $\Gamma \cup \{\varphi\} \models \psi$ if and only if the implication $\Gamma \models (\varphi \to \psi)$ is valid. This means every valid implication sentence describes a legitimate inference.
2.  **The Refutation Principle (Proof by Contradiction):** $\Gamma \models \varphi$ if and only if $\Gamma \cup \{\neg\varphi\}$ is **unsatisfiable**.

*Note: The Refutation Principle (also known as reductio ad absurdum) is the foundation of many modern automated theorem provers. Instead of proving that a query is true, algorithms will assume the query is false ($\neg\varphi$) and attempt to find a contradiction within the Knowledge Base*.