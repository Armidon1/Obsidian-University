# Distinzione tra identità della risorsa e nome testuale

Simone ha scritto correttamente le tre triple su John e Mary, compresa l'appartenenza a `:Person` tramite `rdf:type`, e ha trasferito la distinzione IRI/literal al nuovo esempio `:Ann :knows :John .` e `:Ann :name "Anna" .`. Ha spiegato che Anna è il valore stringa del nome della risorsa Ann, usando l'analogia con un oggetto e un attributo.

La spiegazione assume però che Ann sia un'istanza di Person: le due triple fornite non dichiarano questo tipo. Chiarire che occorre un'asserzione `rdf:type` o una deduzione fondata su dichiarazioni note; un prefisso o il nome di una proprietà non bastano. Questa precisazione è stata proposta, ma non ancora verificata con una sua risposta. Prossimo passo: verificare il tipo senza affidarsi all'analogia con classi a schema obbligatorio, poi passare ai blank node.
