# Mengimpor module random untuk memilih item secara acak
import random

# Mengimpor module string untuk mendapatkan karakter-karakter khusus (seperti !, @, #, dll)
import string

# Menampilkan pesan pembuka
print("Welcome to password maker !")

# List berisi kata sifat (adjective) yang akan digunakan dalam password
adjectives = [
    "sleepy", "slow", "red", "orange", "yellow",
    "green", "blue", "purple", "fluffy", "white", 
    "happy", "sad", "brave", "beautiful", "calm", "kind"
]

# List berisi kata benda (noun) yang akan digunakan dalam password
nouns = [
    "Apple", "Dinosaur", "Ball", "Toaster", 
    "goat", "dragon", "hammer", "duck", 
    "panda", "cat", "car", "book", 
    "tree", "chair", "apple", "flower"
]

# Fungsi untuk membuat password secara acak
def password_maker():
    # Memilih satu kata sifat secara acak dari list adjectives
    adjective = random.choice(adjectives)

    # Memilih satu kata benda secara acak dari list nouns
    noun = random.choice(nouns)

    # Membuat angka acak dari 0 sampai 100
    number = random.randint(0, 100)

    # Memilih satu karakter spesial secara acak, seperti ! @ # dll
    special_char = random.choice(string.punctuation)

    # Menggabungkan semua bagian menjadi password: kata sifat + kata benda + angka + simbol
    password = adjective + noun + str(number) + special_char

    # Menampilkan password baru ke pengguna
    print("Your new password is : " + password)

# Perulangan agar program terus menanyakan apakah ingin membuat password lagi
while True:
    password_maker()  # Panggil fungsi untuk buat password

    # Menanyakan kepada pengguna apakah ingin password baru lagi
    response = input("Would you like another password Type y or n : ")

    # Jika pengguna menjawab "n", maka keluar dari perulangan (berhenti)
    if response == "n":
        break

    # Jika jawabannya bukan "y" atau "n", maka tampilkan pesan bingung lalu berhenti
    elif response != "y" and "n":
        print("What do you mean ?")
        break
