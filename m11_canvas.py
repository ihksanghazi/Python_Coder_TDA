# Mengimpor dua komponen dari tkinter: Tk (jendela utama) dan Canvas (area gambar)
from tkinter import Tk, Canvas

# Membuat jendela utama aplikasi GUI (Graphical User Interface)
root = Tk()

# Memberi judul pada jendela
root.title("Empty Canvas")

# Membuat area gambar (canvas) berukuran 400x300 piksel dengan latar belakang putih
canvas = Canvas(root, width=400, height=300, bg="white")

# Menampilkan canvas ke dalam jendela (agar terlihat)
canvas.pack()

# Menjalankan aplikasi (loop utama), agar jendela tetap terbuka dan merespons
root.mainloop()
