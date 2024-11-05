powers = 0
for base in range(1, 10):
    for n in range(1, 22):
        if len(str(base**n)) == n:
            powers += 1

print(powers)