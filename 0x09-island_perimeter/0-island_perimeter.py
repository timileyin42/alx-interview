#!/usr/bin/python3
"""Island perimeter computing"""


def island_perimeter(grid):
    """
    Computes the perimeter of an island with no lakes.

    Parameters:
    grid: 2D grid representing the map where 0 is water and 1 is land.

    Returns:
    int: The perimeter of the island.
    """
    if not isinstance(grid, list):
        return 0

    perimeter = 0
    rows = len(grid)

    for u in range(rows):
        cols = len(grid[u])
        for v in range(cols):
            if grid[u][v] == 1:
                # Check the four surrounding cells
                if u == 0 or grid[u-1][v] == 0:
                    perimeter += 1
                if u == rows-1 or grid[u+1][v] == 0:
                    perimeter += 1
                if v == 0 or grid[u][v-1] == 0:
                    perimeter += 1
                if v == cols-1 or grid[u][v+1] == 0:
                    perimeter += 1

    return perimeter
