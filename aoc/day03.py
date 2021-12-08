from typing import Generator, List, Iterable, Tuple

from aoc import cache


class Solution:
    def yield_lines(self) -> Generator[List[int], None, None]:
        for line in cache.input_for_day(3).lines():
            yield [int(item) for item in list(line)]

    def run_part_1(self):
        ones = None
        count = 0
        for line in self.yield_lines():
            if ones is None:
                ones = [0] * len(line)
            count += 1
            for i in range(len(ones)):
                if line[i]:
                    ones[i] += 1
        majority = count // 2
        gamma = int("".join(["1" if i > majority else "0" for i in ones]), base=2)
        epsilon = int("".join(["0" if i > majority else "1" for i in ones]), base=2)
        return gamma * epsilon

    def filter(self, greater: bool, remaining: List[List[int]]) -> int:
        ix = 1
        while len(remaining) > 1:
            zeroes = []
            ones = []
            for item in remaining:
                if item[ix] == 0:
                    zeroes.append(item)
                else:
                    ones.append(item)
            if greater:
                remaining = zeroes if len(zeroes) > len(ones) else ones
            else:
                remaining = ones if len(zeroes) > len(ones) else zeroes
            ix += 1
        return int("".join([str(i) for i in remaining[0]]), base=2)

    def run_part_2(self):
        zeroes = []
        ones = []
        for line in self.yield_lines():
            if line[0] == 0:
                zeroes.append(line)
            else:
                ones.append(line)
        oxy_start = zeroes if len(zeroes) > len(ones) else ones
        co2_start = ones if oxy_start is zeroes else zeroes
        return self.filter(True, oxy_start) * self.filter(False, co2_start)


if __name__ == "__main__":
    print(Solution().run_part_1())
    print(Solution().run_part_2())

