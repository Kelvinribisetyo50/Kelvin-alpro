from pathlib import Path
import json

path = Path(__file__).parent / 'favorite_number.json'

if path.exists():
    number = json.loads(path.read_text())
    print(f"I know your favorite number! It's {number}.")
else:
    number = int(input("Berapa angka favoritmu? "))
    path.write_text(json.dumps(number))
    print("Angka favoritmu sudah disimpan.")