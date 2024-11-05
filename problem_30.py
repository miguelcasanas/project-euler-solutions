from itertools import count

for digits in count():
    if len(str(p := digits * 9**5)) < digits: break
    max_dpsum = p

powers = [n**5 for n in range(10)]

def dpsum(n):
    return sum(powers[d] for d in map(int, str(n)))

is_valid = lambda n: dpsum(n) == n
print(sum(filter(is_valid, range(2, max_dpsum + 1))))