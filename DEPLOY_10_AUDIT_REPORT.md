# Patient Comet — DEPLOY_10 Full Site Audit
**Date:** 11 June 2026 · **Base:** DEPLOY_9 → clean copy `PatientComet_v60_DEPLOY_10/`
**Scope:** code QA, SEO/GEO/AEO, consistency & cohesion, visual/UX QA, efficiency, link integrity (internal + all 77 external)

---

## 1. Fixed in DEPLOY_10 ✅

### Code errors (5 HTML parse errors → 0)
- **essay-05**: stray `</section>` after the Content Engine paragraph — removed
- **essay-06**: unclosed `<p>` (Judge Chesney paragraph ran into the next block) — closed
- **index**: same two errors in the embedded legacy views + a stray `</div>` in the essay-05 view TOC — all three fixed
- Post-fix: **all 11 pages parse clean**, verified headlessly at 390/768/1024/1440 px — no overflow, no JS errors

### Schema / JSON-LD (39 blocks of duplication removed)
- **index.html had 26 JSON-LD blocks**: the site-wide WebSite/ItemList/Person graph was injected **9×** and every article schema **2×** (with conflicting stale headlines, plus duplicate `id="schema-article-07/08"`). Removed 15 duplicates → **12 clean blocks**
- Every essay carried its BlogPosting + FAQPage **twice** (build artifact). Deduped all 10 essays → 3 blocks each (BlogPosting + BreadcrumbList + FAQPage), `keywords` merged into the kept block
- **essay-10 had no schema on the home page at all** — added its BlogPosting
- **ItemList** pointed to dead SPA anchors (`/#essay-01`…`/#essay-09`) and was missing essay-10 — rebuilt with all **10 real page URLs**, newest first

### SEO / GEO / AEO
- **sitemap.xml was missing essay-09 and essay-10** (the two newest articles were invisible to crawlers) — added, valid XML, 11 URLs
- **llms.txt was missing essays 09 + 10** — added in house format (10 articles listed)
- **Meta descriptions**: essay-05 trimmed 173→156 chars; essay-10 trimmed **289→155** chars (was nearly double the SERP limit) — OG/Twitter copies updated too

### Performance / efficiency
- **pc-hero-09.png (28.3 MB) → pc-hero-09.jpg (312 KB)**; **pc-home-09.png (28.6 MB) → pc-home-09.jpg (219 KB)**. ~56 MB → 0.5 MB; all 13 references (img src, og:image, twitter:image, JSON-LD) updated across every page. og:image for essay-09 was previously a 28 MB PNG — would fail most social scrapers
- **Inter font removed from the Google Fonts URL on all 11 pages** — loaded everywhere, used nowhere (one wasted render-blocking request per page)
- **Sora fallback fixed**: table styles declared `font-family:Sora` but Sora is never loaded (silently fell back to generic sans). Switched to Montserrat (the site's actual UI font) on all affected pages

### House rules
- **essay-09 had 6 em dashes in body prose** (em=0 rule). All replaced with parentheticals/commas/colons. Sweep confirms 0 prose em dashes remaining site-wide (alt-text/SVG label dashes untouched)

---

## 2. Round 2 — approved 11 June 2026, all done ✅

1. **Legacy SPA views stripped from index.html.** The 9 hidden `view-essay-XX` articles (full duplicate copies of essays 01–09) are gone: **631 KB → 172 KB (-73%)**. A small router shim now redirects any legacy `#essay-XX` hash link to the standalone `essay-XX.html` page (verified working headlessly). `#about` view and home behaviour unchanged. The essay-09 home schema was relocated out of the removed view and kept. Bonus: this exposed a pre-existing latent JS error (a filter script appending to a non-existent `#pc-art-tags` container) — now guarded; **zero page errors on every page**.

2. **3 broken/wrong citations fixed in essay-05** (body + Sources section):
   - **Heinz**: was "Heinz/Edelman, 2023 — two billion impressions, 25,000 personalised videos" with a dead Edelman link. Corrected to the verified facts: **Heinz/Rethink, 2022 A.I. Ketchup — 1.15 billion earned impressions, engagement 38% above past campaigns**, linked to The One Club award page. (The agency, year, link and both figures were wrong.)
   - **Omnicom–IPG**: dead constructed Reuters URL → verified live **Campaign Asia (Feb 2026)** article confirming the $13bn deal completed Nov 2025, 4,000 job cuts, $1.5bn doubled savings target, agency names retired. Body parenthetical updated too.
   - **ANA**: dead URL + wrong year ("Survey 2024") → real report: **"The Continued Rise of the In-House Agency: 2023 Edition"** (ana.net), which carries the exact 82%/78% figures cited.

3. **Leftover files deleted**: pc-hero-09.png + pc-home-09.png (28 MB originals), pc-hero-home-loop.mp4, pc-hero-about.jpg, .DS_Store. **Folder: 83 MB → 24 MB.**

**Final verification after round 2:** all 11 pages parse clean, all JSON-LD valid (essays 3 blocks, index 12), no missing assets, no duplicate IDs, no JS/console errors, no overflow at 390/1280, hash redirect works.

---

## 3. Still parked (tied to essay-10 rewrite approval) ⏸

1. **essay-10 title mismatch** — page says "The AI Team Member: Enthusiastic, Error-Prone, and Off Every Invoice"; home card says "The Invisible Invoice: The AI Team Member No One Charges For". Resolve when the pending rewrite lands.
2. **essay-10 is orphaned in Keep Reading** — no essay's rail links to it. Add after the title settles. There's also no `pc-home-10` thumbnail asset yet (home rail reuses pc-hero-10.png).

---

## 4. Verified healthy ✓

- **Visual QA**: headless render at 4 widths × all key pages — no horizontal overflow, no console/JS errors, heroes legible, mobile clean (before and after fixes)
- **Internal links**: every essay↔essay, essay↔home, and asset reference resolves; `index.html#about`/`#home` are live hash-router routes (not broken anchors)
- **External links**: 74 of 77 verified live (3 suspects above). All YouTube thumbnails point at live videos
- **Chrome consistency**: identical nav, footer, byline ("Nadim A. Massih") across all 11 pages; canonical URLs, OG, Twitter Cards present everywhere; titles follow the "Term: Plain subtitle" format
- **robots.txt**: all AI crawlers (GPTBot, PerplexityBot, Claude-Web, etc.) explicitly allowed; sitemap referenced
- **Note for content freshness**: the METR study cited in essay-07 now carries an on-page banner saying its results are superseded by METR's Feb 2026 update — worth a one-line acknowledgement at next content refresh

---

## File inventory
11 HTML pages · sitemap.xml (11 URLs) · robots.txt · llms.txt (10 articles) · 33 media assets.
DEPLOY_9 remains untouched. Excluded from the copy: nested DEPLOY_7 folder, essay-10 backups (.BACKUP/.bak_loop3), session handover, mockup PNGs.
