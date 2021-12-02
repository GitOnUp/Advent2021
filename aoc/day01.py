from logging import INFO

from aoc import cache


class Solution:
    def run(self) -> int:
        previous = None
        result = 0
        for line in cache.input_for_day(1).lines():
            val = int(line)
            if previous is None:
                previous = val
                continue
            if val > previous:
                result += 1
            previous = val
        return result


if __name__ == "__main__":
    print(Solution().run())
