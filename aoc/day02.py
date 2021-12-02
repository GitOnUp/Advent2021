from collections import namedtuple
from typing import Tuple

from aoc import cache


Instruction = namedtuple("Instruction", ["direction", "value"])


class Solution:
    def lines(self) -> Instruction:
        for line in cache.input_for_day(2).lines():
            vals = line.strip().split(' ')
            yield Instruction(vals[0], int(vals[1]))

    def run(self):
        horizontal = 0
        depth = 0
        for direction, value in self.lines():
            if direction == 'forward':
                horizontal += value
            elif direction == 'down':
                depth += value
            elif direction == 'up':
                depth -= value
            else:
                raise ValueError("Bad line")
        return horizontal * depth

    def run_part_2(self):
        aim = 0
        depth = 0
        horizontal = 0
        for direction, value in self.lines():
            if direction == 'forward':
                horizontal += value
                depth += aim * value
            elif direction == 'down':
                aim += value
            elif direction == 'up':
                aim -= value
            else:
                raise ValueError("Bad line")
        return horizontal * depth


if __name__ == "__main__":
    print(Solution().run())
    print(Solution().run_part_2())
