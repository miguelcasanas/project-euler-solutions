factorial = [1]
for n in range(1, 101): factorial.append(n * factorial[-1])

print(sum(map(int, str(factorial[-1]))))