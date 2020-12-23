#%% Part1
from collections import deque
from tqdm import tqdm
input_data = deque(int(x) for x in "389547612")


def play(start_cups, moves):
    num_cups = len(start_cups)
    for _ in tqdm(range(moves)):
        current_cup = start_cups[0]
        start_cups.rotate(-1)
        destination = (current_cup - 2) % num_cups + 1
        while (idx := start_cups.index(destination)) < 3:
            destination = (destination - 2) % num_cups + 1
        taken = [start_cups.popleft() for _ in range(3)]
        start_cups.rotate(2 - idx)
        start_cups.extend(taken)
        start_cups.rotate(idx + 1)
    return start_cups


cups = play(input_data, 100)
cups.rotate(-cups.index(1))
print("".join(map(str, list(cups)[1:])))

#%% Part2
input_data = [int(x) for x in "389547612"]
input_data.extend(range(10, 1000001))


def play_fast(start_cups, moves):
    num_cups = len(start_cups)
    lookup = dict(zip(start_cups, start_cups[1:] + start_cups[:1]))
    current_cup = start_cups[-1]
    for _ in tqdm(range(moves)):
        current_cup = lookup[current_cup]

        pick_up = [lookup[current_cup]]
        for _ in range(2):
            pick_up.append(lookup[pick_up[-1]])
        lookup[current_cup] = lookup[pick_up[-1]]

        destination = (current_cup - 2) % num_cups + 1
        while destination in pick_up:
            destination = (destination - 2) % num_cups + 1

        lookup[destination] = pick_up[0]
        lookup[pick_up[-1]] = lookup[destination]

    return lookup


result = play_fast(input_data, 10_000_000)
cup_1 = result[1]
cup_2 = result[cup_1]

cup_1 * cup_2
