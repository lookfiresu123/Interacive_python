# Application of moving a ball, and you should try to attach the bomb

# import module
import simpleguitk as simplegui
import random
import math

# define globals
width = 500		# frame width
height = 500	# frame height
speed = 10		# the ball's default speed
current_key = ' '		# the default current key
rebound = False		# disable rebound for default
current_score = 0	# current score you get
required_score = 20		# required score that you have to get
score_per_green = 1		# score once you attach a green bomb
score_per_yellow = 2	# score once you attach a yellow bomb
score_per_blue = 3		# score once you attach a blue bomb

# define class
class Ball:
	pos = [width / 2, height / 2]		# the ball's current position in the frame
	radius = 20		# radius of ball
	line_width = 2		# line width of ball
	line_color = "Red"		# line color of ball
	fill_color = "White"	# filling color of ball
	# ball move left
	def move_left(self):
		if self.pos[0] > 0:
			self.pos[0] -= speed

	# ball move right
	def move_right(self):
		if self.pos[0] < width:
			self.pos[0] += speed

	# ball move up
	def move_up(self):
		if self.pos[1] > 0:
			self.pos[1] -= speed

	# ball move down
	def move_down(self):
		if self.pos[1] < height:
			self.pos[1] += speed

class Bomb_Green:
	pos = [0, 0]
	radius = 4
	line_width = 4
	line_color = "Green"
	fill_color = "Green"

class Bomb_Yellow:
	pos = [0, 0]
	radius = 3
	line_width = 3
	line_color = "Yellow"
	fill_color = "Yellow"

class Bomb_Blue:
	pos = [0, 0]
	radius = 2
	line_width = 2
	line_color = "Blue"
	fill_color = "Blue"

# define instance of class Ball and class Bomb
ball = Ball()

# define bomb list
bomb_green_list = Bomb_Green()
bomb_yellow_list = Bomb_Yellow()
bomb_blue_list = Bomb_Blue()

# define event handlers
# generate a bomb
def generate_bomb():
	global bomb_green_list, bomb_yellow_list, bomb_blue_list
	bomb_green_list.pos[0] = random.randrange(0, width)
	bomb_green_list.pos[1] = random.randrange(0, height)
	bomb_yellow_list.pos[0] = random.randrange(0, width)
	bomb_yellow_list.pos[1] = random.randrange(0, height)
	bomb_blue_list.pos[0] = random.randrange(0, width)
	bomb_blue_list.pos[1] = random.randrange(0, height)

# condition of catch bomb
def catch(ball, bomb):
	distance = (ball.pos[0] - bomb.pos[0]) ** 2 + (ball.pos[1] - bomb.pos[1]) ** 2
	limit = (ball.radius + bomb.radius) ** 2
	if distance <= limit:
		return True
	else:
		return False

# calculator the score
def get_score():
	global current_score
	if catch(ball, bomb_green_list) == True:
		current_score += score_per_green
	if catch(ball, bomb_yellow_list) == True:
		current_score += score_per_yellow
	if catch(ball, bomb_blue_list) == True:
		current_score += score_per_blue

# speed up the ball's movement
def speed_up():
	global speed
	speed += 1
	speed_label.set_text("speed = " + str(speed))

# speed down the ball's movement
def speed_down():
	global speed
	if speed > 0:
		speed -= 1
	speed_label.set_text("speed = " + str(speed))

# press the key "up" or "down" or "left" or "right" in the label
def keydown(key):
	global current_key
	current_key = key

# handler of timer
def time_handler_ball():
	global current_key
	if current_key == simplegui.KEY_MAP["left"]:
		if rebound == True and ball.pos[0] == 0:
			current_key = simplegui.KEY_MAP["right"]
			ball.move_right()
		else:
			ball.move_left()
	elif current_key == simplegui.KEY_MAP["right"]:
		if rebound == True and ball.pos[0] == width:
			current_key = simplegui.KEY_MAP["left"]
			ball.move_left()
		else:
			ball.move_right()
	elif current_key == simplegui.KEY_MAP["up"]:
		if rebound == True and ball.pos[1] == 0:
			current_key = simplegui.KEY_MAP["down"]
			ball.move_down()
		else:
			ball.move_up()
	elif current_key == simplegui.KEY_MAP["down"]:
		if rebound == True and ball.pos[1] == height:
			current_key = simplegui.KEY_MAP["up"]
			ball.move_up()
		else:
			ball.move_down()
	get_score()
	if current_score >= required_score:
		stop()

def time_handler_bomb():
	generate_bomb()

# reset: make the speed and ball's position default value
def reset():
	global speed, ball, bomb, rebound, score_string
	# stop()
	speed = 10
	ball.pos = [width / 2, height / 2]
	bomb_green_list.pos = [0, 0]
	bomb_yellow_list.pos = [0, 0]
	bomb_blue_list.pos = [0, 0]
	rebound = False
	rebound_label.set_text("rebound = " + str(rebound))
	current_score = 0
	score_string =  "0/" + str(required_score)
	# frame.set_draw_handler(draw)	# draws 50 times per second
	stop()

# start movement
def start():
	timer_ball.start()
	timer_bomb.start()

# stop movement
def stop():
	timer_ball.stop()
	timer_bomb.stop()

# change the set of current rebound
def set_rebound():
	global rebound
	if rebound == True:
		rebound = False
	else:
		rebound = True
	rebound_label.set_text("rebound = " + str(rebound))

# draw the frame
def draw(canvas):
	# global bomb_green_list, bomb_yellow_list, bomb_blue_list
	canvas.draw_circle(ball.pos, ball.radius, ball.line_width, ball.line_color, ball.fill_color)
	canvas.draw_circle(bomb_green_list.pos, bomb_green_list.radius, bomb_green_list.line_width, bomb_green_list.line_color, bomb_green_list.fill_color)
	canvas.draw_circle(bomb_yellow_list.pos, bomb_yellow_list.radius, bomb_yellow_list.line_width, bomb_yellow_list.line_color, bomb_yellow_list.fill_color)
	canvas.draw_circle(bomb_blue_list.pos, bomb_blue_list.radius, bomb_blue_list.line_width, bomb_blue_list.line_color, bomb_blue_list.fill_color)
	score_string = str(current_score) + "/" + str(required_score)
	canvas.draw_text(score_string, [400, 50], 20, "White")

# create frame
frame = simplegui.create_frame("Move Ball", width, height)
timer_ball = simplegui.create_timer(100, time_handler_ball)
timer_bomb = simplegui.create_timer(1000, time_handler_bomb)

# register event handlers into frame
frame.set_draw_handler(draw)	# draws 50 times per second
speed_label = frame.add_label("speed = " + str(speed))
frame.add_button("speed up", speed_up, 50)
frame.add_button("speed down", speed_down, 50)
frame.add_button("reset", reset, 50)
frame.add_button("start", start, 50)
frame.add_button("stop", stop, 50)
rebound_label = frame.add_label("rebound = " + str(rebound))
frame.add_button("rebound", set_rebound, 50)
frame.set_keydown_handler(keydown)

# start frame
frame.start()
