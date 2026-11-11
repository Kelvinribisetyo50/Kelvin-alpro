from pathlib import Path
import json

path = Path(__file__).parent / 'favorite_number.json'

try:
    contents = path.read_text()
except FileNotFoundError:
    print("File favorite_number.json belum ada. Jalankan program penyimpan dulu.")
else:
    number = json.loads(contents)
    print(f"I know your favorite number! It's {number}.")