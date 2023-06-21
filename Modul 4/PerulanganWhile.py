
# i = 0
# while i <= 7:
#     print("HELLO WORD!")
#     i += 1

# #perulangan increment
# a = 1
# b = 10
# while a < b:
#     print("Step ke-", a)
#     a += 1

# #Perulangan decretment
# a = 10
# b = 0
# while a > b:
#     print("Kouta Internet anda sisa", a, "GB")
#     a -= 1


# #break pada while
# a = 0
# while True:
#     print("Step ke-", a, "!")
#     a += 1
#     if a == 7:
#         print("step ke-", a, "dihentikan!")
#         break
    
    
#Countinue pada while
angka = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
#skip jika i adalah bilangan genap
#dan i lebih dari 0
i = -1
while i < len(angka):
    i += 1
    if i % 2 == 0 and i > 0:
        print('skip')
        continue
    #tidak dieksekusi ketika continue dipanggil
    print(angka[i])