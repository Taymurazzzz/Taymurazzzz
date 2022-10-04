import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    s = "abcdefghijklmnopqrstuvwxyz"
    f = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(plaintext)):
        if plaintext[i].isalpha() == True:
            if plaintext[i] in s:
                h = s[(s.find(plaintext[i]) + shift) % 26]
                ciphertext += h
            if plaintext[i] in f:
                h = f[(f.find(plaintext[i]) + shift) % 26]
                ciphertext += h
        else:
            ciphertext += plaintext[i]

    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    s = "abcdefghijklmnopqrstuvwxyz"
    f = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha() == True:
            if ciphertext[i] in s:
                h = s[(s.find(ciphertext[i]) - shift) % 26]
                plaintext += h
            if ciphertext[i] in f:
                h = f[(f.find(ciphertext[i]) - shift) % 26]
                plaintext += h
        else:
            plaintext += ciphertext[i]
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # for i in range(len(dictionary)):
    #     for j in range(26):
    #         if decrypt_caesar(ciphertext, j) == dictionary[i]:
    #             best_shift = j
    #             break
    #     break
    # return best_shift
    pass
