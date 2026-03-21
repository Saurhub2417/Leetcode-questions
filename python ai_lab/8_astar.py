import heapq
import math
import random

ROW = 9
COL = 10


class Cell:
    def __init__(self):
        self.f = float("inf")
        self.g = float("inf")
        self.h = float("inf")
        self.parent = (-1, -1)


def is_valid(r, c):
    return 0 <= r < ROW and 0 <= c < COL


def is_unblocked(grid, r, c):
    return grid[r][c] == 1


def is_destination(r, c, dest):
    return r == dest[0] and c == dest[1]


def heuristic(r, c, dest):
    return math.sqrt((r - dest[0])**2 + (c - dest[1])**2)


def trace_path(cell, dest):
    print("\nPath:")

    path = []
    r, c = dest

    while True:
        path.append((r, c))
        pr, pc = cell[r][c].parent
        if (pr, pc) == (r, c):
            break
        r, c = pr, pc

    path.reverse()

    for p in path:
        print("->", p)


def a_star_search(grid, src, dest):

    if not is_valid(src[0], src[1]) or not is_valid(dest[0], dest[1]):
        print("Invalid source or destination")
        return

    if not is_unblocked(grid, src[0], src[1]) or not is_unblocked(grid, dest[0], dest[1]):
        print("Source or destination blocked")
        return

    closed = [[False]*COL for _ in range(ROW)]
    cell = [[Cell() for _ in range(COL)] for _ in range(ROW)]

    r, c = src

    cell[r][c].f = 0
    cell[r][c].g = 0
    cell[r][c].h = 0
    cell[r][c].parent = (r, c)

    open_list = []
    heapq.heappush(open_list, (0, r, c))

    row_dir = [-1,1,0,0,-1,-1,1,1]
    col_dir = [0,0,1,-1,1,-1,1,-1]

    while open_list:

        f, r, c = heapq.heappop(open_list)
        closed[r][c] = True

        for d in range(8):

            nr = r + row_dir[d]
            nc = c + col_dir[d]

            if is_valid(nr, nc):

                if is_destination(nr, nc, dest):
                    cell[nr][nc].parent = (r, c)
                    print("\nDestination Found!")
                    trace_path(cell, dest)
                    return

                if not closed[nr][nc] and is_unblocked(grid, nr, nc):

                    g_new = cell[r][c].g + (1.0 if d < 4 else 1.414)
                    h_new = heuristic(nr, nc, dest)
                    f_new = g_new + h_new

                    if cell[nr][nc].f > f_new:

                        heapq.heappush(open_list, (f_new, nr, nc))

                        cell[nr][nc].f = f_new
                        cell[nr][nc].g = g_new
                        cell[nr][nc].h = h_new
                        cell[nr][nc].parent = (r, c)

    print("Failed to find destination")


def generate_grid():
    grid = [[1 if random.random() < 0.8 else 0 for _ in range(COL)] for _ in range(ROW)]
    return grid


def print_grid(grid):
    print("Grid:")
    for r in grid:
        print(*r)


grid = generate_grid()

src = (8,0)
dest = (0,0)

grid[src[0]][src[1]] = 1
grid[dest[0]][dest[1]] = 1

print_grid(grid)

a_star_search(grid, src, dest)