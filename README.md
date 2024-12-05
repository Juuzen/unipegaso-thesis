# Project Work Università Telematica "UniPegaso"

## Introduzione

Repository contenente gli elaborati in merito alla Tesi del Corso di Laurea L-31 "Informatica per le Aziende Digitali".
La traccia scelta è la 2.1: "Ruolo della privacy e sull'importanza del GDPR".

L'elaborato richiede lo sviluppo di due script Python il cui obiettivo fosse:
- Il primo script deve generare dati casuali per 10 persone (nome, cognome, numero di telefono, indirizzo), salvando successivamente tali dati in un file di tipo .csv
- Il secondo script deve recuperare i dati dal file .csv precedentemente creato, creare una tabella SQLite ed inserire i dati così recuperati al suo interno, assicurandosi che i dati tra il file .csv e la tabella SQLite corrispondano correttamente

## Requisiti

Per poter verificare il corretto funzionamento degli script, è necessario assicurarsi che siano installate sul proprio sistema operativo le seguenti librerie:
- Faker

Inoltre è necessario che gli script siano contenuti tutti nella stessa cartella, in modo che gli output possano essere recuperati correttamente dai vari script.
Clonare questa repository è condizione sufficiente per poter eseguire gli script senza problemi.

## Esecuzione

Il primo file da eseguire è `first_script.py`. Questo script creerà un file denominato `people_data.csv` contenente i dati degli utenti.

Il secondo file da eseguire è `second_script.py`. Questo script cercherà nella stessa cartella un file `people_data.csv` e, se lo troverà, proverà ad inserire tali dati in un database SQLite. In questo secondo script vengono prese diverse misure per verificare la validità dei dati recuperati dal file `people_data.csv` (come, ad esempio, fermare l'esecuzione del codice se il file non esiste, oppure è vuoto, o se i dati non sono formattati correttamente). 

Tali misure sono prese in misura cautelativa, per dimostrare l'importanza di assicurarsi che i dati in ingresso siano sempre puliti, poiché dati errati possono portare alla corruzione del database e a problemi successivi ben più gravi. Le misure di sicurezza aggiunte, essendo questo comunque un aspetto secondario a ciò che richiede la traccia, non sono esaustivi, ma coprono solo le casistiche più comuni.

Se i due script `first_script.py` e `second_script.py` sono stati eseguiti in successione, nella stessa cartella dovrebbero ora trovarsi due ulteriori file `people_data.csv` e `people_data.db`. I dati all'interno del database possono essere letti con un qualsiasi programma di gestione DB (come, ad esempio DBeaver).