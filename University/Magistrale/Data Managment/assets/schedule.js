'use strict';
// Read/write schedules: parsing, conflicts, precedence graph, random practice.
// Widgets: <div class="sched-drill" data-precedence="r1(x) w2(x) ..." [data-random]></div>
//          <div class="tpl-drill" data-schedule="r1(x) w2(x) ..." [data-random]></div>  (2PL, X and S/X)
// No network, tracking or persistence: answers stay in the open page.

const Schedule = (() => {
  const parse = src => [...src.matchAll(/([rw])\s*(\d+)\s*\(\s*(\w+)\s*\)/gi)]
    .map((m, i) => ({op: m[1].toLowerCase(), tx: +m[2], el: m[3], i}));
  const fmt = a => `${a.op}${a.tx}(${a.el})`;
  const txs = S => [...new Set(S.map(a => a.tx))].sort((a, b) => a - b);
  const conflict = (a, b) => a.tx !== b.tx && a.el === b.el && (a.op === 'w' || b.op === 'w');

  // Edge "i>j" → every conflicting pair (earlier action of Ti, later of Tj) that justifies it.
  function edges(S) {
    const out = new Map();
    S.forEach((a, i) => S.slice(i + 1).forEach(b => {
      if (!conflict(a, b)) return;
      const k = `${a.tx}>${b.tx}`;
      if (!out.has(k)) out.set(k, []);
      out.get(k).push([a, b]);
    }));
    return out;
  }

  // Kahn: a topological order, or null when the graph has a cycle.
  function topo(nodes, keys) {
    const inDeg = new Map(nodes.map(n => [n, 0]));
    const pairs = [...keys].map(k => k.split('>').map(Number));
    pairs.forEach(([, j]) => inDeg.set(j, inDeg.get(j) + 1));
    const order = [], ready = nodes.filter(n => !inDeg.get(n));
    while (ready.length) {
      const n = ready.shift();
      order.push(n);
      pairs.filter(([i]) => i === n).forEach(([, j]) => {
        inDeg.set(j, inDeg.get(j) - 1);
        if (!inDeg.get(j)) ready.push(j);
      });
    }
    return order.length === nodes.length ? order : null;
  }

  // One cycle as a node list [a, b, ..., a], or null.
  function cycle(nodes, keys) {
    const adj = new Map(nodes.map(n => [n, []]));
    [...keys].forEach(k => { const [i, j] = k.split('>').map(Number); adj.get(i).push(j); });
    const state = new Map(), stack = [];
    const dfs = n => {
      state.set(n, 1); stack.push(n);
      for (const m of adj.get(n)) {
        if (state.get(m) === 1) return [...stack.slice(stack.indexOf(m)), m];
        if (!state.get(m)) { const c = dfs(m); if (c) return c; }
      }
      state.set(n, 2); stack.pop();
      return null;
    };
    for (const n of nodes) if (!state.get(n)) { const c = dfs(n); if (c) return c; }
    return null;
  }

  // Random interleaving of nTx transactions, each with 2–3 distinct actions on x, y and at least one write.
  function random(nTx = 3) {
    const pick = arr => arr[Math.floor(Math.random() * arr.length)];
    const actions = t => {
      for (;;) {
        const a = ['rx', 'ry', 'wx', 'wy'].sort(() => Math.random() - .5).slice(0, 2 + (Math.random() < .4));
        if (a.some(s => s[0] === 'w')) return a.map(s => ({op: s[0], tx: t, el: s[1]}));
      }
    };
    const acyclic = Math.random() < .5;  // drawn once, so the verdict can't be guessed
    for (;;) {
      const queues = Array.from({length: nTx}, (_, t) => actions(t + 1));
      const S = [];
      while (queues.some(q => q.length)) S.push(pick(queues.filter(q => q.length)).shift());
      S.forEach((a, i) => { a.i = i; });
      const E = edges(S);
      if (E.size >= 2 && !cycle(txs(S), new Set(E.keys())) === acyclic) return S;
    }
  }

  // 2PL membership. Under 2PL each Ti has a lock point LP: every lock before it, every unlock after it.
  // Given LP, Ti must hold A at least over [min(first, LP), max(last, LP)]; S is 2PL iff some choice
  // of distinct LPs makes these minimal intervals legal. shared=false: exclusive locks only;
  // shared=true: sl for reads, xl from the first write (lock upgrade allowed).
  function twoPL(S, shared) {
    const T = txs(S), m = T.length, D = .01;
    const use = new Map(T.map(t => [t, new Map()]));
    S.forEach((a, k) => {
      const u = use.get(a.tx), p = k + 1, e = u.get(a.el) || {first: p, firstW: null};
      e.last = p;
      if (a.op === 'w' && e.firstW === null) e.firstW = p;
      u.set(a.el, e);
    });
    const span = t => { const ps = S.filter(a => a.tx === t).map(a => a.i + 1); return [Math.min(...ps), Math.max(...ps)]; };
    const intervals = (t, lp) => [...use.get(t)].flatMap(([el, e]) => {
      const s = Math.min(e.first - D, lp), end = Math.max(e.last + D, lp);
      if (!shared) return [{t, el, s, e: end, x: true}];
      if (e.firstW === null) return [{t, el, s, e: end, x: false}];
      const xs = Math.min(e.firstW - D, lp);
      return [...(s < xs ? [{t, el, s, e: xs, x: false, up: true}] : []), {t, el, s: xs, e: end, x: true}];
    });
    const clash = (I, J) => I.some(a => J.some(b => a.el === b.el && (a.x || b.x) && a.s < b.e && b.s < a.e));
    const chosen = [];
    const search = k => {
      if (k === m) return true;
      const t = T[k], [f, l] = span(t);
      for (let g = f - 1; g <= l; g++) for (let s = 1; s <= m; s++) {
        const lp = g + s / (m + 1);
        if (chosen.some(c => c.lp === lp)) continue;
        const I = intervals(t, lp);
        if (chosen.some(c => clash(I, c.I))) continue;
        chosen.push({t, lp, I});
        if (search(k + 1)) return true;
        chosen.pop();
      }
      return false;
    };
    if (search(0)) {
      const ev = S.map((a, k) => ({time: k + 1, ord: 1, txt: fmt(a)}));
      chosen.forEach(({t, I}) => {
        I.forEach(iv => ev.push({time: iv.s, ord: 0, txt: `${shared ? (iv.x ? 'xl' : 'sl') : 'l'}${t}(${iv.el})`}));
        I.filter(iv => !iv.up).forEach(iv => ev.push({time: iv.e, ord: 2, txt: `u${t}(${iv.el})`}));
      });
      ev.sort((a, b) => a.time - b.time || a.ord - b.ord);
      return {ok: true, witness: ev.map(e => e.txt).join(' ')};
    }
    return {ok: false, reason: twoPLReason(S, shared)};
  }

  // A human-readable obstacle: Ti must unlock A before someone else uses it, yet later needs B,
  // and another transaction uses B in between.
  function twoPLReason(S, shared) {
    const T = txs(S), keys = new Set(edges(S).keys()), cyc = cycle(T, keys);
    if (cyc) return `Non è conflict-serializable (ciclo ${cyc.map(t => 'T' + t).join(' → ')}), e ogni schedule 2PL è conflict-serializable.`;
    const clashes = (a, b) => a.tx !== b.tx && a.el === b.el && (!shared || a.op === 'w' || b.op === 'w');
    for (const t of T) {
      const mine = S.filter(a => a.tx === t);
      const force = S.find(b => mine.some(a => a.i < b.i && clashes(a, b)));
      if (!force) continue;
      const held = mine.find(a => a.i < force.i && clashes(a, force));
      for (const later of mine.filter(a => a.i > force.i)) {
        if (later.el === force.el && (!shared || later.op === 'w' || force.op === 'w'))
          return `T${t} deve rilasciare ${held.el} prima di ${fmt(force)}, ma poi gli serve di nuovo per ${fmt(later)}: riprenderlo sarebbe un lock dopo un unlock.`;
        const writes = mine.some(a => a.el === later.el && a.op === 'w');
        const other = S.find(b => b.i > force.i && b.i < later.i && b.tx !== t && b.el === later.el &&
          (!shared || writes || b.op === 'w'));
        if (other) return `T${t} deve rilasciare ${held.el} prima di ${fmt(force)}, quindi a quel punto deve già avere il lock${shared && writes ? ' esclusivo' : ''} su ${later.el} per ${fmt(later)}. Ma in mezzo c’è ${fmt(other)}, che ${shared ? 'è incompatibile con quel lock' : 'ha bisogno dello stesso lock'}.`;
      }
    }
    return 'I vincoli si incastrano a catena: ogni modo di inserire lock e unlock viola la legalità o le due fasi. Prova a costruire i lock passo passo, transazione per transazione.';
  }

  // Random schedule whose 2PL verdicts (X only / S and X) fall equally often in the three possible pairs.
  function random2PL() {
    const want = Math.floor(Math.random() * 3);  // 0: no/no, 1: no/yes, 2: yes/yes
    for (;;) {
      const S = random();
      const kind = twoPL(S, false).ok ? 2 : twoPL(S, true).ok ? 1 : 0;
      if (kind === want) return S;
    }
  }

  return {parse, fmt, txs, conflict, edges, topo, cycle, random, twoPL, random2PL};
})();

// Precedence graph as inline SVG; edges on the cycle are highlighted.
function precedenceSvg(nodes, keys, cyc) {
  const R = 18, cx = 150, cy = 105, r = nodes.length > 2 ? 70 : 60;
  const pos = new Map(nodes.map((n, k) => {
    const t = -Math.PI / 2 + 2 * Math.PI * k / nodes.length;
    return [n, [cx + r * Math.cos(t), cy + r * Math.sin(t)]];
  }));
  const onCycle = new Set();
  if (cyc) cyc.slice(1).forEach((n, k) => onCycle.add(`${cyc[k]}>${n}`));
  const lines = [...keys].map(k => {
    const [i, j] = k.split('>').map(Number);
    const [x1, y1] = pos.get(i), [x2, y2] = pos.get(j);
    const dx = x2 - x1, dy = y2 - y1, L = Math.hypot(dx, dy), ux = dx / L, uy = dy / L;
    const bend = keys.has(`${j}>${i}`) ? 16 : 0;  // two-way pair: bend both arcs apart
    const mx = (x1 + x2) / 2 - uy * bend, my = (y1 + y2) / 2 + ux * bend;
    const sx = x1 + ux * R, sy = y1 + uy * R, ex = x2 - ux * (R + 4), ey = y2 - uy * (R + 4);
    const cls = onCycle.has(k) ? ' class="cyc"' : '';
    return `<path${cls} d="M${sx},${sy} Q${mx},${my} ${ex},${ey}" marker-end="url(#${onCycle.has(k) ? 'ah-c' : 'ah'})"/>`;
  }).join('');
  const circles = nodes.map(n => { const [x, y] = pos.get(n);
    return `<circle cx="${x}" cy="${y}" r="${R}"/><text x="${x}" y="${y + 5}" text-anchor="middle">T${n}</text>`; }).join('');
  return `<svg class="pgraph" viewBox="0 0 300 210" role="img" aria-label="Precedence graph">
<defs><marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0L10,5L0,10z" class="tip"/></marker>
<marker id="ah-c" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0L10,5L0,10z" class="tip cyc"/></marker></defs>
${lines}${circles}</svg>`;
}

if (typeof module !== 'undefined') module.exports = {Schedule, precedenceSvg};
const chips = S => `<div class="sched">${S.map((a, k) =>
  `<span class="act t${a.tx}"><sub>${k + 1}</sub>${a.op}<b>${a.tx}</b>(${a.el})</span>`).join('')}</div>`;

if (typeof document !== 'undefined') {
  document.querySelectorAll('.tpl-drill').forEach((box, n) => {
    let S;
    const yn = (name, q) => `<p class="meta">${q}</p><fieldset class="options inline">
<label><input type="radio" name="${name}" value="yes"> Sì, è 2PL</label><label><input type="radio" name="${name}" value="no"> No, non è 2PL</label></fieldset>`;
    const render = () => {
      box.innerHTML = chips(S) + yn(`tx${n}`, '1 · Con soli lock esclusivi (l, u)?') + yn(`ts${n}`, '2 · Con lock condivisi ed esclusivi (sl, xl, u)?') +
        `<div class="actions"><button type="button" data-check>Controlla</button>${box.hasAttribute('data-random') ?
        '<button type="button" class="secondary" data-new>Nuovo schedule</button>' : ''}</div><div class="feedback" role="status" aria-live="polite"></div>`;
      box.querySelector('[data-check]').onclick = check;
      const again = box.querySelector('[data-new]');
      if (again) again.onclick = () => { S = Schedule.random2PL(); render(); };
    };
    const check = () => {
      const out = box.querySelector('.feedback');
      const parts = [[`tx${n}`, false, 'Soli lock esclusivi'], [`ts${n}`, true, 'Lock condivisi ed esclusivi']];
      if (parts.some(([name]) => !box.querySelector(`input[name=${name}]:checked`))) {
        out.dataset.state = 'incorrect'; out.textContent = 'Rispondi a entrambe le domande.'; return;
      }
      let all = true;
      out.innerHTML = parts.map(([name, shared, label]) => {
        const r = Schedule.twoPL(S, shared), ok = (box.querySelector(`input[name=${name}]:checked`).value === 'yes') === r.ok;
        all = all && ok;
        return `<p><strong>${label}: ${ok ? 'corretto' : 'sbagliato'}</strong>, ${r.ok ? 'è' : 'non è'} 2PL.</p>` +
          (r.ok ? `<pre><code>${r.witness}</code></pre>` : `<p>${r.reason}</p>`);
      }).join('');
      out.dataset.state = all ? 'correct' : 'incorrect';
    };
    S = box.dataset.schedule ? Schedule.parse(box.dataset.schedule) : Schedule.random2PL();
    render();
  });

  document.querySelectorAll('.sched-drill').forEach((box, n) => {
    let S;
    const name = `pg${n}`;
    const render = () => {
      const T = Schedule.txs(S);
      const grid = T.flatMap(i => T.filter(j => j !== i).map(j =>
        `<label><input type="checkbox" value="${i}>${j}"> T${i} → T${j}</label>`)).join('');
      box.innerHTML = `${chips(S)}
<p class="meta">1 · Spunta tutti gli archi del precedence graph.</p><fieldset class="edges">${grid}</fieldset>
<p class="meta">2 · Lo schedule è conflict-serializable?</p>
<fieldset class="options inline"><label><input type="radio" name="${name}" value="yes"> Sì, il grafo è aciclico</label>
<label><input type="radio" name="${name}" value="no"> No, il grafo ha un ciclo</label></fieldset>
<div class="actions"><button type="button" data-check>Controlla</button>${box.hasAttribute('data-random') ?
  '<button type="button" class="secondary" data-new>Nuovo schedule</button>' : ''}</div>
<div class="feedback" role="status" aria-live="polite"></div>`;
      box.querySelector('[data-check]').onclick = check;
      const again = box.querySelector('[data-new]');
      if (again) again.onclick = () => { S = Schedule.random(); render(); };
    };
    const check = () => {
      const T = Schedule.txs(S), E = Schedule.edges(S), keys = new Set(E.keys());
      const ticked = new Set([...box.querySelectorAll('.edges input:checked')].map(c => c.value));
      const verdict = box.querySelector(`input[name=${name}]:checked`);
      const out = box.querySelector('.feedback');
      const why = k => E.get(k).map(([a, b]) => `${Schedule.fmt(a)} prima di ${Schedule.fmt(b)}`).join('; ');
      const missing = [...keys].filter(k => !ticked.has(k)), extra = [...ticked].filter(k => !keys.has(k));
      const arrow = k => k.replace('>', ' → T').replace(/^/, 'T');
      const msgs = [];
      missing.forEach(k => msgs.push(`Manca ${arrow(k)}: ${why(k)}.`));
      extra.forEach(k => { const [i, j] = k.split('>');
        msgs.push(`${arrow(k)} non c’è: nessuna azione di T${i} viene prima di un’azione di T${j} in conflitto con essa (stesso elemento, almeno una write).`); });
      const cyc = Schedule.cycle(T, keys), order = Schedule.topo(T, keys);
      if (!verdict) msgs.push('Scegli anche il verdetto.');
      else if ((verdict.value === 'yes') !== !cyc) msgs.push(cyc
        ? `Verdetto sbagliato: c’è il ciclo ${cyc.map(t => 'T' + t).join(' → ')}, quindi non è conflict-serializable.`
        : 'Verdetto sbagliato: il grafo è aciclico, quindi è conflict-serializable.');
      const ok = !msgs.length;
      const result = cyc ? `Ciclo ${cyc.map(t => 'T' + t).join(' → ')}: <strong>non</strong> conflict-serializable.`
        : `Aciclico: conflict-serializable, equivalente allo schedule seriale <strong>${order.map(t => 'T' + t).join(' ')}</strong>${T.length > 2 ? ' (un ordine topologico; possono essercene altri)' : ''}.`;
      out.dataset.state = ok ? 'correct' : 'incorrect';
      out.innerHTML = (ok ? '<p>Corretto.</p>' : `<ul>${msgs.map(m => `<li>${m}</li>`).join('')}</ul>`) +
        (ok ? `<div class="graph">${precedenceSvg(T, keys, cyc)}</div><p>${result}</p>
<p class="meta">Archi e coppie che li giustificano: ${[...keys].map(k => `${arrow(k)} (${why(k)})`).join(' · ')}</p>` : '');
    };
    S = box.dataset.precedence ? Schedule.parse(box.dataset.precedence) : Schedule.random();
    render();
  });
}
