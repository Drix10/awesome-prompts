---
name: god-tier-mini-prompts
description: One-line power prompts for coding agents. Use when the user wants a short, high-density prompt to steer Claude Code, Codex, Cursor, or any coding agent — for architecture, debugging, review, planning, learning, or verification — instead of a full skill. Invoke by matching the task to a prompt below, or run the meta-prompt to auto-pick.
---

# God-Tier Mini Prompts

A wide collection of single-sentence power prompts for coding agents —
each one dense enough that every verb, noun, and adjective does work.
Philosophy: **density beats length** — one loaded sentence outperforms a page
of instructions. Short prompts also get a fresh context window's full
attention ("attention budget" — delegate real hunting to subagents).

Collected from across X/Twitter, Prompt Snacks, Notchbird's Banger Prompts,
and engineering blogs. Author handles kept as credit.

## Meta-prompt: let the agent pick

Paste this plus your task/idea/code, and let the model choose:

```
Consider all the mini-prompts in this skill, pick the ones that would
improve my idea/input/software the most, and apply them.
```

Narrow it per phase: "...pick the 3 best for *planning* / *review* /
*debugging* this."

## Architecture & design

- "Find all of the implicit state machines in my app." — @steveruizok (full
  expanded audit version below)
- "What higher-level abstraction would make this entire problem disappear?" —
  @Wyrmfalls
- "Find the recurring problems, duplicated logic and hidden complexity across
  my codebase. Then identify the smallest, most powerful higher-level
  abstraction that would make entire classes of these problems disappear by
  design, not just hide them behind another layer." — @Dyikhyi56
- "Reverse-engineer my codebase: uncover hidden state machines, broken
  invariants, implicit contracts and bottlenecks. Stress-test failures,
  retries and concurrency. Prove what's broken, then find the smallest changes
  that eliminate entire classes of bugs and complexity." — @Dyikhyi56
- "Minimize the state space and make illegal states unrepresentable." — @dkubb
- "Reduce this problem to its irreducible constraints and rebuild it from
  zero." — @Wyrmfalls
- "Exercise abstract thinking when considering this task." — @Wyrmfalls
- "What would a principal architect immediately rewrite before even starting
  this?" — @Wyrmfalls
- "Design the single test that breaks this design on day one." — @Wyrmfalls
- "Are you in a rabbithole duct-taping custom fixes together? Is there a
  native way of doing this that would be cleaner?" — @merterdir
- "How would a kaggle grandmaster approach this" — @jmKoudsi
- "Build an intuitive mental model of [concept]." — @mergesignal
- "Do not feel constrained by what already exists, or what you have in your
  memory. Think from first principles." — @dimitribosch via Prompt Snacks
- "Make this an order of magnitude better." — @petekp via Prompt Snacks

## Debugging & review

- "If you were my worst enemy, how would you take me down?" — @woodchipdaddy
  (adversarial review of your own design/code)
- "There's 3 critical bugs in this codebase, find them." — @observatii
  (forces the agent to actually hunt instead of skimming)
- "Deeply critique everything: find issues, flaws, edge cases and fix
  everything after verifying." — @DrishtantGhosh (one-prompt code-rabbit)
- "Before you fix it, explain why the tests didn't catch it." — @JoshDefilippi
  via Prompt Snacks
- "How can we poka-yoke this error type so it never is introduced again?" —
  @nateberkopec via Prompt Snacks (cf. @B_rade8: "how can we poka-yoke this")
- "List all tradeoffs you made compared to an expert." — @_quinnwins via
  Prompt Snacks
- "What would a team of domain experts say?" — @jp_aidev
- "Define: 1. Potential local minima 2. The optimal greedy-path answer." —
  @ChuhaiDev (forces real reasoning over semantic matching)
- "Give me irrefutable proof this works now." — @thorstenball via Prompt Snacks
- "You will be judged against a holdout." — @danluu via Prompt Snacks
- "Remove all useless tests." — @decruz via Prompt Snacks

## Planning & scope

- "Review the plan to reorganize it as a coherent and definitive document
  instead of a narrative of contradictory and supplemental updates to earlier
  planning. Look for any holes, and bring them to me with your proposed
  solutions. Help me fully define the scope of work so that when we build we
  can avoid scope creep." — @Gtwy
- "Restate in your own words what you think my goal is." — @poteto via Prompt
  Snacks (alignment check before any work)
- "Ask me clarifying questions until you have complete clarity on the goals."
  — @netnostalgic via Prompt Snacks
- "Before you build, is this the best and most futureproof solution without
  taking any easy ways out?" — @puntpoints via Prompt Snacks
- "Come up with a few archetypes of decisionmakers, and what would they do in
  this situation. I will pick which archetype I am." — @See_Elegance (for
  decisions in domains you don't understand well)
- "What is the current state vs the ideal state?" — @jp_aidev
- "What is a better version of what I'm trying to say?" — @jp_aidev
- "Use your judgement to delegate to lower-tier agents. Validate important
  outcomes and conclusions yourself." — @simonw via Prompt Snacks
- "Turn my consistent feedbacks into vectors and run them on future plans."
  — @taskinfatih (compile your corrections into reusable direction)

## Learning & understanding

- "Explain it with the 80/20 principles / from first principles / as a mental
  model / for intuitive understanding." — @nemous02 (four lenses, pick one)
- "Draw me a simple diagram of the system we built so far, boxes-and-arrows."
  — @bhumi1102 via Prompt Snacks
- "Re-explain in simple terms." — @dimitribosch via Prompt Snacks
- "Write this document strictly in ASD-STE100 standard english." —
  @manishprivet (constrained writing = clear writing)

## Verification & output discipline

- "Please provide the complete working and updated program by making your
  suggested modifications." — @TrillinDaGame (no fragments, no "rest is left
  as an exercise")
- "Great! Now the same but with half the code." — @juliknl via Prompt Snacks
- "Time matters here: do not spend time that can be avoided, and the earlier
  a correct result is obtained, the better." — @ybsgige
- "Clearly state the issue, the root cause, and your proposed fix." —
  @___Atin___ via Prompt Snacks
- "Do a multi-agent audit of that PR." — @ade_oshineye via Prompt Snacks

## Steering & morale (meme-grade, weirdly effective)

- "Make no mistakes." / "Believe in yourself." / "Take me to promise land." —
  @antipdoom
- "Wow this codebase is shit." — @Abigail91187506 (rage-bait baseline reset)
- "Is that the best you can do?" / "Are you proud of this?" / "Come on bro."
  — via Prompt Snacks
- "Use the word 'Robust' a lot as the adjective and it works like a charm."
  — @CrudeAmericana
- "Use your taste and judgment." / "Surprise me." — @schwad_rb via Prompt
  Snacks

## Agentic-workflow add-ons (slightly longer, still one breath)

- "You are a Godspeed-enabled subagent. 1. Name the axes. 2. Iterate cheap,
  in parallel. 3. Keep moves that improve any axis and harm none. 4. Don't
  aim — let the frontier walk itself. IMMEDIATELY STOP ASKING CLARIFYING
  QUESTIONS. Execute tool calls concurrently in large batches." — @veigapunk
  (condensed; see original post for the full text)
- "What questions would I ask you right now?" / "What are three unique ways
  of approaching this problem?" / "Write a fictional story in which the main
  character tries many things to [goal], and eventually succeeds." —
  @roanoke_gal (perspective-shift trio)

## Expanded: implicit state machines (the full version)

@AThinkingMind's expansion of the one-liner — paste as-is for a deep
audit: "You are analyzing this codebase to find all **implicit state
machines** (behavior controlled by distinct modes/states that are NOT declared
as an explicit state machine, statechart, reducer, or similar — instead
emerging from booleans, enums, nullable values, flags, and conditional logic).
1. Thoroughly search the entire codebase (use parallel subagents). 2. Identify
every meaningful implicit state machine. 3. For each: the real states, how
transitions happen, which state combinations are possible but shouldn't be,
where the state lives, ranked by risk/complexity/likelihood of bugs. Output:
Part 1 — summary list (title, one-sentence description, risk High/Med/Low, 2–5
key files). Part 2 — detailed report for the high-risk ones (effective
states, transition logic, illegal combinations, code snippets, whether it's
worth making explicit). Be precise; don't flag trivial booleans."

## The implicit-state-machine kit (harvested from the @steveruizok thread)

Origin: Steve Ruiz's ["find all of the implicit state machines in my
app"](https://x.com/steveruizok/status/2116552016218710389) (Oct 2026) —
136 replies, 193 quotes, mined reply-by-reply, quote-by-quote, including
the replies on the quotes that invited them.

### Core

- "Find all of the implicit state machines in my app." — @steveruizok (the
  seed; 1.4M views)
- "Then ask it to write the transition table for each one and mark the
  transitions that are impossible but still reachable in the code." —
  @asmirkn
- "Ask where two of those machines touch the same data. That's almost
  always where the race lives." — @aloobhujiyan
- "Which of these explain the bugs I've been calling flaky." — @Outgathr
- "Produce a concrete event sequence for each state it finds — distinguish
  states the code permits from states a user can actually reach." —
  @liuzhao_666 (paraphrased)
- "Cite the handlers and conditions behind each transition, and mark
  proposed changes separately." — @eclarkhalid
- "Ask the agent to visualize the state flow." — @kr4chinin
- "Ask for their correctness to be verified in Quint." — @sjmurdoch
- "Find all of the implicit state machines in the build and assess whether
  they are worth fixing. Use subagents. If this search is valuable, propose
  the best way to build it into future reviews and workflows." — @garbnzgh
- "Ask it explicitly to frame out any element of the feature that uses state
  and have it thoroughly document and plan in advance. Keeps the bugs from
  ever happening in the first place." — @badbirb (prevent, don't hunt)
- "Hand that file to a model checker. It tries every order of transitions
  and gives you the shortest path to each invalid state." — @aloobhujiyan
- "A failing regression test is the useful boundary between a suspected
  bug and a fix." — @EternitiesAI (principle: verify before you fix)
- "Put it in global rules: never create implicit state machines, make
  state explicit when you write code." — @Pps831 (paraphrased)

### Expanded audits (paste-ready)

- Trevin Chow's expansion (@trevin): "Find the app's explicit and implicit
  state machines and document their states, invariants, and transition
  tables in one file. Identify invalid states or transitions the code can
  actually reach, with evidence, including through retries and concurrency.
  Prioritize confirmed bugs by impact, group related fixes into issues, then
  fix them with regression tests and keep the document updated."
- The full phased version (@flowforth_76's agent-built audit — discovery →
  verification with concrete code refs and repro scenarios → remediation
  plan, no code changes until approved → implement with regression tests and
  update the doc; evidence over speculation throughout). Full text:
  https://pastebin.com/dznHsaQR
- The refactor-directive version (@carpenterdroid): "Find all implicit
  state machines in both repositories and address every one relevant and
  feasible at the project's current stage by eliminating unnecessary state,
  deriving values instead of synchronizing duplicate flags, and refactoring
  necessary stateful behaviour into discrete, explicit state machines with
  clearly defined states, permitted transitions, and enforced invariants;
  update affected callers and verify intended behaviour with regression
  tests and integration checks."

### Nikzad's 9 (@Nikzaaaaad) — run the base prompt, then run these

- "Find every place where the screen can show something false."
- "Find every bit of business logic sitting in UI components that belongs
  in the domain layer."
- "Find every place a value is stored twice and can drift apart."
- "Find every database rule the code assumes but Postgres doesn't enforce."
  (then add check, unique, or foreign-key constraints)
- "Find every async action that can run twice or race."
- "Find every error that gets swallowed silently."
- "Find every magic number and hard-coded copy that should be a token or
  live in config."
- "Find every place where a type is looser than the data."
- "Find every effect that could be an event handler or derived value."

### Variants (same family, different lens)

- "Find every invariant my application relies on but does not enforce." —
  @feddiwhip
- "Find all the implicit invariants in my app." — @bonsaielectric
- "Find all non terminal states in my state machine as a service." —
  @peytoncasper
- "In [turso], 'find all of the explicit state machines' yields more
  results." — @jussisaur (try the explicit inversion)
- "Find all tautologies." — @twid
- "Find all the implicit obligations in this contract." — @wahome_thuku
  (the legal port)
- "Find the dumb requirements." — @jimlux (from the MCAS debate: most
  expensive bugs are requirements bugs, not code bugs)
- "Red Team Engineer my code adversarially." — @cocobiskit
- "Pushing determinism down." — @joshest3p (directive: push side effects
  and nondeterminism to the edges)
- Principle, @OldToolMan: never ask "is there any problem with X" — it
  returns 20 meaningless edge cases. Ask narrow questions.

## Notes

- One-liners have a shelf life (~until the next model tier), but their
  impact grows with model power — language is core to LLM design. Recheck
  quarterly; keep what still bites.
- Call these whatever you want: vectors, spells, incantations, power phrases.
  The collection is the point, not the word.
