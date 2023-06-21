angka = int(input('Masukan angka: '))
def bilangan (nilai):
    if nilai % 2 == 0:
        print(nilai, 'merupakan bilangan Genap')
    else:
        print(nilai, 'merupakan bilangan ganjil')

bilangan(angka)