/* ============================================================
   Doc-site chrome: sidebar, header, prev/next, footer.
   One source of truth for navigation across all pages.
   ============================================================ */
(function () {
  "use strict";

  var REPO = "https://github.com/ChenHsieh/agentic-research-toolkit";

  // Flattened order drives prev/next; groups drive the sidebar.
  var GROUPS = [
    { title: "Start", items: [
      { key: "home", label: "Home", href: "index.html" },
      { key: "how-it-works", label: "How it works", href: "how-it-works.html" },
    ]},
    { title: "The ramp", items: [
      { key: "level-1", label: "Level 1 · Chat only", href: "level-1.html" },
      { key: "level-2", label: "Level 2 · File access", href: "level-2.html" },
      { key: "level-3", label: "Level 3 · Starter kit", href: "level-3.html" },
    ]},
    { title: "By role", items: [
      { key: "roles", label: "Skills by role", href: "roles.html" },
    ]},
    { title: "Reference", items: [
      { key: "interfaces", label: "Interfaces", href: "interfaces.html" },
      { key: "modes", label: "Modes", href: "modes.html" },
      { key: "recipes", label: "Recipes", href: "recipes.html" },
      { key: "spotting-errors", label: "Spotting errors", href: "spotting-errors.html" },
      { key: "connect-sources", label: "Connect your sources", href: "connect-sources.html" },
      { key: "refusals", label: "When it wrongly refuses", href: "refusals.html" },
      { key: "beyond-the-ramp", label: "Beyond the ramp", href: "beyond-the-ramp.html" },
    ]},
    { title: "Practical", items: [
      { key: "templates", label: "Templates", href: "templates.html" },
      { key: "cost", label: "What it costs", href: "cost.html" },
      { key: "protect-your-data", label: "Protect your data", href: "protect-your-data.html" },
    ]},
    { title: "More", items: [
      { key: "glossary", label: "Glossary", href: "glossary.html" },
      { key: "resources", label: "Resources", href: "resources.html" },
    ]},
  ];

  var FLAT = [];
  GROUPS.forEach(function (g) { g.items.forEach(function (it) { FLAT.push(it); }); });

  var main = document.querySelector("main.content");
  var current = main ? main.getAttribute("data-page") : null;

  // ---- top bar ----
  var topbar = document.createElement("header");
  topbar.className = "topbar";
  topbar.innerHTML =
    '<button class="menu-btn" id="menuBtn" aria-label="Menu">☰</button>' +
    '<a class="brand" href="index.html"><span class="dot"></span> agentic research</a>' +
    '<span class="spacer"></span>' +
    '<a class="tb-link" href="' + REPO + '" target="_blank" rel="noopener">GitHub</a>';

  var xp = document.createElement("div");
  xp.className = "doc-xp";
  xp.innerHTML = '<div class="xpbar-fill" id="xp"></div>';

  // ---- sidebar ----
  var sidebar = document.createElement("aside");
  sidebar.className = "sidebar";
  sidebar.id = "sidebar";
  var html = "";
  GROUPS.forEach(function (g) {
    html += '<div class="side-group"><div class="side-title">' + g.title + "</div>";
    g.items.forEach(function (it) {
      html += '<a href="' + it.href + '"' + (it.key === current ? ' class="active"' : "") + ">" + it.label + "</a>";
    });
    html += "</div>";
  });
  sidebar.innerHTML = html;

  var scrim = document.createElement("div");
  scrim.className = "scrim";

  // ---- assemble layout around <main> ----
  if (main) {
    var layout = document.createElement("div");
    layout.className = "layout";
    main.parentNode.insertBefore(layout, main);
    layout.appendChild(sidebar);
    layout.appendChild(main);

    // prev / next
    var idx = FLAT.map(function (i) { return i.key; }).indexOf(current);
    var prev = idx > 0 ? FLAT[idx - 1] : null;
    var next = idx >= 0 && idx < FLAT.length - 1 ? FLAT[idx + 1] : null;
    var pn = document.createElement("nav");
    pn.className = "prevnext";
    pn.innerHTML =
      (prev ? '<a class="prev" href="' + prev.href + '"><div class="pn-dir">← Previous</div><div class="pn-title">' + prev.label + "</div></a>"
            : '<a class="prev disabled"></a>') +
      (next ? '<a class="next" href="' + next.href + '"><div class="pn-dir">Next →</div><div class="pn-title">' + next.label + "</div></a>"
            : '<a class="next disabled"></a>');
    main.appendChild(pn);

    var foot = document.createElement("footer");
    foot.className = "docfoot";
    foot.innerHTML = "Part of the <a href=\"" + REPO + "\" target=\"_blank\" rel=\"noopener\">Agentic Research Toolkit</a>. Text and templates are free to reuse under MIT. The assistant drafts and proposes; you are the record of truth.";
    layout.parentNode.insertBefore(foot, layout.nextSibling);
  }

  document.body.insertBefore(xp, document.body.firstChild);
  document.body.insertBefore(topbar, document.body.firstChild);

  // ---- mobile drawer ----
  function closeNav() { document.body.classList.remove("nav-open"); }
  var menuBtn = document.getElementById("menuBtn");
  if (menuBtn) menuBtn.addEventListener("click", function () { document.body.classList.toggle("nav-open"); });
  scrim.addEventListener("click", closeNav);
  document.body.appendChild(scrim);
  sidebar.addEventListener("click", function (e) { if (e.target.tagName === "A") closeNav(); });

  // ---- scroll progress ----
  var xpFill = document.getElementById("xp");
  function onScroll() {
    var h = document.documentElement;
    var max = h.scrollHeight - h.clientHeight;
    var pct = max > 0 ? (h.scrollTop || document.body.scrollTop) / max : 0;
    if (xpFill) xpFill.style.width = (pct * 100).toFixed(1) + "%";
  }
  document.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  // ---- reveal on scroll ----
  var reveals = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } });
    }, { threshold: 0.1 });
    reveals.forEach(function (r) { io.observe(r); });
  } else {
    reveals.forEach(function (r) { r.classList.add("in"); });
  }

  // ---- copy buttons ----
  document.querySelectorAll(".copy-btn").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var el = document.getElementById(btn.getAttribute("data-copy"));
      if (!el) return;
      var text = el.innerText;
      var done = function () {
        var old = btn.textContent;
        btn.textContent = "Copied ✓"; btn.classList.add("ok");
        setTimeout(function () { btn.textContent = old; btn.classList.remove("ok"); }, 1600);
      };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(done).catch(function () { legacyCopy(text, done); });
      } else { legacyCopy(text, done); }
    });
  });
  function legacyCopy(text, cb) {
    var ta = document.createElement("textarea");
    ta.value = text; ta.style.position = "fixed"; ta.style.opacity = "0";
    document.body.appendChild(ta); ta.select();
    try { document.execCommand("copy"); } catch (e) {}
    document.body.removeChild(ta); cb();
  }
})();
