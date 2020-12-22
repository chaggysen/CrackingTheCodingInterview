# Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a
# rearrangement of letters. The palindrome does not need to be limited to dictionary words.
# Example:
# Input: Tact Coa
# Output: True (permutation: "taco cat", "atco cta", etc)

def isPalindromePermutation(string):
    memo = {}
    for char in string:
        if char in memo:
            memo[char] += 1
        else:
            memo[char] = 1

    odd_char_count = 0
    for key in memo:
        if memo[key] % 2 != 0:
            odd_char_count += 1

    return (odd_char_count <= 1)


test_string = "ccttyu"
print(isPalindromePermutation(test_string))
