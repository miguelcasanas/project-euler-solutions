from collections import defaultdict

LIMIT = 10**4

cubes = defaultdict(set)
for n in range(LIMIT):
    digits = sorted(str(n**3))
    cubes[tuple(digits)].add(n**3)

new_cubes = set()
for s in cubes.values():
    if len(s) == 5: new_cubes |= s

print(min(new_cubes))