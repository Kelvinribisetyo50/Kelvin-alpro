pet_1 = {"kind": "kucing", "owner": "Kelvin"}
pet_2 = {"kind": "hamster", "owner": "Naura"}
pet_3 = {"kind": "burung", "owner": "Artha"}
pet_4 = {"kind": "kelinci", "owner": "Bagas"}

pets = [pet_1, pet_2, pet_3, pet_4]

for pet in pets:
    print("Informasi hewan peliharaan:")
    for key, value in pet.items():
        print(f"\t{key.title()}: {value.title()}")
    print()