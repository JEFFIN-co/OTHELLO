from board import *
from ai import *
import math

board = create_board()
current = WHITE  # human first

while not game_over(board):

    print_board(board)

    if current == WHITE:
        print("Your move: row col")
        x, y = map(int, input().split())

        if (x,y) in valid_moves(board, WHITE):
            make_move(board, WHITE, x, y)
            current = BLACK
        else:
            print("Invalid move!")

    else:
        print("AI thinking...")
        score, move = alpha_beta(board, 4, -math.inf, math.inf, True)

        if move:
            make_move(board, BLACK, move[0], move[1])
        current = WHITE

print_board(board)
print("Game Over")
