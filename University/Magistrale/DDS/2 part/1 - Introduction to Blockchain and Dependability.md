Previous lesson [[0 - Trust Matters - Introduction to Trust in Distributed Systems]]
# 1. Blockchain Introduction - Foundations & Architecture

**Tags:** #blockchain #distributed_systems #cryptography #ethereum #smart_contracts #web3

**IMPORTANTE:** integrare con le slides perché queste slides sono troppo poco descrittive e certe cose non sono state trascritte 

Block chain is a datastructure well defined and interesting, but the protocol depends on which is the provider (aetereum,  bitcoin, etc). we can image a chain of blocks, which ieach block is  a specific transaction.  
## 1\. The Evolution of Trust and Value

first ione is blockchain of transaction ( the most succesful one), finally more recentrly the idea of application.

To understand Blockchain, we must first understand the problem it solves: **Trust** in the transfer of value.

![[Pasted image 20260924121544.png]]
### From Centralized to Distributed

Historically, society has evolved from barter to gold, and finally to fiat and digital money . In the current digital era, we rely heavily on the **Client/Server** model.

* **The Black Box (Traditional Banking):** We trust a central bank to manage a private ledger. We send a request, and we trust the bank to update balances correctly. We cannot verify the internal process.
* **The White Box (Blockchain):** We replace the central authority with **Algorithms**. Trust is shifted from individuals/institutions to a distributed protocol and code .

### A transaction: the exchange (or agreement for an exchange) of an asset
those details will be clear later, but the important thing is that everything is puiblic and verifieable. we are transferign a digital asset from source to destination. in the immage is the case of a bitcoin. The abstraction is the righr part of the image, but the important thing is "when" 

![[Pasted image 20251129170753.png]]


![[Pasted image 20260924122112.png]]
if the transaction is face to face, no problem. but if the traansaction is not anymore face to face (me in itally and the destination in india), well i have to do something. Obiusly in 5000B.C we had barter, but it was too heavy to barter a fucking cow, then we decided ti use metal coin, then money etc... Then we have electronic money, which are pretty cool but the problen is that we have to trust on a third party, namelly "banks". But why we are now interested in blockchain? rememebre the [[0 - Trust Matters - Introduction to Trust in Distributed Systems]] which says that we have to trust on banks, which we cannot have a formal proof, but a legal proof. Basically, up to the green rectangular in the image we have the clietn server design, where we have only a legal trust.

![[Pasted image 20260924123751.png]]![[Pasted image 20260924123758.png]]

we are moving trust from the individuals, to the **collectivities.** the problem is:
- if we are a **fixed amount of participants** (10,12,13), it's **easy**
- but if we are possibly unnlimited, we have to do something.
### Network Topologies

Understanding the network structure is crucial for engineering distributed systems. Paul Baran defined three specific topologies:

![[Pasted image 20251129164938.png]]

> [!abstract] Visual Analysis
> **What to look at:** The three diagrams labeled (A), (B), and (C).
> **Meaning:**
>
> * **Centralized:** All nodes connect to a single center. Single point of failure.
> * **Decentralized:** Multiple hubs/centers. More resilient, but still relies on hubs.
> * **Distributed:** A mesh where every node is connected to neighbors. No central authority. **Blockchain operates here.**

In term of trust, centralized and decentralized doesn't change a lot. when we consider the distributed one, we are moving trust from them to the community, but the problem is that there can be malicious nodes, and we have to deal to them.

![[Pasted image 20260924124128.png]]

-----

## 2\. The Core Problem: The Ledger & Consensus
to reach [[Consensus]], we need protocols (not algorithms, notice the differences). 

How do we maintain a ledger (a list of transactions) without a central bank?

### The Double Spending Problem

In a digital world, assets are files. Files can be copied. If I have 1 coin, I shouldn't be able to send it to Alice *and* Bob simultaneously.

* **In Centralized Systems:** The Bank checks the database order. Easy.
* **In Distributed Systems:** It is **DIFFICULT**. We need a way for all nodes to agree on the **order of events** without a master clock.

### Defining Consensus

[[Consensus]] is not just about validating that a transaction is valid (e.g., "Do you have enough money?"). It is about **Ordering**.

* **Validation:** Checks if a transaction adheres to protocol rules (e.g., valid signature, sufficient balance).
* **Consensus:** Determines the specific **ordering** of events to prevent double-spending and selects which block is added next.

**The Rule of the Longest Chain:**
If two incompatible events occur (a fork), the protocol typically follows a rule where the first recorded event (or the one in the longest chain/most accumulated work) is considered the truth.

-----

## Trasaction
![[Pasted image 20260924125528.png]]
![[Pasted image 20260924125538.png]]
![[Pasted image 20260924125548.png]]This book is the proof that the transaction ahppened and it is coherent with the protocol. So this is how thing should change:![[Pasted image 20260924125638.png]]
so basically you see how thing change, and we have to consider the problems of moving from centralized to distributed. The ldeger keeps track of everything, but keeping the ledger sinchronized and consistent, is a new thing. ![[Pasted image 20260924125953.png]]
so dealing with the ledger in a centralized system is easy, in distributed it is not.
## 3\. Blockchain Definition & Taxonomy
![[Pasted image 20260924130100.png]]
A Blockchain is defined as a **[[Distributed Ledger (DLT)]]** that records transactions in an **immutable, verifiable, and permanent way** . 

Read it many times. immutability and verifiability: we deal with it with [[Digital Signature]]! tipically, ifin the client-server paradigm the server implements also the signature, then we have the same properties, but nowadays serevr do not do that ([[HTTPS]] doesn't do that). 

consensus: permissionless is beautifull because everybody can participate, while permissioned is the the opposite: which is shitty because we are killing the trust.  So we will talk about decentralization, security and scalability. 

### Types of Blockchain

Not all Blockchains are Bitcoin. We classify them based on **Read/Write permissions**:
- Permissioned: Only approved participants can participate: makes sense only if the participants DO NOT GROUP TOGETHER a makes decisions together.
- Permissionless: Anyone ca participate. Wonderfull. We are going to focus only on this one becasue is way more sophisticated.

But who can see the blockcain?:
- Public: everyone can **see** the transactions
- private: Only the ones who are permissioned can see transactions

> [!tip] Decision Matrix
> Use the flowchart in Slide 48 to decide if you need a blockchain.
>
> * Do you need to store state? $\rightarrow$ Yes.
> * Are there multiple writers? $\rightarrow$ Yes.
> * Can you use an always online Trusted Third Party (TTP)? $\rightarrow$ **NO** (This is the key trigger for Blockchain).

-----

## 4\. Technology Stack (Layer 1)

A blockchain is not a single technology, but a combination of six existing computer science concepts :

1. **[[Peer-To-Peer (P2P)]] Communication Protocols:** For broadcasting data.
2. **[[Asymmetric Encryption]] (PKI):** Digital signatures for identity and authorization.
3. **[[Hashing|Hash Functions]]:** For immutability and linking blocks.
4. **[[Merkle Trees]]:** For efficient data verification.
5. **Key-Value database**: to create our own database from a blockchain, to increase [[Performance]].
6. **[[Consensus]]**: For each transaction, it requires everyone consensus to add a block.

### Key Properties

* **Immutable:** Once validated, records cannot be changed.
* **Burn Concept:** You cannot "delete" data. To "burn" an asset, you send it to an address with no known private key (e.g., `BurnBurn...`), making it unspendable, but the record remains.
* **Censorship Resistant:** No central authority can block a valid transaction.

-----

## 5\. Ethereum: The World Computer

While Bitcoin is a calculator (Transaction $\rightarrow$ Payment), [[Ethereum]] is a computer (Transaction $\rightarrow$ Code Execution).

### The State Transition Function

Ethereum treats the blockchain as a State Machine.
**The mathematical definition provided is:**

$$
\text{State}' = \Upsilon(\text{State}, \text{Transaction})
$$

> [!abstract] Math Analysis
> \* **State:** The current status of all accounts (balances, storage, code).
> \* **Transaction:** The input (data + signature + value).
> \* **$\Upsilon$ (Upsilon):** The State Transition Function (EVM execution) that processes the transaction and updates the state.

![[Pasted image 20251130131001.png]]
### Smart Contracts

[[Smart Contracts]] are immutable programs deployed on the blockchain. They execute logic autonomously.

**Here is the exact implementation shown in the slides (Solidity):**

```javascript
pragma solidity >=0.7.0 <0.9.0;

/**
* @title Storage
* @dev Store & retrieve value in a variable
*/
contract Storage {

	uint256 number;

	/**
	* @dev Store value in variable
	* @param num value to store
	*/
	function store(uint256 num) public {
		number = num;
	}

	/**
	* @dev Return value
	* @return value of 'number'
	*/
	function retrieve() public view returns (uint256){
		return number;
	}
}
```

> [!abstract] Code Analysis
> This is a basic "Getter/Setter" contract.
>
> * `uint256 number;` defines the **State** variable stored on the blockchain.
> * `store` is a function that changes the state (requires a transaction + gas).
> * `retrieve` is a `view` function (read-only, usually free).

-----

## 6\. The Oracle Problem

Blockchains are **deterministic** and isolated systems. They cannot natively make API calls to the internet (e.g., "What is the weather?" or "What is the price of Apple stock?").

* **The Problem:** If nodes fetched data from a URL, the data might change between requests, breaking consensus.
* **The Solution (Oracles):** Middleware that fetches off-chain data and injects it into the blockchain as a transaction, allowing the network to agree on the value deterministically.

-----

## 7\. Web 2.0 vs. Web 3.0 Architecture

This distinction is vital for engineering modern DApps (Decentralized Applications).

![[Pasted image 20251130131546.png]]

> [!abstract] Visual Analysis
> **Web 2.0:**
>
> * Front-end $\rightarrow$ Backend Server (Node/Python) $\rightarrow$ Centralized Database.
> * *Failure point:* If the server/DB goes down, the app dies.
>
> **Web 3.0:**
>
> * Front-end $\rightarrow$ **Provider (JSON RPC)** $\rightarrow$ **Blockchain Network (EVM)**.
> \* *Storage:* Often uses [[IPFS]]/[[Swarm]] (decentralized storage) instead of AWS S3.
> \* *Identity:* Handled by a "Signer" (e.g., MetaMask), not a username/password database.

-----
