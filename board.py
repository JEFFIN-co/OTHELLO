import numpy as np

SIZE = 8
EMPTY = 0
BLACK = 1   # AI
WHITE = -1  # Human

def create_board():
    board = np.zeros((SIZE, SIZE), dtype=int)
    board[3][3] = WHITE
    board[3][4] = BLACK
    board[4][3] = BLACK
    board[4][4] = WHITE
    return board

def on_board(x, y):
    return 0 <= x < SIZE and 0 <= y < SIZE

directions = [
    (0,1),(1,0),(0,-1),(-1,0),
    (1,1),(1,-1),(-1,1),(-1,-1)
]

def valid_moves(board, player):
    moves = []
    for x in range(SIZE):
        for y in range(SIZE):
            if board[x][y] != EMPTY:
                continue
            if is_valid_move(board, player, x, y):
                moves.append((x,y))
    return moves

def is_valid_move(board, player, x, y):
    if board[x][y] != EMPTY:
        return False

    opponent = -player
    for dx, dy in directions:
        nx, ny = x+dx, y+dy
        found_opponent = False

        while on_board(nx, ny) and board[nx][ny] == opponent:
            nx += dx
            ny += dy
            found_opponent = True

        if found_opponent and on_board(nx, ny) and board[nx][ny] == player:
            return True

    return False

def make_move(board, player, x, y):
    board[x][y] = player
    opponent = -player

    for dx, dy in directions:
        nx, ny = x+dx, y+dy
        flips = []

        while on_board(nx, ny) and board[nx][ny] == opponent:
            flips.append((nx,ny))
            nx += dx
            ny += dy

        if on_board(nx, ny) and board[nx][ny] == player:
            for fx, fy in flips:
                board[fx][fy] = player

def print_board(board):
    symbols = {1:'B', -1:'W', 0:'.'}
    for row in board:
        print(" ".join(symbols[x] for x in row))
        
def game_over(board):
    # game ends when neither player has a legal move
    if len(valid_moves(board, BLACK)) == 0 and len(valid_moves(board, WHITE)) == 0:
        return True
    return False