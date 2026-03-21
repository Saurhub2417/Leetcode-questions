def is_safe(board, row, col, n):

    # check column
    for i in range(row):
        if board[i] == col:
            return False

    # check diagonal
    for i in range(row):
        if abs(board[i] - col) == abs(i - row):
            return False

    return True


def solve_nqueen(board, row, n):

    if row == n:
        print(board)
        return

    for col in range(n):

        if is_safe(board, row, col, n):
            board[row] = col
            solve_nqueen(board, row + 1, n)


# user input
n = int(input("Enter value of N: "))

board = [-1] * n

print("Solutions:")
solve_nqueen(board, 0, n)