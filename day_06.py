from collections import defaultdict
from enum import Enum
from itertools import product
from typing import Iterable

from tqdm import tqdm

from util import read_file


class Direction(Enum):
    LEFT = "<"
    RIGHT = ">"
    UP = "^"
    DOWN = "V"


class Map:
    def __init__(self, data: str):
        self.rows = list(map(lambda x: list(x), data.split("\n")))
        self.height = len(self.rows)
        self.width = len(self.rows[0])

    def all_positions(self) -> Iterable[tuple[int, int]]:
        return product(range(self.height), range(self.width))

    def empty_positions(self) -> Iterable[tuple[int, int]]:
        return filter(lambda pos: self.get_symbol(*pos) == ".", self.all_positions())

    def get_symbol(self, y, x):
        if self.is_out_of_bounds(y, x):
            return None
        return self.rows[y][x]

    def set_symbol(self, y, x, symbol: str):
        self.rows[y][x] = symbol

    def is_out_of_bounds(self, y, x):
        return x < 0 or y < 0 or y >= self.height or x >= self.width

    def get_guard_state(self):
        position = None
        direction = None
        for y, x in self.all_positions():
            char = self.get_symbol(y, x)
            if char in {"<", ">", "^", "v"}:
                position = y, x
                direction = Direction(char)
                break
        return position, direction


class Guard:
    def __init__(self, map_: Map, position, direction):
        self.map_ = map_

        self.position = position
        self.direction = direction

    def move(self):
        y, x = self._next_position()
        while self.map_.get_symbol(y, x) == "#":
            self._turn_right()
            y, x = self._next_position()

        self.position = y, x

    def has_left(self):
        y, x = self.position
        return self.map_.is_out_of_bounds(y, x)

    def _next_position(self) -> tuple[int, int]:
        y, x = self.position
        match self.direction:
            case Direction.LEFT:
                return y, x - 1
            case Direction.RIGHT:
                return y, x + 1
            case Direction.UP:
                return y - 1, x
            case Direction.DOWN:
                return y + 1, x

    def _turn_right(self):
        match self.direction:
            case Direction.LEFT:
                self.direction = Direction.UP
            case Direction.RIGHT:
                self.direction = Direction.DOWN
            case Direction.UP:
                self.direction = Direction.RIGHT
            case Direction.DOWN:
                self.direction = Direction.LEFT


def get_visited_positions(map_: Map):
    pos, direction = map_.get_guard_state()
    guard = Guard(map_, pos, direction)

    visited = set()
    while not guard.has_left():
        visited.add(guard.position)
        guard.move()

    return visited


def get_num_loop_positions(map_: Map):
    num_loops = 0

    guard_pos, guard_dir = map_.get_guard_state()
    guard = Guard(map_, guard_pos, guard_dir)

    empty_positions = list(map_.empty_positions())
    for y, x in tqdm(empty_positions, total=len(empty_positions)):
        map_.set_symbol(y, x, "#")

        guard.position = guard_pos
        guard.direction = guard_dir

        state_history = defaultdict(set)
        while not guard.has_left():
            guard.move()
            # loop detected, we've already been in this position, facing the same direction
            if guard.direction in state_history[guard.position]:
                num_loops += 1
                break

            state_history[guard.position].add(guard.direction)

        map_.set_symbol(y, x, ".")

    return num_loops


def main():
    data = read_file("data/day_06.txt")

    map_ = Map(data)

    # part 1
    visited = get_visited_positions(map_)
    print(len(visited))

    # part 2
    print(get_num_loop_positions(map_))


if __name__ == "__main__":
    main()
