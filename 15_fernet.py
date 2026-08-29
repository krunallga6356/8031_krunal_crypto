from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)
text = b"Secret Message"
encrypted = f.encrypt(text)
decrypted = f.decrypt(encrypted)
print("Key:", key)
print("Original:", text)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
