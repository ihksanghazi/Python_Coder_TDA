# Mengimpor pustaka Tkinter dan beberapa fitur tambahan
from tkinter import Tk, messagebox, font, Label, Entry, Button

# Menampilkan teks di terminal (bukan di GUI)
print('Ask the Expert - Capital Cities of the World')

# Membuat jendela Tkinter tapi langsung disembunyikan
root = Tk()
root.withdraw()  # Tidak perlu jendela utama karena kita pakai jendela dialog custom

# Dictionary kosong untuk menyimpan pasangan negara-ibu kota
the_world = {}

# Fungsi untuk membaca data negara dan ibu kota dari file
def read_from_file():
    with open('m12_capital_data.txt') as file:  # Membuka file data
        for line in file:  # Membaca setiap baris
            line = line.rstrip('\n')  # Menghapus karakter newline
            country, city = line.split('/')  # Memisahkan berdasarkan tanda /
            the_world[country] = city  # Menyimpan ke dictionary

# Membaca data saat program pertama dijalankan
read_from_file()
print(the_world)  # Menampilkan isi dictionary ke terminal (untuk pengecekan)

# Fungsi untuk menulis data negara dan ibu kota baru ke file
def write_to_file(country_name, city_name):
    with open('m12_capital_data.txt', 'a') as file:
        file.write('\n' + country_name + '/' + city_name)  # Tambahkan data ke baris baru

# Fungsi untuk membuat jendela input custom
def custom_askstring(title, prompt, dialog_size="450x150", bg_color="lightblue", font_size=12, font_weight="bold"):
    dialog = Tk()  # Membuat jendela dialog baru
    dialog.title(title)  # Judul dialog
    dialog.configure(bg=bg_color)  # Warna latar belakang

    custom_font = font.Font(size=font_size, weight=font_weight)  # Font kustom

    # Label untuk pertanyaan
    label = Label(dialog, text=prompt, bg=bg_color)
    label.configure(font=custom_font)
    label.pack()

    # Entry untuk mengetik jawaban
    entry = Entry(dialog, font=custom_font)
    entry.pack()

    # Fungsi untuk tombol OK
    def ok():
        dialog.result = entry.get()  # Ambil teks yang diketik
        dialog.destroy()  # Tutup jendela

    # Tombol OK
    button = Button(dialog, text="OK", command=ok, bg=bg_color, font=custom_font)
    button.pack()

    # Ukuran jendela dialog
    dialog.geometry(dialog_size)
    dialog.eval('tk::PlaceWindow . center')  # Letakkan dialog di tengah layar

    entry.focus_set()  # Fokus langsung ke kolom input
    dialog.wait_window()  # Tunggu sampai jendela ditutup

    try:
        return dialog.result  # Kembalikan hasil input
    except AttributeError:
        return ""  # Jika kosong, kembalikan string kosong

# Mulai perulangan utama program
while True:
    # Tampilkan dialog untuk mengetik nama negara
    query_country_input = custom_askstring(
        'Country',
        'Type the name of a country:',
        dialog_size="450x150",
        bg_color="lightgreen",
        font_size=14,
        font_weight="bold"
    )

    # Jika user mengetik sesuatu (tidak kosong)
    if query_country_input:
        query_country = query_country_input.capitalize()  # Huruf pertama kapital (standar nama negara)

        # Jika negara ada dalam data
        if query_country in the_world:
            result = the_world[query_country]  # Ambil ibu kota
            # Tampilkan info ibu kota
            messagebox.showinfo('Answer', 'The capital city of ' + query_country + ' is ' + result + '!')
        else:
            # Jika negara tidak dikenal, minta user mengajarkan
            new_city = custom_askstring(
                'Teach me',
                f"I don't know! What is the capital city of {query_country}?",
                dialog_size="450x150",
                bg_color="lightblue",
                font_size=12,
                font_weight="bold"
            )
            the_world[query_country] = new_city  # Simpan di memori
            write_to_file(query_country, new_city)  # Simpan ke file
    else:
        break  # Jika input kosong, keluar dari loop
