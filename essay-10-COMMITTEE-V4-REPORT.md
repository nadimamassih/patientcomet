# Essay-10 — Committee v4 Trial Report
**Date: 2026-06-11 · 3 full loops · Verdict: SHIP (after Loop 3 fixes)**
**Final file: `essay-10-FINAL-v2.md` · HTML rebuild required (see build notes in file)**

---

## THE FACT-CHECK (adversarial, fresh agent, claim ledger only — never saw the article)

19 claims checked against fresh searches (49 sources, 16 search rounds).
**11 VERIFIED · 7 CORRECTED · 1 UNVERIFIABLE (removed).**

### Killed or corrected — these were in the published-candidate draft:

| # | Claim in old draft | Finding | Action taken |
|---|---|---|---|
| 1 | MedRxiv: 64% of AI clinical notes contain a false claim | **No such study exists.** Garbled mutation of a different metric (64–72% of *residual hallucinations* stem from reasoning failures) | REMOVED entirely |
| 2 | arXiv:2604.22750 = MIT CSAIL + Microsoft Research; source of 18.6×, $0.04→$1.20, 4–6×/10–15× multipliers | **Citation laundering.** Real paper is Stanford + Michigan (Brynjolfsson et al.); it only contains the 1,000× and 30× findings. 18.6× = Jellyfish via TechCrunch; $0.04→$1.20 = EY; multipliers = unsupported | All re-attributed; table caption now labelled "Patient Comet projection" |
| 3 | Cliprise Feb 2026 benchmark = 3.75% broadcast yield | **Wrong source.** 3.75% = Kalshi NBA Finals ad, June 2025 (15 usable from ~400 Veo 3 clips). Cliprise never reported it | Re-attributed to Kalshi; better story, verified |
| 4 | Midjourney Pro $96/user/month | **Wrong. Pro is $60/month.** ($48 annual; Mega is $120) | Line rebuilt: $360 + $60 fast-hours = $420 |
| 5 | ElevenLabs $0.06–0.12/1k chars | **Too low.** Real: ~$0.12–0.30/1k | Register corrected; $30 line item still valid |
| 6 | Higgsfield $0.15–0.20/image | Unsupported. Published rate ~$0.234/call | 500 images = $117 |
| 7 | Stanford RegLab "2025 study" | 2024 study (peer-reviewed JELS 2025) | Dated correctly |
| 8 | Lightrun "42–43%" pre-production | Exactly **43%, in production, after passing QA** | Corrected |
| 9 | Westlaw "early-2000s flat subscriptions, firms absorbed" | **Wrong timeline.** Flat contracts spread through the 2000s; absorption was post-2008 and gradual (97% passed on in 2008 → 73% by 2011 → ~half absorbed) | S2 history rewritten accurately |
| 10 | Standfirst "$2,000/month" Microsoft per-engineer | Figure derives from Uber's documented experience, applied to the story | Now "$500 to $2,000 across the industry's biggest deployments" |
| 11 | Copilot Business $18 | Promotional rate (standard $21, Enterprise $30) | "$18 to $30 depending on tier" in S2; register notes promo |

### Verified and load-bearing (intact):
Zylo 78% + $1.2M avg · ServiceNow/Romack · Uber April exhaustion + caps · Catanzaro quote (Fortune/Axios, Apr 2026) · Goldman 24× by 2030 · Atlanta Fed $3,470 · Digiday March 3 2026 (all names and quotes exact) · Globant AI Pods ($20K/100M tokens, June 2025) · HBR/BetterUp 41% + 1h56m · 98% token price fall · Microsoft Claude Code cancellation · **Claude Fable 5 $10/$50 (launched June 9, 2026)** — session math verified: 2–3hr ≈ $18, 4hr ≈ $30–38, 5hr ≈ $45.

---

## THE NEW ARITHMETIC (every figure recomputed in Python, all PASS)

- Proposal $75,000 = $72,000 team (60×450 + 90×280 + 60×220 + 30×220) + **$3,000 production budget** (new device: the visible production budget mirrors the invisible AI one)
- Type 2 project compute: **$2,861** (was $3,000 — Midjourney and Higgsfield corrections)
- Type 1 subscriptions: $1,350 (unchanged) — now kept OUT of the headline (the old "5.8%, zero lines on the invoice" contradicted the article's own doctrine that Type 1 belongs at zero lines)
- Headline: **$2,861 = 3.8% of engagement, invisible**
- 5 projects: $4,768/month ("just under $5,000") · 25-person: $4,800/project derived (boutique + second video stack + double research) × 60 = $288,000 = 20% of $1.44M planned profit (20% margin now stated explicitly)
- Per-brief compute: ~8 sessions ≈ $150 vs $450 junior afternoon (old $18-vs-$450 was a unit error caught in Loop 3)

---

## THE THREE LOOPS

**Loop 1 — HOLD (≈62/100).** Adversarial verification found the fabricated stat, the citation laundering, two wrong prices. Argument trial found 10 structural flaws (session-cost discrepancy, $1,389/$1,500 wobble, phases timeline broken by its own Globant citation, unsupported "2027" dek). Cold read: "B+ piece with B- quality control on its own numbers." → **Full rewrite** (per your rule: rewrite before looping, not after).

**Loop 2 — FIX (≈80/100).** Fresh agents on the rewrite. Cold reader: "arithmetic impressively clean," flagged $4,800 as unearned + repetitions. Hostile reviewer found four deep holes v3 never touched: the corrected Westlaw history now argued AGAINST the thesis (clients killed per-use billing — answered with the production-expense distinction); the missing "just reprice the rate card" option (answered with the 30× variance argument); Ebiquity quote conditional, not inevitable (re-anchored to AI entering contracts); team-member/camera metaphor war (resolved: "behaves like a colleague; commercially, it is equipment"). All fixed.

**Loop 3 — SHIP after small fixes (≈88 → 92/100).** Cold reader: READY WITH SMALL FIXES. Hostile: "fix items 1–3 and this ships without apology... the arithmetic spine is genuinely sound; I cross-checked every number and the boutique model survives intact." Final fixes applied: per-brief unit correction, Microsoft-owns-Copilot confound acknowledged ("a cheaper tool it happens to own"), 30× properly scoped, $288K reconciled vs Fed average (3× per head), fresh pull quote, TNW attribution.

**Open item for your call:** length. Final prose ≈ 3,520 words incl dek/standfirst (old draft measured 3,105 by the same script — its "2,230" was an undercount). Loop 3 reader suggested ~250–300 words of optional trim (boutique line items → chart, thin the S5 stat stack). Every addition was demanded by a review gate, so I shipped at this length rather than cut substance. Trim pass available on request.

---

## COMMITTEE v4 — TRIAL ASSESSMENT (vs v3)

What changed: 12 simulated voices × 5 passes in one context → **5 isolated gates, each a fresh agent with clean context + hard artifacts** (claim ledger, Python math audit, scripted language checks). Chair (main thread) judges between gates.

Why it worked, with evidence from this run:
1. **The adversarial verifier (never saw the article) found a fabricated statistic and citation laundering that survived two v3 loops.** Isolation removed the halo effect.
2. **True cold reads are now real.** Each loop's reader had genuinely never seen any draft — Loop 3's reader independently caught the $18-vs-$450 unit error that Loops 1–2 fix-writing introduced.
3. **The hostile reviewer escalated instead of converging.** Loop 2 found deeper holes than Loop 1 because it attacked a stronger draft with fresh eyes — the property v3 promised and never delivered.
4. **Scripted math caught everything mechanical** (16/16 then re-run each loop), freeing the agents for judgment.
5. Your diagnosis was right: fewer, deeper, independent seats beat many shallow simulated ones. The v3 checklists weren't discarded — they were absorbed into the gate prompts.

Not yet locked as canonical (your instruction: trial first). If you approve, I'll write committee_pipeline_v4.md to memory as the new standard.

---

## NEXT STEPS
1. Your read + verdict on `essay-10-FINAL-v2.md`
2. Optional 300-word trim pass
3. HTML rebuild (all changes mapped in the file's build notes: new boutique figures, 3 SVG updates, retitles, JSON-LD/FAQ updates)
4. Lock Committee v4 (or adjust)
5. Instagram carousels 09 + 10 (still pending from session plan)
