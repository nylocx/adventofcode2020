#%% Part 1
with open("day_08_input.txt") as input_data:
    op_codes = [x.strip().split() for x in input_data]

position = 0
visited = set()
accumulator = 0


class LoopException(Exception):
    pass


def noop(*args) -> None:
    global position
    if position in visited:
        raise LoopException
    visited.add(position)
    position += 1


def acc(value: int) -> None:
    global position
    global accumulator
    if position in visited:
        raise LoopException
    visited.add(position)
    accumulator += value
    position += 1


def jmp(value: int) -> None:
    global position
    if position in visited:
        raise LoopException
    visited.add(position)
    position += value


op_map = {
    "nop": noop,
    "acc": acc,
    "jmp": jmp
}
callstack = []
while True:
    callstack.append(position)
    op, arg = op_codes[position]
    try:
        op_map[op](int(arg))
    except LoopException:
        print(f"Value in the accumulator on loop detection: {accumulator}")
        break

#%% Part 2
position_to_check = [x for x in callstack[:-1] if op_codes[x][0] in ["nop", "jmp"]]

terminated = False
for corruption_candidate in position_to_check:
    if terminated:
        break
    position = 0
    visited = set()
    accumulator = 0
    altered_op_codes = op_codes.copy()
    old_op, arg = altered_op_codes[corruption_candidate]
    altered_op_codes[corruption_candidate] = ("nop", arg) if old_op == "jmp" else ("jmp", arg)
    while True:
        if position >= len(altered_op_codes):
            print(f"Value in the accumulator on termination: {accumulator}")
            terminated = True
            break
        op, arg = altered_op_codes[position]
        try:
            op_map[op](int(arg))
        except LoopException:
            break
