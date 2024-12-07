from enum import Enum

from util import read_file


class Direction(Enum):
    LEFT = "<"
    RIGHT = ">"
    UP = "^"
    DOWN = "V"


class Map:
    def __init__(self, data: str):
        self.rows = data.split("\n")
        self.height = len(self.rows)
        self.width = len(self.rows[0])

        self.guard = self._initial_guard()

    def _initial_guard(self):
        guard_pos = None
        direction = None
        for y in range(len(self.rows)):
            for x in range(len(self.rows[0])):
                char = self.rows[y][x]
                if char in {"<", ">", "^", "v"}:
                    guard_pos = y, x
                    direction = Direction(char)
                    break

        return Guard(direction, guard_pos)

    def get_visited_positions(self):
        visited = set()
        while not self.guard.has_left(self):
            visited.add(self.guard.position)
            y, x = self.guard.next_position()
            while self.rows[y][x] == "#":
                self.guard.turn_right()
                y, x = self.guard.next_position()

            self.guard.move()

        return visited


class Guard:
    def __init__(self, direction: Direction, position: tuple[int, int]):
        self.direction = direction
        self.position = position

    def next_position(self) -> tuple[int, int]:
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

    def move(self):
        self.position = self.next_position()

    def turn_right(self):
        match self.direction:
            case Direction.LEFT:
                self.direction = Direction.UP
            case Direction.RIGHT:
                self.direction = Direction.DOWN
            case Direction.UP:
                self.direction = Direction.RIGHT
            case Direction.DOWN:
                self.direction = Direction.LEFT

    def has_left(self, m: Map):
        y, x = self.position
        return x < 0 or y < 0 or y > m.height or x > m.width


def main():
    data = read_file("data/day_06.txt").strip()

    m = Map(data)
    visited = m.get_visited_positions()

    print(len(visited))


if __name__ == "__main__":
    main()
