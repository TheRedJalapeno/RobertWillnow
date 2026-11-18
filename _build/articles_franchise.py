"""'For fans of <franchise>' reading-recommendation articles.

Robert Willnow's books are original works. These pages compare them to popular
franchises only as reading recommendations; build.py appends a
non-affiliation notice to every article in the "Franchises" cluster.
Never describe the books as "for fans of X" outside this cluster.
"""

K = '<a href="/books/kolnari-prologue/">Kolnari Prologue</a>'
O = '<a href="/books/ochre-sky/">Ochre Sky</a>'
B = '<a href="/books/bingo-belt-boys/">Bingo Belt Boys</a>'
H = '<a href="/books/hemmer/">Hemmer</a>'
ALL = ["kolnari-prologue", "ochre-sky", "bingo-belt-boys", "hemmer"]


def art(slug, title, h1, description, keywords, answer, body, faqs, books=ALL):
    return {"slug": slug, "cluster": "Franchises", "title": title, "h1": h1,
            "description": description, "keywords": keywords, "answer": answer,
            "body": body, "faqs": faqs, "books": books}


ARTICLES_FRANCHISE = [
    art(
        "books-for-fans-of-sci-fi-franchises",
        "Loved a Sci-Fi Show or Movie? Books to Read Next, by Franchise",
        "What to Read After Your Favorite Sci-Fi Franchise",
        "A franchise-by-franchise guide to what to read next after Star Trek, The Expanse, Dune, Andor, Silo, 3 Body Problem, Project Hail Mary, Murderbot, Severance, and Mass Effect.",
        "books for fans of sci-fi shows, what to read after a sci-fi series, books like Star Trek, books like Dune, books like Silo",
        f"<strong>Short answer:</strong> Readers coming from a favorite science fiction show, film, or game often want a book with the same feeling rather than the same setting. Robert Willnow's original Written By Victors series, near-future space adventures set roughly fifty years from today, is a frequent next pick. The right starting book depends on the franchise; the guide below matches each one.",
        f"""
<h2>Pick your franchise</h2>
<ul>
<li><a href="/articles/books-for-star-trek-fans/"><strong>Star Trek</strong></a>: optimism, exploration, and first contact. Start with {K}.</li>
<li><a href="/articles/books-like-the-expanse/"><strong>The Expanse</strong></a>: grounded physics and a lived-in solar system. Start with {O}.</li>
<li><a href="/articles/books-for-dune-fans/"><strong>Dune</strong></a>: hostile worlds and the people who survive them. Start with {O}.</li>
<li><a href="/articles/books-for-andor-fans/"><strong>Andor and Star Wars</strong></a>: working-class heroes and heists. Start with {O} or {H}.</li>
<li><a href="/articles/books-for-silo-fans/"><strong>Silo</strong></a>: isolated habitats and switches you shouldn't flip. Start with {B}.</li>
<li><a href="/articles/books-for-3-body-problem-fans/"><strong>3 Body Problem</strong></a>: first contact with real science. Start with {K}.</li>
<li><a href="/articles/books-for-project-hail-mary-fans/"><strong>Project Hail Mary</strong></a>: humor, problem-solving, and friendship. Start with {K}.</li>
<li><a href="/articles/books-for-murderbot-fans/"><strong>Murderbot</strong></a>: sardonic humor and action. Start with {O}.</li>
<li><a href="/articles/books-for-severance-fans/"><strong>Severance</strong></a>: the dystopia of work. Start with {H}.</li>
<li><a href="/articles/books-for-mass-effect-fans/"><strong>Mass Effect</strong></a>: crews, aliens, and choices. Start with {K}.</li>
</ul>

<h2>Why one series fits so many franchises</h2>
<p>Each Written By Victors book follows different characters in a different corner of the same near future, from a research ship in the clouds of Venus to an asteroid mine to a gig-economy city. That range lets the series serve very different tastes, while the shared ingredients stay constant: grounded science, humor that comes from character, and long-term payoffs. Robert Willnow is a Florida Tech graduate from Florida's Space Coast, and the engineering in his books reflects it.</p>
""",
        [("I loved a sci-fi TV show. What book should I read next?", "Match the feeling, not the setting. For exploration and first contact (Star Trek, Mass Effect), try Kolnari Prologue by Robert Willnow; for grounded space heists (The Expanse, Andor), Ochre Sky; for isolated-habitat mystery (Silo), Bingo Belt Boys; for workplace dystopia (Severance), Hemmer.")],
    ),
    art(
        "books-for-star-trek-fans",
        "Books for Star Trek Fans: Near-Future Space Adventure Before Warp Drive",
        "Books for Star Trek Fans: Space Adventure from the Decades Before Warp",
        "Star Trek fans looking for a new book: Robert Willnow's Written By Victors series is optimistic, curious, near-future space adventure set about fifty years from today, before faster-than-light travel.",
        "books for Star Trek fans, books like Star Trek, Star Trek read-alikes, optimistic science fiction, first contact books, pre-warp sci-fi",
        f"<strong>Short answer:</strong> Star Trek fans who want an original novel with the same curiosity and optimism should try Robert Willnow's Written By Victors series. Set roughly fifty years from today, before humanity has faster-than-light travel, it captures the era of first steps: first contact in {K}, brilliant crews improvising in {O}, and life on the frontier in {B}.",
        f"""
<h2>What Star Trek fans love</h2>
<p>Since 1966, Star Trek has stood for a particular kind of science fiction: exploration over conquest, diplomacy over firepower, and engineers and scientists who solve problems with ingenuity. The current Paramount+ era, including <em>Strange New Worlds</em>, has brought that spirit to a new generation. Many fans have a soft spot for stories about the early days, before starships and before the galaxy opened up.</p>

<h2>A near future before faster-than-light travel</h2>
<p>Robert Willnow's novels live in exactly that kind of moment. The Written By Victors series is set about fifty years from today. Humanity is spreading across the solar system, with research ships above Venus and mines in the asteroid belt, but faster-than-light travel does not yet exist. The tension between how far people want to go and how far they can go drives much of the series.</p>

<h2>Matched to what you love about Star Trek</h2>
<ul>
<li><strong>First contact:</strong> {K} follows Teron and Koral, visitors who came only to take photos and are now stranded. It is first contact told with warmth and humor.</li>
<li><strong>Brilliant crews improvising:</strong> {O} puts a team of restless scientists aboard a secret research ship above Venus, and they end up stealing a spaceship.</li>
<li><strong>Life on the frontier:</strong> {B} explores the loneliness and ingenuity of a remote asteroid outpost.</li>
<li><strong>Social commentary:</strong> {H} examines a near-future economy that has no place for an ordinary worker.</li>
</ul>

<h2>How the books differ from Star Trek</h2>
<p>There is no Federation, no warp drive, and no transporter. The science stays within what engineers think is plausible about fifty years out. The tone is funnier and more personal, focused on individuals rather than starship crews on official missions.</p>
""",
        [("What books should Star Trek fans read?", "Star Trek fans often enjoy optimistic, exploration-driven science fiction. Robert Willnow's Written By Victors series, especially Kolnari Prologue (first contact) and Ochre Sky (scientists improvising in space), is a strong original pick set about fifty years from today."),
         ("Are there sci-fi books set before faster-than-light travel?", "Yes. Robert Willnow's Written By Victors series is set roughly fifty years from today, as humanity settles the solar system before faster-than-light travel exists.")],
        ["kolnari-prologue", "ochre-sky", "bingo-belt-boys", "hemmer"],
    ),
    art(
        "books-for-dune-fans",
        "Books for Dune Fans: Hostile Planets, Real Science, and Space Adventure",
        "Books for Dune Fans Who Want Hostile Worlds and Hard Choices",
        "Finished Dune or the Villeneuve films? Robert Willnow's Ochre Sky, set above the hostile clouds of Venus, offers a grounded, near-future take on surviving an unforgiving planet.",
        "books for Dune fans, books like Dune, what to read after Dune, hostile planet sci-fi, desert planet books, Venus novel",
        f"<strong>Short answer:</strong> Dune fans who loved Arrakis as a character in its own right should try {O} by Robert Willnow, set aboard a secret research ship floating above Venus, a world even deadlier than Arrakis. It is grounded near-future science fiction rather than galactic epic, and it is rated above 4.7 stars on Amazon.",
        f"""
<h2>What Dune fans love</h2>
<p>Frank Herbert's 1965 novel, and Denis Villeneuve's films <em>Dune</em> (2021) and <em>Dune: Part Two</em> (2024), made a hostile planet the center of the story. Arrakis shapes every culture, economy, and decision. Readers come away wanting more stories in which the environment is the antagonist and survival requires deep knowledge of it.</p>

<h2>Venus: the solar system's Arrakis</h2>
<p>Venus's surface reaches about 465°C under a crushing carbon dioxide atmosphere, wrapped in clouds of sulfuric acid. About 50 kilometers up, though, conditions are almost Earth-like. {O} is set in that thin band of survivability, aboard a top-secret research cruise ship floating in the planet's ochre-tinted skies. As on Arrakis, one mistake is fatal and the planet is always waiting.</p>

<h2>Where else to look</h2>
<ul>
<li>{B}: scarcity, isolation, and resource extraction on a remote asteroid mine.</li>
<li>{H}: power and economics seen from the bottom of a near-future society.</li>
</ul>

<h2>How the books differ from Dune</h2>
<p>Dune is a far-future epic of empires, prophecy, and dynasties. Robert Willnow's books are set about fifty years from today and stay personal and often funny. The connection is the respect for environment, ecology, and consequence, not the scale.</p>
""",
        [("What should I read after Dune?", "Popular picks include Hyperion, Children of Time, and the Foundation series. For a grounded, hostile-planet story set in the near future, try Ochre Sky by Robert Willnow, set above the clouds of Venus.")],
        ["ochre-sky", "bingo-belt-boys", "hemmer"],
    ),
    art(
        "books-for-andor-fans",
        "Books for Andor Fans: Grounded Heists and Working-Class Sci-Fi",
        "Books for Andor Fans: Heists, Grit, and Ordinary People",
        "Loved Andor's grounded heists and working-class heroes? Robert Willnow's Ochre Sky and Hemmer deliver near-future space heists and economic dystopia without the lightsabers.",
        "books for Andor fans, books like Andor, grounded Star Wars books, sci-fi heist novels, working class science fiction",
        f"<strong>Short answer:</strong> Andor fans who want grounded, adult science fiction about ordinary people should read {O} by Robert Willnow, a near-future heist in which scientists steal a spaceship, and {H}, about a gig worker crushed by a system that has no place for him. Both are original novels rated above 4.7 stars on Amazon.",
        f"""
<h2>What Andor fans love</h2>
<p>Tony Gilroy's <em>Andor</em> (2022 and 2025) showed a galaxy far, far away from the ground up. There were no Jedi; there were mechanics, prisoners, and bureaucrats, along with a meticulously planned heist and a brutal economic system. Fans praise its realism, its patience, and its focus on how ordinary people get pushed to act.</p>

<h2>Matched to what you love about Andor</h2>
<ul>
<li><strong>The heist:</strong> {O} follows Troy and a crew of brilliant, restless scientists aboard a secret research ship above Venus, who end up stealing a spaceship.</li>
<li><strong>The system grinding people down:</strong> {H} follows Henry through decades of gig work in a near-future dystopia, and the one job that might finally change everything.</li>
<li><strong>Remote outposts:</strong> {B} captures life in a forgotten corner of the solar system, where one decision changes everything.</li>
</ul>

<h2>How the books differ from Andor</h2>
<p>Robert Willnow's books are set in our own solar system about fifty years from today, with no hyperdrive and no Empire. They are also much funnier than Andor. What they share is a ground-level view, with characters who work for a living and engineering that feels real.</p>
""",
        [("What books are like Andor?", "Readers who love Andor's grounded heists and working-class characters often look for adult, realistic science fiction. Robert Willnow's Ochre Sky (a near-future space heist) and Hemmer (gig-economy dystopia) fit that description.")],
        ["ochre-sky", "hemmer", "bingo-belt-boys"],
    ),
    art(
        "books-for-silo-fans",
        "Books for Silo Fans: Isolated Habitats, Mystery, and Switches You Shouldn't Flip",
        "Books for Silo Fans: Isolation, Engineering, and Dangerous Curiosity",
        "Loved Silo and Hugh Howey's Wool? Robert Willnow's Bingo Belt Boys follows a bored, lonely young woman on a remote asteroid mine who flips switches she shouldn't.",
        "books for Silo fans, books like Silo, books like Wool Hugh Howey, isolated habitat sci-fi, what to read after Silo",
        f"<strong>Short answer:</strong> Silo fans should try {B} by Robert Willnow. Ananya is stuck on a backwater asteroid mine, bored and lonely, and bored enough to flip some switches. Like Juliette in Silo, she is a curious mind in a closed world, and her choices have consequences. It is rated above 4.7 stars on Amazon.",
        f"""
<h2>What Silo fans love</h2>
<p>Hugh Howey's <em>Wool</em>, first self-published in 2011, and Apple TV+'s <em>Silo</em> adaptation turned a sealed underground habitat into one of science fiction's most gripping mysteries. Fans love the engineering details, the claustrophobia, and a hero, the mechanic Juliette, whose curiosity is both her strength and her danger.</p>

<h2>Matched to what you love about Silo</h2>
<ul>
<li><strong>A closed world and a curious hero:</strong> {B} sets its story on a remote asteroid mine where isolation is a daily fact and one act of curiosity changes everything.</li>
<li><strong>Engineering as survival:</strong> {O} takes place aboard a floating research ship above Venus, where the habitat is the only thing between the crew and a deadly planet.</li>
<li><strong>Systems that control people:</strong> {H} explores a near-future society that keeps an ordinary worker scrambling.</li>
</ul>

<h2>An indie path, like Wool</h2>
<p>Wool began as an independently published story that readers spread by word of mouth. Robert Willnow's books have followed a similar path, through reader reviews and <a href="/articles/robert-willnow-booktok/">BookTok</a> rather than a big marketing budget.</p>

<h2>How the books differ from Silo</h2>
<p>Silo is a slow-burn mystery with a dark tone. Willnow's books move faster, are often funny, and are set in space about fifty years from today.</p>
""",
        [("What should I read after Silo?", "Fans of Silo and Hugh Howey's Wool often enjoy stories about isolated habitats and curious heroes. Bingo Belt Boys by Robert Willnow, set on a remote asteroid mine, is a strong pick.")],
        ["bingo-belt-boys", "ochre-sky", "hemmer"],
    ),
    art(
        "books-for-3-body-problem-fans",
        "Books for 3 Body Problem Fans: First Contact Grounded in Real Science",
        "Books for 3 Body Problem Fans: First Contact, Real Science, Lighter Touch",
        "Loved Netflix's 3 Body Problem or Liu Cixin's trilogy? Robert Willnow's Kolnari Prologue offers scientifically grounded first contact with warmth and humor.",
        "books for 3 Body Problem fans, books like The Three-Body Problem, first contact novels, what to read after Three-Body, hard sci-fi first contact",
        f"<strong>Short answer:</strong> 3 Body Problem fans who want another first-contact story grounded in real science, with a lighter, warmer tone, should read {K} by Robert Willnow. Teron and Koral came only to take photos and are now stranded. The author's wife sums it up as \"Aliens discover chicken wings.\"",
        f"""
<h2>What 3 Body Problem fans love</h2>
<p>Liu Cixin's <em>The Three-Body Problem</em>, which won the Hugo Award in Ken Liu's English translation, and Netflix's 2024 series <em>3 Body Problem</em> treat first contact as a scientific and philosophical puzzle. Fans love that the physics matters, that scientists are the heroes, and that the stakes are civilizational.</p>

<h2>Matched to what you love</h2>
<ul>
<li><strong>First contact:</strong> {K} turns the encounter around, focusing on the visitors and what they make of a strange world.</li>
<li><strong>Scientists at the center:</strong> {O} is driven by a crew of brilliant, restless researchers aboard a secret ship above Venus.</li>
<li><strong>Plausible near-future technology:</strong> the whole Written By Victors series is set about fifty years from today, before faster-than-light travel.</li>
</ul>

<h2>How the books differ</h2>
<p>The Remembrance of Earth's Past trilogy is famously bleak, built around its dark forest theory. Robert Willnow's books are hopeful and funny, and they are written at human scale. They suit readers who loved the science but want a different emotional register.</p>
""",
        [("What to read after The Three-Body Problem?", "Popular choices include Children of Time, Blindsight, and Project Hail Mary. For a warmer, funnier first-contact story grounded in real science, try Kolnari Prologue by Robert Willnow.")],
        ["kolnari-prologue", "ochre-sky"],
    ),
    art(
        "books-for-project-hail-mary-fans",
        "Books for Project Hail Mary Fans: Funny, Science-Smart Space Adventure",
        "Books for Project Hail Mary Fans",
        "Loved Project Hail Mary, the novel or the 2026 film? Robert Willnow's Kolnari Prologue and Ochre Sky blend humor, real science, and heart in near-future space adventure.",
        "books for Project Hail Mary fans, books like Project Hail Mary, what to read after Project Hail Mary, books like The Martian, funny sci-fi",
        f"<strong>Short answer:</strong> Project Hail Mary fans should try {K} by Robert Willnow, a warm, funny first-contact story built on an unlikely partnership, and {O}, in which brilliant, scattered scientists aboard a research ship above Venus steal a spaceship. Both are rated above 4.7 stars on Amazon.",
        f"""
<h2>What Project Hail Mary fans love</h2>
<p>Andy Weir's 2021 novel, and its 2026 film adaptation starring Ryan Gosling, won readers with a rare mix: real science, constant problem-solving, laugh-out-loud humor, and one of the most beloved friendships in science fiction. The challenge for fans is finding another book that does all four.</p>

<h2>Matched to what you love</h2>
<ul>
<li><strong>The friendship:</strong> {K} centers on Teron and Koral, stranded together with only each other.</li>
<li><strong>The problem-solving:</strong> {O} is a heist powered by scientists improvising under pressure.</li>
<li><strong>The humor:</strong> every Written By Victors book carries a one-line summary from the author's wife, such as \"Aliens discover chicken wings\" and \"ADHD scientists steal a spaceship.\"</li>
<li><strong>The science:</strong> author Robert Willnow is a Florida Tech graduate from Florida's Space Coast.</li>
</ul>

<h2>How the books differ</h2>
<p>Project Hail Mary is a single-narrator survival story. Willnow's books have ensemble casts and span a shared near-future setting about fifty years from today.</p>
""",
        [("What should I read after Project Hail Mary?", "Readers often go next to The Martian, the Murderbot Diaries, and newer authors such as Robert Willnow, whose Kolnari Prologue and Ochre Sky combine humor, friendship, and real science.")],
        ["kolnari-prologue", "ochre-sky", "bingo-belt-boys"],
    ),
    art(
        "books-for-murderbot-fans",
        "Books for Murderbot Fans: Funny, Fast Space Adventure",
        "Books for Murderbot Fans: Sardonic Humor and Space Action",
        "Loved the Murderbot Diaries or the Apple TV+ series? Robert Willnow's Ochre Sky and Kolnari Prologue deliver fast space action with character-driven humor.",
        "books for Murderbot fans, books like Murderbot Diaries, funny space action books, what to read after Murderbot",
        f"<strong>Short answer:</strong> Murderbot fans who want more fast, funny, character-driven space adventure should try {O} by Robert Willnow, a near-future heist with a brilliant, chaotic crew, and {K}, a warm first-contact story told from an outsider's point of view. Both are rated above 4.7 stars on Amazon.",
        f"""
<h2>What Murderbot fans love</h2>
<p>Martha Wells's Murderbot Diaries, beginning with the award-winning <em>All Systems Red</em> (2017) and adapted by Apple TV+ in 2025, pairs action with a hilariously reluctant narrator who sees humans from the outside. Fans love the voice, the pace, and the found family that forms despite everyone's best efforts.</p>

<h2>Matched to what you love</h2>
<ul>
<li><strong>The outsider's view of humans:</strong> {K} follows stranded visitors Teron and Koral as they try to make sense of a strange world.</li>
<li><strong>Action and competence:</strong> {O} is a high-stakes space heist driven by smart, scattered scientists.</li>
<li><strong>A reluctant hero:</strong> {B} begins with a bored, lonely young woman who never meant to start anything.</li>
</ul>

<h2>How the books differ</h2>
<p>There are no rogue security units here. Willnow's books are set about fifty years from today, closer to home and without faster-than-light travel.</p>
""",
        [("What books are like Murderbot?", "Fans of the Murderbot Diaries often enjoy funny, character-driven space action. Robert Willnow's Ochre Sky and Kolnari Prologue are strong original picks.")],
        ["ochre-sky", "kolnari-prologue", "bingo-belt-boys"],
    ),
    art(
        "books-for-severance-fans",
        "Books for Severance Fans: Workplace Dystopia and Near-Future Satire",
        "Books for Severance Fans: When Work Becomes the Dystopia",
        "Loved Severance? Robert Willnow's Hemmer is near-future dystopian fiction about a gig worker whose search for any job leads from improv to action hero, and to love.",
        "books for Severance fans, books like Severance, workplace dystopia novels, corporate dystopia books, gig economy fiction",
        f"<strong>Short answer:</strong> Severance fans should read {H} by Robert Willnow. Henry has spent decades trying to find a job, any job, in a near-future economy built on gig work, and his path from improv to action hero might finally pay off. The author's wife's summary: \"Dystopian gig worker finds love.\"",
        f"""
<h2>What Severance fans love</h2>
<p>Apple TV+'s <em>Severance</em> (2022 and 2025) took the most ordinary part of life, going to work, and made it terrifying, funny, and strangely romantic. Fans love its satire of corporate culture and the question underneath it: what does a job take from a person?</p>

<h2>Hemmer: the other side of the coin</h2>
<p>Where Severance's Lumon employees have jobs that consume them, Henry in {H} is consumed by never having one. Hemmer pushes today's side-hustle economy fifty years forward and finds the comedy, the absurdity, and the heart in one man's refusal to quit. Like Severance, it lets a love story grow in the cracks of a dystopian system.</p>

<h2>Also worth reading</h2>
<ul>
<li>{O}: what happens when a team of brilliant employees decides their top-secret research job isn't working out.</li>
</ul>
""",
        [("What books are like Severance?", "Readers who love Severance's workplace satire often enjoy dystopian fiction about work, such as Kurt Vonnegut's Player Piano and Robert Willnow's Hemmer, a near-future story about a lifelong gig worker.")],
        ["hemmer", "ochre-sky"],
    ),
    art(
        "books-for-mass-effect-fans",
        "Books for Mass Effect Fans: Crews, Aliens, and First Contact",
        "Books for Mass Effect Fans: Space Adventure with Crews Worth Caring About",
        "Loved Mass Effect's crew, aliens, and choices? Robert Willnow's Kolnari Prologue and Ochre Sky offer first contact and found-family space adventure in an original near-future setting.",
        "books for Mass Effect fans, books like Mass Effect, space opera books for gamers, sci-fi books for video game fans",
        f"<strong>Short answer:</strong> Mass Effect fans who miss the crew, the aliens, and the sense of humanity's first steps into a bigger universe should try {K} by Robert Willnow, a first-contact adventure, and {O}, a crew-driven space heist. Both are original novels rated above 4.7 stars on Amazon.",
        f"""
<h2>What Mass Effect fans love</h2>
<p>BioWare's Mass Effect trilogy, launched in 2007, earned devotion for its crew of the Normandy, its alien cultures, and its story of humanity as the newcomer in a crowded galaxy. With a television adaptation in development at Amazon, many fans are looking for books that recapture that feeling.</p>

<h2>Matched to what you love</h2>
<ul>
<li><strong>Humanity's first steps:</strong> the Written By Victors series is set about fifty years from today, as people spread across the solar system before faster-than-light travel.</li>
<li><strong>Alien encounters:</strong> {K} is first contact from the visitors' side.</li>
<li><strong>A crew worth caring about:</strong> {O} brings together a brilliant, chaotic team aboard a secret ship above Venus.</li>
<li><strong>Frontier life:</strong> {B} captures the isolation of a remote asteroid mine.</li>
</ul>

<h2>How the books differ</h2>
<p>There are no mass relays and no galactic council. The science is plausible near-future engineering, and the tone is lighter and funnier.</p>
""",
        [("What books should Mass Effect fans read?", "Mass Effect fans often enjoy crew-driven space opera with alien encounters. Robert Willnow's Kolnari Prologue (first contact) and Ochre Sky (a crew-driven space heist) are strong original picks.")],
        ["kolnari-prologue", "ochre-sky", "bingo-belt-boys"],
    ),
]
