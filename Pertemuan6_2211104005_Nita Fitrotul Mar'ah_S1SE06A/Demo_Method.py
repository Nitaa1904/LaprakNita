#Functions
def hitung_luas_persegi(sisi):
    hasil = sisi * sisi
    return hasil
print('Luas Persegi: %d' % hitung_luas_persegi(10))

#Prosedure
def hitung_luas_persegi(sisi):
    print(f'Luas Persegi: {sisi * sisi}')
hitung_luas_persegi(10)

#Parameter
def salam(ucapan):
    print(ucapan)
salam('Hallo, selamat pagi')


def hitung_luas_segitiga(alas, tinggi):
    hasil = (alas * tinggi) / 2
    print('Luaas Segitiga: %d' % hasil)
hitung_luas_segitiga(10, 5)
