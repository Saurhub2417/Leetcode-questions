from collections import deque

class BFSGraphSearch:
    def __init__(self, noOfVertex):
        self.V = noOfVertex
        self.adj = [[] for _ in range(noOfVertex)]

    def edge(self, x, y):
        self.adj[x].append(y)

    def BFS(self, srcVertex):
        visited = [False] * self.V
        q1 = deque()

        visited[srcVertex] = True
        q1.append(srcVertex)

        while q1:
            current = q1.popleft()
            print(current, end=" ")

            for node in self.adj[current]:
                if not visited[node]:
                    visited[node] = True
                    q1.append(node)


# Driver code
g1 = BFSGraphSearch(6)

print("BFS Traversal :", end=" ")

g1.edge(0, 1)
g1.edge(0, 2)
g1.edge(0, 5)
g1.edge(1, 0)
g1.edge(1, 2)
g1.edge(2, 0)
g1.edge(2, 1)
g1.edge(2, 3)
g1.edge(2, 4)
g1.edge(3, 2)
g1.edge(4, 2)
g1.edge(4, 5)
g1.edge(5, 0)
g1.edge(5, 4)

g1.BFS(0)