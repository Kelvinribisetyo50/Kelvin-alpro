glossary = {
    # Lima istilah dari latihan 6.3
    "variable": "Nama yang digunakan untuk menyimpan nilai atau data di dalam program.",
    "string": "Rangkaian karakter yang ditulis di dalam tanda kutip, misalnya teks.",
    "list": "Kumpulan item berurutan yang disimpan dalam satu variabel dan ditulis dengan kurung siku.",
    "loop": "Struktur yang mengulang sekumpulan perintah sampai kondisi tertentu terpenuhi.",
    "dictionary": "Kumpulan pasangan key-value yang memungkinkan kita mengambil nilai berdasarkan key-nya.",
  
    # Lima istilah baru
    "integer": "Bilangan bulat tanpa bagian desimal, misalnya 5 atau -12.",
    "float": "Bilangan yang memiliki bagian desimal, misalnya 3.14.",
    "function": "Blok kode bernama yang dapat dipanggil berulang kali untuk melakukan tugas tertentu.",
    "boolean": "Tipe data yang hanya bernilai True atau False.",
    "comment": "Catatan dalam kode yang diawali tanda # dan diabaikan oleh Python.",
}

for word, meaning in glossary.items():
    print(f"{word.title()}:\n\t{meaning}\n")