import hashlib
text = "Hello"
md5_hash = hashlib.md5(text.encode()).hexdigest()
print("MD5:", md5_hash)
