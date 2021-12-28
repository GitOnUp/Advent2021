from typing import List, Optional, Iterator, Tuple

from aoc import cache


class Grid:
    def __init__(self, lines: List[List[int]]):
        self.lines = lines

    def at(self, x: int, y: int) -> Optional[int]:
        if x < 0 or x >= len(self.lines[0]) or y < 0 or y >= len(self.lines):
            return None
        return self.lines[y][x]

    def iterate_coordinates(self) -> Iterator[Tuple[int, int]]:
        for y in range(len(self.lines)):
            for x in range(len(self.lines[y])):
                yield x, y

    def valid_neighbors(self, x, y) -> List[Tuple[int, int]]:
        neighbors = []
        for delta_x, delta_y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_x, new_y = x + delta_x, y + delta_y
            if self.at(new_x, new_y) is not None:
                neighbors.append((new_x, new_y))
        return neighbors

    @classmethod
    def parse(cls) -> "Grid":
        lines = []
        for text_line in cache.input_for_day(9).lines():
            line = [int(ch) for ch in text_line]
            lines.append(line)
        return cls(lines)


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
    grid = Grid.parse()

    danger = 0
    for x, y in yield_low_points(grid):
        danger += grid.at(x, y) + 1
    return danger


if __name__ == "__main__":
    print(solve())
