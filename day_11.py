#%% Part 1
import numpy as np

lookup = {"L": 0, "#": 1, ".": np.nan}

with open("day_11_input.txt") as input_data:
    seat_map = np.pad(
        np.array([[lookup[c] for c in line.strip()] for line in input_data]),
        pad_width=1,
        mode="constant",
        constant_values=np.nan,
    )

height, width = seat_map.shape
seat_view = seat_map[1:-1, 1:-1]

neighbour_map = np.lib.stride_tricks.as_strided(
    seat_map,
    shape=(height - 2, width - 2, 3, 3),
    strides=seat_map.strides + seat_map.strides,
)

last_value = -1
floor = np.isnan(seat_view)
while last_value != (current_value := np.nansum(seat_view, dtype=int)):
    neighbour_sums = np.nansum(neighbour_map, axis=(2, 3), dtype=int)
    become_seated = (neighbour_sums == 0) & ~floor
    become_empty = (neighbour_sums > 4) & np.isclose(seat_view, 1) & ~floor
    seat_view[become_seated] = 1
    seat_view[become_empty] = 0
    last_value = current_value
last_value



# def check_result(sub):
#     if np.isnan(sub[1, 1]):
#         return np.nan
#     if np.isclose(np.sum(sub[~np.isnan(sub)]), 0):
#         return 1
#     elif np.isclose(sub[1, 1], 1) and np.sum(sub[~np.isnan(sub)]) > 4.5:
#         return 0
#     return sub[1, 1]
#
#
# def iterate_seating():
#     global seat_map
#     neighbour_map = np.lib.stride_tricks.as_strided(
#         seat_map,
#         shape=(height - 2, width - 2, 3, 3),
#         strides=seat_map.strides + seat_map.strides,
#     )
#     print(neighbour_map.strides)
#     result = []
#     for sub in neighbour_map.reshape(-1, 3, 3):
#         result.append(check_result(sub))
#     seat_map = np.pad(
#         np.array(result).reshape(height - 2, width - 2),
#         pad_width=1,
#         mode="constant",
#         constant_values=np.nan,
#     )
#     print(seat_map.dtype)
#     print(np.sum(seat_map[~np.isnan(seat_map)]))
#
#
# for i in range(100):
#     iterate_seating()
