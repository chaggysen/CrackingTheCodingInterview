# O(nlog(n)). This is the most popular sorting algorithm.One downside is that if we don't
# pick the pivot correctly, the worst case could be O(n^2). Also this sorting algorithm is not stable
def quickSort(array):
    if len(array) <= 1:
        return array
    pivot = array.pop()
    greater = []
    lower = []
    for item in array:
        if item > pivot:
            greater.append(item)
        else:
            lower.append(item)
    return quickSort(lower) + [pivot] + quickSort(greater)


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
newlist = quickSort(alist)
print(newlist)
