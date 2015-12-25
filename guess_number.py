# Guess the number
# input will come from buttons and an input field
# all output for the game will be printed in the console

# import modules
import simpleguitk as simplegui
import math
import random

# initalize globals
num_range = 100
default_value = 0

# define helper functions which consist of event handlers
# output: print num_range and default_value
def output():
    print "num_range = ", num_range
    # print "default_value = ", default_value
    print ""

# define event handlers
# new_game: generate a new default_value
def new_game():
    global default_value
    if num_range == 100:
        default_value = random.randrange(0, 99)
    else:
        default_value = random.randrange(0, 999)
    # print default_value

# get_input: get a guess from input
def get_input(guess):
    global default_value
    if int(guess) < default_value:
        print "the correct should be higher"
    elif int(guess) > default_value:
        print "the correct should be lower"
    else:
        print "you get it"
    # print guess

# range_100: set the num_range frome0 to 99
def range_100():
    global num_range
    num_range = 100
    # output()

# range_1000: set the num_range from 0 to 999
def range_1000():
    global num_range
    num_range = 1000
    # output()

# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers into frame
frame.add_button("Range is [0, 100)", range_100, 200)
frame.add_button("Range is [0, 1000)", range_1000, 200)
frame.add_input("Enter a guess", get_input, 200)
frame.add_button("New game", new_game, 200);

# start frame
frame.start()
