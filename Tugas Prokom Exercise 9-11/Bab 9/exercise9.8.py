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

hak_akses = [
    "can add post",
    "can delete post",
    "can ban user",
    "can edit user",
]
admin = Admin("Kelvin", "Ribisetyo", 35, "kelvinganteng15@gmail.com", "Pemalang", hak_akses)
admin.privileges.show_privileges()