def hitung_penggajian_jabatan():
    print("=== PROGRAM HITUNG PENGGAJIAN BERDASARKAN JABATAN ===")
    
    # Input data karyawan
    nama = input("Masukkan Nama Karyawan: ")
    
    print("\nPilihan Jabatan yang Tersedia:")
    print("1. Manajer")
    print("2. Supervisor")
    print("3. Staff")
    jabatan = input("Masukkan Jabatan Karyawan (Manajer/Supervisor/Staff): ").strip().capitalize()
    
    # Logika IF untuk menentukan Gaji Pokok dan Tunjangan berdasarkan Jabatan
    if jabatan == "Manajer":
        gaji_pokok = 8500000
        tunjangan = 2000000
    elif jabatan == "Supervisor":
        gaji_pokok = 6000000
        tunjangan = 1200000
    elif jabatan == "Staff":
        gaji_pokok = 4500000
        tunjangan = 6000000
    else:
        # Pilihan jika jabatan tidak dikenali (dianggap Karyawan Magang/Lainnya)
        print("\n[Info] Jabatan tidak terdaftar di sistem. Menggunakan tarif standar.")
        gaji_pokok = 3500000
        tunjangan = 300000
        jabatan = f"Lainnya ({jabatan})"

    # Input potongan (misal: PPh, BPJS, atau absensi)
    try:
        potongan = float(input("Masukkan Total Potongan/Pajak (Rp): "))
    except ValueError:
        print("\n[Error] Harap masukkan angka yang valid untuk potongan!")
        return

    # Rumus menghitung gaji bersih
    gaji_bersih = gaji_pokok + tunjangan - potongan

    # Menampilkan slip gaji
    print("\n==========================================")
    print(f"               SLIP GAJI KARYAWAN        ")
    print("==========================================")
    print(f"Nama Karyawan : {nama}")
    print(f"Jabatan       : {jabatan}")
    print("------------------------------------------")
    print(f"Gaji Pokok    : Rp {gaji_pokok:,.2f}")
    print(f"Tunjangan     : Rp {tunjangan:,.2f}")
    print(f"Potongan      : Rp {potongan:,.2f}")
    print("------------------------------------------")
    print(f"GAJI BERSIH   : Rp {gaji_bersih:,.2f}")
    print("==========================================")

# Menjalankan fungsi program
if __name__ == "__main__":
    hitung_penggajian_jabatan()