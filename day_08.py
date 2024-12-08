from collections import defaultdict
from itertools import combinations

from util import read_file


def subtract(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    return a[0] - b[0], a[1] - b[1]


def add(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    return a[0] + b[0], a[1] + b[1]


def get_freq_to_position(map_: tuple[tuple, ...], height: int, width: int):
    freq_to_positions = defaultdict(set)
    for i in range(height):
        for j in range(width):
            freq = map_[i][j]
            if freq != ".":
                freq_to_positions[freq].add((i, j))

    return freq_to_positions


def in_bounds(pos: tuple[int, int], height: int, width: int) -> bool:
    return 0 <= pos[0] < height and 0 <= pos[1] < width


def main():
    data = read_file("data/day_08.txt")

    map_ = tuple(map(tuple, data.split("\n")))
    height = len(map_)
    width = len(map_[0])

    # part 1
    antinodes = set()
    freq_to_position = get_freq_to_position(map_, height, width)
    for freq, positions in freq_to_position.items():
        for pos_a, pos_b in combinations(positions, 2):
            vec = subtract(pos_b, pos_a)
            antinode_a = add(pos_b, vec)
            antinode_b = subtract(pos_a, vec)

            if in_bounds(antinode_a, height, width):
                antinodes.add(antinode_a)
            if in_bounds(antinode_b, height, width):
                antinodes.add(antinode_b)

    print(len(antinodes))
    # pprint(["".join([map_[i][j] for j in range(width)]) for i in range(height)])
    # pprint(
    #     [
    #         "".join(
    #             [map_[i][j] if (i, j) not in antinodes else "#" for j in range(width)]
    #         )
    #         for i in range(height)
    #     ]
    # )


if __name__ == "__main__":
    main()
