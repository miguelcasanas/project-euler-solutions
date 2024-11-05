from string import digits
from itertools import permutations

primes = [2, 3, 5, 7, 11, 13, 17]

def is_valid(n):
    for i in range(len(n) - 3):
        if int(n[i+1:i+4]) % primes[i]: return False
    return True

result = 0
for p in permutations(digits):
    if p[0] == '0' or p[3] in "1357" or p[5] not in "05":
        continue
    pandigital = ''.join(p)
    if is_valid(pandigital): result += int(pandigital)

print(result)