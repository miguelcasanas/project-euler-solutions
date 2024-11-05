from more_itertools import nth_permutation
from string import digits

print(''.join(nth_permutation(digits, 10, 999_999)))