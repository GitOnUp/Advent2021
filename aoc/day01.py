from typing import Generator

from aoc import cache


class Solution:
    def yield_ints(self) -> Generator[int, None, None]:
        for line in cache.input_for_day(1).lines():
            yield int(line)

    def run_part_1(self) -> int:
        previous = None
        result = 0
        for val in self.yield_ints():
            if previous is None:
                previous = val
                continue
            if val > previous:
                result += 1
            previous = val
        return result

    def run_part_2(self) -> int:
        vals = self.yield_ints()
        current = [next(vals), next(vals), next(vals)]
        result = 0
        for val in vals:
            current_sum = sum(current)
            current = current[1:] + [val]
            next_sum = sum(current)
            if next_sum > current_sum:
                result += 1
        return result


if __name__ == "__main__":
    print(Solution().run_part_1())
    print(Solution().run_part_2())
