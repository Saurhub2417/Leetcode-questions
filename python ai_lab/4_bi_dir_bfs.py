import random
from collections import deque

class Cell:
    def __init__(self, r, c):
        self.row = r
        self.col = c


directions = [
    (-1,0),
    (1,0),
    (0,-1),
    (0,1)
]


# ALL POSSIBLE PATHS (DFS)
def printAllPaths(grid):
    n = len(grid)

    if grid[0][0] == 0 or grid[n-1][n-1] == 0:
        print("No paths exist.")
        return

    visited = [[False]*n for _ in range(n)]
    path = []

    print("\nAll Possible Paths:")
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
        for d in directions:
            dfsAll(grid,r+d[0],c+d[1],visited,path)

    path.pop()
    visited[r][c] = False


# BI-DIRECTIONAL BFS
def biDirectionalShortestPath(grid):

    n = len(grid)

    if grid[0][0] == 0 or grid[n-1][n-1] == 0:
        print("No shortest path exists.")
        return

    visStart = [[False]*n for _ in range(n)]
    visEnd = [[False]*n for _ in range(n)]

    parentStart = [[None]*n for _ in range(n)]
    parentEnd = [[None]*n for _ in range(n)]

    qStart = deque()
    qEnd = deque()

    qStart.append(Cell(0,0))
    qEnd.append(Cell(n-1,n-1))

    visStart[0][0] = True
    visEnd[n-1][n-1] = True

    while qStart and qEnd:

        meet = expand(grid,qStart,visStart,visEnd,parentStart)
        if meet:
            printBiPath(parentStart,parentEnd,meet)
            return

        meet = expand(grid,qEnd,visEnd,visStart,parentEnd)
        if meet:
            printBiPath(parentStart,parentEnd,meet)
            return

    print("No shortest path exists.")


def expand(grid,q,visitedThis,visitedOther,parent):

    n = len(grid)
    size = len(q)

    while size > 0:
        cur = q.popleft()
        size -= 1

        for d in directions:

            nr = cur.row + d[0]
            nc = cur.col + d[1]

            if nr < 0 or nc < 0 or nr >= n or nc >= n:
                continue
            if grid[nr][nc] == 0 or visitedThis[nr][nc]:
                continue

            parent[nr][nc] = cur
            visitedThis[nr][nc] = True

            if visitedOther[nr][nc]:
                return Cell(nr,nc)

            q.append(Cell(nr,nc))

    return None


def printBiPath(pStart,pEnd,meet):

    path = []

    cur = meet
    while cur:
        path.append(f"({cur.row},{cur.col})")
        cur = pStart[cur.row][cur.col]

    path.reverse()

    cur = pEnd[meet.row][meet.col]
    while cur:
        path.append(f"({cur.row},{cur.col})")
        cur = pEnd[cur.row][cur.col]

    print("\nBi-Directional Shortest Path:")
    print(" ".join(path))
    print("Shortest Path Length =", len(path)-1)


# MAIN
n = int(input("Enter grid size n: "))

grid = [[1 if random.random() < 0.7 else 0 for _ in range(n)] for _ in range(n)]

grid[0][0] = 1
grid[n-1][n-1] = 1

print("\nGrid:")
for row in grid:
    print(*row)

printAllPaths(grid)
biDirectionalShortestPath(grid)