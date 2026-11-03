favorite_numbers = {
    "Kelvin": [7, 21],
    "Jeish": [14],
    "Willy": [3, 9, 33],
    "Eshan": [21, 5],
    "Kaka": [9, 18, 27],
}

for name, numbers in favorite_numbers.items():
    print(f"Angka favorit {name}:")
    for number in numbers:
        print(f"\t{number}")
    print()