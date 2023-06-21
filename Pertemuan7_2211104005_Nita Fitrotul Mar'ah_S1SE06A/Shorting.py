import timeit
print('Ascending')
print('')
#insertion sort
def insertion_sort (array):
    start = timeit.default_timer()
    for i in range(1, len(array)):
        item = array [1]
        j = i - 1
        while j >= 0 and array[j] > item:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = item

    stop = timeit.default_timer()
    print(f"insertion sort successfull Elapsed time: + {stop - start}")
    return array
list_1 = [45, 7, 9, 32, 41, 33, 51, 9, 24, 66]
print(f"Before: {list_1}")
insertion_sort(list_1)
print(f"After: {list_1}")


import timeit
print('Ascending')
print('')
#insertion sort
def insertion_sort (array):
    start = timeit.default_timer()
    for i in range(1, len(array)):
        item = array [1]
        j = i - 1
        while j >= 0 and array[j] < item:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = item

    stop = timeit.default_timer()
    print(f"insertion sort successfull Elapsed time: + {stop - start}")
    return array
list_1 = [45, 7, 9, 32, 41, 33, 51, 9, 24, 66]
print(f"Before: {list_1}")
insertion_sort(list_1)
print(f"After: {list_1}")


import timeit
print('Ascending')
print('')
def bubble_sort(array):
    start = timeit.default_timer()
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array [j]

    stop = timeit.default_timer()
    print(f"Bubble sort successfull Elapsed time: + {stop - start}")
    return array

list_1 = [45, 7, 9, 32, 41, 33, 51, 9, 24, 66]
print(f"Before: {list_1}")
bubble_sort(list_1)
print(f"After: {list_1}")

import timeit
print('Ascending')
print('')
def bubble_sort(array):
    start = timeit.default_timer()
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] < array[j+1]:
                array[j], array[j+1] = array[j+1], array [j]

    stop = timeit.default_timer()
    print(f"Bubble sort successfull Elapsed time: + {stop - start}")
    return array

list_1 = [45, 7, 9, 32, 41, 33, 51, 9, 24, 66]
print(f"Before: {list_1}")
bubble_sort(list_1)
print(f"After: {list_1}")


import timeit
print('Ascending')
print('')
def selection_sort(array):
    start = timeit.default_timer()
    for i in range(len(array)):
        min_index = i
        for j in range(i+1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]

    stop = timeit.default_timer()
    print(f"Selection sort successfull Elapsed time: + {stop - start}")
    return array

list_1 = [45, 7, 9, 32, 41, 33, 51, 9, 24, 66]
print(f"Before: {list_1}")
selection_sort(list_1)
print(f"After: {list_1}")

import timeit
print('Ascending')
print('')
def selection_sort(array):
    start = timeit.default_timer()
    for i in range(len(array)):
        min_index = i
        for j in range(i+1, len(array)):
            if array[min_index] < array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]

    stop = timeit.default_timer()
    print(f"Selection sort successfull Elapsed time: + {stop - start}")
    return array

list_1 = [45, 7, 9, 32, 41, 33, 51, 9, 24, 66]
print(f"Before: {list_1}")
selection_sort(list_1)
print(f"After: {list_1}")