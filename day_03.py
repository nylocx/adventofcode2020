#%% Build the map
import numpy as np
import math

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

with open("day_03_input.txt") as input_data:
    tree_map = np.array(
        [np.array([c == "#" for c in row.strip()], dtype=bool) for row in input_data]
    )
height, width = tree_map.shape

#%% Count the trees (Part 1)
result = np.sum(tree_map[(np.arange(height), np.arange(0, height * 3, 3) % width)])
print(f"Number of trees encountered: {result}")

#%% Count the trees for different slopes (Part 2)
slope_index_generator = (
    (np.arange(0, height, d), np.arange(0, math.ceil(height / d) * r, r) % width)
    for r, d in slopes
)
result = math.prod(np.sum(tree_map[s]) for s in slope_index_generator)
print(f"The product of tree encounters on different slopes is: {result}")


#%% The naive solutions is slower and uses more memory...
def count_trees(tree_map, right: int, down: int):
    columns = len(tree_map[0])
    return sum(row[i*right % columns] == "#" for i, row in enumerate(tree_map[::down]))


with open("day_03_input.txt") as input_data:
    tree_map = [r.strip() for r in input_data]

#%% Count the trees for different slopes (Part 2)
result = count_trees(tree_map, 3, 1)
print(f"Number of trees encountered: {result}")

#%% Count the trees (Part 1)
result = math.prod(count_trees(tree_map, r, d) for r, d in slopes)
print(f"The product of tree encounters on different slopes is: {result}")

#%%
import sys
sys.getsizeof([True, False, True, False, True, False, True, False])
