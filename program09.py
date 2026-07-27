
#Generate MD5 hash


import hashlib

text = input("Enter message to create hash value :")

md5_hash = hashlib.md5(text.encode()).hexdigest()

print("MD5 Hash : " , md5_hash)
