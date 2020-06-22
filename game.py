#!/usr/bin/env python3
import pygame

WIDTH = 800
HEIGHT = 800
FPS = 30

WHITE = (255, 255, 255)

## initialize pygame and create window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TicTacToe AI")
clock = pygame.time.Clock()     ## For syncing the FPS

# Create TicTacToe Grid
for i in range(1, 4):
	XPoint = WIDTH/3 * i
	YPoint = HEIGHT/3 * i

	# Vertical Lines
	pygame.draw.line(screen, WHITE, (XPoint,0), (XPoint, HEIGHT), 10)
	# Horizontal Lines
	pygame.draw.line(screen, WHITE, (0, YPoint), (WIDTH, YPoint), 10)

## Game loop
running = True
while running:

    #1 Process input/even
    clock.tick(FPS)     ## will make the loop run at the same speed all the time
    for event in pygame.event.get():        # gets all the events which have occured till now and keeps tab of them.
        ## listening for the the X button at the top
        if event.type == pygame.QUIT:
            running = False

    ########################

    ### Your code comes here

    ########################

    ## Done after drawing everything to the screen
    pygame.display.flip()       

pygame.quit()
