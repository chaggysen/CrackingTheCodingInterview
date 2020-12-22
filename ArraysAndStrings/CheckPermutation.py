# Given two strings, write a method to decide if one is a permutation of the other
# Simple solution but requires sorting O(nlogn)
def checkPermutationBySorting(string1, string2):
    if len(string1) != len(string2):
        return False
    sorted_string1 = sorted(string1)
    sorted_string2 = sorted(string2)
    if sorted_string1 == sorted_string2:
        return True
    else:
        return False


def checkPermutationByComparingCharCount(string1, string2):
    if len(string1) != len(string2):
        return False
    memo_string1 = {}
    for char in string1:
        if char in memo_string1:
            memo_string1[char] += 1
        else:
            memo_string1[char] = 1
    for char in string2:
        if char not in memo_string1:
            return False
        else:
            memo_string1[char] -= 1
    for key in memo_string1:
        if memo_string1[key] != 0:
            return False
    return True


test_string1 = "helloy"
test_string2 = "ollehu"
print(checkPermutationByComparingCharCount(test_string1, test_string2))
