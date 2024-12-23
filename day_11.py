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


def main():
    data = read_file("data/day_11.txt")
    stones = data.split()

    # part 1
    for _ in range(25):
        stones = update(stones)

    print(len(stones))


if __name__ == "__main__":
    main()
