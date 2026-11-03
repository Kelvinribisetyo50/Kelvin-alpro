# 5-9. No Users

# Versi 1: daftar berisi pengguna
print("Versi 1 (daftar berisi):")
usernames = ['admin', 'budi', 'siti', 'rina', 'agus']

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Halo admin, apakah kamu ingin melihat laporan status?")
        else:
            print(f"Halo {username.title()}, terima kasih sudah login kembali.")
else:
    print("Kita perlu mencari beberapa pengguna!")

# Versi 2: semua nama dihapus dari daftar
print("\nVersi 2 (daftar kosong):")
usernames.clear()

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Halo admin, apakah kamu ingin melihat laporan status?")
        else:
            print(f"Halo {username.title()}, terima kasih sudah login kembali.")
else:
    print("Kita perlu mencari beberapa pengguna!")