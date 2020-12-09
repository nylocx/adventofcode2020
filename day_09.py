#%% Part 1
import numpy as np

offset = 25

with open("day_09_input.txt") as input_data:
    numbers = np.array([int(x) for x in input_data])

x = np.lib.stride_tricks.as_strided(numbers, (len(numbers) - offset, offset), (numbers.strides[0], numbers.strides[0]))

for c, p in zip(numbers[25:], x):
    if not (np.triu(p.reshape(-1, 1) + p.reshape(1, -1), 1) == c).any():
        result_p1 = c
        break

print(f"The first number not composed from two of the {offset} previous is {result_p1}")

#%% Part 2
accumulated = numbers.cumsum()
found = False
for left in range(len(numbers) - 2):
    if found:
        break
    for right in range(left + 2, len(numbers)):
        if accumulated[right] - accumulated[left] == result_p1:
            involved = numbers[left + 1:right + 1]
            result_p2 = min(involved) + max(involved)
            found = True
            break

print(f"The sum of first and last element from the interval summing up tp {result_p1} is {result_p2}")
