# PL_Backward_Chaining

• Cartelle: – data : cartella contenente i datasets generati, suddivisi per variabile utilizzata nelle simu￾lazioni (Branching, Depth...) e i valori dei parametri aggiuntivi.
– results: cartella contenente le tabelle dei risultati dei test, suddivisi per parametro utiliz￾zato nelle simulazioni.
– plots: cartella contenente i grafici dei risultati dei test, suddivisi per parametro utilizzato
nelle simulazioni. Contiene anche le cartelle dove sono salvati i plot dei grafi creati dai test
giocattolo.

• File classi .py : – Literal.py : classe per la rappresentazione dei letterali.
– HornClause.py : classe per la rappresentazione delle clausole di Horn.
– KnowledgeBase.py : classe per la rappresentazione della KB.
– Node.py : classe per la rappresentazione dei nodi nei grafi AND OR.
– Connector.py : classe per la rappresentazione dei connettori nei grafi AND OR.
– ANDORGraph.py : classe per la rappresentazione dei grafi AND OR.
– InferenceMethods.py : contiene gli algoritmi di Forward Chaining e Backward Chaining.
– Utilities.py : contiene quality-of-life methods utili alle classi.

• File eseguibili .py
– KnowledgeBaseCreation.py : contiene il codice eseguibile per generare i datasets utiliz￾zati nei test di performance.
– PerformanceTest.py : contiene il codice eseguibile per testare gli algoritmi sui datasets
generati in precedenza.
– ToyTests.py : contiene il codice eseguibile per testare gli algoritmi sugli esempi Wumpus
World e West-Criminal.
– UserTest.py : contiene il codice eseguibile per testare gli algoritmi su una Knowledge Base
fornita dall’utente tramite un’interfaccia.
– main.py : contiene un test arbitrario da eseguire per testare velocemente gli algoritmi.

Per realizzare le classi Python che vanno a comporre gli algoritmi di Theorem Proving, le clausole di
Horn e la rispettiva Horn Knowledge Base, non sono stati utilizzati né moduli esterni né frammenti
di codice di progetti esterni.
Per realizzare i grafici e le tabelle sono stati utilizzati i moduli:
• MatPlotLib.pyplot
• NetworkX
• Plotly
• numpy
Per cronometrare gli algoritmi `e stato utilizzato il modulo:
• Timeit
Per salvare i dataset in forma seriale `e stato utilizzato il modulo:
• Pickle
