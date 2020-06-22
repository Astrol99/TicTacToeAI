#!/usr/bin/env python3
import pygame

WIDTH = 800
HEIGHT = 800
SIZE = WIDTH / 3
FPS = 30

WHITE = (255, 255, 255)

# 0 = Empty
# 1 = X -> Player
# 2 = O -> AI

grid = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

## initialize pygame and create window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TicTacToe AI")
clock = pygame.time.Clock()     ## For syncing the FPS

# Create TicTacToe Grid
for i in range(1, 4):

    XPoint = int(SIZE * i)
    YPoint = int(SIZE * i)

    # Vertical Lines
    pygame.draw.line(screen, WHITE, (XPoint,0), (XPoint, HEIGHT), 10)
    # Horizontal Lines
    pygame.draw.line(screen, WHITE, (0, YPoint), (WIDTH, YPoint), 10)

def changeState(pos: tuple, state: int):
    # Check if grid is empty
    if grid[pos[0]][pos[1]] == 0:
        grid[pos[0]][pos[1]] = state

## Game loop
running = True
while running:
    
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            pos = (int(pos[0] / SIZE), int(pos[1] / SIZE))
            changeState(pos, 1)
            print(grid)

    pygame.display.flip()       

pygame.quit()
