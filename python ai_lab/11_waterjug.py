from collections import deque

def water_jug(jug1, jug2, target):

    visited = set()
    q = deque()

    q.append((0,0))

    while q:

        x, y = q.popleft()

        if (x,y) in visited:
            continue

        visited.add((x,y))

        print(x, y)

        if x == target or y == target:
            print("Target achieved!")
            return

        q.append((jug1, y))      # fill jug1
        q.append((x, jug2))      # fill jug2
        q.append((0, y))         # empty jug1
        q.append((x, 0))         # empty jug2

        # pour jug1 → jug2
        transfer = min(x, jug2-y)
        q.append((x-transfer, y+transfer))

        # pour jug2 → jug1
        transfer = min(y, jug1-x)
        q.append((x+transfer, y-transfer))


water_jug(4,3,2)