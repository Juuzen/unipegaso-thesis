from faker import Faker
import csv

# Inizializzazione dell'oggetto Faker
faker = Faker('it_IT')

# Funzione per generare dati casuali di una persona
def generate_person_fake_data():
    name = faker.first_name()
    surname = faker.last_name()
    phone_number = faker.phone_number()
    address = faker.address().replace("\n", ", ")

    # Restituzione dei dati generati
    return [name, surname, phone_number, address]

# Funzione per generare multipli dati casuali di persone, con un numero di righe ricevuto come argomento
def generate_people_fake_data(num_rows=10):
    people_data = []

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


# Generazione di 10 righe di dati casuali di persone
people_data = generate_people_fake_data(10)

# Salvataggio dei dati in un file CSV
save_fake_data_to_csv('people_data.csv', people_data)

# Messaggio di conferma
print("I dati sono stati scritti nel file 'people_data.csv'.")