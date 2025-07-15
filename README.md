# 🧒 Belajar Python GUI dengan Tkinter: Gambar dan Karakter Lucu!

Halo, teman-teman kecil! 👋  
Hari ini kita akan belajar membuat gambar dan karakter lucu menggunakan **Python dan Tkinter**. Kita akan membuat:

1. 🎨 **Lingkaran dan Kotak di Layar**
2. 🐱 **Peliharaan Digital yang Bisa Berkedip!**

---

## 1️⃣ Gambar Lingkaran dan Kotak

**📁 File: `m13_coordinate.py`**

### 💡 Tujuan:

- Belajar membuat gambar menggunakan **Canvas**
- Menentukan posisi (koordinat) di layar
- Menggambar **lingkaran** dan **kotak**

### 🧠 Konsep yang Dipelajari:

- Titik X dan Y (koordinat)
- Warna dan bentuk
- Ukuran dan posisi

### 🖼️ Contoh Kode:

```python
from tkinter import Tk, Canvas

window = Tk()
window.geometry("400x300")

canvas = Canvas(window, width=400, height=300)
canvas.pack()

x_center = 200
y_center = 150
radius = 50

# Menggambar lingkaran biru di tengah
canvas.create_oval(x_center - radius, y_center - radius, x_center + radius, y_center + radius, fill="blue")

# Menggambar kotak kuning di pojok kanan bawah
canvas.create_rectangle(210, 210, 280, 280, fill="yellow")

window.mainloop()
```

### 🧪 Coba Sendiri!

- Ganti warna lingkaran dan kotak.
- Ubah posisi dengan mengganti angka koordinat.
- Tambahkan lebih banyak bentuk.

---

## 2️⃣ Screen Pet - Karakter Lucu yang Berkedip!

**📁 File: `screen_pet.py`**

### 🐾 Tujuan:

- Membuat karakter dengan wajah lucu
- Menambahkan mata, pipi, mulut, lidah
- Membuat animasi **berkedip** otomatis

### 🧠 Konsep yang Dipelajari:

- Gambar karakter dengan **oval, rectangle, line**
- Mengatur elemen untuk **muncul dan menghilang**
- Menggunakan `after()` untuk membuat **animasi**

### 🖼️ Contoh Fitur yang Dibuat:

- Mata putih dan pupil hitam
- Mulut (normal, senyum, sedih)
- Lidah (disembunyikan)
- **Animasi berkedip setiap 3 detik!**

### ✨ Contoh Kode Ringkas:

```python
from tkinter import HIDDEN, NORMAL, Tk, Canvas

root = Tk()
root.title("Screen Pet")

c = Canvas(root, width=400, height=400, bg='dark blue', highlightthickness=0)
c.pack()

c.body_color = 'SkyBlue1'
body = c.create_oval(35, 20, 365, 350, outline=c.body_color, fill=c.body_color)

eye_left = c.create_oval(130, 110, 160, 170, outline='black', fill='white')
eye_right = c.create_oval(230, 110, 260, 170, outline='black', fill='white')
pupil_left = c.create_oval(140, 145, 150, 155, outline='black', fill='black')
pupil_right = c.create_oval(240, 145, 250, 155, outline='black', fill='black')

# Fungsi berkedip
def toggle_eyes():
    current_color = c.itemcget(eye_left, 'fill')
    new_color = c.body_color if current_color == 'white' else 'white'
    current_state = c.itemcget(pupil_left, 'state')
    new_state = NORMAL if current_state == HIDDEN else HIDDEN
    c.itemconfigure(pupil_left, state=new_state)
    c.itemconfigure(pupil_right, state=new_state)
    c.itemconfigure(eye_left, fill=new_color)
    c.itemconfigure(eye_right, fill=new_color)

def blink():
    toggle_eyes()
    root.after(250, toggle_eyes)
    root.after(3000, blink)

root.after(1000, blink)
root.mainloop()
```
