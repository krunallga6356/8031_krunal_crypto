from pycipher import Railfence

message = input("Enter message: ")
rails = int(input("Enter number of rails: "))

cipher = Railfence(rails)

encrypted = cipher.encipher(message)
print("Encrypted:", encrypted)

decrypted = cipher.decipher(encrypted)
print("Decrypted:", decrypted)
