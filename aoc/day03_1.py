from typing import Generator, List

from aoc import cache


def yield_lines() -> Generator[List[int], None, None]:
    for line in cache.input_for_day(3).lines():
        yield [int(item) for item in list(line)]


def run():
    ones = None
    count = 0
    for line in yield_lines():
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


if __name__ == "__main__":
    print(run())

