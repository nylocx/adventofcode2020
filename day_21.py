#%%
import re
from collections import defaultdict

pattern = re.compile(r"^((?:\w+\s)+)\(contains ((?:\w+(?:,\s)?)+)\)$")
with open("day_21_input.txt") as input_data:
    foods = [pattern.match(line).groups() for line in input_data]

food_ingredients = [i.split() for i, _ in foods]

allergens_dict = defaultdict(list)
for ingredients, allergens in foods:
    for allergen in allergens.split(", "):
        allergens_dict[allergen].append(set(ingredients.split()))

for allergen, ingredients in allergens_dict.items():
    allergens_dict[allergen] = ingredients[0].intersection(*ingredients[1:])

allergens_dict = {
    k: v for k, v in sorted(allergens_dict.items(), key=lambda x: len(x[1]))
}

seen = set()
while len(seen) < len(allergens_dict):
    for allergen, ingredients in allergens_dict.items():
        if len(ingredients) == 1:
            seen.update(ingredients)
        else:
            allergens_dict[allergen] = ingredients - seen

ingredients_with_allergens = [y for x in allergens_dict.values() for y in x]
print(
    "Occurence of non allergic ingredients:",
    sum(
        sum(x not in ingredients_with_allergens for x in ingredients)
        for ingredients in food_ingredients
    ),
)

#%% Part 2

print(
    "dangerous ingredient list",
    ",".join(y for x in dict(sorted(allergens_dict.items())).values() for y in x),
)
