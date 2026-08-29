def rail_fence_encrypt(text, rails):
    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1
    for char in text:
        fence[rail].append(char)
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction = -direction
    return "".join("".join(row) for row in fence)

def rail_fence_decrypt(cipher, rails):
    n = len(cipher)
    fence = [['' for _ in range(n)] for _ in range(rails)]
    rail = 0
    direction = 1
    for i in range(n):
        fence[rail][i] = '*'
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction = -direction
    idx = 0
    for r in range(rails):
        for c in range(n):
            if fence[r][c] == '*' and idx < n:
                fence[r][c] = cipher[idx]
                idx += 1
    result = []
    rail = 0
    direction = 1
    for i in range(n):
        result.append(fence[rail][i])
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction = -direction
    return "".join(result)

text = "HELLOWORLD"
rails = 3
encrypted = rail_fence_encrypt(text, rails)
decrypted = rail_fence_decrypt(encrypted, rails)
print("Original:", text)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
