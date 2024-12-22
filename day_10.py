from collections import defaultdict
from itertools import product

from util import read_file

Node = tuple[int, int]
Matrix = tuple[tuple[int, ...], ...]


class Graph:
    def __init__(self, topographic_map: Matrix, adj_lists):
        self.topographic_map = topographic_map
        self.adj_lists = adj_lists

    def get_value(self, node: Node) -> int:
        i, j = node
        return self.topographic_map[i][j]

    def get_neighbors(self, i: int, j: int) -> list[Node]:
        return self.adj_lists[(i, j)]

    @property
    def nodes(self):
        n_rows, n_cols = len(self.topographic_map), len(self.topographic_map[0])
        return product(range(n_rows), range(n_cols))


def parse_map(data: str) -> Matrix:
    matrix = map(lambda line: tuple(map(int, line)), data.splitlines())
    return tuple(matrix)


def build_graph(topographic_map: Matrix):
    adj_lists = defaultdict(set)
    n_rows, n_cols = len(topographic_map), len(topographic_map[0])
    for i, j in product(range(n_rows), range(n_cols)):
        neighbors = ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1))
        for y, x in neighbors:
            if 0 <= y < n_rows and 0 <= x < n_cols:
                adj_lists[(i, j)].add((y, x))

    return Graph(topographic_map, adj_lists)


def trailhead_score(graph: Graph, trailhead: Node) -> int:
    stack = [trailhead]
    trail_ends = set()

    while len(stack) > 0:
        cur_node = stack.pop()
        cur_val = graph.get_value(cur_node)
        if cur_val == 9:
            trail_ends.add(cur_node)
        else:
            neighbors = graph.get_neighbors(*cur_node)
            for neighbor in neighbors:
                neighbor_val = graph.get_value(neighbor)
                if neighbor_val - cur_val == 1:
                    stack.append(neighbor)

    return len(trail_ends)


def trailhead_rating(graph: Graph, trailhead: Node) -> int:
    stack = [trailhead]
    n_trails = 0

    while len(stack) > 0:
        cur_node = stack.pop()
        cur_val = graph.get_value(cur_node)
        if cur_val == 9:
            n_trails += 1
        else:
            neighbors = graph.get_neighbors(*cur_node)
            for neighbor in neighbors:
                neighbor_val = graph.get_value(neighbor)
                if neighbor_val - cur_val == 1:
                    stack.append(neighbor)

    return n_trails


def main():
    data = read_file("data/day_10.txt")
    topographic_map = parse_map(data)
    graph = build_graph(topographic_map)
    trail_heads = [(i, j) for i, j in graph.nodes if graph.get_value((i, j)) == 0]

    # part 1
    total_score = sum([trailhead_score(graph, trailhead) for trailhead in trail_heads])
    print(total_score)

    # part 2
    total_score = sum([trailhead_rating(graph, trailhead) for trailhead in trail_heads])
    print(total_score)


if __name__ == "__main__":
    main()
