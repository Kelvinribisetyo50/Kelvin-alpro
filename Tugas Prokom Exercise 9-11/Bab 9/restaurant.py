
class Restaurant:
    """Kelas sederhana untuk merepresentasikan sebuah restoran."""

    def __init__(self, restaurant_name, cuisine_type):
        """Inisialisasi atribut nama restoran, jenis masakan, dan jumlah pelanggan."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # nilai default

    def describe_restaurant(self):
        """Mencetak nama restoran dan jenis masakannya."""
        print(f"Nama restoran: {self.restaurant_name}")
        print(f"Jenis masakan: {self.cuisine_type}")

    def open_restaurant(self):
        """Mencetak pesan bahwa restoran sedang buka."""
        print(f"{self.restaurant_name} sedang buka!")

    def set_number_served(self, number_served):
        """Mengatur jumlah pelanggan yang sudah dilayani."""
        self.number_served = number_served

    def increment_number_served(self, increment):
        """Menambah jumlah pelanggan yang sudah dilayani."""
        self.number_served += increment