from aoc import cache


def run():
    placements = [int(s) for s in next(cache.input_for_day(7).lines()).split(',')]
    min_p = min(placements)
    max_p = max(placements)
    min_cost = None
    for candidate in range(min_p, max_p + 1):
        total_cost = 0
        for placement in placements:
            diff = abs(candidate - placement)
            move_cost = (diff * (diff + 1)) // 2
            total_cost += move_cost
        if min_cost is None or total_cost < min_cost:
            min_cost = total_cost
    return min_cost


if __name__ == "__main__":
    print(run())
