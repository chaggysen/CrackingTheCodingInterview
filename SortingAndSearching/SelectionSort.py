# never use selection sort its trash
def selectionSort(array):
    for i in range(len(array)):
        min = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min]:
                min = j
        array[i], array[min] = array[min], array[i]


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selectionSort(alist)
print(alist)
