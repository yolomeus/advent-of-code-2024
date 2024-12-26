import time
from functools import lru_cache

from util import read_file


def update(stones):
    result = []
    for stone in stones:
        if stone == "0":
            result.append("1")
        elif len(stone) % 2 == 0:
            new_stone_a, new_stone_b = (
                int(stone[: len(stone) // 2]),
                int(stone[len(stone) // 2 :]),
            )
            result.extend([str(new_stone_a), str(new_stone_b)])
        else:
            result.append(str(int(stone) * 2024))

    return result


@lru_cache(maxsize=None)
def count_resulting_stones(stone: int, depth: int, max_depth: int) -> int:
    stone_str = str(stone)

    if depth == max_depth:
        return 1
    elif stone == 0:
        return count_resulting_stones(1, depth + 1, max_depth)
    elif len(stone_str) % 2 == 0:
        k = len(stone_str) // 2
        a, b = int(stone_str[:k]), int(stone_str[k:])

        count_a = count_resulting_stones(a, depth + 1, max_depth)
        count_b = count_resulting_stones(b, depth + 1, max_depth)

        return count_a + count_b

    return count_resulting_stones(stone * 2024, depth + 1, max_depth)


def main():
    data = read_file("data/day_11.txt")
    stones = data.split()

    start = time.time()
    # part 1
    for _ in range(10):
        stones = update(stones)
    total = len(stones)

    end = time.time()
    print(total)
    print(f"took: {(end - start) * 1000:.2f}ms")

    # part 2
    # recursive + memoization
    start = time.time()

    stones = list(map(int, data.split()))
    total = 0
    for stone in stones:
        total += count_resulting_stones(stone, 0, 75)

    end = time.time()
    print(total)
    print(f"took: {(end - start) * 1000:.2f}ms")


if __name__ == "__main__":
    main()
