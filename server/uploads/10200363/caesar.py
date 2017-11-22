import sys

if len(sys.argv) != 2:
    print("usage: python caesar.py key")
    sys.exit(1)

key = int(sys.argv[1])
text = input("Enter a text to encrypt: ")

for letter in text:
    if letter.isupper():
         print(chr((ord(letter) - ord("A") + key) % 26 + ord("A")), end = "")
    elif letter.islower():
        print(chr((ord(letter) - ord("a") + key) % 26 + ord("a")), end = "")
    else:
        print(letter, end = "")
print()
