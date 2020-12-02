#%% check how may passwords are valid (Part 1)
counter = 0
with open("day_02_input.txt") as input_data:
    for x in input_data:
        definition, password = x.split(": ")
        bounds, character = definition.split()
        min_bound, max_bound = map(int, bounds.split("-"))
        occurrence = len([x for x in password if x == character])
        if min_bound <= occurrence <= max_bound:
            counter += 1
print(f"We found {counter} valid passwords in the database.")

#%% check how may passwords are valid (Part 2)
counter = 0
with open("day_02_input.txt") as input_data:
    for x in input_data:
        definition, password = x.split(": ")
        positions, character = definition.split()
        first_pos, second_pos = map(int, positions.split("-"))
        pw_length = len(password)
        first_match = password[first_pos - 1] == character if pw_length >= first_pos else False
        second_match = password[second_pos - 1] == character if pw_length >= second_pos else False
        if first_match != second_match:
            counter += 1
print(f"We found {counter} valid passwords in the database.")
