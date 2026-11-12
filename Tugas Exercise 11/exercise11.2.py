from fungsi_kota import get_kota_negara
def test_kota_negara():
    """Apakah 'santiago' dan 'chile' menghasilkan 'Santiago, Chile'?"""
    hasil = get_kota_negara('santiago', 'chile')
    assert hasil == 'Santiago, Chile'

def test_kota_negara_populasi():
    """Apakah 'santiago', 'chile', populasi=5000000 berhasil?"""
    hasil = get_kota_negara('santiago', 'chile', populasi=5000000)
    assert hasil == 'Santiago, Chile - population 5000000'