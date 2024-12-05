from util import read_file


def match_count(i, j, rows, h, w):
    forward = None
    backward = None
    diagonal_right = None
    diagonal_right_backward = None
    downward = None
    upward = None
    diagonal_left = None
    diagonal_left_backward = None

    if not j + 3 >= w:
        forward = [rows[i][j + k] for k in range(4)]
        backward = forward[::-1]

    if not i + 3 >= h and not j + 3 >= w:
        diagonal_right = [rows[i + k][j + k] for k in range(4)]
        diagonal_right_backward = diagonal_right[::-1]

    if not i + 3 >= h:
        downward = [rows[i + k][j] for k in range(4)]
        upward = downward[::-1]

    if not j - 3 < 0 and not i + 3 >= h:
        diagonal_left = [rows[i + k][j - k] for k in range(4)]
        diagonal_left_backward = diagonal_left[::-1]

    words = map(
        lambda x: "".join(x),
        filter(
            lambda x: x is not None,
            [
                forward,
                backward,
                downward,
                upward,
                diagonal_right,
                diagonal_right_backward,
                diagonal_left,
                diagonal_left_backward,
            ],
        ),
    )

    return sum([w == "XMAS" for w in words])


def match_xmas(i, j, rows):
    if rows[i][j] != "A":
        return 0

    left_up = rows[i - 1][j - 1]
    right_down = rows[i + 1][j + 1]

    right_up = rows[i - 1][j + 1]
    left_down = rows[i + 1][j - 1]

    return {left_up, right_down} == {right_up, left_down} == {"M", "S"}


def main():
    data = read_file("data/day_04.txt")
    rows = data.split("\n")

    # part 1
    total_count = 0
    h, w = len(rows), len(rows[0])
    for i in range(h):
        for j in range(w):
            total_count += match_count(i, j, rows, h, w)

    print(total_count)

    # part 2
    total_x_mas = 0
    h, w = len(rows), len(rows[0])
    for i in range(h):
        for j in range(w):
            if not i + 1 >= h and not j + 1 >= w and not i - 1 < 0 and not j - 1 < 0:
                total_x_mas += match_xmas(i, j, rows)

    print(total_x_mas)


if __name__ == "__main__":
    main()
