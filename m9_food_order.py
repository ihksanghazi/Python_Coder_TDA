# Membuat kelas MenuItem untuk mewakili item di menu makanan/minuman
class MenuItem:
    # Konstruktor: dipanggil saat objek dibuat
    def __init__(self, name, price, details):
        self.name = name        # Nama item, misalnya "Sandwich"
        self.price = price      # Harga item
        self.details = details  # Detail tambahan seperti kalori atau volume

    # Method untuk menampilkan informasi item dalam format yang rapi
    def info(self):
        return f"{self.name}: ${self.price} ({self.details})"

    # Method untuk menghitung total harga berdasarkan jumlah pembelian
    def get_total_price(self, count):
        total_price = self.price * count  # Total harga awal (belum diskon)
        if count >= 3:                    # Jika beli 3 atau lebih, dapat diskon 10%
            total_price *= 0.9            # Diskon 10%
        return round(total_price)         # Mengembalikan harga total dibulatkan
        

# Daftar item menu dimasukkan ke dalam list
menu_items = [
    MenuItem('Sandwich', 5, '330kcal'),
    MenuItem('Chocolate Cake', 4, '450kcal'),
    MenuItem('Cream Puff', 2, '180kcal'),
    MenuItem('Coffee', 3, '180mL'),
    MenuItem('Orange Juice', 2, '350mL'),
    MenuItem('Espresso', 3, '30mL')
]

# Menampilkan daftar menu dengan nomor urut
print('Menu:')
for index, item in enumerate(menu_items, start=1):
    print(f"{index}. {item.info()}")  # Menampilkan info dari tiap item menu

print('--------------------')

# Meminta input dari user untuk memilih item menu (berdasarkan nomor)
menu_order = int(input('Enter menu item number: ')) - 1  # dikurangi 1 karena index list mulai dari 0
selected_menu = menu_items[menu_order]  # Mengambil item yang dipilih

# Meminta jumlah pesanan
count = int(input("How many meals would you like to purchase? (10% off for 3 or more): "))

# Hitung total harga berdasarkan jumlah
result = selected_menu.get_total_price(count)

# Tampilkan total harga yang harus dibayar
print(f"Your total is ${result}")
