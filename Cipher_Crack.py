import sys

a = input("Enter filename to brute force: ")
file = open(a, "r", encoding="utf-8")
file.seek(0)
x = file.read()
l = ""
for i in range(256):
    for ch in x:
        a = ord(ch)
        try:
            l += chr(a - i)
        except ValueError:
            sys.exit("Character out of range. Last entry may be incomplete.")
    print(i, "\n" + l, "\n")
    l = ""
