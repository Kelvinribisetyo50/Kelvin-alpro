cities = {
    "jakarta": {
        "country": "indonesia",
        "population": 10_500_000,
        "fact": "Ibu kota Indonesia yang dulunya bernama Batavia.",
    },
    "tokyo": {
        "country": "jepang",
        "population": 14_000_000,
        "fact": "Salah satu kota dengan wilayah metropolitan terbesar di dunia.",
    },
    "paris": {
        "country": "prancis",
        "population": 2_100_000,
        "fact": "Menara Eiffel selesai dibangun pada tahun 1889.",
    },
}

for city, info in cities.items():
    print(f"Kota: {city.title()}")
    print(f"\tNegara: {info['country'].title()}")
    print(f"\tPopulasi: {info['population']:,}")
    print(f"\tFakta: {info['fact']}\n")