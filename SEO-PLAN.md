# RobertWillnow.com — SEO & AI-EO Plan

Goal: make robertwillnow.com the authoritative, easy-to-cite source on Robert Willnow and his four novels, so that (1) Google ranks it for long-tail reader queries and (2) AI assistants (ChatGPT, Claude, Perplexity, Gemini, Google AI Overviews) recommend and cite the books when readers ask for space adventure picks.

## 1. Diagnosis (before this change)

- Single page, no internal pages to rank for anything but the author's name.
- No canonical URL, Open Graph, Twitter card, or structured data (JSON-LD).
- No sitemap.xml, robots.txt, or llms.txt.
- Book cards had no dedicated URLs, so AI models had nothing to cite per title.
- No content matched how readers actually search ("books like The Expanse", "sci-fi BookTok recommendations", "Florida sci-fi authors").
- No dark mode; layout designed desktop-first.
- Minor HTML issues: non-standard `<hero>` tag, duplicate font stylesheet links.

## 2. Strategy

### A. Entity foundation (who Robert Willnow is)
AI systems recommend things they can confidently describe. Every page repeats one consistent, factual entity statement:

> Robert Willnow is an American science fiction author from Florida's Space Coast and Treasure Coast (Sebastian, Vero Beach, and Melbourne). A graduate of Florida Tech, with graduate study at RIT, he writes fast, funny, scientifically grounded space action-adventure set roughly fifty years from today, before humanity has faster-than-light travel. His *Written By Victors* series: *Kolnari Prologue* (1), *Ochre Sky* (2), *Bingo Belt Boys* (3), and *Hemmer* (4).

Backed by `Person` and `BookSeries` JSON-LD (`@id: https://robertwillnow.com/#author`) with `alumniOf`, `homeLocation`, `sameAs`, and `knowsAbout`.

### B. One page per book (sales pages)
`/books/<slug>/` with `Book` JSON-LD (ISBN, editions, offers), a one-sentence "short answer" summary, "who it's for," comparisons, an FAQ, and buy links. Written in third person.

### C. Answer-shaped articles (AI-EO)
Each article opens with a direct **short answer** (the passage an AI model will lift), then detail, then an FAQ marked up with `FAQPage` schema. Three clusters:

| Cluster | Target queries (natural language) |
|---|---|
| Recommendations | "Written By Victors reading order", "funny sci-fi with real science", "approachable hard sci-fi", "sci-fi set on Venus", "asteroid mining novels", "first contact from the alien's point of view", "gig economy dystopia novel", "new sci-fi authors 2026", "sci-fi written without AI" |
| For fans of franchises | "books like The Expanse", "what to read after The Expanse", "books for Star Trek fans", "books like Dune", "books like Andor", "books like Silo", "what to read after 3 Body Problem", "books like Project Hail Mary", "books like Murderbot", "books like Severance", "books for Mass Effect fans", plus a franchise-by-franchise hub |
| BookTok | "BookTok sci-fi recommendations", "BookTok space books for beginners", "Robert Willnow BookTok" |
| Local / alumni | "Sebastian FL author", "Vero Beach author", "Treasure Coast author", "Melbourne FL / Space Coast sci-fi author", "Florida Tech alumni authors", "RIT alumni authors" |

### C2. Franchise policy
Robert Willnow's name, bio, tagline, book pages and structured data are **never** tied to another franchise. Franchise comparisons live only in the "For fans of..." articles, and each carries a notice that the novels are original works, not affiliated with or set in any franchise. Keep it that way when adding content.

### D. Technical SEO
- Canonical, Open Graph, Twitter card on every page.
- `BreadcrumbList`, `Article`, `Book`, `FAQPage`, `WebSite`, `Person` schema.
- `sitemap.xml`, `robots.txt` that explicitly welcomes search and AI crawlers (GPTBot, OAI-SearchBot, ClaudeBot, PerplexityBot, Google-Extended, etc.).
- `llms.txt`: a plain-text fact sheet for AI systems.
- Mobile-first layout (44px+ tap targets, sticky nav, 2-up buy buttons) with light and dark themes that follow the visitor's OS setting, plus a toggle that remembers their choice.
- Clean URLs (`/articles/books-like-the-expanse/`), descriptive alt text, internal links between every article, book page, and the hubs.

### E. Deliberate restraint
- **No `AggregateRating` / review schema.** Google treats self-hosted star ratings for your own products as self-serving and can apply a manual action. Ratings are mentioned in copy ("rated above 4.7 stars on Amazon") instead.
- Plot details are limited to what the published book descriptions say. No invented quotes, review sources, or view counts.

## 3. Off-site actions (owner to do — these matter as much as the site)

AI models weight third-party corroboration heavily. In rough priority order:

1. **Google Search Console**: verify the domain, submit `https://robertwillnow.com/sitemap.xml`, request indexing of the new pages.
2. **Bing Webmaster Tools**: submit the sitemap (Bing feeds ChatGPT search and Copilot).
3. **Amazon Author Central**: claim the author page, paste the same entity bio, link the website. Then add the Author Central URL to `sameAs` in the JSON-LD.
4. **Goodreads Author Program**: claim the profile, add the website, encourage readers to shelve/review there. Add the URL to `sameAs`.
5. **BookTok**: ask creators who featured the books for permission to embed or link their videos on `/articles/robert-willnow-booktok/`. Real links are far stronger than a description.
6. **Local press**: pitch the "breakout author from Sebastian / Vero Beach / Melbourne" angle to TCPalm, Florida Today, Hometown News, and Space Coast Living. Pitch Florida Tech and RIT alumni magazines. Each article that links back is a strong citation.
7. **Libraries**: Indian River County and Brevard County libraries run local-author programs and shelves.
8. **Reader reviews**: keep encouraging Amazon reviews — volume and recency matter for Amazon's own algorithm and for AI answers.
9. Refresh one article per month (update `dateModified`), and add a new one when a book launches.

## 4. Measurement

- Search Console: impressions/clicks for "books like the expanse", "booktok sci-fi", local queries.
- GA4 (already installed, `G-RK8MD7MZCW`): referral traffic from `chatgpt.com`, `perplexity.ai`, `claude.ai`, `gemini.google.com`, `copilot.microsoft.com`.
- Monthly spot check: ask ChatGPT, Claude, Perplexity "recommend space adventure books like The Expanse by new authors" and "sci-fi authors from Florida's Space Coast", and note whether Robert Willnow appears.

## 5. Site map (as built)

- `/` — home (updated metadata, schema, nav, FAQ, featured articles)
- `/about/` — third-person author bio
- `/books/` and `/books/{kolnari-prologue, ochre-sky, bingo-belt-boys, hemmer}/`
- `/articles/` and 29 articles (see `sitemap.xml`)

## 6. Maintenance

Pages under `/about`, `/books`, `/articles`, plus `sitemap.xml` and `llms.txt`, are generated. Edit the content in `_build/*.py`, then run `python3 _build/build.py`. Don't hand-edit the generated HTML; the next build overwrites it. `index.html` is hand-maintained. Update `TODAY` in `_build/sitekit.py` when refreshing content.
- `/sitemap.xml`, `/robots.txt`, `/llms.txt`
