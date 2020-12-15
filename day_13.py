#%% Part 1
with open("day_13_input.txt") as input_data:
    earliest_arrival = int(input_data.readline().strip())
    bus_ids = [int(x) for x in input_data.readline().split(",") if x != "x"]

wait_time, bus_id = sorted((bus_id - earliest_arrival % bus_id, bus_id) for bus_id in bus_ids)[0]

print(wait_time, bus_id, wait_time * bus_id)

#%% Part 2
with open("day_13_input.txt") as input_data:
    input_data.readline()
    bus_ids = [(offset, int(x)) for offset, x in enumerate(input_data.readline().split(",")) if x != "x"]

step_size = bus_ids.pop(0)[1]
position = step_size
while bus_ids:
    offset, bus_id = bus_ids.pop(0)
    while (position + offset) % bus_id != 0:
        position += step_size
    step_size *= bus_id

position

