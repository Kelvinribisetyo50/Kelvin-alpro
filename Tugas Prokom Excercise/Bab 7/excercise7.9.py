sandwich_orders = ['tuna', 'pastrami', 'telur', 'pastrami', 'ayam',
                   'keju', 'pastrami']
finished_sandwiches = []

print("Maaf, pastrami sudah habis.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    pesanan = sandwich_orders.pop(0)
    print(f"Saya sudah membuat sandwich {pesanan} Anda.")
    finished_sandwiches.append(pesanan)

print("\nSandwich yang sudah dibuat:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")