# application of change the radius of circle

# import module
import simpleguitk as simplegui

# define globals
value = 10          # according to "Values" in the frame
radius = 10         # according to "Radius" in the frame

# define helper functions which consist of event handlers

# define event handlers
def increase_value_handlers():
    global value
    value += 1
    label_value.set_text("Values: " + str(value))

def decrease_value_handlers():
    global value
    if value > 0:
        value -= 1
        label_value.set_text("Values: " + str(value))

def change_circle_radius_handler():
    global radius
    radius = value
    label_radius.set_text("Radius: " + str(radius))

def draw(canvas):
    canvas.draw_circle([100,100], radius, 1, "Red")

# create frame
frame = simplegui.create_frame("Change Circle", 200, 200)

# register event handlers into frame
label_value = frame.add_label("Values: " + str(value))
frame.add_button("Increase", increase_value_handlers, 50)
frame.add_button("Decrease", decrease_value_handlers, 50)
label_radius = frame.add_label("Radius: " + str(value))
frame.add_button("Change circle", change_circle_radius_handler, 50)
frame.set_draw_handler(draw)


# start frame
frame.start()
