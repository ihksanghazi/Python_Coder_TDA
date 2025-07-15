# 🐾 Python Screen Pet (Pertemuan 14)

## 🎯 Tujuan Proyek

Di pertemuan ini, kita akan membuat **karakter digital lucu** (seperti hewan peliharaan virtual) yang bisa:

- 😄 Tersenyum saat kamu arahkan mouse
- 😢 Sedih kalau kamu diamkan
- 😝 Menjulurkan lidah dan silang mata saat diklik 2x
- 👀 Berkedip sendiri setiap 3 detik

Kita akan belajar membuat ini menggunakan **Python** dan **Tkinter** (modul GUI).

---

## 👶 Apa yang Akan Kamu Pelajari?

- Cara membuat gambar di layar dengan `Canvas`
- Cara membuat karakter dari lingkaran, oval, dan garis
- Cara mendeteksi pergerakan dan klik mouse
- Cara membuat animasi seperti **berkedip** dan **gerak mata**

---

## 📂 Struktur Program

| Bagian                        | Fungsinya                                  |
| ----------------------------- | ------------------------------------------ |
| `Canvas`                      | Tempat menggambar karakter                 |
| Tubuh & Mata                  | Dibuat dengan oval                         |
| Mulut (normal, senyum, sedih) | Ditampilkan berdasarkan emosi karakter     |
| Lidah & pipi                  | Muncul saat karakter senang atau cheeky    |
| Fungsi berkedip               | Otomatis berkedip tiap 3 detik             |
| Fungsi senyum & sedih         | Senyum jika disentuh, sedih jika diabaikan |
| Fungsi cheeky 😝              | Klik 2x → mata silang & lidah keluar       |

---

## 🧠 Penjelasan Mudah Kode

```python
from tkinter import HIDDEN, NORMAL, Tk, Canvas
```

📦 Kita mengimpor alat dari Tkinter untuk membuat jendela dan gambar di layar. `HIDDEN` & `NORMAL` untuk menyembunyikan atau menampilkan bagian wajah.

---

```python
root = Tk()
root.title("Screen Pet")
```

🪟 Membuat jendela utama bernama Screen Pet.

---

```python
c = Canvas(root, width=400, height=400, bg='dark blue')
```

📋 Membuat kanvas tempat menggambar karakter.

---

👤 Gambar Karakter

```python
body = c.create_oval(35, 20, 365, 350, fill='SkyBlue1')  # tubuh
eye_left = c.create_oval(130, 110, 160, 170, fill='white')  # mata kiri
eye_right = c.create_oval(230, 110, 260, 170, fill='white')  # mata kanan
pupil_left = c.create_oval(140, 145, 150, 155, fill='black')  # bola mata kiri
pupil_right = c.create_oval(240, 145, 250, 155, fill='black')  # bola mata kanan
```

---

👄 Mulut dan Lidah

```python
mouth_normal = c.create_line(...) # mulut biasa
mouth_happy = c.create_line(..., state=HIDDEN) # mulut senyum (disembunyi)
mouth_sad = c.create_line(..., state=HIDDEN) # mulut sedih (disembunyi)

tongue_main = c.create_rectangle(..., state=HIDDEN)
tongue_tip = c.create_oval(..., state=HIDDEN)
```

---

😊 Pipi Lucu (Cheeks)

```python
cheek_left = c.create_oval(..., state=HIDDEN)
cheek_right = c.create_oval(..., state=HIDDEN)
```

---

👀 Fungsi Berkedip Otomatis

```python
def toggle_eyes():  # Membuka dan menutup mata
    ...
def blink():  # Berkedip tiap 3 detik
    toggle_eyes()
    root.after(250, toggle_eyes)
    root.after(3000, blink)

root.after(1000, blink)  # Mulai berkedip
```

---

🤗 Ekspresi Senang saat Mouse Mendekat

```python
def show_happy(event):
    # Tampilkan pipi & senyum
    ...

def hide_happy(event):
    # Kembali ke wajah normal

c.bind('<Motion>', show_happy)  # Mouse bergerak di atas karakter
c.bind('<Leave>', hide_happy)   # Mouse keluar dari karakter
```

---

😢 Ekspresi Sedih kalau Tidak Diapa-apain

```python

def sad():
    if c.happy_level == 0:
        # Tampilkan mulut sedih
    else:
        c.happy_level -= 1
    root.after(4000, sad)

root.after(1000, sad)
```

---

😜 Fungsi “Cheeky” (Jail Mode)

```python
def toggle_tongue():
    # Lidah keluar dan masuk

def toggle_pupils():
    # Bola mata berpindah silang dan kembali

def cheeky(event):
    # Gabungkan semuanya: mata silang + lidah keluar
    ...
c.bind('<Double-1>', cheeky)  # Klik dua kali karakter
```
