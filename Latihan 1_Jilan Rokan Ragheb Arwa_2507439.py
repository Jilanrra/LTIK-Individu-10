"""
Jilan Rokan Ragheb Arwa
2507439
Kelas 1A RPL
"""

#NOMOR 1
def fibonacci(n):
    deret = [0, 1]
    for i in range(2, n):
        deret.append(deret[-1] + deret[-2]) #menambah bilangan index terakhir dan kedua terakhir, dan ditambahkan ke list deret
    return deret

print(fibonacci(9))


#NOMOR 2
def volumeTabung(r, t):
    hasilVolume = 3.14 * r * r * t
    print(f"Volume tabung adalah: {hasilVolume}cm³")
    return hasilVolume

r = int(input("Masukkan jari-jari tabung: "))
t = int(input("Masukkan tinggi tabung: "))

volumeTabung(r, t)


#NOMOR 3
nilai = []
def nilaiTotal():
    total = sum(nilai)
    average = total/len(nilai)
    print(f"Input: {nilai}")
    print(f"Nilai total adalah: {total}")
    print(f"Rata-rata nilai: {average}")

n = 1
while n > 0:
    angka = input(f"Masukkan angka ke-{n} (Tekan enter untuk berhenti): ") #ini kalo inputnya vertikal, satu per satu
    if angka == "": #saat user menekan enter, maka inputan dinyatakan kosong dan program berhenti
        break
    nilai.append(int(angka))
    n += 1
nilaiTotal()


#Alternatif :)
def nilaiTotal(nilai):
    total = sum(nilai)
    average = total/len(nilai)
    print(f"Input: {nilai}")
    print(f"Nilai total adalah: {total}")
    print(f"Rata-rata nilai: {average}")

input_nilai = input("Masukkan nilai (piasahkan dengan spasi): ") #nasih bertipe data string
nilai = [int(i) for i in input_nilai.split()] #ubah i ke integer untuk setiap i pada variabel input_nilai yang dipisah dengan spasi, dan dimasukkan ke list

nilaiTotal(nilai)
