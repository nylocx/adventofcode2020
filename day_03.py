#%% Build the map
import numpy as np
import math

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

with open("day_03_input.txt") as input_data:
    tree_map = np.array([[0 if c == "." else 1 for c in row.strip()] for row in input_data])
height, width = tree_map.shape

tree_map = np.tile(tree_map, math.ceil(height / width * max(s[0] for s in slopes)))

#%% Count the trees (Part 1)
print(f"Number of trees encountered: {sum(tree_map[:, 0::3].diagonal())}")

#%% Count the trees for different slopes (Part 2)
result = math.prod(sum(tree_map[0::d, 0::r].diagonal()) for r, d in slopes)
print(f"The product of tree encounters on different slopes is: {result}")
