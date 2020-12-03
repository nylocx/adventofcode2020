#%% Build the map
import numpy as np
import math

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

with open("day_03_input.txt") as input_data:
    tree_map = np.array(
        [[c == "#" for c in row.strip()] for row in input_data], dtype=bool
    )
height, width = tree_map.shape

#%% Count the trees (Part 1)
result = sum(tree_map[np.arange(height), np.arange(0, height * 3, 3) % width])
print(f"Number of trees encountered: {result}")

#%% Count the trees for different slopes (Part 2)
slope_index_generator = (
    (np.arange(0, height, d), np.arange(0, math.ceil(height / d) * r, r) % width)
    for r, d in slopes
)

result = math.prod(sum(tree_map[s]) for s in slope_index_generator)
print(f"The product of tree encounters on different slopes is: {result}")
