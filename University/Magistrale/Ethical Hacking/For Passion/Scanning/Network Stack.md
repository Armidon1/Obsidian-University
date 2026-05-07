# What is a TCP/IP Stack / Network Stack / IP stack

Every operating system needs to implement the TCP/IP protocols to communicate over a network. That implementation — the actual code inside the kernel that handles sending/receiving packets, managing connections, responding to flags, calculating timeouts — is called the **TCP/IP stack** (or network stack, or IP stack).

It's called a "stack" because it mirrors the **layered model** of network protocols:

```
Application layer    (HTTP, FTP, SSH…)
Transport layer      (TCP, UDP)          ← where most fingerprinting happens
Network layer        (IP, ICMP)
Data link layer      (Ethernet, WiFi)
```

Each OS has its **own implementation** of this stack, written independently by different teams over decades.

---

## Why implementations differ

The TCP/IP standard is defined in RFCs — but RFCs leave many behaviors **unspecified or ambiguous**. When the standard says _"if you receive an unexpected packet, you SHOULD respond with RST"_, different OS developers made different choices about:

- Default TTL values in IP packets
- Initial window size in TCP headers
- How to handle malformed or ambiguous packets
- Whether to respond to certain ICMP messages
- How to set the IP ID field
- Timestamp behavior
- How quickly to retransmit
- Whether to send RST or just drop unexpected packets

Nobody coordinated these decisions — every OS team just made their own call.

---

## Why this enables fingerprinting

Because these implementation differences are **consistent and measurable**. If you send the same weird packet to Linux, Windows, Solaris and FreeBSD, you get four subtly different responses — and those differences are stable across versions and machines.

Nmap's OS detection (`-O`) exploits exactly this. It sends a **battery of carefully crafted probes** and compares the responses against a database of known stack behaviors:

```
Probe 1 — SYN to open port
  → measures: initial window size, TTL, TCP options order

Probe 2 — SYN to closed port
  → measures: RST behavior, window size in RST

Probe 3 — FIN+PSH+URG to open port (Xmas-like)
  → measures: does it respond? how?

Probe 4 — TCP packet with bogus options
  → measures: how does the stack handle unknown options?

Probe 5 — ICMP echo request with unusual fields
  → measures: how does the stack echo back the fields?

... (Nmap sends ~16 probes total)
```

Each probe reveals something about the stack's personality. Combined, they produce a **fingerprint** that Nmap matches against its `nmap-os-db` database.

---

## Concrete examples of stack differences

|Behavior|Linux|Windows|Solaris|
|---|---|---|---|
|Default TTL|64|128|255|
|Initial TCP window size|29200|65535|65535|
|Response to FIN on open port|Silence|RST|Silence|
|IP ID field|Incremental or random|Incremental|Incremental|
|ICMP error quoting|Full original header|Partial|Varies|

TTL alone is often enough for a rough guess — if you see TTL=128 in a packet, it almost certainly left a Windows machine. TTL=64 suggests Linux. TTL=255 suggests Solaris or a network device.

---

## The connection to what you've already studied

This is why the FIN/NULL/Xmas scans **don't work on Windows** — it's not a rule, it's a consequence of how Microsoft implemented their TCP/IP stack. Their stack responds with RST to malformed packets on open ports, while the Linux/BSD stacks silently drop them as per RFC 793.

That behavioral difference is simultaneously:

- What **breaks** those scan techniques against Windows
- What allows Nmap to **identify** Windows vs Linux via `-O`

Same underlying cause, two different security implications.