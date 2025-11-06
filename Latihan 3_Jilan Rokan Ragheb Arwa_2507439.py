"""
Jilan Rokan Ragheb Arwa
2507439
Kelas 1A RPL
"""

def selisih(a, b):
    selisih = a - b
    return selisih
    
def border():
    print("x------------------------------------------x") #agar tidak mengetik print secara berulang
    
def KalkulatorSelisih():
    border()
    print("Selamat datang di Kalkulator Selisih Waktu!")
    print("Silakan masukkan waktu mulai dan waktu selesai:")
    border()
    jamMulai = int(input("Masukkan jam mulai: "))
    menitMulai = int(input("Masukkan menit mulai: "))
    detikMulai = int(input("Masukkan detik mulai: "))
    border()
    jamSelesai = int(input("Masukkan jam selesai: "))
    menitSelesai = int(input("Masukkan menit selesai: "))
    detikSelesai = int(input("Masukkan detik selesai: "))
    border()

    detik = selisih(detikSelesai, detikMulai) #menyatakan variabel dengan fungsi selisih yang argumennya diganti dengan inputan 
    if detik < 0: #jika hasil negatif, maka
        detik += 60 #detik ditamvah 60
        menitMulai += 1 #dan menit mulai ditambah 1 (berkurang 1 menit)
    menit = selisih(menitSelesai, menitMulai)
    if menit < 0:
        menit += 60
        jamMulai += 1
    jam = selisih(jamSelesai, jamMulai)
    if jam < 0:
        print("Inputan jam selesai tidak valid!")
    print(f"Selisihnya adalah: {jam} jam - {menit} menit - {detik} detik") 

KalkulatorSelisih()

