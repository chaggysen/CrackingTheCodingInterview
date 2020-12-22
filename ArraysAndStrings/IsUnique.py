# Is Unique: Implememnt an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
def isUnique(string):
    memo = {}
    for char in string:
        if char in memo:
            return False
        else:
            memo[char] = True
    return True


testString = "Hello"
print(isUnique(testString))

# If we can't use additional data structures we can do the following:
# 1. Compare every character of the string to every other character of the string. This will take O(n^2) time and O(1) space
# 2. If we are allowed to modify the input string, we could sort the string in O(nlogn) time and then linearly check the string for neighboring characters that are identical. Careful: many
# sorting algorithms take extra space.
