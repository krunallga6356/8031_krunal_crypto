import random

def generate_key(length):
    return [random.randint(0, 25) for _ in range(length)]

def otp_encrypt(text, key):
    return "".join(chr((ord(c) - ord('A') + k) % 26 + ord('A')) for c, k in zip(text.upper(), key))

def otp_decrypt(cipher, key):
    return "".join(chr((ord(c) - ord('A') - k) % 26 + ord('A')) for c, k in zip(cipher, key))

text = "HELLO"
key = generate_key(len(text))
encrypted = otp_encrypt(text, key)
decrypted = otp_decrypt(encrypted, key)
print("Original:", text)
print("Key:", key)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
