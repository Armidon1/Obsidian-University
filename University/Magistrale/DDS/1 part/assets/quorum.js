'use strict';
// Shared widgets for the quorum lessons. No network or persistence, no scores.
//
// Quorum simulator: the reader picks which servers answer.
//   <div class="qsim" data-n="5" data-written="1,2,3" data-q="3"></div>
// Numeric exercise:
//   <form data-num="4" data-right="..." data-wrong="...">...<div class="feedback" data-feedback></div></form>

function readOutcome(picked, written) {
  const fresh = picked.filter(s => written.includes(s));
  return {fresh, stale: picked.filter(s => !written.includes(s)), seesNew: fresh.length > 0};
}

if (typeof module !== 'undefined') module.exports = {readOutcome};

if (typeof document !== 'undefined') {
  const names = list => list.map(s => 'S' + s).join(', ');

  document.querySelectorAll('.qsim').forEach(sim => {
    const n = Number(sim.dataset.n), q = Number(sim.dataset.q);
    const written = sim.dataset.written.split(',').map(Number);
    const row = document.createElement('div');
    row.className = 'servers';
    const out = document.createElement('div');
    out.className = 'feedback';
    const picked = new Set();

    const update = () => {
      const list = [...picked].sort((a, b) => a - b);
      if (list.length < q) {
        out.dataset.state = '';
        out.textContent = `Risposte ricevute: ${list.length} su ${q}.`;
        return;
      }
      const r = readOutcome(list, written);
      out.dataset.state = r.seesNew ? 'correct' : 'incorrect';
      out.textContent = r.seesNew
        ? `La read ha sentito ${names(list)}. ${names(r.fresh)} ha il valore nuovo: la read lo trova. Deseleziona un server e prova a evitarlo.`
        : `La read ha sentito ${names(list)}: nessuno ha il valore nuovo. La read restituisce il valore vecchio anche se la write è già finita. Questo è l'errore da evitare.`;
    };

    for (let s = 1; s <= n; s++) {
      const b = document.createElement('button');
      b.type = 'button';
      const isNew = written.includes(s);
      b.className = 'srv ' + (isNew ? 'new' : 'old');
      b.setAttribute('aria-pressed', 'false');
      b.innerHTML = `<strong>S${s}</strong><small>${isNew ? 'nuovo' : 'vecchio'}</small>`;
      b.addEventListener('click', () => {
        if (picked.has(s)) picked.delete(s);
        else if (picked.size < q) picked.add(s);
        else return;
        b.setAttribute('aria-pressed', String(picked.has(s)));
        update();
      });
      row.append(b);
    }
    sim.append(row, out);
    update();
  });

  document.querySelectorAll('form[data-num]').forEach(form => {
    const out = form.querySelector('[data-feedback]');
    form.addEventListener('submit', e => {
      e.preventDefault();
      const value = form.querySelector('input').value.trim();
      if (value === '') { out.dataset.state = 'incorrect'; out.textContent = 'Scrivi un numero e poi controlla.'; return; }
      const ok = Number(value) === Number(form.dataset.num);
      out.dataset.state = ok ? 'correct' : 'incorrect';
      out.textContent = ok ? form.dataset.right : form.dataset.wrong;
    });
    form.addEventListener('input', () => { out.textContent = ''; });
  });
}
