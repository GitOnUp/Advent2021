import statistics

from aoc import cache


def run():
    placements = [int(s) for s in next(cache.input_for_day(7).lines()).split(',')]
    median = int(statistics.median(placements))
    sum = 0
    for placement in placements:
        sum += abs(placement - median)
    return sum


if __name__ == "__main__":
    print(run())
