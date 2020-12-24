# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array):
    depth = 1
    return productSumHelper(depth, array)


def productSumHelper(depth, array):
    cur_sum = 0
    for element in array:
        if type(element) is list:
            cur_sum += productSumHelper(depth + 1, element)
        else:
            cur_sum += element
    return depth * cur_sum
