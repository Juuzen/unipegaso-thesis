from faker import Faker
from consts import CSV_FILENAME
import csv

# Inizializzazione dell'oggetto Faker
faker = Faker('it_IT')

### Funzioni ###

# Genera dati casuali di una persona
def generate_person_fake_data():
    name = faker.first_name()
    surname = faker.last_name()
    phone_number = faker.phone_number()
    address = faker.address().replace("\n", ", ")

    # Restituzione dei dati generati
    return [name, surname, phone_number, address]

# Genera dati casuali di persone multiple, con un numero di righe ricevuto come argomento
def generate_people_fake_data(num_rows=10):
    people_data = []

    # Check per evitare dati incorretti
    if num_rows > 0:
        for _ in range(num_rows):
            people_data.append(generate_person_fake_data())
    
    # Restituzione dei dati generati
    return people_data

# Funzione per salvare dati casuali di persone in un file CSV
def save_fake_data_to_csv(filename, people_data):
    header = ["Nome", "Cognome", "Numero di telefono", "Indirizzo"]

    # Apertura del file CSV
    with open(filename, mode='w', newline='') as file:
        # Creazione dell'oggetto writer
        writer = csv.writer(file)

        # Scrittura dell'header nel file CSV
        writer.writerow(header)
        
        # Scrittura dei dati nel file CSV
        writer.writerows(people_data)

def main():
    # Generazione di 10 righe di dati casuali di persone
    people_data = generate_people_fake_data(10)

    # Salvataggio dei dati in un file CSV
    save_fake_data_to_csv(CSV_FILENAME, people_data)

    # Messaggio di conferma
    print(f"I dati sono stati scritti nel file {CSV_FILENAME}.")
    
### Main script ###

main();