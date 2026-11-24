last lesson [[17 CS Lower Level - Secure Shell (SSH)]]
# Shamir's Secret Sharing

Course of Cybersecurity — Prof. Fabrizio d'Amore. See the map: [[MOC - Cybersecurity]].

How can a secret be split among several people so that **only a large enough subset**, acting together, can recover it — and any smaller subset learns *nothing*? This is **secret sharing**, and Shamir's scheme solves it with [[Perfect Cipher|information-theoretic]] security.

## Sharing a secret

Assume a **secret** $S$ is given (a password, code, PIN, passphrase, any string).

- **Goal**: share $S$ with $n$ subjects by consigning some data (a **fragment**) to each of them, so that
  - none of them alone knows $S$;
  - they can reconstruct $S$ **only** by "joining" the fragments they hold.
- **Applications**: boards of directors, nuclear-weapon control, system shutdown sequences, joint bank accounts, consensus protocols — any case where **all (or enough) authorised members must agree** to act.
- It can be **easily implemented** in an **information-theoretically secure** mode: it cannot be broken even if the adversary has **infinite computing power** (same notion of security as the [[One-Time Pad (OTP)]]).

---
## The simple case: sharing $S$ with all $n$ subjects (XOR scheme)

When **every** one of the $n$ subjects is required to reconstruct $S$ (an *n-out-of-n* scheme), a single [[Nonce|random]] XOR split is enough. Assume $S$ is an unsigned integer (a bit sequence) and $n \ge 2$.

**Algorithm** (uses the XOR operation `^`):
- randomly generate $n-1$ fragments (nonces) $s_1, \dots, s_{n-1}$;
- set $s_n = S \oplus s_1 \oplus s_2 \oplus \dots \oplus s_{n-1}$;

so that
$$S = s_1 \oplus s_2 \oplus \dots \oplus s_n .$$

- $S$ is reconstructed by XORing **all** $n$ fragments.
- If an attacker knows only $n' < n$ fragments, they **cannot** reconstruct $S$ (not enough information).
- Knowing $n' < n$ fragments gives **no more information** than knowing a single fragment → **information-theoretically secure** (exactly the key-reuse-free guarantee of the [[One-Time Pad (OTP)]]: each missing fragment acts as a one-time pad over $S$).

> [!note] Limitation
> This XOR scheme is *all-or-nothing*: you need **all** $n$ fragments. The general Shamir scheme relaxes this to **any $k$ out of $n$**.

---
## Shamir Secret Sharing (SSS): the threshold scheme

> Shamir, *"How to share a secret"*, Communications of the ACM **22**(11), 612–613 (1979).

A **$(k, n)$ threshold scheme**, with $1 < k \le n$: given a secret $S$, find $n$ data fragments $s_1, s_2, \dots, s_n$ such that

- given **any** $m \ge k$ fragments it is possible to reconstruct $S$;
- $m < k$ fragments are **not sufficient** to reconstruct $S$;
- a reconstruction attempt from $k-1$ fragments is **not easier** than one from a single fragment.

**Requirement**: information-theoretically secure.

The case $k = n$ is exactly the XOR scheme above. The interesting case is $k < n$, solved with polynomials.

---
## Ingredients for the general case

Two mathematical tools:

- **modular arithmetic** and **finite fields** (see [[Galois Field]]);
- **polynomial interpolation**.

Polynomial interpolation rests on the **unisolvence theorem**:

> [!important] Unisolvence theorem
> Given $r > 1$ points of $\mathbb{R}^2$ (with distinct abscissae), there exists a **unique** polynomial of degree $r-1$ going exactly through the $r$ points.
>
> The theorem also holds for polynomials defined over **Galois fields**.

The idea of SSS: hide $S$ as the value at $x=0$ of a secret polynomial of degree $k-1$. Since $k$ points uniquely determine such a polynomial (and $k-1$ points leave it completely undetermined), exactly $k$ fragments are needed.

---
## Generation of the fragments

- let $p$ be a **prime** with $p > S$ and $p > n$ (we work in the field $\mathbb{Z}_p$);
- randomly choose $k-1$ integers in $[0, p)$: $a_1, a_2, \dots, a_{k-1}$, and let $a_0 = S$;
- consider the polynomial
$$P(x) = a_{k-1}x^{k-1} + a_{k-2}x^{k-2} + \dots + a_1 x + a_0 \pmod{p};$$
- let $s_i = P(i)$, for $i = 1, 2, \dots, n$.

By construction $P(0) = a_0 = S$: **the secret is the value of the polynomial at $0$**.

After discarding $P(x)$ and $S$, only the $n$ points $(i, s_i)$ are kept — one per subject.

![[SSS-interpolating-polynomial.png]]

The figure shows the idea: the $n$ fragments are **points** $(1,s_1), (2,s_2), \dots, (7,s_7)$ lying on the secret polynomial. The **abscissae** $1, 2, \dots, n$ are known (public); the secret $S = P(0)$ is the value where the curve crosses the $y$-axis. (For simplicity a polynomial over the real plane is drawn; in practice it lives over $\mathbb{Z}_p$.)

---
## Reconstructing $S$

Given **$k$** fragments $s_{i_1}, s_{i_2}, \dots, s_{i_k}$, find the degree-$(k-1)$ polynomial going through the points $(i_1, s_{i_1}), \dots, (i_k, s_{i_k})$. The standard tool is **Lagrange interpolation**.

Given $k+1$ data points $(x_0, y_0), \dots, (x_k, y_k)$ with distinct $x_j$, the interpolation polynomial in **Lagrange form** is
$$L(x) := \sum_{j=0}^{k} y_j\, \ell_j(x), \qquad \ell_j(x) := \prod_{\substack{0 \le m \le k \\ m \ne j}} \frac{x - x_m}{x_j - x_m}.$$

Then the secret is recovered as
$$S = L(0).$$

> [!tip] Why $k-1$ fragments reveal nothing
> With only $k-1$ points, **every** value of $S = P(0)$ is still possible: for each candidate secret there is exactly one degree-$(k-1)$ polynomial through the $k-1$ points *and* that candidate. So $k-1$ fragments leave $S$ uniformly undetermined — information-theoretic security, just like the OTP.

---
## Properties of SSS

- the size of fragments and of the secret are upper-bounded by the size of $p$ ($|s_i|, |S| < |p|$);
- if $k$ is kept fixed, fragments can be **dynamically added or deleted** without affecting the other fragments (just evaluate $P$ at new abscissae);
- it is straightforward to **generate a fresh set** of fragments: randomly build a new polynomial with the same $a_0 = S$;
- members can be given **higher weight** by assigning them **more than one** fragment.

---
## Introducing a third party

![[SSS-third-party.png]]

One can reserve some **unknown abscissae** (points not handed to the subjects) and give them to a **trusted third party** (see [[Trusted Third Party (TTP)]]) for additional services. The subjects hold $(x_1, s_1), \dots$; the third party holds extra points on the same polynomial.

### Third party: extra services

- **gives evidence of reconstruction** and identifies the contributors (the *crystal safe-box* metaphor: everyone can see the result formed, and by whom);
- can **recognise possible cheaters** — if it stores the **hashes** of the fragments (see [[Hashing]]), a tampered fragment is detected;
- maintains **at least the same security** as the traditional approach;
- if the third party is **compromised**, it still **does not reveal** the secret (it only holds extra points, not $S$ itself).

---
This is the final topic of the Lower Level module. Back to the map: [[MOC - Cybersecurity]].
