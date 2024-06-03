import pygame
from pygame.locals import *
import words
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
YELLOW = (255, 255, 0)
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

#Var for input_letter
#current_x_pos = 120
#current_y_pos = 70
key_pressed = ""
letter_font = pygame.font.SysFont("arial", 70, True, False)
#letter_size = 75


#Var for guessing word
total_guess = 0
guess_word = []
guess_word_string = ""

answer = "final"
#answer = random.choice()

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
		self.text_rect = self.text_surface.get_rect(center=(x_pos + 40, y_pos + 40))
	def draw(self):
		pygame.draw.rect(screen, self.bg_color, [self.x, self.y, tile_size, tile_size])
		pygame.draw.rect(screen, BLACK, [self.x, self.y, tile_size, tile_size], 4)
		screen.blit(self.text_surface, self.text_rect)
	def delete(self):
		pygame.draw.rect(screen, Darkgray, [self.x, self.y, tile_size, tile_size]) 		
		pygame.draw.rect(screen, BLACK, [self.x, self.y, tile_size, tile_size], 4)

def create_letter():
	global default_x, guess_word_string
	new_letter = Letter(key_pressed, default_x, default_y)
	new_letter.draw()
	default_x += tile_size + tile_spacing_x
	guess_word_string += key_pressed
	guess_word.append(new_letter)

def delete_letter():
	global default_x, guess_word_string
	guess_word_string = guess_word_string[:-1]
	guess_word[-1].delete()
	guess_word.pop()
	default_x -= tile_size + tile_spacing_x

def guess_check(guessed_word):
	global guess_word_string
	for i in range(5):
		guessed_letter = guessed_word[i].letter.lower()
		if guessed_letter in answer:
			if guessed_letter == answer[i]:
				guessed_word[i].bg_color = GREEN
			else:
				guessed_word[i].bg_color = YELLOW
		else:
			guessed_word[i].bg_color = Dimgray
		guessed_word[i].text_color = WHITE
		guessed_word[i].draw()
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
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RETURN:
				if len(guess_word_string) == 5 and guess_word_string.lower() in words.WORDS:
						guess_check(guess_word)
						default_y += 90
						guess_word_string = ""
						default_x = 80
			elif event.key == pygame.K_BACKSPACE:
				if len(guess_word_string) > 0:
					delete_letter()
			else:
				key_pressed = event.unicode.upper()
				if key_pressed in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
					if len(guess_word_string) < 5:
						create_letter()
	pygame.display.flip()



#Quit Code
pygame.quit()
