#%% Part 1
import numpy as np

lookup = {"L": 0, "#": 1, ".": np.nan}

with open("day_11_input.txt") as input_data:
    seat_map = np.array([[lookup[c] for c in line.strip()] for line in input_data])

floor = np.isnan(seat_map)
height, width = seat_map.shape

seat_map = np.zeros((height + 2, width + 2), dtype=bool)
seat_view = seat_map[1:-1, 1:-1]

neighbour_map = np.lib.stride_tricks.as_strided(
    seat_map,
    shape=(height, width, 3, 3),
    strides=seat_map.strides + seat_map.strides,
)

last_value = -1
it = 0
while last_value != (current_value := np.sum(seat_view, dtype=int)):
    neighbour_sums = np.sum(neighbour_map, axis=(2, 3), dtype=np.uint8)
    seat_view[(neighbour_sums == 0) & ~floor] = True
    seat_view[(neighbour_sums > 4) & seat_view & ~floor] = False
    last_value = current_value
    it += 1

print("Iterations needed", it)
print(f"The seating stabilizes at {last_value} occupied seats.")

#%% Part 2
with open("day_11_input.txt") as input_data:
    seat_map = np.array([[lookup[c] for c in line.strip()] for line in input_data])

floor = np.isnan(seat_map)
height, width = seat_map.shape

seat_map = np.zeros((height, width), dtype=bool)
neighbour_map = np.zeros((height, width, 2, 8), dtype=np.uint8)


def find_neighbours(xy: np.ndarray) -> tuple[np.ndarray]:
    neighbours = []
    for d in np.array([[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]):
        pos = xy + d
        while (pos >= np.array([0, 0])).all() & (pos < np.array([height, width])).all():
            if not floor[pos[0], pos[1]]:
                neighbours.append(pos)
                break
            pos += d
    return tuple(np.array(list(zip(*neighbours))))


neighbour_lookup = {(y, x): find_neighbours(np.array([y, x])) for y, x in np.ndindex(seat_map.shape)}


def visible_seated(ys, xs):
    res = np.zeros_like(seat_map, dtype=np.uint8)
    for y, x in np.nditer((ys, xs)):
        y, x = int(y), int(x)
        res[y, x] = np.sum(seat_map[neighbour_lookup[(y, x)]], dtype=np.uint8)
    return res

last_value = -1
it = 0
while last_value != (current_value := np.sum(seat_map, dtype=int)):
    neighbour_sums = np.fromfunction(visible_seated, shape=seat_map.shape)
    seat_map[(neighbour_sums == 0) & ~floor] = True
    seat_map[(neighbour_sums > 4) & seat_map & ~floor] = False
    last_value = current_value
    it += 1

print("Iterations needed", it)
print(f"The seating stabilizes at {last_value} occupied seats.")