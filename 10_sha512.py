import hashlib
text = "Hello"
sha512_hash = hashlib.sha512(text.encode()).hexdigest()
print("SHA512:", sha512_hash)
