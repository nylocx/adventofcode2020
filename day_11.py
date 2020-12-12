#%% Part 1
import numpy as np

lookup = {"L": 0, "#": 1, ".": np.nan}

with open("day_11_input.txt") as input_data:
    seat_map = np.array([[lookup[c] for c in line.strip()] for line in input_data])

floor = np.isnan(seat_map)
height, width = seat_map.shape

seat_map = np.zeros((height + 2, width + 2), dtype=bool)
seat_view = seat_map[1:-1, 1:-1]

neighbour_map = np.lib.stride_tricks.as_strided(
    seat_map,
    shape=(height, width, 3, 3),
    strides=seat_map.strides + seat_map.strides,
)

last_value = -1
while last_value != (current_value := np.sum(seat_view, dtype=int)):
    neighbour_sums = np.sum(neighbour_map, axis=(2, 3), dtype=np.uint8)
    seat_view[(neighbour_sums == 0) & ~floor] = True
    seat_view[(neighbour_sums > 4) & seat_view & ~floor] = False
    last_value = current_value

print(f"The seating stabilizes at {last_value} occupied seats.")
