import math
import numpy as np
from board import *

def evaluate(board):
    # heuristic evaluation
    black = np.sum(board == BLACK)
    white = np.sum(board == WHITE)

    # corner bonus (VERY IMPORTANT in Othello)
    corners = [(0,0),(0,7),(7,0),(7,7)]
    corner_score = 0

    for x,y in corners:
        if board[x][y] == BLACK:
            corner_score += 25
        elif board[x][y] == WHITE:
            corner_score -= 25

    return (black - white) + corner_score



def alpha_beta(board, depth, alpha, beta, maximizing):

    if depth == 0 or game_over(board):
        return evaluate(board), None

    player = BLACK if maximizing else WHITE
    moves = valid_moves(board, player)

    if not moves:
        return alpha_beta(board, depth-1, alpha, beta, not maximizing)

    best_move = None

    if maximizing:
        max_eval = -math.inf
        for move in moves:
            new_board = board.copy()
            make_move(new_board, player, move[0], move[1])
            eval, _ = alpha_beta(new_board, depth-1, alpha, beta, False)

            if eval > max_eval:
                max_eval = eval
                best_move = move

            alpha = max(alpha, eval)
            if beta <= alpha:
                break

        return max_eval, best_move

    else:
        min_eval = math.inf
        for move in moves:
            new_board = board.copy()
            make_move(new_board, player, move[0], move[1])
            eval, _ = alpha_beta(new_board, depth-1, alpha, beta, True)

            if eval < min_eval:
                min_eval = eval
                best_move = move

            beta = min(beta, eval)
            if beta <= alpha:
                break

        return min_eval, best_move
