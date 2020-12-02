#%% Parsing helper
import re
from typing import Tuple

parse_expression = re.compile(r"^(\d+)-(\d+)\s+(\w):\s+(.*)$")


def parse_entry(entry: str) -> Tuple:
    groups = parse_expression.match(entry).groups()
    return *map(int, groups[:2]), *groups[2:]


#%% check how may passwords are valid (Part 1)
with open("day_02_input.txt") as input_data:
    result = sum(f <= p.count(c) <= s for f, s, c, p in map(parse_entry, input_data))
print(f"We found {result} valid passwords in the database.")

#%% check how may passwords are valid (Part 2)
with open("day_02_input.txt") as input_data:
    result = sum(
        (p[f - 1] == c) != (p[s - 1] == c)
        for f, s, c, p in map(parse_entry, input_data)
    )
print(f"We found {result} valid passwords in the database.")
