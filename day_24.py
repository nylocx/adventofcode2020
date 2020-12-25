import numpy as np
from collections import Counter

directions_map = {
    "e": np.array([1, -1, 0]),
    "se": np.array([0, -1, 1]),
    "sw": np.array([-1, 0, 1]),
    "w": np.array([-1, 1, 0]),
    "ne": np.array([1, 0, -1]),
    "nw": np.array([0, 1, -1]),
}

hex_grid = Counter()

with open("day_24_input.txt") as input_data:
    for line in input_data:
        idx = 0
        pos = np.zeros(3, dtype=int)
        while idx < len(line.strip()):
            if line[idx] in "ew":
                pos += directions_map[line[idx]]
                idx += 1
            else:
                pos += directions_map[line[idx : idx + 2]]
                idx += 2
        hex_grid[tuple(pos)] += 1

sum((x % 2 != 0) for x in hex_grid.values())


#%% Part 2
hex_grid = Counter()

with open("day_24_input.txt") as input_data:
    for line in input_data:
        idx = 0
        pos = np.zeros(3, dtype=int)
        while idx < len(line.strip()):
            if line[idx] in "ew":
                pos += directions_map[line[idx]]
                idx += 1
            else:
                pos += directions_map[line[idx : idx + 2]]
                idx += 2
        hex_grid[tuple(pos)] += 1

def get_neighbours(position):
    return [position + x for x in directions_map.values()]


for i in range(100):
    black_tiles = {p for p, c in hex_grid.items() if c % 2 != 0}
    flip_positions = set()
    visited = set()
    for pos in black_tiles:
        neighbours = get_neighbours(np.array(pos, dtype=int))
        num_black_neighbours = sum(tuple(x) in black_tiles for x in neighbours)
        if num_black_neighbours == 0 or num_black_neighbours > 2:
            flip_positions.add(tuple(pos))
        for npos in neighbours:
            npos_tuple = tuple(npos)
            if npos_tuple not in black_tiles and npos_tuple not in visited:
                num_black_neighbours = sum(
                    tuple(x) in black_tiles for x in get_neighbours(npos)
                )
                if num_black_neighbours == 2:
                    flip_positions.add(npos_tuple)
            visited.add(npos_tuple)
    hex_grid.update(flip_positions)

sum((x % 2 != 0) for x in hex_grid.values())
