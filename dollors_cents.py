"""
# string literals
s1 = "chensu's funny"
s2 = 'chensu"s funny'

# print s1
# print s2
# print s1 + s2

print s1[0]
print len(s1)

# [0th, 7th), just like [0th, 6th]
print s1[0:7]
print s1[:10]
s1 = "0123456789"
il = int(s1[:10])
print il + 1000000
"""

# import module
import simpleguitk as simplegui

# initialize globals
value = 3.12

# define helper functions which consist of event handlers
# handle single quantity
def convert_units(val, name):
    result = str(val) + " " + name
    if val > 1:
        result += "s"
    return result

# convert xx.yy to xx dollars and yy cents
def convert(val):
    # split into dollars and cents
    dollars = int(val)
    cents = int(round(100 * (val - dollars)))

    # convert to strings
    dollars_string = convert_units(dollars, "dollar")
    cents_string = convert_units(cents, "cent")

    # return composite string
    if dollars == 0 and cents == 0:
        return "broke!"
    elif dollars != 0 and cents == 0:
        return dollars_string
    elif dollars == 0 and cents != 0:
        return cents_string
    else:
        return dollars_string + " and " + cents_string;

# define event handlers
# define draw handler
def draw(canvas):
    canvas.draw_text(convert(value), [50, 100], 20, "White")

# define an input field handler
def input_handler(text):
    global value
    value = float(text)

# create frame
frame = simplegui.create_frame("Converter", 400, 200)

# register event handlers into frame
frame.set_draw_handler(draw)
frame.add_input("Input", input_handler, 100)

# start frame
frame.start()
