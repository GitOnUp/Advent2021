from typing import Iterator, Tuple

from aoc.grid import Grid


def yield_low_points(grid: Grid) -> Iterator[Tuple[int, int]]:
    for x, y in grid.iterate_coordinates():
        current = grid.at(x, y)
        for neighbor_x, neighbor_y in grid.valid_neighbors(x, y):
            neighbor_val = grid.at(neighbor_x, neighbor_y)
            if neighbor_val <= current:
                break
        else:
            yield x, y


def solve() -> int:
    grid = Grid.parse(9)

    danger = 0
    for x, y in yield_low_points(grid):
        danger += grid.at(x, y) + 1
    return danger


if __name__ == "__main__":
    print(solve())
