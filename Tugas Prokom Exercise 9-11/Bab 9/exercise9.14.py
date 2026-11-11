from random import choice

pilihan = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E")

pemenang = []
while len(pemenang) < 4:
    hasil = choice(pilihan)
    if hasil not in pemenang:
        pemenang.append(hasil)

print("Setiap tiket yang cocok dengan keempat angka/huruf berikut memenangkan hadiah:")
for item in pemenang:
    print(item)