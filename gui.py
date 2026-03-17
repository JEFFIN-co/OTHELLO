import pygame
import sys
import math
from board import *
from ai import alpha_beta

# colors
GREEN = (0,128,0)
BLACK_COLOR = (0,0,0)
WHITE_COLOR = (255,255,255)
GRID = (0,70,0)

SQUARE = 80
WIDTH = SIZE * SQUARE
HEIGHT = SIZE * SQUARE

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Othello AI - Alpha Beta Pruning")

font = pygame.font.SysFont("arial", 24)

def draw_board(board):
    for x in range(SIZE):
        for y in range(SIZE):

            pygame.draw.rect(screen, GREEN,
                             (y*SQUARE, x*SQUARE, SQUARE, SQUARE))

            pygame.draw.rect(screen, GRID,
                             (y*SQUARE, x*SQUARE, SQUARE, SQUARE), 2)

            if board[x][y] == BLACK:
                pygame.draw.circle(screen, BLACK_COLOR,
                    (y*SQUARE+SQUARE//2, x*SQUARE+SQUARE//2), 30)

            elif board[x][y] == WHITE:
                pygame.draw.circle(screen, WHITE_COLOR,
                    (y*SQUARE+SQUARE//2, x*SQUARE+SQUARE//2), 30)

def show_turn(text):
    label = font.render(text, True, (255,255,0))
    screen.blit(label, (10,10))

def get_square(pos):
    x = pos[1] // SQUARE
    y = pos[0] // SQUARE
    return x,y

def game_over(board):
    # game ends when neither player has a legal move
    if len(valid_moves(board, BLACK)) == 0 and len(valid_moves(board, WHITE)) == 0:
        return True
    return False


def game_loop():

    board = create_board()
    current = WHITE  # player

    running = True

    while running:

        screen.fill(GREEN)
        draw_board(board)

        if current == WHITE:
            show_turn("Your Turn (White)")
        else:
            show_turn("AI Thinking...")

        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # player click
            if event.type == pygame.MOUSEBUTTONDOWN and current == WHITE:
                pos = pygame.mouse.get_pos()
                x,y = get_square(pos)

                if (x,y) in valid_moves(board, WHITE):
                    make_move(board, WHITE, x, y)
                    current = BLACK

        # AI move
        if current == BLACK and not game_over(board):

            pygame.display.update()
            pygame.time.wait(500)

            score, move = alpha_beta(board, 4, -math.inf, math.inf, True)

            if move:
                make_move(board, BLACK, move[0], move[1])

            current = WHITE

        # check game over
        if game_over(board):
            black = (board == BLACK).sum()
            white = (board == WHITE).sum()

            if black > white:
                text = "AI Wins!"
            elif white > black:
                text = "You Win!"
            else:
                text = "Draw!"

            label = font.render(text, True, (255,0,0))
            screen.blit(label, (WIDTH//2 - 80, HEIGHT//2))
            pygame.display.update()
            pygame.time.wait(4000)
            running = False

    pygame.quit()

if __name__ == "__main__":
    game_loop()
