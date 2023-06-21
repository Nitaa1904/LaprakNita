array = []

y = int(input('\nMasukkan Jumlah Mata Kuliah : ')) 
print()

for i in range(y):
    nilai = float(input('Masukkan nilai mata kuliah ke-{} : '.format(i + 1)))
    #format = untuk melakukan pengaturan format string
    array.append(nilai)
    #append menambahkan data baru diakhir list
mean = sum(array)/y
#sum = menjumlahkan seluruh anggota list array
print()
if mean < 100  and mean  >= 90 :
    print('Hasil Predikat A dengan nilai : ')
    for x in range(y):
        print('Mata kuliah ke-{}' .format(x), ' : ', (array[x]))
elif mean < 90 and mean >= 70 :
    print('Hasil Predikat B dengan nilai : ')
    for x in range(y):
        print('Mata kuliah ke-{}' .format(x), ' : ', (array[x]))
elif mean < 70 and mean >= 50 :
    print('Hasil Predikat C dengan nilai : ')
    for x in range(y):
        print('Mata kuliah ke-{}' .format(x), ' : ', (array[x]))
elif mean < 50 and mean >= 30 :
    print('Hasil Predikat D dengan nilai : ')
    for x in range(y):
        print('Mata kuliah ke-{}' .format(x), ' : ', (array[x]))
elif mean < 30 and mean >= 0 :
    print('Hasil Predikat E dengan nilai : ')
    for x in range(y):
        print('Mata kuliah ke-{}' .format(x), ' : ', (array[x]))
else:
    print('Nilai tidak valid !')