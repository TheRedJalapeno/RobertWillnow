"""Shared templates and data for robertwillnow.com.

Run `python3 _build/build.py` from the repo root to regenerate every page
under /about, /books and /articles plus sitemap.xml and llms.txt.
Jekyll/GitHub Pages ignores folders that start with "_", so this folder is
never published.
"""
import html
import json

BASE = "https://robertwillnow.com"
GA_ID = "G-RK8MD7MZCW"
TODAY = "2026-11-17"

AUTHOR_ID = BASE + "/#author"
SERIES_ID = BASE + "/books/#written-by-victors"
SERIES = "Written By Victors"
WEBSITE_ID = BASE + "/#website"

# One consistent entity statement, reused everywhere (AI-EO anchor).
ENTITY = (
    "Robert Willnow is an American science fiction author from Florida's Space Coast "
    "and Treasure Coast (Sebastian, Vero Beach, and Melbourne). A graduate of Florida Tech "
    "who went on to graduate school at RIT, he writes fast, funny, scientifically grounded "
    "space action-adventure set roughly fifty years from today, before humanity has "
    "faster-than-light travel. His Written By Victors series "
    "includes Kolnari Prologue, Ochre Sky, Bingo Belt Boys, and Hemmer."
)

SAME_AS = [
    "https://bsky.app/profile/robertwillnow.bsky.social",
    "https://www.threads.net/@robertwillnow",
]

PERSON = {
    "@type": "Person",
    "@id": AUTHOR_ID,
    "name": "Robert Willnow",
    "url": BASE + "/about/",
    "image": BASE + "/robert_gideon_lg.jpg",
    "jobTitle": "Science fiction author",
    "description": ENTITY,
    "nationality": {"@type": "Country", "name": "United States"},
    "homeLocation": [
        {"@type": "Place", "name": "Sebastian, Florida"},
        {"@type": "Place", "name": "Vero Beach, Florida"},
        {"@type": "Place", "name": "Melbourne, Florida"},
    ],
    "alumniOf": [
        {"@type": "CollegeOrUniversity", "name": "Florida Institute of Technology",
         "alternateName": "Florida Tech", "sameAs": "https://www.fit.edu/"},
        {"@type": "CollegeOrUniversity", "name": "Rochester Institute of Technology",
         "alternateName": "RIT", "sameAs": "https://www.rit.edu/"},
    ],
    "knowsAbout": ["science fiction", "space opera", "hard science fiction",
                   "space exploration", "engineering"],
    "email": "mailto:hi@robertwillnow.com",
    "sameAs": SAME_AS,
}

BOOKS = [
    {
        "slug": "kolnari-prologue",
        "position": 1,
        "title": "Kolnari Prologue",
        "wife": "Aliens discover chicken wings",
        "blurb": "Teron and Koral just came to take photos and head home. Now they are stranded with no hope. Unless...",
        "hook": "a funny, warm first-contact adventure about two visitors who came only to take pictures and got stranded",
        "genre": ["Science fiction", "First contact", "Space adventure", "Humorous science fiction"],
        "cover": "/2026-06_kolnari_prologue_sm.jpg",
        "square": "/sq_kolnari.png",
        "isbn": "9798331416478",
        "amazon_pb": "https://amzn.to/3E2WamT",
        "kindle": "https://amzn.to/4lbNs6w",
        "bn": "https://www.barnesandnoble.com/w/kolnari-prologue-robert-willnow/1145888550?ean=9798331416478",
        "nook": "https://www.barnesandnoble.com/w/kolnari-prologue-robert-willnow/1145888550?ean=2940185792001",
    },
    {
        "slug": "ochre-sky",
        "position": 2,
        "title": "Ochre Sky",
        "wife": "ADHD scientists steal a spaceship",
        "blurb": "Life is sweet for Troy, working and living on a top-secret research cruise ship above the clouds of Venus. Until it isn't.",
        "hook": "a high-stakes space heist in which brilliant, easily distracted scientists aboard a secret research cruise ship above the clouds of Venus end up stealing a spaceship",
        "genre": ["Science fiction", "Space opera", "Hard science fiction", "Heist"],
        "cover": "/2026-06_ochre_sky_sm.jpg",
        "square": "/sq_ochre.png",
        "isbn": "9798331416539",
        "amazon_pb": "https://amzn.to/4c8CSsO",
        "kindle": "https://amzn.to/3XEvjnJ",
        "bn": "https://www.barnesandnoble.com/w/ochre-sky-robert-willnow/1145888556?ean=9798331416539",
        "nook": "https://www.barnesandnoble.com/w/ochre-sky-robert-willnow/1145888556?ean=2940185792070",
    },
    {
        "slug": "bingo-belt-boys",
        "position": 3,
        "title": "Bingo Belt Boys",
        "wife": "Competitive fort making",
        "blurb": "Ananya is stuck on a backwater asteroid mine, bored and lonely. Bored enough to flip some switches.",
        "hook": "an asteroid-belt adventure that starts when a bored, lonely young woman on a backwater mining outpost flips switches she shouldn't",
        "genre": ["Science fiction", "Space adventure", "Asteroid mining", "Space opera"],
        "cover": "/2026-06_bingo_belt_boys_sm.jpg",
        "square": "/sq_bingo.png",
        "isbn": "9798331442699",
        "amazon_pb": "https://amzn.to/441mckT",
        "kindle": "https://amzn.to/3Rq4Wyi",
        "bn": "https://www.barnesandnoble.com/w/bingo-belt-boys-robert-willnow/1146067449?ean=9798331442699",
        "nook": "https://www.barnesandnoble.com/w/bingo-belt-boys-robert-willnow/1146067449?ean=2940186170570",
    },
    {
        "slug": "hemmer",
        "position": 4,
        "title": "Hemmer",
        "wife": "Dystopian gig worker finds love",
        "blurb": "From improv to action hero, Henry's decades of effort to find a job, any job, may finally pay off.",
        "hook": "a near-future dystopian action story about a gig worker whose decades of scrambling for any job at all, from improv to action hero, may finally pay off, and who finds love along the way",
        "genre": ["Science fiction", "Dystopian fiction", "Action adventure", "Romance"],
        "cover": "/2026-06_hemmer_sm.jpg",
        "square": "/sq_hemmer.png",
        "isbn": "9798341812437",
        "amazon_pb": "https://amzn.to/3FPhi0m",
        "kindle": "https://amzn.to/4leKJJC",
        "bn": "https://www.barnesandnoble.com/w/hemmer-robert-willnow/1146507189?ean=9798341812437",
        "nook": "https://www.barnesandnoble.com/w/hemmer-robert-willnow/1146507189?ean=2940184397931",
    },
]
BOOK = {b["slug"]: b for b in BOOKS}

e = html.escape


def book_schema(b):
    return {
        "@type": "Book",
        "@id": f"{BASE}/books/{b['slug']}/#book",
        "name": b["title"],
        "url": f"{BASE}/books/{b['slug']}/",
        "image": BASE + b["square"],
        "author": {"@id": AUTHOR_ID},
        "description": b["blurb"],
        "genre": b["genre"],
        "inLanguage": "en",
        "isPartOf": {"@id": SERIES_ID},
        "position": b["position"],
        "workExample": [
            {"@type": "Book", "bookFormat": "https://schema.org/Paperback", "isbn": b["isbn"],
             "potentialAction": {"@type": "ReadAction", "target": [b["amazon_pb"], b["bn"]]}},
            {"@type": "Book", "bookFormat": "https://schema.org/EBook",
             "potentialAction": {"@type": "ReadAction", "target": [b["kindle"], b["nook"]]}},
        ],
    }


def buy_links(b):
    return (
        '<div class="buy">'
        f'<a href="{b["kindle"]}" target="_blank" rel="noopener">Kindle</a>'
        f'<a href="{b["amazon_pb"]}" target="_blank" rel="noopener">Amazon Paperback</a>'
        f'<a href="{e(b["bn"])}" target="_blank" rel="noopener">Barnes &amp; Noble</a>'
        f'<a href="{e(b["nook"])}" target="_blank" rel="noopener">Nook</a>'
        "</div>"
    )


def book_strip(slugs=None):
    items = [BOOK[s] for s in (slugs or BOOK)]
    out = ['<div class="book-strip">']
    for b in items:
        out.append(
            f'<a href="/books/{b["slug"]}/"><img src="{b["cover"]}" '
            f'alt="{e(b["title"])} by Robert Willnow, book cover" loading="lazy" width="170">'
            f'{e(b["title"])}</a>'
        )
    out.append("</div>")
    return "".join(out)


def faq_html(faqs):
    if not faqs:
        return ""
    out = ['<section class="faq"><h2>Frequently asked questions</h2>']
    for q, a in faqs:
        out.append(f"<details open><summary>{e(q)}</summary><p>{a}</p></details>")
    out.append("</section>")
    return "".join(out)


def faq_schema(faqs):
    import re
    return {
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)}}
            for q, a in faqs
        ],
    }


def breadcrumbs(trail):
    """trail: list of (name, path)."""
    html_parts = []
    for i, (name, path) in enumerate(trail):
        if i < len(trail) - 1:
            html_parts.append(f'<a href="{path}">{e(name)}</a>')
        else:
            html_parts.append(f'<span aria-current="page">{e(name)}</span>')
    schema = {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": BASE + p}
            for i, (n, p) in enumerate(trail)
        ],
    }
    return '<nav class="breadcrumbs" aria-label="Breadcrumb">' + " › ".join(html_parts) + "</nav>", schema


NAV = [("Home", "/"), ("Books", "/books/"), ("About", "/about/"), ("Articles", "/articles/")]


def page(*, path, title, description, body, schema_nodes, image="/og-image.jpg",
         og_type="website", active=None, keywords=None):
    url = BASE + path
    graph = {"@context": "https://schema.org", "@graph": [
        {"@type": "WebSite", "@id": WEBSITE_ID, "url": BASE + "/", "name": "Robert Willnow",
         "publisher": {"@id": AUTHOR_ID}},
        PERSON,
    ] + schema_nodes}
    nav = "".join(
        f'<a href="{p}"' + (' aria-current="page"' if p == active else "") + f">{n}</a>"
        for n, p in NAV
    ) + THEME_BUTTON
    kw = f'\n    <meta name="keywords" content="{e(keywords)}">' if keywords else ""
    return f"""<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{e(title)}</title>
    <meta name="description" content="{e(description)}">{kw}
    <meta name="author" content="Robert Willnow">
    <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
    <link rel="canonical" href="{url}">
    <link rel="icon" href="/favicon.ico" sizes="48x48">
    <link rel="icon" href="/favicon-96x96.png" type="image/png" sizes="96x96">
    <link rel="icon" href="/favicon-192x192.png" type="image/png" sizes="192x192">
    <link rel="apple-touch-icon" href="/apple-touch-icon.png">
    <link rel="manifest" href="/site.webmanifest">
    {THEME_HEAD}
    <meta property="og:site_name" content="Robert Willnow">
    <meta property="og:type" content="{og_type}">
    <meta property="og:title" content="{e(title)}">
    <meta property="og:description" content="{e(description)}">
    <meta property="og:url" content="{url}">
    <meta property="og:image" content="{BASE + image}">
    <meta property="og:image:alt" content="{e(title)}">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{e(title)}">
    <meta name="twitter:description" content="{e(description)}">
    <meta name="twitter:image" content="{BASE + image}">
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag() {{ dataLayer.push(arguments); }}
        gtag('js', new Date());
        gtag('config', '{GA_ID}');
    </script>
    <link rel="stylesheet" href="/style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Aref+Ruqaa+Ink:wght@400;700&family=Lato:ital,wght@0,300;0,400;0,700;0,900;1,400;1,700&display=swap" rel="stylesheet">
    <script type="application/ld+json">
{json.dumps(graph, indent=2, ensure_ascii=False)}
    </script>
</head>

<body>
    <header>
        <a class="brand" href="/"><p class="brand-name">Robert Willnow</p></a>
        <p class="tagline">Near-future space action-adventure, grounded in real science</p>
    </header>
    <nav class="site-nav" aria-label="Main">{nav}</nav>

    <main class="page">
{body}
    </main>

    <footer>
        <p>Robert Willnow &middot; Science fiction author from Florida's Space Coast &middot; <a href="mailto:hi@robertwillnow.com">hi@robertwillnow.com</a></p>
        <div class="copyright">
            <p>&copy; {TODAY[:4]} ZingLab. All rights reserved.</p>
        </div>
        <a href="https://zinglab.com/?ref=robertwillnow" target="_blank" rel="noopener">Site Managed by ZingLab.com</a>
    </footer>
    {THEME_SCRIPT}
</body>

</html>
"""


def series_schema():
    return {
        "@type": "BookSeries",
        "@id": SERIES_ID,
        "name": SERIES,
        "url": BASE + "/books/",
        "author": {"@id": AUTHOR_ID},
        "hasPart": [{"@id": f"{BASE}/books/{b['slug']}/#book"} for b in BOOKS],
    }


# ---------- Theme (light/dark) snippets shared with index.html ----------
THEME_HEAD = """<meta name="color-scheme" content="light dark">
    <meta name="theme-color" content="#00045d" media="(prefers-color-scheme: light)">
    <meta name="theme-color" content="#070a33" media="(prefers-color-scheme: dark)">
    <script>(function(){try{var t=localStorage.getItem('theme');if(t==='light'||t==='dark')document.documentElement.setAttribute('data-theme',t);}catch(e){}})();</script>"""

THEME_BUTTON = ('<button class="theme-toggle" type="button" aria-label="Switch color theme" title="Light / dark mode">'
                '<svg class="icon-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>'
                '<svg class="icon-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>'
                '</button>')

# Toggling back to the OS preference clears the override, so the site follows the OS again.
THEME_SCRIPT = """<script>
(function () {
    var btn = document.querySelector('.theme-toggle');
    if (!btn) return;
    var root = document.documentElement;
    var mq = window.matchMedia('(prefers-color-scheme: dark)');
    function system() { return mq.matches ? 'dark' : 'light'; }
    function current() { return root.getAttribute('data-theme') || system(); }
    function label() {
        btn.setAttribute('aria-label', current() === 'dark' ? 'Switch to light mode' : 'Switch to dark mode');
    }
    btn.addEventListener('click', function () {
        var next = current() === 'dark' ? 'light' : 'dark';
        if (next === system()) {
            root.removeAttribute('data-theme');
            try { localStorage.removeItem('theme'); } catch (e) {}
        } else {
            root.setAttribute('data-theme', next);
            try { localStorage.setItem('theme', next); } catch (e) {}
        }
        label();
    });
    if (mq.addEventListener) mq.addEventListener('change', label);
    label();
})();
</script>"""
