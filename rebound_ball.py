# Application : rebound ball given a start speed

# import module
import simpleguitk as simplegui

# define globals
width = 500		# width of frame
height = 500	# height of frame
current_speed_x = 0		# the current speed on the x line, right is position and left is negative
current_speed_y = 0		# the current speed on the y line, up is position and down is negative
# speed_string = "[ 0, 0 ]"	# default speed string
# pass_time = 0	# the passing time started from the program start
accelerate_speed_rate = -1	# accelerated speed

class Ball:
	pos = [width / 2, height / 2]	# the core position of this ball
	radius = 20		# radius of ball
	line_width = 2		# line width of ball
	line_color = "Red"		# line color of ball
	fill_color = "White"	# filling color of ball

	def move_rule(self):
		global current_speed_x, current_speed_y
		# rule_x = self.pos[0] <= self.radius or self.pos[0] >= (width - self.radius)
		# rule_y = self.pos[1] <= self.radius or self.pos[1] >= (height - self.radius)
		# if rule_x == True and rule_y == False:
		# 	current_speed_x = 0 - current_speed_x
		# elif rule_x == False and rule_y == True:
		# 	current_speed_y = 0 - current_speed_y
		# elif rule_x == True and rule_y == True:
		# 	current_speed_x = 0 - current_speed_x
		# 	current_speed_y = 0 - current_speed_y
		rule_x_left = self.pos[0] <= self.radius and current_speed_x < 0
		rule_x_right = self.pos[0] >= (width - self.radius) and current_speed_x > 0
		rule_y_up = self.pos[1] <= self.radius and current_speed_y > 0
		rule_y_down = self.pos[1] >= (width - self.radius) and current_speed_y < 0

		if (rule_x_left == True and ((rule_y_up == False and rule_y_down == False) == True)) or (rule_x_right == True and ((rule_y_up == False and rule_y_down == False) == True)):
			current_speed_x = 0 - current_speed_x
		elif (rule_y_up == True and ((rule_x_left == False and rule_x_right == False) == True)) or (rule_y_down == True and ((rule_x_left == False and rule_x_right == False) == True)):
			current_speed_y = 0 - current_speed_y
		elif (rule_x_left == True and rule_y_up == True) or (rule_x_left == True and rule_y_down == True) or (rule_x_right == True and rule_y_up == True) or (rule_x_right == True and rule_y_down == True):
			current_speed_x = 0 - current_speed_x
			current_speed_y = 0 - current_speed_y


ball = Ball()

# define helper function which consist of event handlers

# define event handlers
def get_initial_speed_x(value):
	global current_speed_x
	current_speed_x = int(value)

def get_initial_speed_y(value):
	global current_speed_y
	current_speed_y = int(value)

# situation: constant speed x
def formula_speed_x():
	global current_speed_x
	current_speed_x = current_speed_x * 1
	return current_speed_x

# situation: constant speed of y
def formula_speed_y():
	global current_speed_y
	current_speed_y += accelerate_speed_rate
	return current_speed_y

def formula_new_position(pos):
	pos[0] += formula_speed_x()
	pos[1] -= formula_speed_y()
	return pos

# draw the frame
def draw(canvas):
	# global bomb_green_list, bomb_yellow_list, bomb_blue_list
	canvas.draw_circle(ball.pos, ball.radius, ball.line_width, ball.line_color, ball.fill_color)
	# global speed_string
	# speed_string = "[ " + str(current_speed_x) + ", " + str(current_speed_y) + " ]"
	# canvas.draw_text(speed_string, [400, 50], 20, "White")

def time_handler_ball():
	global pass_time
	ball.move_rule()
	# pass_time += 1
	ball.pos = formula_new_position(ball.pos)

def reset():
	global current_speed_x, current_speed_y
	current_speed_x = current_speed_y = 0
	ball.pos = [width / 2, height / 2]


def start():
	timer_ball.start()

def stop():
	timer_ball.stop()

# create frame
frame = simplegui.create_frame("Rebound Ball", width, height)
timer_ball = simplegui.create_timer(100, time_handler_ball)		# implement time_handler_ball per 100ms

# register event handlers into frame
frame.set_draw_handler(draw)
frame.add_input("initial speed x : ", get_initial_speed_x, 50)
frame.add_input("initial speed y : ", get_initial_speed_y, 50)
frame.add_button("start", start, 50)
frame.add_button("stop", stop, 50)
frame.add_button("reset", reset, 50)

# start frame
frame.start()
