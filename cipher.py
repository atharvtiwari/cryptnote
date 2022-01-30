def encrypt(x, y):
    l = ""
    for ch in x:
        a = ord(ch)
        l += chr(a + y)
    return l


def decrypt(x, y):
    l = ""
    for ch in x:
        a = ord(ch)
        l += chr(a - y)
    return l
