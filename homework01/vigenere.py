def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    s = "abcdefghijklmnopqrstuvwxyz"
    f = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(plaintext)):
        if plaintext[i].isalpha() == True:
            if plaintext[i] in s and keyword[i % len(keyword)] in s:
                h = s[(s.find(plaintext[i]) + s.find(keyword[i % len(keyword)])) % 26]
                ciphertext += h
            if plaintext[i] in f and keyword[i % len(keyword)] in f:
                h = f[(f.find(plaintext[i]) + f.find(keyword[i % len(keyword)])) % 26]
                ciphertext += h
        else:
            ciphertext += plaintext[i]

    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    s = "abcdefghijklmnopqrstuvwxyz"
    f = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha() == True:
            if ciphertext[i] in s and keyword[i % len(keyword)] in s:
                h = s[(s.find(ciphertext[i]) - s.find(keyword[i % len(keyword)])) % 26]
                plaintext += h
            if ciphertext[i] in f and keyword[i % len(keyword)] in f:
                h = f[(f.find(ciphertext[i]) - f.find(keyword[i % len(keyword)])) % 26]
                plaintext += h
        else:
            plaintext += ciphertext[i]
    return plaintext
