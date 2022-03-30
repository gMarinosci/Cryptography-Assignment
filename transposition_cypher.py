import math

def encryption (path, key):

    cypher = ['']*key

    with open(path) as plain:
        plain = plain.read()

    print(cypher)
    
    grid = [plain[i:i+key] for i in range(0, len(plain), key)]
    print(grid)

    for row in grid:
        for i in range(key):
            try:
                cypher[i] += row[i]
            except IndexError:
                continue

    print(cypher)

    with open('t_cypher.txt','w') as cyphertext:
        for word in cypher:
            cyphertext.write(word)

def decryption (path, key):

    with open(path) as cypher:
        cypher = cypher.read()

    n = math.ceil(len(cypher) / key)
    plain = ['']*n
    grid = [cypher[i:i+n] for i in range(0, len(cypher), n)]
    print(grid)
    for row in grid:
        for i in range(len(row)):
            try:
                plain[i] += row[i]
            except IndexError:
                continue

    with open('t_plain.txt', 'w') as plaintext:
        for word in plain:
            plaintext.write(word)
