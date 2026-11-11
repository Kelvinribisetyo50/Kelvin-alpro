class User:
    """Kelas sederhana untuk merepresentasikan profil pengguna."""

    def __init__(self, first_name, last_name, age, email, location):
        """Inisialisasi atribut profil pengguna."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location
        self.login_attempts = 0  # nilai default

    def describe_user(self):
        """Mencetak ringkasan informasi pengguna."""
        print(f"Nama lengkap : {self.first_name} {self.last_name}")
        print(f"Umur         : {self.age} tahun")
        print(f"Email        : {self.email}")
        print(f"Lokasi       : {self.location}")

    def greet_user(self):
        """Mencetak sapaan yang dipersonalisasi untuk pengguna."""
        print(f"Halo, {self.first_name} {self.last_name}! Selamat datang kembali.")

    def increment_login_attempts(self):
        """Menambah jumlah percobaan login sebanyak 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Mengatur ulang jumlah percobaan login menjadi 0."""
        self.login_attempts = 0


user = User("Kelvin", "Ribisetyo", 25, "kelvinganteng15@gmail.com", "Pemalang")

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

print(f"Percobaan login: {user.login_attempts}")

user.reset_login_attempts()
print(f"Percobaan login setelah reset: {user.login_attempts}")