# Search setup for https://sricf.org/2026-schedule/

The schedule itself lives on GitHub and is shown inside the sricf.org page. Search engines credit
an embedded schedule to GitHub, not to sricf.org, so everything below goes on the **sricf.org page**.
The GitHub copy points search engines back to sricf.org (`canonical`), so the two don't compete.

## 1. Yoast: title and meta description

Edit the page → scroll to the **Yoast SEO** box.

- **SEO title:** `2026 Convocation Schedule | High Council SRICF`
- **Slug:** leave as `2026-schedule`
- **Meta description** (153 characters):

  `Tentative schedule for the SRICF High Council 2026 Convocation, Nov. 13–14 in Louisville, KY: papers and presenters, meals, rooms and hospitality suites.`

- **Focus keyphrase** (optional): `SRICF Convocation 2026`

## 2. Event schema (structured data)

In Avada Builder, add a second **Code Block** (anywhere on the page, e.g. under the schedule) and
paste everything from `dist/schema-event.html`. It's invisible to visitors.
It tells Google the event's name, dates, city, organizer, presenters and registration link,
which makes the page eligible for Google's event listings.

`build.py` regenerates this file from the schedule data. Re-paste it only if the dates, venue,
prices or presenters change. Claude will say so when that happens.

Check it after publishing: https://search.google.com/test/rich-results?url=https://sricf.org/2026-schedule/

## 3. A short visible intro (recommended)

Search engines can't credit the embedded schedule's text to sricf.org, so the page has almost no
words of its own. A text block above the schedule fixes that:

> The 2026 Convocation of the High Council, Societas Rosicruciana in Civitatibus Foederatis,
> meets November 13–14, 2026 in Louisville, Kentucky. Below is the tentative schedule of papers,
> meetings, meals and hospitality suites. See the speaker biographies and abstracts on the
> Speaker Info page, and register for meals and events on the Event Registration page.

(Link "Speaker Info" and "Event Registration" to their pages.)

## Open items

- **Venue:** the schema says only "Louisville, KY". Google prefers a full venue name and street address.
  The room names and the "Hot Brown" lunch suggest **The Brown Hotel, 335 West Broadway, Louisville, KY 40202**.
  Confirm with the High Council, then fill in `venue` in `data/event.json`, run `python3 build.py`, re-paste the schema.
- **Duplicate social-sharing tags:** sricf.org pages output Open Graph tags twice (Yoast and Avada).
  Fix site-wide: Avada → Options → Advanced → Theme Features → turn off **Open Graph Meta Tags** (Yoast keeps its own).
- **Old PDF:** the schedule PDF on sricf.org has outdated times and suites. Remove it or replace it with a link to this page.
