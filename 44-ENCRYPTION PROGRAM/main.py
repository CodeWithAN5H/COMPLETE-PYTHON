import random
import string
# print(help(string))

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)

key = chars.copy()
random.shuffle(key)

# print(f"chars: {chars}")
# print(f"key: {key}")

#ENCRYPT
plain_text = input("Enter the plain message: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]
print(f"Cipher text: {cipher_text}")


#DECRYPT
cipher_text = input("Enter the encrypted message: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]
print(f"Plain text: {plain_text}")