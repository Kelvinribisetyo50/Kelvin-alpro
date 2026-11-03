favorite_languages = {
    "Kelvin": "python",
    "Willy": "c",
    "Eshan": "ruby",
    "Kaka": "python",
}
people = ["Kelvin", "Willy", "Eshan", "Kaka", "Siti", "Budi"]
for person in people:
    if person in favorite_languages.keys():
        print(f"Terima kasih, {person.title()}, sudah mengikuti polling!")
    else:
        print(f"{person.title()}, silakan ikut polling bahasa pemrograman favorit ya!")