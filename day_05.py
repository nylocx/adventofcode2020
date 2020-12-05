#%% Parsing boarding passes
import numpy as np


def seat_id(input_string: str) -> int:
    return int(input_string.translate(str.maketrans("FLBR", "0011")), 2)


with open("day_05_input.txt") as input_data:
    seat_ids = sorted(map(seat_id, input_data))

#%% Part 1
print(f"Maximum seat id: {seat_ids[-1]}")

#%% Part 2
print(f"My seat id is: {seat_ids[np.nonzero(np.diff(seat_ids) == 2)[0][0]] + 1}")
