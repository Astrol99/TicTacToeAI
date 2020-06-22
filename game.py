#!/usr/bin/env python3
import pygame

WIDTH = 800
HEIGHT = 600
FPS = 30

# Define Colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

## initialize pygame and create window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TicTacToe AI")
clock = pygame.time.Clock()     ## For syncing the FPS

# Create TicTacToe Grid


## Game loop
running = True
while running:

    #1 Process input/even
    clock.tick(FPS)     ## will make the loop run at the same speed all the time
    for event in pygame.event.get():        # gets all the events which have occured till now and keeps tab of them.
        ## listening for the the X button at the top
        if event.type == pygame.QUIT:
            running = False


    #3 Draw/render
    screen.fill(BLACK)

    ########################

    ### Your code comes here

    ########################

    ## Done after drawing everything to the screen
    pygame.display.flip()       

pygame.quit()
