def get_kota_negara(kota, negara, populasi=''):
    """Mengembalikan 'Kota, Negara', atau 'Kota, Negara - population xxx'."""
    kota_negara = f"{kota.title()}, {negara.title()}"
    if populasi:
        kota_negara += f" - population {populasi}"
    return kota_negara