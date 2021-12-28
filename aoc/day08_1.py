from typing import List, Tuple, Iterator

from aoc import cache


def parse() -> Iterator[Tuple[List[str], List[str]]]:
    for line in cache.input_for_day(8).lines():
        tests, values = line.split(' | ')
        yield tests.split(' '), values.split(' ')


def solve() -> int:
    count = 0
    for _, values in parse():
        for value in values:
            if len(value) in [2, 3, 4, 7]:
                count += 1

    return count


if __name__ == "__main__":
    print(solve())
