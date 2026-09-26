const path = require("path");
const slugify = require("slugify");
const { loadCsv, splitList } = require("./_csv.js");

function slug(str) {
  return slugify(String(str || ""), { lower: true, strict: true });
}

module.exports = async function () {
  const rows = await loadCsv(
    process.env.HELMETS_CSV_URL,
    path.join(__dirname, "sample", "helmets.csv")
  );

  const helmets = rows
    .filter((r) => r.Name && r.Name.trim())
    .map((r) => ({
      name: r.Name.trim(),
      maker: (r.Maker || "").trim(),
      eras: splitList(r.Eras),
      approvable: (r.Approvable || "yes").trim().toLowerCase() !== "no",
      images: splitList(r.Images),
      modelLink: (r.ModelLink || "").trim(),
      buyLink: (r.BuyLink || "").trim(),
      notes: (r.Notes || "").trim(),
    }));

  // Precompute a stable, unique slug for each helmet's detail page URL.
  const seen = new Map();
  for (const h of helmets) {
    const base = `${slug(h.name)}-${slug(h.maker)}`;
    const n = (seen.get(base) || 0) + 1;
    seen.set(base, n);
    h.slug = n === 1 ? base : `${base}-${n}`;
  }

  return helmets;
};
