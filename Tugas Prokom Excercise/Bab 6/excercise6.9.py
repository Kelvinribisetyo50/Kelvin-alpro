favorite_places = {
    "Kelvin": ["Pantai Parangtritis", "Wisata Guci"],
    "Enayy": ["Gunung Bromo"],
    "Elfa": ["Kawah Ijen", "Alun-alun Solo", "Dieng"],
}

for name, places in favorite_places.items():
    print(f"Tempat favorit {name}:")
    for place in places:
        print(f"\t- {place}")
    print()