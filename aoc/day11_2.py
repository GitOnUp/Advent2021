from aoc.day11_1 import step
from aoc.grid import MutableGrid


def solve() -> int:
    grid = MutableGrid.parse(11)
    step_number = 1
    while step(grid) != 100:
        step_number += 1
    return step_number


if __name__ == "__main__":
    print(solve())