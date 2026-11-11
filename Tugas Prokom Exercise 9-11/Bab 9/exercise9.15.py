from random import sample

pilihan = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E")
my_ticket = (3, 7, "A", "C")

percobaan = 0
while True:
    percobaan += 1
    undian = sample(pilihan, 4)
    if set(undian) == set(my_ticket):
        break

print(f"Tiketmu menang setelah {percobaan} kali undian.")
print(f"Tiket kamu: {my_ticket}")
print(f"Hasil undian: {undian}")