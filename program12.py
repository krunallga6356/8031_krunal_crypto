
#Generate SHA512 hash


import hashlib

text = input("Enter message to create hash value :")

SHA512_hash = hashlib.sha512(text.encode()).hexdigest()

print("SHA512 Hash : " , SHA512_hash)
