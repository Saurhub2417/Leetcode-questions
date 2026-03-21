import heapq
import copy

goal = [
    [1,2,3],
    [4,5,6],
    [7,8,0]
]


class PuzzleNode:

    def __init__(self, board, g, parent=None):
        self.board = board
        self.g = g
        self.h = self.heuristic()
        self.f = self.g + self.h
        self.parent = parent

    # Manhattan distance heuristic
    def heuristic(self):
        distance = 0

        for i in range(3):
            for j in range(3):

                value = self.board[i][j]

                if value != 0:
                    target_x = (value-1)//3
                    target_y = (value-1)%3

                    distance += abs(i-target_x) + abs(j-target_y)

        return distance

    def __lt__(self, other):
        return self.f < other.f

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return hash(str(self.board))


def generate_neighbors(node):

    neighbors = []

    x = y = 0

    # find blank
    for i in range(3):
        for j in range(3):
            if node.board[i][j] == 0:
                x,y = i,j

    directions = [(1,0),(-1,0),(0,1),(0,-1)]

    for dx,dy in directions:

        nx = x + dx
        ny = y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:

            new_board = copy.deepcopy(node.board)

            new_board[x][y] = new_board[nx][ny]
            new_board[nx][ny] = 0

            neighbors.append(PuzzleNode(new_board,node.g+1,node))

    return neighbors


def print_board(board):

    for row in board:
        print(*row)
    print("---------")


def print_solution(node):

    path = []

    while node:
        path.append(node)
        node = node.parent

    path.reverse()

    print("Solution Steps:",len(path)-1)

    for step in path:
        print_board(step.board)


def solve_puzzle(start_board):

    open_list = []
    closed = set()

    start_node = PuzzleNode(start_board,0)

    heapq.heappush(open_list,start_node)

    while open_list:

        current = heapq.heappop(open_list)

        if current.board == goal:
            print_solution(current)
            return

        closed.add(current)

        for neighbor in generate_neighbors(current):

            if neighbor not in closed:
                heapq.heappush(open_list,neighbor)

    print("No Solution Found")


# Start state
start = [
    [1,2,3],
    [4,0,6],
    [7,5,8]
]

solve_puzzle(start)