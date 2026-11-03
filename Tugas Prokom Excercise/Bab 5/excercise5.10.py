current_users = ['Admin', 'Bahlil', 'Kelvin', 'Gibran', 'Agus']
new_users = ['kelvin', 'Prabowo', 'ADMIN', 'Jokowi', 'Putri']

current_users_lower = []
for user in current_users:
    current_users_lower.append(user.lower())

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Username '{new_user}' sudah dipakai. Silakan masukkan username lain.")
    else:
        print(f"Username '{new_user}' tersedia.")