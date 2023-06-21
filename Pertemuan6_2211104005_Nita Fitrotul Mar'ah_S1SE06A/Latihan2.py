def perbandingan_bilangan(a, b):
    if a > b:
        print(f"{a} lebih besar dari {b}")
    elif a < b:
        print(f"{a} lebih kecil dari {b}")
    else:
        print("Bilangan a dan b sama besar")


bilangan_a = int(input('Masukan bilangan a : '))
bilangan_b = int(input('Masukan bilangan b : '))
perbandingan_bilangan(bilangan_a, bilangan_b)