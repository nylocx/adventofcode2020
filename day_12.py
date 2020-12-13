#%% Part 1
import numpy as np

with open("day_12_input.txt") as input_data:
    directions = [(line[0], int(line[1:].strip())) for line in input_data]

position = np.array([0, 0])
direction = np.array([0, 1])

direction_lookup = {
    "N": np.array([-1, 0]),
    "E": np.array([0, 1]),
    "S": np.array([1, 0]),
    "W": np.array([0, -1]),
}
# [[cos a, -sin a], [sin a, cos a]]
rotation_lookup = {
    90: np.array([[0, -1], [1, 0]]),
    180: np.array([[-1, 0], [0, -1]]),
    270: np.array([[0, 1], [-1, 0]]),
}

for command, value in directions:
    if command in "NESW":
        position += value * direction_lookup[command]
    elif command in "RL":
        rotation_value = value if command == "R" else 360 - value
        direction = np.matmul(direction, rotation_lookup[rotation_value])
    elif command == "F":
        position += value * direction
    else:
        print("Unsupported command", command)


print(f"Route distance: {np.sum(np.abs(position))}")

#%% Part 2

position = np.array([0, 0])
waypoint = np.array([-1, 10])

for command, value in directions:
    if command in "NESW":
        waypoint += value * direction_lookup[command]
    elif command in "RL":
        rotation_value = value if command == "R" else 360 - value
        waypoint = np.matmul(waypoint, rotation_lookup[rotation_value])
    elif command == "F":
        position += value * waypoint
    else:
        print("Unsupported command", command)

print(f"Route distance: {np.sum(np.abs(position))}")
