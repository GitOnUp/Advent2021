from aoc.day01_1 import yield_ints


def run() -> int:
    vals = yield_ints()
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
    print(run())
