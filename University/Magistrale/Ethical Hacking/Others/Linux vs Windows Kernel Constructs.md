# Linux vs Windows Kernel Constructs

A comparison of low-level OS constructs between Linux and Windows, relevant to exploit development and privilege escalation on both platforms.

---

### Virtual Memory & Page Tables

The **page table hardware is identical** on x86-64 — both OSes use the same 4-level paging structure enforced by the CPU. The difference lies in how each kernel tracks virtual memory regions in software.

- **Linux** uses `mm_struct` per process, which contains a linked list/tree of `vm_area_struct` (VMAs) — each VMA describes a contiguous region with permissions, backing file, flags, etc. Inspectable via `/proc/<pid>/maps`.
- **Windows** uses `EPROCESS.VadRoot`, a red-black tree of **VADs** (Virtual Address Descriptors). Inspectable with `VirtualQuery()` or WinDbg's `!vad` command.
- **Allocation:** `mmap()` on Linux maps to `VirtualAlloc()` / `MapViewOfFile()` on Windows. Memory protection changes use `mprotect()` vs `VirtualProtect()`.

---

### Process & Thread Structures

| Linux | Windows |
|---|---|
| `task_struct` (kernel object for both processes and threads) | `EPROCESS` (process) + `ETHREAD` (thread) |
| `fork()` + `exec()` model | `CreateProcess()` only — no true `fork()` |
| PID as primary identifier | PID + opaque **handle** required to operate on a process |
| `/proc/<pid>/` virtual filesystem | `NtQuerySystemInformation()`, handle table |

The **absence of `fork()` in Windows** is architecturally significant. `CreateProcess()` always launches a fresh process from an image on disk. WSL2 emulates `fork()` by running a Linux kernel in a Hyper-V VM — it is not a native Windows primitive.

---

### File Descriptors vs Handles

- **Linux** uses file descriptors — small integers indexing a per-process table. The **VFS (Virtual File System)** layer makes sockets, pipes, devices, and regular files all share the same `read()`/`write()`/`close()` interface. Everything is a file.
- **Windows** uses **handles** — opaque values managed by the kernel's **Object Manager**. A handle can refer to a file, process, thread, mutex, event, registry key, etc. The API is not unified; different object types have different function sets (`ReadFile`, `WaitForSingleObject`, `RegQueryValue`...).

Both have per-process handle/descriptor tables, and both leak security-sensitive information if handles are inherited incorrectly by child processes.

---

### System Calls

| Linux | Windows |
|---|---|
| `syscall` instruction directly into the kernel | `syscall` → `ntdll.dll` stubs → `NtXxx` kernel functions |
| **Stable, documented ABI** | **Unstable ABI** — syscall numbers change between OS versions |
| `strace` for tracing | API Monitor, ETW, WinDbg for tracing |

This distinction is critical for exploit and malware development on Windows. Because Microsoft provides no guarantee of stability for raw syscall numbers, code is expected to call through `ntdll.dll`. EDR products hook `ntdll.dll` to intercept calls — which is why advanced techniques use **direct syscalls** or **indirect syscalls** (calling into the kernel directly, bypassing `ntdll` hooks).

---

### Memory Protections

Both OSes sit on the same hardware mitigations, but differ in how they expose and enforce them:

| Mitigation | Linux | Windows |
|---|---|---|
| Non-executable pages | NX bit (page table entry) | **DEP** (Data Execution Prevention) |
| Address randomization | ASLR via `/proc/sys/kernel/randomize_va_space` | ASLR, configurable per-module via `DYNAMICBASE` PE flag |
| Stack protection | Stack canaries (GCC `-fstack-protector`) | Stack cookies (`/GS` MSVC flag) |
| Position-independent code | PIE (`-fPIE`) | `DYNAMICBASE` + `HIGHENTROPYVA` in PE header |

On Windows, ASLR entropy depends on whether the module was compiled with `DYNAMICBASE`. Many legacy DLLs are still compiled without it, making them useful as ROP gadget sources at predictable addresses — a classic technique.

---

### Signals vs SEH / APCs

- **Linux signals** (`SIGKILL`, `SIGSEGV`, `SIGTERM`...) are asynchronous notifications delivered to a process, handled via `signal()` / `sigaction()`.
- **Windows Structured Exception Handling (SEH)** is a stack-based mechanism where exception handler records are chained on the stack. Overwriting an SEH record was a classic Windows exploit primitive (now mitigated by **SafeSEH** and **SEHOP**).
- **APCs (Asynchronous Procedure Calls)** are a Windows-specific construct with no Linux equivalent — a function queued to execute in the context of a specific thread when it enters an alertable wait state. Used legitimately for I/O completion, and abused for **APC injection** in process injection techniques.

---

### Key Takeaway for Exploit Development

The **CPU hardware is the same** — x86-64 rings, page tables, MSRs, and hardware mitigations are shared. This means the *concepts* of exploitation (stack overflows, heap corruption, ROP chains, use-after-free) transfer between platforms.

What differs is everything on top: the kernel objects, the syscall interface, the binary format (ELF vs PE), the runtime libraries (`libc` vs `ntdll`/`msvcrt`), and the mitigation implementations. Windows exploit development is treated as a separate discipline, with *Windows Internals* (Russinovich et al.) as the standard reference.
