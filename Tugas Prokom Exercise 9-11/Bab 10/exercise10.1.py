from pathlib import Path

path = Path(__file__).parent / 'learning_python.txt'

contents = path.read_text()
print("Membaca seluruh file:")
print(contents)

lines = contents.splitlines()
print("\nMembaca per baris dari list:")
for line in lines:
    print(line)