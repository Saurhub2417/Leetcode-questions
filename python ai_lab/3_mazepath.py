import random
from collections import deque

class Cell:
    def __init__(self, r, c, d):
        self.row = r
        self.col = c
        self.dist = d


def shortestPath(grid):
    n = len(grid)

    if grid[0][0] == 0 or grid[n-1][n-1] == 0:
        print("No path exists.")
        return

    visited = [[False]*n for _ in range(n)]
    parent = [[None]*n for _ in range(n)]

    q = deque()
    q.append(Cell(0,0,0))

    visited[0][0] = True

    directions = [
        (-1,0),  # up
        (1,0),   # down
        (0,-1),  # left
        (0,1)    # right
    ]

    while q:
        cur = q.popleft()

        if cur.row == n-1 and cur.col == n-1:
            printPath(parent, cur)
            print("Shortest Path Length =", cur.dist)
            return

        for d in directions:
            nr = cur.row + d[0]
            nc = cur.col + d[1]

            if nr < 0 or nr >= n or nc < 0 or nc >= n:
                continue
            if grid[nr][nc] == 0:
                continue
            if visited[nr][nc]:
                continue

            visited[nr][nc] = True
            parent[nr][nc] = cur
            q.append(Cell(nr, nc, cur.dist + 1))

    print("No path exists.")


def printPath(parent, end):
    path = []
    current = end

    while current is not None:
        path.append(f"({current.row},{current.col})")
        current = parent[current.row][current.col]

    path.reverse()

    print("Shortest Path index positions:")
    print(" ".join(path))


# DFS for all paths
def printAllPaths(grid):
    n = len(grid)

    if grid[0][0] == 0 or grid[n-1][n-1] == 0:
        print("No paths exist.")
        return

    visited = [[False]*n for _ in range(n)]
    path = []

    print("All possible paths (as index positions):")
    dfsAll(grid,0,0,visited,path)


def dfsAll(grid,r,c,visited,path):
    n = len(grid)

    if r < 0 or c < 0 or r >= n or c >= n:
        return
    if grid[r][c] == 0 or visited[r][c]:
        return

    visited[r][c] = True
    path.append(f"({r},{c})")

    if r == n-1 and c == n-1:
        print(" ".join(path))
    else:
        dfsAll(grid,r-1,c,visited,path)
        dfsAll(grid,r+1,c,visited,path)
        dfsAll(grid,r,c-1,visited,path)
        dfsAll(grid,r,c+1,visited,path)

    path.pop()
    visited[r][c] = False


# Main
n = int(input("Enter grid size n: "))

grid = [[random.randint(0,1) for _ in range(n)] for _ in range(n)]

print("Generated Grid:")

for row in grid:
    print(*row)

printAllPaths(grid)

print()

shortestPath(grid)