# Project Work Università Telematica "UniPegaso"

## Introduzione

Repository contenente gli elaborati in merito alla Tesi del Corso di Laurea L-31 "Informatica per le Aziende Digitali".
La traccia scelta è la 2.1: "Ruolo della privacy e sull'importanza del GDPR".

L'elaborato richiede lo sviluppo di due script Python il cui obiettivo fosse:
- Il primo script deve generare dati casuali per 10 persone (nome, cognome, numero di telefono, indirizzo), salvando successivamente tali dati in un file di tipo .csv
- Il secondo script deve recuperare i dati dal file .csv precedentemente creato, creare una tabella SQLite ed inserire i dati così recuperati al suo interno, assicurandosi che i dati tra il file .csv e la tabella SQLite corrispondano correttamente

## Requisiti

Come primo passo, è necessario scaricare questo progetto sul proprio PC in modo da poter eseguire i vari script contenuti al suo interno. Per far ciò, aprendo il terminale, spostarsi in una cartella a proprio piacimento ed eseguire il seguente comando:
> git clone https://github.com/Juuzen/unipegaso-thesis.git

In alternativa, è possibile scaricare l'intero progetto in formato .zip, ed estrarlo una volta completato il download. Per far ciò, è necessario cliccare sul tasto "Code" in alto, e nel menu che si apre selezionare "Download zip".

Per il corretto funzionamento degli script, è necessario che sul PC sia installato Python (può essere scaricato per tutti i comuni OS dal sito ufficiale: https://www.python.org/downloads/).

Dopo aver installato con successo Python (qualora non fosse presente sul proprio PC), è necessario installare Faker (https://github.com/joke2k/faker).

Faker è un package Python di generazione casuale di dati, semplice da utilizzare e da configurare. E' stata scelta per questo progetto perché permette una localizzazione dei dati e la selezione tra un ampio range di dati disponibili, coprendo ampiamente le richieste da soddisfare.

Per installarlo, basta aprire il terminale ed eseguire il seguente comando:
> pip install faker

Infine è necessario che gli script siano contenuti tutti nella stessa cartella, in modo che gli output possano essere recuperati correttamente dai vari script.
Clonare o scaricare questo progetto è condizione sufficiente per poter eseguire gli script senza problemi.

## Esecuzione

Per poter eseguire correttamente gli scripts, aprire il terminale del proprio OS di riferimento, e spostarsi all'interno della cartella clonata di questo progetto, contenente tutti i file necessari.

Dopodiché, eseguire il comando:
> python ./<NOME_SCRIPT>.py

All'interno della cartella è possibile trovare:
- `README.md` (ciò che si sta visualizzando in questo momento)
- `consts.py`
- `first_script.py`
- `second_script.py`

Il file `consts.py` contiene semplicemente dati e variabili condivise dagli altri file, anche eseguendo tale script non si otterrà nessun risultato, per cui verrà ignorato da questo momento in avanti.

Il primo file da eseguire è `first_script.py`. Questo script creerà un file denominato `people_data.csv` contenente i dati degli utenti.

Il secondo file da eseguire è `second_script.py`. Questo script cercherà nella stessa cartella un file `people_data.csv` e, se lo troverà, proverà ad inserire tali dati in un database SQLite. In questo secondo script vengono prese diverse misure per verificare la validità dei dati recuperati dal file `people_data.csv` (come, ad esempio, fermare l'esecuzione del codice se il file non esiste, oppure è vuoto, o se i dati non sono formattati correttamente). 

Tali misure sono prese in misura cautelativa, per dimostrare l'importanza di assicurarsi che i dati in ingresso siano sempre puliti, poiché dati errati possono portare alla corruzione del database e a problemi successivi ben più gravi. Le misure di sicurezza aggiunte, essendo questo comunque un aspetto secondario a ciò che richiede la traccia, non sono esaustivi, ma coprono solo le casistiche più comuni.

Se i due script `first_script.py` e `second_script.py` sono stati eseguiti in successione, nella stessa cartella dovrebbero ora trovarsi due ulteriori file `people_data.csv` e `people_data.db`. 

I dati all'interno del database possono essere letti con un qualsiasi programma di gestione DB (come, ad esempio DBeaver).

Lo script `second_script.py` una volta creata la tabella 'people' (se non presente) ed aver inserito i dati recuperati dal file `people_data.csv` (dopo aver eliminato i precedenti), effettua un check di validazione tra i dati contenuti in `people_data.csv` e quelli in `people_data.db`. Il confronto tra i dati viene effettuato dopo aver ordinato le relative righe di entrambi i file in modo che il confronto sia position-insensitive. Ottenuto tale risultato, esso viene mostrato all'interno del terminale.