# https://replit.com/@appbrewery/caesar-cipher-1-start

"""
Encrypt and decrypt messages using the Caesar Cipher
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text, shift):
    cipher_text = ""
    for letter in text:
        index = alphabet.index(letter)
        new_index = index + shift
        if new_index >= len(alphabet):
            new_index -= len(alphabet)
        cipher_text += alphabet[new_index]
    print("The encoded message is:", cipher_text)

def decrypt(text, shift):
    if text == "":
        print("There is no text to decrypt")
        exit()

    cipher_text = ""
    for letter in text:
        index = alphabet.index(letter)
        new_index = index - shift
        if new_index < 0:
            new_index += len(alphabet)
        cipher_text += alphabet[new_index]
    print("The decoded message is:", cipher_text)


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")

if direction == "encode":
    user_text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))
    encrypt(user_text, shift)

elif direction == "decode":
    user_text = input("Type your message: ").lower()
    shift = int(input("Type the shift number:"))
    decrypt(user_text, shift)

else:
    print("Invalid input")