# MMCC Helmet Reference Library

A static site (built with [Eleventy](https://www.11ty.dev/)) that replaces the Canva helmet gallery. All content — helmets, makers, and the welcome-page text — lives in **Google Sheets**. Nobody needs to touch code or log into an admin panel to add, remove, or edit an entry: they just edit a spreadsheet, and the live site updates itself within a couple of minutes.

## How it works

- Three published-to-web Google Sheets (as CSV) are the entire content database:
  1. **Helmets** — one row per helmet.
  2. **Makers** — one row per maker (name + link to their store/site).
  3. **Site** — key/value pairs for the welcome page's intro & notes text.
- At build time, the site fetches those three CSVs and generates every page: the home page, one page per era/style (listing every helmet approved for it), and one page per maker (listing everything they make).
- Netlify rebuilds the site automatically whenever the sheets change (see the Apps Script trigger below), and whenever the code repo changes.

## Local development

```bash
npm install
npm start
```

This serves the site at `http://localhost:8080` using the small sample CSVs in `src/_data/sample/` (so it works before any real Google Sheet is connected).

To build the static output once:

```bash
npm run build
```

Output goes to `_site/`.

## 1. Set up the Google Sheet

Create one Google Sheet with three tabs, named exactly:

### Tab: `Helmets`

| Column | Meaning |
|---|---|
| `Name` | Helmet name |
| `Maker` | Maker's name — must match a row in the `Makers` tab exactly |
| `Eras` | Semicolon-separated list of era/style tags this helmet is approved for, e.g. `Modern; Legacy; Covert`. Leave blank if not approvable. Valid tags: Early Crusader, Neo Crusader, Comic Crusader, Tech Crusader, Modern, Legacy, Pilot w/ Acc., Covert, Mercenary, Survivor, Master |
| `Approvable` | `Yes` or `No`. If `No`, the site shows it as "not currently approvable" instead of an era list. |
| `Images` | Semicolon-separated photo URLs (or `/images/helmets/...` paths for images bundled in the site itself). Paste a direct image link — from Imgur, a Google Drive/Photos share link set to "anyone with the link", or the maker's own site. |
| `BuyLink` | Optional — a direct link to *this specific helmet's* product/listing page, if the maker has one. Leave blank to fall back to the maker's general site (see below). |
| `ModelLink` | Optional — link to a 3D model / build reference |
| `Notes` | Optional freeform notes |

### How "buy this helmet" links work

Each helmet's page shows a **"Buy this helmet"** button. It uses, in order:
1. That row's own `BuyLink`, if set — use this when the maker has a distinct product page per helmet (e.g. separate Etsy/Shopify listings).
2. Otherwise, the matching maker's `Website` column from the `Makers` tab — use this for makers with one storefront covering everything they make.

The original Canva deck didn't contain any purchase links, so **this is new information the club will need to add** — realistically the `Makers` tab (one link per maker) covers most cases with the least data entry; `BuyLink` is there for the exceptions.

### Tab: `Makers`

| Column | Meaning |
|---|---|
| `Name` | Maker's name — must match the `Maker` column in `Helmets` exactly |
| `Website` | Their store/site — this is what the site links out to |
| `Notes` | Optional |

### Tab: `Site`

| Column | Meaning |
|---|---|
| `Key` | `title`, `intro`, or `notes` |
| `Content` | The text for that section (shown on the home page) |

**Adding, editing, or removing a helmet or maker is just editing/adding/deleting a row.** No other step is required for the content to update on the live site (Netlify rebuilds automatically — see step 3).

## 2. Publish each tab as CSV

For **each of the three tabs**:

1. Select the tab.
2. File → Share → **Publish to web**.
3. Under "Link", choose the specific sheet (tab) — not "Entire Document".
4. Choose format **Comma-separated values (.csv)**.
5. Click **Publish**, copy the URL it gives you.

You'll end up with three URLs, one per tab.

## 3. Deploy to Netlify

1. Push this repo to GitHub.
2. In Netlify: **Add new site → Import an existing project**, pick the repo. Build command and publish directory are already set in `netlify.toml`.
3. In **Site configuration → Environment variables**, add:
   - `HELMETS_CSV_URL` → the Helmets tab's published CSV URL
   - `MAKERS_CSV_URL` → the Makers tab's published CSV URL
   - `SITE_CSV_URL` → the Site tab's published CSV URL
4. Trigger a deploy. Your site is live.
5. In **Site configuration → Build & deploy → Build hooks**, create a build hook (e.g. named "Sheet edited") and copy its URL — you'll need it for the next step.

## 4. Auto-rebuild when the sheet changes

So editors never have to remember to "publish" or trigger a deploy:

1. Open the Google Sheet → **Extensions → Apps Script**.
2. Paste this, replacing `YOUR_NETLIFY_BUILD_HOOK_URL` with the build hook URL from step 3:

   ```javascript
   function onEditRebuild() {
     UrlFetchApp.fetch("YOUR_NETLIFY_BUILD_HOOK_URL", { method: "post" });
   }
   ```

3. Click the clock icon (**Triggers**) → **Add Trigger**:
   - Function: `onEditRebuild`
   - Event source: **From spreadsheet**
   - Event type: **On edit**
4. Save, authorize it when prompted.

Now any edit to the sheet triggers a rebuild automatically (Netlify builds typically take under a minute for a site this size).

## Project structure

```
src/
  _data/
    eras.json       # fixed list of era/style tags (edit this only if the club adds a new era)
    helmets.js       # fetches+parses the Helmets sheet
    makers.js        # fetches+parses the Makers sheet
    site.js          # fetches+parses the Site sheet
    sample/          # fallback CSVs used for local dev before a real sheet is connected
  _includes/
    base.njk         # page shell
    macros.njk        # helmet card component
  eras/               # era index + one generated page per era
  makers/             # maker index + one generated page per maker
  images/             # bundled photos for the initial ~300 scraped helmets
  index.njk           # home page
```
