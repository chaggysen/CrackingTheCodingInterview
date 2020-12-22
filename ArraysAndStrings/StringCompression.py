# String Compression: Implement a method to perform basic string compression using the counts of repeated characters.
# For example, the string aabcccccaaa would become a2b1c5a3. If the compressed string would not become smaller than the original string, your method should return the original string.
# You can assume the string has only uppercase and lowercase letters

# aabcccccaaa

def stringCompression(string):
    output = ""
    count = 0
    start = 0
    end = 0
    string_len = len(string)
    while end < string_len:
        if string[start] == string[end]:
            count += 1
            end += 1
        else:
            output += str(string[start]) + str(count)
            start = end
            count = 0
    output += str(string[start]) + str(count)
    if len(string) < len(output):
        return string
    else:
        return output


print(stringCompression("aabcccccaaa"))
