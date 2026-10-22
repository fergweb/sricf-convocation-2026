"""Builds the 2026 Convocation schedule page from the files in data/.

Run:  python3 build.py
Makes:
  docs/index.html                             the live page GitHub Pages serves
  dist/convocation-2026.html                  the same page as a file to upload elsewhere
  dist/convocation-2026-wordpress-block.html  the same page for a WordPress Custom HTML block
"""
import json
from pathlib import Path

here = Path(__file__).parent
data = {name: json.loads((here / "data" / f"{name}.json").read_text()) for name in ("event", "schedule", "notices")}

# Keep "</" out of the inline script so a value can never close the <script> tag early.
payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
fragment = (here / "template.html").read_text().replace("/*__DATA__*/", payload, 1)

event = data["event"][0]
page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{event['edition']} Schedule · {event['short_name']}</title>
<meta name="description" content="{event['status']} for the {event['name']} {event['edition']}.">
<style>body {{ margin: 0; background: #ffffff; }}</style>
</head>
<body>
{fragment}
</body>
</html>
"""

out = here / "dist"
out.mkdir(exist_ok=True)
(out / "convocation-2026.html").write_text(page)
(out / "convocation-2026-wordpress-block.html").write_text(fragment)

site = here / "docs"
site.mkdir(exist_ok=True)
(site / "index.html").write_text(page)
(site / ".nojekyll").write_text("")  # serve the files as they are
print(f"Built {len(data['schedule'])} sessions and {len(data['notices'])} notices into docs/ and dist/")
