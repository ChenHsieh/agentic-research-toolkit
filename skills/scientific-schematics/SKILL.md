---
name: scientific-schematics
description: >
  Create publication-quality scientific workflow diagrams as interactive HTML files with
  one-click SVG export for Figma. Use this skill whenever the user wants to build or recreate
  a flowchart, decision tree, pipeline schematic, methodology diagram (CONSORT, PRISMA),
  biological pathway, or any scientific workflow figure -- including when they upload or
  describe an existing diagram they want digitized or improved. No AI image generation,
  no API keys needed. Outputs are self-contained HTML (browser-viewable, pannable/zoomable)
  plus a download-SVG button for direct Figma import. Trigger on "diagram", "schematic",
  "flowchart", "workflow figure", "pipeline figure", "recreate this diagram", or any
  image of a scientific workflow the user wants reproduced.
allowed-tools: Read Write Edit Bash
---

# Scientific Schematics -- Interactive HTML/SVG Diagrams

## What this skill produces

A **self-contained `.html` file** that:
- Opens in any browser with pan/zoom of the whole canvas
- Every node (box, diamond, oval) is **individually draggable** -- click-drag to reposition
- **Arrows re-route automatically** as nodes move, always snapping to both endpoints
- **Double-click any node** to edit its text in-place
- **Reset All** restores every node position AND the viewport to the original layout
- **Export SVG** downloads a clean vector file importable directly into Figma, Inkscape, or Illustrator
- Requires no internet connection, no external dependencies, no API keys

Save to the project's `figures/` folder. Name files descriptively, e.g. `figures/duplication_workflow.html`.

---

## Choosing an approach

| Situation | Use |
|-----------|-----|
| Simple flowchart with auto-layout | **Mermaid.js** (less code) |
| Custom shapes, colors, exact positioning, image-matching | **Hand-coded SVG** (full control) |

**Default: hand-coded SVG** for any scientific figure. Mermaid is a fallback for truly simple
diagrams where auto-layout is acceptable. Always use hand-coded SVG when the user provides an
image to recreate.

---

## Approach 1: Mermaid.js (simple flowcharts only)

Load Mermaid from CDN, render inside a `<div class="mermaid">` block, and add an SVG export
button. Use `mermaid.initialize({ theme:'base', themeVariables:{...} })` to apply scientific
styling. This approach does not support individual node dragging.

---

## Approach 2: Hand-coded SVG (standard for all scientific figures)

### Core architecture: data-driven rendering

Everything is derived from two data structures. Never hardcode positions into path strings.

```javascript
// 1. NODE DATA -- all positions and styles live here
const N = {
  input:  { type:'rect',    x:100, y:30, w:200, h:55, fill:'#2B7A80', text:'Input data', ts:14 },
  decide: { type:'diamond', cx:200, cy:200, hw:110, hh:60, fill:'#4A1860', lines:['Decision?'], ts:13 },
  out_a:  { type:'rect',    x:380, y:165, w:180, h:55, fill:'#1A4F3F', text:'Output A', ts:14 },
  out_b:  { type:'ellipse', cx:200, cy:350, rx:80, ry:45, fill:'#257525', text:'Output B', ts:13 },
};

// 2. INITIAL POSITIONS snapshot -- for "Reset All"
const INIT_POS = {};
for (const [id, n] of Object.entries(N))
  INIT_POS[id] = n.type === 'rect' ? { x: n.x, y: n.y } : { cx: n.cx, cy: n.cy };

// 3. BOUNDS HELPER -- computes edges and center from current N positions
function B(id) {
  const n = N[id];
  if (n.type === 'rect')    return { left:n.x, right:n.x+n.w, top:n.y, bottom:n.y+n.h, cx:n.x+n.w/2, cy:n.y+n.h/2 };
  if (n.type === 'diamond') return { left:n.cx-n.hw, right:n.cx+n.hw, top:n.cy-n.hh, bottom:n.cy+n.hh, cx:n.cx, cy:n.cy };
  if (n.type === 'ellipse') return { left:n.cx-n.rx, right:n.cx+n.rx, top:n.cy-n.ry, bottom:n.cy+n.ry, cx:n.cx, cy:n.cy };
}
```

### Orthogonal elbow routing (REQUIRED for all arrows)

**Always use elbow routing.** Never write `M cx bottom V top` or `M right cy H left` -- these
only stay at the source's coordinate and break when either node is dragged to a different axis.

```javascript
// bottom-of-source → top-of-target via horizontal midpoint jog
function elbowV(fid, tid) {
  const f=B(fid), t=B(tid), my=(f.bottom+t.top)/2;
  return `M ${f.cx} ${f.bottom} V ${my} H ${t.cx} V ${t.top}`;
}

// right-of-source → left-of-target via vertical midpoint jog
function elbowH(fid, tid) {
  const f=B(fid), t=B(tid), mx=(f.right+t.left)/2;
  return `M ${f.right} ${f.cy} H ${mx} V ${t.cy} H ${t.left}`;
}

// For custom routing (e.g. junction buses, around-corner paths), always read
// from B() so positions update on drag:
function customPath() {
  const f=B('syntenic'), t=B('in_syn'), jx=f.right+36;  // jx relative to current f.right
  return `M ${f.right} ${f.cy} H ${jx} V ${t.cy} H ${t.left}`;
}
```

### Arrow definitions

```javascript
const ARROWS = [
  // Vertical connection (source bottom → target top)
  { id:'a1', pathFn(){ return elbowV('input', 'decide'); } },

  // Horizontal connection with Yes/No label
  { id:'a2',
    pathFn(){ return elbowH('decide', 'out_a'); },
    label(){  const f=B('decide'), t=B('out_a'); return { text:'Yes', x:(f.right+t.left)/2, y:f.cy-10 }; }
  },

  // Vertical with label
  { id:'a3',
    pathFn(){ return elbowV('decide', 'out_b'); },
    label(){  const f=B('decide'), t=B('out_b'); return { text:'No', x:f.cx+14, y:(f.bottom+t.top)/2+5 }; }
  },

  // Dashed arrow
  { id:'a4', dashed:true, pathFn(){ return elbowV('out_a', 'out_b'); } },

  // No arrowhead (for bus spine lines)
  { id:'a5', noArrow:true, pathFn(){ const f=B('decide'), jx=f.right+40; return `M ${f.right} ${f.cy} H ${jx}`; } },
];
```

### SVG shape rendering

```javascript
function shapeHTML(id) {
  const n = N[id];
  if (n.type === 'rect') {
    const ds = n.dashed ? `stroke="${n.dstroke||'#888'}" stroke-width="1.5" stroke-dasharray="6,3"` : '';
    return `<rect x="${n.x}" y="${n.y}" width="${n.w}" height="${n.h}" rx="5" fill="${n.fill}" ${ds}/>`;
  }
  if (n.type === 'diamond') {
    const pts = `${n.cx},${n.cy-n.hh} ${n.cx+n.hw},${n.cy} ${n.cx},${n.cy+n.hh} ${n.cx-n.hw},${n.cy}`;
    return `<polygon points="${pts}" fill="${n.fill}"/>`;
  }
  if (n.type === 'ellipse')
    return `<ellipse cx="${n.cx}" cy="${n.cy}" rx="${n.rx}" ry="${n.ry}" fill="${n.fill}"/>`;
}

function textHTML(id) {
  const n = N[id];
  const tc = n.textColor || 'white';
  const fw = n.bold ? '600' : '400';
  const lh = (n.ts||14) < 13 ? 15 : 18;
  const lines = n.lines || (n.text ? [n.text] : []);
  let cx, cy;
  if (n.type === 'rect') { cx = n.x + n.w/2; cy = n.y + n.h/2; }
  else { cx = n.cx; cy = n.cy; }
  const startY = cy - (lines.length - 1) * lh / 2;
  let t = `<text text-anchor="middle" font-size="${n.ts||14}" font-weight="${fw}" fill="${tc}"
    font-family="'Helvetica Neue',Arial,sans-serif" pointer-events="none">`;
  lines.forEach((l, i) => { t += `<tspan x="${cx}" ${i===0?`y="${startY}"`:`dy="${lh}"`}>${l}</tspan>`; });
  return t + '</text>';
}
```

### Render and arrow drawing

```javascript
const arrowsLayer = document.getElementById('arrows-layer');
const nodesLayer  = document.getElementById('nodes-layer');
let selectedNode = null;

function renderArrows() {
  let html = '';
  for (const a of ARROWS) {
    const d  = a.pathFn();
    const mk = a.noArrow ? '' : `marker-end="url(#${a.dashed?'arr-d':'arr'})"`;
    const da = a.dashed ? 'stroke-dasharray="5,3"' : '';
    const sc = a.dashed ? '#999' : '#555';
    html += `<path d="${d}" stroke="${sc}" stroke-width="1.8" fill="none" ${mk} ${da}/>`;
    if (a.label) {
      const lb = a.label();
      html += `<text x="${lb.x}" y="${lb.y}" text-anchor="middle" font-size="13" fill="#222"
        font-family="'Helvetica Neue',Arial,sans-serif" pointer-events="none"
        style="paint-order:stroke;stroke:white;stroke-width:5px;stroke-linejoin:round;">${lb.text}</text>`;
    }
  }
  arrowsLayer.innerHTML = html;
}

function renderNodes() {
  let html = '';
  for (const id of Object.keys(N)) {
    const sel = id === selectedNode ? ' is-selected' : '';
    html += `<g class="node-g${sel}" data-nid="${id}">${highlightHTML(id)}${shapeHTML(id)}${textHTML(id)}</g>`;
  }
  nodesLayer.innerHTML = html;
}

function renderAll() { renderArrows(); renderNodes(); }
```

---

## Full interactive HTML template

Use this as the complete starting point for every hand-coded diagram. Fill in `N`, `INIT_POS`,
`elbowV`/`elbowH`, and `ARROWS`. The interaction code (drag, zoom, editor, reset, export) is
boilerplate -- copy it verbatim.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>DIAGRAM TITLE</title>
<style>
* { box-sizing: border-box; }
body {
  margin: 0; font-family: 'Helvetica Neue', Arial, sans-serif;
  background: #e0e0e0; overflow: hidden; user-select: none; -webkit-user-select: none;
}
#toolbar {
  position: fixed; top: 0; left: 0; right: 0; height: 48px;
  background: #fff; border-bottom: 1px solid #ddd;
  display: flex; align-items: center; padding: 0 18px; gap: 12px;
  z-index: 100; box-shadow: 0 1px 5px rgba(0,0,0,.1);
}
#toolbar h2 { margin: 0; font-size: 15px; font-weight: 500; color: #333; flex: 1; }
.hint { font-size: 12px; color: #bbb; white-space: nowrap; }
button {
  padding: 5px 14px; border: 1px solid #ccc; border-radius: 5px;
  cursor: pointer; font-size: 13px; background: #fff; color: #333; white-space: nowrap;
}
button:hover { background: #f5f5f5; }
button.primary { background: #2B7A80; color: white; border-color: #2B7A80; }
button.primary:hover { background: #226368; }
#viewport { position: fixed; top: 48px; left: 0; right: 0; bottom: 0; overflow: hidden; }
#scene { transform-origin: 0 0; display: block; }
.node-g { cursor: grab; }
.node-g.is-selected .sel-hl { opacity: 1 !important; }
.node-g .sel-hl { opacity: 0; transition: opacity 0.1s; }
.node-g:hover .sel-hl { opacity: 0.4; }
body.node-dragging * { cursor: grabbing !important; }
body.canvas-dragging { cursor: grabbing !important; }
#text-editor-wrap {
  display: none; position: fixed; z-index: 300; background: transparent;
}
#text-editor-wrap.active { display: block; }
#text-editor {
  width: 100%; background: rgba(255,255,255,0.97);
  border: 2.5px solid #3A8FFF; border-radius: 6px;
  font-family: 'Helvetica Neue', Arial, sans-serif;
  text-align: center; resize: none; outline: none;
  color: #1a1a1a; line-height: 1.4; padding: 4px 8px;
  box-shadow: 0 4px 20px rgba(58,143,255,0.25);
}
#edit-hint { font-size: 11px; color: #888; text-align: center; margin-top: 3px; white-space: nowrap; }
</style>
</head>
<body>

<div id="toolbar">
  <h2>DIAGRAM TITLE</h2>
  <span class="hint">Drag nodes · Double-click to edit text · Scroll to zoom · Drag canvas to pan</span>
  <button onclick="resetView()">Reset All</button>
  <button class="primary" onclick="exportSVG()">Export SVG for Figma</button>
</div>

<div id="viewport">
<svg id="scene" width="WIDTH" height="HEIGHT" viewBox="0 0 WIDTH HEIGHT"
     xmlns="http://www.w3.org/2000/svg" style="background:white;">
  <defs>
    <marker id="arr"   markerWidth="9" markerHeight="9" refX="7" refY="3.5" orient="auto">
      <path d="M0,0 L0,7 L9,3.5 z" fill="#555"/>
    </marker>
    <marker id="arr-d" markerWidth="9" markerHeight="9" refX="7" refY="3.5" orient="auto">
      <path d="M0,0 L0,7 L9,3.5 z" fill="#999"/>
    </marker>
  </defs>
  <g id="arrows-layer"></g>
  <g id="nodes-layer"></g>
</svg>
</div>

<div id="text-editor-wrap">
  <textarea id="text-editor" rows="2" spellcheck="false"></textarea>
  <div id="edit-hint">Enter to save &nbsp;·&nbsp; Shift+Enter for new line &nbsp;·&nbsp; Esc to cancel</div>
</div>

<script>
'use strict';

// ═══════════════════════════════════════════════════════
// DATA MODEL  ← edit N and ARROWS; leave the rest alone
// ═══════════════════════════════════════════════════════

const N = {
  // FILL IN YOUR NODES HERE
  // rect:    { type:'rect',    x, y, w, h, fill, text OR lines:[], ts, bold, dashed, dstroke, textColor }
  // diamond: { type:'diamond', cx, cy, hw, hh, fill, lines:[], ts }
  // ellipse: { type:'ellipse', cx, cy, rx, ry, fill, text OR lines:[], ts }
};

const INIT_POS = {};
for (const [id, n] of Object.entries(N))
  INIT_POS[id] = n.type === 'rect' ? { x: n.x, y: n.y } : { cx: n.cx, cy: n.cy };

function B(id) {
  const n = N[id];
  if (n.type === 'rect')    return { left:n.x, right:n.x+n.w, top:n.y, bottom:n.y+n.h, cx:n.x+n.w/2, cy:n.y+n.h/2 };
  if (n.type === 'diamond') return { left:n.cx-n.hw, right:n.cx+n.hw, top:n.cy-n.hh, bottom:n.cy+n.hh, cx:n.cx, cy:n.cy };
  if (n.type === 'ellipse') return { left:n.cx-n.rx, right:n.cx+n.rx, top:n.cy-n.ry, bottom:n.cy+n.ry, cx:n.cx, cy:n.cy };
}

// Orthogonal elbow helpers -- ALWAYS use these instead of bare V/H paths
function elbowV(fid, tid) {
  const f=B(fid), t=B(tid), my=(f.bottom+t.top)/2;
  return `M ${f.cx} ${f.bottom} V ${my} H ${t.cx} V ${t.top}`;
}
function elbowH(fid, tid) {
  const f=B(fid), t=B(tid), mx=(f.right+t.left)/2;
  return `M ${f.right} ${f.cy} H ${mx} V ${t.cy} H ${t.left}`;
}

const ARROWS = [
  // FILL IN YOUR ARROWS HERE
  // { id:'a1', pathFn(){ return elbowV('src', 'dst'); } }
  // { id:'a2', pathFn(){ return elbowH('src', 'dst'); },
  //            label(){  const f=B('src'), t=B('dst'); return { text:'Yes', x:(f.right+t.left)/2, y:f.cy-10 }; } }
];

// ═══════════════════════════════════════════════════════
// RENDERING  ← boilerplate, do not change
// ═══════════════════════════════════════════════════════

const arrowsLayer = document.getElementById('arrows-layer');
const nodesLayer  = document.getElementById('nodes-layer');
let selectedNode  = null;

function shapeHTML(id) {
  const n = N[id];
  if (n.type === 'rect') {
    const ds = n.dashed ? `stroke="${n.dstroke||n.stroke||'#888'}" stroke-width="1.5" stroke-dasharray="6,3"` : '';
    return `<rect x="${n.x}" y="${n.y}" width="${n.w}" height="${n.h}" rx="5" fill="${n.fill}" ${ds}/>`;
  }
  if (n.type === 'diamond') {
    const pts = `${n.cx},${n.cy-n.hh} ${n.cx+n.hw},${n.cy} ${n.cx},${n.cy+n.hh} ${n.cx-n.hw},${n.cy}`;
    return `<polygon points="${pts}" fill="${n.fill}"/>`;
  }
  if (n.type === 'ellipse')
    return `<ellipse cx="${n.cx}" cy="${n.cy}" rx="${n.rx}" ry="${n.ry}" fill="${n.fill}"/>`;
}

function highlightHTML(id) {
  const n = N[id], c = '#3A8FFF';
  if (n.type === 'rect')
    return `<rect class="sel-hl" x="${n.x-4}" y="${n.y-4}" width="${n.w+8}" height="${n.h+8}" rx="8" fill="none" stroke="${c}" stroke-width="2" stroke-dasharray="5,3"/>`;
  if (n.type === 'diamond') {
    const pts = `${n.cx},${n.cy-n.hh-5} ${n.cx+n.hw+5},${n.cy} ${n.cx},${n.cy+n.hh+5} ${n.cx-n.hw-5},${n.cy}`;
    return `<polygon class="sel-hl" points="${pts}" fill="none" stroke="${c}" stroke-width="2" stroke-dasharray="5,3"/>`;
  }
  if (n.type === 'ellipse')
    return `<ellipse class="sel-hl" cx="${n.cx}" cy="${n.cy}" rx="${n.rx+5}" ry="${n.ry+5}" fill="none" stroke="${c}" stroke-width="2" stroke-dasharray="5,3"/>`;
}

function textHTML(id) {
  const n = N[id];
  const tc = n.textColor || 'white';
  const fw = n.bold ? '600' : '400';
  const lh = (n.ts||14) < 13 ? 15 : 18;
  const lines = n.lines || (n.text ? [n.text] : []);
  let cx, cy;
  if (n.type === 'rect') { cx = n.x + n.w/2; cy = n.y + n.h/2; }
  else { cx = n.cx; cy = n.cy; }
  const startY = cy - (lines.length - 1) * lh / 2;
  let t = `<text text-anchor="middle" font-size="${n.ts||14}" font-weight="${fw}" fill="${tc}" font-family="'Helvetica Neue',Arial,sans-serif" pointer-events="none">`;
  lines.forEach((l, i) => { t += `<tspan x="${cx}" ${i===0?`y="${startY}"`:`dy="${lh}"`}>${l}</tspan>`; });
  return t + '</text>';
}

function renderNodes() {
  let html = '';
  for (const id of Object.keys(N)) {
    const sel = id === selectedNode ? ' is-selected' : '';
    html += `<g class="node-g${sel}" data-nid="${id}">${highlightHTML(id)}${shapeHTML(id)}${textHTML(id)}</g>`;
  }
  nodesLayer.innerHTML = html;
}

function renderArrows() {
  let html = '';
  for (const a of ARROWS) {
    const d  = a.pathFn();
    const mk = a.noArrow ? '' : `marker-end="url(#${a.dashed?'arr-d':'arr'})"`;
    const da = a.dashed ? 'stroke-dasharray="5,3"' : '';
    const sc = a.dashed ? '#999' : '#555';
    html += `<path d="${d}" stroke="${sc}" stroke-width="1.8" fill="none" ${mk} ${da}/>`;
    if (a.label) {
      const lb = a.label();
      html += `<text x="${lb.x}" y="${lb.y}" text-anchor="middle" font-size="13" fill="#222"
        font-family="'Helvetica Neue',Arial,sans-serif" pointer-events="none"
        style="paint-order:stroke;stroke:white;stroke-width:5px;stroke-linejoin:round;">${lb.text}</text>`;
    }
  }
  arrowsLayer.innerHTML = html;
}

function renderAll() { renderArrows(); renderNodes(); }

// ═══════════════════════════════════════════════════════
// VIEWPORT -- pan + zoom
// ═══════════════════════════════════════════════════════

let vpScale = 1, vpTx = 40, vpTy = 30;
const INIT_VP = { scale: 1, tx: 40, ty: 30 };

function applyVP() {
  document.getElementById('scene').style.transform = `translate(${vpTx}px,${vpTy}px) scale(${vpScale})`;
}
applyVP();

function vpRect() { return document.getElementById('viewport').getBoundingClientRect(); }

function clientToSVG(cx, cy) {
  const r = vpRect();
  return { x: (cx - r.left - vpTx) / vpScale, y: (cy - r.top - vpTy) / vpScale };
}

function svgToScreen(svgX, svgY) {
  const r = vpRect();
  return { x: r.left + vpTx + svgX * vpScale, y: r.top + vpTy + svgY * vpScale };
}

// ═══════════════════════════════════════════════════════
// DRAG -- nodes (individual) + canvas (pan)
// ═══════════════════════════════════════════════════════

let nodeDrag = null, canvasDrag = null, wasDragged = false;

document.getElementById('scene').addEventListener('mousedown', e => {
  const g = e.target.closest('[data-nid]');
  if (!g) return;
  e.stopPropagation(); e.preventDefault();
  const nid = g.dataset.nid, n = N[nid];
  const pt = clientToSVG(e.clientX, e.clientY);
  nodeDrag = { nid, startSVG: pt, origX: n.type==='rect'?n.x:n.cx, origY: n.type==='rect'?n.y:n.cy };
  selectedNode = nid; document.body.classList.add('node-dragging'); renderNodes();
}, true);

document.getElementById('viewport').addEventListener('mousedown', e => {
  if (e.target.closest('[data-nid]')) return;
  canvasDrag = { sx: e.clientX, sy: e.clientY, origTx: vpTx, origTy: vpTy };
  document.body.classList.add('canvas-dragging');
});

window.addEventListener('mousemove', e => {
  if (nodeDrag) {
    const pt = clientToSVG(e.clientX, e.clientY);
    const dx = pt.x - nodeDrag.startSVG.x, dy = pt.y - nodeDrag.startSVG.y;
    if (Math.abs(dx) > 2 || Math.abs(dy) > 2) wasDragged = true;
    const n = N[nodeDrag.nid];
    if (n.type === 'rect') { n.x = nodeDrag.origX + dx; n.y = nodeDrag.origY + dy; }
    else { n.cx = nodeDrag.origX + dx; n.cy = nodeDrag.origY + dy; }
    renderAll();
  } else if (canvasDrag) {
    vpTx = canvasDrag.origTx + (e.clientX - canvasDrag.sx);
    vpTy = canvasDrag.origTy + (e.clientY - canvasDrag.sy);
    applyVP();
  }
});

window.addEventListener('mouseup', () => {
  nodeDrag = null; canvasDrag = null;
  document.body.classList.remove('node-dragging', 'canvas-dragging');
  setTimeout(() => { wasDragged = false; }, 50);
});

document.getElementById('viewport').addEventListener('click', e => {
  if (!e.target.closest('[data-nid]')) { selectedNode = null; renderNodes(); }
});

document.getElementById('viewport').addEventListener('wheel', e => {
  e.preventDefault();
  const r = vpRect(), mx = e.clientX - r.left, my = e.clientY - r.top;
  const ns = Math.max(0.15, Math.min(6, vpScale * (e.deltaY < 0 ? 1.12 : 0.89)));
  vpTx = mx - (mx - vpTx) * ns / vpScale;
  vpTy = my - (my - vpTy) * ns / vpScale;
  vpScale = ns; applyVP();
}, { passive: false });

// ═══════════════════════════════════════════════════════
// DOUBLE-CLICK TEXT EDITOR
// ═══════════════════════════════════════════════════════

let editingNid = null;
const editorWrap = document.getElementById('text-editor-wrap');
const editorTA   = document.getElementById('text-editor');

function openEditor(nid) {
  if (editingNid) closeEditor(false);
  editingNid = nid;
  const n = N[nid], b = B(nid);
  const tl = svgToScreen(b.left, b.top);
  const w = (b.right - b.left) * vpScale, h = (b.bottom - b.top) * vpScale;
  editorWrap.style.left  = tl.x + 'px';
  editorWrap.style.top   = tl.y + 'px';
  editorWrap.style.width = Math.max(w, 80) + 'px';
  const lines = n.lines || (n.text ? [n.text] : ['']);
  editorTA.value = lines.join('\n');
  editorTA.style.fontSize  = Math.max(11, (n.ts||14) * vpScale) + 'px';
  editorTA.style.minHeight = Math.max(32, h) + 'px';
  editorTA.rows = lines.length + 1;
  editorWrap.classList.add('active');
  editorTA.focus(); editorTA.select();
}

function closeEditor(save) {
  if (!editingNid) return;
  if (save) {
    const lines = editorTA.value.split('\n').map(l => l.trim()).filter(Boolean);
    const n = N[editingNid];
    if (lines.length === 1) { n.text = lines[0]; delete n.lines; }
    else { n.lines = lines; delete n.text; }
    renderAll();
  }
  editorWrap.classList.remove('active'); editingNid = null;
}

editorTA.addEventListener('keydown', e => {
  if (e.key === 'Escape') { e.preventDefault(); closeEditor(false); }
  if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); closeEditor(true); }
});
editorTA.addEventListener('blur', () => { setTimeout(() => { if (editingNid) closeEditor(true); }, 80); });

document.getElementById('scene').addEventListener('dblclick', e => {
  const g = e.target.closest('[data-nid]');
  if (!g || wasDragged) return;
  e.preventDefault(); e.stopPropagation();
  openEditor(g.dataset.nid);
}, true);

document.getElementById('viewport').addEventListener('mousedown', e => {
  if (editingNid && !editorWrap.contains(e.target) && !e.target.closest('[data-nid]'))
    closeEditor(true);
});

// ═══════════════════════════════════════════════════════
// TOUCH SUPPORT
// ═══════════════════════════════════════════════════════

let touchNode = null, touchCanvas = null, lastTap = 0;

document.getElementById('scene').addEventListener('touchstart', e => {
  const g = e.target.closest('[data-nid]');
  if (g && e.touches.length === 1) {
    e.stopPropagation();
    const nid = g.dataset.nid, n = N[nid];
    const pt = clientToSVG(e.touches[0].clientX, e.touches[0].clientY);
    touchNode = { nid, startSVG: pt, origX: n.type==='rect'?n.x:n.cx, origY: n.type==='rect'?n.y:n.cy };
    selectedNode = nid; renderNodes();
    const now = Date.now();
    if (now - lastTap < 300) openEditor(nid);
    lastTap = now;
  }
}, { passive: false });

document.getElementById('viewport').addEventListener('touchstart', e => {
  if (!e.target.closest('[data-nid]') && e.touches.length === 1)
    touchCanvas = { sx: e.touches[0].clientX, sy: e.touches[0].clientY, origTx: vpTx, origTy: vpTy };
}, { passive: true });

window.addEventListener('touchmove', e => {
  if (touchNode && e.touches.length === 1) {
    e.preventDefault();
    const pt = clientToSVG(e.touches[0].clientX, e.touches[0].clientY);
    const dx = pt.x - touchNode.startSVG.x, dy = pt.y - touchNode.startSVG.y;
    const n = N[touchNode.nid];
    if (n.type === 'rect') { n.x = touchNode.origX + dx; n.y = touchNode.origY + dy; }
    else { n.cx = touchNode.origX + dx; n.cy = touchNode.origY + dy; }
    renderAll();
  } else if (touchCanvas && e.touches.length === 1) {
    vpTx = touchCanvas.origTx + (e.touches[0].clientX - touchCanvas.sx);
    vpTy = touchCanvas.origTy + (e.touches[0].clientY - touchCanvas.sy);
    applyVP();
  }
}, { passive: false });

window.addEventListener('touchend', () => { touchNode = null; touchCanvas = null; });

// ═══════════════════════════════════════════════════════
// RESET + EXPORT
// ═══════════════════════════════════════════════════════

function resetView() {
  closeEditor(false);
  for (const [id, orig] of Object.entries(INIT_POS)) {
    const n = N[id];
    if (n.type === 'rect') { n.x = orig.x; n.y = orig.y; }
    else { n.cx = orig.cx; n.cy = orig.cy; }
  }
  vpScale = INIT_VP.scale; vpTx = INIT_VP.tx; vpTy = INIT_VP.ty;
  selectedNode = null; applyVP(); renderAll();
}

function exportSVG() {
  closeEditor(true);
  const src = document.getElementById('scene');
  const clone = src.cloneNode(true);
  clone.removeAttribute('style');
  clone.setAttribute('xmlns', 'http://www.w3.org/2000/svg');
  clone.querySelectorAll('.sel-hl').forEach(el => el.setAttribute('opacity', '0'));
  const st = document.createElementNS('http://www.w3.org/2000/svg', 'style');
  st.textContent = "text,tspan{font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;}";
  clone.insertBefore(st, clone.firstChild);
  const blob = new Blob([clone.outerHTML], { type: 'image/svg+xml;charset=utf-8' });
  const url  = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url; a.download = 'diagram.svg';
  document.body.appendChild(a); a.click();
  document.body.removeChild(a);
  setTimeout(() => URL.revokeObjectURL(url), 1000);
}

// Initial render
renderAll();
</script>
</body>
</html>
```

---

## Color palette (colorblind-safe defaults)

| Role | Hex | Use for |
|------|-----|---------|
| `#2B7A80` | Teal | Input data / source nodes |
| `#7A2D10` | Dark brown | Processing / computation boxes |
| `#4A1860` | Deep purple | Decision diamonds |
| `#1A4F3F` | Forest green | Primary outputs |
| `#1A3F5A` | Dark blue | Secondary outputs |
| `#1A2F50` | Navy | Terminal / final categories |
| `#257525` | Green | Intermediate classification nodes |
| `#C07C10` | Amber | Alternate inputs / highlights |
| `#1A5A5A` | Dark teal | Sub-categories (pair with dashed border) |

Text: always white on dark backgrounds. Default `ts` (font-size): 14. Font: Helvetica Neue / Arial / sans-serif.

For dashed-border boxes (e.g. optional categories): `fill:'white', textColor:'#333', dashed:true, dstroke:'#888'`.

---

## Node property reference

| Property | Applies to | Description |
|----------|------------|-------------|
| `type` | all | `'rect'` / `'diamond'` / `'ellipse'` |
| `x, y` | rect | top-left corner |
| `w, h` | rect | width, height |
| `cx, cy` | diamond, ellipse | center point |
| `hw, hh` | diamond | half-width, half-height |
| `rx, ry` | ellipse | x-radius, y-radius |
| `fill` | all | background color |
| `text` | all | single-line label string |
| `lines` | all | multi-line label array (use instead of `text`) |
| `ts` | all | font-size in px (default 14) |
| `bold` | all | `true` for font-weight 600 |
| `textColor` | all | label color (default `'white'`) |
| `dashed` | rect | dashed border |
| `dstroke` | rect | dashed border color (default `'#888'`) |

---

## Recreating a diagram from an image

1. Identify every unique node: shape, color, border style (solid vs dashed), label text
2. Trace all connections -- note Yes/No labels on every decision branch
3. Lay out nodes first in `N` using rough coordinates; refine after first render
4. Define arrows second using `elbowV` / `elbowH` for all connections; use custom `B()`-based paths only for routing around specific shapes (bus lines, around-corners)
5. Match colors to the palette above; preserve any dashed borders exactly
6. Check that every decision diamond has both branches labeled

---

## Quality checklist

- [ ] `elbowV` / `elbowH` used for ALL arrows (no bare `V ${t.top}` or `H ${t.left}` paths)
- [ ] All nodes have readable text, minimum ts:12
- [ ] Arrowheads visible and pointing correct direction
- [ ] Yes/No labels on every decision diamond branch
- [ ] Double-click text editing works on each node
- [ ] Drag a node -- all connected arrows follow correctly
- [ ] Reset All restores every node position AND viewport
- [ ] Export SVG button produces a valid downloadable file
- [ ] File opens with no external dependencies (no CDN for the data-driven version)
- [ ] Title matches user specification
