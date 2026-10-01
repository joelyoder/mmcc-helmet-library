const slugify = require("slugify");
const eras = require("./src/_data/eras.json");

// Some helmets carry a qualifier on their era tag, e.g. "Covert w/ Traditional
// Earcaps" or "Survivor (Full visor required)" — that detail is worth keeping
// visible on the helmet card, but the tag should still file under the plain
// "Covert" / "Survivor" era page. Match the longest canonical era name that's
// a prefix of the tag (longest-first so "Pilot w/ Acc." wins over any shorter
// false match).
const eraNamesByLength = [...eras].sort((a, b) => b.name.length - a.name.length);
function canonicalEraName(tag) {
  const found = eraNamesByLength.find((e) =>
    String(tag || "").toLowerCase().startsWith(e.name.toLowerCase())
  );
  return found ? found.name : tag;
}

module.exports = function (eleventyConfig) {
  eleventyConfig.addPassthroughCopy("src/css");
  eleventyConfig.addPassthroughCopy("src/images");
  eleventyConfig.addPassthroughCopy("src/fonts");

  eleventyConfig.addFilter("slug", (str) =>
    slugify(String(str || ""), { lower: true, strict: true })
  );

  eleventyConfig.addFilter("findMaker", (makers, name) =>
    (makers || []).find((m) => m.name === name)
  );

  eleventyConfig.addFilter("canonicalEra", canonicalEraName);

  function byName(a, b) {
    return a.name.localeCompare(b.name);
  }

  eleventyConfig.addFilter("helmetsForEra", (helmets, eraName) =>
    (helmets || [])
      .filter((h) => h.eras.some((tag) => canonicalEraName(tag) === eraName))
      .sort(byName)
  );

  eleventyConfig.addFilter("helmetsForMaker", (helmets, makerName) =>
    (helmets || []).filter((h) => h.maker === makerName).sort(byName)
  );

  return {
    dir: {
      input: "src",
      output: "_site",
      includes: "_includes",
    },
  };
};
