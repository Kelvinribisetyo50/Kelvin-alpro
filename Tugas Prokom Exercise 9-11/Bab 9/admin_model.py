"""Modul yang berisi kelas Privileges dan Admin."""

from user_model import User


class Privileges:
    """Kelas terpisah untuk menyimpan hak akses administrator."""

    def __init__(self, privileges):
        """Inisialisasi atribut privileges berupa list string."""
        self.privileges = privileges

    def show_privileges(self):
        """Menampilkan daftar hak akses."""
        print("Hak akses yang dimiliki:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    """Kelas untuk administrator, turunan dari kelas User."""

    def __init__(self, first_name, last_name, age, email, location, privileges):
        """Inisialisasi atribut User, lalu buat objek Privileges."""
        super().__init__(first_name, last_name, age, email, location)
        self.privileges = Privileges(privileges)