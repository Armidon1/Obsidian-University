# Artificial Intelligence

## A.Y. 2025/

## Prof. Fabio Patrizi


# Introduction to AI


### What is AI?

AI is about devising _agents_ (programs or devices) that act "Intelligently"

Blurry definition, informal

Several approaches, over time:

1. Turing test (1950): act as a human
    - Needs Knowledge Representation and Reasoning abilities (we have it!)
2. Cognitive modeling: think as a human
    - Do we really know how we think?
3. Think rationally: use rules of logic (e.g., Aristotle Syllogisms)
    - Needs formalization of logical reasoning (we have it!)
4. **Act rationally** : act so as to achieve best (expected) outcome
    - Prevailing approach to date, combines 1, 3 and additional abilities (e.g., autonomy, uncertainty)


### What is AI, (a bit more) formally

Devising agents that behave so as to _maximize an objective function_

- Autonomous drive:
    - Reach destination safely and in shortest possible time
- Trading agent:
    - Make as much money as possible
- Chatbot:
    - Reply correctly to as many questions as possible
- E-commerce recommender system:
    - Recommend products so as to maximize number of customers who buy them
- ...


### And Machine Learning?

- Subarea of AI
- Grown so much that it is now studied separately
- Still about **acting rationally** , but:
    - behavior learned from examples (data), not built-in
    - no (primary) interest on internal details (why a decision was made?)


### Inductive vs Deductive AI

Two approaches:

- _Deductive_ (reasoning-based, ``traditional'' AI)
    - Start from general rules, facts, requirements, goals
    - Deduce new knowledge, sequence of actions, etc... through some form of reasoning
    - Includes probabilistic reasoning
    - Typically, ``exact'' methods
- _Inductive_ (ML)
    - Start from collected data
    - Learn input-output relationship underlying data
    - Use learned laws for your purposes (classification, regression, generation, etc...)
    - System may need to generate data itself (e.g., Reinforcement-Learning)
       Modern AI systems typically combine the two!

#### (AI)

#### (ML)


### Some Examples/

AlphaZero:

- A World-Champion level algorithm for Go, Chess and Shogi (Japanese Chess)
- Combines probabilistic approach (MCTS) with ML (Reinforcement-Learning, Neural Nets)
- Self-taught by playing against itself

```
(courtesy of DeepMind https://deepmind.google/discover/blog/alphazero-shedding-new-light-on-chess-shogi-and-go/) 7
```

### Some Examples/

NASA Planning, Scheduling and Resource Management tools

```
(courtesy of NASA https://deepmind.google/discover/blog/alphazero-shedding-new-light-on-chess-shogi-and-go/) 8
```

### In this course

We shall see much simpler applications

By the end of the course, you'll be able to:

- Understand the basics of AI systems
- Develop simple AI systems based on basic forms of reasoning
- Learn about advanced approaches of practical relevance


### Official Birth of AI

Summer '56:

- Two-month workshop at Dartmouth College, Hanover (New Hampshire)
- Organized by John McCarthy and Claude Shannon

_The study is to proceed on the basis of the conjecture that every aspect of learning or any other feature of
intelligence can_ **_in principle be so precisely described_** _that a machine can be made to simulate it. An
attempt will be made to find how to make machines use language, form abstractions and concepts, solve
kinds of problems now reserved for humans, and improve themselves. We think that a_ **_significant
advance can be made in one or more of these problems_** _if a carefully selected group of scientists work
on it together_ **_for a summer_**_._

```
(John McCarthy and Claude Shannon, Dartmouth Workshop Proposal)
```
Today we see the proposal as overly optimistic (to say the least) – almost 7 decades have passed since


### AI's Highs and Lows (see Ch. 1.3 for an interesting in-depth report)

Soaring expectations, significant breakthroughs, disillusionment, renewed enthusiasm

```
'40 '50 '60 '70 '80 '90 '00 '10 '20 11
```
```
Early days
first AI programs:Excitement,^
```
chess, checkers,theorem provers, (^)
logical reasoning
DartmouthWS
Knowledge-basedapproaches:
optimism, unrealizable expert systems,^
promises
hype
Probabilisticapproaches: (^)
Uncertainty, agents, learning systems
Big data, big compute, deep learning, LLMs
deep RL, GPUs


### Where does AI stand?

- Autonomous Vehicles (Taxis Available in SF)
- Legged Robots (BigDog)
- Automated Translation (ChatGPT, Gemini, Translate)
- Recommender Systems (Netflix, Amazon, Investments)
- Game Playing (From DeepBlue to AlphaZero)
- Medicine (Automated Diagnosis, Image Analysis)
- Image Recognition, Tagging, etc.
- Summarize text
- Produce essays based on input guidelines


### What can't AI do (to date)?

- Inductive systems can hardly explain their outputs or decisions
- Behave ethically
- Distinguishing right, wrong, good, bad
- Empathize
- Act Creatively (despite appearances)
- Context understanding (e.g., when is a sad situation funny? Sarcasm?)
- Write code (in general)
- Identify and prove interesting Math theorems
- ...


### Summarizing

- AI is a vast (and growing) discipline, encompassing many other
- Incredible successes achieved from inception
- Still a lot of work to be done
- We need to fully understand the basic principles


### Agents

_Agent_ : entity capable of _perceiving_ and _acting_ in an _environment_

```
Agent Environment
```
```
Action
```
```
Perception
```

### A general definition

```
16
```
```
Environment Agent
Chessboard (with Chess rules) Software able to:
```
- access board state (perception)
- move pieces (actions)
Urban roads Autonomous car able to:
- see road/cars, check distances,
access own state (perception)
- accelerate, turn, stop, etc. (actions)
House Robot able to:
- recognize objects, see house/people
(perception)
- grasp, push, pull objects

```
Environment/Agent can be any
```

```
Agent
```
- Perceive through _sensors_ (e.g., a camera)
- Act through _actuators_ (a gripper)
- Deliberate through dedicated module (agent function)

### Agents

```
Environment
```
```
Action
```
```
Perception
```
```
actuators
```
```
sensors
```
```
deliberation
```

_- Utility_ function: function associating a cumulative reward for the overall
    behavior of the agent (through reward/penalty for acting right/wrong)
- Rational agents act so as to _maximize their overall (expected) utility_

```
Agent
```
```
sensors
```
### Rational Agents

```
Environment
```
```
Action
```
```
Perception
```
```
actuators
```
```
deliberation
```

### Rational Agents - Examples

- Chess:
    - Reward for capturing piece (e.g., +10, may depend on specific piece)
    - Penalty for losing a piece (e.g., -10, may depend on specific piece)
    - High reward for checkmating
    - High penalty for being checkmated
    - 0 for Tie
- Maze:
    - Penalty for every step (e.g., -1)
    - High reward for exiting
- Investing agent:
    - High reward for gaining money
    - High penalty for losing money


Question: How to design (and realize) agents able to deliberate so as to maximize
their utility?

```
Agent
```
```
sensors
```
### Rational Agents

```
Environment
```
```
Action
```
```
Perception
```
```
actuators
```
```
deliberation
```
## ?


Question: How to design (and realize) agents able to deliberate so as to maximize
their utility?

Many solution approaches, depending on **nature of environment (and task)**

### Rational Agents


_Environment_ : world the agent acts in (and interacts with)

Nature of environment has **huge** impact on design of agents

Main features:

- Observability: full, partial, unobservable
- # of agents: single-, multi- agent
- Uncertainty: deterministic, non-deterministic, stochastic
- Dynamicity: static, dynamic
- Density: discrete, continuous

### Environment


### Environment Examples


### Reasoning Agents

Focus on _Reasoning_ approaches

Agent requires a _model of the environment_ to _reason_ and _deliberate_

Distinguish between:

- current environment state: what the environment _is_ now
- possible future states: how the environment _would be_ (based on my actions)


### Reasoning Agents

```
sensors
```
```
Environment
```
```
Action
```
```
Perception
```
```
actuators
```
```
Agent
```
```
deliberation module
Current
env state
representation
```
```
Environment
model
```

### Reasoning Agents - Example

```
X
O O
```
```
X
O
```
```
X
O
O
```
```
O X
O
```
(1,1,O)(2,2,X) (^)
(1,1,O)(2,2,X) (^)
(2,1,O)
(1,1,O)(2,2,X) (^)
(1,2,O)
(1,1,O)(2,2,X) (^)
(0,2,O)

#### ... ...

#### ... ... ... ... ... ...

#### ... ...

#### ... ... ... ... ... ...^

```
Environment model
```
```
state
representation
```

