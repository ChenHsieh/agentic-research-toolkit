/* ============================================================
   Swipe decision-tree (home page only).
   Chrome, reveal, copy, and scroll progress live in nav.js.
   ============================================================ */
(function () {
  "use strict";

  var deck = document.getElementById("deck");
  if (!deck) return; // not the home page

  var dots = document.getElementById("dots");
  var controls = document.getElementById("controls");

  var TREE = {
    start: "scale",
    steps: 2,
    nodes: {
      scale: { emoji: "💬", text: "Does what you're working on fit in a single chat message?", hint: "one experiment, a page of notes, a paragraph to draft", yes: "repeat", no: "stakes" },
      repeat: { emoji: "🔁", text: "Do you keep redoing the same cleanup or lookup, many times over?", hint: "the same task on file after file", yes: "l2", no: "l1" },
      stakes: { emoji: "👥", text: "Do others depend on this data, or will the project run for months?", hint: "a shared table, a curated dataset, a long project", yes: "l3", no: "l2" }
    }
  };

  var ARCHETYPES = {
    l1: {
      emoji: "🌱", name: "The Bench Recorder", badge: "The simplest setup is the right one",
      blurb: "Your task fits in a chat and it is not a repeating job. That does not call for tooling; it calls for a good prompt and your own eyes on the result.",
      setupLine: "A chat window, the notebook prompt, and the verify habit. Nothing to install.",
      lv: 1, lvName: "Level 1 · Chat only",
      steps: ["Open Claude or ChatGPT and paste the notebook-entry prompt.", "Drop in one real bench note; read what it says is missing.", "Retype the final entry yourself, so you stay the record of truth."],
      cta: [{ label: "Go to Level 1 →", href: "level-1.html" }]
    },
    l2: {
      emoji: "🔭", name: "The Cross-Referencer", badge: "Your work has outgrown a single chat",
      blurb: "Either the data is too big to paste, or you redo the same lookup constantly. A tool that can read your files pays off, as long as approval stays on and it quotes its sources.",
      setupLine: "One agentic tool (Claude Code or Codex), pointed at your data folder.",
      lv: 2, lvName: "Level 2 · Agentic access",
      steps: ["Point an agentic tool at the one folder your files live in.", "Ask it to quote the actual rows back, not just give you a count.", "Keep approval on: it proposes the change, you say yes."],
      cta: [{ label: "Go to Level 2 →", href: "level-2.html" }, { label: "Interfaces", href: "interfaces.html" }]
    },
    l3: {
      emoji: "🧭", name: "The Project Steward", badge: "Others depend on this, and it's long-lived",
      blurb: "People trust your tables, and the project outlives any one session. Give the assistant a written memory it cannot drift from.",
      setupLine: "Three files: AGENT_BRIEF.md, CLAUDE.md, and a dated docs/log/.",
      lv: 3, lvName: "Level 3 · Starter kit",
      steps: ["Start with AGENT_BRIEF.md, the most value for the least effort.", "Add CLAUDE.md house rules: quote the source before any claim.", "Log each decision in docs/log/YYYYMMDD_topic.md."],
      cta: [{ label: "Go to Level 3 →", href: "level-3.html" }]
    }
  };

  var current = TREE.start, answered = 0, trail = [];

  function buildDots() {
    dots.innerHTML = "";
    for (var i = 0; i < TREE.steps; i++) dots.appendChild(document.createElement("i"));
    updateDots();
  }
  function updateDots() {
    var ds = dots.children;
    for (var i = 0; i < ds.length; i++) ds[i].className = i < answered ? "done" : (i === answered ? "current" : "");
  }

  function render() {
    var node = TREE.nodes[current];
    deck.innerHTML = "";
    var ghost = document.createElement("div");
    ghost.className = "card"; ghost.style.transform = "translateY(10px) scale(0.96)"; ghost.style.zIndex = "1";
    ghost.setAttribute("aria-hidden", "true");
    deck.appendChild(ghost);
    var card = document.createElement("div");
    card.className = "card"; card.style.zIndex = "2";
    card.innerHTML =
      '<div class="stamp yes">Yes</div><div class="stamp no">No</div>' +
      '<div class="q-emoji">' + node.emoji + '</div>' +
      '<div><div class="q-text">' + node.text + '</div><div class="q-hint">' + node.hint + '</div></div>' +
      '<div class="q-hint">Question ' + (answered + 1) + ' of ' + TREE.steps + '</div>';
    deck.appendChild(card);
    attachDrag(card, node);
    updateDots();
  }

  function decide(dir, node) {
    var next = dir > 0 ? node.yes : node.no;
    trail.push({ emoji: node.emoji, ans: dir > 0 ? "Yes" : "No" });
    answered++;
    if (ARCHETYPES.hasOwnProperty(next)) showResult(next);
    else { current = next; render(); }
  }

  function flyOut(card, dir, cb) {
    card.style.transition = "transform .38s cubic-bezier(.4,.1,.3,1), opacity .38s";
    card.style.transform = "translate(" + (dir * 600) + "px," + (dir * -40) + "px) rotate(" + (dir * 22) + "deg)";
    card.style.opacity = "0";
    setTimeout(cb, 240);
  }

  function attachDrag(card, node) {
    var startX = 0, dx = 0, dy = 0, dragging = false;
    var yes = card.querySelector(".stamp.yes"), no = card.querySelector(".stamp.no");
    function point(e) { return e.touches && e.touches[0] ? { x: e.touches[0].clientX, y: e.touches[0].clientY } : { x: e.clientX, y: e.clientY }; }
    function down(e) { dragging = true; startX = point(e).x; card.style.transition = "none"; card.setPointerCapture && e.pointerId != null && card.setPointerCapture(e.pointerId); }
    function move(e) {
      if (!dragging) return;
      dx = point(e).x - startX;
      card.style.transform = "translate(" + dx + "px,0) rotate(" + (dx / 18) + "deg)";
      var t = Math.min(Math.abs(dx) / 90, 1);
      yes.style.opacity = dx > 0 ? t : 0; no.style.opacity = dx < 0 ? t : 0;
    }
    function up() {
      if (!dragging) return; dragging = false;
      if (Math.abs(dx) > 95) { var dir = dx > 0 ? 1 : -1; flyOut(card, dir, function () { decide(dir, node); }); }
      else { card.style.transition = "transform .28s ease"; card.style.transform = "translateY(0) scale(1)"; yes.style.opacity = 0; no.style.opacity = 0; }
      dx = dy = 0;
    }
    if (window.PointerEvent) {
      card.addEventListener("pointerdown", down); card.addEventListener("pointermove", move);
      card.addEventListener("pointerup", up); card.addEventListener("pointercancel", up);
    } else {
      card.addEventListener("touchstart", down, { passive: true }); card.addEventListener("touchmove", move, { passive: true }); card.addEventListener("touchend", up);
      card.addEventListener("mousedown", down); window.addEventListener("mousemove", move); window.addEventListener("mouseup", up);
    }
  }

  function programmatic(dir) {
    if (ARCHETYPES.hasOwnProperty(current)) return;
    var top = deck.querySelector(".card:last-child"), node = TREE.nodes[current];
    if (top) flyOut(top, dir, function () { decide(dir, node); }); else decide(dir, node);
  }
  document.getElementById("btnNo").addEventListener("click", function () { programmatic(-1); });
  document.getElementById("btnYes").addEventListener("click", function () { programmatic(1); });
  document.addEventListener("keydown", function (e) {
    if (ARCHETYPES.hasOwnProperty(current)) return;
    var r = deck.getBoundingClientRect();
    if (r.bottom < 0 || r.top > window.innerHeight) return;
    if (e.key === "ArrowRight") { e.preventDefault(); programmatic(1); }
    else if (e.key === "ArrowLeft") { e.preventDefault(); programmatic(-1); }
  });

  function showResult(leafKey) {
    current = leafKey;
    dots.innerHTML = "";
    controls.style.display = "none";
    document.querySelector(".swipe-hint").style.display = "none";
    var a = ARCHETYPES[leafKey];
    var lvColor = a.lv === 1 ? "var(--l1)" : a.lv === 2 ? "var(--l2)" : "var(--l3)";
    var lvSoft = a.lv === 1 ? "var(--l1-soft)" : a.lv === 2 ? "var(--l2-soft)" : "var(--l3-soft)";
    var trailHtml = trail.map(function (t) { return '<span class="trail-chip">' + t.emoji + " " + t.ans + "</span>"; }).join('<span class="trail-arrow">→</span>');
    var stepsHtml = a.steps.map(function (t) { return "<li>" + t + "</li>"; }).join("");
    var ctaHtml = a.cta.map(function (c, i) { return '<a class="btn ' + (i === 0 ? "btn-accent" : "btn-ghost") + '" href="' + c.href + '">' + c.label + "</a>"; }).join("");
    deck.style.height = "auto";
    deck.innerHTML =
      '<div class="result">' +
        '<div class="trail">' + trailHtml + '</div>' +
        '<div class="arche-emoji">' + a.emoji + '</div>' +
        '<div class="badge">' + a.badge + '</div>' +
        '<h3>' + a.name + '</h3>' +
        '<p class="lead" style="margin:10px auto 0">' + a.blurb + '</p>' +
        '<div class="setup-line" style="background:' + lvSoft + ';border-color:' + lvColor + '"><span class="si">🧰</span><span><b>Your setup:</b> ' + a.setupLine + '</span></div>' +
        '<div class="reco"><div class="reco-top"><span class="lv-chip" style="background:' + lvColor + '">' + a.lvName + '</span><span class="muted" style="font-size:.85rem">your recommended starting point</span></div>' +
        '<ol>' + stepsHtml + '</ol><div class="reco-cta">' + ctaHtml + '</div></div>' +
        '<div class="retake"><button id="retake">↺ Start over</button></div>' +
      '</div>';
    document.getElementById("retake").addEventListener("click", reset);
    var r = deck.querySelector(".result");
    if (r.animate) r.animate([{ opacity: 0, transform: "scale(.96)" }, { opacity: 1, transform: "scale(1)" }], { duration: 380, easing: "cubic-bezier(.2,.7,.2,1)" });
  }

  function reset() {
    current = TREE.start; answered = 0; trail = [];
    deck.style.height = "340px"; controls.style.display = "";
    document.querySelector(".swipe-hint").style.display = "";
    buildDots(); render();
  }

  buildDots();
  render();
})();
