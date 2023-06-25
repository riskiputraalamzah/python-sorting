import library


# # case 1
# unordered = [92, 31, 46]
# print("Algoritma Bubble Sort")
# # ascending
# print(library.bubble_sort(unordered))
# # descending
# print(library.bubble_sort(unordered, desc=True))
# print()

# # case 2
# unordered = [92, 31, 46]
# print("Algoritma Selection Sort")
# # ascending
# print(library.selection_sort(unordered))
# # descending
# print(library.selection_sort(unordered, desc=True))
# print()

# case 3

# loop = True
# while loop:
#     unordered = library.insert_arr(unordered)
#     print(unordered)
#     loop = True if input("Tambah Lagi (y/n) : ") == "y" else False

# # case 4
# print()

# # case 4.1
# B = [15, 12, 20, 50, 100]
# condition = True if B[0] > B[-1] else False
# B = library.selection_sort(B, desc=condition)
# print(B)

# # case 4.2
# library.change_value(B, 0, 1000)
# print(B)

def selection_sort(arr, desc=False):
    n = len(arr)
    # perulangan list elemen
    for i in range(n):
        # cari nilai elemen terendah
        # yang masih tersedia
        min_idx = i
        for j in range(i+1, n):
            if desc:
                if arr[min_idx] < arr[j]:
                    min_idx = j
            else:
                if arr[min_idx] > arr[j]:
                    min_idx = j
        # tukar dengan nilai elemen ke-i
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


unordered = []
maxValue = 5
print('Masukkan Nilai Angka random maximal {} buah'.format(maxValue))
try:
    for i in range(maxValue):
        number = int(input('> '))
        unordered.append(number)
except:
    print('Error Woi : Inputan harus berupa angka')
    exit(0)

sort = input("Pilih metode pengurutan(asc/desc) : ")
if (sort not in ['asc', 'desc']):
    print('Metode pengurutan tidak tersedia')
    exit()
desc = True if sort == 'desc' else False

print("Berikut nilai sebelum di urutkan {}".format(unordered))
print("dan berikut nilai setelah di urutkan menggunakan metode {} {}".format(
    sort, selection_sort(unordered, desc)))
