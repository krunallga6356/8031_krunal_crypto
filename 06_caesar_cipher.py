def caesar(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

text = "HELLO"
shift = 3
encrypted = caesar(text, shift)
decrypted = caesar(encrypted, -shift)
print("Original:", text)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
