# Latihan 4-15: Program 2 (kubik dan irisan), sudah sesuai PEP 8

# Membuat daftar kubik dari 1 sampai 10
kubik = []
for nilai in range(1, 11):
    kubik.append(nilai ** 3)

for angka in kubik:
    print(angka)

# Irisan: tiga item pertama, tengah, dan terakhir
print("\nTiga item pertama dalam daftar adalah:")
print(kubik[:3])

print("\nTiga item dari tengah daftar adalah:")
print(kubik[3:6])

print("\nTiga item terakhir dalam daftar adalah:")
print(kubik[-3:])