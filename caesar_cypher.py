import string

def e_shifter(c, alphabet, key):
    return alphabet[ (alphabet.index(c) + key) % len(alphabet) ]

def d_shifter(c, alphabet, key):
    return alphabet[ (alphabet.index(c) - key) % len(alphabet) ]
            
def encrypt(path, key):
    
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    plain = ''
    cypher = ''
    
    with open(path) as file:
        plain = file.read() 
       
    for c in plain:
        if c.isalpha():
            if c.islower():
                cypher += e_shifter(c, lowercase, key)
            
            elif c.isupper():
                cypher += e_shifter(c, uppercase, key)
        
        else:
            cypher += c

    with open('cypher.txt', 'w') as f:
        f.write(cypher)

def decrypt(path,key):
    
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    plain = ''
    cypher = ''
    
    with open(path) as file:
        cypher = file.read() 
       
    for c in cypher:
        if c.isalpha():
            if c.islower():
                plain += d_shifter(c, lowercase, key)
            
            elif c.isupper():
                plain += d_shifter(c, uppercase, key)
        
        else:
            plain += c

    with open('plain.txt', 'w') as f:
        f.write(plain)

path = '/Users/gabrielemarinosci/Desktop/comp_sec/Afrah(Cesar substitution) .txt'

decrypt(path, 7)