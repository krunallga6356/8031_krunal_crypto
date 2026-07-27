
a = int(input("Enter a number for a: "))
b = int(input("Enter a number for b: "))

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

def modulus(a,b):
    if b != 0:
        return a % b
    else:
        return "Cannot divide by zero"
    
print("The sum of a and b is:", add(a, b))
print("The difference of a and b is:", subtract(a, b))
print("The product of a and b is:", multiply(a, b))
print("The quotient of a and b is:", divide(a, b))
print("The remainder of a divided by b is:", modulus(a, b))