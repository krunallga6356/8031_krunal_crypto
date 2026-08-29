import hashlib
text = "Hello"
sha1_hash = hashlib.sha1(text.encode()).hexdigest()
print("SHA1:", sha1_hash)
