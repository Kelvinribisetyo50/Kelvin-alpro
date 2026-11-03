"""
Program Hitung Tarif Parkir Bandara
-----------------------------------
Tarif di bawah hanyalah contoh. Sesuaikan dengan tarif bandara yang sebenarnya
pada kamus TARIF di bagian atas file ini.

Aturan hitung:
- Jam pertama dikenakan tarif jam pertama.
- Jam berikutnya dikenakan tarif per jam (dibulatkan ke atas).
- Total per hari (24 jam) dibatasi tarif maksimum harian.
- Tiket hilang dikenakan denda tetap.

Cara pakai:
    python tarif_parkir_bandara.py
"""

from datetime import datetime
from math import ceil

# Tarif contoh (Rupiah)
TARIF = {
    "motor": {"jam_pertama": 3000, "per_jam": 2000, "maks_harian": 20000},
    "mobil": {"jam_pertama": 6000, "per_jam": 4000, "maks_harian": 60000},
    "bus":   {"jam_pertama": 12000, "per_jam": 8000, "maks_harian": 120000},
}
DENDA_TIKET_HILANG = {"motor": 25000, "mobil": 50000, "bus": 100000}
FORMAT_WAKTU = "%d-%m-%Y %H:%M"


def hitung_tarif(jenis, masuk, keluar, tiket_hilang=False):
    """Mengembalikan dict berisi rincian tarif parkir."""
    if jenis not in TARIF:
        raise ValueError(f"Jenis kendaraan tidak dikenal: {jenis}")
    if keluar < masuk:
        raise ValueError("Waktu keluar tidak boleh lebih awal dari waktu masuk.")

    t = TARIF[jenis]
    durasi_menit = int((keluar - masuk).total_seconds() // 60)
    durasi_jam = max(1, ceil(durasi_menit / 60))  # minimal dihitung 1 jam

    hari_penuh, sisa_jam = divmod(durasi_jam, 24)

    # Biaya untuk sisa jam (di luar hari penuh)
    if sisa_jam == 0:
        biaya_sisa = 0
    else:
        biaya_sisa = t["jam_pertama"] + (sisa_jam - 1) * t["per_jam"]
        biaya_sisa = min(biaya_sisa, t["maks_harian"])

    biaya_parkir = hari_penuh * t["maks_harian"] + biaya_sisa
    denda = DENDA_TIKET_HILANG[jenis] if tiket_hilang else 0

    return {
        "jenis": jenis,
        "durasi_menit": durasi_menit,
        "durasi_jam_dihitung": durasi_jam,
        "biaya_parkir": biaya_parkir,
        "denda": denda,
        "total": biaya_parkir + denda,
    }


def rupiah(angka):
    return "Rp " + f"{angka:,}".replace(",", ".")


def baca_waktu(pesan):
    while True:
        teks = input(pesan).strip()
        try:
            return datetime.strptime(teks, FORMAT_WAKTU)
        except ValueError:
            print("  Format salah. Contoh: 29-10-2026 08:30")


def main():
    print("=== HITUNG TARIF PARKIR BANDARA ===")
    daftar = "/".join(TARIF)
    while True:
        jenis = input(f"Jenis kendaraan ({daftar}): ").strip().lower()
        if jenis in TARIF:
            break
        print("  Jenis tidak valid.")

    while True:
        masuk = baca_waktu("Waktu masuk  (dd-mm-yyyy hh:mm): ")
        keluar = baca_waktu("Waktu keluar (dd-mm-yyyy hh:mm): ")
        if keluar >= masuk:
            break
        print("  Waktu keluar harus setelah waktu masuk. Ulangi.")

    hilang = input("Tiket hilang? (y/t): ").strip().lower() == "y"

    h = hitung_tarif(jenis, masuk, keluar, hilang)
    jam, menit = divmod(h["durasi_menit"], 60)

    print("\n--- RINCIAN ---")
    print(f"Kendaraan     : {h['jenis'].title()}")
    print(f"Durasi        : {jam} jam {menit} menit "
          f"(dihitung {h['durasi_jam_dihitung']} jam)")
    print(f"Biaya parkir  : {rupiah(h['biaya_parkir'])}")
    if h["denda"]:
        print(f"Denda tiket   : {rupiah(h['denda'])}")
    print(f"TOTAL BAYAR   : {rupiah(h['total'])}")


if __name__ == "__main__":
    main()