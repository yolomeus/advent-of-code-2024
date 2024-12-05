import re

from util import read_file


def mul_sum(data: str) -> int:
    exp = r"mul\((\d+,\d+)\)"
    matches = re.findall(exp, data)

    num_pairs = tuple(map(lambda x: tuple(map(int, x.split(","))), matches))
    return sum([a * b for a, b in num_pairs])


def main() -> None:
    data = read_file("data/day_03.txt")
    # part 1
    print(mul_sum(data))

    # part 2
    exp = r"don't\(\).+?(do\(\))"
    cleaned = re.sub(exp, r"\1", data, flags=re.S)
    print(mul_sum(cleaned))


if __name__ == "__main__":
    main()
