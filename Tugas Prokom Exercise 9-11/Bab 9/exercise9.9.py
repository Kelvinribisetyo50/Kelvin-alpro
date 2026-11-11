class Car:
    """Kelas sederhana untuk merepresentasikan mobil."""

    def __init__(self, make, model, year):
        """Inisialisasi atribut mobil."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Mengembalikan nama deskriptif yang rapi."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Mencetak jarak tempuh mobil."""
        print(f"Mobil ini sudah menempuh {self.odometer_reading} mil.")

    def update_odometer(self, mileage):
        """Mengatur odometer; tidak boleh diputar mundur."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Kamu tidak boleh memundurkan odometer!")

    def increment_odometer(self, miles):
        """Menambah jarak tempuh pada odometer."""
        self.odometer_reading += miles


class Battery:
    """Kelas sederhana untuk merepresentasikan baterai mobil listrik."""

    def __init__(self, battery_size=40):
        """Inisialisasi atribut baterai."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Mencetak kapasitas baterai."""
        print(f"Mobil ini memiliki baterai {self.battery_size}-kWh.")

    def get_range(self):
        """Mencetak perkiraan jarak tempuh sesuai ukuran baterai."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"Mobil ini dapat menempuh sekitar {range} mil dengan sekali pengisian penuh.")

    def upgrade_battery(self):
        """Meng-upgrade baterai ke kapasitas 65 jika belum."""
        if self.battery_size != 65:
            self.battery_size = 65


class ElectricCar(Car):
    """Mewakili aspek mobil yang spesifik untuk mobil listrik."""

    def __init__(self, make, model, year):
        """Inisialisasi atribut kelas induk, lalu buat objek Battery."""
        super().__init__(make, model, year)
        self.battery = Battery()


my_leaf = ElectricCar("BYD", "Atto 1", 2024) 
print(my_leaf.get_descriptive_name())

my_leaf.battery.get_range()
my_leaf.battery.upgrade_battery()
my_leaf.battery.get_range()