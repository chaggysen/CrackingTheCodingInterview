def arrayOfProducts(array):
    output = []
    array_len = (len(array))
    cur_left_product = 1
    cur_right_product = 1
    left_values = {}
    right_values = {}
    for i in range(array_len):
        if i == 0:
            left_values[i] = 1
        else:
            cur_left_product *= array[i - 1]
            left_values[i] = cur_left_product

    for i in reversed(range(array_len)):
        if i == array_len - 1:
            right_values[i] = 1
        else:
            cur_right_product *= array[i + 1]
            right_values[i] = cur_right_product

    for i in range(array_len):
        output.append(left_values[i] * right_values[i])

    return output


test_array = [5, 1, 4, 2]
print(arrayOfProducts(test_array))
