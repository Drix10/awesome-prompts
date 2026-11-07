---
name: god-tier-mini-prompts
description: One-line "god-tier" prompt vectors for coding agents. Use when the user wants a short, high-density prompt to steer Claude Code, Codex, Cursor, or any coding agent — for architecture, debugging, review, planning, learning, or verification — instead of a full skill. Invoke by matching the task to a prompt below, or run the meta-prompt to auto-pick.
---

# God-Tier Mini Prompts

Single sentences so dense each verb, noun, and adjective does work.
Philosophy: **density beats length** — one loaded sentence outperforms a page
of skill lists. Short prompts also get a fresh context window's full
attention ("attention budget" — delegate real hunting to subagents).

Sourced from [Bootoshi's thread](https://x.com/KingBootoshi/status/2118803776387928228)
(Nov 2026), [Prompt Snacks](https://promptsnacks.com), and
[Notchbird's Banger Prompts](https://notchbird.com/prompts).
Every prompt keeps its author's credit.

## Meta-prompt: let the agent pick

Paste this plus your task/idea/code, and let the model choose:

```
Consider all the mini-prompts in this skill, pick the ones that would
improve my idea/input/software the most, and apply them. (h/t @PyrosAI)
```

Narrow it per phase: "...pick the 3 best for *planning* / *review* /
*debugging* this."

## Architecture & design

- "Find all of the implicit state machines in my app." — @steveruizok (the
  prompt that started the thread; full expanded version below)
- "What higher-level abstraction would make this entire problem disappear?" —
  @Wyrmfalls (Bootoshi: "last one is a banger")
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

@AThinkingMind's expansion of @steveruizok's prompt — paste as-is for a deep
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

## Notes

- One-liners have a shelf life (~until the next model tier), but their
  impact grows with model power — language is core to LLM design. Recheck
  quarterly; keep what still bites. (debate: @Mockapapella vs @KingBootoshi)
- A "skill" is technically a saved prompt — call these whatever you want:
  vectors, spells (@dkubb: "we need to call these one line god prompts
  spells"), incantations (@pragmaxxer), power phrases. The collection is the
  point, not the word.
- `shortcut: coverage is X-thread + Prompt Snacks/Notchbird only; Bootoshi's
  follow-up "GOD TIER ENGINEERING PROMPTS" thread and Grok-curated lists not
  yet mined — upgrade by appending them here.`
