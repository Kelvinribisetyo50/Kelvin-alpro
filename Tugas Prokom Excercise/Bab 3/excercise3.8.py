places = ['jepang', 'islandia', 'brasil', 'maroko', 'spanyol']

print("Urutan asli:")
print(places)

print("\nsorted() alfabet:")
print(sorted(places))

print("\nMasih urutan asli:")
print(places)

print("\nsorted() alfabet terbalik:")
print(sorted(places, reverse=True))

print("\nMasih urutan asli:")
print(places)

places.reverse()
print("\nSetelah reverse():")
print(places)

places.reverse()
print("\nSetelah reverse() lagi (kembali ke asli):")
print(places)

places.sort()
print("\nSetelah sort():")
print(places)

places.sort(reverse=True)
print("\nSetelah sort(reverse=True):")
print(places)