### CONSTANTS ###
# Query per creare la tabella 'people' nel database SQLite
CREATE_TABLE = '''
    CREATE TABLE IF NOT EXISTS people (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        surname TEXT,
        phone_number TEXT,
        address TEXT
    )
'''

# Query per inserire i dati nella tabella 'people'
INSERT_DATA = '''
    INSERT INTO people (name, surname, phone_number, address)
    VALUES (?, ?, ?, ?)
'''

# Query per eliminare tutti i dati dalla tabella 'people' nel database SQLite
DELETE_DATA = '''
    DELETE FROM people
'''

# Query per selezionare tutti i dati dalla tabella 'people' nel database SQLite
SELECT_ALL_DATA = '''
    SELECT name, surname, phone_number, address
    FROM people
'''



# Nomi dei file
CSV_FILENAME = 'people_data.csv'
DB_FILENAME = 'people_data.db'