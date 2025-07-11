# Mengimpor Tk dan Canvas dari tkinter untuk membuat GUI
from tkinter import Tk, Canvas

# Mengimpor datetime untuk bekerja dengan waktu dan tanggal
from datetime import datetime

# Fungsi untuk memperbarui jam dan tanggal setiap detik
def update_clock():
    now = datetime.now()  # Ambil waktu saat ini
    current_time = now.strftime('%H:%M:%S')  # Format jam: jam:menit:detik
    current_date = now.strftime('%d/%m/%Y')  # Format tanggal: hari/bulan/tahun
    # Update teks jam dan tanggal di canvas
    c.itemconfig(clock_text, text=f"Date: {current_date}\nTime: {current_time}")
    root.after(1000, update_clock)  # Jalankan lagi fungsi ini setelah 1 detik (1000 ms)

# Fungsi untuk mengambil daftar event dari file
def get_events():
    list_events = []  # List kosong untuk menyimpan semua event
    with open('m11_events.txt') as file:  # Buka file event
        for line in file:  # Baca setiap baris dalam file
            line = line.rstrip('\n')  # Hapus karakter newline di akhir baris
            current_event = line.split(',')  # Pisahkan nama event dan tanggalnya
            # Ubah string tanggal menjadi objek tanggal
            event_date = datetime.strptime(current_event[1], '%d/%m/%y').date()
            current_event[1] = event_date
            list_events.append(current_event)  # Tambahkan ke list
    return list_events  # Kembalikan daftar event

# Fungsi untuk menghitung jumlah hari antara dua tanggal
def days_between_dates(date1, date2):
    time_between = str(date1 - date2)  # Hitung selisih waktu
    number_of_days = time_between.split(' ')  # Ambil bagian hari saja
    return number_of_days[0]

# Membuat jendela utama
root = Tk()
root.title("Countdown Calendar")

# Membuat canvas tempat semua teks ditampilkan
c = Canvas(root, width=800, height=500, bg="green")
c.pack()

# Judul kalender
c.create_text(
    100, 50, anchor='w',
    fill='orange', font='Arial 28 bold underline',
    text='My Countdown Calendar'
)

# Mengambil event dari file
events = get_events()

# Ambil tanggal hari ini
today = datetime.now().date()

# Jarak vertikal antar baris teks event
vertical_space = 100

# Urutkan event berdasarkan tanggalnya
events.sort(key=lambda x: x[1])

# Menampilkan setiap event ke canvas
for event in events:
    event_name = event[0]  # Nama event
    days_until = days_between_dates(event[1], today)  # Hitung sisa hari
    display = f"It is {days_until} days until {event_name}"  # Teks ditampilkan

    # Warna teks tergantung seberapa dekat tanggalnya
    if int(days_until) <= 7:
        text_col = 'red'  # Jika kurang dari 7 hari, tampilkan warna merah
    else:
        text_col = 'lightblue'  # Jika masih lama, warna biru muda

    # Tampilkan teks event ke canvas
    c.create_text(
        100, vertical_space,
        anchor='w', fill=text_col,
        font='Arial 28 bold',
        text=display
    )

    # Turunkan posisi vertikal untuk teks selanjutnya
    vertical_space += 30

# Tambahkan placeholder teks jam di pojok kanan bawah canvas
clock_text = c.create_text(
    750, 400, anchor='e',
    fill='white', font='Arial 18 bold'
)

# Mulai pembaruan jam pertama kali
update_clock()

# Jalankan GUI
root.mainloop()