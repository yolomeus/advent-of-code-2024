from copy import deepcopy, copy
from dataclasses import dataclass

from util import read_file


@dataclass
class Block:
    file_id: str
    size: int

    def __repr__(self):
        return "".join([self.file_id] * self.size)


def build_blocks(data: str) -> list[str]:
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


def build_blocks_oop(data: str) -> list[Block]:
    blocks = []
    file_id = 0
    for i, x in enumerate(data):
        if i % 2 == 0:
            if int(x) > 0:
                blocks.append(Block(str(file_id), int(x)))
            file_id += 1
        elif int(x) > 0:
            blocks.append(Block(".", int(x)))

    return blocks


def main():
    data = read_file("data/day_09.txt")

    block_rep = build_blocks(data)

    # part 1
    empty_block_index = [i for i in range(len(block_rep)) if block_rep[i] == "."]
    while len(empty_block_index) > 0:
        empty_idx = empty_block_index.pop(0)
        next_item = block_rep.pop()
        while next_item == ".":
            next_item = block_rep.pop()

        if empty_idx > len(block_rep):
            block_rep.append(next_item)
        else:
            block_rep[empty_idx] = next_item

    checksum = sum([i * int(x) for i, x in enumerate(block_rep)])
    print(checksum)

    # part 2
    blocks = build_blocks_oop(data)
    results = copy(blocks)

    for block in filter(lambda b: b.file_id != ".", blocks[::-1]):
        for i, empty_block in enumerate(results):
            if empty_block == block:
                break
            elif empty_block.file_id == ".":
                # actually an empty block
                if empty_block.size == block.size:
                    results.pop(i)
                    results.insert(i, deepcopy(block))
                    block.file_id = "."
                    break
                elif empty_block.size > block.size:
                    results.insert(i, deepcopy(block))
                    empty_block.size = empty_block.size - block.size
                    block.file_id = "."
                    break

    checksum = 0
    i = 0
    for b in results:
        for _ in range(b.size):
            if b.file_id != ".":
                checksum += int(b.file_id) * i
            i += 1

    print(checksum)


if __name__ == "__main__":
    main()
