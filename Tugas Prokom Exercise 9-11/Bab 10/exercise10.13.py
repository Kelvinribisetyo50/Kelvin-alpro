from pathlib import Path
import json

path = Path(__file__).parent / 'user_info.json'

username = input("Siapa namamu? ")
city = input("Kamu berasal dari kota mana? ")
hobby = input("Apa hobimu? ")

user_info = {
    'username': username,
    'city': city,
    'hobby': hobby,
}

path.write_text(json.dumps(user_info))
print("\nInformasimu sudah disimpan.")

loaded_info = json.loads(path.read_text())

print("\nIni yang aku ingat tentangmu:")
print(f"Nama  : {loaded_info['username']}")
print(f"Kota  : {loaded_info['city']}")
print(f"Hobi  : {loaded_info['hobby']}")