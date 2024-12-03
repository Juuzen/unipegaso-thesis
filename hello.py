# hello.py
from faker import Faker

# Inizializzazione dell'oggetto Faker
faker = Faker('it_IT')

def genera_dati():
    # Generazione di dati casuali
    nome = faker.first_name()
    cognome = faker.last_name()
    telefono = faker.phone_number()
    indirizzo = faker.address().replace("\n", ", ")

    # Restituzione dei dati generati
    return nome, cognome, telefono, indirizzo

# Stampa dei dati generati
print(genera_dati())