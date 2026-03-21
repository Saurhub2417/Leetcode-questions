import heapq

# Graph representation
graph = {
    'A': ['B','C'],
    'B': ['D','E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

# Heuristic values (estimated distance to goal)
heuristic = {
    'A': 6,
    'B': 4,
    'C': 5,
    'D': 3,
    'E': 2,
    'F': 4,
    'G': 0
}

def best_first_search(start, goal):

    visited = set()
    pq = []

    heapq.heappush(pq,(heuristic[start],start))

    while pq:

        h,node = heapq.heappop(pq)

        if node in visited:
            continue

        print(node,end=" ")
        visited.add(node)

        if node == goal:
            print("\nGoal reached!")
            return

        for neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq,(heuristic[neighbor],neighbor))


best_first_search('A','G')