from collections import Counter
from itertools import batched, starmap
import re

with open("0054_poker.txt") as f:
    cards = re.findall(r'\w{2}', f.read())

def counts(hand):
    values = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    v_c, s_c = Counter(), Counter()
    for card in hand:
        value, suit = card
        if value in values: v_c[values[value]] += 1
        else: v_c[int(value)] += 1
        s_c[suit] += 1
    return v_c, s_c

def classify(hand):
    v_c, s_c = counts(hand)
    if 3 in v_c.values() and 2 in v_c.values(): return "ful"
    if 5 in s_c.values(): return "flush"
    sorted_values = sorted(v_c.keys())
    if (sorted_values[-1] - sorted_values[0] == 4) and len(set(v_c.values())) == 1: return "straight"
    if 3 in v_c.values(): return "three of a kind"
    if list(v_c.values()).count(2) == 2: return "two pairs"
    if 2 in v_c.values(): return "one pair"
    return "high card"
    
def wins_player1(h1, h2):
    scores = ["high card", "one pair", "two pairs", "three of a kind", "straight", "flush", "ful"]
    s1, s2 = scores.index(classify(h1)), scores.index(classify(h2))
    if s1 > s2: return True
    if s1 == s2:
        v_c1, _ = counts(h1)
        v_c2, _ = counts(h2)
        if s1 == 0:
            return max(v_c1.keys()) > max(v_c2.keys())
        elif s1 == 1:
            return v_c1.most_common(1)[0][0] > v_c2.most_common(1)[0][0]
    return False

game_gen = batched(batched(cards, 5), 2)
print(sum(starmap(wins_player1, game_gen)))