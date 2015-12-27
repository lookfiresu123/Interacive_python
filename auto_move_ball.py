# Application of moving a ball, and you should try to attach the bomb

# import module
import simpleguitk as simplegui
import random
import math

# define globals
width = 300		# frame width
height = 300	# frame height
speed = 10		# the ball's default speed
current_key = ' '		# the default current key
rebound = False		# disable rebound for default

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

class Bomb:
	pos = [0, 0]		# the bomb's current position in the frame
	radius = 2		# radius of bomb
	line_width = 2		# line width of bomb
	line_color = "Green"		# line color of bomb
	fill_color = "Green"	# filling color of bomb
	# generate a bomb
	def generate_bomb(self):
		self.pos[0] = random.randrange(0, width)
		self.pos[1] = random.randrange(0, height)


# define instance of class Ball and class Bomb
ball = Ball()
bomb = Bomb()

# define event handlers
# condition of catch bomb
def catch():
	distance = (ball.pos[0] - bomb.pos[0]) ** 2 + (ball.pos[1] - bomb.pos[1]) ** 2
	limit = (ball.radius + bomb.radius) ** 2
	if distance <= limit:
		return True
	else:
		return False

# define event handlers
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
	if catch() == True:
		stop()

def time_handler_bomb():
	bomb.generate_bomb()

# reset: make the speed and ball's position default value
def reset():
	global speed, ball, bomb, rebound
	stop()
	speed = 10
	ball.pos = [width / 2, height / 2]
	bomb.pos = [0, 0]
	rebound = False
	rebound_label.set_text("rebound = " + str(rebound))

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
	canvas.draw_circle(ball.pos, ball.radius, ball.line_width, ball.line_color, ball.fill_color)
	canvas.draw_circle(bomb.pos, bomb.radius, bomb.line_width, bomb.line_color, bomb.fill_color)

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
