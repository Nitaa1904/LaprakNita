print("======SISTEM LOG IN SEDERHANA======")

login = 0
while True:
    username = input("Masukan usename: ")
    password = input("Masukan password: ")

    if login == 3:
        print("Login gagal! Kesempatan mencoba sudah habis, Silahkan coba lagi nanti!")
        break

    if username == "NitaFitrotul" and password == "nita1904":
        print("Selamat datang", username, "!")
        break
    else:
        print("Coba cek kembali, username atau password salah!")
        login += 1