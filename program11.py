
#Generate SHA256 hash


import hashlib

text = input("Enter message to create hash value :")

SHA256_hash = hashlib.sha256(text.encode()).hexdigest()

print("SHA256 Hash : " , SHA256_hash)
