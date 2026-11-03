def hitung_bbi_dan_status():
    print("=== PROGRAM HITUNG BBI & STATUS BERAT BADAN ===")
    
    # Input dari pengguna
    nama = input("Masukkan nama Anda: ")
    gender = input("Masukkan jenis kelamin (Pria/Wanita): ").strip().lower()
    tinggi = float(input("Masukkan tinggi badan (cm): "))
    berat = float(input("Masukkan berat badan (kg): "))
    
    # 1. Menghitung Berat Badan Ideal (BBI) - Rumus Broca
    if gender == "pria":
        bbi = (tinggi - 100) - ((tinggi - 100) * 0.10)
    elif gender == "wanita":
        bbi = (tinggi - 100) - ((tinggi - 100) * 0.15)
    else:
        print("Jenis kelamin tidak valid. Menggunakan perhitungan standar umum.")
        bbi = tinggi - 100
        
    # 2. Menghitung Indeks Massa Tubuh (IMT) untuk Status Berat Badan
    tinggi_meter = tinggi / 100
    imt = berat / (tinggi_meter ** 2)
    
    # Menentukan Status Berat Badan (Standar Kemenkes RI)
    if imt < 18.5:
        status = "Kurus (Kekurangan berat badan)"
    elif 18.5 <= imt <= 25.0:
        status = "Normal (Ideal)"
    elif 25.1 <= imt <= 27.0:
        status = "Gemuk (Kelebihan berat badan tingkat ringan)"
    else:
        status = "Obesitas (Kelebihan berat badan tingkat berat)"
        
    # Menampilkan Hasil
    print("\n" + "="*40)
    print(f"Hasil Analisis untuk {nama}:")
    print(f"- Berat Badan Ideal (BBI) Anda : {bbi:.2f} kg")
    print(f"- Skor IMT Anda                : {imt:.2f}")
    print(f"- Status Berat Badan Anda      : {status}")
    print("="*40)

# Menjalankan program
hitung_bbi_dan_status()