import pygame
from pygame.locals import *

#Pygame Initailize
pygame.init()

#Screen Setting
size = [600, 900]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Wordle")

#Color Var
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
Dimgray = (105, 105, 105)
Darkgray = (169, 169, 169)

#Setting Initial Screen BackgoundColor
screen.fill(Darkgray)

#Var for word_tile
default_x = 80
default_y = 30
tile_width = 80
tile_height = 80
tile_spacing_x = 10
tile_spacing_y = 10

#Creating Rect OBJ for word tile
for i in range(6):
	for j in range(5):
		pygame.draw.rect(screen, Dimgray, [default_x + j *(tile_width + tile_spacing_x), default_y + i*(tile_height + tile_spacing_y), tile_width, tile_height], 4)	

done = False

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	pygame.display.flip()



#Quit Code
pygame.quit()
