glossary = {
    "variable": "Nama yang digunakan untuk menyimpan nilai atau data di dalam program.",
    "string": "Rangkaian karakter yang ditulis di dalam tanda kutip, misalnya teks.",
    "list": "Kumpulan item berurutan yang disimpan dalam satu variabel dan ditulis dengan kurung siku.",
    "loop": "Struktur yang mengulang sekumpulan perintah sampai kondisi tertentu terpenuhi.",
    "dictionary": "Kumpulan pasangan key-value yang memungkinkan kita mengambil nilai berdasarkan key-nya.",
}

for word, meaning in glossary.items():
    print(f"{word.title()}:\n\t{meaning}\n")