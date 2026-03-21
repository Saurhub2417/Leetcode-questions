import heapq

# Manhattan heuristic
def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])


def greedy_bfs(grid, start, goal):

    n = len(grid)

    visited = set()

    pq = []
    heapq.heappush(pq, (heuristic(start, goal), start))

    while pq:

        h, current = heapq.heappop(pq)

        if current == goal:
            print("Goal reached:", current)
            return

        if current in visited:
            continue

        visited.add(current)

        x, y = current

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        for dx, dy in directions:

            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] != -1:

                if (nx, ny) not in visited:
                    heapq.heappush(pq, (heuristic((nx,ny), goal), (nx,ny)))

    print("Goal not reachable")


# Example grid
grid = [
[0,0,0,0],
[0,-1,0,0],
[0,0,0,-1],
[0,0,0,0]
]

start = (0,0)
goal = (3,3)

greedy_bfs(grid, start, goal)