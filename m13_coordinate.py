# Mengimpor Tk dan Canvas dari pustaka tkinter
from tkinter import Tk, Canvas

# Membuat jendela utama
window = Tk()

# Mengatur ukuran jendela menjadi 400x300 piksel
window.geometry("400x300")

# Membuat area gambar (canvas) berukuran 400x300
canvas = Canvas(window, width=400, height=300)
canvas.pack()  # Menampilkan canvas ke dalam jendela

# Menentukan titik tengah lingkaran (x=200, y=150)
x_center = 200
y_center = 150

# Menentukan jari-jari lingkaran
radius = 50

# Menggambar lingkaran dengan cara membuat oval (dari kotak pembatas)
canvas.create_oval(
    x_center - radius, y_center - radius,  # Titik kiri atas dari oval
    x_center + radius, y_center + radius,  # Titik kanan bawah dari oval
    fill="blue"  # Warna dalamnya biru
)

# Menggambar persegi panjang (kotak) dengan koordinat pojok kiri atas (210,210) dan kanan bawah (280,280)
canvas.create_rectangle(210, 210, 280, 280, fill="yellow")  # Kotak berwarna kuning

# Menjalankan jendela agar tetap tampil
window.mainloop()
