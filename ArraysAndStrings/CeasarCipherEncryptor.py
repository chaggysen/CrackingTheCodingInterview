def caesarCipherEncryptor(string, key):
    output = []
    key %= 26
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    for letter in string:
        output.append(getNewLetter(letter, key, alphabet))
    return "".join(output)


def getNewLetter(letter, key, alphabet):
    newKey = alphabet.index(letter) + key
    newKey %= 26
    return alphabet[newKey]
