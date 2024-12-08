from collections import defaultdict
from itertools import combinations

from util import read_file


def subtract(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    return a[0] - b[0], a[1] - b[1]


def add(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    return a[0] + b[0], a[1] + b[1]


def get_freq_to_positions(map_: tuple[tuple, ...], height: int, width: int):
    freq_to_positions = defaultdict(set)
    for i in range(height):
        for j in range(width):
            freq = map_[i][j]
            if freq != ".":
                freq_to_positions[freq].add((i, j))

    return freq_to_positions


def in_bounds(pos: tuple[int, int], height: int, width: int) -> bool:
    return 0 <= pos[0] < height and 0 <= pos[1] < width


def get_nodes_on_line(
    start: tuple[int, int], direction: tuple[int, int], map_height: int, map_width: int
) -> set[tuple[int, int]]:
    antinodes = set()

    antinode = start
    # positive direction
    while in_bounds(antinode, map_height, map_width):
        antinodes.add(antinode)
        antinode = add(antinode, direction)

    antinode = start
    # negative direction
    while in_bounds(antinode, map_height, map_width):
        antinodes.add(antinode)
        antinode = subtract(antinode, direction)

    return antinodes


def main():
    data = read_file("data/day_08.txt")

    map_ = tuple(map(tuple, data.split("\n")))
    height = len(map_)
    width = len(map_[0])

    # part 1
    freq_to_positions = get_freq_to_positions(map_, height, width)
    antinodes = set()
    for freq, antennas in freq_to_positions.items():
        for antenna_a, antenna_b in combinations(antennas, 2):
            direction_vec = subtract(antenna_b, antenna_a)
            for antinode in [
                add(antenna_b, direction_vec),
                subtract(antenna_a, direction_vec),
            ]:
                if in_bounds(antinode, height, width):
                    antinodes.add(antinode)

    print(len(antinodes))

    # part 2
    antinodes = set()
    for freq, antennas in freq_to_positions.items():
        for antenna_a, antenna_b in combinations(antennas, 2):
            direction_vec = subtract(antenna_b, antenna_a)
            # diagonal, all points on grid
            if direction_vec[0] == direction_vec[1]:
                antinodes |= get_nodes_on_line(antenna_a, (1, 1), height, width)
            # only multiple of vec are on the grid
            else:
                antinodes |= get_nodes_on_line(antenna_a, direction_vec, height, width)

    print(len(antinodes))


if __name__ == "__main__":
    main()
