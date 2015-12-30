# Application : mouse click

# import module
import simpleguitk as simplegui
import math

# define globals
# default value of frame
FRAME_WIDTH = 450
FRAME_HEIGHT = 300
FRAME_COLOR = "White"
# default value of ball
DEFAULT_POSITION = [FRAME_WIDTH / 2, FRAME_HEIGHT / 2]
DEFAULT_RADIUS = 20
DEFAULT_LINE_WIDTH = 2
DEFAULT_LINE_COLOR = "Red"
DEFAULT_FILL_COLOR = "Red"
DEFAULT_CHANGE_COLOR_LIST = ["Green", "Yellow", "Blue", "Black", "Red"]


class Ball:
	pos = DEFAULT_POSITION		# ball's position
	radius = DEFAULT_RADIUS		# ball's radius
	line_width = DEFAULT_LINE_WIDTH		# ball's line width
	line_color = DEFAULT_LINE_COLOR		# ball's line color
	fill_color = DEFAULT_FILL_COLOR		# ball's filling color
	change_color_list = DEFAULT_CHANGE_COLOR_LIST	# the list color of ball once mouse click the circle
	catch_count = 0		# the click number that catch the circle, it will determine the color in the change_color_list

ball = Ball()

# define helper functions which consist of event handlers
# calculate the distance between pointer p and pointer q
def distance(p, q):
	return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

# define event handlers
# draw handler: draw a circle
def draw(canvas):
	canvas.draw_circle(ball.pos, ball.radius, ball.line_width, ball.line_color, ball.fill_color)

# mouse click handler: set the circle's position the same as the mouse's position
def click(pos):
	# the parameter: pos can not be changed
	if distance(pos, ball.pos) < ball.radius:
		ball.catch_count += 1
		ball.line_color = DEFAULT_CHANGE_COLOR_LIST[ball.catch_count % len(DEFAULT_CHANGE_COLOR_LIST)]
		ball.fill_color = ball.line_color
	else:
		# ball.pos = pos 	# ball.pos is a reference of pos
		ball.pos = list(pos)	# ball.pos is a copy of pos

# create frame
frame = simplegui.create_frame("Mouse Click", FRAME_WIDTH, FRAME_HEIGHT)

# register event handlers into frame
frame.set_canvas_background(FRAME_COLOR)
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)

# start frame
frame.start()
