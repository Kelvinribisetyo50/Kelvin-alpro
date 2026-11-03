def hitung_cairan_dehidrasi():
    print("=== Program Menentukan Kebutuhan Cairan Pengganti Dehidrasi ===")
    
    try:
        # Input berat badan pasien
        berat_badan = float(input("Masukkan berat badan pasien (kg): "))
        
        # Menu pilihan tingkat dehidrasi
        print("\nPilih Derajat Dehidrasi:")
        print("1. Dehidrasi Ringan (Defisit ~50 ml/kgBB)")
        print("2. Dehidrasi Sedang (Defisit ~75 ml/kgBB)")
        print("3. Dehidrasi Berat  (Defisit ~100 ml/kgBB)")
        pilihan = int(input("Masukkan pilihan (1/2/3): "))
        
        # Logika penentuan faktor pengali cairan
        if pilihan == 1:
            faktor = 50
            status = "Dehidrasi Ringan"
        elif pilihan == 2:
            faktor = 75
            status = "Dehidrasi Sedang"
        elif pilihan == 3:
            faktor = 100
            status = "Dehidrasi Berat"
        else:
            print("Pilihan derajat dehidrasi tidak valid!")
            return

        # Perhitungan total cairan
        cairan_pengganti = berat_badan * faktor
        
        # Output hasil perhitungan
        print("\n================ Hasil Analisis ================")
        print(f"Berat Badan: {berat_badan} kg")
        print(f"Status: {status}")
        print(f"Kebutuhan Cairan Pengganti: {cairan_pengganti:.0f} ml ({cairan_pengganti/1000:.2f} Liter)")
        
        if pilihan == 3:
            print("\n[PERINGATAN]: Dehidrasi berat membutuhkan penanganan medis segera!")
        print("================================================")
        
    except ValueError:
        print("Pesan Kesalahan: Harap masukkan input berupa angka yang valid!")

# Menjalankan program
if __name__ == "__main__":
    hitung_cairan_dehidrasi()