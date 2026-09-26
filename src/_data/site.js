const path = require("path");
const { loadCsv } = require("./_csv.js");

module.exports = async function () {
  const rows = await loadCsv(
    process.env.SITE_CSV_URL,
    path.join(__dirname, "sample", "site.csv")
  );

  const content = {};
  for (const r of rows) {
    const key = (r.Key || "").trim();
    if (key) content[key] = (r.Content || "").trim();
  }
  return content;
};
