#%% Part 1
import numpy as np

offset = 25

with open("day_09_input.txt") as input_data:
    numbers = np.array([int(x) for x in input_data])

x = np.lib.stride_tricks.as_strided(numbers, (len(numbers) - offset, offset), (numbers.strides[0], numbers.strides[0]))

for c, p in zip(numbers[25:], np.expand_dims(x, axis=1)):
    if not (p + p.T == c).any():
        print(p.shape)
        result_p1 = c
        break

print(f"The first number not composed from two of the {offset} previous is {result_p1}")

#%% Part 2
accumulated = numbers.cumsum().reshape(1, -1)
for left, right in zip(*np.nonzero((accumulated - accumulated.T) == result_p1)):
    if right - left > 2:
        involved = numbers[left + 1:right + 1]
        result_p2 = min(involved) + max(involved)
        print(f"The sum of first and last element from the interval summing up tp {result_p1} is {result_p2}")
