from aoc import cache


def run(days: int):
    timers = {key: 0 for key in range(9)}
    initial_state = [int(s) for s in next(cache.input_for_day(6).lines()).split(',')]
    for val in initial_state:
        timers[val] += 1

    for _ in range(days):
        new_timers = {key: 0 for key in range(9)}
        for i in range(8):
            new_timers[i] = timers[i+1]
        new_timers[8] = timers[0]
        new_timers[6] += timers[0]
        timers = new_timers

    sum = 0
    for i in range(9):
        sum += timers[i]

    return sum


if __name__ == "__main__":
    print(run(80))
