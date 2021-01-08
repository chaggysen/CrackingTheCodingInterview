# Use insertion sort when we have small data set or when most of the elements
# already sorted. It uses O(1) spacew and its easy to implement. It's a stable sorting algorithm
def insertionSort(array):
    for i in range(1, len(array)):
        while array[i - 1] > array[i] and i > 0:
            array[i], array[i - 1] = array[i - 1], array[i]
            i -= 1


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(alist)
insertionSort(alist)
print(alist)
