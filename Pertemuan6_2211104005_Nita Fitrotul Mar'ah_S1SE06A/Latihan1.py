#Menggunakan Prosedur
panjang = int(input("masukkan sisi : "))

def hitung_keliling_persegi(sisi):
    keliling = 4 * sisi
    luas = sisi*sisi
    print('Keliling persegi panjang: %d' % keliling)
    print('Luaas Persegi Panjang: %d' % luas)

hitung_keliling_persegi(panjang)


#Menggunakan Function
panjang = int(input('Masukan sisi: '))

def hitung_keliling_persegi(sisi):
    return 4 * sisi

def hitung_luas_persegi(sisi):
    return sisi * sisi

print('Keliling persegi panjang : ', hitung_keliling_persegi(panjang))
print('Luas Persegi Pnajang :', hitung_luas_persegi(panjang))
