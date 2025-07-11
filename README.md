# 👾 Perteuan 10: Password & Game Batu Gunting Kertas!

Hai teman-teman! Kali ini kita akan belajar dua hal keren dengan Python:

1. 🔐 Membuat **Password Otomatis**
2. ✊✌️🖐 Bermain **Batu Gunting Kertas** melawan komputer!

Yuk mulai!

---

## 🔐 Proyek 1: Pembuat Password Otomatis

### Apa yang dilakukan program ini?

Program ini akan membuat password unik yang terdiri dari:

- Kata sifat (contoh: `happy`)
- Kata benda (contoh: `panda`)
- Angka acak (contoh: `42`)
- Simbol spesial (contoh: `!`)

Contoh hasilnya:  
`happyPanda42!`

### Kode Sederhana:

```python
import random
import string

print("Welcome to password maker!")

# Daftar kata sifat dan kata benda
adjectives = ["happy", "sad", "brave", "calm", "red"]
nouns = ["cat", "book", "flower", "panda", "apple"]

# Fungsi pembuat password
def password_maker():
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    number = random.randint(0, 100)
    symbol = random.choice(string.punctuation)
    password = adjective + noun + str(number) + symbol
    print("Your new password is:", password)

# Perulangan agar bisa membuat password terus-menerus
while True:
    password_maker()
    lagi = input("Mau buat password lagi? (y/n): ")
    if lagi.lower() == "n":
        break
```

---

## ✊✌️🖐 Proyek 2: Batu-Gunting-Kertas (Melawan Komputer!)

### Apa yang dilakukan program ini?

Kita akan bermain **Batu Gunting Kertas** melawan komputer! Komputer akan memilih secara acak, dan kita harus pilih juga!

### Aturan Main:

- Batu VS Gunting → Menang: **Batu**
- Gunting VS Kertas → Menang: **Gunting**
- Kertas VS Batu → Menang: **Kertas**
- Kalau pilihan sama → **Seri**

### Kode Sederhana:

```python
import random

print("Let's play Rock Paper Scissors!")

while True:
    print("1. Rock")
    print("2. Scissors")
    print("3. Paper")

    # Pemain memilih
    player = int(input("Your choice (1/2/3): "))

    # Komputer memilih secara acak
    computer = random.randint(1, 3)

    choices = ["Rock", "Scissors", "Paper"]
    print("You chose:", choices[player - 1])
    print("Computer chose:", choices[computer - 1])

    # Menentukan hasil pertandingan
    if player == computer:
        print("It's a tie!")
    elif (player == 1 and computer == 2) or \
         (player == 2 and computer == 3) or \
         (player == 3 and computer == 1):
        print("You win!")
    else:
        print("Computer wins!")

    # Tanya lagi
    again = input("Play again? (y/n): ")
    if again.lower() == "n":
        break
```
