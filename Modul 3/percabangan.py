# #Membuat variabel dengan nilai (if satu kondisi)
# nilai = int(input("Masukan Bilangan Bulat :"))
# if (nilai > 0) :
#     print("Bilangan", nilai, "merupakan bilangan positif")
# else : #kondisi menggunakan else
#     print("Bilangan", nilai, "merupakan bilangan negatif")
    


# #IF 3 kondisi atau lebih
# nilai = int(input("Masukan Bilangan Bulat :"))
# if (nilai > 0) :
#     print("Bilangan", nilai, "merupakan bilangan positif")
# elif (nilai < 0):
#     print("Bilangan", nilai, "merupakan bilangan negatif")
# else :
#     print("Bilangan nol")
    
    
    
# #huruf vokal konsonan
# user = input("Masukkan sebuah huruf: ")
# if user.isalpha():
#     if user.lower() in ['a', 'i', 'u', 'e', 'o']:
#         print("Huruf vokal")
#     else:
#         print("Huruf konsonan")
# else:
#     print("Inputan bukan huruf")
    
    
    
# #validasi nilai
# nilai = int(input("Masukkan nilai: "))
# nilai_pembagi = int(input("masukkan pembagi: "))
# if (nilai_pembagi == 0):
#     print("Pembagi tidak boleh 0")
# else:
#     print(nilai/nilai_pembagi)



# #Tahun kabisat
# tahun = int(input("Input tahun: "))
# if (tahun % 4) == 0:
#     if (tahun % 100) == 0:
#         if (tahun % 400) == 0:
#             print ("Tahun Kabisat")
#         else:
#             print ("Bukan Tahun Kabisat")
#     else:
#         print ("Tahun Kabisat")
        
        
# suhu = int(input("Masukan Besarnya suhu: "))
    
# if(suhu<=0):
#     print("Pada suhu ", suhu ," derajat celcius, air akan berwujud es")
# elif(suhu > 0 & suhu < 100):
#     print("Pada suhu ", suhu ," derajat celcius, air akan berwujud air")
# else:
#     print("Pada suhu ", suhu ," derajat celcius, air akan berwujud gas")

# #Panggilan berdasarkan status
# gender = input("Perempuan atau Laku-laki ? (L/P): ")

# if(gender == 'L'):
#     status = input("Anda sudah menikah atau belum? (Y/N): ")
#     if(status == 'Y'):
#         print("Hallo Bapak")
#     elif(status == 'N'):
#         print("Hallo Mas")
#     else:
#         print("Tidak ada dalam pilihan")
# elif(gender == "P"):
#     status = input("Anda sudah meningkah atau belum? (Y/N): ")
#     if(status == 'Y'):
#         print("Hallo ibu")
#     elif(status == 'N'):
#         print("Hallo Mbak")
#     else:
#         print("Tidak ada dalam pilihan")
# else:
#     print("Tidak ada dalam pilihan")
    
    