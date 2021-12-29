from typing import List, Optional, Iterator, Tuple

from aoc import cache


class Grid:
    CARDINAL_NEIGHBOR_DELTAS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    ALL_NEIGHBOR_DELTAS = CARDINAL_NEIGHBOR_DELTAS + [(1, 1), (-1, -1), (1, -1), (-1, 1)]

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

    def valid_neighbors(self, x, y, cardinal_only=True) -> List[Tuple[int, int]]:
        neighbors = []
        deltas = self.CARDINAL_NEIGHBOR_DELTAS if cardinal_only else self.ALL_NEIGHBOR_DELTAS
        for delta_x, delta_y in deltas:
            new_x, new_y = x + delta_x, y + delta_y
            if self.at(new_x, new_y) is not None:
                neighbors.append((new_x, new_y))
        return neighbors

    @classmethod
    def parse(cls, day: int) -> "Grid":
        lines = []
        for text_line in cache.input_for_day(day).lines():
            line = [int(ch) for ch in text_line]
            lines.append(line)
        return cls(lines)


class MutableGrid(Grid):
    def set(self, x: int, y: int, value: int) -> None:
        self.lines[y][x] = value
