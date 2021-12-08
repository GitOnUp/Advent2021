from typing import List

from aoc.day03_1 import yield_lines


def filter_remaining(greater: bool, remaining: List[List[int]]) -> int:
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


def run():
    zeroes = []
    ones = []
    for line in yield_lines():
        if line[0] == 0:
            zeroes.append(line)
        else:
            ones.append(line)
    oxy_start = zeroes if len(zeroes) > len(ones) else ones
    co2_start = ones if oxy_start is zeroes else zeroes
    return filter_remaining(True, oxy_start) * filter_remaining(False, co2_start)


if __name__ == "__main__":
    print(run())
