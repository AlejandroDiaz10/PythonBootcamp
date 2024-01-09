# https://replit.com/@appbrewery/caesar-cipher-1-start

"""
Encrypt and decrypt messages using the Caesar Cipher (improved)
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

def caesar(text, shift, direction):
    cipher_text = ""
    for letter in text:
        if letter not in alphabet:
            cipher_text += letter
            continue
        index = alphabet.index(letter)
        if direction == "encode":
            new_index = index + shift
        elif direction == "decode":
            new_index = index - shift
        if new_index >= len(alphabet):
            new_index -= len(alphabet)
        elif new_index < 0:
            new_index += len(alphabet)
        cipher_text += alphabet[new_index]
    print(f"The {direction}d message is: {cipher_text}")

print(logo)

while True:
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt: ")
    if direction != "encode" and direction != "decode":
        print("Invalid direction")
        exit()
    user_text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))
    shift = shift % len(alphabet)
    caesar(user_text, shift, direction)
    restart = input("Type ENTER if you want to go again. Otherwise type anything: ")
    if restart != "":
        print("Goodbye")
        break