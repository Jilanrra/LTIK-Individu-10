"""
Jilan Rokan Ragheb Arwa
2507439
Kelas 1A RPL
"""


def border():
    print("x------------------------------------------x") #agar tidak mengetik print berulang

def login():
    username = "Daspro2023"
    password = "Latihan"
    border()
    print("Selamat datang di Menu Login!\nSilakan Login dengan benar :D")
    border()
    n = 3
    while n > 0 :
        pwInput = input("Masukkan password anda: ")
        if pwInput == password: #memvalidasi passwoerd
            border()
            print("Login berhasil!")
            print(f"Selamat datang, {username}!")
            border()
            break #keluar dari loop 
        else:
            n -= 1
            print(f"Password salah! Kesempatan login tersisa: {n} kali.")
            border()
            if n <= 0:
                print("Anda telah gagal login 3 kali!")
                print("Akses ditolak.")
                border()
            #karena n sudah habis atau sudah kurang dari sama dengan nol maka sistem berhenti :(

login()