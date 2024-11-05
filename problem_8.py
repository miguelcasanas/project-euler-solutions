from math import prod

large_number = "NUMBER HERE"

greatest = 0
for i in range(len(large_number) - 12):
    product = prod(map(int, large_number[i:i + 13]))
    greatest = max(greatest, product)

print(greatest)