from pathlib import Path
import json

number = int(input("Berapa angka favoritmu? "))

path = Path(__file__).parent / 'favorite_number.json'
contents = json.dumps(number)
path.write_text(contents)

print("Angka favoritmu sudah disimpan.")