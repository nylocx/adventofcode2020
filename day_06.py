#%% Part 1
with open("day_06_input.txt") as input_data:
    groups = [{q for q in g.replace("\n", "")} for g in input_data.read().split("\n\n")]
print(f"Anyone yes answers per group summed: {sum(len(x) for x in groups)}")

#%% Part 2
with open("day_06_input.txt") as input_data:
    groups = [[set(q) for q in g.split("\n")] for g in input_data.read().split("\n\n")]
print(
    f"Everyone yes answers per group summed: {sum(len(set.intersection(*[y for y in x])) for x in groups)}"
)
