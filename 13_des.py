from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

key = b'8bytekey'
text = b'HelloDES'
cipher = DES.new(key, DES.MODE_ECB)
encrypted = cipher.encrypt(pad(text, DES.block_size))
decrypted = unpad(DES.new(key, DES.MODE_ECB).decrypt(encrypted), DES.block_size)
print("Original:", text)
print("Encrypted:", encrypted.hex())
print("Decrypted:", decrypted)
