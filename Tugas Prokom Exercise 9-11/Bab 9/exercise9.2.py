class Restaurant: 
    """Kelas Sederhana untuk mempresentasikan sebuah restoran"""
    
    def __init__(self, restaurant_name, cuisine_type):
        """inisialisasi atribut restaurant name dan cuisine type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        """Mencetak nama restaurant dan jenis masakannya"""
        print(f"Nama restaurant: {self.restaurant_name.title()}")
        print(f"Jenis masakan: {self.cuisine_type.title()}")
        
    def open_restaurant(self):
        """Mencetak bahwa restaurant sedang buka"""
        print(f"{self.restaurant_name} sedang buka.""")
        
restaurant_1 = Restaurant("Sarapan Bu Yanti", "Nasi Uduk dan Nasi Bungkus")
restaurant_2 = Restaurant("Warjaw Fakultas Teknik", "Ayam Geprek dan Soto Ayam")
restaurant_3 = Restaurant("Warung Makan Aurora", "Sayur Asem dan Ayam Balado")

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()
