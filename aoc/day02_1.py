from collections import namedtuple

from aoc import cache

Instruction = namedtuple("Instruction", ["direction", "value"])


def yield_lines() -> Instruction:
    for line in cache.input_for_day(2).lines():
        vals = line.strip().split(' ')
        yield Instruction(vals[0], int(vals[1]))


def run() -> int:
    horizontal = 0
    depth = 0
    for direction, value in yield_lines():
        if direction == 'forward':
            horizontal += value
        elif direction == 'down':
            depth += value
        elif direction == 'up':
            depth -= value
        else:
            raise ValueError("Bad line")
    return horizontal * depth


if __name__ == "__main__":
    print(run())
