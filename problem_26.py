def cycle_length(d):
    r_pos, pos, r = {}, 0, 1
    
    while r:
        if r in r_pos: return pos - r_pos[r]
        r_pos[r], pos, r = pos, pos + 1, (r * 10) % d

    return 0

max_length = 0
for d in range(2, 1000):
    if (length := cycle_length(d)) > max_length:
        max_length, longest = length, d

print(longest)