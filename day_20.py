#%% Part 1
import math
from collections import defaultdict
from typing import Iterator

import numpy as np
import re
import networkx as nx
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

    def rotate(self) -> None:
        self.data = np.rot90(self.data)

    def flip(self) -> None:
        self.data = np.flipud(self.data)

    def match_right(self, right_border: str) -> None:
        borders = self.borders()
        right_index = borders.index(right_border)
        if right_index == 0:
            self.data = np.rot90(self.data, k=-1)
        elif right_index == 1:
            self.data = np.flipud(np.rot90(self.data, k=1))
        elif right_index == 2:
            self.data = np.fliplr(self.data)
        elif right_index == 4:
            self.data = np.flipud(np.rot90(self.data, k=-1))
        elif right_index == 5:
            self.data = np.rot90(self.data, k=1)
        elif right_index == 6:
            self.data = np.flipud(np.fliplr(self.data))
        elif right_index == 7:
            self.data = np.flipud(self.data)

    def match_left(self, left_border: str) -> None:
        self.match_right(left_border)
        self.data = np.fliplr(self.data)

    def match_top(self, top_border: str) -> None:
        self.match_right(top_border)
        self.data = np.rot90(self.data)


def tile_generator(filename: str) -> Iterator[tuple[int, ImageTile]]:
    with open(filename) as input_data:
        text = input_data.read()

    for tile_string in text.strip().split("\n\n"):
        _id, *data = tile_string.split("\n")
        _id = int(re.search(r"\d+", _id).group())
        data = np.array([[c == "#" for c in row] for row in data], dtype=np.uint8)
        yield _id, ImageTile(data)


tile_connections = defaultdict(set)
tiles = dict(tile_generator("day_20_input.txt"))

for tile_id, tile in tiles.items():
    for border in tile.borders():
        tile_connections[border].add(tile_id)

G = nx.from_edgelist(
    [
        (*tile_ids, {"border": border})
        for border, tile_ids in tile_connections.items()
        if len(tile_ids) == 2
    ]
)

corner_tiles = [n[0] for n in G.degree() if n[1] == 2]

print(f"Product of edge tile ids: {math.prod(corner_tiles)}")

#%% Part 2

visited = {corner_tiles[0]}


def tile_score(x: int) -> int:
    return visited.add(x) or -sum(n in visited for n in G.neighbors(x))


c0 = corner_tiles[0]
tile_ids = [c0] + [v for _, v in nx.bfs_beam_edges(G, c0, tile_score, 4)]

tile_map = np.zeros((12, 12), dtype=int)
idx = np.argsort(np.add.outer(np.arange(12), np.arange(12)).ravel(), kind="stable")
tile_map.ravel()[idx] = np.array(tile_ids)

result = np.zeros((12*8, 12*8), dtype=int)

top_left_tile: ImageTile = tiles[tile_map[0, 0]]
top_left_tile.match_right(G.get_edge_data(tile_map[0, 0], tile_map[0, 1])["border"])
if top_left_tile.borders()[1] != G.get_edge_data(tile_map[0, 0], tile_map[1, 0])["border"]:
    top_left_tile.flip()
result[0:8, 0:8] = top_left_tile.data[1:9, 1:9]
for y in range(1, 12):
    tile_above: ImageTile = tiles[tile_map[y-1, 0]]
    tile: ImageTile = tiles[tile_map[y, 0]]
    tile.match_top(tile_above.borders()[1])
    result[y*8:y*8+8, 0:8] = tile.data[1:9, 1:9]

for y in range(0, 12):
    for x in range(1, 12):
        tile_left: ImageTile = tiles[tile_map[y, x - 1]]
        tile: ImageTile = tiles[tile_map[y, x]]
        tile.match_left(tile_left.borders()[3])
        result[y * 8:y * 8 + 8, x*8:x*8+8] = tile.data[1:9, 1:9]


monster = """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """
monster = np.array([[c == "#" for c in row] for row in monster.split("\n")], dtype=np.uint8)

monster_height, monster_length = monster.shape
monster_points = np.sum(monster)
height, width = result.shape

result_map = np.lib.stride_tricks.as_strided(
    result,
    (height - monster_height, width - monster_length, monster_height, monster_length),
    result.strides + result.strides
)

for _ in range(2):
    result = np.flipud(result)
    for _ in range(4):
        result = np.rot90(result)
        result_map = np.lib.stride_tricks.as_strided(
            result,
            (height - monster_height, width - monster_length, monster_height, monster_length),
            result.strides + result.strides
        )
        counter = 0
        for y in range(result_map.shape[0]):
            for x in range(result_map.shape[1]):
                if np.sum(result_map[y, x] & monster) == 15:
                    counter += 1

        if counter > 0:
            print("Remaining water:", int(np.sum(result) - monster_points * counter))
