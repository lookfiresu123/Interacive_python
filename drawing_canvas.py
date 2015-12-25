# import module
import simpleguitk as simplegui

# define helper functions
# draw_text: draw_text("Title", position, font, color);
def draw(canvas):
    canvas.draw_text("Hello!", [100, 100], 24, "White")
    canvas.draw_circle([100, 100], 2, 2, "Red")

# define event handlers


# create frame
frame = simplegui.create_frame("Test", 300, 200)

# register event handlers into frame
frame.set_draw_handler(draw)

# start frame
frame.start()
