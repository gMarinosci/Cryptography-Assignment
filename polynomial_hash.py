def polynomial_hash (word):
    n = 0
    x = 23
    hash_value = 0
    for c in word:
        hash_value += ord(c) * (x**n)
        n += 1
    return hash_value % 255

