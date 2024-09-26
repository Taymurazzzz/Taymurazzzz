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
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            if plaintext[i] in s:
                h = s[(s.find(plaintext[i]) + shift) % 26]
                ciphertext += h
            if plaintext[i] in s.upper():
                h = s[(s.find(plaintext[i].lower()) + shift) % 26].upper()
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
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            if ciphertext[i] in s:
                h = s[(s.find(ciphertext[i]) - shift) % 26]
                plaintext += h
            if ciphertext[i] in s.upper():
                h = s[(s.find(ciphertext[i].lower()) - shift) % 26].upper()
                plaintext += h
        else:
            plaintext += ciphertext[i]
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift
