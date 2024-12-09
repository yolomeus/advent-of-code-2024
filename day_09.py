from util import read_file


def build_block_representation(data: str):
    block_rep = []
    file_id = 0
    for i, x in enumerate(data):
        if i % 2 == 0:
            for _ in range(int(x)):
                block_rep.append(str(file_id))
            file_id += 1
        else:
            for _ in range(int(x)):
                block_rep.append(".")

    return block_rep


def main():
    data = read_file("data/day_09.txt")

    block_rep = build_block_representation(data)
    initial_len = len(block_rep)

    block_index = [i for i in range(len(block_rep)) if block_rep[i] == "."]
    while len(block_index) > 0:
        empty_idx = block_index.pop(0)
        next_item = block_rep.pop()
        while next_item == ".":
            next_item = block_rep.pop()

        if empty_idx > len(block_rep):
            block_rep.append(next_item)
        else:
            block_rep[empty_idx] = next_item

    checksum = sum([i * int(x) for i, x in enumerate(block_rep)])
    print(checksum)


if __name__ == "__main__":
    main()
