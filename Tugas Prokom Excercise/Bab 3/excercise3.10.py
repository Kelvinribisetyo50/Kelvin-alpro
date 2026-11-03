cities = ["Pemalang", "Surakarta", "Boyolali", "Klaten", "Semarang"]

cities.append("Tegal")
print("Setelah append():")
print(cities)

cities.insert(2, "Sukoharjo")
print("\nSetelah insert():")
print(cities)

del cities[0]
print("\nSetelah del:")
print(cities)

popped_city = cities.pop()
print("\nKota yang dihapus dengan pop():", popped_city)
print(cities)

cities.remove("Boyolali")
print("\nSetelah remove():")
print(cities)

cities.sort()
print("\nSetelah sort():")
print(cities)

cities.sort(reverse=True)
print(cities)

cities.reverse()
print("\nSetelah reverse():")
print(cities)

print("\nMenggunakan sorted():")
print(sorted(cities))

print("\nJumlah kota:", len(cities))