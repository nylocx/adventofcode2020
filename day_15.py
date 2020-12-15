#%% Part 1 and Part 2 just change last_turn value
input_data = [6, 3, 15, 13, 1, 0]

history = {x: i + 1 for i, x in enumerate(input_data[:-1])}
last_value = input_data[-1]
turn = len(input_data) + 1
last_turn = 30000000
while turn <= last_turn:
    if turn % (last_turn // 100) == 0:
        print(f"{turn / last_turn * 100:.0f} % finished")
    if last_value not in history:
        current_value = 0
    else:
        current_value = turn - history[last_value] - 1
    history[last_value] = turn - 1
    last_value = current_value
    turn += 1

last_value
