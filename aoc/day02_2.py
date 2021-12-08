from aoc.day02_1 import yield_lines


def run():
    aim = 0
    depth = 0
    horizontal = 0
    for direction, value in yield_lines():
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
    print(run())
