# Application : Calculator
# Data: Store, Operand
# Print, Swap, Add, Subtract, Multiple, Divide

# calculator layout
# left: Control area
# right: Canvas

# import modules
import simpleguitk as simplegui

# initalize globals
store = 0
operand = 0

# define functions that manipulate store and operand: a helper function
def output():
    print "Store = ", store
    print "Operand = ", operand
    print ""

# define a function that swap between store and operand: an event handler
def swap():
    global store, operand
    store, operand = operand, store
    output()

def add():
    global store, operand
    store += operand
    output()

def sub():
    global store, operand
    store -= operand
    output()

def mul():
    global store, operand
    store *= operand
    output()

def div():
    global store, operand
    store /= operand
    output()

def enter(input):
    global operand
    operand = float(input)
    output()

# create frame
frame = simplegui.create_frame("calculator", 300, 300)

# register events into frame
frame.add_button("Print", output, 100)
frame.add_button("Swap", swap, 100)
frame.add_button("Add", add, 100)
frame.add_button("Sub", sub, 100)
frame.add_button("Mul", mul, 100)
frame.add_button("Div", div, 100)
frame.add_input("Enter operand", enter, 100)

# start frame
frame.start()
