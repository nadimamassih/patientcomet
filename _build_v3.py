#!/usr/bin/env python3
# Essay-10 v3 rebuild: surgical region replacement. Run from the DEPLOY_10 folder.
import sys

PATH = 'essay-10.html'
data = open(PATH, encoding='utf-8').read()
orig = data

# ---------------- 1. HEAD METADATA ----------------
NEW_DESC = ("There is a fifth team member on every agency campaign now: the AI. "
            "It works the whole project, it costs the agency close to $3,000 a time, "
            "and it appears on no invoice anywhere. Clients are about to find out.")

old_meta = '<meta name="description" content="AI is on every brief, generating output around the clock. The compute costs are real. The invoices are blank. Here is the arithmetic agencies are avoiding.">'
assert old_meta in data
data = data.replace(old_meta, '<meta name="description" content="' + NEW_DESC + '">')

old_og = '<meta property="og:description" content="AI tools are on every brief, in every team, generating output around the clock. The compute costs are real. The invoices are blank.">'
assert old_og in data
data = data.replace(old_og, '<meta property="og:description" content="' + NEW_DESC + '">')

old_tw = '<meta name="twitter:description" content="AI tools are on every brief, in every team, generating output around the clock. The compute costs are real. The invoices are blank.">'
assert old_tw in data
data = data.replace(old_tw, '<meta name="twitter:description" content="' + NEW_DESC + '">')

old_ld_desc = '"description": "AI is on every brief, generating output around the clock. The compute costs are real. The invoices are blank. Here is the arithmetic agencies are avoiding."'
assert old_ld_desc in data
data = data.replace(old_ld_desc, '"description": "' + NEW_DESC + '"')

assert '"timeRequired": "PT10M"' in data
data = data.replace('"timeRequired": "PT10M"', '"timeRequired": "PT11M"')
assert '"dateModified": "2026-06-10"' in data
data = data.replace('"dateModified": "2026-06-10"', '"dateModified": "2026-06-11"')

# ---------------- 2. BODY REGION ----------------
START = '<article id="view-essay-10"'
END = '<section class="col block rv"><div class="refs"><div class="refs-hd"><div><div class="eyebrow" style="margin-bottom:6px">Keep reading'
i0 = data.index(START)
i1 = data.index(END)

DIV = '<div style="height:1px;background:var(--line);margin:0"></div>'

FAQ = ('<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":['
 '{"@type":"Question","name":"Should agencies bill clients for AI model costs?","acceptedAnswer":{"@type":"Answer","text":"Yes, for project-specific consumption (Type two costs). When a team runs agentic research sessions, generates hundreds of images, or renders video for a named client, those costs are attributable and belong in the proposal. Flat-rate subscriptions (Type one) are overhead and stay in the rate card."}},'
 '{"@type":"Question","name":"What is the difference between Type one and Type two AI costs?","acceptedAnswer":{"@type":"Answer","text":"Type one costs are flat-rate subscriptions (Claude Teams, Microsoft Copilot, ChatGPT Plus) that do not change with project complexity. They belong in agency overhead and the rate card. Type two costs are project-specific and variable: agentic research sessions, image generation runs, video rendering. They are consumed on behalf of a named client and belong in the client proposal. A subscription procured for a single campaign counts as Type two for that campaign."}},'
 '{"@type":"Question","name":"How much does AI compute cost on a typical agency project?","acceptedAnswer":{"@type":"Answer","text":"For a ten-person boutique agency on a three-month brand campaign, project-specific AI compute runs $2,861, which is 3.8 per cent of a $75,000 engagement. Standing AI subscriptions add a further $1,350 across the same quarter ($450 a month), but those are Type one overhead that belongs in the rate card and is shown separately, not on the project invoice. At a 25-person agency running sixty projects a year, unrecovered AI compute reaches $288,000 a year, around one-fifth of planned profit at a 20 per cent target margin on $7.2 million in billings."}},'
 '{"@type":"Question","name":"What is the Westlaw argument against billing AI costs, and why does it fail?","acceptedAnswer":{"@type":"Answer","text":"The Westlaw argument holds that AI tools, like legal research databases, will become flat-rate infrastructure absorbed into overhead. That is correct for Type one flat-rate subscriptions. It does not apply to Type two project-specific consumption, which works like the legal database before flat-rate contracts: real, variable, per-use costs attributable to specific client work."}}'
 ']}</script>')

HERO = ('<article id="view-essay-10" class="essay-standalone">' + FAQ + '''<div class="ah aD">
  <div class="grid">
    <div class="left">
      <div class="rubric">Patient Comet &middot; Strategy</div>
      <h1>The AI Team Member: Enthusiastic, Error-Prone, and <span class="it">Off Every Invoice</span></h1>
      <p class="dek">Agency campaign teams used to have four members. Now there is a fifth: the AI. It works the whole project, start to finish, it runs up close to $3,000 in costs every time, and it appears on no invoice anywhere. Clients are about to find out.</p>
      <div style="margin-top:26px"><div class="byl"><span class="av"><img src="pc-nadim.jpg" alt="Nadim A. Massih" onerror="this.remove()"></span><span class="t"><span class="nm">Nadim A. Massih</span><span class="mt">10 June 2026 &middot; 11 min read</span></span></div></div>
    </div>
    <div class="right"><img src="pc-hero-10.png" alt="Two professionals in a business meeting reviewing proposals and cost documents, representing the human team at the heart of agency work"></div>
  </div>
</div>''')

INTRO = '''<section id="e10-intro" class="col block rv">
<p class="lead"><span class="drop">I</span>n late 2025, Microsoft gave an AI coding assistant called Claude Code to thousands of its engineers. Five months later it cancelled most of the licences. The tools had become 98 per cent cheaper per use over three years, yet the heaviest users were still costing $500 to $2,000 a month each, because they were using them vastly more than anyone had planned. Advertising agencies now run the same kind of tools on every campaign. Microsoft could read its bill and act on it. Most agencies cannot even find theirs.</p>
<p>The brief lands on a Tuesday morning: a fashion retailer wants the full relaunch. New strategy, a new look, new advertising across every channel, twelve weeks to deliver. The director of the advertising agency builds the team on paper. A strategy lead. A senior designer. A copywriter. A project manager. Four people, their rates, their hours, and a $3,000 production budget with every photo licence accounted for. The proposal goes out at six that evening. The client signs.</p>
<p>By the end of week one a fifth member has joined the team, and it never clocks off. By the first coffee break each morning it has already researched the competition. Through weeks three and four it redrafts the campaign&#8217;s big idea fourteen times before the strategy lead settles on one. Twice it invents a competitor that does not exist. Twice the strategy lead catches it. By week nine it is recording test voiceovers for the brand film. On the morning of delivery it is still re-cutting social media videos. And all the while a meter is turning, because AI is not bought once like a camera. It charges as it is used, the way electricity does. Twelve weeks of work. $2,861 in computing costs on that meter. Almost exactly the size of the production budget the director wrote down so carefully.</p>
<p>It is not in the proposal. That missing line is the mistake quietly eating agency profits this decade.</p>
</section>'''

# -------- Boutique Arithmetic SVG (rebuilt, bar chart) --------
def bar_rows():
    items = [
        ("Claude Fable 5 research sessions", "25 agentic sessions &#215; ~$18 &#183; API overage", 450),
        ("Copy iteration", "Claude, running past the plan under revision pressure", 150),
        ("Midjourney Pro", "2 seats &#215; 3 months ($360) + fast-hour top-ups ($60)", 420),
        ("Sora 2 Pro video", "1,600 seconds generated @ $0.70 per second", 1120),
        ("Runway Gen-4", "social format adaptations", 225),
        ("Seedance 2.0", "motion content", 44),
        ("Higgsfield", "500 campaign images at published per-image rates", 117),
        ("ElevenLabs", "voice prototypes, including final-week redos", 30),
        ("Deck iteration", "Claude Sonnet 4.6 across three months", 305),
    ]
    out = []
    y0 = 64
    for n, (label, sub, val) in enumerate(items):
        y = y0 + n * 44
        w = round(val / 1120 * 380)
        out.append(f'  <text x="20" y="{y+12}" font-size="12.5" font-weight="600" fill="var(--ink)">{label}</text>')
        out.append(f'  <text x="20" y="{y+27}" font-size="9.5" fill="var(--ink-3)">{sub}</text>')
        out.append(f'  <rect x="350" y="{y+4}" width="{w}" height="14" rx="2" fill="var(--accent)" fill-opacity="{1 if val==1120 else 0.8}"/>')
        out.append(f'  <text x="{350+w+8}" y="{y+15}" font-size="11.5" font-weight="600" fill="var(--accent)">${val:,}</text>')
    return "\n".join(out)

BOUTIQUE_ARIA = ("Boutique arithmetic: project-specific AI compute on a 75,000 dollar engagement. "
 "Claude Fable 5 research sessions, 25 sessions at about 18 dollars each, 450 dollars. Copy iteration 150 dollars. "
 "Midjourney Pro, two seats at 360 dollars plus fast-hour top-ups at 60 dollars, 420 dollars. "
 "Sora 2 Pro, 1,600 seconds at 70 cents per second, 1,120 dollars. Runway Gen-4 225 dollars. Seedance 2.0 44 dollars. "
 "Higgsfield 500 images 117 dollars. ElevenLabs 30 dollars. Deck iteration through Claude Sonnet 4.6, 305 dollars. "
 "Total project-specific 2,861 dollars, 3.8 per cent of the engagement. "
 "Standing subscriptions shown separately: 450 dollars a month, 1,350 dollars across the quarter, recovered through the rate card.")

BOUTIQUE = ('<div class="ah diag" style="margin:32px 0;padding:28px 28px 24px">\n'
 '<div class="dt">The Boutique Arithmetic</div>\n'
 '<svg viewBox="0 0 820 600" xmlns="http://www.w3.org/2000/svg" font-family="Sora,sans-serif" role="img" aria-label="' + BOUTIQUE_ARIA + '" style="width:100%;height:auto;display:block">\n'
 '  <text x="20" y="22" font-size="11" fill="var(--ink-3)">$2,861 project-specific &#183; 3.8% of engagement &#183; standing subscriptions shown separately below</text>\n'
 '  <line x1="20" y1="36" x2="800" y2="36" stroke="var(--line)" stroke-width="1"/>\n'
 + bar_rows() + '\n'
 '  <line x1="20" y1="466" x2="800" y2="466" stroke="var(--line-2)" stroke-width="1.2"/>\n'
 '  <text x="20" y="494" font-size="10.5" font-weight="700" letter-spacing=".14em" fill="var(--ink-3)">TOTAL PROJECT-SPECIFIC</text>\n'
 '  <text x="350" y="500" font-size="24" font-weight="700" fill="var(--accent)">$2,861</text>\n'
 '  <text x="460" y="497" font-size="11.5" fill="var(--ink-2)">= 3.8% of the $75,000 engagement</text>\n'
 '  <rect x="20" y="516" width="780" height="72" rx="4" fill="rgba(159,178,255,0.08)" stroke="var(--violet)" stroke-width="0.9"/>\n'
 '  <text x="38" y="538" font-size="9.5" font-weight="700" letter-spacing=".14em" fill="var(--violet)">STANDING SUBSCRIPTIONS &#183; TYPE ONE &#183; RATE CARD, NOT THIS TOTAL</text>\n'
 '  <text x="38" y="556" font-size="11" fill="var(--ink-2)">Claude Teams (10 staff) $300/month &#183; Copilot Business (5 seats) $90/month &#183; ChatGPT Plus (3 staff) $60/month</text>\n'
 '  <text x="38" y="574" font-size="11" fill="var(--ink-2)">= $450/month &#183; $1,350 across the quarter, recovered through the rate card</text>\n'
 '</svg>\n</div>')

S1 = '''<section id="e10-s1" class="col block rv">
<h2>The Meter That <span class="it">Doesn&#8217;t Stop</span></h2>
<p>To see why the meter runs so hot, start with the most public AI advert ever made. When Kalshi (a prediction market platform where people bet on real-world events) aired an AI-generated commercial during the NBA Finals in June 2025, the team behind it generated roughly 400 video clips to find 15 it could broadcast. A 3.75 per cent yield. Everything else was money spent discovering what did not work.</p>
<p>That gap between what gets generated and what gets delivered is where the cost lives. Professional teams do far better than 3.75 per cent: with experienced people choosing and discarding at every stage, a team typically generates 1,600 seconds of footage to deliver 400 finished seconds. One second in four survives. The other three are the cost of finding the one. Any budget priced only on delivered seconds ignores everything it took to get there.</p>
<p>The problem is built into how the tools are sold. A photographer&#8217;s day rate is fixed. A software licence is fixed. AI compute, the computing power consumed every time the tool generates something, is variable: the price of one usable output depends on how many attempts it took to find the one worth keeping. Nor is this a quirk of video. Lightrun (a software engineering tools company) surveyed engineers in 2026 and found that 43 per cent of AI-generated code changes need human debugging once they reach production, even after passing every automated test.</p>
<p>So the failure rate is not a quality disclaimer. It is a cost driver. Every failed generation is compute already spent. The retry is compute spent again. The revision round is a third pass. A budget that counts only the final output is paying for all three without saying so. That arithmetic is what made Microsoft blink, as the technology news site The Next Web reported: the licences were cancelled not because the tools failed, but because nobody had decided who owns a meter that never stops.</p>
''' + BOUTIQUE + '''
<p>Here is what that meter looks like on one project.</p>
<p>A ten-person boutique agency. A three-month brand campaign. The proposal totals $75,000, and most of it is people: 60 hours of strategy direction at $450 an hour, 90 hours of senior design at $280, 60 hours of copy at $220, and 30 hours of account and project management at $220. That is $72,000. The last $3,000 is the production budget: stock imagery, music licensing, font licences. Every dollar is itemised, and the client can audit every line.</p>
<p>There is a second production budget on this campaign. It appears nowhere.</p>
<p>It starts with strategy research: 25 agentic sessions through Claude Fable 5 (Anthropic&#8217;s 2026 flagship model) to produce three client-ready briefs. Agentic means the AI works through multi-step research on its own, without being prompted at each step. Each session runs two to three hours and costs about $18, and that billing lands as API overage: the Claude Teams plan covers everyday usage, and sessions like these exhaust its allocation early. The 25 sessions come to $450. Copy iteration running past the plan under revision pressure adds $150.</p>
<p>Then the visuals: Midjourney Pro seats for two designers at $60 per user per month across three months, $360, plus $60 in fast-hour top-ups, the extra processing time Midjourney sells when the monthly allocation runs out during crunch weeks. An agency that already has Midjourney on its rate card, the standard price list it bills from, carries only the top-ups. One procuring it for this campaign carries the full $420.</p>
<p>The video stack is project-specific no matter what the agency already subscribes to, because no standing plan absorbs meaningful video generation volume. The production team generates 1,600 seconds of Sora 2 Pro footage to deliver 400 finished seconds of film and social content: $1,120. Runway Gen-4 for social format adaptations: $225. Seedance 2.0 (ByteDance&#8217;s video model) for motion content: $44. Higgsfield (an AI image generation platform) for 500 campaign images at published per-image rates: $117. ElevenLabs voice prototypes, including the redos that always happen in the final week: $30. Deck iteration through Claude Sonnet 4.6 across three months: $305.</p>
<p>Total project-specific AI compute: $2,861. The second production budget, line by line. Every dollar of it ran on behalf of this one client. One of the two budgets is itemised and recoverable. The other does not exist on paper.</p>
<p>The standing subscriptions run in parallel: Claude Teams for ten staff at $300 a month, Microsoft Copilot Business for five seats at $90, ChatGPT Plus for three staff at $60. That is $450 a month, $1,350 across the campaign, and it is true overhead. It belongs in the rate card, and the rate card is how it gets recovered. The $2,861 has no such home. It is 3.8 per cent of the whole engagement, consumed for a named client, and invisible to them.</p>
<p>If those overage lines look pessimistic, the industry&#8217;s own data says otherwise. Zylo (a firm that tracks company software spending) found in its 2026 SaaS Management Index that 78 per cent of IT leaders reported unexpected charges from consumption-based AI pricing in the past year. Not outliers. The majority. ServiceNow&#8217;s chief information officer, Kellie Romack, disclosed that the company burned through its full-year Anthropic coding budget in the first months of 2026, joining Uber in the same admission. Deadline compression, revision rounds and parallel generation runs are not exceptional events. They are the last two weeks of every project.</p>
<p>Now scale it. Five concurrent projects, the standard operating state for a boutique, put unrecovered AI spend at just under $5,000 a month. A 25-person agency running sixty projects a year, where a typical brief carries a second video deliverable and roughly twice the research load, lands near $4,800 per project. Across sixty projects, that is $288,000 a year. For an agency billing $7.2 million on a typical 20 per cent target margin, that is one-fifth of the year&#8217;s planned profit, absorbed without a single client conversation.</p>
'''

# -------- Cross-industry table SVG: reuse rows, new attributions --------
tbl_start = orig.index('<figure class="pc-figure" style="margin:var(--gap-xl) 0"><svg viewBox="0 0 720 620"')
tbl_end = orig.index('</figure>', tbl_start) + len('</figure>')
TABLE = orig[tbl_start:tbl_end]

old_sub = '<text x="18" y="60" font-size="9" fill="var(--ink-3)">2026 real costs + 2027&#8211;2028 agentic scenario &#183; Lower bound = 4&#8211;6&#215; governed agentic; upper bound = 10&#8211;15&#215; uncapped pipelines. Source: arXiv:2604.22750</text>'
assert old_sub in TABLE
TABLE = TABLE.replace(old_sub, '<text x="18" y="60" font-size="9" fill="var(--ink-3)">2026 actuals + 2027&#8211;2028 Patient Comet projection built on published usage trajectories &#183; flat-rate subscriptions excluded</text>')

old_src = TABLE[TABLE.index('<text x="18" y="549"'):TABLE.index('</text>', TABLE.index('<text x="18" y="549"')) + 7]
TABLE = TABLE.replace(old_src, '<text x="18" y="549" font-size="8" fill="var(--ink-3)"><tspan font-weight="600">Sources:</tspan> API pricing: Anthropic, OpenAI, Runway ML, ByteDance/fal.ai, Midjourney, ElevenLabs, Higgsfield AI. Federal Reserve Bank of Atlanta, May 2026. Jellyfish engineering analytics via TechCrunch, June 2026. EY agentic task cost analysis, 2026. Stanford RegLab legal AI accuracy study (2024).</text>')

old_method = TABLE[TABLE.index('<text x="18" y="577"'):TABLE.index('</text>', TABLE.index('<text x="18" y="577"')) + 7]
TABLE = TABLE.replace(old_method, '<text x="18" y="577" font-size="8" fill="var(--ink-4)"><tspan font-weight="600">2027&#8211;2028 method:</tspan> Patient Comet projection built on published usage trajectories: Jellyfish per-engineer token growth (18.6&#215; in nine months, via TechCrunch) and EY agentic task costs ($0.04&#8594;$1.20). Lower bound assumes governed pipelines; upper bound uncapped agentic use. Healthcare/Education capped by regulation.</text>')

old_caption = TABLE[TABLE.index('<figcaption>'):TABLE.index('</figcaption>') + len('</figcaption>')]
TABLE = TABLE.replace(old_caption, '<figcaption>Monthly AI compute per professional knowledge worker. The 2026 columns are current actuals; the 2027&#8211;2028 columns are a Patient Comet projection built on published usage trajectories (Jellyfish per-engineer growth, EY agentic task costs). Lower bound assumes governed pipelines; upper bound assumes uncapped agentic use. Flat-rate subscriptions excluded; every figure is project-specific consumption only.</figcaption>')

old_aria_tbl = 'aria-label="Monthly AI compute cost per professional knowledge worker across ten industries, 2026 to 2028, in US dollars. Software engineering highest at 350 to 880 dollars per month in 2026, rising to 2500 to 12000 by 2028 under agentic scenario. Education lowest at 90 to 220 dollars in 2026, rising to 180 to 500. Cross-industry average 170 dollars per month."'
assert old_aria_tbl in TABLE
TABLE = TABLE.replace(old_aria_tbl, 'aria-label="Monthly AI compute cost per professional knowledge worker across ten industries, 2026 to 2028, in US dollars. Software engineering highest at 350 to 880 dollars per month in 2026, rising to 2,500 to 12,000 by 2028 in a Patient Comet projection built on published usage trajectories. Education lowest at 90 to 220 dollars in 2026, rising to 180 to 500. Lower bound assumes governed pipelines, upper bound uncapped agentic use. Flat-rate subscriptions excluded."')

S1 = S1 + TABLE + '''
<p>The arithmetic repeats across every sector in that table. The tool names change by industry. The billing gap does not.</p>
</section>'''

# -------- Type one vs Type two SVG --------
TYPES_ARIA = ("Left column: Type one flat-rate subscriptions including Claude Teams 30 dollars per user per month, "
 "Microsoft Copilot 18 to 30 dollars per seat by tier, ChatGPT Plus 20 dollars per month. Fixed cost, 450 dollars a month here, "
 "1,350 dollars across the quarter. These are overhead, belonging in the rate card. Right column: Type two project-specific "
 "consumption including Claude Fable 5 research sessions, Midjourney image runs, Sora and ElevenLabs production. Variable, "
 "consumed on behalf of a named client: 2,861 dollars on this campaign. These are project costs belonging in the proposal.")

TYPES = ('<div class="ah diag" style="margin:32px 0;padding:28px 28px 24px" aria-label="Type one versus Type two AI costs comparison">\n'
 '<div class="dt">Two Types of AI Cost</div>\n'
 '<svg viewBox="0 0 820 260" xmlns="http://www.w3.org/2000/svg" font-family="Sora,sans-serif" role="img" aria-label="' + TYPES_ARIA + '" style="width:100%;height:auto;display:block">\n'
 '''  <!-- Type 1 card -->
  <rect x="20" y="20" width="370" height="220" rx="6" fill="var(--card)" stroke="var(--violet)" stroke-width="1.5" opacity="0.9"/>
  <text x="205" y="48" text-anchor="middle" font-size="10" font-weight="700" letter-spacing="0.18em" fill="var(--violet)">TYPE ONE: FLAT-RATE SUBSCRIPTIONS</text>
  <line x1="40" y1="58" x2="370" y2="58" stroke="var(--violet)" stroke-width="0.5" opacity="0.4"/>
  <text x="40" y="82" font-size="13" fill="var(--ink)">Claude Teams</text><text x="370" y="82" text-anchor="end" font-size="13" fill="var(--ink-3)">$30 / user / month</text>
  <text x="40" y="108" font-size="13" fill="var(--ink)">Microsoft Copilot</text><text x="370" y="108" text-anchor="end" font-size="13" fill="var(--ink-3)">$18&#8211;30 / seat by tier</text>
  <text x="40" y="134" font-size="13" fill="var(--ink)">ChatGPT Plus</text><text x="370" y="134" text-anchor="end" font-size="13" fill="var(--ink-3)">$20 / month</text>
  <line x1="40" y1="152" x2="370" y2="152" stroke="var(--line)" stroke-width="0.6"/>
  <text x="205" y="176" text-anchor="middle" font-size="11" fill="var(--ink-3)">Fixed. $450/month here &#183; $1,350 across the quarter.</text>
  <rect x="55" y="190" width="300" height="32" rx="4" fill="rgba(159,178,255,0.12)"/>
  <text x="205" y="211" text-anchor="middle" font-size="11" font-weight="600" fill="var(--violet)">Overhead &#8594; belongs in your rate card</text>

  <!-- Type 2 card -->
  <rect x="430" y="20" width="370" height="220" rx="6" fill="var(--card)" stroke="var(--accent)" stroke-width="1.8" opacity="0.95"/>
  <text x="615" y="48" text-anchor="middle" font-size="10" font-weight="700" letter-spacing="0.18em" fill="var(--accent)">TYPE TWO: PROJECT-SPECIFIC CONSUMPTION</text>
  <line x1="450" y1="58" x2="780" y2="58" stroke="var(--accent)" stroke-width="0.5" opacity="0.4"/>
  <text x="450" y="82" font-size="13" fill="var(--ink)">Claude Fable 5 research sessions</text><text x="780" y="82" text-anchor="end" font-size="13" fill="var(--ink-3)">per session</text>
  <text x="450" y="108" font-size="13" fill="var(--ink)">Midjourney image generation</text><text x="780" y="108" text-anchor="end" font-size="13" fill="var(--ink-3)">per image run</text>
  <text x="450" y="134" font-size="13" fill="var(--ink)">Sora / ElevenLabs production</text><text x="780" y="134" text-anchor="end" font-size="13" fill="var(--ink-3)">per second / per character</text>
  <line x1="450" y1="152" x2="780" y2="152" stroke="var(--line)" stroke-width="0.6"/>
  <text x="615" y="176" text-anchor="middle" font-size="11" fill="var(--ink-3)">Variable. Consumed for a named client: $2,861 this campaign.</text>
  <rect x="465" y="190" width="300" height="32" rx="4" fill="rgba(103,224,196,0.12)"/>
  <text x="615" y="211" text-anchor="middle" font-size="11" font-weight="600" fill="var(--accent)">Project cost &#8594; belongs in the proposal</text>
</svg>
</div>''')

S2 = '''<section id="e10-s2" class="col block rv">
<h2>The Two Costs You Are <span class="it">Treating as One</span></h2>
<p>A gap this large, repeated this widely, raises an obvious question: why is nobody billing for it? The most common answer is a history lesson, and it comes from the legal profession.</p>
<p>In the 1990s, law firms billed clients for legal database research line by line; Westlaw and LexisNexis charges passed straight through to the client file. Flat-rate contracts spread through the 2000s, and after the 2008 recession clients began refusing the line item altogether: 97 per cent of firms still passed research costs on in 2008, 73 per cent by 2011, and within a few years firms were absorbing roughly half of those costs themselves. The lesson the industry drew: research tools end up in the overhead column, the general running costs no client pays for directly. AI, the argument goes, will follow the same path and disappear from client invoices.</p>
<p>This argument is half right. The half it misses is where the money goes.</p>
''' + TYPES + '''
<p>Two types of AI cost are running at the same time in every agency, and the industry is treating them as one.</p>
<p><strong>Type one: flat-rate subscriptions.</strong> A Claude Teams licence at $30 per user per month. A Microsoft Copilot (Microsoft&#8217;s AI assistant) seat at $18 to $30 depending on tier. A ChatGPT Plus plan at $20. These costs do not change based on how complex any individual project is. They are infrastructure, exactly like the legal database contract. They belong in the rate card.</p>
<p><strong>Type two: project-specific consumption.</strong> When a strategy team runs a three-hour agentic session for a named client&#8217;s brief, that compute was consumed on behalf of that client. When a production team renders eight minutes of video for one campaign, the per-second cost is exact and traceable. One boundary rule keeps the categories clean: a subscription procured for a single campaign is Type two for that campaign; if the agency keeps it afterwards, it moves to the rate card.</p>
<p>Type two is not the legal database after the flat-rate contract. It is the database before it: real, variable, per-use costs that belong in the client budget. Every firm treating Type two as flat overhead has mistaken infrastructure for project cost.</p>
<p>Read the legal story again with that split in mind and it makes the same point. What clients killed was a fee that looked identical on every invoice whatever the matter: Type one&#8217;s profile exactly. What they have never killed is the production expense. The stock library, the location fee, the photography day rate all still sit on invoices, because each one maps to a deliverable the client can point at. Type two has that shape. The 1,600 seconds of generated footage map to this campaign&#8217;s film and to nothing else.</p>
<p>And the legal profession&#8217;s own story has a sting in its tail. In 2024, Stanford&#8217;s RegLab (its regulation and technology research lab) tested the AI research assistants that Westlaw and LexisNexis now sell on top of those classic databases. Westlaw&#8217;s AI was accurate on 42 per cent of queries. LexisNexis&#8217;s did better at 65 per cent. Both numbers mean the same thing: most AI-generated legal analysis still needs human verification before it reaches a client. The tool whose history is used to argue that AI becomes invisible overhead now ships an AI layer that, in Westlaw&#8217;s case, fails more often than it succeeds. That verification runs on someone&#8217;s account. The question is whether it appears in the proposal.</p>
</section>'''

S3 = '''<section id="e10-s3" class="col block rv">
<h2>Why More AI Means <span class="it">More Judgment, Not Less</span></h2>
<p>There is a reason agencies flinch from that question, and it is not only the fear of looking expensive next to a rival that bills nothing. Underneath sits a sharper fear: if the machine now does this much of the work, perhaps the people are worth less, and putting the machine on the invoice only advertises it.</p>
<p>The numbers say the opposite. The yield rates from the meter section are not evidence of a failing tool. They are a description of the job. The professional running AI is not doing less work. They are reviewing more outputs, making more judgment calls about which ones are worth developing, and closing the gap between what AI produces and what a client can actually use. That is not automation. It is skilled editorial work performed at a volume that was not possible before.</p>
<p>Research confirms the size of that gap. BetterUp Labs (the research arm of the BetterUp employee development platform) published a study with Stanford University in the Harvard Business Review in September 2025: 41 per cent of professionals had received AI output requiring significant rework in the prior month, and each instance took almost two hours to fix. That rework is not optional, and it is not running itself.</p>
<p>Which is why one distinction settles the fear. The fifth presence on that Tuesday brief behaves like a colleague. Commercially, it is equipment. A film production company renting cinema-grade cameras does not absorb the rental into the director of photography&#8217;s day rate. The camera is the cost of delivering work to that standard. The director is the value. Neither is optional, and the rental goes in the client budget because it was consumed on behalf of that client&#8217;s production.</p>
<p>AI model costs follow the same logic. The strategist is not the AI, and the judgment that filters the AI&#8217;s output has never been worth more. So the open question is not whether that judgment deserves its rate. It is who pays for the tools it runs on. And on that question, the industry has already split in two.</p>
</section>'''

S4 = '''<section id="e10-s4" class="col block rv">
<h2>The Agencies That Already <span class="it">Bill for AI</span></h2>
<p>In March 2026, Digiday (a publication covering the marketing industry) asked media houses, creative agencies, production shops and consultants how they handle AI compute costs. The answers split cleanly.</p>
<p>On one side, the agencies already billing. Full-service agency Merge meters AI costs and bills them per project on a case-by-case basis. Production company Big Spaceship treats compute like catering or equipment hire; its chief executive, Taryn Crouthers, put it directly: &#8220;We&#8217;re treating it similar to a production cost.&#8221; Lerma/ (a Dallas agency that styles its name with the slash) charges AI token costs as a transparent line item, no different from other project expenses. Tokens are the base unit AI uses to measure work, roughly one word of text per token. Pencil (the AI marketing platform owned by marketing services group Brandtech) charges generation credits: one per image, one per second of video.</p>
<p>On the other side, the agencies absorbing everything. Chris Neff, global chief AI officer at creative agency Anomaly, named the fear behind that choice: &#8220;It feels like a money grab.&#8221;</p>
<p>Sit with that fear for a moment and three objections emerge, each harder to answer than the last. The first is administrative: nobody wants to send a client an invoice with a $44 line for motion content. Nobody has to. Production expenses have always rolled up; no agency itemises gaffer tape. One AI production line in the proposal, backed by a metered report if the client asks for one, is exactly how the agencies above are handling it.</p>
<p>The second is the tempting middle path: skip the line item and quietly fold 4 per cent into next year&#8217;s blended rates. It feels safer. It also misprices every project on the books, because AI intensity varies enormously between briefs, and even the same task can swing thirty-fold in token use from one run to the next. A rate set in January is chasing a curve that, on the latest engineering data, multiplied eighteen times in nine months. Burying a cost this variable in a flat rate is not recovering it. It is guessing.</p>
<p>The third objection cuts deepest, because transparency runs both ways. Each of the boutique&#8217;s client-ready briefs took roughly eight agentic sessions, call it $150 of compute, against $450 for a single afternoon of the junior research time a brief like this used to swallow. Show a client those numbers side by side and a hard-nosed procurement team will ask why the research line still exists at all. The honest answer: it survives wherever a human must be accountable for what the brief claims, and it shrinks where one need not be. That repricing is coming either way, and a price move an agency leads reads as efficiency, while one an auditor forces reads as concealment. The discarded generations invite the same scrutiny: why should a client fund the 1,200 seconds that never made the film? They always have. Photography shoots bill the full day, not the eleven frames that made the campaign. Selects have outtakes. The ratio is the craft.</p>
<p>That scrutiny is coming whether agencies invite it or not, because AI is entering the contracts. Lerma/ already line-items tokens. Pencil bills by generation credit. Once contracts start naming AI, procurement templates learn to ask about it everywhere, and Ruben Schreurs, chief executive of marketing analytics consultancy Ebiquity, has already told Digiday how that ends: clients will audit agency AI usage the way they audit media spending today. &#8220;If it&#8217;s part of the contract, then yes, we&#8217;d audit that.&#8221; The agencies that meter first get to answer the procurement question with their own numbers, on their own framing. The agencies that chose silence will have it answered for them, by an auditor, with no goodwill in the room.</p>
</section>'''

PQ = '<div class="pq rv"><p>&#8220;The camera was never free. The agency just stopped sending the bill.&#8221;</p></div>'

THREE_ARIA = ("Three models of AI billing. Model one, cost passthrough, happening now: AI compute as a transparent line item in proposals, at cost. "
 "Model two, capability packaging, live since June 2025: Globant AI Pods at approximately 20,000 dollars per month, bundling 100 million tokens with dedicated human experts. "
 "Model three, outcome pricing, where the market heads: premium rates that build AI capability into the deliverable itself.")

THREE = ('<div class="ah diag" style="margin:32px 0;padding:28px 28px 24px" aria-label="Three models of AI billing in professional services">\n'
 '<div class="dt">Three Models of AI Billing</div>\n'
 '<svg viewBox="0 0 820 170" xmlns="http://www.w3.org/2000/svg" font-family="Sora,sans-serif" role="img" aria-label="' + THREE_ARIA + '" style="width:100%;height:auto;display:block">\n'
 '''  <!-- Model 1 -->
  <rect x="20" y="30" width="230" height="110" rx="6" fill="var(--card)" stroke="var(--accent)" stroke-width="1.8"/>
  <text x="135" y="56" text-anchor="middle" font-size="10" font-weight="700" letter-spacing="0.16em" fill="var(--accent)">NOW</text>
  <text x="135" y="82" text-anchor="middle" font-size="16" font-weight="600" fill="var(--ink)">Cost Passthrough</text>
  <text x="135" y="102" text-anchor="middle" font-size="10.5" fill="var(--ink-3)">AI compute as a line item</text>
  <text x="135" y="118" text-anchor="middle" font-size="10.5" fill="var(--ink-3)">in proposals, at cost</text>

  <!-- Arrow 1 -->
  <line x1="258" y1="85" x2="286" y2="85" stroke="var(--line-2)" stroke-width="1.8"/>
  <polygon points="286,80 296,85 286,90" fill="var(--line-2)"/>

  <!-- Model 2 -->
  <rect x="300" y="30" width="220" height="110" rx="6" fill="var(--card)" stroke="var(--violet)" stroke-width="1.5"/>
  <text x="410" y="56" text-anchor="middle" font-size="9" font-weight="700" letter-spacing="0.14em" fill="var(--violet)">LIVE SINCE JUNE 2025</text>
  <text x="410" y="82" text-anchor="middle" font-size="16" font-weight="600" fill="var(--ink)">Capability Packaging</text>
  <text x="410" y="102" text-anchor="middle" font-size="10.5" fill="var(--ink-3)">Globant AI Pods: ~$20K/month,</text>
  <text x="410" y="118" text-anchor="middle" font-size="10.5" fill="var(--ink-3)">100M tokens + human experts</text>

  <!-- Arrow 2 -->
  <line x1="528" y1="85" x2="556" y2="85" stroke="var(--line-2)" stroke-width="1.8"/>
  <polygon points="556,80 566,85 556,90" fill="var(--line-2)"/>

  <!-- Model 3 -->
  <rect x="570" y="30" width="230" height="110" rx="6" fill="var(--card)" stroke="var(--line)" stroke-width="1.2"/>
  <text x="685" y="56" text-anchor="middle" font-size="9" font-weight="700" letter-spacing="0.14em" fill="var(--ink-3)">WHERE THE MARKET HEADS</text>
  <text x="685" y="82" text-anchor="middle" font-size="16" font-weight="600" fill="var(--ink)">Outcome Pricing</text>
  <text x="685" y="102" text-anchor="middle" font-size="10.5" fill="var(--ink-3)">Premium rates build AI capability</text>
  <text x="685" y="118" text-anchor="middle" font-size="10.5" fill="var(--ink-3)">into the deliverable itself</text>
</svg>
</div>''')

S5 = '''<section id="e10-s5" class="col block rv">
<h2>Cheaper Models, <span class="it">Bigger Bills</span></h2>
<p>Every argument for silence rests, in the end, on one hope: that the cost is melting. Models improve, prices keep falling, so why build billing machinery around a problem that will shrink on its own? The research says the problem is growing instead.</p>
<p>In April 2026, researchers at Stanford and the University of Michigan, a team including the economist Erik Brynjolfsson, published a study of what AI agents actually cost when deployed at scale (arXiv:2604.22750). Two findings carry the argument. Agentic workflows consume up to 1,000 times more tokens than simple back-and-forth chat. And the same task can vary by up to 30 times in token consumption from one run to the next. The meter is not just running. It is unpredictable while it runs.</p>
<p>The usage data tells the same story at company level. Jellyfish (an engineering analytics firm) measured per-engineer AI token consumption rising 18.6 times in nine months as agentic tools became standard workflow, a figure reported by TechCrunch in June 2026. EY&#8217;s analysis of agentic task costs found that a single AI task that cost $0.04 in 2023 costs $1.20 in 2026, a 30-fold rise over the same years in which raw processing prices collapsed. That is why large companies&#8217; AI bills tripled even as efficiency gains were expected to shrink them: volume swallowed every saving. Bryan Catanzaro, Vice President of Applied Deep Learning at Nvidia, put it plainly in April 2026: &#8220;For my team, the cost of compute is far beyond the costs of the employees.&#8221;</p>
<p>Cheaper models do not mean smaller bills, because every price drop so far has been swallowed by appetite. When image generation got cheap, clients started expecting video. When chat got cheap, agencies started running three-hour agentic research sessions. Goldman Sachs projects 24-fold growth in total token consumption by 2030. The Federal Reserve Bank of Atlanta&#8217;s survey, published in May 2026, already puts AI spending in professional and business services at $3,470 per employee per year, around $289 a month. Set that average against the $500 to $2,000 a month of a heavy agentic engineer and the direction of travel is visible: agencies are migrating from the first group to the second, one workflow at a time. The 25-person agency absorbing $288,000 a year runs at roughly three times the Fed&#8217;s sector average per head, which is exactly where a generation-heavy shop should expect to sit. If agentic adoption spreads at anything like the rates the usage data shows, the average plausibly runs two to four times higher by 2028.</p>
<p>Which brings the story back to Microsoft. Its answer to its own runaway bill was to cancel the licences and move its engineers to a cheaper tool it happens to own. That is the luxury of owning the alternative. An agency holding a signed scope of work has no such exit. The film is due whether the meter ran hot or not. The only open question is who pays for it.</p>
''' + THREE + '''
<p>The market has already produced three answers. Cost passthrough: AI compute as a transparent line item in proposals, at cost, the way production expenses appear today. Capability packaging: live at the top of the market since June 2025, when digital services company Globant launched AI Pods at approximately $20,000 per month, bundling 100 million tokens with dedicated human experts who direct the work. And outcome pricing: premium rates that build AI capability into the deliverable itself, which is where the market heads once packaging is normal. These are not distant phases. They are a ladder, and the firms on the upper rungs started climbing from the first one.</p>
<p>The agencies that skip the first rung do not arrive at the third with stronger margins. They arrive having absorbed years of compute silently, having set no commercial precedent with clients, and having trained the market to expect AI as a free inclusion. The conversation starts in the next proposal. Or it starts in the next audit, on someone else&#8217;s terms.</p>
</section>'''

S6 = '''<section id="e10-s6" class="col block rv">
<h2>Where <span class="it">to Start</span></h2>
<p>If it is going to start in the next proposal, it starts with four moves.</p>
<p><strong>Separate your AI costs by type first.</strong> Flat-rate subscriptions are overhead. They go in the rate, not the proposal. Consumption-based production costs are project costs. These include Claude research sessions, image runs above plan allocations, Sora or Runway video seconds, and ElevenLabs voice prototypes. They belong in the brief.</p>
<p><strong>Track what you spend on a project before you decide what to bill.</strong> You cannot have a pricing conversation without a number. Run one project end-to-end with full AI cost visibility: what gets consumed, what it costs, what fraction of engagement value it represents. The number will either validate your instinct or surprise you.</p>
<p><strong>Frame it as production transparency, not a surcharge.</strong> AI production costs belong in the same section of the proposal as software licences, photography, and motion graphics rendering. It is the cost of the tools your team used to produce the work. That is a different conversation from adding a new fee.</p>
<p><strong>Start with one client you trust.</strong> Not a new pitch. Not every project. One existing relationship where you can have an honest conversation about what your team deployed and what it cost. The agencies already doing this are not losing that client. They are having a better commercial conversation with them.</p>
<p>The AI team member was on Tuesday&#8217;s brief. It will be on Monday&#8217;s. The only thing that changes is the proposal.</p>
</section>'''

# -------- Sources (17 entries) --------
refs = [
 ("Kalshi: The NBA Finals AI Commercial (June 2025)",
  "Kalshi aired an AI-generated commercial during the NBA Finals in June 2025. Roughly 400 Veo 3 generations produced 15 broadcast-usable clips, a 3.75 per cent yield. Reported by AdMonsters and NPR, June 2025. Source for the generation-to-delivery yield argument in Section 1."),
 ("Lightrun: State of AI-Powered Engineering Report (2026)",
  "Lightrun (2026). State of AI-Powered Engineering Report. Key finding: 43 per cent of AI-generated code changes require manual debugging in production, even after passing QA. Reported by VentureBeat and GlobeNewswire, April 2026."),
 ("Stanford RegLab: Legal AI Accuracy Study",
  "Stanford RegLab (2024; peer-reviewed in the Journal of Empirical Legal Studies, 2025). Westlaw AI-Assisted Research accurate on 42 per cent of queries; Lexis+ AI on 65 per cent. Source for the legal AI verification argument in Section 2."),
 ("HBR / BetterUp Labs / Stanford: The Rework Study",
  "BetterUp Labs and Stanford University (September 2025). <em>Harvard Business Review</em>. Key findings: 41 per cent of professionals received AI output requiring significant rework in the prior month; average rework time 1 hour 56 minutes per instance."),
 ("arXiv:2604.22750: AI Agent Cost Study",
  "Stanford University and the University of Michigan, including Brynjolfsson, Mihalcea and Pentland (24 April 2026). arXiv:2604.22750. Key findings used here: agentic workflows consume up to 1,000 times more tokens than chat, and the same task varies up to 30 times in token consumption across runs."),
 ("Jellyfish / TechCrunch: Agentic Consumption Benchmark",
  "Jellyfish engineering analytics, reported by TechCrunch (June 2026): per-engineer AI token consumption increased 18.6 times in nine months as agentic tools entered mainstream workflows. The Next Web (2026): enterprise AI bills tripled despite an estimated 98 per cent token price reduction."),
 ("EY: Agentic Task Cost Analysis (2026)",
  "EY analysis of agentic task costs (2026): a single agentic AI task that cost $0.04 in 2023 costs $1.20 in 2026, a 30-fold rise over the same period in which raw processing prices collapsed."),
 ("Microsoft: Claude Code Licence Cancellation (2026)",
  "Microsoft cancelled the majority of its Claude Code licences in May to June 2026, five months after rollout, with per-engineer costs running $500 to $2,000 a month across major deployments. Reported by The Next Web, Windows Central, Enterprise DNA and OpenTools."),
 ("Uber: AI Budget Exhaustion (2026)",
  "Uber consumed its full annual AI coding tools budget by April 2026 and introduced spending caps. Reported by TechCrunch, June 2026."),
 ("Nvidia: Bryan Catanzaro on Compute Costs",
  "Catanzaro, B., Vice President of Applied Deep Learning at Nvidia (April 2026): &#8220;For my team, the cost of compute is far beyond the costs of the employees.&#8221; Reported by Fortune and Axios."),
 ("Goldman Sachs: Token Consumption to 2030",
  "Goldman Sachs Research (2026). Projection of 24-fold growth in total token consumption by 2030. Used as a direction-of-travel figure in Section 5, not a near-term operational number."),
 ("Federal Reserve Bank of Atlanta: AI Spend per Employee",
  "Federal Reserve Bank of Atlanta macroblog (6 May 2026). Planned 2026 AI spending in professional and business services: $3,470 per employee per year, around $289 a month. Benchmark used to reconcile the 25-person agency scenario in Section 5."),
 ("Digiday: Agencies and the AI Token Economy",
  "Bradley, S. (3 March 2026). &#8220;Agencies grapple with economics of a new marketing currency: the AI token.&#8221; Digiday. Named practices: Merge, Big Spaceship (Taryn Crouthers), Lerma/, Pencil/Brandtech. Chris Neff (Anomaly): &#8220;It feels like a money grab.&#8221; Ruben Schreurs (Ebiquity) on client AI audits."),
 ("Globant AI Pods: Capability Packaging (June 2025)",
  "Globant (5 June 2025). AI Pods launch: subscription model bundling approximately 100 million tokens for approximately $20,000 per month with dedicated human supervision. Globant investor release. The live example of capability packaging in Section 5."),
 ("Zylo: 2026 SaaS Management Index",
  "Zylo (January 2026). 2026 SaaS Management Index. Key finding: 78 per cent of IT leaders reported unexpected charges from consumption-based AI pricing in the past year; average enterprise AI spend reached $1.2 million. Primary source for the overage-is-the-norm argument in Section 1."),
 ("ServiceNow: CIO Budget Disclosure (2026)",
  "Romack, K. (2026). ServiceNow CIO Kellie Romack disclosed that the company burned through its full annual Anthropic coding budget in the first months of 2026, joining Uber in the same admission. Reported by multiple outlets, June 2026."),
 ("Platform Pricing (verified June 2026)",
  "Anthropic: Claude Fable 5 at $10 per million input tokens and $50 per million output tokens (launched 9 June 2026); Claude Teams at $30 per user per month. Microsoft Copilot Business: $18 per seat per month promotional ($21 standard; Enterprise $30). ChatGPT Plus: $20 per month. Midjourney Pro: $60 per user per month. OpenAI Sora 2 Pro: $0.70 per second at 1080p. Runway Gen-4: $0.12 per second. ByteDance Seedance 2.0: approximately $0.24 per second (fast tier, 720p, via fal.ai). Higgsfield: approximately $0.23 per image at published per-call rates. ElevenLabs: $0.12 to $0.30 per 1,000 characters depending on tier."),
 ("Boutique Arithmetic: Assumptions",
  "Illustrative calculation at verified June 2026 platform rates. Claude agentic sessions: 25 sessions at roughly $18 each at Fable 5 API rates (a two-to-three-hour session consumes roughly 1.25M input and 125K output tokens). Midjourney Pro: $60 per user per month, two users, three months, plus $60 in fast-hour top-ups. Sora 2 Pro: 1,600 seconds at $0.70. Higgsfield: 500 images at published per-call rates. Project-specific total $2,861 equals 3.8 per cent of the $75,000 engagement; standing subscriptions ($450 a month, $1,350 a quarter) are Type one overhead, shown separately."),
]
ref_html = []
for title, body in refs:
    ref_html.append('<div class="ref"><div class="rs">' + title + '</div><p>' + body + '</p></div>')

SOURCES = ('<section class="col block rv"><div class="refs"><div class="refs-hd"><div><div class="eyebrow" style="margin-bottom:6px">Receipts</div>'
 '<h2 style="font-size:clamp(26px,3.4vw,38px)">Sources &amp; <span class="it">references</span></h2></div>'
 '<div class="refs-nav"><button class="rprev" aria-label="Previous">&#8249;</button><button class="rnext" aria-label="Next">&#8250;</button></div></div><div class="refs-rail">\n'
 + "\n".join(ref_html) + '\n</div></div></section>')

NEW_REGION = (HERO + '\n\n' + DIV + '\n\n' + INTRO + '\n\n' + DIV + '\n\n' + S1 + '\n\n' + DIV + '\n\n'
 + S2 + '\n\n' + S3 + '\n\n' + S4 + '\n\n' + PQ + '\n\n' + S5 + '\n\n' + S6 + '\n\n' + SOURCES)

data = data[:i0] + NEW_REGION + data[i1:]

open(PATH, 'w', encoding='utf-8').write(data)
print('OK: wrote', PATH, len(data), 'bytes (was', len(orig), ')')
