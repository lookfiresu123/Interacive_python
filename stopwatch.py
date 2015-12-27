# template for "Stopwatch: The Game"

# import module
import simpleguitk as simplegui

# define globals
minute = 0
second = 0
min_second = 0
time_string = "0:00.0"

# define helper functions which consist of event handlers
def time_handler():
	global min_second
	global second
	global minute
	min_second += 1
	if min_second == 10:
		second += 1
		min_second = 0
	if second == 60:
		minute += 1
		second = 0

def time_format():
	global time_string
	time_string = ""
	time_string += str(minute) + ":"
	if second < 10:
		time_string += str(0) + str(second) + "."
	else:
		time_string += str(second) + "."
	time_string += str(min_second)

# define event handlers
def start_handler():
	timer.start()

def stop_handler():
	timer.stop()

def reset_handler():
	global min_second, minute, second, time_string
	min_second = minute = second = 0
	time_string = "0:00.0"

def draw(canvas):
	time_format()
	canvas.draw_text(time_string, [60, 120], 20, "White")

# create frame
frame = simplegui.create_frame("Stopwatch", 200, 200)
timer = simplegui.create_timer(100, time_handler)

# register event handlers into frame
frame.add_button("Start", start_handler, 50)
frame.add_button("Stop", stop_handler, 50)
frame.add_button("Reset", reset_handler, 50)
frame.set_draw_handler(draw)

# start frame
frame.start()
