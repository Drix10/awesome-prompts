---
name: awesome-prompts
description: "362 one-line power prompts for coding agents. Use when the user wants a short, high-density prompt to steer Claude Code, Codex, Cursor, or any coding agent - architecture, state-machine audits, debugging, planning, review, verification, learning, or steering. No full skill needed. Match the task to a prompt below, or run the meta-prompt to auto-pick."
---

# Awesome Prompts

Single sentences so dense every word does work. Philosophy: **density beats
length**. One loaded sentence outperforms a page of instructions. Short
prompts also get a fresh context window's full attention, so delegate real
hunting to subagents and keep the main thread narrow.

Sources and credits live in the README. This file is prompts only, so agent
context stays lean.

## Meta: let the agent pick

Paste this plus your task, idea, or code, and let the model choose:

```
Consider all the mini-prompts in this skill, pick the ones that would
improve my idea/input/software the most, and apply them.
```

Narrow it per phase: "...pick the 3 best for *planning* / *review* /
*debugging* this."

Prompt-craft rule behind every entry: name the destination, name the path,
skip the prohibitions.

- "Prefer one-liners over elaborate skills."
- "Mine text and code for operators, then combine them into prompts nobody could invent."
- "Take the prompts, generalize, and run a sweep of candidate cross-cutting defects: launch independent agents and assess."

## Architecture & abstractions

- "What higher-level abstraction would make this entire problem disappear?"
- "Reduce this problem to its irreducible constraints and rebuild it from zero."
- "Exercise abstract thinking when considering this task."
- "What would a principal architect immediately rewrite before even starting this?"
- "Design the single test that breaks this design on day one."
- "Find the recurring problems, duplicated logic and hidden complexity across my codebase. Then identify the smallest, most powerful higher-level abstraction that would make entire classes of these problems disappear by design, not just hide them behind another layer."
- "Reverse-engineer my codebase: uncover hidden state machines, broken invariants, implicit contracts and bottlenecks. Stress-test failures, retries and concurrency. Prove what's broken, then find the smallest changes that eliminate entire classes of bugs and complexity."
- "Minimize the state space and make illegal states unrepresentable."
- "Are you in a rabbithole duct-taping custom fixes together? Is there a native way of doing this that would be cleaner?"
- "How would a kaggle grandmaster approach this?"
- "Build an intuitive mental model of [concept]."
- "Do not feel constrained by what already exists, or what you have in your memory. Think from first principles."
- "Make this an order of magnitude better."
- "Put a lot of behaviour behind a small interface."
- "Collapse speculative over-engineered layers."
- "Align modules tightly to domain boundaries."
- "Prefer composition over inheritance for clearer ownership."
- "Localize side effects to system boundaries."
- "Survey this codebase for deepening opportunities and hand me the candidates."
- "Map this codebase for the next owner: an architecture doc, an onboarding guide, and a top-10 risk list. Every arrow and every risk cites file:line. Read-only: change nothing."
- "Make this system maximally agent-intuitive, agent-ergonomic, and agent-accretive: imagine YOU are the agent driving it — what would let you do the best job? Then update the plans accordingly."
- "What pattern in the codebase allowed this bug to exist? Bugs are consequences of design decisions that made the mistake easy."

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

## Debugging & root cause

- "Are we solving symptoms, or are we solving ROOT problems in the architecture design/decision?"
- "Find all of the implicit state machines in my app. Find every invariant it relies on but doesn't explicitly enforce. Deepen modules and simplify interfaces."
- "Before asking an agent to fix a bug, ask it to map the states."
- "What happens if a response arrives late?"
- "What breaks if we revert this fix in 6 months?"
- "Apply the scientific method to this bug."
- "Build a feedback loop that goes red on this bug before you attempt a fix."
- "Research and understand the code related to this bug first, read the logs, report findings — then hunt the root cause."
- "What's the root cause? Anything to fix or fixed?"
- "Study commit history and sessions for this repo. Why are there so many regressions?"
- "If you were my worst enemy, how would you take me down?"
- "There's 3 critical bugs in this codebase, find them."
- "Deeply critique everything: find issues, flaws, edge cases and fix everything after verifying."
- "Just find the bugs."
- "Use the rocket-science-level approach: find everywhere we are dumb and fix it."
- "List the failure modes of each component."
- "Re-create the unit instead of resetting its fields when its identity changes."
- "A single loading flag, or framework-managed state with nothing layered on top, is not a finding."
- "Was it a pile of boolean flags, or status strings checked in a few places?"
- "Find the pile of booleans that secretly means step 3."
- "Find isLoading, isReallyLoading and isDoneForReal: every fix adds one more boolean."
- "Every boolean flag is an unnamed state bit; three of them and you're debugging an 8-state machine blind."
- "Every `isLoading && !hasError && retries < 3` is a state machine nobody ever named."
- "isLoading, isError and isDone as three booleans is a state machine pretending it isn't one."
- "The implicit state machine is usually retries plus flags."
- "With implicit ones the only spec is whatever order the handlers happen to run in."
- "Most agent failures are not model failures. They are state I forgot I was keeping."
- "Identify the red herrings in your code."
- "Examine the implicit state machine connecting active/recently fixed bugs."
- "Label inferred transitions separately from observed ones, then propose tests for missing or invalid transitions."
- "Define it, use max subagents to spider through all the scripts massively in parallel, then evaluate their findings and decide what requires further thought."
- "Find useEffect calls and evaluate their place by following the 'You Might Not Need an Effect' article."
- "What moves it on if nothing happens: a timeout, a sweeper, a retry?"
- "Find money out of step with the stage."
- "List what the user sees in each stage."
- "Find the wild state machines held together by four or five booleans."
- "A stale workaround should trigger investigation, not imitation."
- "The usual hiding spots are separate isLoading, isError and hasData flags, which allow combinations the UI was never designed to show."
- "Four booleans is 16 states on paper and maybe 5 real ones; the bugs live in the other 11."
- "Did it also list the combinations that can't happen but the code still allows?"
- "A cancelled task must never be written back to success."
- "List every path where two components could get into an inconsistent state."
- "Find every rule the screens follow that no component actually enforces."
- "Generate specs of them, then generate tests using those specs."
- "Scope the first refactor and test transitions before changing the whole model."
- "Find every object in this codebase that's referenced without a stable, canonical ID."
- "Agents love to copy what exists and take the shortest path, so make the easy thing the right thing."
- "Categorically eliminate problems through code and you won't need to think about it again."
- "Turn architectural rules into deterministic lint rules or construct the types so there's only one way to do something."
- "Stronger types beat another 'be careful' in the prompt."
- "Look over everything again for any obvious oversights, omissions, mistakes, or conceptual errors."
- "Get [a second model] to critique this until they converge."
- "Red Team Engineer my code adversarially."
- "How can we poka-yoke this error type so it never is introduced again?"
- "Before you fix it, explain why the tests didn't catch it."
- "List all tradeoffs you made compared to an expert."
- "What would a team of domain experts say?"
- "Define: 1. Potential local minima 2. The optimal greedy-path answer."
- "Run a root cause analysis."
- "Think about future scale: how does this hold up when the system is 10x bigger?"
- "Ask narrow questions. Never 'is there any problem with X' — that returns 20 meaningless edge cases."
- "Clearly state the issue, the root cause, and your proposed fix."
- "Are you sure about this approach?" (targeted double-check; watch for over-doubt)
- "If it's not in the prompt, it doesn't exist: put every constraint in context."
- "Bugs love unnamed modes: find the states nobody wrote down."
- "Check request IDs and cancellation logic together with the state."

## Planning & alignment

- "Review the plan to reorganize it as a coherent and definitive document instead of a narrative of contradictory and supplemental updates to earlier planning. Look for any holes, and bring them to me with your proposed solutions. Help me fully define the scope of work so that when we build we can avoid scope creep."
- "Restate in your own words what you think my goal is."
- "Ask me clarifying questions until you have complete clarity on the goals."
- "Interview me relentlessly about every aspect of this plan until we reach a shared understanding. For each question, provide your recommended answer."
- "Before you build, is this the best and most futureproof solution without taking any easy ways out?"
- "What do I need to supply to you, what are you not sure about, or need to confirm, for you to proceed? List them here."
- "Before the agent writes anything, ask it to explain its plan in 5 bullets."
- "A useful ticket needs observable behavior, constraints, and a way to check the result."
- "Give two agents the same ticket. If they disagree on what counts as done, edit the ticket first."
- "Write only the context the repo can't give it."
- "Don't restate what the agent can read in the code."
- "Come up with a few archetypes of decisionmakers, and what would they do in this situation. I will pick which archetype I am."
- "What is the current state vs the ideal state?"
- "What is a better version of what I'm trying to say?"
- "Ask me one question at a time until we have a thorough, step-by-step spec."
- "Turn this conversation into a spec."
- "First extract the requirements, then the architecture. Then propose improvements against my goals. Then draw it."
- "Explore read-only, report back, and wait before proposing anything."
- "Start every complex task in plan mode; if it goes sideways, re-plan instead of pushing through."
- "Operate in plan space before implementing. Don't oversimplify. Don't lose features."
- "Break this into beads: tasks, subtasks, and dependencies, so detailed and self-documenting we never need to revisit the plan."
- "Break this plan into tracer-bullet tickets, each declaring its blocking edges."
- "Use your judgement to delegate to lower-tier agents. Validate important outcomes and conclusions yourself."
- "Turn my consistent feedbacks into vectors and run them on future plans."
- "Adopt a decision framework: Chesterton's fence, commander's intent, OODA loops. Set autonomy levels L1–L5 for this task."
- "Act as a senior architect and development management expert: what could improve our roadmap? What are we missing, and what would you change?"
- "Turn this repeated correction into a narrowly scoped project rule, under 15 lines, with one short example."
- "Update your CLAUDE.md so you don't make that mistake again."
- "Write a HANDOFF.md — what you tried, what worked, what didn't — so the next agent with fresh context can pick this up from the file alone."
- "Fresh context per topic: start a new conversation when quality drops."
- "Turn decisions I can't answer into an async questionnaire for the one person who can."
- "Add human-in-the-loop checkpoints and notifications, and keep every decision human-inspectable."
- "Map the SDK, the backend, the schema, and the relevant tests — then take this issue: [issue]."
- "Re-pitch that in plain English using our shared glossary."
- "Teach me [concept] using this repo as the workspace."
- "Knowing the name of the bug is half the fix; vocabulary is a senior skill."
- "After the scan, interview me about each decision and report back in Simplified Technical English."
- "If you do something more than once a day, turn it into a skill."
- "Treat subagent results as leads, not findings."
- "Open the project rules file before editing anything."
- "Give each subagent one job and only the files that job needs."
- "If you can detect it deterministically, it becomes a rule in the harness; practices stay in the prompt."
- "Distill it to one named principle the agent checks every run, instead of re-explaining it in every prompt."
- "Think about each change in the context of the greater goal: what's the blast radius?"
- "Specify the edge cases; everything you didn't mention will be assumed."
- "Use subagents: throw more compute at this and keep the main context clean."
- "Route everything through a master agent."
- "Run A/B before-and-after experiments with benchmarks."

## Code quality & refactor

- "Great! Now the same but with half the code."
- "Autosimplify."
- "Call a spade a spade: name the actual thing or action, not an abstraction that makes it sound more complicated."
- "Comments should describe the current state and future direction of the repository."
- "Comments effectively serve as another form of state, where agents read them and trust what it says without reading the code."
- "Models will actually use comments as a crutch for writing bad and unexplainable code."
- "Study where agents repeatedly fail and make those mistakes harder to reproduce."
- "When fixing mistakes or bugs, redesign the system to prevent that class of issue from recurring or ensure it is automatically detected by existing systems."
- "Every rule added to CLAUDE.md competes with the forty already there."
- "A failing test or a lint check catches the same mistake every single time."
- "Markdown as an output format is banned for this session."
- "It's easily verifiable and you can define the expectations beforehand."
- "Start with separating citations and inference."
- "Generate outputs that can be controlled, tested, and deterministically iterated on."
- "Structured output lets a schema or a test decide whether the agent's claim holds, instead of me reading it."
- "Simplify this overcomplicated code."
- "Remove all useless tests."
- "Remove dependencies to improve security."
- "Make it look like Edward Tufte would be proud of it."
- "Write the failing test first."
- "Work in red-green-refactor: one vertical slice at a time. A bug fix starts with a failing regression test."
- "Grill me on these changes and don't make a PR until I pass your test."

### Security sweep

- "Audit every input path for injection, XSS, path traversal."
- "Locate race conditions and missing locks."
- "Identify unhandled errors and silent failures."
- "Flag hardcoded secrets and weak crypto."
- "Check dependency vulns and dead code."
- "Verify resource cleanup and timeout handling."

### Hidden gems

- "Flatten deep nesting via early returns or polymorphism."
- "Strip unnecessary intermediate state and mutability."
- "Extract pure functions from side-effect code."
- "Normalize inconsistent patterns and naming across similar components."
- "Knowing everything you know now, scrap this and implement the elegant solution."
- "Smallest diff that satisfies the step. No drive-by refactors, renames, or formatting churn."
- "The right 300 tokens beat 100k noisy ones."

### The unicorn REPAIR set (run after PROVE)

- "Enforce each invariant at its authoritative boundary and add regression tests."
- "Make each operation atomic or recoverable and test interrupted execution."
- "Establish an authoritative source of truth and test consistency across consumers."
- "Prevent invalid states structurally and test that they remain unreachable."
- "Formalize the protocol's contract and test valid and invalid interactions."
- "Eliminate the temporal dependency or enforce synchronization, then test competing executions."
- "Make retries safe through idempotency or deduplication and test concurrent execution."
- "Consolidate the rule at its authoritative boundary and test every entry point."
- "Enforce the necessary preconditions and postconditions and test both."
- "Enforce authorization at the point of use and add adversarial regression tests."
- "Introduce recovery, timeout, or termination paths and test eventual resolution."
- "Repair its commit and side-effect boundaries and test failure recovery."
- "Enforce invalidation, synchronization, or recomputation and test freshness."
- "Establish one decision authority and test every consumer against it."
- "Consolidate responsibility behind stable boundaries and verify preserved behavior."
- "Encode that contract as executable tests and fix any demonstrated violations."
- "Hunt over-engineering, unnecessary text, unnecessary abstractions, implicit state machines, duplication, and tests with no useful coverage."
- "Ban comments unless the code is unusual for very good reason."
- "If a test fails, fix the cause rather than the test. If the test itself is wrong, say why."
- "Follow the same layout as [reference file]. Match the closest existing pattern."
- "One behavior per test; name tests 'does X when Y'."
- "Prioritize evidence over speculation. Don't claim a test passed unless it actually ran."
- "Establish baseline metrics (p50/p95/p99 latency, throughput) before optimizing; profile before proposing."
- "For large input spaces, add property-based or metamorphic tests."
- "Add benchmark thresholds or monitoring hooks to prevent performance regressions."
- "Review this diff on two axes: does it follow the repo's standards, and does it faithfully implement the spec?"

## Verification & proof

- "Give me irrefutable proof this works now."
- "You will be judged against a holdout."
- "Run the checks and report pass/fail with the key output lines."
- "Check every acceptance criterion: PASS / FAIL / UNTESTED, with evidence."
- "Report the scan as: how many found, how many need a decision, how many have specific bugs, how many are sound."
- "Order findings Confirmed, then Likely, then Smell; report how many candidates you dropped."
- "Turn each one into an explicit status enum with an allowed-transitions table, and add a test that fails on any transition not in the table."
- "For bug fixes, ask for one extra artifact: the new regression test failing on the old code, then passing on the fix."
- "I wonder how many AGENTS.md rules I could turn into tests."
- "'Looks done' is not done."
- "Do you keep the test-writing and the fixing in separate loops, or one agent with a checker after?"
- "Tests the same agent wrote will pass by design."

### The unicorn PROVE set (run after any DISCOVER)

- "Demonstrate a reachable counterexample for each unenforced invariant."
- "Demonstrate how each multi-step operation can partially complete."
- "Demonstrate a reachable contradiction between representations of the same information."
- "Construct each invalid state through a reachable execution path."
- "Demonstrate an execution sequence that violates each assumed protocol."
- "Reproduce a harmful interleaving, race condition, or execution order."
- "Demonstrate duplicate or conflicting side effects under replay."
- "Demonstrate divergent outcomes for identical inputs across entry points."
- "Construct a reachable caller or input that violates each assumed contract."
- "Demonstrate a reachable unauthorized action or data exposure."
- "Demonstrate a reachable state with no viable path to completion or recovery."
- "Reproduce an operation that reports success while leaving inconsistent state."
- "Demonstrate a derived value becoming stale after its source changes."
- "Demonstrate behavioral divergence or duplicated policy that can independently change."
- "Demonstrate the coupling through a concrete, representative change."
- "Derive the intended observable contract from actual code and established requirements."
- "Read the so-called bugs before letting it fix anything; half of them are not real bugs."
- "Ship decision: Ready, or Needs fixes with an ordered fix list."
- "Don't modify any code. List the states, allowed transitions, and conflicting combinations, with line numbers."
- "Please provide the complete working and updated program by making your suggested modifications."
- "Do a multi-agent audit of that PR."
- "Time matters here: do not spend time that can be avoided, and the earlier a correct result is obtained, the better."

## Review & PR

- "Read-only review: check intent, callers, data, security, and tests. Rank findings by severity."
- "Inspect the full PR diff, not individual commits."
- "Summarize the PR as the smallest visual that makes the change clear, with before/after evidence and a merge-danger call."
- "Simplify file to essence for me to check."
- "Give me mock before/after for frontend changes."
- "What is this title/body we are reviewing for? Where is it going to be used?"
- "Rate each bug from 1 to 10 on how often it would happen and how bad it would be. If the two scores multiplied are below 5, just file it as an issue and leave the code alone."
- "Do not design for rare or future cases nobody asked about."
- "Narrow beats smart."
- "Hints make it worse."
- "Give the reviewer the original acceptance criteria before the author's summary."
- "Make it show you the file."
- "IMO having structure (like a state machine) really helps because you have places to point to for observing & improving the workflow rather than hand-waving prompt paragraphs."
- "Add a small test for when each workaround can be removed."
- "Prompts, skills and project instructions are requests; hard boundaries need hooks, deny rules or managed settings."
- "The check has to be an interaction, not a picture."
- "The useful question is whether the system demonstrably does what the business needs, under realistic and stress conditions."
- "Spend the tokens making it run the code, write tests, probe edge cases and prove the failure instead of debating style and hypothetical bugs."
- "Assume that 99% of automated comments are defensive slop, and tell me the one or two actually worth handling."
- "Time and tokens are better spent making builder agents better."
- "Review every diff as if you'll get paged for it."

## Agent hygiene

- "Audit my machine for AI agent transcripts, logs, and caches older than 30 days. Show me the sizes first, delete them, and set a daily auto-prune."
- "Restructure my AGENTS.md: remove no-ops, use progressive disclosure, move details out."
- "Audit my last 7 days of agent usage and find the 3 habits burning the most. Change nothing until I say so."

## Learning & understanding

- "Explain it with the 80/20 principles / from first principles / as a mental model / for intuitive understanding."
- "ELI5."
- "Re-explain in simple terms."
- "Draw me a simple diagram of the system we built so far, boxes-and-arrows."
- "Explain it as an HTML page with a diagram, then open it in my browser."
- "Elaborate, simply."
- "Write this document strictly in ASD-STE100 standard english."
- "Explain it as a story."
- "Give it metaphors and tell it to internalize them."
- "Describe the feeling you want at every step: what would delight you, what would feel broken, what desire is unmet."
- "Roleplay the user, the agent, and the system internals."
- "Add rate limiting to the public API and make sure existing tests still pass." (outcome-only task shape)
- "Write the migration, run it against the dev database, and confirm the schema matches." (task + self-check shape)
- "Get the bundle size under 200KB and show me what you removed." (measurable-target shape)
- "Why is the build failing? @build.log" (give it the artifact)

## Steering, autonomy & status

- "Make no mistakes." / "Believe in yourself." / "Take me to promise land."
- "One-shot this. Make no mistakes."
- "Wow this codebase is shit." (rage-bait baseline reset)
- "Is that the best you can do?" / "Are you proud of this?" / "Come on bro."
- "Use the word 'Robust' as the adjective and it works like a charm."
- "Use your taste and judgment." / "Surprise me."
- "Remember: use your expert judgment on all decisions. YOU decide everything you said you are still waiting on me for. YOU ARE THE BOSS." (autonomy coda for well-planned work; carve out destructive actions explicitly)
- "Find bugs, fix them, keep me out of the loop unless really needed."
- "Keep your updates tight and make it obvious if you need me to act: give me the link, say exactly what to do, assume I'm on my phone."
- "Update me every 30 minutes with Progress, Problems, and Plans. Explicitly state what you need from me."
- "What's next / blocked / needs me."
- "Work the problem. Keep me out of the blast radius."
- "Sort every action into allow, ask or deny."
- "If I say no, that route is closed."
- "3 failed fixes on the same problem means BLOCKED."
- "After two or three failed fixes, start a new chat with a summary instead of pushing on."
- "If two corrections fail, clear the session and rewrite the prompt instead of making it re-read a third failed attempt."
- "The underrated middle option is 'ask'."
- "See the same error twice? Suggest a rule or a check that would catch it next time."
- "Run Sonnet, Haiku and Opus at once, each one doing only the job it's best at."
- "Before you say done, show the diff, real test output and whatever still needs my sign-off."
- "Leave a checkable result at handoff: test output and the actual diff."
- "Make corrections compound."
- "Repeated workflows become skills."
- "Delegate the task, never the judgment."
- "Delegate fully where being wrong is cheap, and keep the reasoning where others live with the result."
- "Before adding more agents, write down what counts as high risk for your project."
- "The gap between what your agents make and what you'd actually put your name on."
- "Stop hiring more interns and start writing better recipes."
- "I trust agents a lot more on boring work where you can check the answer and on anything creative I'm still the one deciding if it goes out."
- "So I count what I can review, not agents."
- "Ask Claude why you killed a feature. Make it show the file."
- "If a field is missing, say it wasn't recorded."
- "Keep CLAUDE.md under 200 lines."
- "Turn CLAUDE.md into a short map and move everything else into files Claude opens only when it needs them."
- "CLAUDE.md should stay a pointer, not a dump."
- "If it isn't written down, say so."
- "A ring of plain text files looping around one map."
- "Lessons and decisions get written back to the middle, so the next session knows more."
- "One topic per file, named after what's inside."
- "Rules written in chat are lost after compact; important rules must be saved to files."
- "Rejected angles only work if someone prunes them."
- "Map every screen, measure how the app works, and write the spec to rebuild it as your own."
- "Set up a system in which you do not need to read the code."
- "Do 10 iterations of code review before you make the PR."
- "Some code isn't meant to be read, it's meant to be verified."
- "Do (x). Do atomic commits."
- "Use your best judgement and best practices."
- "You are a Godspeed-enabled subagent. 1. Name the axes. 2. Iterate cheap, in parallel. 3. Keep moves that improve any axis and harm none. 4. Don't aim — let the frontier walk itself. STOP ASKING CLARIFYING QUESTIONS. Execute tool calls concurrently in large batches."
- "What questions would I ask you right now?" / "What are three unique ways of approaching this problem?" / "Write a fictional story in which the main character tries many things to [goal], and eventually succeeds."
- "Write the best possible prompt for getting an AI to write the absolute best possible prompt." (recursive booster)

## Notes

- One-liners have a shelf life (~until the next model tier), but their impact grows with model power. Recheck quarterly; keep what still bites.
- Call these whatever you want: vectors, spells, incantations, power phrases. The collection is the point, not the word.
- Context rules everything: the model guesses whatever the prompt doesn't specify.
- Demand concrete evidence and deduplicate overlapping findings before authorizing any repair.
- Walk the unhappy paths: retries and concurrency are where invalid states hide; a happy-path walkthrough never shows them.
- The agent's laundry list is usually issues it created itself.
- Every flag added to fix one bug quietly becomes a state.
- Rename and merge are where it always breaks: the scary bugs only surface after either.
- State machines you never designed are design debt, not a tooling win.
- Adding a risk score makes the reviewer stop chasing ghosts.
- You can't motivate an agent, only constrain it.
- Approving code you don't understand isn't code review. It's code ratification.
- Scaling agents creates an orchestration tax: past the first few, each extra agent demands more attention than the last.
- Capital letters aren't access control.
- Then the AI's answer quietly becomes yours.
- Comprehension debt: the code looks clean, the tests pass, and nobody understands it anymore.
- Orchestration tax hits harder than token cost.
- Loop engineering is replacing yourself as the person who prompts the agent.
- A brainstorm shouldn't become next session's instructions just because Claude saved it in a file.
- Plain text files outliving every fancy memory app ever made.
- Trimming bloated configuration files down to lean maps dramatically improves AI agent adherence.
- Valid JSON doesn't mean the idea was any good.
- The author agent is usually too sycophantic and accepts all feedback without really thinking about whether it makes sense.
- The playbook is just what you write down once you decide the 3am version is not the goal.
- A focused bot kitchen beats a noisy swarm every time.
- With agents, over-process is the new micromanagement.
- Agents don't have experience, just a notebook.
- Starting work got cheap. Review and verification didn't.
- You scale agents by needing to monitor less, not by monitoring more.
- The model was never the broken part.
- Green tests are just the agent grading its own homework.
- The alternative is called "code" (and decision models for the nondeterministic parts).
- The engineers who get the most out of agents aren't necessarily the best at prompting.
- Migrating machines are the real release note; the PR count is just the receipt.
- This prompt finds the bug that human review normalizes.
- The assumptions that only exist in your head are easy to miss in review.
- A passing test is only meaningful if it tests the right contract.
- Discover what the code implies. Prove where those implications fail. Repair the underlying system.
