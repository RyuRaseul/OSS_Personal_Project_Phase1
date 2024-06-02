import pygame
from pygame.locals import *

#Pygame Initailize
pygame.init()

#Screen Setting
size = [800, 600]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Wordle")

done = False

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	pygame.display.flip()

#Quit Code
pygame.quit()
