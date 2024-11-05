from itertools import combinations, product
from string import digits

squares = []
for n in range(1, 10):
    sq = sorted(f"{n**2:02}")
    squares.append(sq)

count, cube_gen = 0, map(set, combinations(digits, 6))
for cubes in map(list, combinations(cube_gen, 2)):
    for i in range(2):
        if '6' in cubes[i] or '9' in cubes[i]:
            cubes[i].update({'6', '9'})

    unseen = squares.copy()
    for num in map(sorted, product(*cubes)):
        if num in unseen: unseen.remove(num)
        if not unseen: break
    else: continue
    count += 1

print(count)