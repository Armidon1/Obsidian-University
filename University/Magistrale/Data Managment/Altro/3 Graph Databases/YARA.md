---
title: YARA
tags:
  - data-management
  - concept
  - malware-analysis
  - cybersecurity
---

# YARA

> [!summary] In short
> Pattern-matching language and tool for identifying and classifying malware: a rule combines text, hex and **regular-expression** strings with a boolean condition.

```yara
rule Suspicious_Downloader {
  strings:
    $url = /https?:\/\/[a-z0-9.-]+\/[a-z]{6}\.exe/
    $api = "URLDownloadToFileA"
  condition:
    uint16(0) == 0x5A4D and all of them
}
```

- `strings`: text, hex (with wildcards) and regex patterns; `condition`: boolean formula over them.
- Mentioned in [[Regular Expressions]] as a practical use of regex in malware hunting.

## Links

- **Related concepts**: [[Regular Expressions]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[03 - DM - Graph Databases - RDF, SPARQL e Knowledge Graphs#Espressioni regolari sui cammini|Lecture 3 — Espressioni regolari sui cammini]]
