# Meminta input bilangan dan pangkat dari pengguna
bilangan = int(input("Masukkan bilangan: "))
pangkat = int(input("Masukkan pangkat: "))

# Inisialisasi variabel hasil dengan nilai 1
hasil = 1

# Perulangan untuk menghitung hasil pangkat
for i in range(pangkat):
    hasil *= bilangan

# Menampilkan output hasil pangkat
print(bilangan, "pangkat", pangkat, "adalah", hasil)
