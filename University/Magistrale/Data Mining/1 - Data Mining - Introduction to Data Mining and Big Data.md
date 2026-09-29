---
course: Data Mining / Big Data
university: Sapienza University of Rome
instructors:
  - Aris Anagnostopoulos
  - Luca Becchetti
lecture: 1
topic: Introduction
tags:
  - data-mining
  - big-data
  - lecture-notes
aliases:
  - DM Lecture 1
  - Intro Data Mining
---

# Data Mining / Big Data: Introduction

> [!abstract] What this lecture is about
> The first lecture does not teach a specific algorithm. It sets the stage: **where data come from**, **what makes data "big"**, **why big data is hard to handle**, **what we typically want to do with it**, and, most importantly, **how easy it is to draw wrong conclusions from it**. Everything in the rest of the course (similarity, clustering, dimensionality reduction, etc.) is a technical answer to the problems raised here.

---

## Instructors

The course is taught by two instructors, both from the Department of Computer, Control and Management Engineering (DIAG) at Sapienza.

### Aristidis Anagnostopoulos

- Professor in computer engineering at Sapienza.
- Studied in Greece and in the USA, worked in the US for a while, then moved to Sapienza.
- Works on **algorithms, data mining and data analysis**.
- Application areas: search engines, social networks, recommender systems, misinformation, biology, finance, medicine, …

### Luca Becchetti

- Works on **algorithms and theory** for data mining, machine learning and distributed processes.
- Recent research: mining large (possibly **temporal**) graphs and datasets, algorithms for **high-dimensional spaces**, algorithmic aspects of complex systems.
- Constant theme: **probabilistic analysis**.

> [!tip] Why this matters for you
> The instructors' backgrounds tell you the flavour of the course. Expect a **theoretical, algorithmic and probabilistic** approach: you will not only be asked *how* an algorithm works but *why* it works and *how well* (with bounds, expectations and probabilities). Brush up on basic probability (expectation, variance, independence, concentration bounds).

---

## Goals

- Learn **advanced tools for data analysis** that are not covered in the basic curriculum (e.g., a standard databases or ML course).
  - The **algorithms** and the **intuition/theory** behind them.
  - Their **implementation in realistic scenarios** (hence the hackathon in the exam).
- The emphasis is on datasets that are somehow **"big"**. What "big" really means is discussed later in the lecture, and the answer is more subtle than "many gigabytes".

> [!info] Data mining in one sentence
> **Data mining** is the process of discovering *non-trivial, useful and (ideally) valid* patterns, models or summaries from data. In the context of this course, the key twist is that the data are so large, fast or heterogeneous that **naïve methods stop working**, and we need algorithms designed with memory, time and communication limits in mind.

---

## Where do data come from?

### Data sources

A classic categorisation (from IBM's Big Data hub) divides big data sources into four families:

| Family | Examples | Typical nature of the data |
|---|---|---|
| **Social networking and media** | Facebook, Twitter/X, LinkedIn, blogs, site comments | Text, graphs (who follows whom), images, interactions |
| **Mobile devices** | Calls, texts/IM, location, in-app activity | Logs, time series, GPS traces |
| **Internet transactions** | Purchases (automated or manual), banking activity, investment activity | Structured records, sequences of events |
| **Networked devices / sensors** | Internet-connected hardware (IoT), sensors (temperature, movement, pressure, humidity), beacon interactions | Continuous numeric streams |

> [!note] Key observation
> Most of this data is **not generated for the purpose of analysis**. It is a *by-product* of other activities (communicating, buying, moving). This is one of the roots of many of the "traps" discussed at the end of the lecture: the data were not designed as a scientific sample.

### Digital universe and digital footprint

- The **digital universe** is the totality of data created, captured and replicated worldwide.
- Your **digital footprint** (or *digital shadow*) is the trail of data you leave behind by using apps and services: social profiles, search history, purchases, locations, streaming habits, etc.
  - **Active footprint**: data you deliberately publish (a post, a review).
  - **Passive footprint**: data collected about you without explicit action (cookies, logs, location pings, metadata).

The footprint is what makes many data mining applications possible (recommendations, targeted ads), and also what raises **privacy** concerns.

---

## How big is "big"?

### The growth of things

According to the **IDC Digital Universe Study**:

- In **2009** the digital universe was about **0.8 zettabytes**.
- It was projected to reach **35.2 zettabytes in 2020**, i.e., growth by a **factor of 44**.
- A visual comparison: a stack of DVDs holding all the data in 2009 would reach the Moon and back; by 2020 it would reach halfway to Mars.

> [!info] Reality exceeded the forecast
> Later IDC estimates put the data created and replicated in 2020 at around **64 ZB**, almost twice the original projection. Growth is roughly exponential.

**Units refresher** (decimal, powers of $10^3$):

| Unit | Bytes | Intuition |
|---|---|---|
| Kilobyte (KB) | $10^3$ | A short text page |
| Megabyte (MB) | $10^6$ | A photo, a book |
| Gigabyte (GB) | $10^9$ | A movie |
| Terabyte (TB) | $10^{12}$ | A consumer hard drive |
| Petabyte (PB) | $10^{15}$ | A large company's data warehouse |
| Exabyte (EB) | $10^{18}$ | A large cloud provider's storage |
| Zettabyte (ZB) | $10^{21}$ | Order of the whole digital universe |

**The "data deluge" in science** (sizes of scientific datasets):

| Project | Size |
|---|---|
| ENCODE (Encyclopedia of DNA Elements), 2012 | 15 TB |
| US National Climate Assessment (NASA projects), 2013 | 1,000 TB (1 PB) |
| IPCC Fifth Assessment Report, 2014 | 2,500 TB (2.5 PB) |
| Square Kilometre Array (SKA) radio telescope | ~22,000,000,000 TB **per year** (22 ZB/year of raw data) |

The SKA figure shows that science, not only the Web, produces data volumes that simply **cannot be stored in full**. Data must be processed and reduced *as it arrives*.

### In a nutshell: the 3 → 4 V's

The most cited definition is Gartner's:

> [!quote] Gartner's definition
> "Big data is **high-volume**, **high-velocity** and/or **high-variety** information assets that demand cost-effective, innovative forms of information processing that enable enhanced insight, decision making, and process automation."

Unpacking it:

- **Volume**: scale of the data (how much).
- **Velocity**: speed at which data is generated and must be processed (how fast).
- **Variety**: diversity of formats and sources (how heterogeneous).
- The "and/or" is important: a dataset can be "big" because of **just one** of these dimensions.
- The second half of the definition matters too: big data **demands new forms of processing**. Data is "big" when conventional tools no longer suffice.

The 4th V, added by IBM, is:

- **Veracity**: certainty/trustworthiness of the data (noise, errors, bias, fake data).

Other V's sometimes added: **Validity** (is the data correct and appropriate for the intended use?), **Volatility** (how long does the data remain relevant, and how long should it be stored?), and **Value** (the ability to turn data into insights and decisions: the actual *point* of the whole effort).

Figures from the IBM infographic, useful to fix orders of magnitude:

- **Volume**: about 2.5 quintillion bytes ($2.5 \times 10^{18}$) created every day; 90% of the world's data was created in the preceding two years.
- **Velocity**: global Internet traffic estimated at 50,000 GB/second by 2018.
- **Variety**: 90% of generated data is **unstructured** (tweets, photos, customer purchase histories, customer service calls).
- **Veracity**: 1 in 3 business leaders do not trust the information they use to make decisions; poor data quality was estimated to cost the US economy around \$3.1 trillion per year.
- **Value**: case study of an aircraft engine manufacturer using analytics to predict engine events that lead to costly airline disruptions.

> [!warning] Don't forget veracity
> The instructors stress veracity explicitly. Big data does **not** mean good data. A huge dataset with systematic bias gives you a very *precise* estimate of the *wrong* quantity. More data reduces random error, **not** systematic error.

---

## Challenges

Each of the V's translates into a concrete technical challenge.

### Volume

**Level 1: the data do not fit in main memory (RAM).** Examples:

- A search engine **query log** (billions of queries).
- A **snapshot of the Web** (billions of pages).
- The **user pairwise-similarity matrix** in a collaborative filtering system: with $n$ users you need $n^2$ entries. For $n = 10^6$ users that is $10^{12}$ entries; at 4 bytes each, **4 TB**, far beyond any RAM.

**Level 2: the data do not fit on the secondary storage (disk) of a single machine.** Examples:

- A **Web corpus** (the crawl used by a search engine).
- **Large Hadron Collider** data at CERN: on the order of 100 GB/s after filtering. The raw collision data rate is much higher; "trigger" systems discard the vast majority of events in real time, keeping only potentially interesting ones.

> [!info] Why memory matters so much: the memory hierarchy
> Approximate access latencies:
>
> | Level | Latency | Relative to RAM |
> |---|---|---|
> | CPU cache (L1) | ~1 ns | 100× faster |
> | Main memory (RAM) | ~100 ns | 1× |
> | SSD random read | ~100 µs | ~1,000× slower |
> | HDD seek | ~10 ms | ~100,000× slower |
> | Network round trip (datacenter) | ~0.5 ms | ~5,000× slower |
>
> Once data leaves RAM, **the cost model changes**: the number of *disk accesses* or *network transfers* dominates, not the number of CPU operations. This is why big-data algorithms are designed to minimise passes over the data and communication between machines (e.g., MapReduce, streaming algorithms, sketches).

### Velocity

Data arrive continuously and fast. An (older, ~2012) estimate of what happens on the Internet **every 60 seconds**:

- 98,000+ tweets
- 695,000 Facebook status updates
- 11 million instant messages
- 698,445 Google searches
- 168 million+ emails sent
- 1,820 TB of data created
- 217 new mobile web users

These numbers are much larger today (see live counters at internetlivestats.com). The accompanying picture describes the evolution of IT: **Mainframe → Client/Server → The Internet → Mobile, Social, Big Data & the Cloud**.

> [!note] Consequence: the streaming model
> When data arrive faster than you can store them, you must process each item **once, on the fly**, using limited memory. This is the **data stream model**: you see a sequence $x_1, x_2, \dots$ and at any time must answer queries (e.g., "how many distinct items so far?") using memory much smaller than the stream. Exact answers are often impossible, so we accept **approximate answers with probabilistic guarantees**.

### Variety

- **Heterogeneous sources**: social media, sensors, transactions, logs, images, video, audio.
- **Structured vs unstructured**:
  - *Structured*: fixed schema, e.g., relational tables.
  - *Semi-structured*: some structure but flexible (JSON, XML, HTML, log lines).
  - *Unstructured*: free text, images, video.
  - Big data is **often unstructured or semi-structured**, so part of the job is turning it into a representation algorithms can use (e.g., vectors, sets, graphs).
- **Part of the data is transient** (e.g., streamed videos): it flows through the system and is never stored.
- **Only part of it is available for analysis** (privacy, proprietary data, technical limits). What you analyse is already a (possibly biased) subset.

### Issues: a random list

A collection of practical problems that arise with big data:

- **Data may not be stored permanently.** For example, only around 1% of LHC data is actually analysed (as reported by ScienceAlert). You often get one chance to look at the data.
- **Moving data is expensive.** Transferring petabytes over the network takes a long time and costs money. Principle of **data locality**: *move the computation to the data, not the data to the computation*.
- **It may be impossible to keep all data in a single place**, so data are distributed across many machines and possibly data centres.
- **In general, space becomes an issue**, not only time.
- **Distributed/parallel programming** is required, with all its difficulties: synchronisation, failures, load balancing, communication costs.
- **Heterogeneous programming environments**: different frameworks, languages, clusters.
- **Performance is the main issue.** A computation that is normally trivial may become infeasible.

> [!example] Exercise: pairwise similarity with the naïve method
> **Problem.** You have feature vectors for $n = 10^6$ users and want all pairwise similarities. Computing the similarity of one pair takes 10 ns (all in main memory). How long does the naïve method take?
>
> **Solution.** The number of unordered pairs is
> $$\binom{n}{2} = \frac{n(n-1)}{2} \approx \frac{n^2}{2} = \frac{10^{12}}{2} = 5 \times 10^{11}.$$
> Total time:
> $$5 \times 10^{11} \times 10 \text{ ns} = 5 \times 10^{11} \times 10^{-8} \text{ s} = 5 \times 10^{3} \text{ s} \approx 1.4 \text{ hours}.$$
>
> **Why this is still a problem.** 1.4 hours may look acceptable, but:
> 1. The assumption "everything in main memory" is unrealistic, as we saw: the output matrix alone is terabytes.
> 2. The cost is **quadratic**. Scaling $n$ by 10 multiplies time by 100:
>
> | Users $n$ | Pairs $\approx n^2/2$ | Time at 10 ns/pair |
> |---|---|---|
> | $10^6$ | $5 \times 10^{11}$ | ~1.4 hours |
> | $10^7$ | $5 \times 10^{13}$ | ~6 days |
> | $10^8$ | $5 \times 10^{15}$ | ~1.6 years |
> | $10^9$ | $5 \times 10^{17}$ | ~160 years |
>
> Real platforms have hundreds of millions or billions of users. The lesson: **$O(n^2)$ is not acceptable at scale**. We need methods that find *similar pairs* without comparing *all* pairs (e.g., **Locality-Sensitive Hashing**, covered later in the course under similarity and neighbourhood search).

### A look at the data

What does big data actually look like? Mostly three kinds of objects:

- **Text**, possibly with some structure, e.g., Web pages (HTML).
- **Graphs**, e.g., social networks, the Web link graph, communication networks.
- **Sequences**, e.g., search engine or recommender system logs, the human genome. for instance something that is being etichettato. 

Data are often stored as **simple text files** in more or less standard formats, e.g., **CSV**. The example shown in the lecture:

```
2::1207::4::978298478
2::1968::2::978298881
2::3678::3::978299250
3::3421::4::978298147
...
```

This is the format of the **MovieLens** ratings dataset: `UserID::MovieID::Rating::Timestamp`. Each line says "user 2 rated movie 1207 with 4 stars at time 978298478" (a **Unix timestamp**, seconds since 1 January 1970; this one is at the end of 2000). This is a typical input for a **recommender system**: a sparse user × item matrix stored as a list of triples.

> [!tip] Practical note
> Real datasets are rarely clean: unusual separators (like `::`), missing values, encoding issues, duplicate lines. A big part of real data mining (and of the hackathon) is **parsing and cleaning** before any algorithm is applied.

---

## Application domains

### Some typical tasks

Most data mining applications fall into one of three high-level families:

**1. Retrieving items related to a given query** (the query may be *implicit*):

- **Search engines**: given keywords, return relevant documents.
- **Continuous, DB-like queries** over streams, which are standing questions continuously answered as data flow in:
  - *Top-k most interesting trends* (e.g., trending hashtags).
  - *Number of distinct IP flows* passing through a router. This is the **count-distinct problem**: storing every flow seen is too expensive, so we use probabilistic sketches (e.g., Flajolet–Martin, HyperLogLog) that estimate the count using tiny memory. Used in network monitoring, e.g., to detect anomalies such as scans or DDoS attacks.
- **Classification**: assign items to categories, e.g., *which Web pages are spam?*

**2. Recommending items:**

- **Products** (e.g., Amazon: "customers who bought this also bought…").
- **Documents of potential interest** (e.g., Google Alerts).
- **New links** (e.g., friend suggestions on Facebook: *link prediction* in graphs).
- **Pages for personalised ads**.

**3. Detecting groups of items that are related in some way:**

- **Communities** in social networks (graph clustering).
- **Similar Web pages** (near-duplicate detection, mirrors, plagiarism).

> [!important] Seems little, but it is actually a lot
> Many applications fit one of these high-level descriptions, and the three families are **themselves related**. They all rely on a notion of **similarity**: retrieval returns items similar to a query, recommendation suggests items similar to what you liked (or liked by users similar to you), and clustering groups similar items. This is why the course starts from **similarity measures**.

---

## Caveats and traps

This is the conceptual core of the lecture. Having lots of data and powerful algorithms makes it *easier*, not harder, to fool yourself.

### When is "big" really big?

"Big" is **not an absolute size**. It is the result of your **data size and goals** compared with your **computational resources**:

- **Data volume vs memory**: data are "big" when they don't fit where you need them.
- **Computational/communication complexity vs available resources**: 1 GB of data is small for counting words but big for an algorithm that is quadratic or worse in the input size.

"Big" is a **moving target**: what is big now may not be in the future, as hardware improves (what needed a cluster in 2005 fits on a laptop today).

Some things are going to stay, however. If your algorithm requires $\Omega(2^n)$ steps too often, ask:

- **Is it the algorithm?** Maybe a better (polynomial) algorithm exists.
- **Is it the problem?** Maybe the problem is intrinsically hard (e.g., NP-hard), and no hardware improvement will save you. Then you must change the question: use **approximation algorithms**, **heuristics**, **randomisation**, or accept approximate answers.

> [!note] Why exponential never becomes "small"
> Hardware improvements multiply your capacity by a constant factor. Against $2^n$, doubling the computing power lets you handle just **$n+1$** instead of $n$. Against $n^2$, doubling lets you handle $\sqrt{2}\,n$. Against $n$, doubling lets you handle $2n$. Algorithmic efficiency matters more than hardware.

### Data collection traps

#### The election example

> [!question] Problem
> A political election takes place in country C with two parties, A and B. In the **ideal** case, we collect a sample of Twitter (now X) users that is **representative of all of C's X users**, and 60% of them like party A.
> 1. What can we say about the accuracy of this predictor of the election's outcome?
> 2. Elaborate on the factors affecting the accuracy of our estimate.

**Part 1: statistical (sampling) error.** Even assuming perfect sampling, the 60% is only an *estimate* $\hat p$ of the true fraction $p$ of X users who like A. With a sample of size $n$, the standard error is
$$\text{SE} = \sqrt{\frac{\hat p (1-\hat p)}{n}},$$
and an approximate 95% confidence interval is $\hat p \pm 1.96\,\text{SE}$. For $n = 1000$: $\text{SE} = \sqrt{0.24/1000} \approx 0.0155$, so the interval is about $60\% \pm 3\%$.

A distribution-free alternative (the kind of tool this course likes) is the **Hoeffding bound**: for $n$ independent samples,
$$\Pr\big(|\hat p - p| \geq \varepsilon\big) \leq 2 e^{-2 n \varepsilon^2}.$$
So the probability of a large error decreases **exponentially** in the sample size. The sampling error is *easy to control*: just take more samples. With big data, this is usually the **least** of your problems.

**Part 2: systematic errors (bias), which do not decrease with more data.** The key word is "representative of **X users**", not of **voters**:

- **Population mismatch (selection bias)**: X users are not a random sample of the electorate. They differ in age, education, income, geography, political engagement. Many voters are not on X at all.
- **Self-selection and vocal minorities**: people who post about politics are a particular subset; a small, very active group can dominate the signal.
- **"Liking" ≠ voting**: expressing sympathy online is not the same as going to vote for that party. Social desirability, irony and sarcasm distort the signal.
- **Turnout**: supporters of different parties vote at different rates.
- **Measurement error**: how do we decide that a user "likes A"? Usually via an automatic classifier (sentiment analysis) that itself has errors, possibly biased towards one side.
- **Fake accounts, bots and coordinated campaigns**: inauthentic accounts can inflate apparent support for a party. This is a **veracity** issue.
- **Temporal drift**: opinions change between the time of data collection and election day.
- **Electoral system**: even the exact vote share may not translate directly into who "wins" (seats, districts, coalitions).

> [!warning] Take-home message
> **Total error = random error + systematic error (bias).** Big data shrinks the first term towards zero, but leaves the second untouched. A biased sample of 100 million people is still biased. Famous historical example: the 1936 *Literary Digest* poll, which surveyed about 2 million people (drawn from telephone directories and car registrations, biased towards the wealthy) and predicted the wrong winner, while a much smaller but better-designed sample predicted correctly.

#### General lessons on data collection

- **Data are the result of a sampling process → potential bias.** Whatever you analyse is a subset of reality, selected by some mechanism (who uses the platform, what the API returns, which sensors were working). If the mechanism is correlated with what you measure, your conclusions are biased.
- **Filtering: some attributes may be omitted.** Data cleaning and pre-processing drop columns or records. This can cause:
  - **loss of possibly important information**;
  - **introduction of artificial correlations** (e.g., keeping only "complete" records may retain a subpopulation with special properties);
  - **removal of real ones** (e.g., dropping the variable that explains a relation).
- **At least part of the context is missing.** Data record *what* happened, rarely *why* or *under which circumstances*.

### Data analysis traps

#### Spurious correlations

The lecture shows a chart in which **per capita cheese consumption** in the US correlates almost perfectly (2000–2009) with the **number of people who died by becoming tangled in their bedsheets**. Obviously, there is no relation.

(Source: Tyler Vigen's *Spurious Correlations* website, full of similar absurd examples.)

Why does this happen?

- Many time series simply **trend** over time (population growth, economic growth). Any two trending series will correlate, even if unrelated.
- With **short series** (here only 10 points) high correlation arises by chance easily.
- If you compare **thousands of series with each other**, you are guaranteed to find some that correlate strongly. This is the multiple comparisons problem, formalised by Bonferroni's principle.

Recall the **Pearson correlation coefficient** between $X$ and $Y$:
$$\rho_{X,Y} = \frac{\operatorname{Cov}(X,Y)}{\sigma_X \sigma_Y} \in [-1, 1].$$
It only measures **linear association**; it says nothing about causation or about whether the association is due to chance.

#### Bonferroni's principle

- Data can always present some **unusual patterns that look significant but are not**.
- Example: a database table where rows are people and columns are attributes. With **thousands of attributes**, you can form an enormous number of hypotheses ("people with attribute $i$ also tend to have attribute $j$"). Some of them will seem supported by the data **purely by chance**.

> [!quote] Michael Jordan (IEEE Spectrum interview), in short
> If you just grab a few hypotheses because the data seem to suggest them, you may get lucky and the data will provide some support. But unless you do the full-scale statistical analysis, with error bars and quantified errors, **it's gambling**.

**The multiple testing problem, formally.** Suppose you test $m$ hypotheses, each at significance level $\alpha$ (the probability of a false positive when the hypothesis is actually false). If all hypotheses are false, the **expected number of false positives** is
$$\mathbb{E}[\text{false positives}] = m \cdot \alpha.$$
With $m = 10{,}000$ tests and the classic $\alpha = 0.05$, you expect **500 "significant" findings that are pure noise**.

The classical **Bonferroni correction** tests each hypothesis at level $\alpha / m$, which guarantees (via the union bound) that the probability of *at least one* false positive is at most $\alpha$:
$$\Pr\Big(\bigcup_{i=1}^{m} \text{FP}_i\Big) \leq \sum_{i=1}^{m} \Pr(\text{FP}_i) = m \cdot \frac{\alpha}{m} = \alpha.$$

**Bonferroni's principle (as stated in the main textbook, *Mining of Massive Datasets*).** Compute the **expected number of occurrences** of the pattern you are looking for **under the assumption that data are random**. If this number is significantly larger than the number of *real* occurrences you hope to find, then most of what you find will be **bogus**: you are detecting noise, not the phenomenon.

> [!example] The "evil-doers in hotels" example (from the textbook)
> Suppose we look for pairs of people who meet at the same hotel on two different days, as a sign of suspicious activity. Assume:
> - $10^9$ people, each goes to a hotel on 1 day out of 100;
> - $10^5$ hotels, each holding 100 people (enough for 1% of $10^9$ people);
> - we observe $1000$ days.
>
> Probability that two given people are at the **same hotel on a given day**: both in a hotel, $0.01 \times 0.01 = 10^{-4}$, and in the same one, $\times 10^{-5}$, giving $10^{-9}$.
> Probability of that happening on **two given days**: $(10^{-9})^2 = 10^{-18}$.
> Number of pairs of people: $\binom{10^9}{2} \approx 5 \times 10^{17}$. Number of pairs of days: $\binom{1000}{2} \approx 5 \times 10^{5}$.
>
> Expected number of "suspicious" pairs if everyone behaves **completely at random**:
> $$5 \times 10^{17} \times 5 \times 10^{5} \times 10^{-18} = 250{,}000.$$
> If only a handful of real evil-doer pairs exist, they are buried among 250,000 innocent coincidences. The search is useless, however "big" and clever the data analysis.

The lecture anticipates that the course will show a few funny examples of this, and that other examples are **less funny** (think of innocent people flagged by automatic surveillance systems).

### Data interpretation traps

#### Correlation is not causation

> [!example] Classic example
> - Sleeping with one's shoes on is **strongly correlated** with waking up with a headache.
> - *Therefore, sleeping with one's shoes on causes headache.* ❌
>
> The conclusion is wrong. Both events are caused by a third one: **having gone to bed drunk**. Alcohol makes you fall asleep with your shoes on *and* gives you a hangover.

If $A$ and $B$ are correlated, possible explanations include:

| Explanation | Structure | Example |
|---|---|---|
| $A$ causes $B$ | $A \to B$ | Smoking → lung cancer |
| **Reverse causation** | $B \to A$ | Firefighters on site correlate with fire damage; the fire causes both, not the firefighters |
| **Confounder** (common cause) | $C \to A$, $C \to B$ | Drunkenness → shoes on and headache; summer → ice cream sales and drownings |
| **Pure chance** | none | Cheese and bedsheets (Bonferroni) |
| **Selection effect** | the way data were collected creates the link | Only analysing a filtered subpopulation |

Establishing causation requires either **controlled experiments** (randomised trials, A/B tests) or careful **causal inference** methods, not just observational correlations.

#### Generality

Is the population the data refer to **representative of a larger population**? Usually not entirely:

- **We are mostly working on biased samples.** Platform users, customers of one company, patients of one hospital: none is the general population.
- **Information-rich attributes may have been filtered out during data cleaning.**
- **A lot of context is missing.**
- Example: using **social networking platform data to infer trends in society** may be misleading if not done carefully. Platform users differ from society, platform algorithms shape what people see and post, and bots add noise.

---

## Wrapping up

Analysing data requires **a lot of knowledge and critical thinking**:

- **Data are "projections" of often complex processes.** Like a 2D shadow of a 3D object, data capture only some dimensions of reality. Different realities can produce the same data.
- **Part of the context is lost in collection** or is simply unavailable.
- There may be **a wealth of information** in the data, but we need **tools to tell statistically significant patterns from bogus ones**.

The closing cartoon ("Data don't make any sense, we will have to resort to statistics") is a joke with a serious point: **statistics and probability are not optional**, they are what separates insight from illusion.

> [!summary] The big picture of the lecture
> 1. Data come from everywhere, mostly as by-products of other activities.
> 2. Data are "big" relative to your resources and goals (Volume, Velocity, Variety, Veracity).
> 3. This forces new algorithmic approaches: limited memory, one pass, distribution, approximation.
> 4. Typical tasks: retrieval, recommendation, grouping, all based on **similarity**.
> 5. More data ≠ more truth: beware of **sampling bias**, **spurious correlations/multiple testing** (Bonferroni), and **confusing correlation with causation**.

---

## Course outline

### Course philosophy

```mermaid
flowchart LR
    A[Questions / Goals] --> B[Mining tasks]
    B --> C[Techniques]
```

- Start from a **question or goal** (e.g., "which products should we suggest to this user?").
- Translate it into a **mining task** (e.g., "find items similar to those the user liked"; "find users similar to this user").
- Choose/design the **technique** (e.g., Jaccard similarity + MinHash + LSH).

The course focuses on the **techniques** box, but always motivated by the first two: techniques are tools to answer questions, not ends in themselves.

### Prerequisites

- **Calculus** and basic knowledge of **probability theory and statistics** (random variables, expectation, variance, independence, common distributions, basic bounds).
- **Programming**, fundamental **algorithms and data structures** (asymptotic complexity, hashing, sorting, graphs).
- **Some linear algebra** (vectors, matrices, norms, eigenvalues). The instructors cover what is needed, mainly for dimensionality reduction (e.g., SVD, PCA).

### Logistics

- **Mailing list** registration: http://aris.me/registerDM.html
- **Course web page**: http://aris.me
- **Physical attendance** only (no remote attendance).
- **Office hours**: by email appointment.
- **Google Classroom** code: `pzsdkxdd`
- **Books and notes**: see below.
- **Exam**, three components:
  - **Hackathon** (practical implementation on real data);
  - **Written exam**;
  - **Class participation**.

### Topics

- **Similarity measures**: how to quantify how "close" two objects are (sets, vectors, documents, users). Examples: Jaccard similarity, cosine similarity, Euclidean distance, edit distance.
- **Text mining**: representing and analysing text (tokenisation, bag-of-words, TF-IDF, shingling, near-duplicate detection).
- **Clustering**: grouping similar objects without labels (e.g., k-means, hierarchical clustering), including scalable variants.
- **Neighbourhood search**: finding the nearest/similar items efficiently, without all-pairs comparisons (e.g., Locality-Sensitive Hashing). This answers the pairwise-similarity exercise above.
- **Data modelling**: building models that describe or explain the data.
- **The curse of dimensionality and dimensionality reduction**: in high dimensions, intuition breaks (distances concentrate, space becomes mostly "empty"), so we project data to fewer dimensions while preserving structure (e.g., PCA/SVD, random projections).

### What should I study?

- **Take as much as you can from classes.**
- **Main reference**: the book on massive datasets, i.e., *Mining of Massive Datasets* by J. Leskovec, A. Rajaraman, J. D. Ullman (freely available online at mmds.org), plus additional references that expand specific topics or cover topics not in the book.
- **Spend time on the references at home**, trying to understand the key notions.
  - Discuss with friends/colleagues.
  - Ask the instructor.
- **Studying on slides is very poor practice.**
  - Slides **are not** study material.
  - They are necessarily incomplete.
  - Important details are missing.
  - Without the instructor's comments, some claims may even be inaccurate.

> [!tip] Suggested reading for this lecture
> *Mining of Massive Datasets*, **Chapter 1** (Data Mining): definition of data mining, statistical limits on data mining, **Bonferroni's principle** (with the hotel example above), and useful background facts (hash functions, power laws, secondary storage).

---

## Related

- [[Similarity Measures]]
- [[Locality-Sensitive Hashing]]
- [[Bonferroni's Principle]]
- [[Streaming Algorithms]]
