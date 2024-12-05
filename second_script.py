import csv
import os
import sqlite3

# Verifica la correttezza di un file CSV, assicurandosi che esista e che i dati al suo interno corrispondano alla traccia data
def is_csv_valid(csv_file):
    # Se il file non esiste, esce preventivamente
    if not os.path.exists(csv_file):
        print(f"Il file '{csv_file}' non esiste. Assicurati di aver eseguito first_script.py prima di questo script.")
        return False

    with open(csv_file, newline='') as csvfile:
        reader = csv.reader(csvfile)

        # Se il file esiste ma è vuoto, esce preventivamente
        if not any(reader):
            print("Il file CSV esiste ma è vuoto.")
            return False

        # Se l'header non è valido, esce preventivamente
        header = next(reader, None)
        if header is None or len(header) != 4:
            print("Il file CSV non ha un header valido.")
            return False

        # Verifica tutte le righe
        for row in reader:
            if not is_csv_row_valid(row):
                # Riga non valida, esce preventivamente
                print(f"Il file '{csv_file}' esiste ma i dati al suo interno non sono corretti. Esegui nuovamente first_script.py per generare i dati corretti.")
                return False

    return True

# Verifica la correttezza di una singola riga di un file CSV, assicurandosi che i dati al suo interno corrispondano alla traccia data
def is_csv_row_valid(row):
    # Le righe devono avere esattamente 4 colonne
    if len(row) != 4: 
        return False
    
    # I campi non devono essere vuoti
    if any(not field.strip() for field in row):
        return False
    
    # I numeri di telefono devono contenere solo numeri, spazi, trattini e + (per indicare il prefisso internazionale)
    if not row[2].replace(" ", "").replace("-", "").replace("+", "").isdigit():
        return False
    
    # La riga è corretta
    return True

# Query per creare la tabella 'people' nel database SQLite
CREATE_TABLE = '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        surname TEXT,
        phone_number TEXT,
        address TEXT
    )
'''

INSERT_DATA = '''
    INSERT INTO users (name, surname, phone_number, address)
    VALUES (?, ?, ?, ?)
'''

### Main script ###

if not is_csv_valid('people_data.csv'):
    exit()

else:
    # Check di sicurezza per evitare eccezioni
    try:
        with sqlite3.connect('people_data.db') as conn:
            cursor = conn.cursor()

            # Create a new SQL table if it doesn't exist already
            cursor.execute(CREATE_TABLE)

            # Apertura del file CSV e inserimento dei dati nella tabella SQL
            with open('people_data.csv', newline='') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)

                for row in reader:
                    cursor.execute(INSERT_DATA, (row[0], row[1], row[2], row[3]))

            # Commit cambiamenti (la connessione viene chiusa dal blocco 'with')
            conn.commit()
        
        print("I dati dal file 'people_data.csv' sono stati inseriti nella tabella 'users' del database SQLite.")

    except sqlite3.Error as e:
        print(f"Errore SQLite: {e}")
        exit()