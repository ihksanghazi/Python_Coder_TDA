# 🎨 Pertemuan 11 Python GUI: Canvas & Kalender Countdown

Hai teman-teman! Hari ini kita akan belajar **Python GUI (Graphical User Interface)** menggunakan **Tkinter**. Kita akan membuat dua proyek seru:

1. 🖼️ Membuat kanvas kosong
2. 📆 Menampilkan countdown ke hari-hari penting + jam digital

---

## 📦 Apa Itu Tkinter?

`Tkinter` adalah cara untuk membuat **jendela dan tombol-tombol** di Python. Kita bisa membuat aplikasi dengan tampilan seperti game atau alat bantu visual!

---

## 🖼️ Proyek 1: Kanvas Kosong (Empty Canvas)

### 🎯 Tujuan:

- Membuat jendela kosong
- Menambahkan area gambar (canvas)

### 💻 Kode:

```python
from tkinter import Tk, Canvas

# Membuat jendela utama
root = Tk()

# Judul jendela
root.title("Empty Canvas")

# Membuat kanvas putih berukuran 400x300 piksel
canvas = Canvas(root, width=400, height=300, bg="white")
canvas.pack()

# Menjalankan jendela
root.mainloop()
```

### 📌 Hasil:

- Sebuah jendela muncul dengan latar putih.
- Ini seperti kertas kosong tempat kamu bisa menggambar nanti!

---

## 📆 Proyek 2: Countdown Calendar + Jam

### 🎯 Tujuan:

Tujuan:

- Menampilkan daftar event penting
- Menampilkan berapa hari lagi menuju event
- Menampilkan **jam dan tanggal** yang berjalan real-time!

### 🧠 Hal yang Dipelajari:

- Membaca file teks (**m11_events.txt**)
- Menghitung selisih tanggal
- Menampilkan waktu
- Menggambar teks ke kanvas
- Gunakan **warna berbeda** untuk event yang dekat!

### 💻 Kode (singkat):

```python
from tkinter import Tk, Canvas
from datetime import datetime

# Fungsi untuk update jam
def update_clock():
    now = datetime.now()
    current_time = now.strftime('%H:%M:%S')
    current_date = now.strftime('%d/%m/%Y')
    c.itemconfig(clock_text, text=f"Date: {current_date}\nTime: {current_time}")
    root.after(1000, update_clock)

# Fungsi ambil event dari file
def get_events():
    list_events = []
    with open('m11_events.txt') as file:
        for line in file:
            line = line.rstrip('\n')
            current_event = line.split(',')
            event_date = datetime.strptime(current_event[1], '%d/%m/%y').date()
            current_event[1] = event_date
            list_events.append(current_event)
    return list_events

# Hitung selisih hari
def days_between_dates(date1, date2):
    return str((date1 - date2).days)

# Setup jendela dan canvas
root = Tk()
root.title("Countdown Calendar")
c = Canvas(root, width=800, height=500, bg="green")
c.pack()
c.create_text(100, 50, anchor='w', fill='orange', font='Arial 28 bold underline', text='My Countdown Calendar')

events = get_events()
today = datetime.now().date()
vertical_space = 100

# Urutkan dan tampilkan event
events.sort(key=lambda x: x[1])
for event in events:
    event_name = event[0]
    days_until = days_between_dates(event[1], today)
    display = f"It is {days_until} days until {event_name}"
    text_col = 'red' if int(days_until) <= 7 else 'lightblue'
    c.create_text(100, vertical_space, anchor='w', fill=text_col, font='Arial 28 bold', text=display)
    vertical_space += 30

# Tampilkan jam digital
clock_text = c.create_text(750, 400, anchor='e', fill='white', font='Arial 18 bold')
update_clock()
root.mainloop()
```
