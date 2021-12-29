from aoc.grid import MutableGrid


def flood_fill(grid: MutableGrid, x: int, y: int) -> int:
    """
    Floodfills and returns size of basin.
    """
    size = 0
    stack = [(x, y)]
    while len(stack) > 0:
        current_x, current_y = stack.pop()
        if grid.at(current_x, current_y) == 9:
            continue
        grid.set(current_x, current_y, 9)
        size += 1
        for neighbor_x, neighbor_y in grid.valid_neighbors(current_x, current_y):
            stack.append((neighbor_x, neighbor_y))
    return size


def solve() -> int:
    grid = MutableGrid.parse(9)
    basin_sizes = []
    for x, y in grid.iterate_coordinates():
        current = grid.at(x, y)
        if current == 9:
            continue
        basin_sizes.append(flood_fill(grid, x, y))
    basin_sizes = sorted(basin_sizes)[-3:]
    return basin_sizes[0] * basin_sizes[1] * basin_sizes[2]


if __name__ == "__main__":
    print(solve())
