# Application of move a ball

# import module
import simpleguitk as simplegui

# define globals
width = 600		# frame width
height = 400	# frame height
ball_pos = [width / 2, height / 2]		# the ball's current position in the frame
radius = 20		# radius of ball
line_width = 2		# line width of ball
line_color = "Red"		# line color of ball
fill_color = "White"	# filling color of ball
speed = 4		# the ball's default speed

# define helper function which consist of event handlers

# define event handlers
def keydown(key):
	if key == simplegui.KEY_MAP["left"]:
		ball_pos[0] -= speed
	elif key == simplegui.KEY_MAP["right"]:
		ball_pos[0] += speed
	elif key == simplegui.KEY_MAP["up"]:
		ball_pos[1] -= speed
	elif key == simplegui.KEY_MAP["down"]:
		ball_pos[1] += speed

def speed_up():
	global speed
	speed += 1
	speed_label.set_text("speed = " + str(speed))

def speed_down():
	global speed
	if speed > 0:
		speed -= 1
	speed_label.set_text("speed = " + str(speed))

def draw(canvas):
	canvas.draw_circle(ball_pos, radius, line_width, line_color, fill_color)

# create frame
frame = simplegui.create_frame("Move Ball", width, height)

# register event handlers into frame
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
speed_label = frame.add_label("speed = " + str(speed))
frame.add_button("speed up", speed_up, 50)
frame.add_button("speed down", speed_down, 50)

# start frame
frame.start()
