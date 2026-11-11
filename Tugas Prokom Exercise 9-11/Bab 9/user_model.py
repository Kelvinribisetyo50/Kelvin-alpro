"""Modul yang berisi kelas User."""


class User:
    """Kelas sederhana untuk merepresentasikan profil pengguna."""

    def __init__(self, first_name, last_name, age, email, location):
        """Inisialisasi atribut profil pengguna."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location

    def describe_user(self):
        """Mencetak ringkasan informasi pengguna."""
        print(f"Nama lengkap : {self.first_name} {self.last_name}")
        print(f"Umur         : {self.age} tahun")
        print(f"Email        : {self.email}")
        print(f"Lokasi       : {self.location}")

    def greet_user(self):
        """Mencetak sapaan yang dipersonalisasi untuk pengguna."""
        print(f"Halo, {self.first_name} {self.last_name}! Selamat datang kembali.")