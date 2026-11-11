try:
    first_number = int(input("Masukkan angka pertama: "))
    second_number = int(input("Masukkan angka kedua: "))
except ValueError:
    print("Maaf, input harus berupa angka. Silakan coba lagi.")
else:
    total = first_number + second_number
    print(f"Hasil penjumlahan: {total}")