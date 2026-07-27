# Write a Python Program to implement Caesar Cipher.

def caesar_cipher(msg, key):
    encrypted_msg = ""

    for char in msg:
        if char.isupper():
            encrypted_char = chr((ord(char) + key - 65) % 26 + 65)
        elif char.islower():
            encrypted_char = chr((ord(char) + key - 97) % 26 + 97)
        else:
            encrypted_char = char
        encrypted_msg += encrypted_char
    return encrypted_msg

msg = input("Enter The Message:")
key = int(input("Enter Key:"))

encrypted_msg = caesar_cipher(msg, key)

print("Original message:", msg)
print("Original Key", key)
print("Original Caeser Cipher", encrypted_msg)
