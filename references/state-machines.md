## State-machine audit kit

- "Find all of the implicit state machines in my app."
- "Then ask it to write the transition table for each one and mark the transitions that are impossible but still reachable in the code."
- "Ask where two of those machines touch the same data. That's almost always where the race lives."
- "Which of these explain the bugs I've been calling flaky?"
- "Produce a concrete event sequence for each state it finds — distinguish states the code permits from states a user can actually reach."
- "Cite the handlers and conditions behind each transition, and mark proposed changes separately."
- "The loop owns retries; the harness just caps them."
- "Prompt isn't the bug. Own tools and retries in the harness."
- "I stopped rewriting the prompt and started rewriting the rule for done."
- "How do you tell whether the issue is the harness or the feedback loop when the tests pass but the task isn't done?"
- "Green tests and an open issue means the agent followed the done rule it was given. Change that rule."
- "If every test passed and the issue is still open, fix the harness or the loop first, not the prompt."
- "Does the new test fail on the commit before the change?"
- "What is the piece of text to copy-paste to your agent? That's the programming paradigm now."
- "Rewriting the prompt for a loop problem is the classic mistake."
- "Passing tests only means it did what you asked. The bug was something nobody asked about."
- "Ask the agent to visualize the state flow."
- "Ask for their correctness to be verified in Quint."
- "Find all of the implicit state machines in the build and assess whether they are worth fixing. Use subagents. If this search is valuable, propose the best way to build it into future reviews and workflows."
- "Frame out every element of the feature that uses state and document and plan it in advance, before writing code."
- "Hand the state file to a model checker. Try every order of transitions and give the shortest path to each invalid state."
- "A failing regression test is the useful boundary between a suspected bug and a fix."
- "Add to the global rules: never create implicit state machines; make state explicit when you write code."

### Expanded audits (paste-ready)

- "Find the app's explicit and implicit state machines and document their states, invariants, and transition tables in one file. Identify invalid states or transitions the code can actually reach, with evidence, including through retries and concurrency. Prioritize confirmed bugs by impact, group related fixes into issues, then fix them with regression tests and keep the document updated."
- "Find all implicit state machines in both repositories and address every one relevant and feasible at the project's current stage by eliminating unnecessary state, deriving values instead of synchronizing duplicate flags, and refactoring necessary stateful behaviour into discrete, explicit state machines with clearly defined states, permitted transitions, and enforced invariants; update affected callers and verify intended behaviour with regression tests and integration checks."
- Full phased audit (discovery → verification with concrete code refs and repro scenarios → remediation plan with no code changes until approved → implement with regression tests and update the doc; evidence over speculation throughout): https://pastebin.com/dznHsaQR
- Full deep-audit expansion: "You are analyzing this codebase to find all **implicit state machines** — behavior controlled by distinct modes/states that are NOT declared as an explicit state machine, statechart, reducer, or similar, instead emerging from booleans, enums, nullable values, flags, and conditional logic. 1. Thoroughly search the entire codebase (use parallel subagents). 2. Identify every meaningful implicit state machine. 3. For each: the real states, how transitions happen, which state combinations are possible but shouldn't be, where the state lives, ranked by risk/complexity/likelihood of bugs. Output: Part 1 — summary list (title, one-sentence description, risk High/Med/Low, 2–5 key files). Part 2 — detailed report for the high-risk ones (effective states, transition logic, illegal combinations, code snippets, whether it's worth making explicit). Be precise; don't flag trivial booleans."

### The 9 follow-ups: run the base prompt, then run these

- "Find every place where the screen can show something false."
- "Find every bit of business logic sitting in UI components that belongs in the domain layer."
- "Find every place a value is stored twice and can drift apart."
- "Find every database rule the code assumes but Postgres doesn't enforce." (then add check, unique, or foreign-key constraints)
- "Find every async action that can run twice or race."
- "Find every error that gets swallowed silently."
- "Find every magic number and hard-coded copy that should be a token or live in config."
- "Find every place where a type is looser than the data."
- "Find every effect that could be an event handler or derived value."

### Variants (same family, different lens)

- "Find every invariant my application relies on but does not enforce."
- "Find all the implicit invariants in my app."
- "Find all non terminal states in my state machine as a service."
- "Try the explicit inversion: find all of the *explicit* state machines."
- "For each one, list: the states, how it moves between them, any impossible or conflicting combinations, and the risk level. Rank by risk. Don't change any code yet."
- "Make this permanent in AGENTS.md."
- "Study and find all of the implicit state machines in this codebase."
- "Find the hidden machines disagreeing about what 'done' means."
- "What did the refactor replace the implicit machine with: an explicit enum of states or a reducer?"
- "Don't put the rule where compaction will summarize it away; use a type that rejects the fourth flag."
- "Model implicit state machines with typestate."
- "Make every long-running thing an explicit state machine."
- "Pivot to explicit state machines with explicit translation logging."
- "Refactor them into explicit lifecycle enums and type-state transfers."
- "Let's pretend it's not OOP."
- "Be thorough in your analysis and bold in your recommendations."
- "Convert them to actors. Then add a rules-file line: no new implicit ones."
- "Find all of the implicit state machines in my database and convert them to actors."
- "Make all implicit state machines explicit, tested, and documented."
- "Find all tautologies."
- "Find all non-terminal states in my state machine as a service."
- "Find all the implicit obligations in this contract."
- "Find the dumb requirements." (most expensive bugs are requirements bugs, not code bugs)
- "Pushing determinism down." (push side effects and nondeterminism to the edges)
- "Show me (A) if we're doing things wrong, and (B) if we're doing the wrong things."
- "Document them in a living HTML file; keep it open and updated until every one is explicit or gone."
- "Synchronize state enumeration across the app so it doesn't keep 10 copies of the same strings."
- "Make sure every communications interface pair shares the same timeout contract on both sides."
- "Check cross-interface settings: they go hyper-local, which is why state transitions get spread out."
