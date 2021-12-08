from typing import Generator

from aoc import cache


def yield_ints() -> Generator[int, None, None]:
    for line in cache.input_for_day(1).lines():
        yield int(line)


def run() -> int:
    previous = None
    result = 0
    for val in yield_ints():
        if previous is None:
            previous = val
            continue
        if val > previous:
            result += 1
        previous = val
    return result


if __name__ == "__main__":
    print(run())
