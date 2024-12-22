from collections import defaultdict
from itertools import product

from util import read_file


class Graph:
    def __init__(self, topographic_map, adj_lists):
        self.topographic_map = topographic_map
        self.adj_lists = adj_lists

    def get_value(self, node: tuple[int, int]) -> int:
        i, j = node
        return self.topographic_map[i][j]

    def get_neighbors(self, i, j) -> list[tuple[int, int]]:
        return self.adj_lists[i][j]

    @property
    def nodes(self):
        n_rows, n_cols = len(self.topographic_map), len(self.topographic_map[0])
        return product(range(n_rows), range(n_cols))


def parse_data(data: str) -> tuple[tuple[int, ...], ...]:
    matrix = map(lambda line: tuple(map(int, line)), data.splitlines())
    return tuple(matrix)


def build_graph(topographic_map: tuple[tuple[int, ...], ...]):
    adj_lists = defaultdict(set)
    n_rows, n_cols = len(topographic_map), len(topographic_map[0])
    for i, j in product(range(n_rows), range(n_cols)):
        neighbors = ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1))
        for y, x in neighbors:
            if 0 <= y < n_rows and 0 <= x < n_cols:
                adj_lists[(i, j)].add((y, x))

    return Graph(topographic_map, adj_lists)


def main():
    data = read_file('data/day_10.txt')
    topographic_map = parse_data(data)
    graph = build_graph(topographic_map)
    starting_nodes = [(i, j) for i, j in graph.nodes if graph.get_value(node)]


if __name__ == '__main__':
    main()
