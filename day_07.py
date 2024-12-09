from itertools import product
from operator import add, mul
from typing import Callable

from util import read_file


def concat(a: int, b: int):
    return int(f"{a}{b}")


def reduce(ops: tuple[Callable], nums: list[int]):
    first, rest = nums[0], nums[1:]
    total = first
    for op, num in zip(ops, rest):
        total = op(total, num)

    return total


def compute_total_calibration(data, operators):
    total_calibration = 0
    for test_value, parts in data:
        for ops in product(operators, repeat=len(parts) - 1):
            x = reduce(ops, parts)
            if x == test_value:
                total_calibration += test_value
                break
    return total_calibration


def main():
    data = read_file("data/day_07.txt")
    data = [
        (int(total), list(map(int, parts.split())))
        for total, parts in map(lambda x: x.split(":"), data.split("\n"))
    ]

    # part 1
    print(compute_total_calibration(data, [add, mul]))
    # part 2
    print(compute_total_calibration(data, [add, mul, concat]))


if __name__ == "__main__":
    main()
