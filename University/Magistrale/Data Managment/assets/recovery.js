'use strict';
// Strict and rigorous schedules (note 05, § 5.5), with commits inserted where they are missing.
// No network, tracking or persistence.

const Recovery = (() => {
  // Actions r/w with an element, and commits c (abort is not used in these drills).
  function parse(src) {
    const out = [];
    for (const m of src.matchAll(/([rwc])\s*(\d+)(?:\s*\(\s*(\w+)\s*\))?/gi))
      out.push({op: m[1].toLowerCase(), tx: +m[2], el: m[3] || null});
    return out;
  }
  const fmt = a => a.op === 'c' ? `c${a.tx}` : `${a.op}${a.tx}(${a.el})`;

  // A missing commit goes right after the last action of its transaction: every condition below
  // has the form "ci comes before some action", so committing as early as possible is optimal.
  function complete(S) {
    const out = S.map(a => ({...a}));
    const txs = [...new Set(S.map(a => a.tx))];
    for (const t of txs) {
      if (out.some(a => a.op === 'c' && a.tx === t)) continue;
      let last = -1;
      out.forEach((a, k) => { if (a.tx === t) last = k; });
      out.splice(last + 1, 0, {op: 'c', tx: t, el: null, added: true});
    }
    out.forEach((a, k) => { a.i = k; });
    return out;
  }
  const commitPos = (S, t) => S.find(a => a.op === 'c' && a.tx === t).i;

  // Strict: every read or write on x by Tj after a write on x by Ti (i ≠ j) needs ci before it.
  // Rigorous: the same for every conflicting pair, so a read followed by a write counts too.
  function check(S0, rigorous) {
    const S = complete(S0);
    for (const b of S) {
      if (b.op === 'c') continue;
      for (const a of S) {
        if (a.i >= b.i || a.op === 'c' || a.tx === b.tx || a.el !== b.el) continue;
        if (a.op !== 'w' && !(rigorous && b.op === 'w')) continue;
        if (commitPos(S, a.tx) > b.i) {
          const kind = a.op === 'w' ? (b.op === 'r' ? 'legge un valore scritto' : 'scrive sopra un valore scritto')
            : 'scrive un elemento letto';
          return {ok: false, S, reason: `${fmt(b)} ${kind} da T${a.tx} con ${fmt(a)}, ma c${a.tx} arriva dopo.`};
        }
      }
    }
    return {ok: true, S};
  }

  function random() {
    const els = ['x', 'y'], n = 2 + Math.floor(Math.random() * 2);
    const queues = [];
    for (let t = 1; t <= n; t++) {
      const k = 1 + Math.floor(Math.random() * 2), q = [];
      const pool = ['r', 'w'].flatMap(op => els.map(el => ({op, tx: t, el})));
      for (let j = 0; j < k; j++) q.push(pool.splice(Math.floor(Math.random() * pool.length), 1)[0]);
      if (!q.some(a => a.op === 'w')) q[q.length - 1].op = 'w';
      if (Math.random() < .75) q.push({op: 'c', tx: t, el: null});
      queues.push(q);
    }
    const S = [];
    while (queues.some(q => q.length)) {
      const live = queues.filter(q => q.length);
      const q = live[Math.floor(Math.random() * live.length)];
      S.push(q.shift());
    }
    return S;
  }
  // Rigorous implies strict, so only three verdict pairs exist; draw them equally often.
  function randomBalanced() {
    const want = Math.floor(Math.random() * 3);  // 0: no/no, 1: strict only, 2: both
    for (;;) {
      const S = random();
      const kind = check(S, true).ok ? 2 : check(S, false).ok ? 1 : 0;
      const conflicts = S.some((a, k) => a.op !== 'c' && S.slice(k + 1).some(b => b.op !== 'c' && b.tx !== a.tx && b.el === a.el));
      if (kind === want && conflicts) return S;
    }
  }
  return {parse, fmt, complete, check, random, randomBalanced};
})();

if (typeof module !== 'undefined') module.exports = {Recovery};

if (typeof document !== 'undefined') {
  const chip = (a, k) => a.op === 'c'
    ? `<span class="act t${a.tx}"${a.added ? ' style="border-style:dashed"' : ''}><sub>${k + 1}</sub><b>c${a.tx}</b></span>`
    : `<span class="act t${a.tx}"><sub>${k + 1}</sub>${a.op}<b>${a.tx}</b>(${a.el})</span>`;
  const row = S => `<div class="sched">${S.map(chip).join('')}</div>`;
  document.querySelectorAll('.rec-drill').forEach((box, n) => {
    let S;
    const yn = (name, q) => `<p class="meta">${q}</p><fieldset class="options inline">
<label><input type="radio" name="${name}" value="yes"> Sì</label><label><input type="radio" name="${name}" value="no"> No</label></fieldset>`;
    const render = () => {
      const missing = Recovery.complete(S).some(a => a.added);
      box.innerHTML = row(S) + (missing ? '<p class="meta">Alcune transazioni non hanno il commit: inseriscilo tu dove conviene.</p>' : '') +
        yn(`st${n}`, '1 · È strict?') + yn(`rg${n}`, '2 · È rigorous?') +
        `<div class="actions"><button type="button" data-check>Controlla</button>${box.hasAttribute('data-random') ?
        '<button type="button" class="secondary" data-new>Nuovo schedule</button>' : ''}</div><div class="feedback" role="status" aria-live="polite"></div>`;
      box.querySelector('[data-check]').onclick = check;
      const again = box.querySelector('[data-new]');
      if (again) again.onclick = () => { S = Recovery.randomBalanced(); render(); };
    };
    const check = () => {
      const out = box.querySelector('.feedback');
      const parts = [[`st${n}`, false, 'Strict'], [`rg${n}`, true, 'Rigorous']];
      if (parts.some(([name]) => !box.querySelector(`input[name=${name}]:checked`))) {
        out.dataset.state = 'incorrect'; out.textContent = 'Rispondi a entrambe le domande.'; return;
      }
      let allOk = true;
      const html = parts.map(([name, rig, label]) => {
        const r = Recovery.check(S, rig), said = box.querySelector(`input[name=${name}]:checked`).value === 'yes';
        const good = said === r.ok; allOk = allOk && good;
        return `<p><strong>${label}: ${good ? 'corretto' : 'sbagliato'}, ${r.ok ? 'sì' : 'no'}.</strong> ${r.ok ? '' : r.reason}</p>`;
      }).join('');
      const full = Recovery.complete(S);
      out.dataset.state = allOk ? 'correct' : 'incorrect';
      out.innerHTML = html + (full.some(a => a.added)
        ? `<p class="meta">Con i commit mancanti messi subito dopo l’ultima azione (tratteggiati):</p>${row(full)}` : '');
    };
    S = box.hasAttribute('data-random') ? Recovery.randomBalanced() : Recovery.parse(box.dataset.schedule);
    render();
  });
}
