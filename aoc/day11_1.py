from aoc.grid import MutableGrid


def step(grid: MutableGrid) -> int:
    new_flashes = set()

    for x, y in grid.iterate_coordinates():
        new_value = grid.at(x, y) + 1
        grid.set(x, y, new_value)
        if new_value > 9:
            new_flashes.add((x, y))

    flashes = set(new_flashes)
    while len(new_flashes):
        current_flashes = set(new_flashes)
        new_flashes = set()
        for flash_x, flash_y in current_flashes:
            for neighbor_x, neighbor_y in grid.valid_neighbors(flash_x, flash_y, cardinal_only=False):
                if (neighbor_x, neighbor_y) in flashes:
                    continue
                new_value = grid.at(neighbor_x, neighbor_y) + 1
                grid.set(neighbor_x, neighbor_y, new_value)
                if new_value > 9:
                    new_flashes.add((neighbor_x, neighbor_y))
                    flashes.add((neighbor_x, neighbor_y))

    for flash_x, flash_y in flashes:
        grid.set(flash_x, flash_y, 0)

    return len(flashes)


def solve() -> int:
    grid = MutableGrid.parse(11)
    total_flashes = 0
    for _ in range(100):
        total_flashes += step(grid)
    return total_flashes


if __name__ == "__main__":
    print(solve())
