p = 23
g = 5
a = 6
b = 15
A = pow(g, a, p)
B = pow(g, b, p)
secret_a = pow(B, a, p)
secret_b = pow(A, b, p)
print("Public values: p =", p, "g =", g)
print("Alice public:", A)
print("Bob public:", B)
print("Shared secret (Alice):", secret_a)
print("Shared secret (Bob):", secret_b)
