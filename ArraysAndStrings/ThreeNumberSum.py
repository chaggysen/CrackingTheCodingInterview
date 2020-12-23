def threeNumberSum(array, targetSum):
    output = []
    array.sort()
    array_len = len(array)
    for i in range(array_len - 2):
        left = i + 1
        right = array_len - 1
        while left < right:
            result = array[i] + array[left] + array[right]
            if result == targetSum:
                output.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif result < targetSum:
                left += 1
            else:
                right -= 1

    return output
