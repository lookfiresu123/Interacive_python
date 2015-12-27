# simple "screensaver" program
# import module
import simpleguitk as simplegui
import random
from multiprocessing import Process

# initialize globals
message = "Python is Fun"       # content of message
position = [50, 50]             # position of message
width = 500                     # width of frame
height = 500                    # height of frame
interval = 2000                 # time interval: ms
font = 20
color = "White"

# define helper functions which consist of event handlers


# define event handlers
# handler for text box
def update_message(text):
    global message
    message = text

def update_font(text):
    global font
    font = int(text)

def update_color(text):
    global color
    color = text

# handler for timer
def tick():
    global position
    x = random.randrange(0, width)
    y = random.randrange(0, height)
    position[0] = x
    position[1] = y

# handler for draw position
def draw(canvas):
    canvas.draw_text(message, position, font, color)

# create frame and timer
frame = simplegui.create_frame("Screensaver", width, height)
timer = simplegui.create_timer(interval, tick)

# register event handlers into frame
frame.add_input("update message", update_message, 100)
frame.add_input("update font", update_font, 100)
frame.add_input("update color", update_color, 100)
frame.set_draw_handler(draw)

# start frame
timer.start()
frame.start()
