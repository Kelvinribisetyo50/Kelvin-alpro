person_1 = {
    "first_name": "Kelvin",
    "last_name": "Ribisetyo",
    "age": 19,
    "city": "Pemalang",
}

person_2 = {
    "first_name": "Artha",
    "last_name": "Maulida",
    "age": 18,
    "city": "Pemalang",
}

person_3 = {
    "first_name": "Naura",
    "last_name": "Ramadhani",
    "age": 19,
    "city": "Pemalang",
}

people = [person_1, person_2, person_3]

for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    print(f"Nama: {full_name}")
    print(f"Usia: {person['age']}")
    print(f"Kota: {person['city']}\n")