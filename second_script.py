import csv
import os
import sqlite3
from consts import (CSV_FILENAME, DB_FILENAME, CREATE_TABLE, DELETE_DATA, INSERT_DATA, SELECT_ALL_DATA)

### Funzioni ###

# Verifica la correttezza di un file CSV, assicurandosi che esista e che i dati al suo interno corrispondano alla traccia data
def is_csv_valid(csv_file):
    # Se il file non esiste, esce preventivamente
    if not os.path.exists(csv_file):
        print(f"Il file '{csv_file}' non esiste. Assicurati di aver eseguito first_script.py prima di questo script.")
        return False

    # Apertura del file CSV
    with open(csv_file, newline='') as csvfile:
        reader = csv.reader(csvfile)

        # Se il file esiste ma è vuoto, esce preventivamente
        if not any(reader):
            print(f"Il file '{csv_file}' esiste ma è vuoto.")
            return False

        # Se l'header non è valido, esce preventivamente
        header = next(reader, None)
        if header is None or len(header) != 4:
            print(f"Il file '{csv_file}' non ha un header valido.")
            return False

        # Verifica tutte le righe
        for row in reader:
            if not is_csv_row_valid(row):
                # Riga non valida, esce preventivamente
                print(f"Il file '{csv_file}' esiste ma i dati al suo interno non sono corretti. Esegui nuovamente first_script.py per generare nuovi dati.")
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

# Legge i dati da un file CSV e li restituisce come una lista di tuple
def read_csv_data(csv_filename):
    data = []

    # Apertura del file CSV
    with open(csv_filename, newline='') as csvfile:
        reader = csv.reader(csvfile)

        # Rimuovi l'header
        next(reader)  

        # Restituisci i dati come una lista di tuple
        for row in reader:
            data.append(tuple(row))
        
    return data

# Legge i dati da un database SQLite e li restituisce come una lista di tuple
def read_db_data(db_filename):
    data = []

    try:
        with sqlite3.connect(db_filename) as conn:
            cursor = conn.cursor()

            # Esegue la query per selezionare tutti i dati
            cursor.execute(SELECT_ALL_DATA)

            # Restituisci i dati come una lista di tuple
            data = cursor.fetchall()  

    except sqlite3.Error as e:
        print(f"Errore SQLite: {e}")

    return data

# Confronta i dati del file CSV e del database SQLite
def compare_data(csv_filename, db_filename):
    # Recupero dei dati dai file CSV e dal database SQLite
    csv_data = read_csv_data(csv_filename)
    db_data = read_db_data(db_filename)
    
    # Confronto tra i dati ordinati in modo da evitare problemi di ordine
    return sorted(csv_data) == sorted(db_data)

def main():
    if not is_csv_valid(CSV_FILENAME):
        exit()
    else:
        # Check di sicurezza per evitare eccezioni
        try:
            with sqlite3.connect(DB_FILENAME) as conn:
                cursor = conn.cursor()

                # Se non esiste, crea una nuova tabella 'users'
                cursor.execute(CREATE_TABLE)

                # Elimina tutte le (eventuali) righe presenti nella tabella 'users'
                cursor.execute(DELETE_DATA)
                
                # Apertura del file CSV e inserimento dei dati nella tabella 'users'
                with open(CSV_FILENAME, newline='') as csvfile:
                    reader = csv.reader(csvfile)
                    next(reader)

                    for row in reader:
                        cursor.execute(INSERT_DATA, (row[0], row[1], row[2], row[3]))

                # Commit cambiamenti (la connessione viene chiusa dal blocco 'with')
                conn.commit()
            
            print(f"I dati dal file '{CSV_FILENAME}' sono stati inseriti nella tabella 'people' del database '{DB_FILENAME}'.")

            if compare_data(CSV_FILENAME, DB_FILENAME):
                print(f"I dati nel file '{CSV_FILENAME}' e nel database '{DB_FILENAME}' sono identici.")
            else:
                print(f"I dati nel file '{CSV_FILENAME}' e nel database '{DB_FILENAME}' NON sono identici.")

        except sqlite3.Error as e:
            print(f"Errore SQLite: {e}")
            exit()

### Main script ###

main();