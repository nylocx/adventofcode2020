#%% Part1
import numpy as np
from collections import deque
with open("day_22_input.txt") as input_data:
    deck1, deck2 = input_data.read().strip().split("\n\n")
deck1 = deque(map(int, deck1.split("\n")[1:]))
deck2 = deque(map(int, deck2.split("\n")[1:]))


def play():
    card1, card2 = deck1.popleft(), deck2.popleft()
    if card1 > card2:
        deck1.extend([card1, card2])
    elif card2 > card1:
        deck2.extend([card2, card1])
    else:
        print("draw - should not happen")


while deck1 and deck2:
    play()

winner = np.array(deck1 if deck1 else deck2)

np.sum(winner * np.arange(len(winner), 0, -1))
