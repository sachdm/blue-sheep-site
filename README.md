# ~/journal

A terminal-style personal journal, hosted free on GitHub Pages. No build tools, no dependencies — just HTML, Markdown, and a blinking cursor.

## Setup (one time)

1. Create a new repo on GitHub (e.g. `journal`). Note: GitHub Pages on a **private** repo requires a paid plan; a public repo is free — anyone with the URL could read it, so keep that in mind.
2. Push these files:
   ```bash
   cd journal
   git init
   git add .
   git commit -m "journal v1.0"
   git remote add origin https://github.com/YOUR_USERNAME/journal.git
   git push -u origin main
   ```
3. In the repo: **Settings → Pages → Source: Deploy from a branch → main / (root) → Save**.
4. Your journal is live at `https://YOUR_USERNAME.github.io/journal/` after a minute or two.

## Writing an entry

1. Create a Markdown file in `entries/`, named by date:
   ```
   entries/2026-07-21.md
   ```
2. Add one line for it in `entries.json`:
   ```json
   { "date": "2026-07-21", "title": "Whatever happened today", "file": "2026-07-21.md" }
   ```
3. Commit and push. Done.

You can do both directly on github.com (Add file → Create new file) — no local git needed.

## Reading it

The site is an interactive terminal. Commands:

| command | what it does |
|---|---|
| `ls` | list all entries |
| `cat 2026-07-20` | read an entry |
| `latest` | read the newest entry |
| `random` | read a random entry |
| `grep word` | search entry titles |
| `clear` | clear the screen |

## Previewing locally

`fetch()` doesn't work on `file://` URLs, so serve the folder:

```bash
python3 -m http.server
# open http://localhost:8000
```

## Supported Markdown

Headers (`#`–`###`), **bold**, *italic*, `code`, links, `-` lists, `>` quotes, and `---` rules.
