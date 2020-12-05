#%% Parsing boarding passes
import numpy as np


def seat_id(input_string: str) -> tuple[int, int, int]:
    return int(input_string.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1"), 2)


with open("day_05_input.txt") as input_data:
    seat_ids = np.array(sorted(map(seat_id, input_data)))

#%% Part 1
print(f"Maximum seat id: {seat_ids[-1]}")

#%% Part 2
print(f"My seat id is: {seat_ids[np.nonzero(np.diff(seat_ids) == 2)[0][0]] + 1}")
