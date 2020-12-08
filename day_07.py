#%% Day 07 Setup
from collections import defaultdict
from functools import lru_cache
import re

bag_regex = r"^(\w+ \w+)"
contained_regex = r"(\d+) (\w+ \w+)"


def parse_rule(input_string: str) -> tuple:
    bag_match = re.match(bag_regex, input_string).group(1)
    contained_match = [m.groups() for m in re.finditer(contained_regex, input_string)]
    return bag_match, [(int(m[0]), m[1]) for m in contained_match]


with open("day_07_input.txt") as input_data:
    bag_map = dict(map(parse_rule, input_data))


#%% Part 1 recursive slow
@lru_cache()
def contains_bag(query_bag: str, bags: set[str]) -> bool:
    if not bags:
        return False
    if query_bag in bags:
        return True
    return any(contains_bag(query_bag, {b for _, b in bag_map[bag]}) for bag in bags)


result = sum(contains_bag("shiny gold", s) for s in ({b for _, b in bags} for _, bags in bag_map.items()))
print(f"Bags that can contain a shiny gold bag: {result}")

#%% Part 1 a bit faster
lookup_dict = defaultdict(set)
for bag, contained_bags in bag_map.items():
    for _, contained_bag in contained_bags:
        lookup_dict[contained_bag].add(bag)

bags_containing_shiny_gold = lookup_dict["shiny gold"]
bags_to_process = bags_containing_shiny_gold.copy()
while bags_to_process:
    new_bags = lookup_dict[bags_to_process.pop()]
    bags_containing_shiny_gold |= new_bags
    bags_to_process |= new_bags

print(f"Bags that can contain a shiny gold bag: {len(bags_containing_shiny_gold)}")


#%% Part 2
def get_sub_bag_count(count: int, bag: str) -> int:
    if not bag_map[bag]:
        return count
    return count + count * sum(get_sub_bag_count(c, b) for c, b in bag_map[bag])


print(f"Bags contained in a shiny gold bag: {get_sub_bag_count(1, 'shiny gold') - 1}")
