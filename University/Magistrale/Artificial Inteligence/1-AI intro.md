# Introduction to Artificial Intelligence

**Tags:** #uni #AI #engineering #notes

---

## 1. What is Artificial Intelligence?

There is no single unique definition, but the field has evolved through several historical approaches. The main goal is to create agents (programs or devices) that act "intelligently".

### The 4 Historical Approaches
The book categorizes AI based on two dimensions: **Thought vs. Action** and **Human vs. Rational**.

1. **Acting Humanly (Turing Test - 1950):** The inability to distinguish the machine from a human . It requires NLP, knowledge representation, and automated reasoning .
2. **Thinking Humanly (Cognitive Modeling):** Trying to simulate the functioning of the human mind (cognitive science) .
3. **Thinking Rationally (Logic):** Using deductive logic (e.g., Aristotle's syllogisms) to reach correct conclusions . *Problem:* It is difficult to formalize everything in logic.
4. **Acting Rationally (Modern Approach):** Acting to maximize the achievement of a goal (or expected utility).
* This is the prevailing approach today.
* It includes logical reasoning as a means but also admits actions based on reflexes or intuitions in cases of uncertainty .

> **Formal Definition:** AI consists of designing **agents** that behave in a way that maximizes an **objective function** (or performance measure).

---

## 2. Deductive vs. Inductive AI (AI vs. ML)

Modern AI applications often combine two souls:

| **Deductive Approach (Reasoning / "Good Old-Fashioned AI")** | **Inductive Approach (Machine Learning)** |
| :--- | :--- |
| Starts from general rules, facts, and goals defined a priori. | Starts from collected **data** (examples). |
| Deduces new knowledge or actions through logical/probabilistic reasoning. | Learns the input-output relationship (the "rule") by analyzing data. |
| "Exact", explainable methods. | Focus on performance, often "black box". |

> **Note:** Machine Learning is a sub-area of AI. It concerns learning from data, but it does not cover the entire AI field (which includes planning, search, knowledge representation) .

---

## 3. Historical Notes

- **Official Birth:** Dartmouth Workshop (1956). Founding hypothesis: *"Every aspect of learning or any other feature of intelligence can in principle be so precisely described that a machine can be made to simulate it"* .
- **Hype Cycles and AI Winters:** The history of AI alternates moments of great expectations with periods of disillusionment (AI Winter) due to unfulfilled promises.
- **State of the Art:** Today AI excels in specific tasks (autonomous driving, translation, games like Chess/Go with AlphaZero, medical diagnosis), but it still lacks ethics, empathy, and deep context understanding (General Intelligence) .

---

## 4. Intelligent Agents

This is the architectural basis of modern AI.

### Definition of Agent
An agent is any entity capable of:
1. **Perceiving** the environment through **sensors**.
2. **Acting** upon the environment through **actuators**.

The agent possesses an "Agent Function" (or deliberation module) that maps the history of perceptions into an action.

![[Insert Image Figure 2.1 from PDF here]]
> *Figure 2.1: General Agent-Environment interaction scheme. The agent receives Percepts and returns Actions.*

### Rational Agent
A rational agent is one that does "the right thing".
- **Criterion:** Maximize the expected value of the **Performance Measure**.
* Rationality depends on :
1. The performance measure (e.g., cleaning the house, winning at chess).
2. Prior knowledge of the environment.
3. Available actions.
4. The sequence of past percepts.

> **Warning:** Rationality $\neq$ Omniscience. Rationality maximizes the *expected* result based on what the agent knows, not the *actual* result (which might depend on unforeseen factors) .

---

## 5. Environments and PEAS Specifications

To design an agent, one must first define the problem using the acronym **PEAS**:
- **P**erformance (Performance Measure)
- **E**nvironment
- **A**ctuators
- **S**ensors

### Example: Autonomous Taxi (Figure 2.4)
![[Insert Image Figure 2.4 from PDF here]]
> *Figure 2.4: PEAS description example for an automated taxi driver.*

### Properties of Environments
The difficulty of the task depends on the characteristics of the environment. The main dimensions (Fig 2.6 of the book) are :

1. **Observable (Fully vs. Partially):** Do sensors see the entire state or only a part? (e.g., Chess = Fully; Poker/Driving = Partially).
2. **Agents (Single vs. Multi):** Am I alone or are there opponents/collaborators?
3. **Deterministic vs. Stochastic:** Does the action have a certain or uncertain effect? (Chess = Deterministic; Driving = Stochastic/Non-deterministic).
4. **Episodic vs. Sequential:** Do current decisions influence future ones? (Image classification = Episodic; Chess = Sequential).
5. **Static vs. Dynamic:** Does the environment change while the agent is "thinking"?
6. **Discrete vs. Continuous:** Are the states finite or continuous? (Chess = Discrete; Driving = Continuous).

![[Insert Image Figure 2.6 from PDF here]]
> *Figure 2.6: Examples of environments classified according to their properties.*

---

## 6. Agent Structures (Reasoning Agents)

The slides focus on agents that *reason*, meaning they use a **model of the environment**. The book (Ch 2.4) details different architectures, from simplest to most complex.

### A. Simple Reflex Agent
Acts only based on the *current* perception. *Condition-Action* rules (e.g., `IF car in front brakes THEN brake`) .
* *Limit:* Works well only if the environment is fully observable.

### B. Model-Based Reflex Agent
Maintains an **Internal State** to handle partial observability .
Must know:
1. How the world evolves independently of the agent.
2. How the agent's actions affect the world.

![[Insert Image Figure 2.11 from PDF here]]
> *Figure 2.11: Scheme of a model-based agent. Note "What the world is like now" which persists over time.*

### C. Goal-Based Agent
Knowing how the world works is not enough; it needs to know **where it wants to go** (Goal).
The agent uses search and planning to find sequences of actions that lead to the *Goal*.

![[Insert Image Figure 2.13 from PDF here]]
> *Figure 2.13: Goal-based agent. Introduces future projection: "What it will be like if I do action A".*

### D. Utility-Based Agent - **Slide Focus**
Often there are many ways to reach a goal, but some are better (faster, safer, cheaper).
- **Utility Function:** Assigns a real number (score) to how "good" a state is.
* The agent chooses the action that maximizes the **Expected Utility**.

![[Insert Image Figure 2.14 from PDF here]]
> *Figure 2.14: Utility-based agent. This is the most general and flexible model for rational agents.*

---
**Next steps:** Deepen understanding of how to represent states (atomic, factored, structured) to allow agents to reason (Ch 3 and following).