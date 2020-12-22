# There are three types of edit that can be performed on a string: Insert a char, remove a char, or replace a char. Given two strings, write a function to check if they are one
# edit or (zero edits) away.
# EXAMPLE:
# pale, ple -> true
# pales, pale -> true
# pale, bale -> true
# pale, bake -> false

def isOneAway(string1, string2):
    if string1 == string2:
        return True
    string1_len = len(string1)
    string2_len = len(string2)
    if abs(string1_len - string2_len) > 1:
        return False
    longer_string = None
    longer_len = 0
    shorter_string = None
    shorter_len = 0
    if string1_len > string2_len:
        longer_string = string1
        longer_len = string1_len
        shorter_string = string2
        shorter_len = string2_len
    elif string2_len > string1_len:
        longer_string = string2
        longer_len = string2_len
        shorter_string = string1
        shorter_len = string1_len

    edit_count = 0
    if longer_string is not None and shorter_string is not None:
        long_pointer = 0
        short_pointer = 0
        while long_pointer < longer_len and short_pointer < shorter_len:
            if longer_string[long_pointer] != shorter_string[short_pointer]:
                long_pointer += 1
                edit_count += 1
            else:
                long_pointer += 1
                short_pointer += 1
    else:
        pointer = 0
        while pointer < string1_len:
            if string1[pointer] != string2[pointer]:
                edit_count += 1
                pointer += 1
            else:
                pointer += 1
    return edit_count <= 1


test_string1 = "pale"
test_string2 = "bake"
print(isOneAway(test_string1, test_string2))
