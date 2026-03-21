from collections import deque

def treasure_hunt(grid, start, treasure):

    rows = len(grid)
    cols = len(grid[0])

    visited = [[False]*cols for _ in range(rows)]

    q = deque()
    q.append((start[0], start[1], 0))

    visited[start[0]][start[1]] = True

    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    while q:
        x, y, dist = q.popleft()

        if (x, y) == treasure:
            return dist

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            if nx>=0 and ny>=0 and nx<rows and ny<cols:
                if grid[nx][ny] != '#' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny, dist+1))

    return -1


grid = [
['S','.','.','.'],
['.','#','.','.'],
['.','.','#','.'],
['.','.','.','T']
]

start = (0,0)
treasure = (3,3)

distance = treasure_hunt(grid,start,treasure)

if distance != -1:
    print("Shortest distance to treasure:", distance)
else:
    print("Treasure not reachable")