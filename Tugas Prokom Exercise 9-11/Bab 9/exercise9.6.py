class Restaurant:
    """Kelas sederhana untuk merepresentasikan sebuah restoran."""

    def __init__(self, restaurant_name, cuisine_type):
        """Inisialisasi atribut nama restoran dan jenis masakan."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Mencetak nama restoran dan jenis masakannya."""
        print(f"Nama restoran: {self.restaurant_name}")
        print(f"Jenis masakan: {self.cuisine_type}")

    def open_restaurant(self):
        """Mencetak pesan bahwa restoran sedang buka."""
        print(f"{self.restaurant_name} sedang buka!")


class IceCreamStand(Restaurant):
    """Kelas untuk kios es krim, turunan dari kelas Restaurant."""

    def __init__(self, restaurant_name, cuisine_type, flavors):
        """Inisialisasi atribut dari kelas induk, lalu tambah atribut flavors."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        """Menampilkan daftar rasa es krim yang tersedia."""
        print(f"Rasa es krim yang tersedia di {self.restaurant_name}:")
        for flavor in self.flavors:
            print(f"- {flavor}")


rasa_es_krim = ["Vanila", "Cokelat", "Stroberi", "Matcha", "Durian"]
ice_cream_stand = IceCreamStand("Es Krim Segar", "Es Krim", rasa_es_krim)
ice_cream_stand.display_flavors()