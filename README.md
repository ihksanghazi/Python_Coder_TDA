# 👶 Belajar Python GUI dengan Tkinter!

Hai, teman-teman! Kali ini kita akan belajar membuat **program GUI (tampilan jendela)** dengan Python menggunakan pustaka bernama **Tkinter**.

Kita akan membuat dua program:

1. 😊 Program menyapa nama kita (Hello!)
2. 🌍 Program tanya jawab ibu kota dunia (dan bisa belajar juga!)

---

## 1️⃣ Program Greet Me! (Sapa Aku)

### 🎯 Tujuan:

- Menampilkan jendela
- Menampilkan kotak teks untuk mengetik nama
- Menampilkan tombol
- (Bonus: Menyapa nama yang diketik)

### 💻 Contoh Kode:

```python
from tkinter import Tk, Entry, Label, Button

# Membuat jendela utama
root = Tk()
root.title("Tkinter Example")
root.geometry("400x100")  # Ukuran jendela

# Label (teks)
label = Label(root, text="Enter Your Name:")
label.pack()

# Kotak untuk mengetik
entry = Entry(root)
entry.pack()

# Tombol
button = Button(root, text="Greet Me")
button.pack()

# Menjalankan jendela
root.mainloop()
```

### 🧠 Catatan:

- **Label** digunakan untuk teks.
- **Entry** adalah tempat kamu bisa mengetik.
- **Button** adalah tombol, tapi belum kita kasih aksi apa-apa (bisa kamu tambahkan sendiri nanti!).

---

## 2️⃣ Program Ask the Expert - Capital Cities 🌍

### 🎯 Tujuan:

- Mengetik nama negara
- Program menjawab apa ibu kotanya
- Kalau tidak tahu, kita bisa ajari dia!
- Semua data disimpan ke file

### 📁 Isi File yang Dibutuhkan: **m12_capital_data.txt**

Contoh isi:

```txt
Indonesia/Jakarta
France/Paris
Japan/Tokyo
```

### 💻 Kode Ringkas:

```python
from tkinter import Tk, messagebox, font, Label, Entry, Button
from os.path import exists

root = Tk()
root.withdraw()  # Menyembunyikan jendela utama

the_world = {}

def read_from_file():
    if exists('m12_capital_data.txt'):
        with open('m12_capital_data.txt') as file:
            for line in file:
                country, city = line.strip().split('/')
                the_world[country] = city

def write_to_file(country_name, city_name):
    with open('m12_capital_data.txt', 'a') as file:
        file.write('\n' + country_name + '/' + city_name)

def custom_askstring(title, prompt):
    dialog = Tk()
    dialog.title(title)
    Label(dialog, text=prompt).pack()
    entry = Entry(dialog)
    entry.pack()

    def ok():
        dialog.result = entry.get()
        dialog.destroy()

    Button(dialog, text="OK", command=ok).pack()
    dialog.wait_window()
    return getattr(dialog, 'result', "")

read_from_file()

while True:
    country = custom_askstring("Country", "Type the name of a country:")
    if not country:
        break

    country = country.capitalize()
    if country in the_world:
        city = the_world[country]
        messagebox.showinfo("Answer", f"The capital of {country} is {city}.")
    else:
        city = custom_askstring("Teach me", f"I don't know! What's the capital of {country}?")
        if city:
            the_world[country] = city
            write_to_file(country, city)
# lanjutannya bisa dilihat di m12_ask_the_expert.py
```
