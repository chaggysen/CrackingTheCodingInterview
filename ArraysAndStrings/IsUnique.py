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
