print("Kalkulator Penjumlahan (ketik 'q' untuk berhenti)")

while True:
    first_number = input("\nMasukkan angka pertama: ")
    if first_number == 'q':
        break

    second_number = input("Masukkan angka kedua: ")
    if second_number == 'q':
        break

    try:
        total = int(first_number) + int(second_number)
    except ValueError:
        print("Maaf, input harus berupa angka. Silakan coba lagi.")
    else:
        print(f"Hasil penjumlahan: {total}")