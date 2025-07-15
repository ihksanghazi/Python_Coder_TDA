# Mengimpor modul dari Tkinter untuk GUI
# HIDDEN dan NORMAL digunakan untuk menyembunyikan dan menampilkan elemen
from tkinter import HIDDEN, NORMAL, Tk, Canvas

# Membuat jendela utama aplikasi
root = Tk()
root.title("Screen Pet")  # Judul jendela

# Membuat area gambar (canvas) dengan ukuran 400x400 dan latar belakang biru gelap
c = Canvas(root, width=400, height=400, bg='dark blue', highlightthickness=0)
c.pack()  # Menampilkan canvas

# Warna tubuh karakter
c.body_color = 'SkyBlue1'

# Menggambar tubuh karakter (lingkaran besar/oval)
body = c.create_oval(35, 20, 365, 350, outline=c.body_color, fill=c.body_color)

# Menggambar mata kiri dan kanan (oval putih)
eye_left = c.create_oval(130, 110, 160, 170, outline='black', fill='white')
eye_right = c.create_oval(230, 110, 260, 170, outline='black', fill='white')

# Menggambar pupil (bulatan hitam di tengah mata)
pupil_left = c.create_oval(140, 145, 150, 155, outline='black', fill='black')
pupil_right = c.create_oval(240, 145, 250, 155, outline='black', fill='black')

# Mulut dalam 3 ekspresi: normal, senyum, sedih
# Hanya mulut normal yang terlihat di awal
mouth_normal = c.create_line(170, 250, 200, 272, 230, 250, smooth=1, width=2, state=NORMAL)
mouth_happy = c.create_line(170, 250, 200, 282, 230, 250, smooth=1, width=2, state=HIDDEN)
mouth_sad = c.create_line(170, 250, 200, 232, 230, 250, smooth=1, width=2, state=HIDDEN)

# Gambar lidah (berwarna merah) tapi disembunyikan dulu
tongue_main = c.create_rectangle(170, 250, 230, 290, outline='red', fill='red', state=HIDDEN)
tongue_tip = c.create_oval(170, 285, 230, 300, outline='red', fill='red', state=HIDDEN)

# Gambar pipi (pink), juga disembunyikan
cheek_left = c.create_oval(70, 180, 120, 230, outline='pink', fill='pink', state=HIDDEN)
cheek_right = c.create_oval(280, 180, 330, 230, outline='pink', fill='pink', state=HIDDEN)

# Fungsi untuk mengganti warna mata dan sembunyikan/tampilkan pupil (seperti membuka/menutup mata)
def toggle_eyes():
    # Ambil warna mata kiri saat ini
    current_color = c.itemcget(eye_left, 'fill')

    # Jika warnanya putih, ganti jadi warna tubuh (tutup mata), jika tidak, ganti jadi putih (buka mata)
    new_color = c.body_color if current_color == 'white' else 'white'

    # Ambil status pupil (NORMAL atau HIDDEN)
    current_state = c.itemcget(pupil_left, 'state')
    new_state = NORMAL if current_state == HIDDEN else HIDDEN

    # Terapkan perubahan ke pupil dan mata
    c.itemconfigure(pupil_left, state=new_state)
    c.itemconfigure(pupil_right, state=new_state)
    c.itemconfigure(eye_left, fill=new_color)
    c.itemconfigure(eye_right, fill=new_color)

# Fungsi untuk animasi berkedip
def blink():
    toggle_eyes()  # Tutup mata
    root.after(250, toggle_eyes)  # Setelah 250ms, buka mata lagi
    root.after(3000, blink)  # Setiap 3 detik, ulangi proses blink

# Mulai animasi berkedip setelah 1 detik aplikasi dibuka
root.after(1000, blink)

# Menjalankan GUI agar jendela tetap tampil
root.mainloop()
