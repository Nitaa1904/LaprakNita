
def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array [j]

    return array

ips_mahasiswa = [3.8, 2.9, 3.3, 4.0, 2.7]
print(f'Indeks Prestasi Semester (IPS)')
print(f"Before: {ips_mahasiswa}")
bubble_sort(ips_mahasiswa)
print(f"After: {ips_mahasiswa}")
