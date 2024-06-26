import pygame
from pygame.locals import *
import words
import random
import datetime
#############################################
################## PHASE 2 ##################
#############################################
import os
import json

#출석 체크하는 json 파일 읽고 불러오기
attendance_file = "attendance.json"

#############################################
################## PHASE 2 ##################
#############################################

#Pygame Initailize
pygame.init()

#Screen Settingi
screen_x = 600
screen_y = 800
size = [screen_x, screen_y]
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
Lightblue = (232,252,252)

#Setting Initial Screen BackgoundColor
screen.fill(Darkgray)	

#Var for word_tile
default_x = 105
default_y = 70
tile_spacing_x = 10
tile_spacing_y = 10
tile_size = 70

#Var for input_letter
key_pressed = ""
letter_font = pygame.font.SysFont("arial", 60, True, False)
key_font = pygame.font.SysFont("arial", 40, True, False)

#Keyboard List
keyboard_keys = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]
keys = []
keyboard_x = 15
keyboard_y = 550

#Var for guessing word
total_guess = 0
guess_word = []
guess_word_string = ""

#Var for Hint Button
hint_x = 460
hint_y = 20
hint_count = 5
hint_font = pygame.font.SysFont("arial", 25)

#Var for Mode Selection
mode_font = pygame.font.SysFont("arial", 40)
daily_text = mode_font.render("Daily MODE", True, 40)
daily_rect = daily_text.get_rect(center = (300, 250))
inf_text = mode_font.render("INF Mode", True, 40)
inf_rect = inf_text.get_rect(center = (300, 450))
#############################################
################## PHASE 2 ##################
#############################################
weekly_text = mode_font.render("Weekly Attendance", True, 40)
weekly_rect = weekly_text.get_rect(center = (300, 650))

#############################################
################## PHASE 2 ##################
#############################################
daily_seed = datetime.datetime.today().strftime("%Y:%m:%d")


#Var for distinguish USED(YELLOW, GREEN), UNUSED(GRAY), UNKNOWN(WHITE)
USED_LIST = ""
UNUSED_LIST = ""
UNKNOWN_LIST = "QWERTYUIOPASDFGHJKLZXCVBNM"

#아이콘 이미지를 위한 변수들
check_icon = pygame.image.load("./assets/check.png")
check_icon = pygame.transform.scale(check_icon, (50, 50))
cross_icon = pygame.image.load("./assets/cross.png")
cross_icon = pygame.transform.scale(cross_icon, (50, 50))
crown_icon = pygame.image.load("./assets/crown.png")
crown_icon = pygame.transform.scale(crown_icon, (50, 50))
fire_icon = pygame.image.load("./assets/fire.png")
fire_icon = pygame.transform.scale(fire_icon, (50, 50))

answer = random.choice(words.WORDS)


#Var for game_result "WIN", "LOSE", "MODE", ""
result = "MODE"
mode = ""
end = ["WIN", "LOSE"]
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
		self.text_rect = self.text_surface.get_rect(center=(x_pos + tile_size//2, y_pos + tile_size//2))
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
		#############################################
		################## PHASE 2 ##################
		if self.key == "ENTER":
			pygame.draw.rect(screen, self.bg_color, [self.x, self.y, 76, 70])
			key_font = pygame.font.SysFont("arial", 20, True, False)
			self.key_surface = key_font.render(self.key, True, self.key_color)
			self.key_rect = self.key_surface.get_rect(center = (self.x + 38, self.y + 35))
			screen.blit(self.key_surface, self.key_rect)
		elif self.key == "<=":
			pygame.draw.rect(screen, self.bg_color, [self.x, self.y, 76, 70])
			self.key_rect = self.key_surface.get_rect(center = (self.x + 38, self.y + 35))
			screen.blit(self.key_surface, self.key_rect)
		################## PHASE 2 ##################
		#############################################
		else:
			pygame.draw.rect(screen, self.bg_color, [self.x, self.y, 48, 70])
			screen.blit(self.key_surface, self.key_rect)

def create_letter(input_key):
	global default_x, guess_word_string
	create_x_idx = len(guess_word)%5
	create_y_idx = len(guess_word)//5
	new_letter = Letter(input_key, default_x + create_x_idx*(tile_spacing_x + tile_size), default_y + create_y_idx*(tile_spacing_y + tile_size))
	new_letter.draw()
	#default_x += tile_size + tile_spacing_x
	guess_word_string += input_key
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
					result = "WIN"
			else:
				guessed_word[check_idx].bg_color = YELLOW
				if guessed_letter.upper() not in USED_LIST:
					USED_LIST += guessed_letter.upper()
					UNKNOWN_LIST = UNKNOWN_LIST.replace(guessed_letter.upper(), '')
				for letter in keys:
					if letter.key == guessed_letter.upper():
						if letter.bg_color == Dimgray or letter.bg_color == WHITE:
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
		result = "LOSE"

#Creating Rect OBJ for word tile
def make_tiles():
	for i in range(6):
		for j in range(5):
			new_tile = Tile(BLACK, default_x + j*(tile_spacing_x + tile_size), default_y + i*(tile_spacing_y+ tile_size))
			new_tile.draw()

for i in range(4):
	#############################################
	################## PHASE 2 ##################
	if i == 3:
		keyboard_y -= 85
		new_key = Keyboard("<=", keyboard_x, keyboard_y)
		keys.append(new_key)
		new_key.draw()
		keyboard_x = 15
		new_key = Keyboard("ENTER", keyboard_x, keyboard_y)
		keys.append(new_key)
		new_key.draw()
	################## PHASE 2 ##################
	#############################################
	else:
		for letter in keyboard_keys[i]:
			new_key = Keyboard(letter, keyboard_x, keyboard_y)
			keys.append(new_key)
			new_key.draw()	
			keyboard_x += 58
		keyboard_y += 85
		if i == 0:
			keyboard_x = 44
		elif i == 1:
			keyboard_x = 102

#############################################
################## PHASE 2 ##################
#############################################
solved_days = 0

#문제 맞힌 총 일수 계산
def calculate_solved(attendance):
	solved = 0
	for state in attendance["attendance"]:
		if state == "WIN":
			solved += 1
	return solved

def initialize_attendance():
    if os.path.exists(attendance_file):
        with open(attendance_file, 'r') as file:
            data = json.load(file)
    else:
        data = {"last_date": "", "attendance": [False] * 7}
        write_attendance(data)
    return data

def write_attendance(data):
    with open(attendance_file, 'w') as file:
        json.dump(data, file)

#한 주 지나면 출석 초기화
def reset_attendance(data):
	current_date = datetime.datetime.today()
	last_date = datetime.datetime.strptime(data["last_date"], "%Y-%m-%d")
	print(current_date, last_date)
	if (current_date - last_date).days >= 7:
		data = {"last_date": "", "attendance": [False] * 7}
		return data
	return False

#오늘 출석 체크
def check_attendance():
	global solved_days
	current_weekday = datetime.datetime.today().weekday()
	data = initialize_attendance()
	data = reset_attendance(data) or data
	if data["attendance"][current_weekday] == False:
		data["attendance"][current_weekday] = True
		current_date = datetime.datetime.today().strftime("%Y-%m-%d")
		data["last_date"] = current_date
	write_attendance(data)
	solved_days = calculate_solved(data)
	return data

attendance_data = check_attendance()

#문제 맞혔으면 업데이트 
def update_attendance():
	global attendance_data, solved_days
	attendance_data["attendance"][datetime.datetime.today().weekday()] = "WIN"
	write_attendance(attendance_data)
	solved_days = calculate_solved(attendance_data)


check_attendance()
#############################################
################## PHASE 2 ##################
#############################################

pygame.draw.rect(screen, BLACK, (hint_x, hint_y, 100, 35), 4)
hint_text = hint_font.render(f"HINT: {hint_count}", True, WHITE)
hint_rect = hint_text.get_rect(center = (510, 35))
screen.blit(hint_text, hint_rect)

def game_end():
	pygame.draw.rect(screen, Darkgray, (0, 550, 600, 300))
	end_message_font = pygame.font.SysFont("arial", 40)
	end_message_text = end_message_font.render("Press ENTER Key to Restart!", True, BLACK)
	end_message_rect = end_message_text.get_rect(center = (size[0]/2, 690))
	answer_font = pygame.font.SysFont("arial", 40)
	answer_text = answer_font.render(f"Answer Word was {answer.upper()}!", True, BLACK)
	answer_rect = answer_text.get_rect(center = (size[0]/2, 640))
	screen.blit(answer_text, answer_rect)
	screen.blit(end_message_text, end_message_rect)

def game_start():
	global answer, total_guess, guess_word, result, mode, hint_text, hint_rect, hint_count, USED_LIST, UNUSED_LIST, UNKNOWN_LIST
	screen.fill(Darkgray)
	make_tiles()
	total_guess = 0
	guess_word = []
	result = ""
	if mode == "DAILY":
		random.seed(daily_seed)
		answer = random.choice(words.WORDS)
	else:
		random.seed()
		answer = random.choice(words.WORDS)
	USED_LIST = ""
	UNUSED_LIST = ""
	UNKNOWN_LIST = "QWERTYUIOPASDFGHJKLZXCVBNM"
	hint_count = 5
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

def Mode_Select():
	screen.fill(WHITE)
	pygame.draw.rect(screen, BLACK, (150, 200, 300, 100), 4)
	pygame.draw.rect(screen, BLACK, (150, 400, 300, 100), 4)
	#############################################
	################## PHASE 2 ##################
	#############################################
	pygame.draw.rect(screen, BLACK, (100, 600, 400, 100), 4)
	screen.blit(daily_text, daily_rect)
	screen.blit(inf_text, inf_rect)
	screen.blit(weekly_text, weekly_rect)

	#############################################
	################## PHASE 2 ##################
	#############################################


#############################################
################## PHASE 2 ##################
#############################################
def Weekly_Attendance():
    global attendance_data

    def draw_text(text, font, color, center):
        rendered_text = font.render(text, True, color)
        text_rect = rendered_text.get_rect(center=center)
        screen.blit(rendered_text, text_rect)

    def draw_icon(icon, x, y):
        screen.blit(icon, (x, y))

    def draw_rectangle(color, x, y, width, height, thickness):
        pygame.draw.rect(screen, color, (x, y, width, height), thickness)

    header_font = pygame.font.SysFont("arial", 40)
    day_font = pygame.font.SysFont("arial", 20)
    solved_font = pygame.font.SysFont("arial", 30)
    try_font = pygame.font.SysFont("arial", 40, bold=True)

    #헤더 텍스트 그리기 
    draw_text("WEEKLY ATTENDANCE", header_font, BLACK, (screen_x // 2, 130))

    day_labels = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    attendance = attendance_data["attendance"]

    # 라벨, 체크 아이콘, 엑스 아이콘, 왕관 아이콘 그리기
    for i in range(7):
        x_pos = 75 + 70 * i
        draw_rectangle(BLACK, x_pos, 200, 50, 50, 2)
        draw_text(day_labels[i], day_font, BLACK, (x_pos + 25, 270))
        if attendance[i] == True:
            draw_icon(check_icon, x_pos, 200)
        elif attendance[i] == False:
            draw_icon(cross_icon, x_pos, 200)
        else:
            draw_icon(crown_icon, x_pos, 200)

    # 푼 문제 수 그리기
    draw_text(f"{solved_days} days of solving!!!", solved_font, BLACK, (screen_x // 2, 320))
    solved_rect = solved_font.render(f"{solved_days} days of solving!!!", True, BLACK).get_rect(center=(screen_x // 2, 320))
    screen.blit(fire_icon, (solved_rect.right + 10, solved_rect.top - 10))
    screen.blit(fire_icon, (solved_rect.left - 70, solved_rect.top - 10))

    draw_text("START GAME?", try_font, BLACK, (300, 420))

    # 버튼 그리기
    draw_rectangle(BLACK, 150, 480, 300, 80, 4)
    draw_rectangle(BLACK, 150, 580, 300, 80, 4)
    screen.blit(daily_text, daily_text.get_rect(center=(300, 520)))
    screen.blit(inf_text, inf_text.get_rect(center=(300, 620)))


#############################################
################## PHASE 2 ##################
#############################################		

def check_keyboard_click(mouse_x, key_line):
	if key_line == 0:
		mouse_x -= 15
		for i in range(len(keyboard_keys[0])):
			if 58*i <= mouse_x <= 58*i + 48:
				clicked_letter = keys[i]		  			
				create_letter(clicked_letter.key)
	elif key_line == 1:
		mouse_x -=44
		for i in range(len(keyboard_keys[1])):
			if 58*i <= mouse_x <= 58*i + 48:
				clicked_letter = keys[i + len(keyboard_keys[0])]
				create_letter(clicked_letter.key)
	else:
		mouse_x -= 102
		for i in range(len(keyboard_keys[2])):
			if 58*i <= mouse_x <= 58*i + 48:
				clicked_letter = keys[i + len(keyboard_keys[1]) + len(keyboard_keys[0])]
				create_letter(clicked_letter.key)
		
done = False
## PHASE 2
game_win = False
while not done:
	#############################################
	################## PHASE 2 ##################
	if mode == "WEEKLY":
		screen.fill(WHITE)
		Weekly_Attendance()
	elif result == "MODE":
		screen.fill(WHITE)
		Mode_Select()
	elif result in end:
		if result == "WIN" and game_win == False:
			update_attendance()
			game_win = True
		game_end()
	################## PHASE 2 ##################
	#############################################
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RETURN:
				if result != "":
					if mode == "INF":
						game_start()
					else:
						result = "MODE"
						mode = ""
				elif len(guess_word_string) == 5 and guess_word_string.lower() in words.WORDS:
						guess_check(guess_word)
			elif event.key == pygame.K_BACKSPACE:
				if len(guess_word_string) > 0:
					delete_letter()
			else:
				key_pressed = event.unicode.upper()
				if key_pressed in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" and key_pressed != "" and result == "":
					if len(guess_word_string) < 5:
						create_letter(key_pressed)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_pos = pygame.mouse.get_pos()
			if result == "MODE" and mode == "":
					#############################################
					################## PHASE 2 ##################
					#############################################
				if (100 <= mouse_pos[0] <= 500) and (600 <= mouse_pos[1] <= 700):
					mode = "WEEKLY"
				elif mode != "WEEKLY" and (150 <= mouse_pos[0] <= 450):
					#######################x######################
					################## PHASE 2 ##################
					#############################################
					if (200 <= mouse_pos[1] <= 300):
						mode = "DAILY"
						game_start()								
					elif (400 <= mouse_pos[1] <=500):
						mode = "INF"
						game_start()
			elif result == "MODE" and mode == "WEEKLY":
				if (150 <= mouse_pos[0] <= 450) and (480 <= mouse_pos[1] <= 560):
					mode = "DAILY"
					game_start()
				elif (150 <= mouse_pos[0] <= 450) and (580 <= mouse_pos[1] <= 660):
					mode = "INF"
					game_start()

					
			elif result == "":
				if hint_count > 0 and (460 <= mouse_pos[0] <= 560 and 20 <= mouse_pos[1] <= 55):
					hint_count -= 1
					Hint()
				elif len(guess_word_string) < 5: 
					if (15 <= mouse_pos[0] <= 585) and (550 <= mouse_pos[1] <= 620):
						check_keyboard_click(mouse_pos[0], 0)	
					elif (44 <= mouse_pos[0] <= 556) and (635 <= mouse_pos[1] <= 705):
						check_keyboard_click(mouse_pos[0], 1)	
					elif (102 <= mouse_pos[0] <= 498) and (720 <= mouse_pos[1] <= 790):	
						check_keyboard_click(mouse_pos[0], 2)
				#############################################
				################## PHASE 2 ##################
				elif len(guess_word_string) == 5:
					if (15 <= mouse_pos[0] <= 90) and guess_word_string.lower() in words.WORDS:
						guess_check(guess_word)
				if (508 <= mouse_pos[0] <= 585) and (720 <= mouse_pos[1] <= 790):
					delete_letter()
				################## PHASE 2 ##################
				#############################################
	pygame.display.flip()


#Quit Code
pygame.quit()
