# Application of keyboard echo

# import module
import simpleguitk as simplegui

# define globals
current_key = ' '

# define helper function which consist of event handlers

# define event handlers
def keydown(key):
	global current_key
	current_key = chr(key)

def keyup(key):
	global current_key
	current_key = ' '

def draw(canvas):
	canvas.draw_text(current_key, [50, 100], 20, "Red")

# create frame
frame = simplegui.create_frame("Keyboard Echo", 200, 200)

# register event handlers into frame
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_draw_handler(draw)

# start frame
frame.start()
