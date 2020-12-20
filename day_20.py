#%% Part 1
import math
from collections import defaultdict, Counter
from typing import Iterator

import numpy as np
import re
from dataclasses import dataclass


@dataclass
class ImageTile:
    data: np.ndarray

    _border_slices: list[tuple] = (
            (0, slice(None)),
            (-1, slice(None)),
            (slice(None), 0),
            (slice(None), -1),
            (0, slice(None, None, -1)),
            (-1, slice(None, None, -1)),
            (slice(None, None, -1), 0),
            (slice(None, None, -1), -1),
    )

    def borders(self) -> list[str]:
        return ["".join(map(str, self.data[x, y])) for x, y in self._border_slices]


def tile_generator(filename: str) -> Iterator[tuple[int, ImageTile]]:
    with open(filename) as input_data:
        text = input_data.read()

    for tile_string in text.strip().split("\n\n"):
        tile_id, *tile_data = tile_string.split("\n")
        tile_id = int(re.search(r"\d+", tile_id).group())
        tile_data = np.array([[c == "#" for c in row] for row in tile_data], dtype=np.uint8)
        yield tile_id, ImageTile(tile_data)


tile_lookup = defaultdict(set)
tiles = dict(tile_generator("day_20_input.txt"))

for tile_id, tile in tiles.items():
    for border in tile.borders():
        tile_lookup[border].add(tile_id)

edge_tiles = Counter(tile_ids.pop() for border, tile_ids in tile_lookup.items() if len(tile_ids) == 1)

print(f"Product of edge tile ids: {math.prod(x[0] for x in edge_tiles.most_common(4))}")
