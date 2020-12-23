def isMonotonic(array):
    array_len = len(array)
    increased = False
    decreased = False
    curr = 0
    while curr < array_len - 1:
        next = curr + 1
        if array[next] > array[curr]:
            increased = True
        elif array[next] < array[curr]:
            decreased = True
        curr += 1
    return not (increased and decreased)
