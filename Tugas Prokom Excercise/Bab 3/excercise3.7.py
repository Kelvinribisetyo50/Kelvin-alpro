guest_list = [
    "Bellingham",
    "Joko Widodo",
    "Neymar Jr.",
    "BJ Habibie",
    "Lionel Messi",
    "Kylian Mbappe"
]
print("Maaf, saya hanya bisa mengundang dua orang untuk makan malam.")
while len(guest_list) > 2:
    removed_guest = guest_list.pop()
    print(f"Maaf {removed_guest}, saya tidak bisa mengundang Anda.")
for guest in guest_list:
    print(f"Halo {guest}, Anda masih diundang untuk makan malam.")
del guest_list[0]
del guest_list[0]
print(guest_list)