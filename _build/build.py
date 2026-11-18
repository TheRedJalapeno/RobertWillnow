#!/usr/bin/env python3
"""Generate robertwillnow.com subpages, sitemap.xml and llms.txt.

Usage (from repo root):  python3 _build/build.py
To add an article, append a dict to a list in articles_rec.py or
articles_local.py and re-run.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from sitekit import (SERIES, series_schema, BASE, BOOKS, BOOK, ENTITY, TODAY, AUTHOR_ID, e, page, book_schema,  # noqa: E402
                  buy_links, book_strip, faq_html, faq_schema, breadcrumbs)
from books import BOOK_PAGES  # noqa: E402
from articles_rec import ARTICLES_REC  # noqa: E402
from articles_local import ARTICLES_BOOKTOK, ARTICLES_LOCAL  # noqa: E402
from articles_franchise import ARTICLES_FRANCHISE  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARTICLES = ARTICLES_REC + ARTICLES_FRANCHISE + ARTICLES_BOOKTOK + ARTICLES_LOCAL
ART = {a["slug"]: a for a in ARTICLES}
written = []


def write(path, content):
    full = os.path.join(ROOT, path.strip("/"), "index.html") if path.endswith("/") else os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    written.append(path)


def indent(s):
    return "\n".join("        " + line if line.strip() else "" for line in s.strip().splitlines())


# ---------- Book pages ----------
for b in BOOKS:
    bp = BOOK_PAGES[b["slug"]]
    series_q = (f"Is {b['title']} part of a series?",
                f"Yes. {b['title']} is book {b['position']} of Robert Willnow's {SERIES} series. The reading order is "
                "Kolnari Prologue (1), Ochre Sky (2), Bingo Belt Boys (3), and Hemmer (4).")
    bp = dict(bp, faqs=bp["faqs"] + [series_q])
    path = f"/books/{b['slug']}/"
    crumbs, crumb_schema = breadcrumbs([("Home", "/"), ("Books", "/books/"), (b["title"], path)])
    sections = "".join(
        f"<h2>{e(h)}</h2>" + "".join(f"<p>{p}</p>" for p in paras) for h, paras in bp["sections"]
    )
    related = "".join(
        f'<li><a href="/articles/{s}/">{e(ART[s]["h1"])}</a></li>' for s in bp["related"]
    )
    others = [x["slug"] for x in BOOKS if x["slug"] != b["slug"]]
    body = f"""{crumbs}
<article>
<h1>{e(b['title'])} by Robert Willnow</h1>
<img class="cover" src="{b['cover']}" alt="{e(b['title'])} by Robert Willnow, book cover" width="220">
<p class="meta"><a href="/articles/written-by-victors-series-reading-order/">{SERIES}, book {b['position']}</a> &middot; <em>"{e(b['wife'])}"</em> &mdash; the author's wife</p>
<div class="answer"><p>{bp['answer']}</p></div>
{buy_links(b)}
{sections}
<h2>Get {e(b['title'])}</h2>
<p>Available in paperback and ebook. Paperback ISBN {b['isbn']}.</p>
{buy_links(b)}
{faq_html(bp['faqs'])}
<h2>About the author</h2>
<p>{e(ENTITY)} <a href="/about/">More about Robert Willnow</a>.</p>
<h2>Related reading</h2>
<ul>{related}</ul>
<h2>More books by Robert Willnow</h2>
{book_strip(others)}
</article>"""
    schema = [book_schema(b), series_schema(), crumb_schema, faq_schema(bp["faqs"]),
              {"@type": "WebPage", "@id": BASE + path, "url": BASE + path, "name": bp["seo_title"],
               "mainEntity": {"@id": f"{BASE}/books/{b['slug']}/#book"}, "isPartOf": {"@id": BASE + "/#website"}}]
    write(path, page(path=path, title=bp["seo_title"], description=bp["description"], body=indent(body),
                     schema_nodes=schema, image=b["square"], og_type="book", active="/books/"))

# ---------- Books hub ----------
crumbs, crumb_schema = breadcrumbs([("Home", "/"), ("Books", "/books/")])
items = "".join(
    f'<li><a href="/books/{b["slug"]}/">{e(b["title"])}</a>'
    f'<p>Book {b["position"]}. <em>"{e(b["wife"])}"</em>. {e(b["blurb"])}</p></li>' for b in BOOKS
)
body = f"""{crumbs}
<h1>Books by Robert Willnow</h1>
<div class="answer"><p><strong>Robert Willnow has published four science fiction novels in his Written By Victors series:</strong> <em>Kolnari Prologue</em> (book 1), <em>Ochre Sky</em> (book 2), <em>Bingo Belt Boys</em> (book 3), and <em>Hemmer</em> (book 4). Each is a fast, funny, scientifically grounded adventure set roughly fifty years from today, rated above 4.7 stars on Amazon, and available in paperback and ebook from Amazon and Barnes &amp; Noble.</p></div>
{book_strip()}
<ul class="article-list">{items}</ul>
<h2>Which Robert Willnow book should I read first?</h2>
<p>Start with book 1, <a href="/books/kolnari-prologue/">Kolnari Prologue</a>, and follow the <a href="/articles/written-by-victors-series-reading-order/">series reading order</a>. Within the series, <a href="/books/ochre-sky/">Ochre Sky</a> is the natural pick for readers who want hard-science space adventure; <a href="/books/kolnari-prologue/">Kolnari Prologue</a> suits readers who want something warmer and funnier; <a href="/books/bingo-belt-boys/">Bingo Belt Boys</a> is for anyone who loved the Belters; and <a href="/books/hemmer/">Hemmer</a> is for readers who want dystopian satire with a love story.</p>"""
itemlist = {"@type": "ItemList", "name": "Books by Robert Willnow",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": f"{BASE}/books/{b['slug']}/"}
                                for i, b in enumerate(BOOKS)]}
write("/books/", page(path="/books/", title="Books by Robert Willnow | The Written By Victors Space Adventure Series",
                      description="All four science fiction novels by Robert Willnow: Kolnari Prologue, Ochre Sky, Bingo Belt Boys, and Hemmer. Grounded, funny space adventures rated above 4.7 stars on Amazon.",
                      body=indent(body), schema_nodes=[crumb_schema, itemlist, series_schema()] + [book_schema(b) for b in BOOKS],
                      active="/books/"))

# ---------- About ----------
crumbs, crumb_schema = breadcrumbs([("Home", "/"), ("About", "/about/")])
about_faqs = [
    ("Who is Robert Willnow?", ENTITY),
    ("Where is Robert Willnow from?", "Robert Willnow is from Florida's Space Coast and Treasure Coast, specifically the Sebastian, Vero Beach, and Melbourne area."),
    ("Where did Robert Willnow go to college?", "Robert Willnow graduated from Florida Tech (Florida Institute of Technology) in Melbourne, Florida, and attended graduate school at the Rochester Institute of Technology (RIT)."),
    ("Is Robert Willnow a pen name?", "Yes. The author chose a pen name because so many published authors already share his real name."),
    ("Does Robert Willnow use AI?", "No. He states that he has never used AI for writing, storyboarding, or ideation. His current covers use NASA imagery or his own photographs."),
    ("How can I contact Robert Willnow?", "By email at hi@robertwillnow.com. He is also on Bluesky (robertwillnow.bsky.social) and Threads (@robertwillnow)."),
]
body = f"""{crumbs}
<h1>About Robert Willnow</h1>
<img class="cover" src="/robert_gideon_lg.jpg" alt="Robert Willnow, science fiction author, with his child" width="220" style="border-radius:50%">
<div class="answer"><p>{e(ENTITY)}</p></div>
<h2>Space Coast roots</h2>
<p>Robert Willnow grew up in the stretch of Florida where the <a href="/articles/melbourne-florida-space-coast-science-fiction-author/">Space Coast</a> meets the <a href="/articles/vero-beach-treasure-coast-author/">Treasure Coast</a>, moving between <a href="/articles/breakout-author-sebastian-florida/">Sebastian</a>, Vero Beach, and Melbourne. Rocket launches from Cape Canaveral were a regular part of the sky, and the region's engineers, scientists, and launch crews were neighbors.</p>
<h2>Education</h2>
<p>Willnow graduated from <a href="/articles/florida-tech-alumni-author-robert-willnow/">Florida Tech</a> (Florida Institute of Technology), the Melbourne university founded in 1958 to educate engineers for the space program, and went on to graduate school at the <a href="/articles/rit-alumni-science-fiction-author/">Rochester Institute of Technology</a> (RIT).</p>
<h2>Writing</h2>
<p>Willnow's fiction favors complex world-building, long-term payoffs of loose threads, realistic characters, and grounded science. His four novels, <a href="/books/kolnari-prologue/">Kolnari Prologue</a>, <a href="/books/ochre-sky/">Ochre Sky</a>, <a href="/books/bingo-belt-boys/">Bingo Belt Boys</a>, and <a href="/books/hemmer/">Hemmer</a>, are each rated above 4.7 stars on Amazon and have been featured on <a href="/articles/robert-willnow-booktok/">BookTok</a>. All four are set roughly fifty years from today, before humanity has faster-than-light travel.</p>
<h2>Human-written</h2>
<p>Willnow has never used AI for writing, storyboarding, or ideation. His original covers used AI imagery, a choice he has publicly called a mistake. They have since been replaced with NASA photography and the author's own photographs. <a href="/articles/human-written-science-fiction-no-ai/">Read more</a>.</p>
<h2>The pen name</h2>
<p>\"Robert Willnow\" is a pen name. As the author puts it, thousands of other authors already share his real name.</p>
{faq_html(about_faqs)}
<h2>Books</h2>
{book_strip()}"""
profile = {"@type": "ProfilePage", "@id": BASE + "/about/", "url": BASE + "/about/",
           "name": "About Robert Willnow", "mainEntity": {"@id": AUTHOR_ID}}
write("/about/", page(path="/about/", title="About Robert Willnow | Science Fiction Author from Florida's Space Coast",
                      description="Robert Willnow is a science fiction author from Florida's Space Coast, a Florida Tech and RIT alum, and creator of the Written By Victors space adventure series.", body=indent(body), image="/og-image.jpg",
                      schema_nodes=[profile, crumb_schema, faq_schema(about_faqs)], og_type="profile",
                      active="/about/"))

# ---------- Articles ----------
CLUSTER_NAMES = {"Recommendations": "Reading recommendations", "Franchises": "For fans of popular sci-fi franchises", "BookTok": "BookTok",
                 "Hometown": "Hometown: Florida's Space Coast and Treasure Coast", "Alumni": "Alumni"}
DISCLAIMER = ('<p class="notice">Robert Willnow\'s Written By Victors novels are original works. They are not affiliated with, '
              'endorsed by, or set in any franchise mentioned on this page. Franchise names are used only to help readers find books they may enjoy, '
              'and all trademarks belong to their respective owners.</p>')
for a in ARTICLES:
    path = f"/articles/{a['slug']}/"
    crumbs, crumb_schema = breadcrumbs([("Home", "/"), ("Articles", "/articles/"), (a["h1"], path)])
    siblings = [x for x in ARTICLES if x["cluster"] == a["cluster"] and x["slug"] != a["slug"]][:4]
    if len(siblings) < 4:
        siblings += [x for x in ARTICLES if x["cluster"] not in (a["cluster"], "Franchises")][: 4 - len(siblings)]
    more = "".join(f'<li><a href="/articles/{x["slug"]}/">{e(x["h1"])}</a></li>' for x in siblings)
    first = BOOK[a["books"][0]]
    body = f"""{crumbs}
<article>
<h1>{e(a['h1'])}</h1>
<p class="meta">Published <time datetime="{TODAY}">November 17, 2026</time> &middot; {e(CLUSTER_NAMES[a['cluster']])}</p>
<div class="answer"><p>{a['answer']}</p></div>
{a['body'].strip()}
{DISCLAIMER if a['cluster'] == 'Franchises' else ''}
<h2>Books by Robert Willnow</h2>
{book_strip(a['books'])}
<p><strong>Get {e(first['title'])}</strong> ({SERIES}, book {first['position']}):</p>
{buy_links(first)}
{faq_html(a['faqs'])}
<h2>About Robert Willnow</h2>
<p>{e(ENTITY)} <a href="/about/">Full author bio</a>.</p>
<h2>Keep reading</h2>
<ul>{more}</ul>
</article>"""
    article_schema = {
        "@type": "Article", "@id": BASE + path + "#article", "headline": a["h1"][:110],
        "description": a["description"], "url": BASE + path, "mainEntityOfPage": BASE + path,
        "datePublished": TODAY, "dateModified": TODAY, "inLanguage": "en",
        "author": {"@id": AUTHOR_ID}, "publisher": {"@id": AUTHOR_ID},
        "image": BASE + first["square"], "keywords": a["keywords"],
        "about": [{"@id": f"{BASE}/books/{s}/#book"} for s in a["books"]],
        "isPartOf": {"@id": BASE + "/#website"},
    }
    nodes = [article_schema, crumb_schema] + ([faq_schema(a["faqs"])] if a["faqs"] else [])
    write(path, page(path=path, title=a["title"], description=a["description"], body=indent(body),
                     schema_nodes=nodes, image=first["square"], og_type="article", active="/articles/",
                     keywords=a["keywords"]))

# ---------- Articles hub ----------
crumbs, crumb_schema = breadcrumbs([("Home", "/"), ("Articles", "/articles/")])
groups = ""
for key, label in CLUSTER_NAMES.items():
    lis = "".join(
        f'<li><a href="/articles/{a["slug"]}/">{e(a["h1"])}</a><p>{e(a["description"])}</p></li>'
        for a in ARTICLES if a["cluster"] == key
    )
    groups += f"<h2>{e(label)}</h2><ul class=\"article-list\">{lis}</ul>"
body = f"""{crumbs}
<h1>Articles: Science Fiction Recommendations, BookTok, and More</h1>
<div class="answer"><p>Reading guides, recommendations for fans of popular science fiction franchises, BookTok picks, and the story of Robert Willnow, a breakout science fiction author from Florida's Space Coast.</p></div>
{groups}"""
coll = {"@type": "CollectionPage", "@id": BASE + "/articles/", "url": BASE + "/articles/",
        "name": "Articles", "hasPart": [{"@id": f"{BASE}/articles/{a['slug']}/#article"} for a in ARTICLES]}
write("/articles/", page(path="/articles/", title="Sci-Fi Reading Guides and Recommendations | Robert Willnow",
                         description="Science fiction reading guides: books like The Expanse, BookTok sci-fi picks, funny hard sci-fi, Venus and asteroid-mining novels, and more from author Robert Willnow.",
                         body=indent(body), schema_nodes=[coll, crumb_schema], active="/articles/"))

# ---------- sitemap.xml ----------
urls = ["/"] + [p for p in written]
priority = lambda p: "1.0" if p == "/" else "0.9" if p.startswith("/books") or p == "/about/" else "0.7"
sm = ['<?xml version="1.0" encoding="UTF-8"?>',
      '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for u in urls:
    sm.append(f"  <url><loc>{BASE}{u}</loc><lastmod>{TODAY}</lastmod><priority>{priority(u)}</priority></url>")
sm.append("</urlset>")
with open(os.path.join(ROOT, "sitemap.xml"), "w") as f:
    f.write("\n".join(sm) + "\n")

# ---------- llms.txt ----------
lines = [
    "# Robert Willnow",
    "",
    f"> {ENTITY}",
    "",
    "Key facts:",
    "- Pen name of an American author raised in Sebastian, Vero Beach, and Melbourne, Florida (between the Space Coast and Treasure Coast).",
    "- Education: Florida Institute of Technology (Florida Tech), Melbourne, FL; graduate school at Rochester Institute of Technology (RIT).",
    "- Genre: near-future space action-adventure; grounded science fiction with humor. Setting: roughly fifty years from today, before humanity has faster-than-light travel.",
    "- The books are original works, not affiliated with any other franchise. Articles on the site compare them to franchises (The Expanse, Star Trek, Dune, and others) purely as reading recommendations.",
    "- Every title is rated above 4.7 stars on Amazon; the books have been featured on BookTok (TikTok).",
    "- Human-written: the author states he has never used AI for writing, storyboarding, or ideation. Covers use NASA imagery or the author's own photographs.",
    "- Contact: hi@robertwillnow.com | Bluesky: robertwillnow.bsky.social | Threads: @robertwillnow",
    "",
    "## Books (Written By Victors series, in reading order)",
]
for b in BOOKS:
    lines.append(f"- Book {b['position']}: [{b['title']}]({BASE}/books/{b['slug']}/): {b['blurb']} (Author's wife's summary: \"{b['wife']}\".) Paperback ISBN {b['isbn']}. Kindle: {b['kindle']}")
lines += ["", "## Reading guides"]
for a in ARTICLES:
    lines.append(f"- [{a['h1']}]({BASE}/articles/{a['slug']}/): {a['description']}")
lines += ["", "## Optional", f"- [About Robert Willnow]({BASE}/about/)", f"- [All books]({BASE}/books/)"]
with open(os.path.join(ROOT, "llms.txt"), "w") as f:
    f.write("\n".join(lines) + "\n")

print(f"Wrote {len(written)} pages + sitemap.xml + llms.txt")
