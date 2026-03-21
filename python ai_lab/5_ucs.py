import heapq

class Node:
    def __init__(self, state):
        self.state = state
        self.cost = float('inf')
        self.neighbors = []

    def __lt__(self, other):
        return self.cost < other.cost


class Edge:
    def __init__(self, to, weight):
        self.to = to
        self.weight = weight


class UniformCostSearchDemo:

    def uniformCostSearch(self, start, goal):

        open_list = []
        closed = set()

        start.cost = 0
        heapq.heappush(open_list, start)

        while open_list:

            current = heapq.heappop(open_list)

            if current == goal:
                print("Goal reached with cost =", current.cost)
                return True

            closed.add(current)

            for edge in current.neighbors:
                neighbor = edge.to
                newCost = current.cost + edge.weight

                if neighbor not in closed and newCost < neighbor.cost:
                    neighbor.cost = newCost
                    heapq.heappush(open_list, neighbor)

        return False


# MAIN
A = Node("S")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")
G = Node("F")

A.neighbors.append(Edge(B, 4))
A.neighbors.append(Edge(C, 2))

B.neighbors.append(Edge(D, 5))
B.neighbors.append(Edge(E, 10))

C.neighbors.append(Edge(B, 1))
C.neighbors.append(Edge(D, 8))

D.neighbors.append(Edge(E, 2))
D.neighbors.append(Edge(G, 6))

E.neighbors.append(Edge(G, 3))

ucs = UniformCostSearchDemo()
found = ucs.uniformCostSearch(A, G)

if not found:
    print("Goal not reachable")