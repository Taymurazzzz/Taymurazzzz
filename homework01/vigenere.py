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
    for i in range(len(plaintext)):
        if plaintext[i].isalpha() == True:
            if plaintext[i] in s:
                if keyword[i % len(keyword)] in s:
                    h = s[(s.find(plaintext[i]) + s.find(keyword[i % len(keyword)])) % 26]
                    ciphertext += h
                if keyword[(i % len(keyword))] in s.upper():
                    h = s[(s.find(plaintext[i]) + s.find(keyword[i % len(keyword)].lower())) % 26]
                    ciphertext += h
            if plaintext[i] in s.upper():
                if keyword[i % len(keyword)] in s:
                    h = s[
                        (s.find(plaintext[i].lower()) + s.find(keyword[i % len(keyword)])) % 26
                    ].upper
                    ciphertext += h
                if keyword[(i % len(keyword))] in f:
                    h = s[
                        (s.find(plaintext[i].lower()) + s.find(keyword[i % len(keyword)].lower())) % 26
                    ].upper()
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
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha() == True:
            if ciphertext[i] in s:
                if keyword[i % len(keyword)] in s:
                    h = s[(s.find(ciphertext[i]) - s.find(keyword[i % len(keyword)])) % 26]
                    plaintext += h
                if keyword[(i % len(keyword))] in s.upper():
                    h = s[(s.find(ciphertext[i]) - s.find(keyword[i % len(keyword)].lower())) % 26]
                    plaintext += h
            if ciphertext[i] in s.upper():
                if keyword[i % len(keyword)] in s:
                    h = s[
                        (s.find(ciphertext[i].lower()) - s.find(keyword[i % len(keyword)])) % 26
                    ].upper()
                    plaintext += h
                if keyword[(i % len(keyword))] in s.upper():
                    h = s[
                        (s.find(ciphertext[i].lower()) - s.find(keyword[i % len(keyword)].lower())) % 26
                    ].upper()
                    plaintext += h
        else:
            plaintext += ciphertext[i]
    return plaintext
