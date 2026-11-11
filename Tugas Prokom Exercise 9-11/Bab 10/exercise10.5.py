from pathlib import Path

names = []

print("Ketik 'q' untuk berhenti.")
while True:
    name = input("Masukkan nama Anda: ")
    if name == 'q':
        break
    names.append(name)
    print(f"Halo, {name}! Nama Anda sudah dicatat.")

contents = "\n".join(names)

path = Path(__file__).parent / 'guest_book.txt'
path.write_text(contents)
