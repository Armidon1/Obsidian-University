
# The Threat Chain (Pathology of Failure)

The "chain of threats" describes the causal relationship between the three main threats to a system:

`[[Faults]]` (Cause) → `[[Errors]]` (State) → `[[Failures]]` (Event)

## The Mechanism
1.  [cite_start]A **Fault** is active when it produces an error; otherwise, it is dormant[cite: 614].
2.  [cite_start]**Activation**: An input is applied to a component that causes a dormant fault to become active[cite: 616].
3.  [cite_start]**Error Propagation**: The error is transformed within the system or propagates to other components[cite: 618].
4.  [cite_start]**Failure**: Occurs when the error reaches the service interface and alters the service[cite: 620].

> [!NOTE] Recursive Nature
> [cite_start]The failure of a component causes a fault in the system that contains that component[cite: 621].