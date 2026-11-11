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
        """Membuat ringkasan informasi pengguna."""
        print(f"Nama lengkap : {self.first_name} {self.last_name}")
        print(f"Umur         : {self.age} tahun")
        print(f"Email        : {self.email}")
        print(f"Lokasi       : {self.location}")

    def greet_user(self):
        """Membuat sapaan yang dipersonalisasi untuk pengguna."""
        print(f"Halo, {self.first_name} {self.last_name}! Selamat datang kembali.")


class Admin(User):
    """Kelas untuk administrator, turunan dari kelas User."""

    def __init__(self, first_name, last_name, age, email, location, privileges):
        """Inisialisasi atribut dari kelas induk, lalu tambah atribut privileges."""
        super().__init__(first_name, last_name, age, email, location)
        self.privileges = privileges

    def show_privileges(self):
        """Menampilkan daftar hak akses administrator."""
        print(f"Hak akses yang dimiliki {self.first_name} {self.last_name}:")
        for privilege in self.privileges:
            print(f"- {privilege}")


hak_akses = [
    "can add post",
    "can delete post",
    "can ban user",
    "can edit user",
]
admin = Admin("Kelvin", "Ribisetyo", 35, "kelvinganteng15@gmail.com", "Surakarta", hak_akses)
admin.show_privileges()