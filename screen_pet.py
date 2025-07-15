# Mengimpor komponen dari tkinter untuk membuat GUI
# HIDDEN dan NORMAL dipakai untuk menyembunyikan atau menampilkan gambar di canvas
from tkinter import HIDDEN, NORMAL, Tk, Canvas

# Membuat jendela utama aplikasi
root = Tk()
root.title("Screen Pet")  # Judul jendela

# Membuat canvas (papan gambar) dengan latar biru tua
c = Canvas(root, width=400, height=400, bg='dark blue', highlightthickness=0)
c.pack()

# Menentukan warna tubuh karakter
c.body_color = 'SkyBlue1'

# Membuat tubuh karakter sebagai oval besar
body = c.create_oval(35, 20, 365, 350, outline=c.body_color, fill=c.body_color)

# Mata karakter (putih)
eye_left = c.create_oval(130, 110, 160, 170, outline='black', fill='white')
eye_right = c.create_oval(230, 110, 260, 170, outline='black', fill='white')

# Pupil (bulatan hitam dalam mata)
pupil_left = c.create_oval(140, 145, 150, 155, outline='black', fill='black')
pupil_right = c.create_oval(240, 145, 250, 155, outline='black', fill='black')

# Mulut dalam 3 versi: normal (tampil), senyum dan sedih (disembunyikan)
mouth_normal = c.create_line(170, 250, 200, 272, 230, 250, smooth=1, width=2, state=NORMAL)
mouth_happy = c.create_line(170, 250, 200, 282, 230, 250, smooth=1, width=2, state=HIDDEN)
mouth_sad = c.create_line(170, 250, 200, 232, 230, 250, smooth=1, width=2, state=HIDDEN)

# Lidah karakter (belum ditampilkan di awal)
tongue_main = c.create_rectangle(170, 250, 230, 290, outline='red', fill='red', state=HIDDEN)
tongue_tip = c.create_oval(170, 285, 230, 300, outline='red', fill='red', state=HIDDEN)

# Pipi karakter (warna pink), juga disembunyikan
cheek_left = c.create_oval(70, 180, 120, 230, outline='pink', fill='pink', state=HIDDEN)
cheek_right = c.create_oval(280, 180, 330, 230, outline='pink', fill='pink', state=HIDDEN)

# Fungsi untuk membuka atau menutup mata (berkedip)
def toggle_eyes():
    current_color = c.itemcget(eye_left, 'fill')  # Ambil warna mata kiri
    new_color = c.body_color if current_color == 'white' else 'white'  # Ganti jadi biru (tutup) atau putih (buka)
    
    current_state = c.itemcget(pupil_left, 'state')  # Cek status pupil (tampil/sembunyi)
    new_state = NORMAL if current_state == HIDDEN else HIDDEN  # Ganti statusnya
    
    # Terapkan ke kedua mata dan pupil
    c.itemconfigure(pupil_left, state=new_state)
    c.itemconfigure(pupil_right, state=new_state)
    c.itemconfigure(eye_left, fill=new_color)
    c.itemconfigure(eye_right, fill=new_color)

# Fungsi untuk berkedip setiap 3 detik
def blink():
    toggle_eyes()
    root.after(250, toggle_eyes)   # Buka mata setelah 250ms
    root.after(3000, blink)        # Lanjut berkedip setiap 3 detik

# Jalankan fungsi blink setelah 1 detik saat program dimulai
root.after(1000, blink)

# ========== Pertemuan 14: interaksi mouse ========== #

# Fungsi menunjukkan ekspresi senang saat mouse masuk area karakter
def show_happy(event):
    if (20 <= event.x <= 350) and (20 <= event.y <= 350):
        c.itemconfigure(cheek_left, state=NORMAL)
        c.itemconfigure(cheek_right, state=NORMAL)
        c.itemconfigure(mouth_happy, state=NORMAL)
        c.itemconfigure(mouth_normal, state=HIDDEN)
        c.itemconfigure(mouth_sad, state=HIDDEN)
        c.happy_level = 1
    return

# Hubungkan gerakan mouse dengan fungsi show_happy
c.bind('<Motion>', show_happy)

# Fungsi menyembunyikan ekspresi senang saat mouse keluar dari canvas
def hide_happy(event):
    c.itemconfigure(cheek_left, state=HIDDEN)
    c.itemconfigure(cheek_right, state=HIDDEN)
    c.itemconfigure(mouth_happy, state=HIDDEN)
    c.itemconfigure(mouth_normal, state=NORMAL)
    c.itemconfigure(mouth_sad, state=HIDDEN)
    return

# Hubungkan saat mouse meninggalkan canvas dengan fungsi hide_happy
c.bind('<Leave>', hide_happy)

# Awal level bahagia karakter (0 = sedih, 1 = normal/senang)
c.happy_level = 1

# Fungsi membuat karakter sedih jika terlalu lama tidak diajak bermain
def sad():
    if c.happy_level == 0:
        c.itemconfigure(mouth_happy, state=HIDDEN)
        c.itemconfigure(mouth_normal, state=HIDDEN)
        c.itemconfigure(mouth_sad, state=NORMAL)
    else:
        c.happy_level -= 1  # Kurangi level bahagia tiap 4 detik
    root.after(4000, sad)

# Jalankan fungsi sad setelah 1 detik
root.after(1000, sad)

# ========== Aksi Lidah dan Mata Silang ========== #

# Status awal lidah karakter (tidak keluar)
c.tongue_out = False

# Fungsi mengeluarkan atau menyembunyikan lidah
def toggle_tongue():
    if not c.tongue_out:
        c.itemconfigure(tongue_tip, state=NORMAL)
        c.itemconfigure(tongue_main, state=NORMAL)
        c.tongue_out = True
    else:
        c.itemconfigure(tongue_tip, state=HIDDEN)
        c.itemconfigure(tongue_main, state=HIDDEN)
        c.tongue_out = False

# Status awal mata silang
c.eyes_crossed = False

# Fungsi membuat mata menyilang (silang atau kembali normal)
def toggle_pupils():
    if not c.eyes_crossed:
        c.move(pupil_left, 10, -5)
        c.move(pupil_right, -10, -5)
        c.eyes_crossed = True
    else:
        c.move(pupil_left, -10, 5)
        c.move(pupil_right, 10, 5)
        c.eyes_crossed = False

# Fungsi gabungan: menjulurkan lidah, silang mata, lalu kembali normal
def cheeky(event):
    toggle_tongue()
    toggle_pupils()
    hide_happy(event)  # Sembunyikan ekspresi bahagia saat cheeky
    root.after(1000, toggle_tongue)  # Balik normal setelah 1 detik
    root.after(1000, toggle_pupils)
    return

# Klik dua kali mouse untuk memicu ekspresi cheeky
c.bind('<Double-1>', cheeky)

# ========== Jalankan GUI ========== #

root.mainloop()  # Menjalankan jendela GUI
