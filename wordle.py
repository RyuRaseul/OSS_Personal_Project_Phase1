import pygame
from pygame.locals import *
from words import *
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
tile_size = 80
tile_spacing_x = 10
tile_spacing_y = 10

#Var for guessing word
total_guess = 0
guess_word = []
guess_word_string = ""
key_pressed = ""


class Tile:
	def __init__(self, bg_color, x_pos, y_pos):
		self.x = x_pos
		self.y = y_pos
		self.bg_color = bg_color
	
	def draw(self):
		pygame.draw.rect(screen, self.bg_color, [self.x, self.y, tile_size, tile_size], 4)

class Letter:
	def __init__(self, letter, x_pos, y_pos):
		self.bg_color = WHITE
		self.text_color = BLACK
		self.x = x_pos
		self.y = y_pos
		self.letter = letter
		self.text_surface = letter_font.render(self.letter, True, self.text_color)
		self.text_rect = self.text_surface.get_rect(center=(x_pos +  tile_width/2, y_pos + tile_height/2))
	def draw(self):
		pygame.draw.rect(screen, self.bg_color, [self.x, self.y, letter_size, letter_size], 4)
		screen.blit(self.text_surface, self.text_rect)

#Creating Rect OBJ for word tile
for i in range(6):
	for j in range(5):
		new_tile = Tile(BLACK, default_x + j*(tile_spacing_x + tile_size), default_y + i*(tile_spacing_y+ tile_size))
		new_tile.draw()
done = False

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	pygame.display.flip()



#Quit Code
pygame.quit()
