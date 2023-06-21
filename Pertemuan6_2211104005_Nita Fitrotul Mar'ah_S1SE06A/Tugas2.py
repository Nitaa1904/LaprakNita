def luas_lingkaran(jari):
    return phi * jari * jari

def keliling_lingkaran(jari):
    return 2 * phi * jari

phi = 3.14
panjang = int(input('Masukan jari-jarinya: '))
print('Luas Lingkaran: ', luas_lingkaran(panjang))
print('Keliling Lingkara: ', keliling_lingkaran(panjang))


# def keliling_luas_lingkaran(jari):
#     luas = phi * jari * jari
#     keliling = 2 * phi * jari
#     print('Keliling Lingkaran: %f' %keliling)
#     print('Luas Lingkaran: %f' %luas)
# phi = 3.14
# panjang = int(input('Masukan jari-jarinya: '))
# keliling_luas_lingkaran(panjang)