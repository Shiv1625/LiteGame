import pygame
import os

import grid

os.environ["SDL_VIDEO-CENTERED"]='1'


#what size of screen you want create here
width,height = 800,800
size = (width,height)

pygame.init()
pygame.display.set_caption("Life Game")
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


black = (0,0,0)
blue = (0,14,71)
white = (255,255,255)

scaler = 10   #size of box
offset = 1

Grid = grid.Grid(width, height, scaler, offset)
Grid.random2D_array()

run = True

while run:
    
    clock.tick(60)
    screen.fill(blue)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run == False
            pygame.quit()
            


    
    Grid.Game(off_color= white, on_color= black, surface= screen)

    pygame.display.update()







