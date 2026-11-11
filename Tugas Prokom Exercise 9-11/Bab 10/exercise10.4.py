from pathlib import Path

name = input("Masukkan nama Anda: ")

path = Path(__file__).parent / 'guest.txt'
path.write_text(name)

print(f"Nama {name} sudah disimpan ke guest.txt")