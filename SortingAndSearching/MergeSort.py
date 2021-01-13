# its good because its O(nlog(n)). But it uses space complexity O(n). So if we don<t care too much about our space complexity,
# we can use merge sort. Its also a stable algorithm
def merge(a, b):
    output = []
    a_idx, b_idx = 0, 0
    while a_idx < len(a) and b_idx < len(b):
        if a[a_idx] < b[b_idx]:
            output.append(a[a_idx])
            a_idx += 1
        else:
            output.append(b[b_idx])
            b_idx += 1
    if a_idx == len(a):
        output.extend(b[b_idx:])
    else:
        output.extend(a[a_idx:])
    return output


def mergeSort(array):
    # a list of zero or one element is sorted by definition
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    left = mergeSort(left)
    right = mergeSort(right)
    return merge(left, right)


alist = [1, 2]
newlist = mergeSort(alist)
print(alist)
