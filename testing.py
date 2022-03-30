import polynomial_hash as ph
import matplotlib.pyplot as plt

path = '/Users/gabrielemarinosci/Desktop/comp_sec/3k_words'

with open(path) as file:
    lst = []
    for line in file:
        lst.append(line.strip())


buckets = ['']*256
sizes=[]

for i in range(len(lst)):
    buckets[ph.polynomial_hash(lst[i])] += lst[i]

for bucket in buckets:
    sizes.append(len(bucket)) 
    
fig = plt.figure()
plt.bar([i for i in range(256)], sizes)
plt.xlabel('Buckets')
plt.ylabel('Number of Elements')
plt.title('Hash Function Distribution')
plt.show()