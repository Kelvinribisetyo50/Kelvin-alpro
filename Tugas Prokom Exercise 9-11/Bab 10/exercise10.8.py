from pathlib import Path

filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    path = Path(__file__).parent / filename
    try:
        contents = path.read_text()
    except FileNotFoundError:
        print(f"Maaf, file {filename} tidak ditemukan.\n")
    else:
        print(f"Isi file {filename}:")
        print(contents)
        print()