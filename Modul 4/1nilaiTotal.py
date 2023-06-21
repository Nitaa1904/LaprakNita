total = 0  # inisialisasi variabel total dengan nilai 0

# Meminta input bilangan dari pengguna
n = int(input("Masukkan bilangan: "))

# Perulangan untuk menjumlahkan bilangan dari 1 hingga n
for i in range(1, n+1):
    total += i

# Menampilkan output total nilai bilangan
print("Total nilai dari bilangan 1 hingga", n, "adalah", total)