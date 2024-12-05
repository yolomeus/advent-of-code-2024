from util import read_file


def parse_lists(text: str) -> list[list[int]]:
    lines = text.strip().split("\n")
    return [list(map(int, line.split())) for line in lines]


def is_safe(levels: list[int]) -> bool:
    is_increasing = levels[0] < levels[1]
    is_decreasing = levels[0] > levels[1]

    if levels[0] == levels[1]:
        return False

    for i in range(len(levels) - 1):
        a, b = levels[i], levels[i + 1]
        dist = abs(a - b)
        if dist > 3 or dist < 1:
            return False

        if is_increasing:
            if a > b:
                return False
        if is_decreasing:
            if a < b:
                return False

    return True


def is_safe_after_removal(levels: list[int]) -> bool:
    for i in range(len(levels)):
        subset = levels[:i] + levels[i + 1 :]
        if is_safe(subset):
            return True

    return False


def main() -> None:
    data = read_file("data/day_02.txt")
    lists = parse_lists(data)

    print(sum(map(is_safe, lists)))

    print(sum(map(is_safe_after_removal, lists)))


if __name__ == "__main__":
    main()
