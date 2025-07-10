# Belajar Python: Buah & Menu Makanan 🍎🍰

## 🧠 Apa itu Class dan Object?

### Class (Kelas)

Class itu seperti **template** atau **cetakan**.
Contoh: Kalau kita punya cetakan untuk membuat kue donat, maka itu disebut `class`.

### Object (Objek)

Object itu adalah **hasil dari class**.
Contoh: Setelah mencetak, kita punya kue donatnya. Nah, itu `object`.

---

## 🍎 Kode Buah-buahan (Fruits)

```python
class Fruits:
    def __init__(self, name, shape, color, taste, stock):
        self.name = name
        self.shape = shape
        self.color = color
        self.taste = taste
        self.stock = stock

    def describe(self):
        print(f"Fruit: {self.name}")
        print(f"Shape: {self.shape}")
        print(f"Color: {self.color}")
        print(f"Taste: {self.taste}")
        print(f"Stock: {self.stock}")
        print(f"We can make salad, juice, and pudding with {self.name}")
        print()

    def make_salad(self):
        print(f"=== {self.name} Stock ===")
        print(f"Remaining stock before making salad is {self.stock} fruits")
        print("Fruit used to make salad : 2 fruits")
        self.stock -= 2
        print(f"Remaining fruit stock now is {self.stock} fruit")
        print()

# Membuat buah-buahan
fruits_1 = Fruits("Apple", "Round", "Red", "Sweet", 50)
fruits_2 = Fruits("Banana", "Curved", "Yellow", "Sweet", 20)

# Menampilkan informasi buah
fruits_1.describe()
fruits_2.describe()

# Membuat salad dari buah
fruits_1.make_salad()
```

### 💡 Apa yang kita pelajari?

- Kita membuat **class Fruits**.
- Setiap buah punya **nama, bentuk, warna, rasa, dan stok**.
- Kita bisa **deskripsikan** dan **mengolah jadi salad**!

---

## 🍰 Kode Menu Makanan dan Minuman

```python
class MenuItem:
    def __init__(self, name, price, details):
        self.name = name
        self.price = price
        self.details = details

    def info(self):
        return f"{self.name}: ${self.price} ({self.details})"

    def get_total_price(self, count):
        total_price = self.price * count
        if count >= 3:
            total_price *= 0.9
        return round(total_price)

# Membuat daftar menu
menu_items = [
    MenuItem('Sandwich', 5, '330kcal'),
    MenuItem('Chocolate Cake', 4, '450kcal'),
    MenuItem('Coffee', 3, '180mL')
]

# Menampilkan menu
print('Menu:')
for index, item in enumerate(menu_items, start=1):
    print(f"{index}. {item.info()}")

# Pilih menu dan jumlah
menu_order = int(input('Pilih nomor menu: ')) - 1
selected_menu = menu_items[menu_order]

count = int(input("Mau beli berapa? (Diskon 10% kalau beli 3 atau lebih): "))
result = selected_menu.get_total_price(count)

print(f"Total harga: ${result}")

```

### 💡 Apa yang kita pelajari?

- Kita membuat menu makanan dengan class **MenuItem**.
- Bisa tampilkan informasi menu.
- Bisa menghitung harga total (dengan diskon jika beli banyak).
