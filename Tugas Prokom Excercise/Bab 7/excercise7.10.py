responses = {}

polling_aktif = True

while polling_aktif:
    nama = input("\nSiapa nama Anda? ")
    tempat = input("Jika Anda bisa mengunjungi satu tempat di dunia, "
                   "ke mana Anda akan pergi? ")

    responses[nama] = tempat

    ulang = input("Apakah ada orang lain yang mau ikut polling? (ya/tidak) ")
    if ulang == 'tidak':
        polling_aktif = False

print("\n--- Hasil Polling ---")
for nama, tempat in responses.items():
    print(f"{nama} ingin berlibur ke {tempat}.")