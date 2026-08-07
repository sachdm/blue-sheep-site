#!/usr/bin/env python3
"""
Generates every page of the Blue Sheep preview from one template.

The old site hand-wrote the nav into 24 separate files, so any nav change was a
24-file edit and they drifted apart. Here the chrome exists once, in this file.
Run:  python3 build.py
"""
import json, os, re, html

HERE = os.path.dirname(os.path.abspath(__file__))
FILMS = json.load(open(os.path.join(HERE, 'data.json'), encoding='utf-8'))

NAV = [('Work', 'work.html'), ('Contact', 'contact.html'), ('Slate', 'investors.html')]

E = lambda s: html.escape(str(s), quote=True)


def chrome(title, body, page=''):
    nav = '\n'.join(
        '    <a href="{}" data-tc="{:02d}"{}>{}</a>'.format(
            h, i + 1, ' class="on"' if h == page else '', t)
        for i, (t, h) in enumerate(NAV))
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="robots" content="noindex,nofollow">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{E(title)} — Blue Sheep (preview)</title>
<link rel="stylesheet" href="bs.css">
</head>
<body>
<header>
  <a class="brand" href="index.html">Blue<i>·</i>Sheep</a>
  <nav>
{nav}
  </nav>
</header>
{body}
<footer>
  <span>Blue Sheep — Toronto</span>
  <span class="muted">Documentary · Narrative · Commercial</span>
  <span><a href="https://vimeo.com/bluesheepfilms">Vimeo</a> · <a href="https://www.instagram.com/bluesheep.films/">Instagram</a></span>
  <span class="muted">© 2026</span>
</footer>
</body>
</html>
"""


def tc(v):
    return f'<div class="tc">{v}</div>'


# ── homepage ────────────────────────────────────────────────────────────
PLACE = [
    dict(k='f', i=0, c=6, w=6, lead=0,  tc='00:00:00:00'),
    dict(k='t', id='who',   c=0, w=3, lead=34, tc='00:00:12:04'),
    dict(k='f', i=1, c=1, w=4, lead=56, tc='00:01:04:11'),
    dict(k='t', id='what',  c=7, w=4, lead=40, tc='00:01:22:19'),
    dict(k='f', i=2, c=7, w=5, lead=14, tc='00:02:09:02'),
    dict(k='t', id='where', c=0, w=3, lead=38, tc='00:02:41:16'),
    dict(k='f', i=3, c=2, w=4, lead=26, tc='00:03:00:07'),
    dict(k='f', i=5, c=7, w=5, lead=52, tc='00:04:30:15'),
    dict(k='t', id='why',   c=0, w=3, lead=44, tc='00:04:11:03'),
    dict(k='f', i=4, c=0, w=4, lead=26, tc='00:03:48:21'),
    dict(k='f', i=6, c=4, w=5, lead=70, tc='00:05:12:09'),
    dict(k='t', id='how',   c=9, w=3, lead=58, tc='00:05:44:22'),
    dict(k='f', i=7, c=0, w=4, lead=48, tc='00:06:03:18'),
]

COPY = {
    'who':   ('Who we are',   ["A lean crew who believe the best stories are found, not forced. "
                               "Shot on real locations, with real people, at the pace the story needs.",
                               '<a href="about.html">More about the studio →</a>']),
    'what':  ('What we do',   ["Development, production and post — for independent shorts, "
                               "documentary and commercial work."]),
    'where': ('Where we are', ["12 Birch Ave, Toronto, Ontario. 43.6532° N, 79.3832° W."]),
    'why':   ('Why we do it', ["Because every project gets the same attention, whether it's a "
                               "ninety-second spot or a feature doc."]),
    'how':   ('How we do it', ["Small units, real locations, and the same three or four people "
                               "who have done it before."]),
}


def home():
    body = ('<div id="canvas"></div>\n'
            f'<script>window.PLACE={json.dumps(PLACE)};'
            f'window.FILMS={json.dumps(FILMS)};'
            f'window.COPY={json.dumps({k: {"l": v[0], "p": v[1]} for k, v in COPY.items()})};</script>\n'
            '<script src="bs.js"></script>')
    return chrome('Home', body)


# ── work ────────────────────────────────────────────────────────────────
def work():
    index = ''.join(
        f'<a href="{f["slug"]}.html">{E(f["title"])}</a>' for f in FILMS)
    tiles = ''.join(f"""
    <a class="tile" href="{f['slug']}.html">
      <figure><span class="idx">{i+1:02d}</span>
        <img src="{E(f['still'])}" alt="{E(f['title'])}"
             loading="{'eager' if i < 4 else 'lazy'}" decoding="async"></figure>
      <figcaption><span class="t">{E(f['title'])}</span>
        <span class="c">{E(f['cat'])}&nbsp;&nbsp;{f['year']}</span></figcaption>
    </a>""" for i, f in enumerate(FILMS))
    body = f"""<main class="page">
  {tc('00:00:00:00')}
  <div class="lbl">Selected work — {len(FILMS)} films, 2023–2026</div>
  <div class="namelist">{index}</div>
  <div class="grid4">{tiles}
  </div>
</main>"""
    return chrome('Work', body, 'work.html')


# ── film page ───────────────────────────────────────────────────────────
def film(i):
    f = FILMS[i]
    prev, nxt = FILMS[i - 1], FILMS[(i + 1) % len(FILMS)]
    h = f'?h={f["vimeoHash"]}&' if f.get('vimeoHash') else '?'
    src = (f'https://player.vimeo.com/video/{f["vimeoId"]}{h}'
           'title=0&byline=0&portrait=0&dnt=1')
    credits = ''.join(
        f'<div class="cr"><span class="r">{E(c["role"])}</span>'
        f'<span class="n">{E(c["name"])}</span></div>' for c in f.get('credits', []))
    body = f"""<main class="page film-page">
  {tc('00:00:00:00')}
  <div class="filmhead">
    <span class="idx-n">{i+1:02d}</span>
    <span class="t">{E(f['title'])}</span>
    <span class="c">{E(f['cat'])}&nbsp;&nbsp;{f['year']}</span>
  </div>
  <div class="player"><iframe src="{E(src)}" allow="autoplay; fullscreen; picture-in-picture"
      title="{E(f['title'])}" loading="lazy"></iframe></div>
  <div class="filmbody">
    <div class="syn">
      <div class="lbl">Synopsis</div>
      <p>{E(f['synopsis'])}</p>
    </div>
    <div class="credits">
      <div class="lbl">Credits</div>
      {credits}
    </div>
  </div>
  <div class="pager">
    <a href="{prev['slug']}.html">← {E(prev['title'])}</a>
    <a href="work.html">All work</a>
    <a href="{nxt['slug']}.html">{E(nxt['title'])} →</a>
  </div>
</main>"""
    return chrome(f['title'], body)


# ── studio ──────────────────────────────────────────────────────────────
def about():
    nums = [('8', 'Films produced'), ('2023', 'Founded'),
            ('3', 'In development'), ('TOR', 'Home base')]
    numhtml = ''.join(f'<div class="num"><span class="v">{v}</span>'
                      f'<span class="k">{k}</span></div>' for v, k in nums)
    svc = [('a', 'Development', 'Scripts, coverage, beat sheets, financing plans and grant packages.'),
           ('b', 'Production',  'Small units on real locations. Narrative shorts, commercial, music video.'),
           ('c', 'Post',        'Edit, colour, sound and delivery — through to festival and distribution.')]
    svchtml = ''.join(f'<div class="svc"><span class="k">{k}</span>'
                      f'<span class="n">{n}</span><span class="d">{d}</span></div>'
                      for k, n, d in svc)
    body = f"""<main class="page">
  {tc('00:00:00:00')}
  <div class="lbl">Est. 2023 — Toronto, Canada</div>
  <div class="lede">
    <p>Blue Sheep handles development, production and post for independent shorts,
    documentary and commercial work. Founded in 2023, we have kept the team small
    on purpose — every project gets the same attention, whether it is a
    ninety-second spot or a feature doc.</p>
    <p>We make films the slow way. The best stories are found, not forced: shot on
    real locations, with real people, at the pace the story actually needs.</p>
  </div>
  <div class="lbl sp">By the numbers</div>
  <div class="nums">{numhtml}</div>
  <div class="lbl sp">What we do</div>
  <div class="svcs">{svchtml}</div>
  <div class="pager"><a href="work.html">See the work →</a></div>
</main>"""
    return chrome('Studio', body)


# ── contact ─────────────────────────────────────────────────────────────
def contact():
    blocks = [
        ('General',    '<a href="mailto:info@bluesheepfilms.com">info@bluesheepfilms.com</a>'),
        ('Studio',     '12 Birch Ave.<br>Toronto, Ontario<br>Canada'),
        ('Elsewhere',  '<a href="https://vimeo.com/bluesheepfilms">Vimeo</a><br>'
                       '<a href="https://www.instagram.com/bluesheep.films/">Instagram</a>'),
        ('Reply time', 'Usually within two days.'),
        ('Coordinates', '43.6532° N<br>79.3832° W'),
    ]
    bh = ''.join(f'<div class="cblk"><div class="lbl">{l}</div><div class="v">{v}</div></div>'
                 for l, v in blocks)
    body = f"""<main class="page">
  {tc('00:00:00:00')}
  <div class="lbl"><span class="dot"></span>Open for 2026 / 2027 projects</div>
  <div class="lede">
    <p>Got a project brewing, or just want to talk shop? We are easy to reach —
    one of us reads everything that comes in.</p>
  </div>
  <div class="cblks">{bh}</div>
</main>"""
    return chrome('Contact', body, 'contact.html')


# ── slate ───────────────────────────────────────────────────────────────
def slate():
    body = f"""<main class="page">
  {tc('00:00:00:00')}
  <div class="lbl">The active development slate</div>
  <div class="lede">
    <p>Titles in script and development, in post, and on a festival run.
    Not everything here is public yet.</p>
  </div>
  <div class="slate">
    <a class="srow" href="../investors-ip.html">
      <span class="n">Working IP</span>
      <span class="d">The active development slate — titles in script/dev, post, and festival run.</span>
      <span class="m">Internal →</span>
    </a>
  </div>
</main>"""
    return chrome('Slate', body, 'investors.html')


# ── write ───────────────────────────────────────────────────────────────
def main():
    pages = {'index.html': home(), 'work.html': work(),
             'about.html': about(), 'contact.html': contact(),
             'investors.html': slate()}
    for i, f in enumerate(FILMS):
        pages[f['slug'] + '.html'] = film(i)
    for name, src in pages.items():
        open(os.path.join(HERE, name), 'w', encoding='utf-8').write(src)
    print(f'wrote {len(pages)} pages:', ', '.join(sorted(pages)))


if __name__ == '__main__':
    main()
