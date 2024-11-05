from itertools import permutations, count
from string import digits

pans = set(''.join(p) for p in permutations(digits[1:]))

def products():
    for n in range(1, 10**5):
        concat = ""
        for k in count(1):
            concat = concat + str(n * k)
            if (l := len(concat)) >= 9: break
        if l == 9 and concat in pans: yield concat

print(max(map(int, products())))