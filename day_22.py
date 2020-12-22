#%% Part1
import numpy as np
from collections import deque
from itertools import islice

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


#%% Part 2
with open("day_22_input.txt") as input_data:
    deck1, deck2 = input_data.read().strip().split("\n\n")
deck1 = deque(map(int, deck1.split("\n")[1:]))
deck2 = deque(map(int, deck2.split("\n")[1:]))


def play_recursive(deck1: deque[int], deck2: deque[int]):
    print("Starting Game", play_recursive.counter, len(deck1), len(deck2))
    play_recursive.counter += 1
    game_history = set()
    while deck1 and deck2:
        if (tuple(deck1), tuple(deck2)) in game_history:
            print("Breaking loop")
            return True
        else:
            game_history.add((tuple(deck1), tuple(deck2)))
        card1, card2 = deck1.popleft(), deck2.popleft()

        if card1 <= len(deck1) and card2 <= len(deck2):
            winner = play_recursive(deque(list(deck1)[:card1]), deque(list(deck2)[:card2]))
            if winner:
                deck1.extend([card1, card2])
            else:
                deck2.extend([card2, card1])
        elif card1 > card2:
            deck1.extend([card1, card2])
        elif card2 > card1:
            deck2.extend([card2, card1])
        else:
            print("draw - should not happen")
    return bool(deck1)

play_recursive.counter = 0
play_recursive(deck1, deck2)

winner = np.array(deck1 if deck1 else deck2)

np.sum(winner * np.arange(len(winner), 0, -1))
