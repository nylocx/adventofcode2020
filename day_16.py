#%% Part 1
import math
import re

import pandas as pd

with open("day_16_input.txt") as input_data:
    rules_dict = {}
    while match := re.match(r"^((?:\w+\s?)+):\s(\d+-\d+)\sor\s(\d+-\d+)", input_data.readline()):
        rules_dict[match.group(1)] = [pd.Interval(*map(int, g.split("-")), closed="both") for g in match.groups()[1:]]
    while "your ticket:" not in input_data.readline():
        pass
    my_ticket = list(map(int, input_data.readline().split(",")))
    while "nearby tickets:" not in input_data.readline():
        pass
    nearby_tickets = [list(map(int, x.split(","))) for x in input_data]


def check_valid(ticket: list[int]) -> tuple[bool, int]:
    valid = True
    error_rate = 0
    for value in ticket:
        if not any(value in rule for name, rules in rules_dict.items() for rule in rules):
            valid = False
            error_rate += value
    return valid, error_rate


print(f"Error Rate: {sum(check_valid(ticket)[1] for ticket in nearby_tickets)}")

#%% Part 2
valid_tickets = [ticket for ticket in nearby_tickets if check_valid(ticket)[0]]


def map_fields(ticket: list[int]) -> list[set]:
    possible_fields = [set() for _ in range(len(ticket))]
    for i, value in enumerate(ticket):
        possible_fields[i] = {name for name, rules in rules_dict.items() for rule in rules if value in rule}

    return possible_fields


candidates = {i: f[0].intersection(*f) for i, f in enumerate(zip(*[map_fields(ticket) for ticket in valid_tickets]))}
candidates_sorted = {k: v for k, v in sorted(candidates.items(), key=lambda item: len(item[1]))}

assigned = {}
for i, fields in candidates_sorted.items():
    fields = fields - assigned.keys()
    if len(fields) == 1:
        field, = fields
        assigned[field] = i
    else:
        print("Should not happen")

print(f"Departure field product: {math.prod(my_ticket[v] for k, v in assigned.items() if k.startswith('departure'))}")
