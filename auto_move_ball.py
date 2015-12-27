# Application of moving a ball, and you should try to attach the bomb

# import module
import simpleguitk as simplegui
import random
import math

# define globals
width = 300		# frame width
height = 300	# frame height
ball_pos = [width / 2, height / 2]		# the ball's current position in the frame
ball_radius = 20		# radius of ball
ball_line_width = 2		# line width of ball
ball_line_color = "Red"		# line color of ball
ball_fill_color = "White"	# filling color of ball

bomb_pos = [0, 0]		# the bomb's current position in the frame
bomb_radius = 2		# radius of bomb
bomb_line_width = 2		# line width of bomb
bomb_line_color = "Green"		# line color of bomb
bomb_fill_color = "Green"	# filling color of bomb

speed = 10		# the ball's default speed
current_key = ' '		# the default current key
rebound = False		# disable rebound for default

# define helper function which consist of event handlers
# ball move left
def move_left():
	if ball_pos[0] > 0:
		ball_pos[0] -= speed

# ball move right
def move_right():
	if ball_pos[0] < width:
		ball_pos[0] += speed

# ball move up
def move_up():
	if ball_pos[1] > 0:
		ball_pos[1] -= speed

# ball move down
def move_down():
	if ball_pos[1] < height:
		ball_pos[1] += speed

# generate a bomb
def generate_bomb():
	bomb_pos[0] = random.randrange(0, width)
	bomb_pos[1] = random.randrange(0, height)

# condition of catch bomb
def catch():
	distance = (ball_pos[0] - bomb_pos[0]) ** 2 + (ball_pos[1] - bomb_pos[1]) ** 2
	limit = (ball_radius + bomb_radius) ** 2
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
		if rebound == True and ball_pos[0] == 0:
			current_key = simplegui.KEY_MAP["right"]
			move_right()
		else:
			move_left()
	elif current_key == simplegui.KEY_MAP["right"]:
		if rebound == True and ball_pos[0] == width:
			current_key = simplegui.KEY_MAP["left"]
			move_left()
		else:
			move_right()
	elif current_key == simplegui.KEY_MAP["up"]:
		if rebound == True and ball_pos[1] == 0:
			current_key = simplegui.KEY_MAP["down"]
			move_down()
		else:
			move_up()
	elif current_key == simplegui.KEY_MAP["down"]:
		if rebound == True and ball_pos[1] == height:
			current_key = simplegui.KEY_MAP["up"]
			move_up()
		else:
			move_down()
	if catch() == True:
		stop()

def time_handler_bomb():
	generate_bomb()

# reset: make the speed and ball's position default value
def reset():
	global speed, ball_pos, bomb_pos, rebound
	speed = 10
	ball_pos = [width / 2, height / 2]
	bomb_pos = [0, 0]
	rebound = False

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
	canvas.draw_circle(ball_pos, ball_radius, ball_line_width, ball_line_color, ball_fill_color)
	canvas.draw_circle(bomb_pos, bomb_radius, bomb_line_width, bomb_line_color, bomb_fill_color)

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
