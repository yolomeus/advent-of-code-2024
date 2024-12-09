from collections import defaultdict

from util import read_file


def is_valid(update: list[str], allowed_after: dict[str, set[str]]) -> bool:
    n = len(update)
    for i in range(n - 1):
        x = update[i]
        # check numbers after
        for j in range(i + 1, n):
            y = update[j]
            if y not in allowed_after[x]:
                return False

    return True


def fix_order(update: list[str], allowed_after: dict[str, set[str]]) -> list[str]:
    reordered = [update[0]]
    # insertion sort?
    for i in range(1, len(update)):
        x = update[i]
        did_insert = False
        for j in range(len(reordered)):
            if reordered[j] in allowed_after[x]:
                reordered.insert(j, x)
                did_insert = True
                break

        if not did_insert:
            reordered.append(x)

    return reordered


def get_mid_elements(updates: list[list[str]]) -> list[int]:
    return [int(update[(len(update) // 2)]) for update in updates]


def main():
    data = read_file("data/day_05.txt")
    rules, updates = data.split("\n\n")

    allowed_after = defaultdict(set)
    rules = [rule.split("|") for rule in rules.split("\n")]
    for k, v in rules:
        allowed_after[k].add(v)

    updates = updates.split("\n")
    updates = [update.split(",") for update in updates]

    # part 1
    valid_updates = [update for update in updates if is_valid(update, allowed_after)]
    mid_elements = get_mid_elements(valid_updates)

    print(sum(mid_elements))

    # part 2
    broken_updates = [
        update for update in updates if not is_valid(update, allowed_after)
    ]
    fixed_updates = [fix_order(update, allowed_after) for update in broken_updates]
    print(sum(get_mid_elements(fixed_updates)))


if __name__ == "__main__":
    main()
