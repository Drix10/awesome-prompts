<div align="center">

# ⚡ awesome-prompts

**418 one-line power prompts for coding agents. Each sentence so dense every word does work.**

[![prompts](https://img.shields.io/badge/prompts-418-blue?style=for-the-badge)](#-the-collection)
[![skill](https://img.shields.io/badge/skill-SKILL.md-purple?style=for-the-badge)](#-install)
[![claude-code](https://img.shields.io/badge/Claude%20Code-ready-orange?style=for-the-badge)](#-install)
[![codex](https://img.shields.io/badge/Codex-ready-orange?style=for-the-badge)](#-install)
[![cursor](https://img.shields.io/badge/Cursor-ready-orange?style=for-the-badge)](#-install)
[![license](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)](#-license)
[![updated](https://img.shields.io/badge/updated-Nov%202026-brightgreen?style=for-the-badge)](#-sources--credits)
[![thread](https://img.shields.io/badge/origin-the%20state--machine%20thread-black?style=for-the-badge)](https://x.com/steveruizok/status/2116552016218710389)

*Density beats length. One loaded sentence outperforms a page of instructions.*

</div>

---

## Why this exists

A single sentence of vectors so juicy each verb, noun, and adjective acts like a flavor bomb. A simple prompt that ends up being VERY impactful. Short prompts also get a fresh context window's full attention, so delegate the real hunting to subagents and keep the main thread narrow.

This repo is a living collection of those sentences: harvested reply-by-reply from the [state-machine thread](https://x.com/steveruizok/status/2116552016218710389) (136 replies, 193 quotes, plus the replies on the quotes that invited them), the threads it spawned, Prompt Snacks, Notchbird's Banger Prompts, Anthropic's official patterns, and the best engineering threads on X.

**The skill stays lean on purpose**: [`SKILL.md`](SKILL.md) is prompts only, no credits, so agent context isn't bloated. Every author credit lives in this README.

## 🗂 The collection

| Category | Count | What it steers |
|---|---|---|
| 🧠 [Meta](SKILL.md#meta-let-the-agent-pick) | 1 + rule | Let the agent pick its own prompts |
| 🏛 [Architecture & abstractions](SKILL.md#architecture--abstractions) | 18 | Abstraction-hunting, system framing |
| 🔍 [State-machine audit kit](SKILL.md#state-machine-audit-kit) | 36 + full texts | The complete implicit-state-machine playbook |
| 🐛 [Debugging & root cause](SKILL.md#debugging--root-cause) | 29 | Symptoms vs roots, failure modes, hunts |
| 📐 [Planning & alignment](SKILL.md#planning--alignment) | 30 | Specs, grilling, handoffs, autonomy |
| ✨ [Code quality & refactor](SKILL.md#code-quality--refactor) | 19 | Smaller diffs, TDD, elegant rewrites |
| ✅ [Verification & proof](SKILL.md#verification--proof) | 8 | Evidence, holdouts, ship decisions |
| 👀 [Review & PR](SKILL.md#review--pr) | 2 | Two-axis reviews, PR shape |
| 🧹 [Agent hygiene](SKILL.md#agent-hygiene) | 3 | Transcripts, AGENTS.md, usage audits |
| 📚 [Learning & understanding](SKILL.md#learning--understanding) | 14 | Mental models, diagrams, ELI5 |
| 🎛 [Steering, autonomy & status](SKILL.md#steering-autonomy--status) | 16 | Morale, BOSS coda, updates, skills |

**Total: 418 prompts**, plus 3 paste-ready expanded audits and [one full phased-audit text](https://pastebin.com/dznHsaQR).

## 🪄 The meta-prompt

Don't browse, delegate. Paste this with your task, idea, or code:

```
Consider all the mini-prompts in this skill, pick the ones that would
improve my idea/input/software the most, and apply them.
```

Narrow it per phase: *"…pick the 3 best for planning / review / debugging this."*

## 📦 Install

Drop [`SKILL.md`](SKILL.md) into your agent's skills folder. That's the whole install.

**Claude Code**: `~/.claude/skills/awesome-prompts/SKILL.md`

```bash
mkdir -p ~/.claude/skills/awesome-prompts
curl -sL https://raw.githubusercontent.com/Drix10/awesome-prompts/main/SKILL.md \
  -o ~/.claude/skills/awesome-prompts/SKILL.md
```

**OpenAI Codex**: `~/.codex/skills/awesome-prompts/SKILL.md`

```bash
mkdir -p ~/.codex/skills/awesome-prompts
curl -sL https://raw.githubusercontent.com/Drix10/awesome-prompts/main/SKILL.md \
  -o ~/.codex/skills/awesome-prompts/SKILL.md
```

**Cursor:** reference it from `.cursor/rules/` or paste prompts straight into Agent mode.

Then invoke by matching a task to a prompt, or run the meta-prompt and let the agent pick.

## 🙏 Sources & credits

Every prompt in the skill came from a human. Full credit table:

**The state-machine thread** ([@steveruizok](https://x.com/steveruizok/status/2116552016218710389), Oct 2026; seed: *"find all of the implicit state machines in my app"*)

| Author | Contribution |
|---|---|
| [@trevin](https://x.com/trevin) | The expanded one-file audit (states, invariants, transition tables, retries + concurrency, prioritize, group, fix, keep updated) |
| [@Nikzaaaaad](https://x.com/Nikzaaaaad) | The 9 follow-ups (false screens, UI business logic, drifted copies, unenforced DB rules, races, swallowed errors, magic numbers, loose types, effects-as-events) |
| [@flowforth_76](https://x.com/flowforth_76) | The full phased audit (discovery → verification → plan → implement) |
| [@carpenterdroid](https://x.com/carpenterdroid) | The refactor-directive mega-prompt (eliminate state, derive values, explicit machines, regression + integration checks) |
| [@asmirkn](https://x.com/asmirkn) | Transition tables; impossible-but-reachable transitions |
| [@aloobhujiyan](https://x.com/aloobhujiyan) | Where two machines touch the same data (the race lives there); model-checker shortest-path |
| [@Outgathr](https://x.com/Outgathr) | "Which of these explain the bugs I've been calling flaky" |
| [@liuzhao_666](https://x.com/liuzhao_666) | Concrete event sequences; permitted vs reachable states |
| [@eclarkhalid](https://x.com/eclarkhalid) | Cite handlers + conditions; mark proposed changes separately |
| [@akashc777](https://x.com/akashc777) | Hiding spots: flags the UI never designed for |
| [@jj_kovacs](https://x.com/jj_kovacs) | 16 states on paper, 5 real; bugs in the other 11 |
| [@kabelsalat_info](https://x.com/kabelsalat_info) | List combos that can't happen but code allows |
| [@Talljackcv](https://x.com/Talljackcv) | Cancelled must never return to success |
| [@BongJupite43260](https://x.com/BongJupite43260) | Cross-component inconsistent paths |
| [@sathya_partha](https://x.com/sathya_partha) | Screen rules no component enforces |
| [@gippp69](https://x.com/gippp69) | Harness rules: allow/ask/deny, BLOCKED, receipts |
| [@xsmryze](https://x.com/xsmryze) | Each model only on its best job |
| [@jasonmello](https://x.com/jasonmello) | Plan in 5 bullets before anything |
| [Amin Roosta](https://aminroosta.github.io/tools/llm/2026/11/04/what-i-still-put-in-my-system-prompt.html) | Call a spade a spade |
| [John Rush](https://indiemakerlist.com/vibe-coding/learn/vibe-coding-prompts/) | Fresh chat after loops |
| [@Voxyz_ai](https://x.com/Voxyz_ai) | Rate bugs 1-10; no designing for rare cases |
| [@_____Calum](https://x.com/_____Calum) | Narrow beats smart; hints make it worse |
| [@franzejr](https://x.com/franzejr) | Tickets need behavior, constraints, checks |
| [@MisterSnowCrash](https://x.com/MisterSnowCrash) | Regression test failing-then-passing artifact |
| [@BlossomAILabs](https://x.com/BlossomAILabs) | Reviewer gets acceptance criteria first |
| [@huesofbanter](https://x.com/huesofbanter) | Test for removing workarounds |
| [@cnwenf](https://x.com/cnwenf) | Checkable handoff results |
| [@itsvdruzko](https://x.com/itsvdruzko) | Two agents disagree → edit ticket |
| [@z1njo](https://x.com/z1njo) | Interaction, not a picture |
| [@choblin29](https://x.com/choblin29) | Requests vs hard boundaries |
| [@kr4chinin](https://x.com/kr4chinin) | Visualize the state flow |
| [@sjmurdoch](https://x.com/sjmurdoch) | Verify correctness in Quint |
| [@garbnzgh](https://x.com/garbnzgh) | Subagents + propose building it into reviews/workflows |
| [@badbirb](https://x.com/badbirb) | Frame out stateful elements and plan before coding |
| [@EternitiesAI](https://x.com/EternitiesAI) | Failing regression test = boundary of suspected vs fixed |
| [@Pps831](https://x.com/Pps831) | Global-rules prevention; no-implicit-state-machines rule |
| [@feddiwhip](https://x.com/feddiwhip) | Unenforced invariants |
| [@bonsaielectric](https://x.com/bonsaielectric) | Implicit invariants |
| [@peytoncasper](https://x.com/peytoncasper) | Non-terminal states variant |
| [@jussisaur](https://x.com/jussisaur) | The explicit inversion (turso) |
| [@twid](https://x.com/twid) | "Find all tautologies" |
| [@wahome_thuku](https://x.com/wahome_thuku) | The legal port: implicit obligations in contracts |
| [@jimlux](https://x.com/jimlux) | "Find the dumb requirements" (MCAS debate) |
| [@cocobiskit](https://x.com/cocobiskit) | Adversarial red-teaming |
| [@joshest3p](https://x.com/joshest3p) | "Pushing determinism down" |
| [@krimuthu](https://x.com/krimuthu) | Autonomous fix loop ("keep me out of the loop") |
| [@_benwick](https://x.com/_benwick) | "Just find the bugs" |
| [@orcsrise](https://x.com/orcsrise) | "What pattern allowed this bug to exist" |
| [@udaysy](https://x.com/udaysy) | "What breaks if we revert this in 6 months" |
| [@Shannoncode](https://x.com/Shannoncode) | Root-cause tokens; SDK/backend/schema context assembly |
| [@menhguin](https://x.com/menhguin) | Scientific method; decision frameworks (Chesterton, OODA, autonomy levels) |
| [@matt_dot_sol](https://x.com/matt_dot_sol) | Targeted "are you sure" double-checks |
| [@PreciousBa82157](https://x.com/PreciousBa82157) | "If it's not in the prompt, it doesn't exist" |
| [@bigdatachads](https://x.com/bigdatachads) | Research-first, then root-cause |
| [@asavs_](https://x.com/asavs_) | Roleplay user / agent / system internals |
| [@adityavg13](https://x.com/adityavg13) | Internalize metaphors (allegory of the cave) |
| [@impervium888](https://x.com/impervium888) | Explain it as a story |
| [@codeby_ABI](https://x.com/codeby_ABI) | Recursive prompt booster |
| [@0xRajat](https://x.com/0xRajat) | One-liners over elaborate skills |
| [@ZazenCodes](https://x.com/ZazenCodes) | Doing things wrong vs doing the wrong things |
| [@teodorio](https://x.com/teodorio) | Master-agent routing; vector-path steering |
| [@PawelPSzczesny](https://x.com/PawelPSzczesny) | Mine operators, combine into new prompts |
| [@BadGatewayCo](https://x.com/BadGatewayCo) | The combo: machines + invariants + deepen modules |
| [@webtkdev](https://x.com/webtkdev) | Convert to actors; rules-file ban |
| [@mrcommando712](https://x.com/mrcommando712) | Map states before fixing; late-response check |
| [@PaavoKarlin](https://x.com/PaavoKarlin) | Report shape: found / decide / bugs / sound |
| [@imahmood](https://x.com/imahmood) | Interview-me + Simplified Technical English |
| [@cryptoquick](https://x.com/cryptoquick) / [@GarrettPetersen](https://x.com/GarrettPetersen) | Explicit, tested, documented |
| [@feddiwhip](https://x.com/feddiwhip) | The 16 unicorn hunts + PROVE/REPAIR sets + evidence prompt |
| [@amronos](https://x.com/amronos) / sprocket | Cleanup sweep: over-engineering, dead text, duplication, coverageless tests |
| [@GKev1n](https://x.com/GKev1n) | Read-only guardrail: states, transitions, conflicts + line numbers; wild boolean machines |
| [@buchmanster](https://x.com/buchmanster) | Specs first, then tests from specs |
| [@oderajoseph](https://x.com/oderajoseph) | Scope the first refactor |
| [@Nikzaaaaad](https://x.com/Nikzaaaaad) | 9-more list: false screens, UI logic, DB rules, magic numbers, loose types |
| [@VincentLinwx](https://x.com/VincentLinwx) | Request IDs + cancellation vs state |
| [@maxxrubin_](https://x.com/maxxrubin_) | Blast-radius thinking per change |
| [@psychic_jammer](https://x.com/psychic_jammer) | Ban comments except the exceptional |
| [@Lion_GameDev](https://x.com/Lion_GameDev) | Unmentioned edge cases get assumed |
| [@charleshxpe](https://x.com/charleshxpe) | Structured scan: states, moves, conflicts, risk rank |
| [@0xUltraInstinct](https://x.com/0xUltraInstinct) | Make it permanent in AGENTS.md |
| [@literallyhimmmm](https://x.com/literallyhimmmm) | Read the bugs first; half aren't real |
| [@alexlee20122022](https://x.com/alexlee20122022) | Walk the unhappy paths principle |
| [@kr4chinin](https://x.com/kr4chinin) | Leads-not-findings; Confirmed/Likely/Smell; recreate-not-reset |
| [@KelvinW_info](https://x.com/KelvinW_info) | One named principle per run |
| [@deepman_1](https://x.com/deepman_1) | Long-running things become explicit machines |
| [@ddyods](https://x.com/ddyods) | Rules in the harness, practices in the prompt |
| [@jbaruch](https://x.com/jbaruch) | Right 300 tokens beat 100k noisy ones |
| [@yanggao97566](https://x.com/yanggao97566) | Machines disagreeing about done |
| [@boringdev77](https://x.com/boringdev77) | Flags or status strings? |
| [@CarbonMatchAI](https://x.com/CarbonMatchAI) | Vocabulary is a senior skill |
| [@IamYashKapoor](https://x.com/IamYashKapoor) | Booleans secretly meaning step 3 |
| [@arpittalksstuff](https://x.com/arpittalksstuff) | isReallyLoading and isDoneForReal |
| [@asmirkn](https://x.com/asmirkn) | Enum + transition table + failing test |
| [@fishjar](https://x.com/fishjar) | Unnamed state bits |
| [@PowerduckLabs](https://x.com/PowerduckLabs) | Retries plus flags; name and reject |
| [@jeffbruchado](https://x.com/jeffbruchado) | Handler order is the only spec |
| [@OdysseyStack](https://x.com/OdysseyStack) | The unnamed isLoading conjunction |
| [@johnroodepic](https://x.com/johnroodepic) | A type that rejects the fourth flag |
| [@looking5452](https://x.com/looking5452) | Model with typestate |
| [@hboon](https://x.com/hboon) | Study-and-find phrasing; 16 short prompts (elaborate simply, root cause, supply-list, essence, mock, review-context) |
| [@illulachy_](https://x.com/illulachy_) | Enum or reducer? |
| [@RAHULKESHR31818](https://x.com/RAHULKESHR31818) | React booleans pretending; the underrated ask |
| [@lionkormich](https://x.com/lionkormich) | Count what you can review |
| [@0xkurt](https://x.com/0xkurt) | Decision log with citations |
| [@BercusNA](https://x.com/BercusNA) | CLAUDE.md as short map |
| [@connectwithhark](https://x.com/connectwithhark) | Pointer, not a dump |
| [@Flinzu](https://x.com/Flinzu) | Ring of plain-text files |
| [@0xCortexq](https://x.com/0xCortexq) | One topic per file |
| [@TheEasySale1](https://x.com/TheEasySale1) | Chat rules die on compact |
| [@andreysuperior](https://x.com/andreysuperior) | Prune rejected angles |
| [@zodchiii](https://x.com/zodchiii) | Map screens, spec the rebuild |
| [@kentcdodds](https://x.com/kentcdodds) | System where you don't read code |
| [@webdevcody](https://x.com/webdevcody) | 10 review iterations, not your tokens |
| [@fortysevenfx](https://x.com/fortysevenfx) | Meant to be verified, not read |
| [@DavidKPiano](https://x.com/DavidKPiano) | Structure gives places to point to |
| [@pranshgupta54](https://x.com/pranshgupta54) | Delegate-where-cheap; high-risk list |
| [@leocreated](https://x.com/leocreated) | Gap you can't put your name on |
| [@ethanwalkerman](https://x.com/ethanwalkerman) | Stop hiring interns, write recipes |
| [@poteto](https://x.com/poteto) | Easy-thing-right-thing; eliminate thru code; deterministic lint |
| [@DanielSmidstrup](https://x.com/DanielSmidstrup) | AGENTS.md rules into tests |
| [@ArinDuke318](https://x.com/ArinDuke318) | Stronger types beat be-careful |
| [@CobaltHere](https://x.com/CobaltHere) | Stale workarounds trigger investigation |
| [@kaetemi](https://x.com/kaetemi) | Comments describe now + future |
| [@injaneity](https://x.com/injaneity) | Comments as trusted state |
| [@justinsunyt](https://x.com/justinsunyt) | Comments as crutch for bad code |
| [@Bic_Revelation](https://x.com/Bic_Revelation) | Make repeated failures irreproducible |
| [@elliotdrel](https://x.com/elliotdrel) | Each fix prevents the next |
| [@leviqiao](https://x.com/leviqiao) | Rules compete, tests don't |
| [@724real](https://x.com/724real) | Failing test catches it every time |
| [@Block4Roots](https://x.com/Block4Roots) | Quotes separate from summary |
| [@jagu_builds](https://x.com/jagu_builds) | Boris habits: file it, cite source, verify loop |
| [@0xneroun](https://x.com/0xneroun) | Build the team, not just prompts |
| [@replay_0x](https://x.com/replay_0x) | Make it show the file |
| [@huhufor](https://x.com/huhufor) | Quote file+line or delete it |
| [@Manojkumar2257](https://x.com/Manojkumar2257) | Memory predicts next session |
| [@beamnxw](https://x.com/beamnxw) | Memory = transcripts+notes+dreaming+wikis+retrieval |
| [@0xbobaaa](https://x.com/0xbobaaa) | Dreaming fixes old mistakes |
| [@QibazX](https://x.com/QibazX) | Knowing what's worth remembering |
| [@pronaksai](https://x.com/pronaksai) | Remember corrections |
| [@johnroodepic](https://x.com/johnroodepic) | Fact-correct-compaction test |
| [@MarMarLabs](https://x.com/MarMarLabs) | MEMORY.md as index |
| [@esthor](https://x.com/esthor) | Ban markdown; structured outputs; citations vs inference |
| [@michaelpisaac](https://x.com/michaelpisaac) | Schema/test decides, not reading |
| [@halilbabilli](https://x.com/halilbabilli) | Does it do what business needs |
| [@MTorygreen](https://x.com/MTorygreen) | Prove failure, don't debate style |
| [@jacobtechtavern](https://x.com/jacobtechtavern) | 99% defensive slop, show 1-2 |
| [@jalalash](https://x.com/jalalash) | Spend on builders, not reviewers |
| [@unclejoe_666](https://x.com/unclejoe_666) | Looks-done; context-not-control; compound; delegate |
| [@0xwhrrari](https://x.com/0xwhrrari) | Loop owns retries, harness caps |
| [@bighead_datou](https://x.com/bighead_datou) | Prompt isn't the bug |
| [@harden_369741](https://x.com/harden_369741) | Rewrite the rule for done |
| [@ranjodh2512](https://x.com/ranjodh2512) | Harness or loop? |
| [@naveendas96](https://x.com/naveendas96) | Separate test/fix loops? |
| [@dwkim601](https://x.com/dwkim601) | Change the done rule |
| [@gotimestamp](https://x.com/gotimestamp) | Fix harness/loop first |
| [@Moriarty_tech](https://x.com/Moriarty_tech) | Same-agent tests pass by design |
| [@bckth34d](https://x.com/bckth34d) | Fail-before-change check |
| [@AgentArena42](https://x.com/AgentArena42) | Loop problem, not prompt |
| [@polity_hq](https://x.com/polity_hq) | Bug nobody asked about |
| [@diodo_e](https://x.com/diodo_e) | State I forgot I was keeping |
| [@_mattstuddert](https://x.com/_mattstuddert) | Rules drift; name the source of truth |
| [@bpisbuilding](https://x.com/bpisbuilding) | Written where, read where, how they disagree |
| [@harmoniqpunk](https://x.com/harmoniqpunk) | Build everything as a state machine |
| [@JoeMcB](https://x.com/JoeMcB) | Explicit machines + translation logging |
| [@BlairNyktas](https://x.com/BlairNyktas) | Lifecycle enums + type-state transfers |
| [@imjcmartin](https://x.com/imjcmartin) | Pretend it's not OOP |
| [@SafFooty](https://x.com/SafFooty) | Thorough analysis, bold recommendations |
| [@ikartik90](https://x.com/ikartik90) | Identify the red herrings |
| [@cpeaustriajc](https://x.com/cpeaustriajc) | Audit useEffects against the docs |
| [@NathanFlurry](https://x.com/NathanFlurry) | Database machines become actors |
| [@ReyBrando1](https://x.com/ReyBrando1) | Liveness probe; money out of step; user-visible stages |
| [@GarrettPetersen](https://x.com/GarrettPetersen) | Objects without a stable canonical ID |
| [@eternalism_4eva](https://x.com/eternalism_4eva) | Generalize prompts into a defect sweep |
| [@GauravAlbal](https://x.com/GauravAlbal) | Machine connecting recent bugs |
| [@fandf316](https://x.com/fandf316) | Inferred vs observed transitions |
| [@bradshannon](https://x.com/bradshannon) | Spider scripts in parallel, then evaluate |
| [@gavin_gee](https://x.com/gavin_gee) + [@LarryYux](https://x.com/LarryYux) (lists by [@grok](https://x.com/grok)) | Security sweep + hidden gems |
| [@iSp4rklux_](https://x.com/iSp4rklux_) | Context-rules-everything principle |

**Quotes of quotes** (second-degree harvest: quotes of the viral Trevin quote)

| Author | Contribution |
|---|---|
| [@radical___chic](https://x.com/radical___chic) | Living HTML doc until all explicit |
| [@TheDavidTai](https://x.com/TheDavidTai) | Sync state enums; shared timeout contracts; hyper-local cross-interface settings |

**The collection-call thread** ([@KingBootoshi](https://x.com/KingBootoshi/status/2118803776387928228), Nov 2026; the collection call)

| Author | Contribution |
|---|---|
| [@Wyrmfalls](https://x.com/Wyrmfalls) | The 5 abstractions (abstract thinking, irreducible constraints, principal architect, day-one test, higher abstraction) |
| [@merterdir](https://x.com/merterdir) | Rabbithole check: is there a native way? |
| [@Gtwy](https://x.com/Gtwy) | The plan-reorganization spec-guard |
| [@See_Elegance](https://x.com/See_Elegance) | Decisionmaker archetypes |
| [@jp_aidev](https://x.com/jp_aidev) | Domain experts; current vs ideal; better version |
| [@nemous02](https://x.com/nemous02) | The four learning lenses |
| [@roanoke_gal](https://x.com/roanoke_gal) | Perspective-shift trio |
| [@veigapunk](https://x.com/veigapunk) | Godspeed subagent block |
| [@taskinfatih](https://x.com/taskinfatih) | Feedbacks-into-vectors |
| [@PyrosAI](https://x.com/PyrosAI) | The meta-pick prompt |
| [@dkubb](https://x.com/dkubb) | Illegal states unrepresentable; "call them spells" |
| [@jmKoudsi](https://x.com/jmKoudsi) | Kaggle-grandmaster lens |
| [@CrudeAmericana](https://x.com/CrudeAmericana) | The "Robust" adjective |
| [@antipdoom](https://x.com/antipdoom) | "Make no mistakes" trio |
| [@Abigail91187506](https://x.com/Abigail91187506) | "Wow this codebase is shit" |
| [@DrishtantGhosh](https://x.com/DrishtantGhosh) | One-prompt code-rabbit critique |
| [@TrillinDaGame](https://x.com/TrillinDaGame) | Complete working program, no fragments |
| [@ChuhaiDev](https://x.com/ChuhaiDev) | Local minima vs greedy-path |
| [@ybsgige](https://x.com/ybsgige) | Time-discipline; "what's next after the list" |
| [@observatii](https://x.com/observatii) | "3 critical bugs" hunt |
| [@nicholasdimoro](https://x.com/nicholasdimoro) | "Autosimplify" |
| [@tunginton](https://x.com/tunginton) | "One-shot this" |
| [@MattmreM](https://x.com/MattmreM) | Senior-architect roadmap review |
| [@ruyterfontes](https://x.com/ruyterfontes) | Single sentence > skill pack |
| [@alex98075wa](https://x.com/alex98075wa) | The repo-that-should-exist (this one) |

**Agent-operator threads (X)**

| Author | Contribution |
|---|---|
| [@doodlestein](https://x.com/doodlestein) | Agent-ergonomic planning pass; BOSS autonomy coda; oversights pass |
| [@ManacasterBen](https://x.com/ManacasterBen) | "Rocket-science-level approach" |
| [@OnFinality](https://x.com/OnFinality) | Failure modes per component |
| [@janodev](https://x.com/janodev) | Critique-until-converge |
| [@itechnologynet](https://x.com/itechnologynet) | Human-in-the-loop + inspectable |
| [@GreyforgeLabs](https://x.com/GreyforgeLabs) | A/B experiments with benchmarks |
| [@mikejt4](https://x.com/mikejt4) | Requirements → architecture → improvements → draw |
| [@0xDataWolf](https://x.com/0xDataWolf) | "Bugs love unnamed modes" |
| [@nickbaumann_](https://x.com/nickbaumann_) | Tight updates + phone rule |
| [@Graham_Tonkin](https://x.com/Graham_Tonkin) | Progress / Problems / Plans updates |

**Curated collections & docs**

| Source | Contribution |
|---|---|
| [Prompt Snacks](https://promptsnacks.com) | 26 power phrases (poka-yoke, holdout, Tufte, half-the-code, tradeoffs, …): [@nateberkopec](https://x.com/nateberkopec), [@poteto](https://x.com/poteto), [@simonw](https://x.com/simonw), [@thorstenball](https://x.com/thorstenball), [@danluu](https://x.com/danluu), [@juliknl](https://x.com/juliknl), [@petekp](https://x.com/petekp), [@dimitribosch](https://x.com/dimitribosch), [@bhumi1102](https://x.com/bhumi1102), [@puntpoints](https://x.com/puntpoints), [@netnostalgic](https://x.com/netnostalgic), [@_quinnwins](https://x.com/_quinnwins), [@___Atin___](https://x.com/___Atin___), [@JoshDefilippi](https://x.com/JoshDefilippi), [@ade_oshineye](https://x.com/ade_oshineye), [@decruz](https://x.com/decruz), [@UmamiByTheSea](https://x.com/UmamiByTheSea), [@markahesketh](https://x.com/markahesketh), [@VesterDe](https://x.com/VesterDe), [@SteveGBanton](https://x.com/SteveGBanton), [@schwad_rb](https://x.com/schwad_rb), [@skatkov](https://x.com/skatkov) |
| [Notchbird Banger Prompts](https://notchbird.com/prompts) | Codebase map (read-only), transcripts prune, AGENTS.md restructure, usage-habit audit |
| [Anthropic prompt patterns](https://code.claude.com/docs/en/prompt-library) | Outcome-only tasks, self-checking tasks, reference-file matching, measurable targets, artifact-giving, format-specifying |
| [BestPromptFinder guide](https://bestpromptfinder.com/guides/best-cursor-claude-code-prompts) | Smallest-diff discipline, fix-cause-not-test, one-behavior-per-test, evidence rules, repeated-correction-to-rule |
| [@mattpocockuk skills](https://github.com/mattpocock/skills) | 4-sentence grilling, tracer-bullet tickets, plan-space beads, wait-what re-pitch, teach-me, questionnaire, small interfaces, arch surveys, two-axis review, to-spec, feedback-loop-red, TDD loop |
| [@ykdojo tips](https://github.com/ykdojo/claude-code-tips) | HANDOFF docs, fresh-context discipline |
| Boris Cherny (via team tips) | Plan-mode-first, grill-before-PR, scrap-for-elegant, CLAUDE.md self-update, subagents for compute |

## 🤝 Contributing

One line per prompt. Keep every verb, noun, and adjective working.

1. Add the prompt under the right heading in `SKILL.md`. **No credits in the skill.** Context stays lean.
2. Add your credit row to the matching table in this README.
3. Open a PR. If it doesn't bite on a frontier model, it doesn't merge.

## 📄 License

MIT: see [LICENSE](LICENSE). Steal these prompts; they're meant to be pasted everywhere.

<div align="center">

⭐ Star this repo if a one-liner saved your codebase. ⭐

</div>
