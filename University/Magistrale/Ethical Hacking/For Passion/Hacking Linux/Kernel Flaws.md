# Kernel Flaws

> [!abstract] In una riga Il kernel non _rispetta_ il modello di sicurezza: lo **è**. Un bug userspace viola le regole; un bug nel kernel riscrive chi le fa rispettare. È la classe di privilege escalation più grave su UNIX — sopra non c'è (quasi) niente che ti possa fermare.

## 1. Perché è la classe più grave

Tutte le altre note di questo capitolo — [[suid_binaries]], [[Symlink Attacks]], [[race_conditions_signals]], [[shared_library_hijacking]] — descrivono attacchi che restano **dentro** il modello di sicurezza del kernel. Sfrutti un programma root, ottieni root, ma il kernel continua a fare il suo lavoro: file permission, namespace, LSM, syscall filtering sono ancora in piedi.

Un kernel flaw è un'altra cosa. Il kernel è il **TCB** (Trusted Computing Base): il codice che _definisce e applica_ l'honor delle permission, la transizione di privilegio dei SUID, la gestione dei signal, l'isolamento dei processi. Gira in **ring 0**. Quando un bug ti dà esecuzione o scrittura arbitraria in ring 0:

- Non "ottieni root" — sei **sopra** il concetto di root. Modifichi direttamente la `cred` struct di qualsiasi processo.
- Ogni mitigazione **userspace** salta. SELinux/AppArmor sono moduli del kernel: codice in ring 0 li disabilita. seccomp idem. La sandbox di Chrome, l'isolamento di un container — tutto poggia sul kernel; se il kernel cade, cadono tutti.
- Puoi **escapare container e namespace**: il confine di un container è una finzione mantenuta dal kernel.
- Puoi installare un **rootkit** a livello kernel, invisibile da userspace.

> [!warning] Il punto d'esame _"Perché un kernel bug è peggio di un bug in un SUID?"_ → Un exploit SUID ti dà root **dentro** le regole del kernel. Un kernel exploit ti mette **dove le regole vengono scritte**. Le difese userspace (LSM, seccomp, container) sono inutili contro un bug in ring 0 perché stanno _sopra_ il livello compromesso.

## 2. Filo conduttore — la attack surface del kernel

Il pattern guida del capitolo: _processo privilegiato + parsing complesso di input untrusted + nessuna autenticazione = bug factory garantita_. Il kernel è la **forma estrema** di questo pattern. È il processo più privilegiato che esista, e ogni **syscall, ioctl, scrittura su `/proc` o `/sys`, pacchetto di rete, filesystem montato** è input untrusted fornito da userspace senza alcuna autenticazione — perché chiamare una syscall non _richiede_ autenticazione, è il meccanismo base del sistema.

Superfici principali oggi:

- **syscall** e relativi argomenti
- **`/proc` e `/sys`** — interfacce pseudo-filesystem (è qui che vive il bug HE7)
- **`ioctl` sui device driver** — storicamente il far west: tanti driver, poco audit
- **network stack** — netfilter/nf_tables, raggiungibile anche da remoto
- **eBPF** — il _verifier_ è codice complesso che valida bytecode untrusted: bug factory moderna
- **io_uring** — sottosistema nuovo, performante, pieno di LPE negli ultimi anni
- **filesystem parser** — montare un'immagine FS malevola (overlayfs & co.)
- **namespace** — `CONFIG_USER_NS` ha esposto a utenti non privilegiati codice prima root-only

## 3. Il caso HE7 — CVE-2012-0056 / mempodipper

HE7 cita un solo caso: la vulnerabilità 2012 in `mem_write()`, kernel Linux ≥ 2.6.39. Vale la pena srotolarla perché il libro salta il meccanismo.

**Setup.** `/proc/<pid>/mem` è un'interfaccia che mappa la memoria virtuale di un processo come fosse un file: `lseek` a un indirizzo, `read`/`write`. Storicamente la **scrittura** era disabilitata da un `#ifdef`. In 2.6.39 quell'`#ifdef` è stato rimosso: gli sviluppatori ritenevano che i controlli di permesso in `mem_open()` fossero solidi abbastanza da reggere anche la scrittura.

**Il bug.** Il controllo di permesso veniva fatto al momento dell'`open()`, legato allo stato/credenziali del processo _in quel momento_. Ma il file descriptor così ottenuto **sopravvive a una `execve()`**. Se in mezzo si esegue un binario **SUID**, le credenziali e l'address space cambiano — il processo diventa root — ma il vecchio fd verso la memoria resta valido e ora la "use" avviene in un contesto privilegiato che il "check" iniziale non aveva previsto.

> [!note] Questo è un check/use gap Mempodipper è concettualmente un cugino del `[[toctou]]`: il **check** del permesso e l'**uso** del fd avvengono in due stati di privilegio diversi, e in mezzo c'è una `execve()` di un SUID. È un controllo legato all'`open` invece che all'operazione — esattamente l'errore del pattern TOCTOU applicato alla transizione di privilegio dei `[[suid_binaries]]`.

**L'exploit (zx2c4).** Ricostruendo l'output di HE7:

1. Il processo fa `fork`. Il **figlio** apre `/proc/<pid_padre>/mem` (il padre è _ancora_ non privilegiato → il check passa) e ottiene un fd scrivibile verso la memoria del padre.
2. Il figlio passa quel fd al padre via `SCM_RIGHTS` (le righe _"Sending fd 3"_ / _"Received fd at 5"_).
3. Il padre risolve l'offset di `exit@plt` dentro l'eseguibile `su`, fa `lseek` del fd-memoria a quell'offset e lo assegna a `stderr` (_"Assigning fd 5 to stderr"_).
4. Il padre fa `execve("/bin/su")`. `su` è SUID root: la `execve` cambia credenziali e address space. Il fd-memoria, aperto prima, **dovrebbe** diventare invalido — il bug è che resta scrivibile e ora punta alla memoria di un processo **root**.
5. `su`, in esecuzione, stampa un messaggio d'errore su `stderr` — che è il fd-memoria seekato su `exit@plt`. Il contenuto del messaggio (influenzato dall'attaccante) viene scritto **sopra `exit@plt`**: è lo shellcode.
6. `su` chiama `exit()` → salta nello shellcode → shell di root.

**Insight.** Non c'è memory corruption, non c'è overflow. È un **bug di logica**: una permission check insufficiente. Eppure l'impatto è identico a un overflow in ring 0 — privilege escalation completa da utente locale. È il motivo per cui i kernel _logic bug_ sono insidiosi quanto i _memory bug_.

## 4. Tassonomia dei kernel bug

|Classe|Cosa va storto|Esempio|
|---|---|---|
|**Logic / permission bug**|check mancante o insufficiente|CVE-2012-0056 mempodipper|
|**Race condition**|finestra TOCTOU _dentro_ il kernel|Dirty COW, Dirty Pipe|
|**Memory corruption**|overflow stack/heap, OOB write in driver/net|CVE-2021-22555 (netfilter)|
|**Use-after-free**|refcount bug, oggetto liberato e riusato|CVE-2016-0728 (keyring), bug nf_tables|
|**Type confusion**|oggetto interpretato come tipo sbagliato|vari bug eBPF / io_uring|
|**Uninitialized memory**|struct/flag non inizializzata|Dirty Pipe|
|**Integer issues**|overflow/signedness nei size|vedi `[[integer_overflow_attacks]]`|
|**Infoleak**|il kernel rivela indirizzi → sconfigge KASLR|dmesg, `/proc` senza `kptr_restrict`|

Sono le stesse classi delle note userspace (`[[integer_overflow_attacks]]`, `[[dangling_pointers]]`, `[[race_conditions_signals]]`) — solo che qui il bersaglio è ring 0.

## 5. Hall of fame — kernel Linux LPE

|CVE / nome|Anno|Classe|Effetto|
|---|---|---|---|
|**CVE-2012-0056** mempodipper|2012|logic / permission|scrittura `/proc/pid/mem` → privesc (caso HE7)|
|**CVE-2016-0728**|2016|refcount UAF|overflow refcount nel keyring → privesc|
|**CVE-2016-5195** Dirty COW|2016|race COW|scrittura su mapping read-only → overwrite file root|
|**CVE-2021-22555**|2021|heap OOB|netfilter `x_tables`, reso famoso da Google kCTF|
|**CVE-2022-0847** Dirty Pipe|2022|uninit flag|overwrite di file read-only via page cache|
|**nf_tables UAF** (varie)|2022–24|UAF|sottosistema netfilter, vettore LPE dominante recente|

Collegamenti:

- **Dirty COW** è una `[[race_conditions_signals|race condition]]` nel sottosistema di memoria: si corre il COW fault contro `madvise(MADV_DONTNEED)`. Permette di scrivere file su cui hai solo permesso di lettura — es. sovrascrivere un `[[suid_binaries|binario SUID]]` o `/etc/passwd`.
- **Dirty Pipe** ottiene un effetto simile (overwrite di file read-only) ma in modo più affidabile, sfruttando un flag non inizializzato nei pipe buffer. Entrambi mostrano come un kernel bug "buchi" il file permission model **dal basso**.

## 6. Pattern di exploitation moderno

Su Linux, una volta ottenuta scrittura o controllo del flusso in ring 0, la primitiva di privesc canonica è:

```c
commit_creds(prepare_kernel_cred(NULL));
```

`prepare_kernel_cred(NULL)` costruisce una `cred` struct con uid/gid 0 e full capabilities; `commit_creds` la applica al processo corrente. Poi si ritorna in userspace e si fa `execve` di una shell — che ora è root. In alternativa si sovrascrive direttamente la `cred` struct del processo, azzerando uid/gid.

Un exploit moderno però deve prima sconfiggere le mitigazioni (vedi §7): serve un **infoleak** per battere KASLR, e ROP/JOP _dentro_ il kernel oppure attacchi _data-only_ perché **SMEP/SMAP** impediscono il classico **ret2usr** (puntare il flusso del kernel a shellcode in userspace).

## 7. Countermeasures

HE7 dice solo _"patcha subito"_. Vero ma datato. Quadro moderno:

|Difesa|Cosa fa|
|---|---|
|**Patching + live patching** (kpatch, livepatch, kGraft)|applica fix di sicurezza al kernel **senza reboot**|
|**KASLR**|randomizza la base del kernel → serve un infoleak per exploitare|
|**SMEP / SMAP**|il kernel non può **eseguire** (SMEP) né **leggere/scrivere** (SMAP) pagine userspace → uccide `ret2usr`|
|**KPTI**|isola le page table kernel/user (mitigazione Meltdown)|
|**seccomp-bpf**|restringe le syscall che un processo può chiamare → **riduce la attack surface** verso il kernel. Arma #1 di sandbox e container|
|**LSM** (SELinux/AppArmor)|confinamento — _ma_ un bug in ring 0 li disabilita: utili contro l'**accesso** al bug, non contro il bug già sfruttato|
|**Restrizione unprivileged user namespaces**|`CONFIG_USER_NS` ha esposto codice kernel a utenti non-root; molti LPE lo richiedono. Ubuntu/Debian ora lo restringono (`kernel.unprivileged_userns_clone=0`, profili AppArmor)|
|**Hardening infoleak**|`kptr_restrict`, `dmesg_restrict`, `perf_event_paranoid` → negano gli indirizzi che servono a battere KASLR|
|**Config hardening (KSPP)**|`STRICT_KERNEL_RWX`, structleak, randstruct, lockdown mode|
|**grsecurity/PaX**|storica suite di hardening (oggi commerciale)|

> [!tip] La gerarchia che conta Contro un kernel flaw, le difese **userspace** (LSM, seccomp, namespace) riducono solo la _probabilità di raggiungere_ il bug. Una volta che il bug è in esecuzione in ring 0, sono aggirabili. Le uniche difese che mordono _l'exploitation_ sono quelle **dentro o sotto** il kernel: SMEP/SMAP, KASLR, KPTI, config hardening — e, sotto tutto, l'**hypervisor**, che sposta il TCB un livello più in basso.

## 8. Stato moderno

- Il kernel LPE è oggi l'anello finale di quasi ogni **exploit chain** seria: sandbox escape del browser → kernel LPE; container escape → kernel LPE. Da solo un kernel bug locale vale poco senza un punto d'appoggio, ma è ciò che trasforma un "code exec da utente" in _game over_.
- Google **kCTF** e il bug bounty Linux hanno reso i kernel bug molto remunerativi e spostato la ricerca sui sottosistemi caldi: **netfilter/nf_tables, eBPF, io_uring, overlayfs**.
- Il caso HE7 del 2012 è vecchio ma la _morale_ regge: un sottosistema (`/proc/pid/mem`) era considerato "sicuro abbastanza" da rimuovere una protezione difensiva preesistente — la classica hubris che precede i kernel bug.

## Collegamenti

- `[[suid_binaries]]` — mempodipper sfrutta proprio la transizione di privilegio `execve` + SUID; e un kernel bug rende ogni protezione SUID irrilevante
- `[[toctou]]` — mempodipper è un check/use gap; Dirty COW / Dirty Pipe sono race _dentro_ il kernel
- `[[race_conditions_signals]]` — Dirty COW come race condition di sottosistema
- `[[dangling_pointers]]` — gli UAF kernel (keyring, nf_tables) sono la stessa classe portata in ring 0
- `[[integer_overflow_attacks]]` — overflow/signedness nei size sono frequenti nei driver


---

# Interesting Claude reasoning

```bash
The student explicitly asked for an Obsidian note, so I need to create one as a markdown file that can be saved to disk and linked within their vault.

Now I'm thinking through what should go into this kernel flaws note based on the student's exam level and study needs.

The HE7 section needs more depth than just the mempodipper example — I should structure this like the other notes in the handoff: starting with the conceptual foundation (why kernel bugs are the most critical class of vulnerability), then the mechanism (how they bypass protections), historical CVEs with actual attack vectors, and modern mitigations. I'll include Linux sysadmin analogies since that's his background, wiki-links to related notes, and code examples where they illustrate the attack pattern.

The kernel attack surface is massive — syscalls, /proc, /sys, ioctl, device drivers, filesystem parsers, network stack, namespaces, eBPF — and most modern LPE exploits target obscure drivers or subsystems rather than the main kernel. For CVE-2012-0056 specifically, the vulnerability was in /proc/<pid>/mem: the permission check happened at open time but didn't bind the file descriptor to the original process, so you could open another process's memory and write to it even after your privileges changed, completely bypassing the intended access controls. ento di `write()`/`exec`. mempodipper di zx2c4: sfrutta il fatto di aprire /proc/self/mem, fare exec di un SUID (su), e poiché il fd di mem rimane aperto attraverso l'exec, ora punta alla memoria di un processo privilegiato (su gira come root). Poi scrive shellcode in exit@plt di su. Quando su chiama exit(), esegue lo shellcode come root.

Actually let me get the mechanism right. CVE-2012-0056: the check in mem_write was insufficient. The original ifdef CONFIG_... blocked writes entirely. When removed, the permission model relied on `__check_mem_permission` / `mem_open`. The flaw: the permission check happened at open time against the current process, but after opening /proc/self/mem, the process can exec a setuid binary — the fd stays valid even though credentials change, giving write access to the privileged process's memory. The exploit uses fd passing to redirect stderr to the mem fd, so when su writes error output, it overwrites exit@plt with shellcode that executes as root.

Now I need to organize the taxonomy of kernel bugs for exam purposes — categorizing by type like memory corruption, logic/permission bugs, race conditions, integer issues, uninitialized memory, and reference counting bugs.

Then I should build a reference collection of notable Linux kernel CVEs that students find useful: mempodipper, Dirty COW with its race condition in copy-on-write memory, Dirty Pipe exploiting uninitialized pipe buffer flags, keyring UAF, eBPF verifier vulnerabilities, Netfilter heap overflow, and recent overlayfs/nf_tables exploits.

Finally, I want to connect this back to why kernel bugs are fundamentally more dangerous than SUID vulnerabilities.

Now I'm explaining the escalation path: a kernel exploit gives you ring 0 access where you can modify credential structures, disable security modules like SELinux or AppArmor, break out of containers and namespaces, or hide rootkits entirely. The typical pattern chains arbitrary write primitives into credential structure overwrites for privilege escalation.

Then I need to cover modern mitigations beyond just patching—kernel live patching tools like kpatch and livepatch that let you apply fixes without rebooting.

Looking at the defensive mechanisms: ASLR randomizes memory layouts, SMEP and SMAP prevent the kernel from executing or reading user memory which kills classic return-to-user attacks, KPTI patches Meltdown, and lockdown mode restricts kernel capabilities. LSMs like SELinux and AppArmor enforce mandatory access control, while seccomp-bpf filters syscalls to reduce the attack surface from userspace and containers. User namespaces are double-edged—they enable sandboxing but have introduced significant LPE vectors, so many distributions now restrict unprivileged namespace creation. Additional hardening includes strict kernel memory execution policies, structure leak detection, and KASAN for memory safety.

Historically grsecurity and PaX provided strong protections, and now hypervisor-based isolation removes the kernel from the trusted computing base entirely. Modern kernel exploitation has become the critical link in exploit chains—escaping Chrome sandboxes or containers requires kernel LPE, making these bugs highly valuable in bug bounty programs like kCTF. Most vulnerabilities cluster in specific subsystems: netfilter, io_uring, eBPF, nf_tables, and overlayfs. The exam's Q5 format typically presents C code to analyze for vulnerabilities, but kernel flaws require a different approach than straightforward code review.

I should map the key vulnerability patterns—SUID binaries, race conditions with signals, TOCTOU bugs, use-after-free from dangling pointers, integer overflows, and shared library hijacking—and note that Dirty COW exemplifies the race condition class. The unifying thread across all these is the pattern of "privileged service plus complex parsing plus missing authentication equals vulnerability factory," and the kernel is the ultimate privileged service where every syscall and ioctl represents untrusted input from userspace.

Now I'm structuring this as a proper Obsidian study note in Italian with headers, tables, and code examples where useful, since the student explicitly requested a markdown note file rather than a chat explanation. Continuing with the structure of the note — I'm outlining the key sections on kernel vulnerabilities, starting with why they're the most critical privilege escalation vector, then moving through the attack surface, a taxonomy of kernel bugs, specific CVE examples like mempodipper, exploitation patterns, and modern countermeasures.

For mempodipper specifically, the vulnerability in CVE-2012-0056 exploits the `/proc/<pid>/mem` interface which allows reading and writing process memory — write access was historically disabled, but in kernel 2.6.39 developers removed the guard code believing permission checks were sufficient, when in fact they weren't properly validating access.

Now I'm adding the current state of kernel security and linking back to related topics like SUID binaries. permission check (`ptrace_may_access` / `__check_mem_permission`) was performed, but there was a window/logic gap. Specifically, the check tied the open fd to the credentials/process state at open time, but the fd could survive an `execve()` of a setuid binary. After exec, the process gains root credentials, and the previously-opened mem fd (or a fd pointing at the now-privileged process) can be used to write into privileged memory.

zx2c4's mempodipper exploits this by opening `/proc/self/mem` before executing su, then using fork and fd-passing to keep that fd alive across the privilege boundary. It dup2's the fd onto stderr and seeks it to the `exit@plt` offset, then triggers su to write an error message to stderr—which is actually the mem fd. By controlling the error message content through argv and locale settings, the attacker crafts it as shellcode that gets written directly over `exit@plt`. When su calls exit(), it jumps to the shellcode and spawns a root shell. The core vulnerability is that the permission check was bound to open time rather than to the privilege transition at execve—a classic TOCTOU race condition.

This connects beautifully to both TOCTOU and SUID binary vulnerabilities: mempodipper is itself a check/use gap where the check happens at one privilege state and the use at another. I'll highlight that transversal synthesis.

Now looking at Dirty COW (CVE-2016-5195): a race condition in the kernel's copy-on-write handling that lets an unprivileged user write to read-only memory mappings—like a root-owned file mapped read-only—by racing the COW fault with `madvise(MADV_DONTNEED)`. This gives write access to files you shouldn't be able to modify.

Dirty Pipe (CVE-2022-0847) achieves a similar effect more reliably: an uninitialized flag in the pipe buffer struct allows overwriting the page cache of read-only files, including SUID binaries, without the complexity of Dirty COW's race condition.

Then there's CVE-2016-0728, a refcount overflow leading to use-after-free in the keyring subsystem, and CVE-2021-22555, a heap out-of-bounds write in netfilter that gained notoriety from Google's kCTF.

More recent vulnerabilities cluster around nf_tables UAF bugs, io_uring issues, and overlayfs problems—I'll focus on the subsystem patterns rather than cataloging every CVE. The classic exploitation flow involves gaining an arbitrary write or control flow hijack to call the credential-setting function that grants root privileges, then returning to userspace to spawn a shell, though modern kernels require defeating KASLR, SMEP, SMAP, and KPTI. SMEP specifically prevents kernel execution of userspace pages, which blocks the traditional ret2usr technique where the kernel jumps into user-controlled code.

SMAP blocks kernel reads and writes to userspace memory without explicit CPU instructions, pushing attackers toward kernel ROP/JOP chains and data-only attacks instead. seccomp restricts which syscalls a process can invoke, shrinking the attack surface significantly in containerized environments. Unprivileged user namespaces were a major expansion of the attack surface—they let non-root users access kernel code paths previously restricted to root, like netfilter setup, though many distributions now disable this capability by default.

Now I'm compiling the main kernel hardening mitigations: patching and live patching to avoid reboots, KASLR to randomize the kernel's memory layout, SMEP/SMAP to prevent ret2usr attacks, KPTI to isolate against Meltdown, LSM frameworks like SELinux and AppArmor for confinement (though a ring-0 bug can still bypass them), seccomp-bpf to reduce syscall surface, restrictions on unprivileged namespaces, and kernel parameters like dmesg_restrict and kptr_restrict to limit information leaks.

Adding more mitigations like perf_event_paranoid, lockdown mode, strict kernel RWX enforcement, KSPP hardened configs, and historical approaches like grsecurity and PaX. The critical insight here is that userspace defenses become irrelevant against kernel vulnerabilities—SELinux can be disabled by ring-0 code, which is why kernel bugs represent the worst class of security threat. I'm going to write this up as a proper note in Italian with a peer-level tone, using Obsidian formatting, tables, and wiki-links throughout.

Writing kernel_flaws.md... o capitolo — `[[suid_binaries]]`, `[[symlink_attacks]]`, `[[race_conditions_signals]]`, `[[shared_library_hijacking]]` — descrivono attacchi che restano **dentro** il modello di sicurezza del kernel. Sfrutti un programma root, ottieni root, ma il kernel continua a fare il suo lavoro: file permission, namespace, LSM, syscall filtering sono ancora in piedi.

Un kernel flaw è un'altra cosa. Il kernel è il **TCB** (Trusted Computing Base): il codice che _definisce e applica_ le permission, la transizione di privilegio dei SUID, la gestione dei signal, l'isolamento dei processi. Gira in **ring 0**. Quando un bug ti dà esecuzione o scrittura arbitraria in ring 0, non stai semplicemente ottenendo root — sei **sopra** il concetto stesso di root, modificando direttamente le strutture di credenziale di qualsiasi processo. Ogni mitigazione userspace crolla: SELinux, AppArmor, seccomp, le sandbox di Chrome, l'isolamento dei container — tutto poggia sul kernel, e se il kernel cade, cadono tutti. Puoi escapare container e namespace perché il confine che li definisce è stato compromesso.

Il punto d'esame è questo: un exploit SUID ti dà root _dentro_ le regole del kernel. Un kernel exploit ti mette _dove le regole vengono scritte_. Le difese userspace sono inutili contro un bug in ring 0 perché stanno sopra il livello compromesso.

Ora sto tracciando il filo conduttore del capitolo: il pattern ricorrente è un processo privilegiato che parsa input non fidato senza autenticazione — una ricetta per i bug.

Il kernel è l'incarnazione estrema di questo pattern: è il processo più privilegiato che esista, e ogni syscall, accesso a /proc e /sys, ioctl su device driver, pacchetto di rete e filesystem montato rappresenta input non autenticato da userspace. Oggi le superfici d'attacco principali sono le syscall stesse, le interfacce pseudo-filesystem, e gli ioctl sui driver — storicamente il territorio più selvaggio.

Ma il panorama si è allargato: il network stack è raggiungibile anche da remoto, eBPF ha introdotto un verifier complesso che valida bytecode non affidabile, io_uring è un sottosistema nuovo e performante ma pieno di vulnerabilità di privilege escalation, i parser dei filesystem possono essere sfruttati montando immagini malevole, e CONFIG_USER_NS ha esposto a utenti non privilegiati codice che prima era accessibile solo a root.

Tornando al caso concreto di HE7: la vulnerabilità del 2012 in `mem_write()` vale la pena analizzarla perché il libro salta i dettagli. L'interfaccia `/proc/<pid>/mem` mappa la memoria virtuale di un processo come un file, permettendo `lseek` e `read`/`write`. Fino a 2.6.39 la scrittura era disabilitata, ma quando è stata abilitata gli sviluppatori hanno confidato che i controlli di permesso in `mem_open()` fossero sufficienti — il bug era che il controllo veniva fatto solo al momento dell'apertura, non durante la scrittura.

Il problema emerge quando il file descriptor sopravvive a un'`execve()`: se il processo che ha aperto il fd esegue un binario SUID come `su`, le credenziali cambiano e il processo diventa root, ma il vecchio fd verso la memoria rimane valido e ora opera in un contesto privilegiato che il controllo iniziale non aveva previsto. È un classico check/use gap, simile a un TOCTOU, dove il check del permesso e l'uso effettivo sono separati nel tempo.

L'exploit di zx2c4 sfrutta questo: un processo figlio mantiene un file descriptor verso la memoria del padre (tramite passaggio via `SCM_RIGHTS`), il padre esegue `execve("/bin/su")` diventando root, e il figlio ora ha accesso in scrittura a una memoria che prima era protetta.

Il figlio ridirige stderr del processo `su` verso questo fd, lo posiziona sull'indirizzo di `exit@plt`, e forza `su` a scrivere un messaggio d'errore — il cui contenuto diventa shellcode che sovrascrive il puntatore di exit. Quando `su` chiama `exit()`, esegue lo shellcode e ottiene una shell root.

Non c'è corruzione di memoria o overflow — è puro sfruttamento della finestra di privilegio tra l'`open` e l'operazione.

Adesso sto guardando come categorizzare questi bug: la tabella mostra che questo rientra nei logic bug, dove il kernel ha una permission check insufficiente, ma l'impatto è identico a un memory corruption in ring 0. Ecco perché i logic bug del kernel sono altrettanto pericolosi quanto i memory bug.

Generating taxonomy table... Generating markdown table...

Both Dirty COW and Dirty Pipe exploit kernel bugs to bypass file permission models—one through a race condition in memory management, the other through an uninitialized flag in pipe buffers, both allowing writes to read-only files like SUID binaries or system files. On Linux, the canonical privilege escalation primitive after gaining kernel-level write or control flow access is a function call that constructs a kernel credential structure and commits it to the current process. isce una `cred` struct con uid/gid 0 e full capabilities; `commit_creds` la applica al processo corrente. Poi si ritorna in userspace ed `execve` di una shell — che ora è root. In alternativa si sovrascrive direttamente la `cred` struct del processo (azzerando uid/gid).

Un exploit moderno però deve prima sconfiggere le mitigazioni (vedi §7): serve un **infoleak** per battere KASLR, e ROP/JOP _dentro_ il kernel oppure attacchi data-only perché **SMEP/SMAP** impediscono il classico _ret2usr_ (puntare il flusso del kernel a shellcode in userspace).

Ora sto guardando le difese moderne: il patching live (kpatch, livepatch) applica fix senza reboot, KASLR randomizza la base del kernel rendendo necessario un infoleak, SMEP e SMAP bloccano l'esecuzione e l'accesso alla memoria userspace dal kernel, e KPTI isola le page table tra kernel e user.

Poi ci sono seccomp-bpf che restringe le syscall disponibili, LSM come SELinux e AppArmor che confinano i processi (anche se un bug in ring 0 può disabilitarli), e la restrizione degli unprivileged user namespaces che Ubuntu e Debian ora applicano per ridurre la superficie d'attacco verso il kernel.

Per quanto riguarda l'hardening vero e proprio, ci sono tecniche come kptr_restrict e dmesg_restrict che nascondono gli indirizzi kernel necessari per aggirare KASLR, insieme alle configurazioni KSPP come STRICT_KERNEL_RWX e randstruct. Storicamente c'è stata anche grsecurity/PaX, una suite completa di hardening che oggi è commerciale.

Il punto cruciale è che tutte queste difese userspace — LSM, seccomp, namespace — riducono solo la probabilità di raggiungere il bug, ma una volta che il bug è in esecuzione in ring 0, possono essere aggirate.

Le difese che contano davvero sono quelle dentro il kernel stesso: SMEP, SMAP, KASLR, KPTI, e l'hardening della configurazione. E ancora più in basso c'è l'hypervisor, che sposta l'intero TCB a un livello inferiore.

Oggi il kernel LPE è diventato l'ultimo anello di quasi ogni exploit chain seria — che sia un sandbox escape del browser o un container escape, tutto converge verso il kernel. Un bug locale da solo vale poco, ma è quello che trasforma un'esecuzione di codice da utente in una compromissione totale. Google con kCTF e i bug bounty Linux hanno reso questi problemi ancora più visibili.

I sottosistemi che attirano più attenzione adesso sono netfilter/nf_tables, eBPF, io_uring e overlayfs. Il caso HE7 del 2012 è emblematico: un sottosistema considerato "abbastanza sicuro" ha portato a rimuovere una protezione difensiva, la solita arroganza che precede i kernel bug.

Questi exploit si collegano a pattern più ampi — mempodipper sfrutta la transizione di privilegio durante execve con SUID, un kernel bug rende ogni SUID irrilevante. È anche un classico check/use gap, come Dirty COW e Dirty Pipe che sono race condition nel kernel. Gli UAF kernel in keyring e nf_tables appartengono alla stessa classe di vulnerabilità in ring 0, e gli overflow di signedness nei driver sono frequenti. The core issue is that the permission check happened at open time against the current process, but the file descriptor remained valid after execve into a setuid binary—so the actual write operation occurred with elevated privileges that the original check never anticipated. I'll stick with that conceptual accuracy rather than getting bogged down in the exact implementation details.

Now I'm seeing the actual attack sequence more clearly: the child process opens the parent's memory file, not its own. The parent forks, then execs into su to become root, while the child opens /proc/<parent_pid>/mem. The ptrace_may_access check should have blocked a non-root process from accessing root's memory, but the flaw in that check allowed it through. Then the child passes the file descriptor back to the parent via fd passing, giving the now-privileged parent write access to its own memory. 5 to stderr, then reads the su binary to locate the exit@plt function, resolves its address to 0x402178, seeks to the right offset, and finally executes su with shellcode injected as arguments. The parent orchestrates this whole sequence after setting up the file descriptor redirection.

The key vulnerability is that when the parent forks, the child can open the parent's /proc/pid/mem while the parent is still unprivileged—this is allowed. The child passes this file descriptor back to the parent via SCM_RIGHTS. Then the parent execs into setuid su, and crucially, the file descriptor remains valid across the exec because it was opened before the privilege escalation. This means the parent can now write directly into su's memory space through that fd, bypassing the post-patch check that would invalidate the fd after execve changes the memory map. I see the key insight now — the exploit code runs before execve, not after. The parent sets up stderr to point to the memfd at the exit@plt offset, then execve's su, which then writes its error message directly to that memory location as shellcode. Let me trace through the corrected sequence: parent forks, child opens /proc to get a writable fd to parent's memory, parent assigns this fd as stderr and seeks to the target offset, then execve's su which writes error output into that prepared location. figlio passa quel fd al padre via `SCM_RIGHTS`. 3. Il padre risolve l'offset di `exit@plt` dentro l'eseguibile `su`, fa `lseek` del fd-memoria a quell'offset, e lo assegna a `stderr`. 4. Il padre fa `execve("/bin/su", ...)`. `su` è SUID root: la `execve` cambia le credenziali e l'address space. Il fd-memoria, aperto prima, **dovrebbe** diventare invalido — il bug è che resta scrivibile e ora punta alla memoria di un processo root. 5. Quando `su` stampa un messaggio d'errore su `stderr` — che è il fd-memoria seekato su `exit@plt` — il contenuto controllato dall'attaccante sovrascrive `exit@plt` con lo shellcode. 6. `su` chiama `exit()`, salta nello shellcode, e ottiene una shell di root.

Sto anche verificando i dettagli tecnici: l'offset di seek (0x40216c) differisce leggermente dall'indirizzo risolto (0x402178) — probabilmente per via del mapping tra offset di file e indirizzi virtuali o della struttura della PLT — ma non è rilevante per la nota.

Ora devo controllare la grafia e assicurarmi che il tono della risposta in chat sia breve e in prosa, senza over-formatting. Poi creerò il file markdown con la documentazione completa.

Nessuna skill disponibile è pertinente per una nota markdown semplice, quindi procedo direttamente con la creazione. Aggiungerò un breve preambolo in chat che sottolinei come i kernel flaws chiudono il capitolo 5 e che il prossimo argomento naturale è suid_binaries.

Sto per scrivere la nota finale, rifinendo l'italiano e assicurandomi che la descrizione di Dirty Pipe sia precisa e concisa.
```