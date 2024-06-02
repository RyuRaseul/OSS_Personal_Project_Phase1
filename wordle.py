import pygame
from pygame.locals import *

#Pygame Initailize
pygame.init()

#Screen Setting
size = [800, 600]
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


done = False

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	pygame.display.flip()

#Quit Code
pygame.quit()
