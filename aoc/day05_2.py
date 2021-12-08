from aoc import cache


def run() -> int:
    points = {}
    dangerous = 0
    for line in cache.input_for_day(5).lines():
        first, second = line.split(' -> ')
        x1, y1 = first.split(',')
        x2, y2 = second.split(',')

        def register_point(point) -> int:
            count = points.get(point, 0)
            count += 1
            points[point] = count
            if count == 2:
                return 1
            return 0

        if x1 == x2:
            start = min(int(y1), int(y2))
            stop = max(int(y1), int(y2)) + 1
            for y in range(start, stop):
                point = f"{x1},{y}"
                dangerous += register_point(point)
        elif y1 == y2:
            start = min(int(x1), int(x2))
            stop = max(int(x1), int(x2)) + 1
            for x in range(start, stop):
                point = f"{x},{y1}"
                dangerous += register_point(point)
        else:
            x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
            x_step = 1 if x1 < x2 else -1
            y_step = 1 if y1 < y2 else -1
            count = abs(x1-x2) + 1
            x, y = x1, y1
            while count > 0:
                point = f"{x},{y}"
                dangerous += register_point(point)
                x += x_step
                y += y_step
                count -= 1

    return dangerous


if __name__ == "__main__":
    print(run())
    