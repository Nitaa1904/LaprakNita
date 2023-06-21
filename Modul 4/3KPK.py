# Meminta input dua bilangan dari pengguna
bilangan1 = int(input("Masukkan bilangan pertama: "))
bilangan2 = int(input("Masukkan bilangan kedua: "))

# Menentukan bilangan dengan nilai lebih besar
if bilangan1 > bilangan2:
    maksimum = bilangan1
else:
    maksimum = bilangan2

# Perulangan untuk mencari KPK
while(True):
    if (maksimum % bilangan1 == 0) and (maksimum % bilangan2 == 0):
        kpk = maksimum
        break
    maksimum += 1

# Menampilkan output KPK
print("KPK dari", bilangan1, "dan", bilangan2, "adalah", kpk)
