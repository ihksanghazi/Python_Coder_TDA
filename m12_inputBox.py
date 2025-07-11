# Mengimpor komponen dari Tkinter:
# Tk -> jendela utama
# Entry -> kotak isian
# Label -> teks tampilan
# Button -> tombol
from tkinter import Tk, Entry, Label, Button

# Membuat jendela utama aplikasi
root = Tk()

# Memberi judul pada jendela
root.title("Tkinter Example")

# Mengatur ukuran jendela menjadi 400x100 piksel
root.geometry("400x100")

# Membuat label (teks) yang muncul di jendela
label = Label(root, text="Enter Your Name:")
label.pack()  # Menempatkan label ke dalam jendela (otomatis diatur)

# Membuat kotak isian (untuk menulis nama)
entry = Entry(root)
entry.pack()  # Menampilkan kotak isian

# Membuat tombol bertuliskan "Greet Me"
button = Button(root, text="Greet Me")
button.pack()  # Menampilkan tombol

# Menjalankan aplikasi GUI (jendela tetap terbuka)
root.mainloop()
