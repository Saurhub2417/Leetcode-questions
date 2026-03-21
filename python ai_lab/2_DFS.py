class DFSGraphSearch:
    def __init__(self, noOfVertex):
        self.V = noOfVertex
        self.adj = [[] for _ in range(noOfVertex)]

    def edge(self, x, y):
        self.adj[x].append(y)

    def DFS(self, srcVertex):
        visited = [False] * self.V
        s1 = []
        s1.append(srcVertex)
        while s1:
            srcVertex = s1[-1]   # peek
            s1.pop()

            for node in self.adj[srcVertex]:
                if not visited[node]:
                    s1.append(node)

            if not visited[srcVertex]:
                print(srcVertex, end=" ")
                visited[srcVertex] = True
print("DFS Traversal :", end=" ")
g1 = DFSGraphSearch(6)
g1.edge(0,1)
g1.edge(0,2)
g1.edge(0,5)
g1.edge(1,0)
g1.edge(1,2)
g1.edge(2,0)
g1.edge(2,1)
g1.edge(2,3)
g1.edge(2,4)
g1.edge(3,2)
g1.edge(4,2)
g1.edge(4,5)
g1.edge(5,0)
g1.edge(5,4)
g1.DFS(0)