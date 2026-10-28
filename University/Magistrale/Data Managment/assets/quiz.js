'use strict';
// Shared practice widgets: radio quizzes and a checker for one-pattern SPARQL class queries.
// No network, tracking or persistence: answers stay in the open page.

function checkClassQuery(source, cls) {
  const q = source.replace(/^\s*PREFIX[^\n]*$/gim, '').replace(/\s+/g, ' ').trim();
  if (!q) return {ok:false, message:'Scrivi la query prima di controllare.'};
  if (!/^SELECT\b/i.test(q)) return {ok:false, message:'Una query di interrogazione inizia con SELECT, seguito dalle variabili da restituire.'};
  if (!/\bWHERE\s*\{/i.test(q) || !q.endsWith('}')) return {ok:false, message:'Manca il blocco WHERE { … }: le triple da cercare vanno tra graffe.'};
  const m = q.match(/^SELECT\s+(?:DISTINCT\s+)?(\*|\?\w+)\s+WHERE\s*\{\s*(\S+)\s+(\S+)\s+(\S+?)\s*\.?\s*\}$/i);
  if (!m) return {ok:false, message:'Basta un solo triple pattern: SELECT ?v WHERE { soggetto predicato oggetto . }. Controlla spazi e graffe.'};
  const [, out, s, p, o] = m;
  if (!s.startsWith('?')) return {ok:false, message:`Il soggetto ${s} è una costante: vuoi lasciarlo libero, quindi serve una variabile come ?x.`};
  if (out !== '*' && out !== s) return {ok:false, message:`Nel SELECT restituisci ${out}, ma nel pattern la variabile è ${s}. Devono coincidere.`};
  if (p !== 'rdf:type' && p !== 'a') return {ok:false, message:`Il predicato ${p} non esprime l’appartenenza a una classe: usa rdf:type (oppure a).`};
  if (/^["']/.test(o)) return {ok:false, message:'La classe è una IRI, non una stringa: niente virgolette.'};
  if (o !== cls) return {ok:false, message:`Classe sbagliata: hai scritto ${o}, la classe richiesta è ${cls} (il prefisso vuoto e le maiuscole contano).`};
  return {ok:true, message:'Corretto. È esattamente la forma attesa all’esame: un solo triple pattern con rdf:type. Il lavoro vero è al punto successivo, dove decidi su quali triple valutarla.'};
}

if (typeof module !== 'undefined') module.exports = {checkClassQuery};
if (typeof document !== 'undefined') {
  const forms = document.querySelectorAll('form[data-quiz],form[data-sparql]');
  const solved = new Set();
  const progress = () => {
    const el = document.querySelector('[data-progress]');
    if (el) el.textContent = `${solved.size} / ${forms.length} esercizi completati correttamente in questa apertura.`;
  };
  const report = (form, ok, message) => {
    const output = form.querySelector('div[data-feedback]');
    output.textContent = message;
    output.dataset.state = ok ? 'correct' : 'incorrect';
    if (ok) solved.add(form.id); else solved.delete(form.id);
    progress();
  };
  forms.forEach(form => {
    form.addEventListener('submit', event => {
      event.preventDefault();
      if (form.hasAttribute('data-sparql')) {
        const r = checkClassQuery(form.querySelector('textarea').value, form.dataset.sparql);
        return report(form, r.ok, r.message);
      }
      const choice = form.querySelector('input:checked');
      if (!choice) return report(form, false, 'Scegli una risposta e poi controlla.');
      report(form, choice.dataset.correct === 'true', choice.dataset.feedback);
    });
    form.addEventListener('input', () => {
      solved.delete(form.id);
      form.querySelector('div[data-feedback]').textContent = '';
      progress();
    });
  });
  progress();
}
