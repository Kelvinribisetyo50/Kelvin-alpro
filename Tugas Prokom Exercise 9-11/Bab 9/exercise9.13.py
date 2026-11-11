from random import randint


class Die:
    """Kelas sederhana untuk merepresentasikan sebuah dadu."""

    def __init__(self, sides=6):
        """Inisialisasi jumlah sisi dadu (default 6)."""
        self.sides = sides

    def roll_die(self):
        """Mencetak angka acak antara 1 dan jumlah sisi dadu."""
        print(randint(1, self.sides))


die_6 = Die()
print("Melempar dadu 6 sisi sebanyak 10 kali:")
for roll_num in range(10):
    die_6.roll_die()

die_10 = Die(10)
print("\nMelempar dadu 10 sisi sebanyak 10 kali:")
for roll_num in range(10):
    die_10.roll_die()

die_20 = Die(20)
print("\nMelempar dadu 20 sisi sebanyak 10 kali:")
for roll_num in range(10):
    die_20.roll_die()