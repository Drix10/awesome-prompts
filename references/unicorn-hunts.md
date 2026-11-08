## Unicorn hunts (DISCOVER family)

One-line discovery prompts in the seed's image: each finds a class of hidden wrongness. Pair any of them with PROVE ("demonstrate a reachable counterexample") and REPAIR ("fix at the authoritative boundary with regression tests") — and never authorize repairs until the breakage is demonstrated.

- "Find all the implicit transactions in my app."
- "Find every place my app can disagree with itself."
- "Find every impossible state my data model permits."
- "Find all the implicit protocols between components."
- "Find every piece of state or data that has more than one source of truth and could drift out of sync. For each, show where it's written, where it's read, and how they could disagree."
- "Build everything as a state machine."
- "Find everything whose correctness depends on timing or execution order."
- "Find every operation that is unsafe to retry."
- "Find every business rule implemented differently across entry points."
- "Find every contract my code assumes but never verifies."
- "Find every trust boundary crossed without revalidating authority."
- "Find every workflow that can become permanently stuck."
- "Find every successful operation that can leave the system inconsistent."
- "Find every derived value that can outlive its source of truth."
- "Find every business decision implemented in more than one place."
- "Find business rules, validation, and domain concepts implemented in more than one place. Flag where copies have drifted, and name the single source of truth each should come from."
- "Find every change that requires modifying unrelated parts of the app."
- "Find every important behavior that lacks an executable specification."
- "Prove findings against actual code paths before repairing them. Preserve intended behavior, prefer the smallest systemic fix, and reject unverified assumptions."
