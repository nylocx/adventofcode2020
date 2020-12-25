#%%
with open("day_25_input.txt") as input_data:
    card_pub_key, door_pub_key = map(int, input_data.read().strip().split("\n"))


def handshake(loop_size, subject_number=7):
    value = 1
    for i in range(loop_size):
        value *= subject_number
        value = value % 20201227
    return value


def handshake_fast(loop_size, subject_number=7):
    return pow(subject_number, loop_size, 20201227)


current_size = 1
while handshake_fast(current_size) != card_pub_key:
    if current_size % 100000 == 0:
        print("Current loop size:", current_size)
    current_size += 1

handshake_fast(current_size, door_pub_key)
