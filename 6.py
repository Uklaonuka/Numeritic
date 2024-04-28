from collections import deque


def is_valid(x, y, n):
    return x >= 0 and y >= 0 and x < n and y < n


def get_moves(x, y, n, piece):
    moves = []
    if piece == 'K':
        possible_moves = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]
    else:  # piece == 'G'
        possible_moves = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]

    for dx, dy in possible_moves:
        new_x, new_y = x + dx, y + dy
        if is_valid(new_x, new_y, n):
            moves.append((new_x, new_y))

    return moves


def min_moves_to_destination(n, board):
    start = None
    end = None
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'S':
                start = (i, j, 'K')  # начинаем с коня
            elif board[i][j] == 'F':
                end = (i, j)

    queue = deque([start])
    visited = set([start])
    moves = 0

    while queue:
        for _ in range(len(queue)):
            x, y, piece = queue.popleft()
            if (x, y) == end:
                return moves

            moves_list = get_moves(x, y, n, piece)
            for new_x, new_y in moves_list:
                if board[new_x][new_y] == 'K':
                    new_piece = 'K'
                elif board[new_x][new_y] == 'G':
                    new_piece = 'G'
                else:
                    new_piece = piece

                if ((new_x, new_y, new_piece)) not in visited:
                    visited.add((new_x, new_y, new_piece))
                    queue.append((new_x, new_y, new_piece))

        moves += 1
    return -1
n = int(input())
board = [list(input().strip()) for _ in range(n)]
result = min_moves_to_destination(n, board)
print(result)