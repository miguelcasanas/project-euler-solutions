from itertools import product, starmap

powers = starmap(pow, product(range(2, 101), repeat=2))
print(len(set(powers)))