# Membuat sebuah class bernama 'Fruits' untuk merepresentasikan buah
class Fruits:
    # Fungsi konstruktor yang dipanggil saat objek dibuat
    def __init__(self, name, shape, color, taste, stock):
        # Menyimpan atribut-atribut buah ke dalam objek
        self.name = name        # Nama buah
        self.shape = shape      # Bentuk buah
        self.color = color      # Warna buah
        self.taste = taste      # Rasa buah
        self.stock = stock      # Jumlah stok buah yang tersedia

    # Method untuk menampilkan deskripsi dari buah
    def describe(self):
        print(f"Fruit: {self.name}")
        print(f"Shape: {self.shape}")
        print(f"Color: {self.color}")
        print(f"Taste: {self.taste}")
        print(f"Stock: {self.stock}")
        print(f"We can make salad, juice, and pudding with {self.name}")
        print()  # Cetak baris kosong

    # Method untuk membuat salad dari buah, dan mengurangi stok
    def make_salad(self):
        print(f"=== {self.name} Stock ===")
        print(f"Remaining stock before making salad is {self.stock} fruits")
        print("Fruit used to make salad : 2 fruits")
        self.stock -= 2  # Kurangi stok sebanyak 2 buah
        print(f"Remaining fruit stock now is {self.stock} fruit")
        print()  # Cetak baris kosong

# Membuat tiga objek buah dengan nama dan atribut yang berbeda
fruits_1 = Fruits("Apple", "Round", "Red", "Sweet", 50)
fruits_2 = Fruits("Banana", "Curved", "Yellow", "Sweet", 20)
fruits_3 = Fruits("Orange", "Round", "Orange", "Sweet and sour", 15)

# Menampilkan deskripsi dari masing-masing buah
fruits_1.describe()
fruits_2.describe()
fruits_3.describe()

# Membuat salad dua kali dari buah 'Apple' (mengurangi stok sebanyak 2 x 2 = 4)
fruits_1.make_salad()
fruits_1.make_salad()

# Menampilkan representasi dari class 'Fruits' (bukan objek)
print(Fruits)        # Output: <class '__main__.Fruits'> (menampilkan tipe class)

# Menampilkan representasi objek fruits_1 (Apple)
print(fruits_1)      # Output: <__main__.Fruits object at ...> (alamat memori objek)

# Menampilkan atribut name dari objek fruits_1
print(fruits_1.name) # Output: Apple
