pets = [
    {
        "name": "Mimi",
        "kind": "kucing",
        "owner": "Kelvin",
        "age": 3,
        "foods": ["ikan", "ayam"],
    },
    {
        "name": "Bruno",
        "kind": "Hamster",
        "owner": "Naura",
        "age": 2,
        "foods": ["jagung", "tumbuhan"],
    },
    {
        "name": "Kiko",
        "kind": "burung",
        "owner": "Artha",
        "age": 1,
        "foods": ["biji-bijian"],
    },
    {
        "name": "Akmil",
        "kind": "kelinci",
        "owner": "Bagas",
        "age": 2,
        "foods": ["wortel", "kangkung", "rumput"],
    },
]

print("=== DAFTAR HEWAN PELIHARAAN ===\n")

for pet in pets:
    print(f"{pet['name']} ({pet['kind'].title()})")
    print(f"\tPemilik : {pet['owner']}")
    print(f"\tUsia    : {pet['age']} tahun")
    print(f"\tMakanan : {', '.join(pet['foods'])}\n")

total_age = sum(pet["age"] for pet in pets)
average_age = total_age / len(pets)
oldest = max(pets, key=lambda pet: pet["age"])

print("=== RINGKASAN ===")
print(f"Jumlah hewan  : {len(pets)}")
print(f"Rata-rata usia: {average_age:.1f} tahun")
print(f"Paling tua    : {oldest['name']} ({oldest['age']} tahun)")