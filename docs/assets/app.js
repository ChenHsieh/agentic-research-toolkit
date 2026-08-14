/* ============================================================
   An on-ramp to agentic research — interactions
   Vanilla JS. No dependencies.
   ============================================================ */
(function () {
  "use strict";

  /* ---------- scroll XP bar ---------- */
  var xp = document.getElementById("xp");
  function onScroll() {
    var h = document.documentElement;
    var max = h.scrollHeight - h.clientHeight;
    var pct = max > 0 ? (h.scrollTop || document.body.scrollTop) / max : 0;
    xp.style.width = (pct * 100).toFixed(1) + "%";
  }
  document.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  /* ---------- reveal on scroll ---------- */
  var reveals = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); }
      });
    }, { threshold: 0.12 });
    reveals.forEach(function (r) { io.observe(r); });
  } else {
    reveals.forEach(function (r) { r.classList.add("in"); });
  }

  /* ---------- copy buttons ---------- */
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

  /* ============================================================
     SWIPE TEST
     ============================================================ */
  // weights: how much a RIGHT swipe ("that's me") points to each level.
  var QUESTIONS = [
    { emoji: "📓", text: "Most days I'm recording one experiment at a time.", hint: "one bench session, not a whole dataset", w: { l1: 2 } },
    { emoji: "✍️", text: "My notes are fast shorthand only I can read.", hint: "abbreviations, no full sentences", w: { l1: 2 } },
    { emoji: "🚫", text: "I'd rather not install or set up anything.", hint: "a chat window is as far as I want to go", w: { l1: 2 } },
    { emoji: "📊", text: "My results live in spreadsheets that have grown huge.", hint: "thousands of rows, too big to eyeball", w: { l2: 2 } },
    { emoji: "🔍", text: "I keep cross-referencing files to answer one question.", hint: "\"which samples also appear in that table?\"", w: { l2: 2 } },
    { emoji: "🗄️", text: "The same lookup gets repeated across many files.", hint: "not a one-off; a whole folder of them", w: { l2: 1, l3: 1 } },
    { emoji: "👥", text: "Other people rely on the same tables staying correct.", hint: "a shared or curated analysis", w: { l3: 2 } },
    { emoji: "🔥", text: "I've been burned by an old copy of a file being wrong.", hint: "or this project has run for months", w: { l3: 2 } }
  ];

  var ARCHETYPES = {
    l1: {
      emoji: "🌱", name: "The Bench Recorder",
      badge: "Chat is your superpower",
      blurb: "Your work is one clean observation at a time. You do not need any tooling to get real value — just a chat window and the verify habit.",
      lv: 1, lvName: "Level 1 · Chat only", color: "var(--l1)",
      steps: [
        "Open Claude or ChatGPT. Copy the notebook-entry prompt below.",
        "Paste one real bench note. Read what it flags as missing.",
        "Retype the final entry yourself. You stay the record of truth."
      ],
      cta: [{ label: "Get the prompt →", href: "#level1" }]
    },
    l2: {
      emoji: "🔭", name: "The Cross-Referencer",
      badge: "Time to give a tool file access",
      blurb: "Your data has outgrown the chat box. An agentic tool that can read and search your files will earn its keep — with approval left on.",
      lv: 2, lvName: "Level 2 · Agentic access", color: "var(--l2)",
      steps: [
        "Try an agentic tool (Claude Code, Codex) pointed at one folder.",
        "Ask it to quote the actual rows back, not just a count.",
        "Keep approval on: it proposes changes, you say yes."
      ],
      cta: [{ label: "When it pays off →", href: "#tools" }, { label: "The templates →", href: "#templates" }]
    },
    l3: {
      emoji: "🧭", name: "The Project Steward",
      badge: "You need the fuller pattern",
      blurb: "People depend on your tables and the project is long-lived. Give the assistant a memory it cannot drift from: house rules, a brief, a decision log.",
      lv: 3, lvName: "Level 3 · Starter kit", color: "var(--l3)",
      steps: [
        "Start with AGENT_BRIEF.md — highest value for least effort.",
        "Add CLAUDE.md house rules: quote before you claim.",
        "Log each decision in docs/log/YYYYMMDD_topic.md."
      ],
      cta: [{ label: "Grab the templates →", href: "#templates" }]
    }
  };

  var deck = document.getElementById("deck");
  var dots = document.getElementById("dots");
  var controls = document.getElementById("controls");
  var idx = 0;
  var score = { l1: 0, l2: 0, l3: 0 };
  var order = [];

  function buildDots() {
    dots.innerHTML = "";
    for (var i = 0; i < QUESTIONS.length; i++) {
      var d = document.createElement("i");
      dots.appendChild(d);
    }
    updateDots();
  }
  function updateDots() {
    var ds = dots.children;
    for (var i = 0; i < ds.length; i++) {
      ds[i].className = i < idx ? "done" : (i === idx ? "current" : "");
    }
  }

  function render() {
    deck.innerHTML = "";
    // render up to 3 stacked cards (top one interactive)
    for (var i = Math.min(idx + 2, QUESTIONS.length - 1); i >= idx; i--) {
      var q = QUESTIONS[i];
      var card = document.createElement("div");
      card.className = "card";
      var depth = i - idx;
      card.style.transform = "translateY(" + (depth * 10) + "px) scale(" + (1 - depth * 0.04) + ")";
      card.style.zIndex = String(10 - depth);
      card.innerHTML =
        '<div class="stamp yes">Me</div><div class="stamp no">Not me</div>' +
        '<div class="q-emoji">' + q.emoji + '</div>' +
        '<div><div class="q-text">' + q.text + '</div>' +
        '<div class="q-hint">' + q.hint + '</div></div>' +
        '<div class="q-hint">' + (i + 1) + ' / ' + QUESTIONS.length + '</div>';
      deck.appendChild(card);
      if (i === idx) attachDrag(card, q);
    }
    updateDots();
  }

  function decide(dir, q) { // dir: 1 right(yes), -1 left(no)
    if (dir > 0) {
      var w = q.w;
      for (var k in w) if (w.hasOwnProperty(k)) score[k] += w[k];
    }
    order.push({ q: q.text, yes: dir > 0 });
    idx++;
    if (idx >= QUESTIONS.length) { showResult(); }
    else { render(); }
  }

  function flyOut(card, dir, cb) {
    card.style.transition = "transform .38s cubic-bezier(.4,.1,.3,1), opacity .38s";
    card.style.transform = "translate(" + (dir * 600) + "px," + (dir * -40) + "px) rotate(" + (dir * 22) + "deg)";
    card.style.opacity = "0";
    setTimeout(cb, 240);
  }

  function attachDrag(card, q) {
    var startX = 0, startY = 0, dx = 0, dy = 0, dragging = false;
    var yes = card.querySelector(".stamp.yes");
    var no = card.querySelector(".stamp.no");

    function down(e) {
      dragging = true;
      var p = point(e);
      startX = p.x; startY = p.y;
      card.style.transition = "none";
      card.setPointerCapture && e.pointerId != null && card.setPointerCapture(e.pointerId);
    }
    function move(e) {
      if (!dragging) return;
      var p = point(e);
      dx = p.x - startX; dy = p.y - startY;
      var rot = dx / 18;
      card.style.transform = "translate(" + dx + "px," + dy + "px) rotate(" + rot + "deg)";
      var t = Math.min(Math.abs(dx) / 90, 1);
      yes.style.opacity = dx > 0 ? t : 0;
      no.style.opacity = dx < 0 ? t : 0;
    }
    function up() {
      if (!dragging) return;
      dragging = false;
      var threshold = 95;
      if (Math.abs(dx) > threshold) {
        var dir = dx > 0 ? 1 : -1;
        flyOut(card, dir, function () { decide(dir, q); });
      } else {
        card.style.transition = "transform .28s ease";
        card.style.transform = "translateY(0) scale(1)";
        yes.style.opacity = 0; no.style.opacity = 0;
      }
      dx = dy = 0;
    }
    function point(e) {
      if (e.touches && e.touches[0]) return { x: e.touches[0].clientX, y: e.touches[0].clientY };
      return { x: e.clientX, y: e.clientY };
    }

    if (window.PointerEvent) {
      card.addEventListener("pointerdown", down);
      card.addEventListener("pointermove", move);
      card.addEventListener("pointerup", up);
      card.addEventListener("pointercancel", up);
    } else {
      card.addEventListener("touchstart", down, { passive: true });
      card.addEventListener("touchmove", move, { passive: true });
      card.addEventListener("touchend", up);
      card.addEventListener("mousedown", down);
      window.addEventListener("mousemove", move);
      window.addEventListener("mouseup", up);
    }
  }

  // buttons + keyboard
  function programmatic(dir) {
    if (idx >= QUESTIONS.length) return;
    var top = deck.querySelector(".card:last-child");
    var q = QUESTIONS[idx];
    if (top) flyOut(top, dir, function () { decide(dir, q); });
    else decide(dir, q);
  }
  document.getElementById("btnNo").addEventListener("click", function () { programmatic(-1); });
  document.getElementById("btnYes").addEventListener("click", function () { programmatic(1); });
  document.addEventListener("keydown", function (e) {
    if (idx >= QUESTIONS.length) return;
    // only when the test is roughly in view
    var rect = deck.getBoundingClientRect();
    if (rect.bottom < 0 || rect.top > window.innerHeight) return;
    if (e.key === "ArrowRight") { e.preventDefault(); programmatic(1); }
    else if (e.key === "ArrowLeft") { e.preventDefault(); programmatic(-1); }
  });

  function winner() {
    // highest score; tie-breaks toward the LOWER level (climb only as far as needed)
    var s = score;
    if (s.l1 >= s.l2 && s.l1 >= s.l3) return "l1";
    if (s.l2 >= s.l3) return "l2";
    return "l3";
  }

  function showResult() {
    dots.innerHTML = "";
    controls.style.display = "none";
    document.querySelector(".swipe-hint").style.display = "none";
    var a = ARCHETYPES[winner()];
    var lvColor = a.lv === 1 ? "var(--l1)" : a.lv === 2 ? "var(--l2)" : "var(--l3)";

    var stepsHtml = a.steps.map(function (t) { return "<li>" + t + "</li>"; }).join("");
    var ctaHtml = a.cta.map(function (c) {
      var primary = c.href.charAt(0) === "#";
      return '<a class="btn ' + (primary ? "btn-accent" : "btn-ghost") + '" href="' + c.href + '"' +
        (primary ? "" : ' target="_blank" rel="noopener"') + ">" + c.label + "</a>";
    }).join("");

    deck.style.height = "auto";
    deck.innerHTML =
      '<div class="result">' +
        '<div class="arche-emoji">' + a.emoji + '</div>' +
        '<div class="badge">' + a.badge + '</div>' +
        '<h3>You are ' + a.name + '</h3>' +
        '<p class="lead" style="margin:10px auto 0">' + a.blurb + '</p>' +
        '<div class="reco">' +
          '<div class="reco-top">' +
            '<span class="lv-chip" style="background:' + lvColor + '">' + a.lvName + '</span>' +
            '<span class="muted" style="font-size:.85rem">your recommended starting point</span>' +
          '</div>' +
          '<ol>' + stepsHtml + '</ol>' +
          '<div class="reco-cta">' + ctaHtml + '</div>' +
        '</div>' +
        '<div class="retake"><button id="retake">↺ Retake the test</button></div>' +
      '</div>';

    document.getElementById("retake").addEventListener("click", reset);
    // celebratory xp nudge
    var r = deck.querySelector(".result");
    r.animate ? r.animate([{ opacity: 0, transform: "scale(.96)" }, { opacity: 1, transform: "scale(1)" }], { duration: 380, easing: "cubic-bezier(.2,.7,.2,1)" }) : null;
  }

  function reset() {
    idx = 0; score = { l1: 0, l2: 0, l3: 0 }; order = [];
    deck.style.height = ""; deck.style.height = "340px";
    controls.style.display = "";
    document.querySelector(".swipe-hint").style.display = "";
    buildDots(); render();
  }

  // init
  buildDots();
  render();
})();
