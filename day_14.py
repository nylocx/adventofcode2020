#%% Part 1
import re

mask_regex = re.compile(r"^mask\s+=\s+([X10]+)")
mem_regex = re.compile(r"^mem\[(\d+)\]\s=\s(\d+)")

result = {}
with open("day_14_input.txt") as input_data:
    for line in input_data:
        if mask_match := mask_regex.match(line):
            and_pattern = int(mask_match.group(1).replace("1", "0").replace("X", "1"), 2)
            or_pattern = int(mask_match.group(1).replace("X", "0"), 2)
        else:
            position, value = map(int, mem_regex.match(line).groups())
            result[position] = value & and_pattern | or_pattern

sum(result.values())

#%% Part 2
result = {}
with open("day_14_input.txt") as input_data:
    for line in input_data:
        if mask_match := mask_regex.match(line):
            and_pattern = int(mask_match.group(1).replace("0", "1").replace("X", "0"), 2)
            or_template = mask_match.group(1)
            or_patterns = []
            x_count = line.count("X")
            for x in range(2**x_count):
                or_pattern = or_template
                for c in bin(x)[2:].zfill(x_count):
                    or_pattern = or_pattern.replace("X", c, 1)
                or_patterns.append(int(or_pattern, 2))
        else:
            position, value = map(int, mem_regex.match(line).groups())
            for or_pattern in or_patterns:
                result[position & and_pattern | or_pattern] = value

sum(result.values())
