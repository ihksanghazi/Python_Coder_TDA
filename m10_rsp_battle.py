# Mengimpor modul random untuk membuat pilihan komputer secara acak
import random

# Mengimpor modul datetime untuk mencatat waktu mulai dan selesai bermain
import datetime

# Menampilkan peraturan permainan
print("""Winning Rules of the Rock Paper Scissors game as follows:
1. Rock vs Paper -> Paper wins
2. Rock vs Scissors -> Rock wins
3. Paper vs Scissors -> Scissors wins
""")

# Mencatat waktu mulai permainan
start_time = datetime.datetime.now()
print("Game started at:", start_time)

# Memulai perulangan permainan
while True:
    # Menampilkan pilihan yang bisa dipilih oleh pemain
    print("""Enter choice:
    1. Rock
    2. Scissors
    3. Paper """)

    # Meminta input dari pemain (1, 2, atau 3)
    choice = int(input("Your turn: "))

    # Validasi input (harus antara 1–3)
    while choice > 3 or choice < 1:
        choice = int(input("Enter valid input: "))

    # Mengubah angka menjadi nama pilihan
    if choice == 1:
        choice_name = "Rock"
    elif choice == 2:
        choice_name = "Scissors"
    else:
        choice_name = "Paper"

    # Menampilkan pilihan pemain
    print("Your choice is: " + choice_name)

    # Komputer membuat pilihan secara acak (1 sampai 3)
    print("\nNow it's the computer's turn")
    comp_choice = random.randint(1, 3)

    # Mengubah angka menjadi nama pilihan komputer
    if comp_choice == 1:
        comp_choice_name = "Rock"
    elif comp_choice == 2:
        comp_choice_name = "Scissors"
    else:
        comp_choice_name = "Paper"

    # Menampilkan pilihan komputer
    print("Computer choice is: " + comp_choice_name)

    # Menampilkan pertarungan pilihan
    print("Battle : " + str(choice_name) + " VS " + str(comp_choice_name))

    # Logika menentukan pemenang (jika pilihan tidak sama)
    if comp_choice != choice:
        if (choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice == 1):
            print("Rock wins")
            result = "Rock"
        elif (choice == 1 and comp_choice == 3) or (choice == 3 and comp_choice == 1):
            print("Paper wins")
            result = "Paper"
        else:
            print("Scissors wins")
            result = "Scissors"

        # Menentukan siapa pemenangnya: user atau komputer
        if result == choice_name:
            print("<== User wins ==>")
        else:
            print("<== Computer wins ==>")
    else:
        # Jika pilihan sama, maka seri
        print("<== Tie ==>")

    # Menanyakan apakah ingin bermain lagi
    response = input("\nDo you want to play again? (Y/N): ")
    if response.lower() == "n":
        break  # Keluar dari permainan

# Mencatat waktu selesai permainan
end_time = datetime.datetime.now()

# Menghitung lama waktu bermain
duration = end_time - start_time

# Menampilkan ucapan terima kasih dan waktu bermain
print("\nThanks for playing!")
print("Game started at:", start_time)
print("Game ended at:", end_time)
print("Duration:", duration)