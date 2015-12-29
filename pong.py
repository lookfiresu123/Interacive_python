# Application : a simple pong game

# import module
import simpleguitk as simplegui
import random

# define globals
FRAME_WIDTH = 600		# frame's width
FRAME_HEIGHT = 400	# frame's height
PAD_WIDTH = 8		# pad's initial width
PAD_HEIGHT = 80		# pad's initial height
BALL_SPEED = [0, 0]		# ball's initial speed
left_score = 0		# the score that left player get during this game
right_score = 0		# the score that right player get during this game
# current_key = ' '	# current keyword that player press
PASS_LENGTH	= 20	# default passing length for either left pad or right pad

class Ball:
	pos = [FRAME_WIDTH / 2, FRAME_HEIGHT / 2]
	radius = 20		# radius of ball
	line_width = 1		# line width of ball
	line_color = "White"	# line color of ball
	fill_color = "White"	# filling color of ball
	speed = BALL_SPEED		# ball's initial speed

	def move_rule(self):
		rule_x_left = self.pos[0] <= self.radius and self.speed[0] < 0
		rule_x_right = self.pos[0] >= (FRAME_WIDTH - self.radius) and self.speed[0] > 0
		rule_y_up = self.pos[1] <= self.radius and self.speed[1] < 0
		rule_y_down = self.pos[1] >= (FRAME_HEIGHT - self.radius) and self.speed[1] > 0
		if (rule_x_left == True and ((rule_y_up == False and rule_y_down == False) == True)) or (rule_x_right == True and ((rule_y_up == False and rule_y_down == False) == True)):
			# print "old speed[0] = " + str(self.speed[0])
			self.speed[0] = 0 - self.speed[0]
			# print "new speed[0] = " + str(self.speed[0])
		elif (rule_y_up == True and ((rule_x_left == False and rule_x_right == False) == True)) or (rule_y_down == True and ((rule_x_left == False and rule_x_right == False) == True)):
			# print "old speed[1] = " + str(self.speed[1])
			self.speed[1] = 0 - self.speed[1]
			# print "new speed[1] = " + str(self.speed[1])
		elif (rule_x_left == True and rule_y_up == True) or (rule_x_left == True and rule_y_down == True) or (rule_x_right == True and rule_y_up == True) or (rule_x_right == True and rule_y_down == True):
			# print "old speed[0] = " + str(self.speed[0]) + ", old speed[1] = " + str(self.speed[1])
			self.speed[0] = 0 - self.speed[0]
			self.speed[1] = 0 - self.speed[1]
			# print "new speed[0] = " + str(self.speed[0]) + ", new speed[1] = " + str(self.speed[1])

class Pad_left:
	pad_width = PAD_WIDTH
	pad_height = PAD_HEIGHT
	pos = [pad_width / 2, FRAME_HEIGHT / 2]
	pass_length = PASS_LENGTH	# passing length if press w or s

class Pad_right:
	pad_width = PAD_WIDTH
	pad_height = PAD_HEIGHT
	pos = [FRAME_WIDTH - (pad_width / 2), FRAME_HEIGHT / 2]
	pass_length = PASS_LENGTH 	# passing length if press up or down

ball = Ball()
pad_left = Pad_left()
pad_right = Pad_right()


# define helper functions which consist of event handlers
# initialize ball's position and ball's speed for new bal in middle of table, and determine the initial direction
def spawn_ball():
	# use random to determine direction, 0 according to upper left, 1 according to upper right, 2 according to down left and 3 according to down right
	# in this game, positive of x is right, and positive of y is down
	ball.pos = [FRAME_WIDTH / 2, FRAME_HEIGHT / 2]
	pad_left.pos = [pad_left.pad_width / 2, FRAME_HEIGHT / 2]
	pad_right.pos = [FRAME_WIDTH - (pad_right.pad_width / 2), FRAME_HEIGHT / 2]
	choice = random.randrange(0, 3)
	start_speed_rate = 8
	if choice == 0:
		ball.speed = [0 - start_speed_rate, 0 - start_speed_rate]
	elif choice == 1:
		ball.speed = [start_speed_rate, 0 - start_speed_rate]
	elif choice == 2:
		ball.speed = [0 - start_speed_rate, start_speed_rate]
	elif choice == 3:
		ball.speed = [start_speed_rate, start_speed_rate]

# define event handlers
def restart():
	spawn_ball()

def keydown(key):
	# handle left pad or right pad
	if key == simplegui.KEY_MAP["w"]:
		pad_left.pos[1] -= pad_left.pass_length
	elif key == simplegui.KEY_MAP["s"]:
		pad_left.pos[1] += pad_left.pass_length
	elif key == simplegui.KEY_MAP["up"]:
		pad_right.pos[1] -= pad_right.pass_length
	elif key == simplegui.KEY_MAP["down"]:
		pad_right.pos[1] += pad_right.pass_length

def time_handler():
	# handle ball
	ball.move_rule()
	ball.pos[0] += ball.speed[0]
	ball.pos[1] += ball.speed[1]

def start():
	timer.start()
	spawn_ball()

def stop():
	timer.stop()

def draw(canvas):
	canvas.draw_line([pad_left.pad_width, 0], [pad_left.pad_width, FRAME_HEIGHT], 1, "White")		# draw left line
	canvas.draw_line([FRAME_WIDTH - pad_right.pad_width, 0], [FRAME_WIDTH - pad_right.pad_width, FRAME_HEIGHT], 1, "White")	# draw right line
	canvas.draw_line([FRAME_WIDTH / 2, 0], [FRAME_WIDTH / 2, FRAME_HEIGHT], 1, "White")		# draw middle line
	# draw pad_left
	pad_left_upper_left = [pad_left.pos[0] - (pad_left.pad_width / 2), pad_left.pos[1] - (pad_left.pad_height / 2)]
	pad_left_upper_right = [pad_left.pos[0] + (pad_left.pad_width / 2), pad_left.pos[1] - (pad_left.pad_height / 2)]
	pad_left_down_left = [pad_left.pos[0] - (pad_left.pad_width / 2), pad_left.pos[1] + (pad_left.pad_height / 2)]
	pad_left_down_right = [pad_left.pos[0] + (pad_left.pad_width / 2), pad_left.pos[1] + (pad_left.pad_height / 2)]
	canvas.draw_polygon([pad_left_upper_left, pad_left_upper_right, pad_left_down_right, pad_left_down_left], 0, "White", "White")
	# draw pad_right
	pad_right_upper_left = [pad_right.pos[0] - (pad_right.pad_width / 2), pad_right.pos[1] - (pad_right.pad_height / 2)]
	pad_right_upper_right = [pad_right.pos[0] + (pad_right.pad_width / 2), pad_right.pos[1] - (pad_right.pad_height / 2)]
	pad_right_down_left = [pad_right.pos[0] - (pad_right.pad_width / 2), pad_right.pos[1] + (pad_right.pad_height / 2)]
	pad_right_down_right = [pad_right.pos[0] + (pad_right.pad_width / 2), pad_right.pos[1] + (pad_right.pad_height / 2)]
	canvas.draw_polygon([pad_right_upper_left, pad_right_upper_right, pad_right_down_right, pad_right_down_left], 0, "White", "White")
	# draw ball
	canvas.draw_circle(ball.pos, ball.radius, ball.line_width, ball.line_color, ball.fill_color)
	canvas.draw_text(str(left_score), [250, 50], 30, "Red")
	canvas.draw_text(str(right_score), [320, 50], 30, "Red")

# create frame
frame = simplegui.create_frame("Pong Game", FRAME_WIDTH, FRAME_HEIGHT)
timer = simplegui.create_timer(100, time_handler)

# register event handlers into frame
frame.add_button("Restart", restart, 50)
frame.set_draw_handler(draw)
frame.add_button("Strat", start, 50)
frame.add_button("Stop", stop, 50)
frame.set_keydown_handler(keydown)

# frame start
frame.start()
