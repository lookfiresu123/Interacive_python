# Application : Control the speed of a ball's movement using keyboard
# click left twice and it will speed up, and then click right once it will speed down

# import module
import simpleguitk as simplegui

# define globals
current_speed = [0, 0]		# default speed
current_key = ' '	# default key
width = 500			# frame's width
height = 500		# frame's height

class Ball:
	pos = [width / 2, height / 2]
	radius = 20		# radius of ball
	line_width = 2		# line width of ball
	line_color = "Red"		# line color of ball
	fill_color = "White"	# filling color of ball

ball = Ball()
# define helper functions which consist of event handlers
# define rules of changing current speed
def change_speed():
	global current_speed
	accelerate_speed_rate = 5
	if current_key == simplegui.KEY_MAP["left"]:
		current_speed[0] -= accelerate_speed_rate
	elif current_key == simplegui.KEY_MAP["right"]:
		current_speed[0] += accelerate_speed_rate
	elif current_key == simplegui.KEY_MAP["up"]:
		current_speed[1] += accelerate_speed_rate
	elif current_key == simplegui.KEY_MAP["down"]:
		current_speed[1] -= accelerate_speed_rate


# define event handlers
def time_handler_ball():
	ball.pos[0] += current_speed[0]
	ball.pos[1] -= current_speed[1]		# because height is up to down, so use minus instead of add

def draw(canvas):
	canvas.draw_circle(ball.pos, ball.radius, ball.line_width, ball.line_color, ball.fill_color)

# press the key "up" or "down" or "left" or "right"
def keydown(key):
	global current_key
	current_key = key
	change_speed()	# update speed after apdating current_key

# according to start button
def start():
	timer_ball.start()	# start timer handler

# according to stop button
def stop():
	timer_ball.stop()	# stop tiemr handler

def reset():
	global current_key, current_speed
	ball.pos = [width / 2, height / 2]
	current_speed = 0
	current_key = ' '
	# stop()


# create frame
frame = simplegui.create_frame("Control Speed Keyboard", width, height)
timer_ball = simplegui.create_timer(100, time_handler_ball)

# register event handlers into frame
frame.set_keydown_handler(keydown)
frame.set_draw_handler(draw)
frame.add_button("start", start, 50)
frame.add_button("stop", stop, 50)
frame.add_button("reset", reset, 50)


# start frame
frame.start()
