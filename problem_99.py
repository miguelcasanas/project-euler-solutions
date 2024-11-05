from math import log

with open("0099_base_exp.txt") as f:
    basexps = f.readlines()

def value(n):
    base, exp = map(int, basexps[n - 1].split(','))
    return exp * log(base)

print(max(range(1, len(basexps) + 1), key=value))