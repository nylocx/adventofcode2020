#%% Part 1
import numpy as np

with open("day_17_input.txt") as input_data:
    initial_plane = np.array(
        [[c == "#" for c in line.strip()] for line in input_data], dtype=bool
    )[np.newaxis, :, :]

space = np.pad(initial_plane, 7, constant_values=False)

depth, height, width = [x - 2 for x in space.shape]

space_view = space[1 : depth + 1, 1 : height + 1, 1 : width + 1]

neighbour_map = np.lib.stride_tricks.as_strided(
    space,
    shape=(depth, height, width, 3, 3, 3),
    strides=space.strides + space.strides,
)

for i in range(6):
    swap_space = space_view.copy()
    neighbour_sums = np.sum(neighbour_map, axis=(3, 4, 5), dtype=np.uint8)

    swap_space[~((neighbour_sums == 3) | (neighbour_sums == 4)) & space_view] = False
    swap_space[(neighbour_sums == 3) & ~space_view] = True

    space_view[:, :, :] = swap_space

print(f"Active cubes: {np.sum(space_view)}")

#%% Part 2
with open("day_17_input.txt") as input_data:
    initial_plane = np.array(
        [[c == "#" for c in line.strip()] for line in input_data], dtype=bool
    )[np.newaxis, np.newaxis, :, :]

space = np.pad(initial_plane, 7, constant_values=False)

time, depth, height, width = [x - 2 for x in space.shape]

space_view = space[1 : time + 1, 1 : depth + 1, 1 : height + 1, 1 : width + 1]

neighbour_map = np.lib.stride_tricks.as_strided(
    space,
    shape=(time, depth, height, width, 3, 3, 3, 3),
    strides=space.strides + space.strides,
)

for i in range(6):
    swap_space = space_view.copy()
    neighbour_sums = np.sum(neighbour_map, axis=(4, 5, 6, 7), dtype=np.uint8)

    swap_space[~((neighbour_sums == 3) | (neighbour_sums == 4)) & space_view] = False
    swap_space[(neighbour_sums == 3) & ~space_view] = True

    space_view[:, :, :, :] = swap_space

print(f"Active cubes: {np.sum(space_view)}")
