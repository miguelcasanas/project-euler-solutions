from collections import Counter
from itertools import count

def same_digits(n):
    digits = Counter(str(n))
    for k in range(2, 7):
        if Counter(str(k*n)) != digits: return False
    return True

for n in count(1):
    if same_digits(n): break
print(n)