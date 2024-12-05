from collections import defaultdict

from util import read_file


def is_valid(update: list[str], allowed_after: dict) -> bool:
    n = len(update)
    for i in range(n - 1):
        x = update[i]
        # check numbers before
        for j in range(i + 1, n):
            y = update[j]
            if y not in allowed_after[x]:
                return False

    return True


def main():
    data = read_file("data/day_05.txt").strip()
    rules, updates = data.split("\n\n")

    allowed_after = defaultdict(set)
    rules = [rule.split("|") for rule in rules.split("\n")]
    for k, v in rules:
        allowed_after[k].add(v)

    updates = updates.split("\n")
    updates = [update.split(",") for update in updates]

    valid_updates = [update for update in updates if is_valid(update, allowed_after)]
    middle_elements = [int(update[(len(update) // 2)]) for update in valid_updates]

    print(sum(middle_elements))


if __name__ == "__main__":
    main()
