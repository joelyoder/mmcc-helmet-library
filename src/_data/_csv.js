const fs = require("fs");
const Papa = require("papaparse");

// Loads rows from a published Google Sheets CSV URL (env var), falling back
// to a local sample CSV when the env var isn't set yet or the fetch fails.
// This lets `npm start` work out of the box before anyone has connected a
// real Google Sheet, and keeps the build resilient if Sheets is briefly down.
async function loadCsv(url, fallbackPath) {
  let text;
  if (url) {
    try {
      const res = await fetch(url);
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      text = await res.text();
    } catch (err) {
      console.warn(
        `[csv] Could not fetch ${url} (${err.message}). Falling back to ${fallbackPath}.`
      );
    }
  }
  if (!text) {
    text = fs.readFileSync(fallbackPath, "utf8");
  }
  const parsed = Papa.parse(text, { header: true, skipEmptyLines: true });
  return parsed.data;
}

function splitList(value) {
  return String(value || "")
    .split(";")
    .map((s) => s.trim())
    .filter(Boolean);
}

module.exports = { loadCsv, splitList };
