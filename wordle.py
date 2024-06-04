import pygame
from pygame.locals import *
import words
import random
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
default_y = 70
tile_size = 80
tile_spacing_x = 10
tile_spacing_y = 10

#Var for input_letter
#current_x_pos = 120
#current_y_pos = 70
key_pressed = ""
letter_font = pygame.font.SysFont("arial", 70, True, False)
key_font = pygame.font.SysFont("arial", 40, True, False)
#letter_size = 75

#Keyboard List
keyboard_keys = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]
keys = []
keyboard_x = 15
keyboard_y = 630

#Var for guessing word
total_guess = 0
guess_word = []
guess_word_string = ""

#Var for Hint Button
hint_x = 460
hint_y = 20
hint_count = 5
hint_font = pygame.font.SysFont("arial", 25)
#Var for distinguish USED(YELLOW, GREEN), UNUSED(GRAY), UNKNOWN(WHITE)
USED_LIST = ""
UNUSED_LIST = ""
UNKNOWN_LIST = "QWERTYUIOPASDFGHJKLZXCVBNM"

#answer = "final"
#random.seed(5)
answer = random.choice(words.WORDS)


#Var for game_result "Win", "Lose", ""
result = ""


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

class Keyboard:
	def __init__(self, key, x_pos, y_pos):
		self.x = x_pos
		self.y = y_pos
		self.key = key
		self.bg_color = WHITE
		self.key_color = BLACK
		self.key_surface = key_font.render(self.key, True, self.key_color)
		self.key_rect = self.key_surface.get_rect(center = (self.x + 24, self.y+33))
	def draw(self):
		pygame.draw.rect(screen, self.bg_color, [self.x, self.y, 48, 70])
		screen.blit(self.key_surface, self.key_rect)

def create_letter():
	global default_x, guess_word_string
	create_x_idx = len(guess_word)%5
	create_y_idx = len(guess_word)//5
	new_letter = Letter(key_pressed, default_x + create_x_idx*(tile_spacing_x + tile_size), default_y + create_y_idx*(tile_spacing_y + tile_size))
	new_letter.draw()
	#default_x += tile_size + tile_spacing_x
	guess_word_string += key_pressed
	guess_word.append(new_letter)

def delete_letter():
	global default_x, guess_word_string
	guess_word_string = guess_word_string[:-1]
	guess_word[-1].delete()
	guess_word.pop()
	#default_x -= tile_size + tile_spacing_x

def guess_check(guessed_word):
	global guess_word_string, total_guess, result, USED_LIST, UNUSED_LIST, UNKNOWN_LIST
	check_result = True
	for i in range(5):
		check_idx = i + 5*total_guess
		guessed_letter = guessed_word[check_idx].letter.lower()
		if guessed_letter in answer:
			if guessed_letter == answer[i]:
				guessed_word[check_idx].bg_color = GREEN
				if guessed_letter.upper() not in USED_LIST:
					USED_LIST += guessed_letter.upper()
					UNKNOWN_LIST = UNKNOWN_LIST.replace(guessed_letter.upper(), '')
				for letter in keys:
					if letter.key == guessed_letter.upper():
						letter.bg_color = GREEN
						letter.draw()
				if check_result == True:
					result = "Win"
			else:
				guessed_word[check_idx].bg_color = YELLOW
				if guessed_letter.upper() not in USED_LIST:
					USED_LIST += guessed_letter.upper()
					UNKNOWN_LIST = UNKNOWN_LIST.replace(guessed_letter.upper(), '')
				for letter in keys:
					if letter.key == guessed_letter.upper():
						letter.bg_color = YELLOW
						letter.draw()
				result = ""
				check_result = False
		else:
			guessed_word[check_idx].bg_color = Dimgray
			if guessed_letter.upper() not in UNUSED_LIST:
				UNUSED_LIST += guessed_letter.upper()
				UNKNOWN_LIST = UNKNOWN_LIST.replace(guessed_letter.upper(), '')
			for letter in keys:
					if letter.key == guessed_letter.upper():
						letter.bg_color = Dimgray
						letter.draw()
			result = ""
			check_result = False
		guessed_word[check_idx].text_color = WHITE
		guessed_word[check_idx].draw()

	total_guess += 1
	guess_word_string = ""
	if total_guess == 6 and result == "":
		result = "Lose"

#Creating Rect OBJ for word tile
def make_tiles():
	for i in range(6):
		for j in range(5):
			new_tile = Tile(BLACK, default_x + j*(tile_spacing_x + tile_size), default_y + i*(tile_spacing_y+ tile_size))
			new_tile.draw()

for i in range(3):
	for letter in keyboard_keys[i]:
		new_key = Keyboard(letter, keyboard_x, keyboard_y)
		keys.append(new_key)
		new_key.draw()	
		keyboard_x += 58
	keyboard_y += 90
	if i == 0:
		keyboard_x = 44
	elif i == 1:
		keyboard_x = 102

pygame.draw.rect(screen, BLACK, (hint_x, hint_y, 100, 35), 4)
hint_text = hint_font.render(f"HINT: {hint_count}", True, WHITE)
hint_rect = hint_text.get_rect(center = (510, 35))
screen.blit(hint_text, hint_rect)

def game_end():
	pygame.draw.rect(screen, Darkgray, (0, 600, 600, 300))
	end_message_font = pygame.font.SysFont("arial", 40)
	end_message_text = end_message_font.render("Press ENTER Key to Restart!", True, BLACK)
	end_message_rect = end_message_text.get_rect(center = (size[0]/2, 760))
	answer_font = pygame.font.SysFont("arial", 40)
	answer_text = answer_font.render(f"Answer Word was {answer.upper()}!", True, BLACK)
	answer_rect = answer_text.get_rect(center = (size[0]/2, 710))
	screen.blit(answer_text, answer_rect)
	screen.blit(end_message_text, end_message_rect)

def restart():
	global answer, total_guess, guess_word, result, hint_text, hint_rect
	screen.fill(Darkgray)
	make_tiles()
	answer = random.choice(words.WORDS)
	total_guess = 0
	guess_word = []
	result = ""
	USED_LIST = ""
	UNUSED_LIST = ""
	UNKNOWN_LIST = "QWERTYUIOPASDFGHJKLZXCVBNM"
	pygame.draw.rect(screen, Darkgray, (hint_x, hint_y, 100, 35))
	pygame.draw.rect(screen, BLACK, (hint_x, hint_y, 100, 35), 4)
	hint_text = hint_font.render(f"HINT: {hint_count}", True, WHITE)
	hint_rect = hint_text.get_rect(center = (510, 35))
	screen.blit(hint_text, hint_rect)


	for key_tile in keys:
		key_tile.bg_color = WHITE
		key_tile.draw()

def Hint():
	global USED_LIST, UNUSED_LIST, UNKNOWN_LIST, hint_text, hint_rect
	hint_letter = random.choice(UNKNOWN_LIST)
	if hint_letter.lower() in answer:
		for letter in keys:
			if letter.key == hint_letter:
				letter.bg_color = YELLOW
				letter.draw()
				USED_LIST += hint_letter
				UNKNOWN_LIST = UNKNOWN_LIST.replace(hint_letter, '')
	else:
		for letter in keys:
			if letter.key == hint_letter:
				letter.bg_color = Dimgray
				letter.draw()
				UNUSED_LIST += hint_letter
				UNKNOWN_LIST = UNKNOWN_LIST.replace(hint_letter, '')
	pygame.draw.rect(screen, Darkgray, (hint_x, hint_y, 100, 35))
	pygame.draw.rect(screen, BLACK, (hint_x, hint_y, 100, 35), 4)
	hint_text = hint_font.render(f"HINT: {hint_count}", True, WHITE)
	hint_rect = hint_text.get_rect(center = (510, 35))
	screen.blit(hint_text, hint_rect)



done = False
make_tiles()

while not done:
	if result != "":
		game_end()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RETURN:
				if result != "":
					restart()
				elif len(guess_word_string) == 5 and guess_word_string.lower() in words.WORDS:
						guess_check(guess_word)
						#default_y += 90
						#default_x = 80
			elif event.key == pygame.K_BACKSPACE:
				if len(guess_word_string) > 0:
					delete_letter()
			else:
				key_pressed = event.unicode.upper()
				if key_pressed in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" and key_pressed != "" and result == "":
					if len(guess_word_string) < 5:
						create_letter()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_pos = pygame.mouse.get_pos()
			if hint_count > 0 and (460 <= mouse_pos[0] <= 560 and 20 <= mouse_pos[1] <= 55):
				hint_count -= 1	
				Hint()
	pygame.display.flip()



#Quit Code
pygame.quit()
