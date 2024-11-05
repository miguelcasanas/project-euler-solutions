total_perimeter_sum = 0
side, prev_area, next_area, sign = 5, 8, 28, 1

while (perimeter := 3 * side + sign) <= 10**9:
    total_perimeter_sum += perimeter
    
    prev_area, next_area, sign = next_area, 4 * next_area - prev_area, -sign
    side = (2 * sign + next_area) // 6

print(total_perimeter_sum)