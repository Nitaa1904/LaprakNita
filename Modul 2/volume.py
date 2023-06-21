print("Program Menghitung Volume Balok")
panjang = int(input("Masukan Panjang Balok: "))
lebar = int(input("Masukan Lebar Balok: "))
tinggi = int(input("Masukan Tinggi Balok: "))
volume = panjang * lebar * tinggi
print("Volume:", volume)

print("Tabung")
jari_jari = int(input("Masukkan jari-jari tabung: "))
tinggi = int(input("Masukkan tinggi tabung: "))
pi = 3.14 
volume = pi * jari_jari ** 2 * tinggi
print("Volume tabung adalah:", volume)