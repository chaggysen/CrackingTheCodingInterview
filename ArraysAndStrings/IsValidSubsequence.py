def isValidSubsequence(array, sequence):
    sequence_len = len(sequence)
    array_len = len(array)
    array_pointer = 0
    sequence_pointer = 0
    while sequence_pointer < sequence_len and array_pointer < array_len:
        if sequence[sequence_pointer] == array[array_pointer]:
            sequence_pointer += 1
            array_pointer += 1
        else:
            array_pointer += 1
    return sequence_pointer == sequence_len
