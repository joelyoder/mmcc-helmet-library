const path = require("path");
const { loadCsv } = require("./_csv.js");

module.exports = async function () {
  const makerRows = await loadCsv(
    process.env.MAKERS_CSV_URL,
    path.join(__dirname, "sample", "makers.csv")
  );
  const helmetRows = await loadCsv(
    process.env.HELMETS_CSV_URL,
    path.join(__dirname, "sample", "helmets.csv")
  );

  const byName = new Map();
  for (const r of makerRows) {
    const name = (r.Name || "").trim();
    if (!name) continue;
    byName.set(name, {
      name,
      website: (r.Website || "").trim(),
      notes: (r.Notes || "").trim(),
    });
  }

  // Ensure every maker referenced by a helmet has an entry, even if nobody
  // has added their info to the Makers sheet yet, so maker links never 404.
  for (const r of helmetRows) {
    const name = (r.Maker || "").trim();
    if (name && !byName.has(name)) {
      byName.set(name, { name, website: "", notes: "" });
    }
  }

  return Array.from(byName.values()).sort((a, b) =>
    a.name.localeCompare(b.name)
  );
};
