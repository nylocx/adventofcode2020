#%% Day 10 Setup
import math
import numpy as np

#%% Part 1
with open("day_10_input.txt") as input_data:
    adapters = np.sort(np.array([int(x) for x in input_data]))

differences = np.diff(np.hstack(([0], adapters, [adapters[-1] + 3])))
result_p1 = np.sum(differences == 1) * (np.sum(differences == 3))

print(f"Result for Part 1: {result_p1}")

#%% Part 2
with open("day_10_input.txt") as input_data:
    adapters = np.sort(np.array([int(x) for x in input_data]))

differences = np.diff(np.hstack(([0], adapters, [adapters[-1] + 3])))
run_diffs = np.diff(np.hstack(([0], differences == 1, [0])))
run_starts, = np.nonzero(run_diffs > 0)
run_ends, = np.nonzero(run_diffs < 0)

lookup = {2: 2, 3: 4, 4: 7}

result_p2 = math.prod(lookup[width] for start, end in zip(run_starts, run_ends) if (width := end - start) > 1)
print(f"Result for Part 2: {result_p2}")
