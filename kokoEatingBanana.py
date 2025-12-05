import math
piles = [30,11,23,4,20]
h = 5
    
Totalsum = 0

for i in piles:
    Totalsum += i

k = Totalsum / h

print (math.ceil(k))
print(Totalsum)