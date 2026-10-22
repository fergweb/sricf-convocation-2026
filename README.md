# High Council SRICF — 2026 Convocation schedule page

A public schedule page for sricf.org, built from the High Council's tentative-schedule PDF
(Sept 2026) plus later updates. It needs no login and runs in any browser.

## What's here

| File | What it is |
|---|---|
| `data/schedule.json` | Every session: day, time, title, presenters, room, floor |
| `data/notices.json` | The notices box (key card, Ladies/Partners suite) |
| `data/event.json` | Name, "2026 Convocation", "Tentative schedule", footer line |
| `template.html` | The page's design and code (no schedule text in it) |
| `build.py` | Combines the above into the two finished files |
| `dist/convocation-2026-wordpress-block.html` | **Paste into WordPress** (Custom HTML block) |
| `dist/convocation-2026.html` | A complete standalone page, if you'd rather upload a file |

## Putting it on sricf.org (first time)

1. In WordPress, add a new page, e.g. **2026 Convocation Schedule**, slug `convocation-2026`.
2. Add a **Custom HTML** block. Open `dist/convocation-2026-wordpress-block.html`,
   copy everything, paste it into the block.
3. In the page's Avada options, hide the page title bar (the schedule has its own title)
   and pick a full-width or 100%-width layout if the content area feels narrow.
4. Publish, then open the page in a private/incognito window to confirm it shows without logging in.

You must be a WordPress administrator to save a block that contains a script.

## Updating it later

Tell Claude the changes (e.g. "Saturday banquet moves to 7:30"). Claude edits the files
in `data/`, runs `python3 build.py`, and also updates the Claude-hosted copy.
Then you replace the Custom HTML block's contents with the new
`dist/convocation-2026-wordpress-block.html` and click **Update**.

To edit by hand: change the text in `data/schedule.json` (keep the quotes and commas),
then run:

```bash
python3 build.py
```

Notes on the data:
- A line break inside a cell is written `\n` (e.g. `"Lunch\nLadies Lunch"`).
- `*word*` in a title shows in italics.
- `kind` controls the filter buttons: `paper`, `meal`, `social`, `business`, `ceremony`, `training`.

## Claude-hosted copy

https://claude.ai/artifact/6f1hq5V2TgBX5EJXzXsAVJ — kept in sync, but visitors must be
signed in to Claude to view it, so the sricf.org page is the public one.
