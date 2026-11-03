# Latihan 4-15: Program 3 (menu prasmanan), sudah sesuai PEP 8

# Tuple tidak bisa diubah itemnya, jadi menu awal ditulis sekali
menu = (
    'nasi uduk', 'ayam goreng', 'semur jengkol', 'sayur sop',
    'sambal terasi',
)

print("Menu prasmanan:")
for makanan in menu:
    print(makanan)

# Menu diganti dengan menimpa seluruh tuple
menu = (
    'nasi goreng', 'ayam goreng', 'semur jengkol', 'soto ayam',
    'sambal terasi',
)

print("\nMenu yang sudah direvisi:")
for makanan in menu:
    print(makanan)