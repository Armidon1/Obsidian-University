Solaris is a **Unix operating system** originally developed by Sun Microsystems in 1992, later acquired by Oracle in 2010 (now called Oracle Solaris).

It's built on top of the original AT&T Unix System V codebase — so it's a "true" Unix, not a Unix-like system the way Linux is.

---

## Why it comes up in hacking/security contexts

It's relevant to your studies mainly for **historical reasons**. A lot of the scanning techniques in Hacking Exposed 7 — FIN scan, NULL scan, Xmas scan, Window scan — were developed and documented specifically because of how **Solaris and older BSD systems** responded differently to malformed packets compared to Windows.

For example:

- The **TCP Window scan** (`-sW`) exploits a quirk in how some Solaris and BSD versions set the Window field in RST packets
- The **Maimon scan** (`-sM`) was named after Uriel Fabian Maimon who discovered that certain **BSD-derived systems** (Solaris included) would drop packets on open ports instead of responding

When you read in Nmap docs _"this scan works on Unix/BSD but not Windows"_ — Solaris is one of the systems being referred to.

---

## What makes it technically different from Linux

||Linux|Solaris|
|---|---|---|
|Kernel origin|Linus Torvalds, 1991|AT&T Unix System V|
|License|GPL (open source)|Partially open (OpenSolaris), now proprietary|
|Filesystem|ext4, btrfs, xfs…|ZFS (Solaris invented it)|
|Package manager|apt, dnf, pacman…|pkg (IPS)|
|Main use case|Everything|Enterprise servers, financial systems|
|TCP/IP stack behavior|Standard|Historically quirky — relevant for scanning|

---

## Is it still relevant today?

Mostly in **legacy enterprise environments** — banks, telecoms, large financial institutions that have been running the same infrastructure since the 90s and never migrated. You're unlikely to encounter it in a modern pentest unless you're targeting that kind of environment.

What _is_ still very relevant today is **ZFS**, the filesystem Solaris invented — it's been ported to Linux and is widely used for storage servers because of its data integrity features.