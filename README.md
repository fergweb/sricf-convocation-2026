# High Council SRICF — 2026 Convocation schedule page

A public schedule page for the 2026 High Council Convocation, built from the High Council's
tentative-schedule PDF (Sept 2026) plus later updates. No login needed, works in any browser.

**Live page:** https://fergweb.github.io/sricf-convocation-2026/
(GitHub Pages, published from the `docs/` folder of the `main` branch)

## How updates go live

1. Tell Claude the changes (e.g. "Saturday banquet moves to 7:30").
2. Claude edits the files in `data/`, runs `python3 build.py`, commits and pushes.
3. GitHub republishes the page by itself, usually within a minute.

Nothing to upload. The Claude-hosted copy
(https://claude.ai/artifact/6f1hq5V2TgBX5EJXzXsAVJ) is kept in sync too, but it needs a
Claude login to view, so the GitHub page is the public one.

## What's here

| File | What it is |
|---|---|
| `data/schedule.json` | Every session: day, time, title, presenters, room, floor |
| `data/notices.json` | The notices box (key card, Ladies/Partners suite) |
| `data/event.json` | Name, "2026 Convocation", "Tentative schedule", footer line |
| `template.html` | The page's design and code (no schedule text in it) |
| `build.py` | Combines the above into the finished page |
| `docs/index.html` | The live page (made by `build.py`; don't edit by hand) |
| `dist/` | The same page as a standalone file and as a WordPress Custom HTML block |

Notes on the data:
- A line break inside a cell is written `\n` (e.g. `"Lunch\nLadies Lunch"`).
- `*word*` in a title shows in italics.
- `kind` controls the filter buttons: `paper`, `meal`, `social`, `business`, `ceremony`, `training`.

## Showing it on sricf.org (Avada)

The page goes inside a normal sricf.org page, with the site's own header, menu and footer around it.
It keeps updating on its own, because it always shows the live GitHub page.

1. WordPress admin → **Pages → Add New**. Title it e.g. *2026 Convocation Schedule*.
2. Open it in **Avada Builder**. Add a **Container** (1 column), then add the **Code Block** element.
3. Paste everything from `avada-embed-code.html` into the Code Block. Save the element.
4. Page Options (below the builder) → **Page Title Bar** → Hide, if you don't want a second title.
5. **Publish**, then open the page in a private/incognito window to check it.
6. Add the page to the site menu (**Appearance → Menus**) or link it from the Convocation page.

The embedded copy sizes itself to fit, so there is no inner scrollbar, and its Friday/Saturday
links scroll the sricf.org page itself, stopping just below Avada's sticky header.
If you ever change the paste-in code, re-paste the whole of `avada-embed-code.html`.

## Optional: a sricf.org address (e.g. schedule.sricf.org)

1. Where sricf.org's DNS is managed (the domain registrar or web host), add a record:
   - Type **CNAME**, Name/Host **schedule**, Value/Target **fergweb.github.io**
2. Tell Claude it's done. Claude sets the custom domain on GitHub Pages and turns on HTTPS
   (GitHub issues the certificate itself; it can take up to an hour).
3. Link to it from the sricf.org menu.

Until then, link to the github.io address above from sricf.org.
