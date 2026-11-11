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


# Membuat beberapa instance pengguna yang berbeda
user_1 = User("Kelvin", "Ribisetyo", 19, "kelvinganteng15@gmail.com", "Pemalang")
user_2 = User("Artha", "Milikku", 18, "maulidaartha98@gmail.com", "Yogyakarta")
user_3 = User("Nay", "Anggriyani", 18, "nysrlanggria@gmail.com", "Semarang")

user_1.describe_user()
user_1.greet_user()
print()

user_2.describe_user()
user_2.greet_user()
print()

user_3.describe_user()
user_3.greet_user()