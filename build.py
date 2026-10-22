"""Builds the 2026 Convocation schedule page from the files in data/.

Run:  python3 build.py
Makes:
  docs/index.html                             the live page GitHub Pages serves
  dist/convocation-2026.html                  the same page as a file to upload elsewhere
  dist/convocation-2026-wordpress-block.html  the same page for a WordPress Custom HTML block
  dist/schema-event.html                      Event schema to paste into the sricf.org page
"""
import html
import json
import re
from pathlib import Path

here = Path(__file__).parent
data = {name: json.loads((here / "data" / f"{name}.json").read_text()) for name in ("event", "schedule", "notices")}
event = data["event"][0]
seo = event["seo"]

# Keep "</" out of the inline script so a value can never close the <script> tag early.
payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
fragment = (here / "template.html").read_text().replace("/*__DATA__*/", payload, 1)


def address(a):
    """A PostalAddress with only the parts we actually know."""
    parts = {"streetAddress": a.get("street"), "addressLocality": a.get("city"), "addressRegion": a.get("region"),
             "postalCode": a.get("postal_code"), "addressCountry": a.get("country")}
    return {"@type": "PostalAddress", **{k: v for k, v in parts.items() if v}}


def presenter_names():
    """Presenters of papers, without honorifics, degrees or college: 'R.W. Fra. Kirk White IX° (Vermont College)' -> 'Kirk White'."""
    names = []
    for row in data["schedule"]:
        if row["kind"] != "paper":
            continue
        for line in row["presenters"].split("\n"):
            name = re.sub(r"\s*\(.*\)$", "", line.strip())
            name = re.sub(r"^(R\.W\.|V\.W\.|M\.W\.|W\.)?\s*Fra\.\s*", "", name)
            name = re.sub(r"\s+[IVX]+°$", "", name).strip()
            if name and name not in names:
                names.append(name)
    return names


days = sorted({row["day"] for row in data["schedule"]})
venue = seo["venue"]
schema = {
    "@context": "https://schema.org",
    "@type": "Event",
    "@id": seo["page_url"] + "#event",
    "name": seo["event_name"],
    "description": seo["event_description"],
    "url": seo["page_url"],
    "mainEntityOfPage": {"@id": seo["page_url"]},
    "image": [seo["image"]],
    "startDate": days[0],
    "endDate": days[-1],
    "eventStatus": "https://schema.org/EventScheduled",
    "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
    "location": {"@type": "Place", "name": venue["name"] or f"{venue['city']}, {venue['region']}", "address": address(venue)},
    "organizer": {"@type": "Organization", "name": seo["organizer"]["name"], "url": seo["organizer"]["url"],
                  "logo": seo["image"], "address": address(seo["organizer"])},
    "offers": {"@type": "AggregateOffer", "url": seo["registration_url"], "priceCurrency": "USD",
               "lowPrice": seo["price_low"], "highPrice": seo["price_high"], "availability": "https://schema.org/InStock"},
    "performer": [{"@type": "Person", "name": n} for n in presenter_names()],
}
schema_tag = ('<script type="application/ld+json">\n'
              + json.dumps(schema, ensure_ascii=False, indent=2).replace("</", "<\\/")
              + "\n</script>\n")

esc = lambda s: html.escape(s, quote=True)
page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(seo['title'])}</title>
<meta name="description" content="{esc(seo['description'])}">
<link rel="canonical" href="{esc(seo['page_url'])}">
<style>body {{ margin: 0; background: transparent; }}</style>
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
(out / "schema-event.html").write_text(schema_tag)

site = here / "docs"
site.mkdir(exist_ok=True)
(site / "index.html").write_text(page)
(site / ".nojekyll").write_text("")  # serve the files as they are
print(f"Built {len(data['schedule'])} sessions and {len(data['notices'])} notices into docs/ and dist/; "
      f"schema lists {len(schema['performer'])} presenters")
