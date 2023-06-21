menu_item = 0
angka = []
while menu_item != 5:
    print("---------------------------")
    print("        KALKULATOR         ")
    print("---------------------------")
    print("1. Penjumlahan")
    print("2. Perkalian")
    print("3. Pembagian")
    print("4. Pengurangan")
    print("5. Pangkat")
    menu_item = int(input("Pilih Menu: "))
    def operasi (angka1, angka2):
        angka = angka1, angka2
    nilai1 = int(input('Masukan angka pertamanya: '))
    nilai2 = int(input('Masukan angka keduanya: '))
    operasi(nilai1, nilai2)
    if menu_item == 1:
        print(f'Jumlahnya adalah: {nilai1 + nilai2}')
    elif menu_item == 2:
        print(f'Jumlahnya adalah: {nilai1 * nilai2}')
    elif menu_item == 3:
        print(f'Jumlahnya adalah: {nilai1 / nilai2}')
    elif menu_item == 4:
        print(f'Jumlahnya adalah: {nilai1 - nilai2}')
    elif menu_item == 5:
        print(f'Jumlahnya adalah: {nilai1 ** nilai2}')
    else:
        print('Menu Tidak ada')

print("terimakasih Selamat tinggal")
