'use strict';
// Small exercises with a deliberately restricted Turtle input grammar.
// No network, tracking, persistence, external libraries, or full Turtle parser.
const RDF_TYPE = 'rdf:type';
const expectedTriples = [
  [':John', ':isFriendOf', ':Mary'],
  [':Mary', ':name', '"Mary"'],
  [':Mary', RDF_TYPE, ':Person']
];

function normalizeTerm(term) {
  if (term === 'a') return RDF_TYPE;
  if (/^'[^'\n]*'$/.test(term)) return JSON.stringify(term.slice(1, -1));
  if (/^"[^"\\\n]*"$/.test(term)) return JSON.stringify(term.slice(1, -1));
  return term;
}

function checkTriples(source) {
  const lines = source.split(/\r?\n/).map(x => x.trim()).filter(Boolean);
  if (!lines.length) return {ok:false, message:'Scrivi le tre triple prima di controllare.'};
  const term = '(?:rdf:type|:[A-Za-z][A-Za-z0-9_]*|a|"[^"\\\\\\n]*"|\'[^\'\\\\\\n]*\')';
  const pattern = new RegExp('^(' + term + ')\\s+(' + term + ')\\s+(' + term + ')\\s*\\.$');
  const triples = [];
  for (let i = 0; i < lines.length; i++) {
    const match = lines[i].match(pattern);
    if (!match) return {ok:false, message:`Riga ${i+1}: usa tre termini separati da spazi e un punto finale. Una tripla per riga; i prefissi sono già dichiarati. Questo correttore guidato non analizza tutta la sintassi Turtle.`};
    const triple = match.slice(1).map(normalizeTerm);
    if (triple[0].startsWith('"')) return {ok:false,message:`Riga ${i+1}: il soggetto non può essere un literal. Usa una IRI come :Mary.`};
    if (triple[1].startsWith('"')) return {ok:false,message:`Riga ${i+1}: il predicato deve essere una IRI, non una stringa tra virgolette.`};
    if (match[1] === 'a' || match[3] === 'a') return {ok:false,message:`Riga ${i+1}: l'abbreviazione a si usa qui solo come predicato; per la classe usa :Person.`};
    triples.push(triple);
  }
  const key = x => JSON.stringify(x);
  const actual = new Set(triples.map(key));
  const target = new Set(expectedTriples.map(key));
  const extra = triples.find(x => !target.has(key(x)));
  if (extra) {
    if (extra[1] === ':name' && extra[2] === ':Mary') return {ok:false,message:'Nella tripla sul nome, :Mary identifica la persona; "Mary" è il valore testuale richiesto come oggetto.'};
    if (extra[1] === ':isFriendOf' && extra[2] === '"Mary"') return {ok:false,message:'John è amico della persona :Mary, non della stringa "Mary". Togli le virgolette dall’oggetto di questa relazione.'};
    if (extra[1] === RDF_TYPE && extra[2] === '"Person"') return {ok:false,message:'La classe è identificata da :Person; "Person" sarebbe una stringa.'};
    return {ok:false,message:`Rileggi questa tripla: ${extra.join(' ')} . Non esprime uno dei tre fatti richiesti con i termini assegnati. Controlla verso della relazione e scelta del predicato.`};
  }
  if (actual.size !== target.size) return {ok:false,message:`Hai rappresentato ${actual.size} dei 3 fatti richiesti. Una tripla ripetuta non aggiunge un fatto nuovo.`};
  return {ok:true,message:'Corretto: hai espresso tutti e tre i fatti. L’ordine delle triple non conta; a e rdf:type sono equivalenti. Ora spiega a voce perché :Mary e "Mary" compaiono in ruoli diversi.'};
}

if (typeof module !== 'undefined') module.exports = {checkTriples};
if (typeof document !== 'undefined') {
  const solved = new Set();
  const report = (form, ok, message) => {
    const output = form.querySelector('[data-feedback]');
    output.textContent = message;
    output.dataset.state = ok ? 'correct' : 'incorrect';
    if (ok) solved.add(form.id); else solved.delete(form.id);
    const progress = document.querySelector('[data-progress]');
    if (progress) progress.textContent = `${solved.size} / 4 esercizi completati correttamente in questa apertura.`;
  };
  document.querySelectorAll('form[data-quiz]').forEach(form => {
    form.addEventListener('submit', event => {
      event.preventDefault();
      const choice = form.querySelector('input:checked');
      if (!choice) return report(form, false, 'Scegli una risposta e poi controlla.');
      report(form, choice.dataset.correct === 'true', choice.dataset.feedback);
    });
  });
  const writing = document.querySelector('form[data-writing]');
  if (writing) writing.addEventListener('submit', event => {
    event.preventDefault();
    const result = checkTriples(writing.querySelector('textarea').value);
    report(writing, result.ok, result.message);
  });
  document.querySelectorAll('form[data-quiz],form[data-writing]').forEach(form => {
    form.addEventListener('input', () => {
      solved.delete(form.id);
      form.querySelector('[data-feedback]').textContent = '';
      const progress = document.querySelector('[data-progress]');
      if (progress) progress.textContent = `${solved.size} / 4 esercizi completati correttamente in questa apertura.`;
    });
  });
}
