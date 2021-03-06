#%% find the two entries that sum to 2020 (Part 1)
from itertools import combinations
import math

searched_sum = 2020
counter = 0

with open("day_01_input.txt") as input_data:
    for i, pair in enumerate(combinations(sorted((int(x) for x in input_data)), 2)):
        if sum(pair) == searched_sum:
            print(f"The two entries that sum to {searched_sum} are {pair}")
            print(f"Their product is {math.prod(pair)}")
            print(f"Found after {i} tries")

#%% find the three entries that sum to 2020 (Part 2)
with open("day_01_input.txt") as input_data:
    for i, pair in enumerate(combinations(sorted((int(x) for x in input_data)), 3)):
        if sum(pair) == searched_sum:
            print(f"The three entries that sum to {searched_sum} are {pair}")
            print(f"Their product is {math.prod(pair)}")
            print(f"Found after {i} tries")
