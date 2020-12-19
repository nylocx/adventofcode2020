#%%
import re

with open("day_19_input.txt") as input_data:
    rules = {}
    while match := re.match(r'^(\d+): "?([^"]+)"?$', input_data.readline().strip()):
        rule_id = match.group(1)
        rule = [f"({x.strip()})" for x in match.group(2).split("|")]
        rules[rule_id] = f"({'|'.join(rule)})"
    for key in sorted(rules, key=lambda x: -int(x)):
        current_rule = rules[key]
        for sub_key in rules:
            rules[sub_key] = rules[sub_key].replace(key, current_rule)
    rule_zero = f'^{rules["0"].replace(" ", "")}$'
    print(f"Number of valid rules: {sum(bool(re.match(rule_zero, line)) for line in input_data)}")

#%% Part 2
from lark import Lark, LarkError

with open("day_19_input.txt") as input_data:
    rules = ["start: x0"]
    while line := input_data.readline().strip():
        if line.startswith("8:"):
            line = "8: 42 | 42 8"
        elif line.startswith("11:"):
            line = "11: 42 31 | 42 11 31"

        rules.append(re.sub(r"(\d+)", r"x\1", line))
    patterns = [x.strip() for x in input_data]


parser = Lark("\n".join(rules))


def check_valid(pattern: str) -> bool:
    try:
        parser.parse(pattern)
    except LarkError:
        return False
    return True


print(f"Number of valid rules: {sum(check_valid(x) for x in patterns)}")
