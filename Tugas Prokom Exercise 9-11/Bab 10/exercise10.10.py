
from pathlib import Path

path = Path(__file__).parent

filenames = [
    'alice.txt',
    'frankenstein.txt',
    'pride_and_prejudice.txt'
]

for filename in filenames:
    file_path = path / filename
    contents = file_path.read_text(encoding='utf-8')

    print(f"\nFile: {filename}")

    count_the = contents.lower().count('the')
    count_the_space = contents.lower().count('the ')

    print(f"Jumlah 'the': {count_the}")
    print(f"Jumlah 'the ': {count_the_space}")
