words = {
    1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
    11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen",
    10: "ten", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety",
    100: "hundred", 1000: "thousand"
}

def letters(n):
    if n % 1000 == 0:
        return letters(n // 1000) + len(words[1000])
    if n % 100 == 0:
        return letters(n // 100) + len(words[100])
    if n in words: return len(words[n])
    if n > 100: return letters(n // 100) + len(words[100]) + 3 + letters(n % 100)
    return letters((n // 10) * 10) + letters(n % 10)

print(sum(map(letters, range(1, 1001))))