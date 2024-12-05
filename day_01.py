from collections import defaultdict

from util import read_file


def parse_lists(text: str) -> tuple[list[int], list[int]]:
    lines = text.strip().split("\n")
    pairs = list(map(str.split, lines))
    list_a, list_b = zip(*pairs)
    return list_a, list_b


def main() -> None:
    data = read_file("data/day_01.txt")

    list_a, list_b = parse_lists(data)
    list_a, list_b = map(sorted, [list_a, list_b])

    # part 1
    diff = 0
    for a, b in zip(list_a, list_b):
        diff += abs(int(a) - int(b))

    print(diff)

    # part 2
    similarity = 0
    appearances = defaultdict(int)
    for a in list_a:
        for b in list_b:
            if a == b:
                appearances[a] += 1

    for key, value in appearances.items():
        similarity += int(key) * value

    print(similarity)


if __name__ == "__main__":
    main()
