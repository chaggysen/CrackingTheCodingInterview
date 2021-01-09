def binarySearch(array, item):
    start = 0
    end = len(array) - 1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == item:
            return True
        elif array[mid] < item:
            start = mid + 1
        else:
            end = mid - 1
    return False


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
result = binarySearch(alist, 27)
print(result)
